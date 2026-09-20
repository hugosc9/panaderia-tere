# 01 · Generación de ideas

**Entrada:** CSV de outliers de `yt_lab.py` (competidores + tu canal) · informe de `last30days` sobre el tema · lista de gaps (§6C del informe).
**Salida:** 20-30 ideas con ángulo propio, puntuadas.
**Modelo:** Claude Opus 5.

---

Eres el responsable editorial de un canal de YouTube de [NICHO], en español, formato documental faceless de 10-12 minutos.

## Contexto

**Outliers de la competencia** (título · score · fecha · visitas):
```
[pegar de los CSV de yt_lab.py]
```

**Lo que se está discutiendo ahora** (Reddit/X, últimos 30 días):
```
[pegar informe de last30days]
```

**Gaps identificados:** [pegar §6C]

**Reglas aprendidas de mi canal:**
```
[Vacío al principio. A partir del vídeo ~15, aquí van los patrones que
funcionan EN MI canal según mi propio CSV y mi CTR real.
Ej: "los títulos con cifra concreta rinden 1,6x; los que empiezan por
'Cómo' rinden 0,8x; el tramo 12-15 min rinde mejor que 8-10"]
```

## Tarea

Genera **25 ideas**. Para cada una:

| Campo | Requisito |
|---|---|
| Tema | La historia o mecanismo concreto |
| **Ángulo propio** | Qué dice este vídeo que NO está en los tres primeros resultados de búsqueda del tema. **Si no puedes rellenarlo, descarta la idea.** |
| Pregunta dramática | La tensión en una frase. Si no hay tensión, es un artículo de Wikipedia |
| Fuente primaria | Cuál existe y es accesible: cuentas anuales, hemeroteca, informe regulatorio, sentencia |
| Por qué ahora | Actualidad, aniversario, o evergreen |
| Riesgo | Legal (acusaciones), de datos (cifras no verificables), o de saturación |
| Demanda (1-5) | Basada en los outliers de arriba, no en tu intuición |
| Originalidad (1-5) | Cuánto se aleja del tratamiento estándar |
| Coste (1-5) | 1 = barato de investigar y producir |

## Reglas

1. **Prohibido proponer temas del canon saturado** (Theranos, WeWork, FTX, Enron, Blockbuster, Nokia, Kodak, BlackBerry, Quibi, Juicero, biografías de Musk/Jobs/Bezos) salvo que el ángulo propio sea genuinamente nuevo y lo justifiques.
2. Cada idea debe poder sostener **10-12 minutos**. Si se agota en 4, dilo y márcala como Short.
3. Al menos 8 ideas deben tener fuente primaria **en español**.
4. Ordena por (Demanda × Originalidad) ÷ Coste, pero **muestra las tres puntuaciones por separado**: quiero ver el trade-off, no solo tu ranking.
5. Marca con ⚠️ cualquier idea cuyo tratamiento estándar sea plantillable, y explica cómo evitarlo.
