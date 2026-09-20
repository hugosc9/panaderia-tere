# 05 · Títulos y thumbnails

**Entrada:** guion final + patrones validados de tu canal.
**Salida:** 15 títulos + 5 conceptos de thumbnail.
**Modelo:** Claude Opus 5 (+ Marketing Skills de Corey Haines si las tienes instaladas).

---

## Contexto

Vídeo: [TEMA]. Hook actual: «[pegar primeras 3 frases del guion]».

**Patrones validados en MI canal** (de la sección 5 del informe de `yt_lab.py`):
```
[Ej: "secreto_oculto lift 1,8x (n=11) · contradiccion lift 1,5x (n=9) ·
numero lift 1,0x (n=24, no explica nada) · como lift 0,8x (n=12)"]
```

**Mis 3 títulos con mejor CTR real** (YouTube Studio): [...]
**Mis 3 peores:** [...]

## Títulos

Genera **15**, agrupados en tres enfoques de 5:

- **A · Hueco de curiosidad con sujeto concreto** — nombra algo identificable y deja un agujero.
- **B · Contradicción** — dos hechos que no deberían convivir.
- **C · Cifra imposible** — un número que obliga a comprobarlo.

Para cada título: **≤ 60 caracteres** (para que no se corte en móvil), qué patrón usa, y **qué promete exactamente**.

**Reglas:**
1. **El título no puede prometer nada que el vídeo no entregue.** El clickbait incumplido se paga en retención, que es lo que de verdad te penaliza.
2. Prohibido «increíble», «impactante», «no te lo vas a creer», «esto cambiará todo».
3. **Si un patrón tiene lift ~1,0 en mi canal, no lo uses** aunque sea un consejo habitual de YouTube.
4. Marca los 3 que más te convencen y **di por qué**, refiriéndote a los datos de arriba.

## Thumbnails

**5 conceptos**. Para un canal faceless sin caras, la fórmula es: **objeto o logo reconocible + cifra + señal de conflicto** (flecha roja, grieta, tachado).

Para cada concepto:
- Descripción visual en una frase
- **Texto: 3-5 palabras como máximo**, funcionando como gancho, no como descripción
- Elemento focal y por qué funciona a 120 px de ancho (el tamaño real en el feed móvil)
- Contraste dominante
- Prompt de generación en inglés
- **Cómo se diferencia** de la thumbnail estándar de este tema

**Regla:** no repitas la composición de mi último vídeo. Un canal se reconoce por la paleta y el estilo, no por clonar el encuadre.

**Dos afinamientos útiles** (de revisar un kit externo, ver `pipeline-10min/EVALUACION-KIT-EXTERNO.md` — el resto de ese kit se descartó, esto sí vale la pena):
- **Texto e imagen deben contar cosas distintas que se completen entre sí**, no la misma idea dos veces. Si el texto ya dice "quebró en 3 años", la imagen no necesita mostrar un gráfico cayendo — puede mostrar la sede vacía, o el logo tachado. La redundancia texto/imagen desperdicia la mitad del espacio de curiosidad.
- **Un elemento de tensión visual concreto** ayuda a que el ojo sepa qué mirar primero en <1s: una flecha, un tachado, un contraste "antes glorioso / ahora destruido". Para un canal sin caras, esto sustituye a la expresión facial exagerada que usan los canales de misterio — aquí la tensión va en el objeto o el logo, no en una persona.
