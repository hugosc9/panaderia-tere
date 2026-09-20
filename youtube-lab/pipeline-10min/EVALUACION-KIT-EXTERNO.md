# Evaluación de un kit externo (canal "Imperator Club")

**Fecha:** 21/09/2026. El usuario compartió una página de Notion pública con un "mega-prompt" para producir vídeos largos monetizables con IA, más una lista de herramientas. No pude abrirla directamente (Notion bloqueado por la política de red de este entorno, y la página no estaba compartida con mi conector), así que el usuario pegó el texto completo. Esto documenta qué se adopta, qué se descarta y por qué — siguiendo el principio del proyecto de estudiar fuentes externas sin copiarlas sin criterio.

---

## Lo adoptado

| Herramienta | Dónde entra | Estado |
|---|---|---|
| **Meta AI** (meta.ai/create) | Alternativa gratuita a Whisk para imágenes fijas, fuera de la cuota de Google | [SECUNDARIO] no verificado en esta sesión |
| **Clipchamp** | Alternativa a DaVinci Resolve para montar el primer vídeo a mano, sin instalar nada | Editor legítimo y gratuito de Microsoft |
| **Google AI Studio Live** | Posible vía de narración gratuita fuera de la cuota de ElevenLabs | [SECUNDARIO] pensado para conversación, no para leer un guion literal — probar antes de depender de él |
| Estructura de título/thumbnail/tags/gancho | Reciclada como plantilla de copywriting en `prompts/05-titulos-thumbnails.md` | Válida como forma, no como sustituto del contenido verificado |

## Lo descartado, y por qué

### 1. El guion generado de una sola vez, sin fuentes ni verificación

El kit pide a un LLM que escriba un guion documental completo de hasta 20 minutos a partir de una sola frase de idea, sin tabla de hechos, sin fuente primaria, sin distinguir lo verificado de lo inventado. Es el patrón exacto que el informe general marca como "malo" (`Idea → IA → vídeo → subir`, sección "Principio fundamental"), solo que con más pasos alrededor.

Además, el propio prompt instruye **evitar deliberadamente expresiones que "suenen a IA"** ("fascinante", "en conclusión", etc.) para que el resultado *parezca* escrito por una persona. Eso no añade verificación ni aportación editorial real — camufla la ausencia de ambas. Es la definición operativa de lo que persigue la política de "contenido no auténtico" de YouTube (§6D del informe general): plantilla, producido en masa, sin aportación de autor real, solo que aquí además disfrazado a propósito.

**No sustituye** a `02-research-brief.md` (tabla de hechos con cita) + `03-guion.md` (estructura + marcas de locución) + `06-quality-control.md` (verificación frase a frase por un segundo modelo). Esos tres prompts siguen siendo el camino para este canal.

### 2. La herramienta para quitar marcas de agua

El kit enlaza una herramienta para eliminar marcas de agua de vídeo, en el contexto de quitar la de Veo/Flow. **No la incorporo y recomiendo no usarla.**

- Las marcas de agua de contenido generado por IA (SynthID en el caso de Veo) existen para identificar ese contenido como sintético. Quitarla **viola los términos de uso de la propia herramienta que generó el vídeo** — no es una cuestión de estilo, es un incumplimiento contractual con Google.
- Combinado con el punto 1 (guiones sin verificar, escritos deliberadamente para parecer humanos), el efecto neto es disfrazar contenido no verificado como si tuviera aportación humana real, tanto ante el espectador como ante los sistemas de moderación de la plataforma.
- Esto no es "agresivo pero válido" — es el tipo de práctica que hace perder la monetización de golpe cuando se detecta, y el proyecto entero (según el CLAUDE.md original) busca justo lo contrario: un canal defendible a largo plazo, no un atajo que se cae a la primera auditoría.

---

## Conclusión

El kit tiene ideas de copywriting reciclables y dos o tres herramientas gratuitas que no teníamos catalogadas. El núcleo de su método (un guion generado de una vez, sin fuentes, con estilo deliberadamente anti-detección, sobre vídeo con la marca de procedencia eliminada) es incompatible con los objetivos que fijaste al principio del proyecto: aprender de negocios de verdad y construir un canal que no dependa de escapar controles de la plataforma.
