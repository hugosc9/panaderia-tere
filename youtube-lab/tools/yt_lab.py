#!/usr/bin/env python3
"""
yt_lab.py - Radiografia de canales de YouTube para investigacion competitiva.

Sin dependencias externas (solo stdlib). Usa la YouTube Data API v3.

Uso:
    export YOUTUBE_API_KEY="AIza..."

    # Descargar + analizar un canal entero
    python3 yt_lab.py channel @exitoocultoyt

    # Comparar varios canales
    python3 yt_lab.py compare @MagnatesMedia @CompanyMan @ModernMBA

    # Reanalizar un volcado ya descargado (0 cuota)
    python3 yt_lab.py channel --from-json ../data/raw/exitoocultoyt_2026-09-20.json

Coste de cuota (limite diario gratuito: 10.000 unidades):
    channels.list        1 unidad
    playlistItems.list   1 unidad por cada 50 videos
    videos.list          1 unidad por cada 50 videos
    => un canal de 300 videos cuesta ~13 unidades. NO se usa search.list (100 u.).
"""

import argparse
import csv
import json
import os
import re
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_ROOT = "https://www.googleapis.com/youtube/v3/"
SHORTS_MAX_SECONDS = 60
DEFAULT_COHORT_WINDOW_DAYS = 120


# --------------------------------------------------------------------------
# Capa API
# --------------------------------------------------------------------------

def api_get(endpoint, params, key):
    params = dict(params)
    params["key"] = key
    url = API_ROOT + endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        raise SystemExit(
            "Error HTTP %s en %s\n%s\n\n"
            "403 suele ser cuota agotada o API no habilitada.\n"
            "404 suele ser un handle/ID que no existe." % (exc.code, endpoint, body)
        )


def resolve_channel(ref, key):
    """Devuelve el recurso channel a partir de @handle, UC... o nombre."""
    part = "snippet,statistics,contentDetails"
    if ref.startswith("UC") and len(ref) == 24:
        data = api_get("channels", {"part": part, "id": ref}, key)
    elif ref.startswith("@"):
        data = api_get("channels", {"part": part, "forHandle": ref}, key)
    else:
        data = api_get("channels", {"part": part, "forHandle": "@" + ref}, key)

    items = data.get("items") or []
    if not items:
        raise SystemExit(
            "No se encontro el canal '%s'.\n"
            "Prueba con el handle exacto (@algo) o con el ID (UC...)." % ref
        )
    return items[0]


def fetch_all_videos(uploads_playlist_id, key, limit=None):
    """Descarga metadatos completos de todos los videos subidos por el canal."""
    video_ids = []
    page_token = None
    while True:
        params = {
            "part": "contentDetails",
            "playlistId": uploads_playlist_id,
            "maxResults": 50,
        }
        if page_token:
            params["pageToken"] = page_token
        data = api_get("playlistItems", params, key)
        for item in data.get("items", []):
            vid = item["contentDetails"].get("videoId")
            if vid:
                video_ids.append(vid)
        if limit and len(video_ids) >= limit:
            video_ids = video_ids[:limit]
            break
        page_token = data.get("nextPageToken")
        if not page_token:
            break

    videos = []
    for i in range(0, len(video_ids), 50):
        chunk = video_ids[i:i + 50]
        data = api_get(
            "videos",
            {"part": "snippet,contentDetails,statistics", "id": ",".join(chunk)},
            key,
        )
        videos.extend(data.get("items", []))
    return videos


# --------------------------------------------------------------------------
# Normalizacion
# --------------------------------------------------------------------------

DURATION_RE = re.compile(
    r"P(?:(?P<d>\d+)D)?T(?:(?P<h>\d+)H)?(?:(?P<m>\d+)M)?(?:(?P<s>\d+)S)?"
)


def parse_duration(iso):
    m = DURATION_RE.match(iso or "")
    if not m:
        return 0
    g = {k: int(v) if v else 0 for k, v in m.groupdict().items()}
    return g["d"] * 86400 + g["h"] * 3600 + g["m"] * 60 + g["s"]


def parse_date(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def normalize(videos, now=None):
    now = now or datetime.now(timezone.utc)
    rows = []
    for v in videos:
        snip = v.get("snippet", {})
        stats = v.get("statistics", {})
        published = parse_date(snip["publishedAt"])
        age_days = max((now - published).total_seconds() / 86400.0, 0.5)
        seconds = parse_duration(v.get("contentDetails", {}).get("duration"))
        views = int(stats.get("viewCount", 0) or 0)
        rows.append({
            "id": v["id"],
            "title": snip.get("title", ""),
            "published": published,
            "published_str": published.strftime("%Y-%m-%d"),
            "age_days": round(age_days, 1),
            "seconds": seconds,
            "duration": "%d:%02d" % (seconds // 60, seconds % 60),
            "views": views,
            # likeCount/commentCount pueden venir ocultos por el creador
            "likes": int(stats["likeCount"]) if "likeCount" in stats else None,
            "comments": int(stats["commentCount"]) if "commentCount" in stats else None,
            "vpd": views / age_days,
            "is_short": seconds <= SHORTS_MAX_SECONDS,
            "description": snip.get("description", ""),
            "tags": snip.get("tags", []),
            "thumb": (snip.get("thumbnails", {}).get("maxres")
                      or snip.get("thumbnails", {}).get("high")
                      or {}).get("url", ""),
        })
    rows.sort(key=lambda r: r["published"], reverse=True)
    return rows


# --------------------------------------------------------------------------
# Deteccion de outliers
# --------------------------------------------------------------------------

def add_outlier_scores(rows, window_days=DEFAULT_COHORT_WINDOW_DAYS):
    """
    Un outlier NO es 'el video con mas visitas'. Es el video que rinde muy por
    encima de lo que rendian sus vecinos temporales del mismo formato.

    Para cada video se construye una cohorte: videos del mismo formato
    (long-form vs short) publicados dentro de +/- window_days, excluido el
    propio video. Se compara contra la MEDIANA de esa cohorte, en dos ejes:

      views_multiple : visitas / mediana de visitas de la cohorte
      vpd_multiple   : visitas-por-dia / mediana de vpd de la cohorte

    views_multiple mide el resultado acumulado; vpd_multiple corrige por
    antiguedad y detecta antes los videos jovenes que estan despegando.
    El score final usa el menor de los dos para evitar falsos positivos de
    videos con 3 dias de vida.
    """
    for row in rows:
        same_format = [
            o for o in rows
            if o["is_short"] == row["is_short"] and o["id"] != row["id"]
        ]
        cohort = [
            o for o in same_format
            if abs((o["published"] - row["published"]).days) <= window_days
        ]
        if len(cohort) < 5:
            cohort = same_format
        if not cohort:
            row["views_multiple"] = None
            row["vpd_multiple"] = None
            row["outlier_score"] = None
            row["cohort_size"] = 0
            continue

        med_views = statistics.median(o["views"] for o in cohort) or 1
        med_vpd = statistics.median(o["vpd"] for o in cohort) or 1e-9
        row["views_multiple"] = row["views"] / med_views
        row["vpd_multiple"] = row["vpd"] / med_vpd
        row["outlier_score"] = min(row["views_multiple"], row["vpd_multiple"])
        row["cohort_size"] = len(cohort)
    return rows


def label(score):
    if score is None:
        return "sin datos"
    if score >= 5:
        return "OUTLIER EXTREMO"
    if score >= 3:
        return "OUTLIER FUERTE"
    if score >= 2:
        return "outlier"
    if score <= 0.4:
        return "bajo rendimiento"
    return "normal"


# --------------------------------------------------------------------------
# Patrones de titulo
# --------------------------------------------------------------------------

TITLE_PATTERNS = {
    "numero": r"\b\d{1,4}([.,]\d{3})*\b|\b\d+%",
    "dinero": r"[$€£]|\b(millones?|millardos?|mil millones|billones?|dolares|euros|"
              r"million|billion|dinero|money|fortuna|facturacion|ingresos)\b",
    "pregunta": r"^\s*[¿?]|\?\s*$|\b(por que|porque|como es que|why|how come)\b",
    "como": r"\bcomo\b|\bhow\b",
    "por_que": r"\bpor que\b|\bwhy\b",
    "secreto_oculto": r"\b(secreto|secretos|oculto|oculta|nadie|nunca te|no quiere|"
                      r"prohibido|verdad|realidad|detras)\b",
    "fracaso_caida": r"\b(fracaso|fracaso[oó]|quebr[oó]|quiebra|arruin[oó]|ruina|caida|cay[oó]|"
                     r"perdio|colapso|desastre|error|hundio|murio|desaparecio)\b",
    "exito_ascenso": r"\b(exito|imperio|conquisto|domina|domino|gigante|lider|"
                     r"revoluciono|construyo|creo)\b",
    "la_empresa_que": r"\bla (empresa|marca|compania|startup|tienda|firma) que\b|"
                      r"\bel (negocio|hombre|tipo|fundador) que\b",
    "superlativo": r"\b(mas|mayor|peor|mejor|unico|jamas|nunca|historia|todos los "
                   r"tiempos|increible|absurdo|loco|brutal)\b",
    "contradiccion": r"\b(pero|aunque|sin embargo|y aun asi|y sin embargo|gana dinero "
                     r"sin|gratis|pierde dinero|no vende)\b",
    "mayusculas_enfasis": r"\b[A-Z]{3,}\b",
    "temporal": r"\b(20\d\d|en \d+ (dias|meses|anos)|de la noche a la manana)\b",
}

_ACCENTS = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN")


def tag_title(title):
    plain = title.translate(_ACCENTS)
    found = []
    for name, pattern in TITLE_PATTERNS.items():
        flags = 0 if name == "mayusculas_enfasis" else re.IGNORECASE
        if re.search(pattern, plain, flags):
            found.append(name)
    return found


def pattern_performance(rows):
    """Cruza cada patron de titulo con el rendimiento real. Esto es lo que
    convierte 'estos patrones suelen funcionar' en 'en ESTE canal funcionan'."""
    scored = [r for r in rows if r.get("outlier_score") is not None and not r["is_short"]]
    out = []
    for name in TITLE_PATTERNS:
        with_p = [r["outlier_score"] for r in scored if name in r["patterns"]]
        without = [r["outlier_score"] for r in scored if name not in r["patterns"]]
        if len(with_p) < 3 or len(without) < 3:
            continue
        med_with = statistics.median(with_p)
        med_without = statistics.median(without)
        out.append({
            "patron": name,
            "n_videos": len(with_p),
            "mediana_con": med_with,
            "mediana_sin": med_without,
            "lift": med_with / med_without if med_without else float("nan"),
        })
    out.sort(key=lambda d: d["lift"], reverse=True)
    return out


# --------------------------------------------------------------------------
# Informe
# --------------------------------------------------------------------------

def fmt(n):
    if n is None:
        return "n/d"
    return "{:,}".format(int(n)).replace(",", ".")


def quarter(dt):
    return "%d-Q%d" % (dt.year, (dt.month - 1) // 3 + 1)


def build_report(channel, rows, window_days):
    snip = channel["snippet"]
    stats = channel["statistics"]
    longform = [r for r in rows if not r["is_short"]]
    shorts = [r for r in rows if r["is_short"]]
    now = datetime.now(timezone.utc)

    L = []
    L.append("# Radiografia: %s" % snip.get("title", "?"))
    L.append("")
    L.append("Generado: %s  |  Fuente: YouTube Data API v3 (datos observados, no estimados)"
             % now.strftime("%Y-%m-%d %H:%M UTC"))
    L.append("")
    L.append("## 1. Identidad")
    L.append("")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append("| Handle | %s |" % snip.get("customUrl", "n/d"))
    L.append("| ID | %s |" % channel["id"])
    L.append("| Creado | %s |" % parse_date(snip["publishedAt"]).strftime("%Y-%m-%d"))
    L.append("| Pais | %s |" % snip.get("country", "no declarado"))
    L.append("| Idioma por defecto | %s |" % snip.get("defaultLanguage", "no declarado"))
    L.append("| Suscriptores | %s%s |" % (
        fmt(stats.get("subscriberCount")),
        " (ocultos)" if stats.get("hiddenSubscriberCount") else ""))
    L.append("| Visitas totales | %s |" % fmt(stats.get("viewCount")))
    L.append("| Videos publicados | %s |" % fmt(stats.get("videoCount")))
    L.append("| Videos analizados | %d (%d long-form, %d shorts) |"
             % (len(rows), len(longform), len(shorts)))
    L.append("")
    desc = (snip.get("description") or "").strip()
    if desc:
        L.append("**Descripcion del canal:**")
        L.append("")
        L.append("> " + desc.replace("\n", "\n> "))
        L.append("")

    if longform:
        views = [r["views"] for r in longform]
        secs = [r["seconds"] for r in longform]
        L.append("## 2. Numeros base (solo long-form)")
        L.append("")
        L.append("| Metrica | Valor |")
        L.append("|---|---|")
        L.append("| Mediana de visitas | %s |" % fmt(statistics.median(views)))
        L.append("| Media de visitas | %s |" % fmt(statistics.mean(views)))
        L.append("| Maximo | %s |" % fmt(max(views)))
        L.append("| Minimo | %s |" % fmt(min(views)))
        L.append("| Duracion mediana | %d:%02d |"
                 % (statistics.median(secs) // 60, statistics.median(secs) % 60))
        ratio = max(views) / statistics.median(views) if statistics.median(views) else 0
        L.append("| Ratio max/mediana | %.1fx |" % ratio)
        L.append("")
        L.append("_Un ratio max/mediana alto (>8x) indica un canal donde unos pocos "
                 "videos cargan con casi todo el trafico: el formato tiene techo alto "
                 "pero poca consistencia._")
        L.append("")

    # Cadencia
    L.append("## 3. Cadencia y evolucion (por trimestre)")
    L.append("")
    L.append("| Trimestre | Videos | Mediana visitas | Duracion mediana |")
    L.append("|---|---|---|---|")
    by_q = {}
    for r in longform:
        by_q.setdefault(quarter(r["published"]), []).append(r)
    for q in sorted(by_q, reverse=True):
        group = by_q[q]
        mv = statistics.median(r["views"] for r in group)
        ms = statistics.median(r["seconds"] for r in group)
        L.append("| %s | %d | %s | %d:%02d |" % (q, len(group), fmt(mv), ms // 60, ms % 60))
    L.append("")

    # Outliers
    L.append("## 4. Outliers (ventana de cohorte: +/- %d dias)" % window_days)
    L.append("")
    L.append("Score = min(visitas/mediana cohorte, vpd/mediana vpd cohorte).")
    L.append("")
    L.append("| Score | Etiqueta | Fecha | Dur. | Visitas | V/dia | Likes | Coment. | Titulo |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    ranked = sorted(
        [r for r in longform if r.get("outlier_score") is not None],
        key=lambda r: r["outlier_score"], reverse=True)
    for r in ranked[:20]:
        L.append("| %.2fx | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["outlier_score"], label(r["outlier_score"]), r["published_str"],
            r["duration"], fmt(r["views"]), fmt(r["vpd"]),
            fmt(r["likes"]), fmt(r["comments"]), r["title"].replace("|", "/")))
    L.append("")

    if len(ranked) > 20:
        L.append("### Peores rendimientos (para saber que NO repetir)")
        L.append("")
        L.append("| Score | Fecha | Visitas | Titulo |")
        L.append("|---|---|---|---|")
        for r in ranked[-8:]:
            L.append("| %.2fx | %s | %s | %s |" % (
                r["outlier_score"], r["published_str"], fmt(r["views"]),
                r["title"].replace("|", "/")))
        L.append("")

    # Patrones
    perf = pattern_performance(rows)
    L.append("## 5. Patrones de titulo vs rendimiento REAL de este canal")
    L.append("")
    if perf:
        L.append("| Patron | Videos | Mediana score CON | Mediana score SIN | Lift |")
        L.append("|---|---|---|---|---|")
        for p in perf:
            L.append("| %s | %d | %.2fx | %.2fx | **%.2fx** |" % (
                p["patron"], p["n_videos"], p["mediana_con"],
                p["mediana_sin"], p["lift"]))
        L.append("")
        L.append("_Lift > 1.3 con n >= 8 videos empieza a ser una senal real. "
                 "Lift cercano a 1.0 significa que ese patron no explica nada en "
                 "este canal, aunque sea un consejo habitual de YouTube._")
    else:
        L.append("_Muestra insuficiente para cruzar patrones (hacen falta >= 3 videos "
                 "con y sin cada patron)._")
    L.append("")

    # Duracion vs rendimiento
    L.append("## 6. Duracion vs rendimiento")
    L.append("")
    buckets = [(0, 300, "< 5 min"), (300, 480, "5-8 min"), (480, 720, "8-12 min"),
               (720, 1080, "12-18 min"), (1080, 10 ** 9, "> 18 min")]
    L.append("| Rango | Videos | Mediana visitas | Mediana score |")
    L.append("|---|---|---|---|")
    for lo, hi, name in buckets:
        group = [r for r in longform if lo <= r["seconds"] < hi
                 and r.get("outlier_score") is not None]
        if not group:
            continue
        L.append("| %s | %d | %s | %.2fx |" % (
            name, len(group), fmt(statistics.median(r["views"] for r in group)),
            statistics.median(r["outlier_score"] for r in group)))
    L.append("")

    L.append("## 7. Que NO da esta API")
    L.append("")
    L.append("- Retencion, CTR, impresiones y fuentes de trafico: solo visibles para "
             "el dueno del canal (YouTube Analytics API). De un canal ajeno no se "
             "pueden obtener. Cualquier cifra de CTR sobre un canal ajeno es inventada.")
    L.append("- Likes/comentarios pueden aparecer como `n/d` si el creador los oculta.")
    L.append("- Thumbnails: las URLs estan en el CSV. El analisis visual hay que "
             "hacerlo mirandolas (o pasandolas a un modelo con vision).")
    L.append("- Estructura narrativa y produccion: requieren ver los videos. Descarga "
             "las transcripciones aparte y analizalas.")
    L.append("")
    return "\n".join(L)


def write_csv(path, rows):
    cols = ["id", "published_str", "title", "duration", "seconds", "views", "vpd",
            "likes", "comments", "views_multiple", "vpd_multiple", "outlier_score",
            "cohort_size", "is_short", "patterns_str", "thumb"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            r = dict(r)
            r["patterns_str"] = "|".join(r.get("patterns", []))
            w.writerow(r)


# --------------------------------------------------------------------------
# Comandos
# --------------------------------------------------------------------------

def load_or_fetch(args, key):
    if args.from_json:
        with open(args.from_json, encoding="utf-8") as fh:
            dump = json.load(fh)
        return dump["channel"], dump["videos"], args.from_json

    channel = resolve_channel(args.channel, key)
    uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    videos = fetch_all_videos(uploads, key, args.limit)
    handle = (channel["snippet"].get("customUrl") or channel["id"]).lstrip("@")
    out = os.path.join(args.outdir, "%s_%s.json" % (
        re.sub(r"[^\w-]", "", handle), datetime.now().strftime("%Y-%m-%d")))
    os.makedirs(args.outdir, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"fetched_at": datetime.now(timezone.utc).isoformat(),
                   "channel": channel, "videos": videos}, fh, ensure_ascii=False)
    print("Volcado crudo -> %s" % out, file=sys.stderr)
    return channel, videos, out


def cmd_channel(args, key):
    channel, videos, src = load_or_fetch(args, key)
    rows = normalize(videos)
    if not rows:
        raise SystemExit("El canal no tiene videos publicos.")
    add_outlier_scores(rows, args.window)
    for r in rows:
        r["patterns"] = tag_title(r["title"])

    report = build_report(channel, rows, args.window)
    base = os.path.splitext(src)[0]
    md_path = base + "_informe.md"
    csv_path = base + "_videos.csv"
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(report)
    write_csv(csv_path, rows)
    print(report)
    print("\n---\nInforme -> %s\nCSV     -> %s" % (md_path, csv_path), file=sys.stderr)


def cmd_compare(args, key):
    print("| Canal | Subs | Videos | Visitas totales | Mediana visitas | "
          "Max/mediana | Dur. mediana | Videos/mes (12m) |")
    print("|---|---|---|---|---|---|---|---|")
    now = datetime.now(timezone.utc)
    for ref in args.channels:
        channel = resolve_channel(ref, key)
        uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]
        videos = fetch_all_videos(uploads, key, args.limit)
        rows = [r for r in normalize(videos) if not r["is_short"]]
        if not rows:
            continue
        views = [r["views"] for r in rows]
        med = statistics.median(views)
        secs = statistics.median(r["seconds"] for r in rows)
        recent = [r for r in rows if (now - r["published"]).days <= 365]
        print("| %s | %s | %s | %s | %s | %.1fx | %d:%02d | %.1f |" % (
            channel["snippet"]["title"],
            fmt(channel["statistics"].get("subscriberCount")),
            fmt(channel["statistics"].get("videoCount")),
            fmt(channel["statistics"].get("viewCount")),
            fmt(med), (max(views) / med if med else 0),
            secs // 60, secs % 60, len(recent) / 12.0))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("channel", help="radiografia completa de un canal")
    c.add_argument("channel", nargs="?", help="@handle o UC...")
    c.add_argument("--from-json", help="reanalizar un volcado ya descargado (0 cuota)")
    c.add_argument("--limit", type=int, help="maximo de videos a descargar")
    c.add_argument("--window", type=int, default=DEFAULT_COHORT_WINDOW_DAYS,
                   help="ventana de cohorte en dias (def. 120)")
    c.add_argument("--outdir", default=os.path.join(os.path.dirname(__file__),
                                                    "..", "data", "raw"))
    c.set_defaults(func=cmd_channel)

    m = sub.add_parser("compare", help="tabla comparativa de varios canales")
    m.add_argument("channels", nargs="+")
    m.add_argument("--limit", type=int, default=200)
    m.set_defaults(func=cmd_compare)

    args = p.parse_args()
    key = os.environ.get("YOUTUBE_API_KEY", "")
    needs_key = not getattr(args, "from_json", None)
    if needs_key and not key:
        raise SystemExit(
            "Falta YOUTUBE_API_KEY.\n"
            "Consiguela gratis en https://console.cloud.google.com -> crear proyecto\n"
            "-> habilitar 'YouTube Data API v3' -> Credenciales -> Clave de API.\n"
            "Despues:  export YOUTUBE_API_KEY=\"AIza...\"")
    if getattr(args, "cmd", None) == "channel" and not args.channel and not args.from_json:
        raise SystemExit("Indica un canal (@handle) o usa --from-json.")
    args.func(args, key)


if __name__ == "__main__":
    main()
