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

---

## Segundo kit evaluado: tutorial "Stickman explainer" (ChatGPT + Google Flow + CapCut)

**Fecha:** 25/09/2026. El usuario pegó la transcripción completa de un tutorial de YouTube con un flujo: prompt maestro en ChatGPT (ideas → guion → hoja de referencia del personaje → prompts de animación con locución integrada) → Google Flow (Nano Banana 2 para la hoja de referencia, Omni Flash para animar cada escena con voz ya incluida) → CapCut (montaje, subtítulos automáticos, exportación).

### Verificación de las cifras "prueba" — ninguna se sostiene

El vídeo cita canales como evidencia de que el formato "stickman" funciona: *Zen* (181.000 subs, 33 vídeos, primer vídeo con 7,8M de visitas), *Rico Animations* (~13M subs), *Good Enough Animations* (1,5M subs), *The Blurb* (119.000 subs), *Simple Paint Official* (430.000 subs). Comprobado vía vidIQ:

- **Zen**: no existe ningún canal de "stickman explainer" con esas cifras. El único "Zen" grande real (1,68M subs) es un canal de memes/ediciones con 510 vídeos, no 33.
- **Rico Animations**: no existe ningún canal con ese nombre cerca de 13M suscriptores. El mayor real tiene 2.260.
- **Good Enough Animations**: no existe. Cero resultados.

Tres de tres verificadas no coinciden con la realidad. Combinado con el gancho de "comenta X para conseguir el prompt gratis" (farming de comentarios) y con la propia admisión en el vídeo de que se agotaron los créditos de la cuenta a mitad del tutorial (contradice el titular de "herramientas completamente gratis"), el vídeo debe tratarse como marketing sin pruebas verificables, no como evidencia de mercado.

### Lo adoptado

**Referenciar la imagen del personaje en cada generación, en vez de describirlo de memoria.** Es una técnica real y correcta para mantener consistencia visual — y ya está incorporada en `03-storyboard.md` de este proyecto ("sube la imagen de referencia... no describas el robot de memoria"), así que no requiere ningún cambio.

### Lo descartado

El prompt maestro que genera de un tirón ideas + guion + personaje + animaciones, sin tabla de hechos ni verificación — mismo antipatrón que el kit de Imperator Club. Para un vídeo de 30 segundos sobre un hecho histórico ampliamente conocido el riesgo es bajo, pero el método sigue siendo el que este proyecto evita deliberadamente para el canal, y las pruebas sociales que lo acompañan no resisten una comprobación básica.
