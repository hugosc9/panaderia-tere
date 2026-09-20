# YouTube Business Automation Lab

Investigación y herramientas para montar un canal de YouTube de negocios, faceless y automatizado con IA.

## Empieza aquí

**[INFORME.md](INFORME.md)** — el informe completo: análisis de mercado, subnichos, oportunidades, stack de IA, pipeline, costes y cinco propuestas de canal.

> ⚠️ **Sobre el análisis de Éxito Oculto:** este entorno bloquea el acceso de red a YouTube y a todos los agregadores de estadísticas, así que no hay ni una métrica real de ese canal en el informe. En lugar de inventarlas, está escrita la herramienta que hace ese análisis en tu máquina en 15 minutos. Ver §2 del informe.

## Herramienta: `yt_lab.py`

Radiografía de canales de YouTube con datos oficiales de la Data API v3. Sin dependencias: solo Python 3.

```bash
# 1. Clave gratuita: console.cloud.google.com → habilitar "YouTube Data API v3" → Credenciales
export YOUTUBE_API_KEY="AIza..."

# 2. Radiografía completa de un canal
python3 tools/yt_lab.py channel @exitoocultoyt

# 3. Comparar varios canales del género
python3 tools/yt_lab.py compare @MagnatesMedia @CompanyMan @ModernMBA

# 4. Reanalizar un volcado ya descargado, sin gastar cuota
python3 tools/yt_lab.py channel --from-json data/raw/exitoocultoyt_2026-09-20.json
```

**Qué devuelve:** identidad del canal, mediana/media/máximo de visitas, ratio máximo/mediana, cadencia y duración por trimestre, **top 20 outliers** y los 8 peores, **cruce de cada patrón de título con el rendimiento real del canal** (con *lift* y tamaño de muestra), y duración vs rendimiento. Escribe un informe `.md`, un `.csv` con todos los vídeos, y el JSON crudo.

**Cómo mide outliers.** No ordena por visitas — eso solo premia a los vídeos antiguos. Compara cada vídeo contra sus vecinos temporales del mismo formato (±120 días) en dos ejes, visitas y visitas/día, y se queda con el menor de los dos múltiplos. Detalle en §3.1 del informe.

**Cuota:** ~13 unidades por canal de 300 vídeos, del límite gratuito de 10.000/día. Evita `search.list` a propósito (cuesta 100 por llamada).

**Lo que la API no da, de ningún canal ajeno:** retención, CTR, impresiones y fuentes de tráfico. Son exclusivos del dueño del canal. Cualquier informe que te dé el CTR de un canal ajeno se lo está inventando.

## Prompts del pipeline

| Archivo | Etapa |
|---|---|
| [`prompts/01-idea-generation.md`](prompts/01-idea-generation.md) | Outliers + gaps → 25 ideas con ángulo propio |
| [`prompts/02-research-brief.md`](prompts/02-research-brief.md) | Fuentes primarias → tabla de hechos con cita y fecha |
| [`prompts/03-guion.md`](prompts/03-guion.md) | Tabla de hechos → guion marcado para locución |
| [`prompts/04-storyboard.md`](prompts/04-storyboard.md) | Guion → 60-90 planos con fuente y prompt |
| [`prompts/05-titulos-thumbnails.md`](prompts/05-titulos-thumbnails.md) | 15 títulos + 5 conceptos de thumbnail |
| [`prompts/06-quality-control.md`](prompts/06-quality-control.md) | Verificación factual + comprobación de autenticidad |

Los prompts 01, 03 y 05 tienen una sección **«Reglas aprendidas de mi canal»**, vacía al principio. Es el único punto del sistema que debe cambiar con el tiempo: ahí van los patrones que funcionan *en tu canal*, medidos con `yt_lab.py` y con tu CTR real. Ese es el bucle de aprendizaje (§8.1 del informe).

## La regla que resume el proyecto

**Automatiza lo que ya has hecho tres veces a mano. Nunca antes.**
