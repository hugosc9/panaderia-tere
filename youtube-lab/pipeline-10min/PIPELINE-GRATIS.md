# Pipeline de coste cero para vídeos de 10 minutos

Diseñado para lo que ya tienes: **Google AI Plus** (4,99 €/mes, ya pagado) + **Claude** (esta sesión) + herramientas open-source locales. Ningún paso de aquí abajo tiene coste marginal adicional. Todo lo ejecutas en **tu ordenador**, no en este sandbox (este entorno es efímero y es el repo de la panadería — aquí solo vive la documentación).

> ⚠️ **Corrección:** la primera versión de este documento asumía el plan Google AI Pro (19,99 $/mes). El usuario tiene **AI Plus** (4,99 €/mes), un escalón por debajo, con muchos menos créditos. Los números de abajo ya están corregidos, pero **verifica tú mismo tu saldo real de créditos** en la app de Gemini/Flow antes de planificar un vídeo — los precios y cuotas de estos planes cambian con frecuencia y las fuentes secundarias no siempre coinciden entre sí. **[SECUNDARIO]**

---

## 0. Lo que ya tienes y lo que vale cada cosa

| Recurso | Ya lo pagas / es gratis | Para qué |
|---|---|---|
| **Google AI Plus** — Gemini 3 Pro | Ya pagado (4,99 €/mes) | Investigación, guion de apoyo |
| **Google AI Plus** — Flow / Veo 3.1 Fast | Ya pagado — **~200 créditos/mes** [SECUNDARIO, verificar saldo real en la app] | Un puñado de planos de alto impacto, no todos — ver §4, cálculo revisado |
| **Google AI Plus** — Whisk (imagen) | Ya pagado, mismos créditos | Miniatura + imágenes fijas para gráficos |
| **NotebookLM** (Gemini Notebook) | Incluido en Plus, con límites más bajos que Pro/Ultra | **Investigación con citas verificables** — ver §1, mejor que Deep Research para esto |
| **Claude** (esta sesión / claude.ai) | Ya lo tienes | Guion, estructura narrativa, control de calidad, prompts de Veo |
| **edge-tts** (Python, open-source) | Gratis, sin límite, sin clave | Voz en off — ver §3 |
| **Remotion** (Node/React, open-source) | Gratis (licencia de empresa solo si facturas >100k$/año como compañía, no aplica a un creador individual) | Montaje programático, subtítulos, gráficos animados — **hace la mayor parte del vídeo**, no Veo |
| **Pexels API** | Gratis, sin límite práctico | B-roll genérico (oficinas, ciudad, manos) |
| **FFmpeg** | Gratis, open-source | Pegamento: mezclar audio, normalizar, exportar |
| **YouTube Data API v3** | Gratis, 10.000 unidades/día | Subir el vídeo por API en vez de manual |

**Coste real de un vídeo de 10 min con este pipeline: 0 €.** Con AI Plus, los créditos de Veo son escasos (§4) — el peso real del vídeo lo lleva Remotion + Pexels + archivo real, y Veo se reserva para 3-5 planos verdaderamente clave, no para 15-20 como en el plan Pro.

---

## 1. Investigación — NotebookLM como motor principal, Deep Research como descubrimiento

Dos herramientas, dos papeles distintos. No son intercambiables:

**Deep Research (Gemini)** rastrea la web abierta y te trae un resumen — rápido, amplio, pero es más difícil verificar de dónde sale cada frase exacta.

**NotebookLM (incluido en tu Plus) es mejor para lo que de verdad pide `02-research-brief.md`: una tabla de hechos con cita exacta.** Funciona por RAG estrictamente sobre lo que tú subes — cada respuesta cita el párrafo concreto del documento del que sale, no la web en general. Es la herramienta correcta para esta etapa, no un sustituto de peor calidad de Deep Research.

**Flujo recomendado:**
1. **Descubrimiento (Deep Research):** una pasada rápida para localizar qué fuentes existen — cuentas anuales, artículos de hemeroteca, informes de la CNMV, comunicados.
2. **Recopilación (tú):** descarga esas fuentes primarias — PDFs de cuentas anuales, capturas de hemeroteca, informes. Esto sigue siendo tuyo, es el requisito de autenticidad de §6D del informe general, y ninguna IA lo sustituye.
3. **Extracción grounded (NotebookLM):** crea un notebook, sube esas fuentes primarias (no enlaces sueltos, los documentos en sí), y pide la tabla de hechos con cita — página y frase exacta de origen. Esto te da la tabla de `02-research-brief.md` con trazabilidad real, verificable clicando cada cita.
4. NotebookLM en Plus tiene límites más bajos que en Pro/Ultra (fuentes por notebook, consultas/día) — si topas con el límite en un tema con muchas fuentes, prioriza las 10-15 más relevantes en vez de subir todo.

**Sobre "Video Overview" de NotebookLM — no lo uses como el vídeo final:** NotebookLM puede generar un vídeo narrado automáticamente a partir de las fuentes (la versión "Cinematic", con Veo, probablemente requiere Pro/Ultra — verifícalo en tu cuenta, no está confirmado que Plus la incluya). Es tentador porque parece resolver todo el pipeline de golpe, pero **no lo es para tu canal**: no controlas el hook, la estructura de 8 bloques, ni qué afirmación va marcada y verificada — exactamente lo que el control de calidad de `06-quality-control.md` exige. Publicar ese vídeo tal cual es casi la definición de "sin aportación editorial real" que persigue la política de contenido no auténtico (§6D del informe general). Úsalo, si acaso, como **prueba rápida de si el tema tiene suficiente material** antes de invertir horas en el guion — no como sustituto del guion.

## 2. Guion (Claude)

Usa `youtube-lab/prompts/03-guion.md` tal cual está, pegando la investigación de Gemini como material de entrada. Es donde Claude rinde mejor de los dos: control fino de estructura, marcas de locución, verificación línea a línea.

**Salida que necesitas para el siguiente paso: el guion troceado en bloques con su timecode aproximado**, a 150 palabras/minuto. Para 10 minutos: ~1.500 palabras.

## 3. Voz — edge-tts (gratis, local, sin límite)

`edge-tts` es una librería Python que usa el mismo motor de voz neuronal que el lector de Microsoft Edge, sin API key y sin coste. Calidad muy por encima de un TTS robótico clásico — no es ElevenLabs, pero para un canal que empieza es más que suficiente, y puedes migrar a ElevenLabs (§7.3 del informe general) el día que la economía del canal lo justifique.

```bash
# En tu máquina (no en este sandbox):
pip install edge-tts

# Listar voces en español para elegir la que mejor encaje con el tono del canal
edge-tts --list-voces | grep es-

# Voces recomendadas para negocios/documental (masculina y femenina, neutras):
#   es-ES-AlvaroNeural   (España, masculina, seria)
#   es-ES-ElviraNeural   (España, femenina, clara)
#   es-MX-JorgeNeural    (México, masculina, cálida)
#   es-US-PalomaNeural   (neutro LatAm, femenina)

# Generar el audio completo del guion:
edge-tts --voice es-ES-AlvaroNeural --file guion.txt --write-media voz.mp3 --write-subtitles voz.srt
```

**Detalle importante: `--write-subtitles` te da el `.srt` con los timecodes reales de la narración generada.** Eso resuelve de un tiro el problema de sincronizar subtítulos y storyboard — no necesitas transcribir nada a posteriori, ya tienes el timing exacto de cada frase.

Si el guion tiene marcas `[pausa]`, `[más lento]`, etc. (como pide `03-guion.md`), edge-tts no las interpreta directamente — dos opciones:
- Insertar silencios manuales editando el SSML (edge-tts soporta SSML básico).
- Más simple: dejar que el ritmo natural del TTS marque el paso, y ajustar pausas en el montaje (Remotion) añadiendo un frame de espera donde el guion lo pedía.

## 4. Visuales — el reparto que hace esto gratis

Con el guion troceado y el `.srt` con timecodes, divides el vídeo en planos (usa `04-storyboard.md`). La clave económica:

| Tipo de plano | Cuántos en 10 min | Fuente | Coste |
|---|---|---|---|
| Gráficos de datos, cifras, mapas | 20-30 | **Remotion** (código, tuyo) | 0 € |
| Ambiente genérico (oficina, ciudad, manos, calle) | 15-20 | **Pexels** | 0 € |
| Archivo real (logos, productos, prensa, anuncios) | 5-10 | Búsqueda manual, hemeroteca | 0 € |
| **Planos de alto impacto** (solo apertura + clímax) | **3-5** | **Veo 3.1 Fast vía Flow** (Google AI Plus) | Ya pagado |

**Con AI Plus, Veo es un recurso escaso, no la columna vertebral del vídeo.** El plan da ~200 créditos/mes [SECUNDARIO, confirma tu saldo real en la app]; si un clip de Veo 3.1 Fast cuesta en torno a 20 créditos, eso son **~10 clips al mes en total**, no por vídeo. Con esa cuota, un vídeo de 10 minutos solo puede permitirse **3-5 planos Veo verdaderamente decisivos** — el hook de apertura y el momento de giro/clímax — dejando margen para otro vídeo o dos al mes. El resto del peso visual (25-40 planos) lo llevan Remotion y Pexels, que no gastan nada. Esto además **obliga a mejor criterio editorial**: elegir qué 3-5 momentos merecen de verdad IA generativa es más sano para el vídeo que rellenar con IA por defecto.

Si más adelante el canal genera ingresos y quieres más planos generados, el cálculo de pago por uso está en el informe general (§7.4, ~0,09 $/s en Kling 3.0 como alternativa más barata que Veo).

**Cómo generar esos 3-5 planos:**
1. En la app Gemini, sección **Flow**.
2. Solo para los planos marcados como `VIDEO_IA` en el storyboard que de verdad importan (`04-storyboard.md` los marca con ⭐) — no generes de más "por si acaso".
3. Guarda cada clip con el número de plano en el nombre de archivo (`plano-07.mp4`) — lo necesitas para el montaje automático del siguiente paso.

Para las imágenes fijas (miniatura, fondos de gráficos): usa **Whisk** dentro de la misma app Gemini, mismos créditos — son más baratas que un vídeo, así que aquí sí puedes ser más generoso.

## 5. Montaje — Remotion (gratis, con código)

Remotion te da control total sin pagar por minuto de render. Ya tienes Node instalado (`node --version` → v22, comprobado). Instalación en tu máquina:

```bash
npx create-video@latest mi-canal-videos
cd mi-canal-videos
```

Estructura mínima para automatizar el ensamblado (composición que lee tu `.srt`, tus clips numerados y tu audio, y monta el vídeo):

- Una composición `Documental10min.tsx` que:
  1. Coloca el audio de `voz.mp3` como pista base.
  2. Lee `voz.srt` y quema los subtítulos sincronizados (Remotion tiene el paquete `@remotion/captions` para esto).
  3. Coloca cada `plano-XX.mp4`/imagen en su timecode según el storyboard.
  4. Añade las cartelas de capítulo si tu estructura las usa (§3.4 del informe: Hook/Apuesta/Contexto/Ascenso/Grieta/Giro/Consecuencia/Cierre).
  5. Aplica una transición estándar (fundido cruzado de 0,3s) entre planos — defínelo una vez, se aplica a todos.

- Render final: `npx remotion render Documental10min out/video-final.mp4`. Corre en tu máquina, sin coste por minuto.

**Por qué Remotion y no un editor manual para esta fase:** una vez que tengas la composición hecha para tu primer vídeo, los siguientes solo cambian los assets de entrada (audio, srt, clips) — el montaje se vuelve casi automático. Es la inversión de tiempo que menciona el informe general (§7.6): cuesta más arrancar, pero el vídeo 4 en adelante sale mucho más rápido que editando a mano cada vez.

**Si prefieres no tocar código todavía:** monta el primer vídeo a mano en DaVinci Resolve (gratis) para aprender qué plantilla necesitas, y automatiza con Remotion a partir del vídeo 3-4, tal como recomienda §8.2 del informe general.

## 6. Miniatura

Whisk (dentro de tu Google AI Plus) para el concepto base, siguiendo `05-titulos-thumbnails.md`. Retoque final de texto/contraste con una herramienta gratuita (Photopea, en el navegador, sin instalar nada).

## 7. Publicación

YouTube Data API v3 (gratis, cuota diaria de 10.000 unidades — subir un vídeo cuesta 1.600). Si prefieres no programar la subida, YouTube Studio manual es igual de válido y no cuesta nada; automatizar esto solo merece la pena a partir de que publiques con regularidad.

---

## Resumen del flujo, de principio a fin

```
Gemini Deep Research (investigación)
        ↓
Claude + 02-research-brief.md (tabla de hechos verificada)
        ↓
Claude + 03-guion.md (guion de ~1.500 palabras, marcado)
        ↓
edge-tts (voz.mp3 + voz.srt, con timecodes reales)
        ↓
Claude + 04-storyboard.md (60-90 planos, marcados por fuente)
        ↓
  ├── Remotion: gráficos + cartelas (planos de datos)
  ├── Pexels: b-roll genérico
  ├── Hemeroteca/archivo: material real
  └── Flow/Veo 3.1 Fast (Google AI Plus): 3-5 planos de alto impacto

(NotebookLM ya se usó antes, en el paso 1, para la tabla de hechos con cita)
        ↓
Remotion (composición): ensambla audio + subtítulos + planos + transiciones
        ↓
Whisk (Google AI Plus): miniatura
        ↓
Claude + 06-quality-control.md (verificación factual antes de publicar)
        ↓
YouTube (manual o API)
```

**Coste marginal por vídeo: 0 €.** Coste de tiempo: el mismo 3-5 horas de revisión humana del informe general (§9.3) — eso no lo quita ninguna herramienta, es lo que hace que el vídeo no sea "slop" y siga siendo monetizable bajo la política de contenido no auténtico (§6D del informe general).

## Primer vídeo: qué instalar en tu máquina, en orden

```bash
# 1. Python + edge-tts
pip install edge-tts

# 2. FFmpeg (Remotion lo necesita para renderizar)
#   macOS:   brew install ffmpeg
#   Ubuntu/Debian: sudo apt install ffmpeg
#   Windows: winget install ffmpeg

# 3. Remotion (Node ya lo tienes si hiciste `node --version` y te dio v18+)
npx create-video@latest

# 4. (Opcional) clave de Pexels — gratis, para b-roll por API en vez de descarga manual
#    https://www.pexels.com/api/
```

Con eso — y tu Google AI Plus ya activo — tienes el pipeline completo funcionando sin pagar nada adicional.
