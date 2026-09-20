# Informe: canal de YouTube de negocios faceless + automatización con IA

**Fecha:** 20 de septiembre de 2026
**Encargo:** analizar el canal *Éxito Oculto*, estudiar el mercado de canales de negocios, elegir subnicho, montar un stack de IA y diseñar el pipeline completo.

---

## ⚠️ Nota de honestidad sobre los datos (léela antes que nada)

Este informe distingue cuatro niveles. Aparecen marcados en todo el documento:

| Marca | Significado |
|---|---|
| **[OBSERVADO]** | Dato que he visto directamente en una fuente en esta sesión. |
| **[SECUNDARIO]** | Dato publicado por un tercero (blog, comparativa, prensa) que no he podido contrastar contra la fuente primaria. Trátalo como orientativo. |
| **[INFERENCIA]** | Conclusión mía a partir de lo anterior. Es un razonamiento, no un hecho. |
| **[NO VERIFICABLE]** | No he podido comprobarlo desde este entorno. No lo doy por bueno. |

### Actualización: ya hay datos reales de Éxito Oculto

Cuando escribí esta sección, el entorno bloqueaba `youtube.com` y todos los agregadores de estadísticas (`403` en el proxy de egreso), y no quise rellenar el análisis con cifras inventadas. Desde entonces se conectó el **conector vidIQ** en esta sesión, que da acceso directo y oficial a datos de canal, y con él he hecho la radiografía completa: **el 100% del catálogo largo (8/8 vídeos)** y una muestra de 71 shorts, con outlier scoring por cohorte temporal (mismo método que `tools/yt_lab.py`) y cruce de patrones de título contra rendimiento real.

**El análisis completo está en [`ANALISIS-EXITO-OCULTO.md`](ANALISIS-EXITO-OCULTO.md).** Las secciones 2 y 3 de este documento quedan como el protocolo general (sigue siendo válido si en el futuro quieres analizar otros canales sin vidIQ), pero para Éxito Oculto en concreto, ese archivo es la fuente autorizada, no lo que sigue aquí abajo.

**Un hallazgo que cambia una premisa del encargo:** los datos reales muestran que Éxito Oculto **no es un canal de historias empresariales** como asumía el CLAUDE.md del proyecto — es un canal de *dinero + mentalidad + desarrollo personal* (según su propia descripción), con solo 4 meses de vida, 88% del catálogo en formato Shorts, y sin publicar desde hace ~8 semanas. El hueco de "historias empresariales puras en español" que identifica la sección 6C de este informe **sigue abierto**: ni el canal de referencia del proyecto lo ocupa.

Pedías explícitamente que no inventara métricas y que dijera claramente lo que no puedo verificar. Por eso la primera versión de esta sección documentó el bloqueo en vez de rellenarlo con ficción — y por eso, en cuanto hubo una vía real de datos, la usé y sustituí la ficción por hechos.

---

## 1. RESUMEN EJECUTIVO

**Nueve conclusiones que cambian decisiones:**

1. **El análisis de Éxito Oculto ya está hecho, con datos reales, vía vidIQ.** Resultado clave: no es un canal de historias empresariales, es un canal de dinero/mentalidad con 4 meses de vida, 88% Shorts, y parado desde hace 8 semanas. Su fórmula real: el ángulo de "mecanismo psicológico + estatus" multiplica por 6-35x sobre "guía práctica genérica" en sus vídeos largos — comprobado con el catálogo completo, no con folclore de YouTube. Detalle completo en [`ANALISIS-EXITO-OCULTO.md`](ANALISIS-EXITO-OCULTO.md).

2. **El riesgo número uno de este proyecto no es la calidad: es la desmonetización.** YouTube renombró su política de "contenido repetitivo" a **"contenido no auténtico"** el 15 de julio de 2025, apuntando a vídeo plantillado, producido en masa y sin aportación editorial real. **[SECUNDARIO]** El pipeline literal *ChatGPT → ElevenLabs → stock → subir* es la definición textual de lo que la política persigue. Tu instinto de "no quiero un canal de contenido vacío" no es una preferencia estética: es la condición de supervivencia económica del canal. Sección 6D y 7.

3. **La automatización debe atacar la producción, no el criterio.** Reparto realista: ~80% automatizable (investigación, borradores, voz, visuales, montaje, render, publicación, analítica), ~20% irrenunciablemente tuyo (elección del tema, ángulo original, verificación de datos, pase final del guion, decisión del thumbnail). Ese 20% son unas 3-5 horas por vídeo, y es lo que separa un canal de un vertedero.

4. **El idioma es la decisión económica más grande, y va antes que el nicho.** Contenido en inglés se paga entre 3x y 5x más que el mismo tema en español; el RPM típico en español está en torno a 2,00-3,30 USD por 1.000 visualizaciones monetizadas, frente a CPM de 10-25 USD citados para *business case studies* en inglés. **[SECUNDARIO]** Pero en español tienes ventaja competitiva real y puedes juzgar la calidad de tu propio guion. Sección 10.

5. **El hueco de mercado más claro que he encontrado es el storytelling empresarial sobre empresas hispanas, en español.** El catálogo de casos en inglés (Theranos, WeWork, FTX, Blockbuster, Nokia, Kodak) está agotado y recontado cientos de veces. Mercadona, Inditex, Mercado Libre, Bimbo, Glovo, Cabify, Hawkers, Freixenet, Telepizza, Rappi o Cupra tienen historias equivalentes en calidad narrativa y una fracción de la cobertura. Sección 6C.

6. **Los primeros 30 segundos deciden el vídeo.** El vídeo medio pierde un 30-40% de la audiencia en esos 30 segundos y casi nunca recupera lo perdido ahí; los guiones que entregan una promesa concreta antes del segundo 15 retienen ~52% frente a ~44% de los que no. **[SECUNDARIO]** Consecuencia de diseño: el hook no se escribe al final, se escribe **primero**, y el resto del guion se escribe para sostener esa promesa.

7. **Un outlier no es "el vídeo con más visitas".** Es el vídeo que rindió muy por encima de sus vecinos temporales del mismo formato. Es la única medida que separa "este tema funciona" de "este vídeo es antiguo y ha acumulado". La herramienta lo calcula así a propósito, y además cruza cada patrón de título con el rendimiento real para decirte si ese patrón explica algo **en ese canal concreto** o es folclore de YouTube. Sección 3.

8. **El coste marginal por vídeo está entre 15 y 25 USD; el fijo, entre 60 y 130 USD al mes.** Con 4 vídeos al mes: ~150-200 €/mes todo incluido. El cuello de botella no es el dinero, es tu tiempo de revisión. Sección 9.

9. **No te doy un ranking de nichos.** Te doy cinco direcciones de canal con sus diferencias en coste, techo, saturación, riesgo de política y —lo que pediste explícitamente— **qué aprenderías tú** con cada una. Decides tú. Sección 10.

---

## 2. ANÁLISIS DE ÉXITO OCULTO

### 2.1 Qué he intentado y qué ha fallado

| Vía | Resultado |
|---|---|
| Abrir `youtube.com/@exitoocultoyt` y `/about` | `403` del proxy de egreso. **[OBSERVADO]** |
| `curl` directo al canal | `CONNECT tunnel failed, response 403`. **[OBSERVADO]** |
| Social Blade, ViewStats, NoxInfluencer, youtubers.me | `403`, todos. **[OBSERVADO]** |
| Búsqueda web por nombre, handle y variantes (4 consultas) | Cero referencias al canal. **[OBSERVADO]** |

El bloqueo es de la política de red del entorno, no un fallo puntual. No se puede ni se debe rodear.

### 2.2 El protocolo que lo resuelve (15 minutos de tu tiempo)

**Paso 1 — Clave de API (5 min, gratis).**
`console.cloud.google.com` → crear proyecto → *APIs y servicios* → habilitar **YouTube Data API v3** → *Credenciales* → *Crear credenciales* → *Clave de API*.
Cuota gratuita: 10.000 unidades/día. **[OBSERVADO]** La herramienta gasta ~13 unidades por canal de 300 vídeos, porque evita deliberadamente `search.list` (cuesta 100 unidades por llamada y se come la cuota diaria en 100 búsquedas **[OBSERVADO]**). Puedes radiografiar ~700 canales al día con la cuota gratis.

**Paso 2 — Ejecutar.**

```bash
export YOUTUBE_API_KEY="AIza..."
cd youtube-lab
python3 tools/yt_lab.py channel @exitoocultoyt
```

Sin dependencias: solo Python 3 y biblioteca estándar.

**Paso 3 — Leer.** Genera tres archivos en `data/raw/`: el volcado JSON crudo (para reanalizar sin gastar cuota, con `--from-json`), un CSV con todos los vídeos, y un informe en Markdown con:

- Identidad del canal: fecha de creación, país, idioma declarado, suscriptores, visitas totales, descripción.
- Números base: mediana, media, máximo, mínimo de visitas y **ratio máximo/mediana** (por encima de 8x = canal que vive de unos pocos vídeos).
- Cadencia por trimestre: cuántos vídeos, mediana de visitas y duración mediana. Ahí se ve si acelera o se apaga, y si está alargando o acortando.
- **Top 20 outliers** con score, etiqueta, fecha, duración, visitas, visitas/día, likes y comentarios.
- **Los 8 peores**, que suelen enseñar más que los mejores.
- **Cruce patrón de título → rendimiento real**, con *lift* y tamaño de muestra.
- Duración vs rendimiento por tramos.

**Paso 4 — Lo que la API no da, y que nadie puede darte de un canal ajeno:**
retención, CTR, impresiones y fuentes de tráfico son exclusivos del dueño del canal vía YouTube Analytics API. **Cualquier informe que te dé el CTR de un canal ajeno se lo está inventando.** Likes y comentarios pueden venir ocultos si el creador los desactiva.

**Paso 5 — La capa cualitativa (la que no automatiza nadie).** Con el CSV delante, ordena por score y mira **los 5 outliers y los 5 peores**:

- Thumbnails: las URLs están en el CSV. Ábrelas en pestañas y compara outliers contra fracasos. Cuenta elementos, texto, caras, contraste, si hay logo, si hay cifra.
- Estructura: cronometra los 5 outliers. Anota en qué segundo aparece la promesa, en qué segundo empieza el conflicto, cuántos giros hay, cómo cierran.
- Producción: ¿voz humana o sintética? ¿stock, imágenes IA, vídeo IA, capturas, gráficos? ¿subtítulos quemados? ¿música continua?

Para esa capa, el plugin `claude-video-vision` (extrae fotogramas + transcribe y se lo pasa a Claude) es la vía práctica, porque Claude no acepta vídeo de forma nativa a día de hoy. **[SECUNDARIO]** Sección 7.

### 2.3 Lo que NO voy a escribir

No voy a rellenar aquí "temática exacta, subnicho, público objetivo, tono, estilo narrativo" de Éxito Oculto. Con cero datos, eso sería ficción con formato de informe. El protocolo de arriba te da la radiografía real en 15 minutos, y con el CSV en la mano puedo hacerte el análisis completo en la siguiente sesión.

---

## 3. FÓRMULA DE SUS VÍDEOS

Mismo principio: no puedo darte la fórmula de un canal cuyos datos no he visto. Lo que sí puedo darte es **el método para extraerla** y **las hipótesis concretas que hay que poner a prueba**, para que el análisis no sea "parece que los títulos con números funcionan".

### 3.1 Cómo mide outliers la herramienta (y por qué así)

El error habitual es ordenar por visitas. Eso premia a los vídeos antiguos, que han tenido más tiempo de acumular. La herramienta hace esto:

```
Para cada vídeo:
  cohorte = vídeos del MISMO formato (long-form vs short)
            publicados dentro de ±120 días, excluido él mismo
  views_multiple = visitas / mediana de visitas de la cohorte
  vpd_multiple   = visitas-por-día / mediana de visitas-por-día de la cohorte
  score          = min(views_multiple, vpd_multiple)
```

- La cohorte temporal neutraliza el crecimiento del canal: un vídeo de 2023 se compara con 2023, no con hoy.
- `vpd_multiple` detecta antes los vídeos jóvenes que están despegando.
- Tomar el **mínimo** de los dos evita el falso positivo clásico: un vídeo de tres días con visitas/día altísimas pero poco recorrido.
- Escala: ≥5x extremo, ≥3x fuerte, ≥2x outlier, ≤0,4x bajo rendimiento.

### 3.2 Cómo se valida un patrón de título (y no al revés)

Pediste explícitamente: *"no asumas que estos patrones funcionan: compruébalo con los datos del canal"*. La herramienta etiqueta cada título con 12 patrones (número, dinero, pregunta, "cómo", "por qué", secreto/oculto, fracaso/caída, éxito/ascenso, "la empresa que…", superlativo, contradicción, mayúsculas de énfasis, temporal) y luego calcula, para cada patrón:

```
lift = mediana del score de los vídeos CON el patrón
     / mediana del score de los vídeos SIN el patrón
```

Lectura: **lift > 1,3 con n ≥ 8 vídeos** empieza a ser señal. Lift ~1,0 significa que ese patrón no explica nada en ese canal, por muy repetido que esté el consejo. Y con n < 8 no concluyas: en canales pequeños, tres vídeos afortunados inflan cualquier patrón. La herramienta te da la n siempre, precisamente para que puedas desconfiar.

### 3.3 Las cuatro hipótesis a contrastar

Cuando tengas el CSV, contrasta estas cuatro. Son las que más veces discriminan en este género. **[INFERENCIA]**

- **H1 — Hueco de curiosidad con sujeto concreto.** Un título funciona cuando nombra algo identificable (empresa, producto, cifra) **y** deja un agujero: *"La empresa que vendió agua por 300 € el litro"*. Ni misterio puro sin sujeto ("El secreto que nadie te cuenta") ni sujeto sin misterio ("Historia de Mercadona"). Se contrasta cruzando los patrones `secreto_oculto` y `mayusculas_enfasis` contra `la_empresa_que` y `dinero`.
- **H2 — La contradicción rinde más que el superlativo.** *"Gana 40.000 millones y nadie sabe su nombre"* (tensión) frente a *"La mayor empresa del mundo"* (afirmación). El patrón `contradiccion` debería superar a `superlativo` si H2 se cumple.
- **H3 — El fracaso rinde más que el éxito.** Patrón `fracaso_caida` vs `exito_ascenso`. En el género de negocios suele ser la asimetría más marcada.
- **H4 — Existe una duración óptima por canal.** La sección 6 del informe generado la revela. Si la mediana de score sube monótonamente con la duración, el canal tiene audiencia de documental y estás dejando retención sobre la mesa publicando vídeos de 7 minutos.

### 3.4 Estructura narrativa: lo que sí está documentado del género

Sobre la estructura sí hay material publicado. De MagnatesMedia, referencia del formato, se describe un esqueleto recurrente: **alguien quiso algo grande → creció rápido → el mercado se creyó la historia → apareció una debilidad oculta → las consecuencias se volvieron inevitables**; los vídeos se conciben como "mini películas" con principio, medio y final. **[SECUNDARIO]**

Traducido a bloques cronometrados para un vídeo de 10-12 minutos, esto es el molde que yo usaría como punto de partida (y que luego ajustarás con lo que salga de tu propio canal):

| Bloque | Minutos | Función | Regla dura |
|---|---|---|---|
| Hook | 0:00-0:20 | Promesa concreta + agujero | Cifra o imagen imposible antes del segundo 15 |
| Apuesta | 0:20-1:20 | Qué está en juego y por qué te importa | Nombrar a la persona/empresa; nada de contexto histórico todavía |
| Contexto | 1:20-3:00 | El mínimo imprescindible para entender | Si se puede quitar sin romper la trama, fuera |
| Ascenso | 3:00-5:30 | Cómo funcionó, con mecanismo | Aquí va el aprendizaje de negocio real |
| Grieta | 5:30-7:00 | La debilidad que ya estaba ahí | Debe haberse sembrado en el bloque de Ascenso |
| Giro | 7:00-9:00 | El momento en que todo cambia | El pico emocional del vídeo |
| Consecuencia | 9:00-10:30 | Qué pasó después, con números | Datos verificables, con fecha |
| Cierre | 10:30-11:00 | La lección, sin moralina | Una frase. Sin "dale like y suscríbete" largo |

**Cómo se verifica esto contra Éxito Oculto:** cronometra sus 5 outliers y anota en qué minuto cae cada bisagra. Si los tiempos se parecen entre sí, has encontrado su molde. Si no se parecen, su fórmula no está en la estructura sino en la selección de temas — que es una conclusión igual de accionable.

### 3.5 DNA DEL CANAL — cómo se rellena

Esta sección la pediste en términos concretos. Te dejo la plantilla con la regla de evidencia al lado de cada hueco, para que ni tú ni yo la rellenemos con tópicos:

> **"Este canal consigue que una persona quiera hacer clic porque…"**
> → Se responde con: los 3 patrones de título con mayor *lift* y n ≥ 8, + qué tienen en común los thumbnails de los 5 outliers que no tengan los de los 5 peores.
>
> **"Los vídeos suelen funcionar cuando…"**
> → Se responde con: el tema de los outliers (agrupa en 5-6 categorías y mira qué categoría concentra score alto), + el tramo de duración con mayor mediana de score.
>
> **"La estructura narrativa habitual es…"**
> → Se responde con: los tiempos de bisagra cronometrados en los 5 outliers (§3.4).
>
> **"Las thumbnails suelen…"**
> → Se responde con: recuento de elementos, palabras de texto, presencia de cara/logo/cifra y contraste dominante en outliers vs fracasos.
>
> **"El público parece responder especialmente a…"**
> → Se responde con: ratio comentarios/visitas y likes/visitas por categoría temática (ambos están en el CSV). La categoría con mayor ratio de comentarios es la que genera conversación, que no siempre es la de más visitas.

Cada afirmación del DNA tiene que poder apuntar a una celda del CSV. Si no puede, es opinión.

---

## 4. ANÁLISIS DE OTROS CANALES

Mismo bloqueo: no he podido abrir ningún canal, así que **no doy ni una cifra de suscriptores o visualizaciones como si la hubiera comprobado**. Lo que sí tengo es el mapa del género y una lista de referencias que el mercado reconoce, lista para meter en `yt_lab.py compare`.

### 4.1 Referencias del género (inglés)

Canales que las comparativas del sector citan sistemáticamente como el estándar de *business case study* faceless: **MagnatesMedia, Business Casual, Company Man, Modern MBA, ColdFusion, Logically Answered, Wall Street Millennial, How Money Works, Economics Explained y Newsthink**. **[SECUNDARIO]**

Qué está documentado de ellos, y por qué importa para ti:

- El valor del formato **no está en la personalidad sino en investigación, narrativa, edición, locución y packaging**. **[SECUNDARIO]** Es decir: es un formato donde un desconocido con buen criterio puede competir con un canal establecido, a diferencia de los canales de cara.
- MagnatesMedia: "Netflix para emprendedores", vídeos como mini-películas, con la estructura de ascenso-grieta-caída descrita en §3.4. **[SECUNDARIO]**
- El género es de los que **mejor se pagan**: se citan CPM de 10-25 USD para *business case studies*. **[SECUNDARIO]**

Diferencias de formato que sí puedes usar como ejes de posicionamiento **[INFERENCIA]**:

| Eje | Extremo A | Extremo B |
|---|---|---|
| Unidad narrativa | Una empresa por vídeo (Company Man) | Un concepto por vídeo (How Money Works) |
| Tono | Analítico y seco (Modern MBA) | Dramático y cinematográfico (MagnatesMedia) |
| Visual | Gráficos y datos en pantalla | Archivo, b-roll y recreación |
| Ritmo | Pausado, documental | Corte rápido, tensión constante |

Elegir una casilla concreta de esa matriz es más útil que "hacer historias de empresas". Nadie es todo a la vez.

### 4.2 Referencias en español

Lo que he podido confirmar por búsqueda **[SECUNDARIO]**:

- **Emprende Aprendiendo** (Eugenio Oller): el canal de referencia de emprendimiento en español, citado con más de dos millones de suscriptores. Divulgación de negocio, con cara, y un ecosistema de formación detrás.
- **Negocios TV** (José Antonio Vizner): información económica española; alcanzó el millón de suscriptores unos tres años y medio después de su lanzamiento. Formato de plató y directos, no faceless.
- **Forbes México** mantiene una lista de reproducción de "Historias" sobre empresas.
- Aparecen canales genéricos de "historias de empresas y casos de éxito" pero sin ninguno que el mercado reconozca como referencia dominante del formato documental faceless en español.

**[INFERENCIA — y es la observación más importante de esta sección]** En inglés el formato documental de negocios tiene un canon con diez canales consolidados. En español, las referencias que emergen son (a) divulgación con cara y ecosistema de infoproducto, o (b) periodismo económico en plató. **No he encontrado el equivalente hispano consolidado de MagnatesMedia o Company Man.** Eso es exactamente lo que en la sección 6 llamo el hueco principal. Con la salvedad de que la ausencia en un buscador estadounidense no prueba la ausencia en el mercado: **esto hay que verificarlo con datos**, y para eso existe el comando `compare`.

### 4.3 Cómo verificarlo tú en 10 minutos

```bash
export YOUTUBE_API_KEY="AIza..."

# El canon en inglés: te da el techo del formato
python3 tools/yt_lab.py compare @MagnatesMedia @CompanyMan @ModernMBA \
  @ColdFusion @HowMoneyWorks @LogicallyAnswered @BusinessCasual

# El terreno en español: te da tu competencia real
python3 tools/yt_lab.py compare @EmprendeAprendiendo @exitoocultoyt ...
```

Devuelve una tabla con subs, nº de vídeos, visitas totales, **mediana de visitas** (mucho más informativa que la media), **ratio máximo/mediana**, duración mediana y **vídeos/mes de los últimos 12 meses**. Con esa tabla contestas de una sentada:

- ¿El formato tiene techo en español, o es que nadie lo ha hecho bien todavía? → compara la mediana de visitas de los canales españoles contra los ingleses, normalizando por suscriptores.
- ¿Cuál es la cadencia sostenible real? → vídeos/mes de los canales que funcionan. Si el canon publica 2-4 al mes, publicar 12 no es ambición, es una apuesta contra la evidencia.
- ¿Qué duración es la norma del género? → duración mediana.
- ¿Qué canales viven de un solo viral? → ratio máximo/mediana alto = formato inestable; bajo = formato fiable.

Después, un `channel` completo sobre los 3 que más se parezcan a lo que quieres hacer. Eso son ~40 unidades de cuota de las 10.000 diarias.

---

## 5. SUBNICHOS DE NEGOCIOS DETECTADOS

No hay ranking. Hay ejes de decisión. Los cinco que de verdad discriminan **[INFERENCIA, construida sobre los datos de secciones anteriores]**:

1. **Tamaño del catálogo** — ¿cuántos vídeos puedes hacer antes de repetirte? Por debajo de 100 no es un canal, es una serie.
2. **Coste de investigación por vídeo** — horas tuyas, que es tu recurso escaso.
3. **Saturación** — cuánta competencia y, sobre todo, cuánta competencia *buena*.
4. **Riesgo de política de contenido no auténtico** — cuanto más plantillable es un formato, más se parece a lo que YouTube persigue.
5. **Densidad de aprendizaje** — cuánto sabes de negocio después de 50 vídeos. Lo pusiste como requisito explícito, así que va como eje de primer orden.

| Subnicho | Catálogo | Investigación | Saturación (ES) | Riesgo política | Aprendizaje | Nota |
|---|---|---|---|---|---|---|
| Ascenso y caída de empresas | Alto | **Alta** (4-8 h) | Media | Bajo | **Muy alto** | El formato con más techo y más coste |
| Empresas que quebraron | Medio-alto | Alta | Media | Bajo | Muy alto | Hueco de curiosidad natural en el título |
| **Cómo gana dinero X** | **Muy alto** | Media (2-4 h) | Media-baja | Medio | Alto | El más escalable; el que peor envejece si lo plantillas |
| Negocios raros / absurdamente rentables | Alto | Media | **Baja** | Medio | Medio | CTR alto, prestigio bajo; buen combustible de crecimiento |
| Modelos de negocio (concepto) | Muy alto | Media | Baja | **Alto** | **Muy alto** | Riesgo: sin historia concreta se vuelve genérico rápido |
| Marketing y campañas legendarias | Medio | Media | Media | Bajo | Alto | Muy visual: el archivo publicitario es b-roll gratis |
| IA y empresas | Alto y creciendo | **Baja-media** | Media y subiendo rápido | **Muy alto** | Alto | Caduca en meses; es donde más "slop" se está produciendo |
| Economía con historias | Alto | Alta | Media | Bajo | Muy alto | Difícil de diferenciar; techo altísimo |
| SaaS / negocios de internet | Medio | Baja | Baja | Medio | Alto | Audiencia pequeña pero de altísimo valor para patrocinio |
| Emprendedores (biografías) | Alto | Media | **Muy alta** | **Alto** | Medio | El más saturado y el más plantillado. Evitar como eje central |
| Productos que fracasaron | Medio-alto | Media | Baja | Bajo | Alto | Muy visual, casos acotados, ideal para empezar |
| E-commerce / dropshipping | Alto | Baja | **Muy alta** | **Muy alto** | Bajo | Nicho contaminado por contenido promocional. Evitar |

**Tres lecturas que te ahorro:**

- **La correlación incómoda:** los subnichos con menos coste de investigación (IA, emprendedores, e-commerce) son exactamente los que tienen más saturación y más riesgo de política. No es casualidad: son los baratos de producir, así que todo el mundo los produce. **El coste de investigación es tu foso defensivo.** **[INFERENCIA]**
- **"Cómo gana dinero X" es la mejor relación escalabilidad/aprendizaje**, pero es también el formato más fácil de convertir en plantilla — y la plantilla es lo que la política de contenido no auténtico penaliza. Se salva si cada vídeo contiene una cifra o un mecanismo que no está en los tres primeros resultados de búsqueda.
- **"IA y empresas" es la trampa del momento.** Máxima demanda y mínimo coste aparente, pero es donde se concentra la producción masiva de IA, y el contenido caduca en meses. Funciona como **sección** dentro de un canal más amplio, no como canal. **[INFERENCIA]**

---

## 6. OPORTUNIDADES

### A. Temas recurrentes (el suelo del género)

Aparecen una y otra vez en los canales que funcionan **[SECUNDARIO + INFERENCIA]**:

- El monopolio invisible: la empresa que domina un sector que nadie mira.
- El modelo de negocio contraintuitivo: pierde dinero en el producto y gana en otro sitio.
- El fraude y su desmontaje.
- La decisión que mató a la empresa, contada como error evitable.
- La guerra entre dos competidores.
- El producto que fracasó y acabó siendo la base de otro éxito.

### B. Temas saturados (no empieces aquí)

**[INFERENCIA]** El canon anglosajón está agotado y traducido al español hasta el desgaste: Theranos, WeWork, FTX, Enron, Blockbuster vs Netflix, Nokia, Kodak, BlackBerry, Juicero, Quibi, Bernie Madoff, la biografía de Musk / Jobs / Bezos.

Regla práctica: si el caso tiene documental en Netflix o HBO, tu vídeo compite contra un documental de un millón de dólares **y** contra los 200 vídeos que ya se hicieron. Solo tiene sentido si aportas un ángulo que nadie ha usado (un dato de cuentas anuales, un actor secundario, la consecuencia a 10 años).

### C. Gaps: demanda con poca oferta

**Este es el núcleo del informe.** **[INFERENCIA, a contrastar con `yt_lab.py`]**

1. **Empresas hispanas con historia de calidad anglosajona.** Mercadona (y el modelo de "jefe" que estudian en escuelas de negocio de medio mundo), Inditex/Zara (logística como ventaja competitiva), Mercado Libre, Grupo Bimbo, Cemex, Glovo, Cabify, Hawkers, Freixenet, Telepizza, Rappi, Cupra, Chupa Chups. Son casos con cuentas anuales públicas, prensa económica abundante y cero saturación en formato documental. **Y tienen una ventaja de distribución: nadie más puede hacerlos bien sin hablar español.**
2. **La economía de lo aburrido.** Palés, contenedores, tornillos, seguros de reaseguro, certificación, calibración industrial, gases industriales, ascensores. Sectores gigantes, invisibles y con márgenes extraordinarios. Ángulo natural: *"Esta empresa que no conoces factura más que…"*.
3. **Empresas familiares y medianas europeas** (los *hidden champions* alemanes, italianos y españoles): líderes mundiales en nichos que nadie sabe nombrar.
4. **La trastienda operativa.** Cómo funciona de verdad la cadena de suministro de algo cotidiano. Alta densidad de aprendizaje y visualmente agradecido.
5. **Fracasos recientes y locales**, no los de hace 20 años en EE. UU. Tienen menos cobertura y más relevancia emocional para tu audiencia.

### D. Nuevas oportunidades (y una advertencia seria)

Lo que está creciendo **[SECUNDARIO]**:

- La demanda de servicios de vídeo y animación relacionados con IA creció un 278% interanual, y la creación de contenido es la línea donde más rápido crece la demanda de IA en 2026.
- Los canales generados o asistidos por IA aparecen ya con regularidad en las pestañas de tendencias de varios países.
- El tiempo de visualización en formato largo (10+ minutos) vuelve a crecer, y los canales que combinan Shorts para descubrimiento con formato largo para retención y monetización rinden mejor que los que solo hacen Shorts.
- Pocos vídeos buenos superan a muchos mediocres; la plataforma prioriza profundidad de engagement sobre volumen.

**La advertencia, que afecta al diseño entero del proyecto:**

El 15 de julio de 2025 YouTube actualizó su política de "contenido repetitivo" y la renombró **"contenido no auténtico"**, aclarando que cubre contenido repetitivo o producido en masa. Desmonetiza vídeos que siguen una plantilla con poca variación, se reproducen a escala y no tienen aportación real de autor. Desde entonces se reportan canales con ingresos de decenas de miles de dólares al mes desmonetizados de un día para otro, y 16 canales con 4.700 millones de visitas acumuladas terminados de forma permanente. **[SECUNDARIO — no he podido leer el texto oficial de la política desde este entorno; verifícalo en la ayuda de YouTube antes de tomar decisiones grandes.]**

Lo que **no** dice la política: los canales faceless no están prohibidos ni desmonetizados como categoría. Los canales faceless con guion original, curación real y estilo consistente siguen siendo plenamente monetizables. **[SECUNDARIO]** La línea que YouTube traza es **IA como aumento vs IA como sustitución**.

**Consecuencia de diseño, y es la razón de ser de todo el pipeline de la sección 8:** cada vídeo tiene que contener algo que no podría existir sin ti. En este formato eso significa, como mínimo: (1) una fuente primaria consultada por ti — cuentas anuales, hemeroteca, informe regulatorio; (2) una tesis o un ángulo que no esté en los tres primeros resultados de búsqueda del tema; (3) tu pase de guion, no el borrador del modelo. Es el control de calidad de la etapa 14 del pipeline y es innegociable.

---

## 7. STACK DE IA

**Advertencia de precios:** los precios de herramientas de IA cambian cada pocas semanas. Todo lo que viene está fechado a septiembre de 2026 y buena parte procede de comparativas de terceros, no de las páginas oficiales. **Verifica en la web del proveedor antes de comprometer dinero.** Lo marco como **[SECUNDARIO]** salvo donde indique otra cosa.

### 7.1 Investigación

| Herramienta | Qué hace | API | Coste | Veredicto |
|---|---|---|---|---|
| **YouTube Data API v3** | Datos oficiales: canales, vídeos, estadísticas | Sí | **Gratis**, 10.000 unidades/día **[OBSERVADO]** | **La base de todo.** Ya envuelta en `tools/yt_lab.py` |
| **`yt_lab.py`** (este repo) | Radiografía, outliers, cruce patrón→rendimiento | — | 0 | Escrito y probado. Sustituye a la capa de pago para lo esencial |
| vidIQ | Buscador de outliers con filtros (score, views/hora, tamaño de canal, formato) | Limitada | Boost ~25-39 USD/mes **[SECUNDARIO]** | Útil para descubrir canales que no conoces. Su valor está en el descubrimiento, no en el análisis |
| ViewStats | Outlier Score y analítica cruzada de canales | No | Pro 49,99 USD/mes **[SECUNDARIO]** | Solapa mucho con `yt_lab.py`. Yo esperaría |
| **skill `last30days`** | Investiga un tema en Reddit + X de los últimos 30 días y pondera por engagement | Skill de Claude Code | Gratis (repo público `kellyoconor/last30days-skills`) **[SECUNDARIO]** | **Muy recomendable.** Cubre el punto ciego de `yt_lab.py`: lo que la gente está discutiendo *ahora* y que todavía no tiene vídeos |
| **Marketing Skills** (Corey Haines) | ~34 skills de SEO, copywriting, CRO, estrategia de contenidos | Skill de Claude Code | Gratis (`coreyhaines31/marketingskills`) **[SECUNDARIO]** | Su fuerte es la profundidad estratégica. Para títulos y descripciones, mejor que prompts improvisados |
| yt-dlp | Metadatos + transcripciones sin clave de API | CLI | Gratis | Para transcripciones, que la Data API no da. No lo escales: te bloquean la IP **[SECUNDARIO]** |
| Google Trends / Google News | Validación de demanda fuera de YouTube | Parcial | Gratis | Imprescindible para distinguir moda pasajera de demanda estable |

**Qué automatizar:** descarga y scoring, semanal. **Qué revisas tú:** qué outlier merece un vídeo. Un outlier te dice que un tema funcionó *en otro canal*; no te dice que tú puedas aportar algo.

### 7.2 Guion

| Herramienta | Precio (por millón de tokens) | Para qué |
|---|---|---|
| **Claude Opus 5** | 5 USD entrada / 25 USD salida **[SECUNDARIO]** | Guion final, estructura narrativa, control de calidad. Es donde la calidad se nota |
| **Gemini 3.1 Pro** | ~2 / 12 USD **[SECUNDARIO]** | Ventana larga: digerir informes anuales y hemeroteca de golpe |
| GPT-5.6 Terra | ~2 / 12 USD **[SECUNDARIO]** | Alternativa; útil como segunda opinión en verificación |

**Coste real por guion:** un vídeo de 10-12 minutos son ~1.500-1.800 palabras en español. Con 50.000 tokens de contexto de investigación y ~2.500 de salida, sale por **0,30-0,40 USD** con Opus 5. Con tres iteraciones, **~1 USD**. El guion es lo más barato del pipeline y lo que más determina el resultado: no ahorres aquí.

**Cómo usarlos — reparto de tareas entre modelos (más importante que cuál elijas):**
1. Gemini digiere las fuentes y extrae los hechos con cita y fecha → tabla de hechos.
2. Claude convierte la tabla de hechos en estructura narrativa (§3.4).
3. Claude escribe el guion desde la estructura.
4. **Un modelo distinto** verifica el guion contra la tabla de hechos y marca cada afirmación sin respaldo. Un modelo no es buen auditor de su propio texto.
5. **Tú** haces el pase final. Innegociable (§6D).

### 7.3 Voz

| Herramienta | Coste | Español | API | Notas |
|---|---|---|---|---|
| **ElevenLabs** (v3 / Multilingual v2) | **0,10 USD / 1.000 caracteres** vía API **[SECUNDARIO]** | Sí, 70+ idiomas al mismo precio **[SECUNDARIO]** | Sí | El estándar en naturalidad y clonación. Había una promoción del 50% activa: confirma el precio de lista |
| ElevenLabs Flash/Turbo | 0,05 USD / 1.000 car. **[SECUNDARIO]** | Sí | Sí | La mitad de precio. Pensado para latencia baja, no para narración |
| Cartesia Sonic | Variable | Sí | Sí | Líder en latencia (~90 ms). Diseñado para conversación en tiempo real, no para narración larga **[SECUNDARIO]** |
| Hume | Variable | Sí | Sí | Líder en emoción **[SECUNDARIO]** |
| MiniMax | Variable | Sí | Sí | Buen rendimiento en contenido largo **[SECUNDARIO]** |
| Gemini TTS | Incluido en Google AI | Sí | Sí | La opción barata si ya estás en Google |

**Nota:** evita PlayHT — las comparativas de 2026 recomiendan excluirlo y migrar. **[SECUNDARIO]**

**Coste real por vídeo:** 1.600 palabras en español ≈ 9.500 caracteres ≈ **0,95 USD** a precio de API. Con retomas, **~1,50 USD**. Si haces 4 vídeos al mes, un plan de suscripción de ~22 USD/mes con 100.000 caracteres sale parecido y es más predecible.

**Lo que decide la calidad no es el modelo, es el guion:** marca las pausas, los énfasis y el ritmo en el texto. Un guion escrito para ser leído en voz alta suena humano en cualquier motor; uno escrito para ser leído con los ojos suena a robot en todos.

### 7.4 Vídeo generativo

El panorama se ha movido mucho. A septiembre de 2026 **[SECUNDARIO en todo el bloque]**:

| Modelo | Precio aprox. | Fuerte en | Aviso |
|---|---|---|---|
| **Kling 3.0** | ~0,084-0,10 USD/s con audio | 4K nativo, 60 fps, clips de 15 s, modo storyboard multi-plano con audio sincronizado entre cortes | La mejor relación precio/calidad ahora mismo |
| **Google Veo 3.1** | desde 0,15 USD/s (modo rápido) | Mejor seguimiento de instrucciones, audio nativo, 4K; el único que genera diálogo sincronizado a 48 kHz | El techo de calidad, al doble de precio |
| Seedance 2.0 (ByteDance) | Variable | Primer puesto en Artificial Analysis (feb. 2026) | Muy nuevo |
| Runway Gen-4.5 | Unlimited ~76 USD/mes | Mejor superficie de control (motion brushes, consistencia de escena) | Ha caído del top 10 de calidad; sigue siendo el mejor si necesitas control fino |
| **Sora 2** | — | — | **Obsoleto desde el 26/04/2026; su API cierra el 24/09/2026 — en cuatro días. No construyas nada sobre ella.** |
| **fal.ai** | 0,05-0,40 USD/s | Agregador con 600+ modelos tras una sola API | **La decisión correcta para un pipeline:** te desacopla del modelo concreto, que es lo que más rápido cambia |

**Decisión de arquitectura, y es la que más dinero te ahorra:** en un documental de negocios **la mayor parte de los planos no necesitan vídeo generativo**. Gráficos, cifras animadas, mapas, archivo, capturas y fotografía fija con movimiento de cámara (Ken Burns) cubren perfectamente el 70-80% de un vídeo de este género, cuestan una fracción y envejecen mejor. Reserva el vídeo IA para 10-20 planos de alto impacto: la apertura, el giro y los momentos de tensión. **[INFERENCIA]**

A 0,09 USD/s, 20 planos de 5 s = **9 USD**. Generar los 12 minutos enteros con IA = ~65 USD y un resultado peor.

### 7.5 Imagen y b-roll

| Vía | Coste | Notas |
|---|---|---|
| Flux.2 Pro | ~0,03 USD/imagen **[SECUNDARIO]** | Buen equilibrio calidad/precio |
| GPT Image 1.5 / Imagen 4 / Ideogram 3.0 | 0,005-0,06 USD/imagen **[SECUNDARIO]** | Ideogram destaca en texto dentro de la imagen |
| Flux Schnell | ~0,003 USD/imagen **[SECUNDARIO]** | Para volumen y bocetos |
| **Storyblocks** | 21 USD/mes (Essentials) o 30 USD/mes (todo, con música y SFX) **[SECUNDARIO]** | Descargas ilimitadas HD/4K/8K. **La mejor compra del stack para este género** |
| Artgrid | ~200 USD/año **[SECUNDARIO]** | Licencia universal que sigue vigente al cancelar |
| **Pexels** | Gratis | Uso comercial sin atribución. Empieza aquí |
| **Higgsfield** (ya conectado en tu entorno vía MCP) | Plus 49 USD/mes = 1.000 créditos (~600 imágenes Nano Banana Pro o ~200 vídeos Kling 3.0); Ultra 129 USD/mes = 3.000 créditos **[OBSERVADO — consultado en tu sesión]** | Agrega modelos de imagen, vídeo y voz tras una sola interfaz, con generación por lotes. Si vas a usar bastante vídeo IA, sale más barato que pagar por segundo |

**Verifica siempre la licencia comercial** antes de usar material en un canal monetizado. **[SECUNDARIO]**

### 7.6 Edición y render

Aquí es donde se decide si tienes un pipeline o una cadena de copiar y pegar.

| Herramienta | Coste | API | Para qué |
|---|---|---|---|
| **Remotion** | Open source (licencia de empresa según uso) | Es código React | **Vídeo programático de verdad.** Composiciones como componentes, animación por fotograma, reutilizables. Ideal para gráficos de datos, transiciones de marca, cartelas. Curva de aprendizaje real |
| **HyperFrames** (HeyGen) | Open source; render en la nube de HeyGen **[SECUNDARIO]** | Sí | Convierte HTML/CSS/JS en MP4. Pensado para que un agente (Claude Code, Cursor) cree, previsualice y renderice vídeo desde un prompt. Más rápido de arrancar que Remotion; menos control fino |
| JSON2Video | 49 USD/mes (200 min FHD, TTS incluido); Hobby 16,95 USD/mes **[SECUNDARIO]** | Sí | Envías un JSON con la estructura y devuelve el vídeo montado. La vía más rápida a un pipeline funcionando |
| Shotstack | 49 USD/mes (200 min 720p); 20 min gratis **[SECUNDARIO]** | Sí | Alternativa madura |
| Creatomate | desde 54 USD/mes **[SECUNDARIO]** | Sí | Subió precios en 2026 |
| **FFmpeg** | Gratis | CLI | El pegamento de todo: concatenar, mezclar audio, quemar subtítulos, normalizar volumen. Insustituible |
| DaVinci Resolve | Gratis / 295 USD Studio | Scripting Python | Para el pase manual cuando el vídeo lo merece |
| CapCut | Freemium | No real | Rápido para thumbnails y Shorts; no automatizable |

**Recomendación:** **HyperFrames o JSON2Video para arrancar, Remotion cuando el formato se estabilice.** Razón: hasta que no tengas 10 vídeos no sabes cuál es tu plantilla, y construir un sistema Remotion sobre una plantilla que va a cambiar es trabajo tirado. Cuando la plantilla se asiente, Remotion te da control total y coste marginal cero. **[INFERENCIA]**

### 7.7 Thumbnails

| Herramienta | Notas |
|---|---|
| Nano Banana Pro / GPT Image / Ideogram 3.0 | Generación base. Ideogram si hay texto en la imagen **[SECUNDARIO]** |
| Pikzels | Orientado a rendimiento: testear variantes y ver cuál gana **[SECUNDARIO]** |
| Miraflow | Entrenado sobre thumbnails de alto rendimiento 2025-2026 **[SECUNDARIO]** |
| Photopea / Figma / GIMP | El retoque final: contraste, recorte, texto. Siempre hace falta |

Lo que las comparativas coinciden en señalar **[SECUNDARIO]**: **una cara, una emoción, grande**; **tres a cinco palabras máximo** de texto, funcionando como gancho y no como descripción.

Para un canal faceless de negocios sin caras, el equivalente es: **un objeto o logo reconocible + una cifra + una señal de conflicto** (flecha roja, grieta, tachado). Genera 5 variantes por vídeo (≈0,25 USD) y quédate con una. **[INFERENCIA]**

Cuidado: **tú no puedes medir el CTR de un thumbnail antes de publicar**, y ninguna herramienta lo predice de forma fiable. Lo que sí puedes hacer es cambiarlo a las 48 horas si el CTR real es bajo.

### 7.8 Análisis de vídeo (el eslabón que falta)

Claude **no admite vídeo de forma nativa** a día de hoy. **[SECUNDARIO]** La vía práctica es extraer fotogramas + transcripción y pasárselos como imágenes y texto:

- **`claude-video-vision`** (plugin de Claude Code): extrae fotogramas, detecta cambios de escena, transcribe audio y se lo entrega a Claude. **[SECUNDARIO]**
- Alternativa manual: `yt-dlp` para la transcripción + `ffmpeg -vf fps=1/5` para un fotograma cada 5 segundos.

**Para qué lo quieres, en concreto:** es lo que convierte la sección 2.5 (capa cualitativa) de "ver vídeos a mano durante tres horas" en "analizar los 5 outliers de un competidor en 20 minutos". Detecta dónde están las bisagras narrativas, qué tipo de material visual se usa en cada bloque y cada cuántos segundos hay un corte.

### 7.9 Orquestación

| Herramienta | Precio | Veredicto |
|---|---|---|
| **n8n** | **Gratis autoalojado** (sin límite de ejecuciones, pagas el VPS ~5-10 €/mes); cloud desde 20 USD/mes **[SECUNDARIO]** | **La elección correcta.** Factura por ejecución (un flujo entero = 1 unidad), no por paso. En un flujo de 10 pasos × 10.000 ejecuciones/mes ahorra un 80-90% frente a Zapier **[SECUNDARIO]** |
| Make | desde 9 USD/mes **[SECUNDARIO]** | Buena lógica visual con ramificaciones, ~60% más barato que Zapier |
| Zapier | desde 19,99 USD/mes; Professional 10.000 tareas ~129 USD/mes anual **[SECUNDARIO]** | El más caro y el más fácil. No lo necesitas |
| **Scripts propios + cron** | Gratis | Para lo que ya es código (`yt_lab.py`, FFmpeg, render). No metas en n8n lo que un script hace mejor |

**Criterio:** n8n para lo que cruza servicios (API de YouTube → hoja → notificación → generación → subida). Scripts para lo que es transformación de datos o proceso de medios. La trampa clásica es montar en un orquestador visual lo que debería ser un script de 40 líneas.

---

## 8. PIPELINE DE AUTOMATIZACIÓN

Leyenda: 🤖 automatizable · 👁️ requiere tu criterio · ⚙️ automatizable tras estabilizar el formato

| # | Etapa | Herramienta | Qué hace | Auto | Tu papel | Coste/vídeo | API |
|---|---|---|---|---|---|---|---|
| 1 | **Trend detection** | `yt_lab.py` + `last30days` + Google Trends | Barre competidores semanalmente, puntúa outliers, cruza con lo que se discute en Reddit/X | 🤖 | Leer el informe semanal (10 min) | ~0 | Sí |
| 2 | **Competitor analysis** | `yt_lab.py compare` + `claude-video-vision` | Métricas de canal + disección de los 5 outliers ajenos | 🤖 | Decidir qué canales vigilar | ~0 | Sí |
| 3 | **Idea generation** | Claude Opus 5 + `prompts/01` | Convierte outliers y gaps en 20 ideas con ángulo propio | 🤖 | **Elegir. Esta es la decisión más importante del pipeline** | ~0,10 $ | Sí |
| 4 | **Topic validation** | `yt_lab.py` + Trends | ¿Existe demanda? ¿está saturado? ¿hay ángulo libre? | 🤖 | Descartar lo que no puedes hacer mejor que lo existente | ~0 | Sí |
| 5 | **Research** | Gemini 3.1 Pro + fuentes primarias + `prompts/02` | Digiere cuentas anuales, hemeroteca e informes → tabla de hechos con cita y fecha | ⚙️ | **Abrir al menos una fuente primaria tú.** Es el requisito de autenticidad (§6D) | ~0,30 $ | Sí |
| 6 | **Script** | Claude Opus 5 + `prompts/03` | Estructura narrativa → guion marcado para locución | 🤖 borrador | **Pase final tuyo. Innegociable** | ~1 $ | Sí |
| 7 | **Storyboard** | Claude + `prompts/04` | Trocea el guion en 60-90 planos con prompt visual y tipo de fuente para cada uno | 🤖 | Revisar los 10 planos clave | ~0,20 $ | Sí |
| 8 | **Voice** | ElevenLabs (o Higgsfield) | Locución desde el guion marcado | 🤖 | Escuchar entera una vez. Siempre | ~1,50 $ | Sí |
| 9 | **Visuals** | fal.ai (Kling/Veo) + Flux + Storyblocks + Higgsfield | Genera/descarga los planos del storyboard | 🤖 | Sustituir los que no funcionen (suele ser el 10-20%) | ~10-15 $ | Sí |
| 10 | **Editing** | HyperFrames o JSON2Video → Remotion + FFmpeg | Monta sobre la pista de voz, cartelas, subtítulos, música, normalización | ⚙️ | Revisar el montaje entero antes de exportar | ~0-2 $ | Sí |
| 11 | **Thumbnail** | Nano Banana Pro / Ideogram + retoque | 5 variantes | 🤖 | **Eliges tú.** Ninguna herramienta predice el CTR | ~0,25 $ | Sí |
| 12 | **Title** | Claude + Marketing Skills + `prompts/05` | 15 títulos según los patrones validados en TU canal | 🤖 | Eliges tú | ~0,05 $ | Sí |
| 13 | **Quality control** | Claude (modelo distinto) + `prompts/06` | Verifica cada afirmación contra la tabla de hechos; marca lo no respaldado | 🤖 | **Resolver cada marca antes de publicar** | ~0,30 $ | Sí |
| 14 | **Autenticidad** | Tú | Checklist §6D: fuente primaria + ángulo propio + pase de guion | 👁️ | **Solo tú. Es lo que protege la monetización** | 0 | No |
| 15 | **YouTube** | YouTube Data API (`videos.insert`) | Sube, programa, metadatos, miniatura, capítulos | 🤖 | Aprobar antes de publicar | 0 (1.600 unidades de cuota) | Sí |
| 16 | **Analytics** | YouTube Analytics API (tu canal) | CTR, retención, fuentes de tráfico, curva de abandono | 🤖 | Leerlo. De verdad | 0 | Sí |
| 17 | **Learning loop** | `yt_lab.py` sobre tu propio canal + Claude | Recalcula tus outliers, actualiza qué patrones funcionan **en tu canal** | 🤖 | Decidir qué cambias en el siguiente | ~0,10 $ | Sí |
| 18 | **Next video** | → etapa 1 con el aprendizaje incorporado | | | | | |

### 8.1 El bucle de aprendizaje, que es lo que distingue esto de "vídeos generados con IA"

La etapa 17 es la que pediste y la que casi nadie implementa. En concreto:

1. Pasa `yt_lab.py channel @tucanal` cada mes. Tus propios outliers son mejor señal que los de cualquier competidor, porque están medidos sobre tu audiencia.
2. Cruza el **CTR real** (de YouTube Analytics, que sí tienes en tu canal) con los patrones de título de cada vídeo. Después de 15-20 vídeos, sabrás qué patrones funcionan **contigo**, no en general.
3. Mira la **curva de retención** de tus 3 mejores y tus 3 peores. Los puntos de caída se corresponden con bloques concretos del guion (§3.4). Si todos caen en el mismo minuto, tienes un problema de estructura, no de tema.
4. Alimenta esas conclusiones al prompt de guion como reglas duras. Los prompts en `prompts/` tienen una sección **"Reglas aprendidas de mi canal"** justamente para eso: es el único sitio del sistema que debe cambiar con el tiempo.

### 8.2 Orden de construcción (no lo montes todo a la vez)

**[INFERENCIA]** El error clásico es construir el pipeline entero antes del primer vídeo, descubrir que el formato no funciona y tirar el sistema.

- **Vídeos 1-3: casi todo a mano.** Solo etapas 1-6 automatizadas (investigación, ideas, guion). Monta en DaVinci. Objetivo: descubrir tu formato, no ser eficiente.
- **Vídeos 4-10: automatiza voz, visuales y montaje** (8-10), porque ya sabes qué plantilla necesitas.
- **Vídeos 11-20: automatiza publicación y analítica** (15-17), y monta el bucle de aprendizaje.
- **A partir de 20: Remotion** sobre una plantilla ya estable, y n8n como orquestador de todo.

---

## 9. COSTE ESTIMADO

### 9.1 Coste variable por vídeo (10-12 minutos, español)

| Partida | Cálculo | Coste |
|---|---|---|
| Investigación (Gemini) | ~150k tokens entrada | 0,30 $ |
| Guion (Claude Opus 5, 3 iteraciones) | ~50k entrada + 2,5k salida ×3 | 1,00 $ |
| Storyboard + títulos + QC | | 0,55 $ |
| Voz (ElevenLabs API, con retomas) | ~9.500 caracteres + margen | 1,50 $ |
| Imágenes (60-80 planos fijos) | ×0,03 $ | 2,00 $ |
| Vídeo IA (15-20 planos × 5 s, Kling 3.0) | ~90 s × 0,09 $ | 8,00 $ |
| Stock y música | prorrateo de suscripción | 2,00 $ |
| Thumbnails (5 variantes) | | 0,25 $ |
| Render | FFmpeg local | 0 $ |
| **Total variable** | | **≈ 15,60 $** (~14 €) |

Con render en servicio de pago (JSON2Video/Shotstack) en vez de local, súmale 2-4 $. Rango realista: **15-25 USD por vídeo**.

### 9.2 Coste fijo mensual, en tres escenarios

| Partida | Arranque | Serio | Escalado |
|---|---|---|---|
| ElevenLabs | — (API pago por uso) | 22 $ (Creator) | 99 $ (Pro) |
| Stock (Storyblocks) | 0 $ (Pexels) | 30 $ | 30 $ |
| Investigación (vidIQ) | 0 $ (`yt_lab.py`) | 25 $ | 49 $ (+ViewStats) |
| Render (JSON2Video) | 0 $ (FFmpeg local) | 17 $ (Hobby) | 49 $ |
| VPS (n8n autoalojado) | 0 $ | 6 $ | 12 $ |
| Higgsfield (opcional) | 0 $ | 0 $ | 49-129 $ |
| **Fijo/mes** | **0 $** | **100 $** | **288-368 $** |
| Vídeos/mes | 2 | 4 | 8 |
| Variable | 31 $ | 62 $ | 160 $ |
| **TOTAL/mes** | **≈ 31 $ (29 €)** | **≈ 162 $ (150 €)** | **≈ 448-528 $ (415-490 €)** |

### 9.3 Lo que hay que entender de estos números

- **El escenario de arranque cuesta 29 €/mes.** No hay barrera económica de entrada. La barrera es tu tiempo.
- **Tu coste real es el tiempo.** Con el pipeline maduro, un vídeo son ~3-5 horas tuyas (elegir tema, leer fuentes primarias, pase de guion, elegir thumbnail, revisar montaje). A 4 vídeos/mes son 12-20 horas. **Ese es el número que decide si esto es sostenible, no los 150 €.**
- **Rentabilidad, con cautela:** a RPM de 2-3,30 USD en español **[SECUNDARIO]**, cubrir 150 $/mes requiere ~50.000-75.000 visualizaciones monetizadas al mes. Alcanzable en este género, pero **no en los primeros meses**. Planifica 6-12 meses a pérdidas.
- **La palanca económica más grande no es el coste, es el idioma.** El mismo vídeo en inglés se paga 3-5x más **[SECUNDARIO]**. Doblar el canal a inglés con ElevenLabs cuesta ~1,50 $ extra por vídeo. Si funciona en español, es la ampliación de margen más barata que existe. (Ojo: un canal en inglés no es "el mismo canal traducido" — el guion, las referencias y los ejemplos cambian.)

---

## 10. PROPUESTAS DE CANAL

Cinco direcciones. **Sin ranking**, como pediste. Están ordenadas de mayor a menor coste de producción, para que la comparación sea legible. Los títulos son ejemplos para que veas el tono, no un calendario editorial.

---

### Propuesta A — «Imperios» · Ascenso y caída, escala global

**Concepto.** El formato canónico del género, en español y bien hecho: una empresa por vídeo, contada como película, con la estructura ascenso → grieta → giro → consecuencia. Mercado global, casos conocidos y desconocidos.

**Público.** 22-45, interés en negocios y economía, consumidor de documental. Gran solapamiento con la audiencia que ya ve MagnatesMedia y Company Man en inglés.

**Tipos de vídeo.** Caída de un gigante · fraude desmontado · guerra entre competidores · la decisión que lo cambió todo.

**Ejemplos de títulos.**
- «Facturaba 4.000 millones al año. Tardó 11 meses en desaparecer»
- «El error contable que hundió a una empresa de 90 años»
- «Dos hermanos, una empresa, y la pelea que creó a su mayor competidor»

**Producción.** Alta dificultad. 6-8 h de investigación + 3-4 h tuyas de guion y revisión. Necesita archivo real, lo que complica el b-roll.
**Potencial.** El techo más alto del género y el mayor riesgo de comparación directa con el canon anglosajón, que lleva años de ventaja.
**Qué aprenderías.** Muchísimo: contabilidad, estructuras de capital, gobierno corporativo, dinámica competitiva. Es la opción de máxima densidad de aprendizaje.
**Herramientas.** Todo el stack. Es la propuesta que más vídeo IA y archivo necesita.

---

### Propuesta B — «Hecho aquí» · Historias de empresas hispanas

**Concepto.** El mismo formato documental, aplicado a empresas españolas y latinoamericanas. Mercadona, Inditex, Mercado Libre, Bimbo, Glovo, Cabify, Hawkers, Freixenet, Cemex, Rappi, Cupra, Chupa Chups.

**Público.** El mismo que A, pero con un vínculo emocional que A no puede tener: son empresas cuyos productos la audiencia usa cada semana.

**Tipos de vídeo.** Cómo funciona por dentro una empresa que conoces · la empresa española que domina un sector mundial · el fracaso que nadie recuerda · la guerra por un mercado local.

**Ejemplos de títulos.**
- «Por qué Mercadona no tiene marcas (y gana más por ello)»
- «La empresa española que fabrica una de cada tres piezas de tu coche»
- «Vendió 60 millones de gafas de sol desde un piso. Luego se rompió»

**Producción.** Media-alta. 4-6 h de investigación. **Ventaja decisiva: las fuentes primarias están en español y son accesibles** — cuentas anuales en el Registro Mercantil, hemeroteca de *Expansión*, *Cinco Días*, *El Economista*, informes de la CNMV. Eso reduce el coste de investigación **y** cumple de forma natural el requisito de autenticidad de §6D.
**Potencial.** **Es el hueco más claro que he identificado** (§6C). Y tiene un foso defensivo que ningún canal anglosajón puede cruzar: hace falta hablar español y entender el mercado. **[INFERENCIA — contrástalo con `yt_lab.py compare` antes de comprometerte]**
**Qué aprenderías.** Lo mismo que A, más algo más valioso para ti: cómo funcionan de verdad los mercados en los que podrías operar.
**Herramientas.** Como A, pero con menos vídeo IA: hay más archivo y material fotográfico disponible.

---

### Propuesta C — «¿Cómo gana dinero…?» · Modelos de negocio

**Concepto.** Un mecanismo económico por vídeo. No la historia de la empresa: **cómo entra el dinero exactamente**. Gimnasios low cost, aerolíneas, supermercados, aparcamientos, seguros, apps gratis, restaurantes, autopistas.

**Público.** Más amplio que A y B, y más joven. Curiosidad general, no necesariamente interés previo en negocios.

**Tipos de vídeo.** El negocio real detrás de un producto · por qué X es gratis · dónde está el margen de verdad · la economía de un objeto cotidiano.

**Ejemplos de títulos.**
- «Los gimnasios de 20 € ganan dinero porque no vas»
- «Ryanair no gana dinero con los billetes»
- «El negocio de las máquinas de vending es mejor de lo que parece»

**Producción.** **La más barata y la más escalable.** 2-4 h de investigación. Casi todo se resuelve con gráficos y animación de datos, que es exactamente para lo que sirve Remotion. Catálogo prácticamente infinito.
**Potencial.** Crecimiento más rápido (temas más accesibles), techo por vídeo más bajo que A/B.
**Riesgo real.** Es el formato más fácil de convertir en plantilla, y la plantilla es lo que la política de contenido no auténtico penaliza (§6D). Se salva **solo** si cada vídeo aporta una cifra o un mecanismo que no está en los tres primeros resultados de búsqueda.
**Qué aprenderías.** Estructura de costes, márgenes, economía unitaria. Es la formación más directamente aplicable si algún día montas algo.
**Herramientas.** Stack ligero: mucho Remotion/HyperFrames, poco vídeo generativo. **La más barata de operar con diferencia.**

---

### Propuesta D — «Negocios imposibles» · Lo raro y lo absurdamente rentable

**Concepto.** Negocios que no deberían existir y facturan millones. Alquiler de cabras, hielo para whisky, plañideras profesionales, bancos de semillas, empresas de una sola persona con márgenes del 90%.

**Público.** El más amplio de los cinco. Entretenimiento con sustancia; capta gente que no busca contenido de negocios.

**Ejemplos de títulos.**
- «Cobra 400 € por hora por dormir. Es un negocio legal»
- «Vende tierra en botes. Factura 2 millones»
- «El hombre que alquila amigos»

**Producción.** Media-baja (2-3 h). Muy visual, muy agradecido para vídeo IA porque las escenas son absurdas por definición y la imperfección generativa no molesta.
**Potencial.** **El mejor CTR de los cinco** y el crecimiento inicial más rápido. Techo de autoridad más bajo: cuesta más convertirlo en un canal que la gente respete.
**Qué aprenderías.** Menos que en A, B o C. Aprendes creatividad de modelo de negocio y detección de nichos; no aprendes finanzas.
**Herramientas.** Stack ligero + más vídeo IA.

---

### Propuesta E — «La IA y el dinero» · Cómo la IA está cambiando industrias concretas

**Concepto.** No hype ni "las 10 mejores herramientas". Casos concretos con números: qué industria se está reconfigurando, quién gana, quién pierde, qué queda del modelo anterior.

**Público.** El más valioso económicamente: profesionales, emprendedores, técnicos. CPM alto y patrocinadores obvios.

**Ejemplos de títulos.**
- «La IA no mató a esta industria. Le cambió el dueño»
- «Cuánto cuesta realmente sustituir a un equipo de 20 personas»
- «Esta empresa despidió al 40% y facturó más. Un año después, esto es lo que pasó»

**Producción.** Baja-media en investigación, **pero exige rigor extremo** porque tu audiencia sabe del tema y te va a corregir en comentarios.
**Potencial.** Máxima demanda **actual**. **Y máximo riesgo:** es donde más contenido generado por IA se está publicando, por lo que es donde más escrutinio hay; y el contenido caduca en meses, así que no acumulas catálogo evergreen. Tu biblioteca no trabaja para ti mientras duermes.
**Qué aprenderías.** Mucho y muy aplicable a lo que ya estás haciendo, pero con fecha de caducidad.
**Herramientas.** Stack ligero. La skill `last30days` pasa de "recomendable" a **imprescindible**: sin ella llegas tarde a todo.

---

### 10.1 Comparación directa

| | A · Imperios | B · Hecho aquí | C · Cómo gana dinero | D · Imposibles | E · IA y dinero |
|---|---|---|---|---|---|
| Coste investigación | Muy alto | Alto | Medio | Bajo | Bajo |
| Coste producción | Alto | Medio-alto | **Bajo** | Bajo | Bajo |
| Tamaño de catálogo | Alto | Alto | **Muy alto** | Alto | Medio |
| Saturación en español | Media | **Baja** | Media-baja | **Baja** | Media, subiendo |
| Ventaja defendible | Baja | **Muy alta** | Media | Media | **Muy baja** |
| Riesgo política §6D | Bajo | **Muy bajo** | Medio | Medio | **Alto** |
| Velocidad de crecimiento | Lenta | Media | Media-rápida | **Rápida** | Rápida |
| Techo por vídeo | **Muy alto** | Alto | Medio | Medio-alto | Medio |
| Valor evergreen | Alto | **Muy alto** | **Muy alto** | Alto | **Bajo** |
| CPM esperado | Alto | Alto | Medio | Medio | **Muy alto** |
| **Lo que aprendes** | **Máximo** | **Máximo** | Alto y aplicable | Medio | Alto pero perecedero |
| Horas tuyas/vídeo | 8-12 | 6-9 | 4-6 | 3-5 | 4-6 |

### 10.2 Dos observaciones antes de que decidas

**No son excluyentes.** B y C combinan especialmente bien: mismo público, misma promesa de fondo ("cómo funciona el dinero de verdad"), distinto coste de producción. Un canal que alterna un documental caro (B) con dos explicativos baratos (C) al mes sostiene la cadencia sin quemarte. Lo que **no** funciona es mezclar D o E con A o B: el tono y la expectativa de la audiencia son incompatibles, y acabas con un canal que el algoritmo no sabe a quién recomendar. **[INFERENCIA]**

**El eje que de verdad decide.** Si tu prioridad real es **aprender de negocios** (lo dijiste al principio), A y B ganan por bastante, y B además es donde está el hueco de mercado. Si tu prioridad es **validar rápido que puedes hacer esto**, C y D llegan antes a los primeros resultados. La decisión honesta es cuál de esas dos cosas quieres primero.

---

## 11. PRÓXIMOS PASOS

De «tengo una idea» a «tengo mi primer vídeo listo para publicar». Cuatro semanas, con el trabajo de cada una.

### Semana 1 — Datos reales (6-8 h)

1. **Clave de la YouTube Data API v3** (5 min, gratis). §2.2.
2. **Radiografía de Éxito Oculto:** `python3 tools/yt_lab.py channel @exitoocultoyt`. Esto cierra las secciones 2 y 3 de este informe con datos de verdad.
3. **Tabla comparativa** de 8-10 canales del género en inglés y en español: `yt_lab.py compare`. §4.3.
4. **Capa cualitativa:** los 5 outliers y los 5 peores de los 2 canales más parecidos a lo que quieres hacer. Cronometra las bisagras y compara thumbnails. §2.2 paso 5.
5. **Entregable de la semana:** el DNA rellenado (§3.5) con una celda del CSV detrás de cada afirmación.

> Si me pasas el CSV que genera la herramienta, te hago el análisis completo y el DNA en una sesión.

### Semana 2 — Decisión y validación (4-6 h)

6. **Elige dirección de canal** (§10) con los datos de la semana 1 delante, no con la intuición de hoy.
7. **Escribe 30 ideas** con `prompts/01-idea-generation.md`. Si no llegas a 30 cómodamente, el nicho es demasiado estrecho: es la prueba de estrés más barata que existe.
8. **Valida las 10 mejores:** ¿hay demanda? ¿hay fuente primaria accesible? ¿tienes un ángulo que no esté ya en los tres primeros resultados?
9. **Elige el vídeo 1.** Criterio: que sea **el segundo o tercer mejor tema**, no el mejor. Tu primer vídeo va a ser el peor que hagas; no quemes tu mejor idea aprendiendo a montar.
10. **Decide nombre, identidad visual y plantilla de thumbnail.** Una decisión, no una exploración de tres semanas.

### Semana 3 — Producción del vídeo 1, casi a mano (10-14 h)

11. **Investigación con fuentes primarias** (`prompts/02`). Abre al menos una tú: cuentas anuales, hemeroteca, informe regulatorio. Es el requisito de §6D y no se delega.
12. **Guion** (`prompts/03`) sobre la estructura de §3.4, y **pase final tuyo**, en voz alta. Si tropiezas al leerlo, el motor de voz también.
13. **Storyboard** (`prompts/04`): 60-90 planos con su fuente (IA, stock, gráfico, archivo).
14. **Voz** con ElevenLabs. Escúchala entera.
15. **Visuales** y **montaje en DaVinci, a mano.** Sí, a mano, esta vez. Es la única forma de descubrir qué plantilla necesitas automatizar después. Automatizar antes de saber qué automatizas es la forma más común de perder dos meses.
16. **5 thumbnails** (`prompts/05`), eliges uno.
17. **Control de calidad** (`prompts/06`) con un modelo distinto al que escribió el guion. Resuelve **cada** marca antes de publicar.

### Semana 4 — Publicar y montar el bucle (6-8 h)

18. **Publica.** Fija el título y el thumbnail elegidos; revisa el CTR a las 48 h y cámbialo si está por debajo del 4%.
19. **Vídeos 2 y 3** con el mismo proceso manual. Con tres vídeos sabrás qué es repetitivo; con uno, no.
20. **Automatiza solo lo que hayas repetido tres veces.** Empieza por la voz y el troceado del storyboard (§8.2).
21. **Monta el bucle de aprendizaje** (§8.1): `yt_lab.py channel @tucanal` mensual + lectura de retención y CTR + reglas nuevas en la sección «Reglas aprendidas de mi canal» de los prompts.

### La regla que resume todo

**Automatiza lo que ya has hecho tres veces a mano. Nunca antes.** Todo lo demás de este documento es detalle de implementación.

---

## Anexo — Contenido del repositorio

```
youtube-lab/
├── INFORME.md                  este documento
├── README.md                   arranque rápido
├── tools/
│   └── yt_lab.py               radiografía de canales, outliers, patrones (probado)
├── prompts/
│   ├── 01-idea-generation.md   outliers + gaps → ideas con ángulo propio
│   ├── 02-research-brief.md    fuentes primarias → tabla de hechos con cita
│   ├── 03-guion.md             tabla de hechos → guion marcado para locución
│   ├── 04-storyboard.md        guion → 60-90 planos con prompt visual
│   ├── 05-titulos-thumbnails.md  títulos y conceptos de thumbnail
│   └── 06-quality-control.md   verificación factual + autenticidad §6D
└── data/raw/                   volcados, CSV e informes generados (ignorado por git)
```

---

## Fuentes consultadas

Todas por buscador web, entre el 20 y el 21 de septiembre de 2026. No he podido abrir las páginas, solo leer los resúmenes que devuelve el buscador, así que **trata las cifras concretas como orientativas hasta verificarlas en la fuente oficial**.

**Política y plataforma:** [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en) · [ScaleLab, AI content crackdown 2026](https://scalelab.com/en/why-youtube-is-cracking-down-on-ai-generated-content-in-2026) · [Flocker, Inauthentic Content enforcement](https://flocker.tv/posts/youtube-inauthentic-content-ai-enforcement/) · [Mensaje del CEO de YouTube para 2026](https://blog.youtube/intl/es-419/inside-youtube/el-futuro-de-youtube-2026/) · [vidIQ, YouTube trends 2026](https://vidiq.com/blog/post/future-youtube-trends/) · [Mediacube, YouTube Trends 2026](https://mediacube.io/en-US/blog/youtube-trends-2026)

**API y datos:** [Elfsight, guía YouTube Data API v3](https://elfsight.com/blog/youtube-data-api-v3-limits-operations-resources-methods-etc/) · [OutlierKit, cuota de la API](https://outlierkit.com/resources/youtube-api-quota/) · [getphyllo, límites 2026](https://www.getphyllo.com/post/youtube-api-limits-how-to-calculate-api-usage-cost-and-fix-exceeded-api-quota) · [Scrapfly, cómo se extraen datos de YouTube](https://scrapfly.io/blog/posts/how-to-scrape-youtube) · [CreatorCrawl, alternativas a la API](https://creatorcrawl.com/blog/youtube-data-api-alternatives/)

**Género y competencia:** [Overseeros, canales faceless de business case study](https://www.overseeros.com/blog/top-faceless-business-case-study-youtube-channels) · [OutlierKit, nichos faceless y CPM](https://outlierkit.com/resources/faceless-youtube-channels/) · [BBVA, canales de YouTube para emprendedores](https://www.bbva.com/es/innovacion/youtube-para-emprendedores-siete-canales-para-inspirarse-y-hacer-crecer-un-negocio/) · [okdiario, Negocios TV alcanza el millón](https://okdiario.com/economia/negocios-tv-alcanza-primer-millon-suscriptores-youtube-3-anos-medio-despues-lanzamiento-12311167) · [MagnatesMedia](https://www.youtube.com/@MagnatesMedia)

**Retención y CPM:** [prepublish, benchmarks de retención 2026](https://prepublish.ai/blog/youtube-retention-benchmarks-2026) · [prepublish, los primeros 30 segundos](https://prepublish.ai/guides/first-30-seconds) · [Lenos, CPM y RPM 2026](https://www.lenostube.com/en/youtube-cpm-rpm-rates/) · [TubeAnalytics, benchmark España](https://www.tubeanalytics.net/pt/benchmarks/spain) · [Upgrowth, CPM por país](https://upgrowth.in/youtube-cpm-by-country-global-comparison-2026/)

**Voz:** [ElevenLabs, precios de API](https://elevenlabs.io/pricing/api) · [BIGVU, ElevenLabs 2026](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/) · [SurePrompts, comparativa de modelos de voz 2026](https://sureprompts.com/blog/voice-generation-models-compared-2026) · [Inworld, alternativas a ElevenLabs](https://inworld.ai/resources/elevenlabs-alternatives)

**Vídeo e imagen:** [teamday, mejores modelos de vídeo 2026](https://www.teamday.ai/blog/best-ai-video-models-2026) · [evolink, precios de APIs de vídeo](https://evolink.ai/blog/best-ai-video-generation-models-2026-pricing-guide) · [tech-insider, Veo 3.1 vs Sora 2 vs Kling](https://tech-insider.org/best-ai-video-generator-2026/) · [buildmvpfast, precios de imagen](https://www.buildmvpfast.com/api-costs/ai-image) · [SiliconFlow, modelos de imagen más baratos](https://www.siliconflow.com/articles/the-cheapest-image-gen-models)

**Edición y stock:** [Wireflow, plataformas de vídeo programático](https://www.wireflow.ai/blog/best-programmatic-video-generation-platform-tools-in-2026) · [samautomation, Shotstack vs Creatomate vs JSON2Video](https://samautomation.work/blog/best-video-apis-developers-2026/) · [HyperFrames x HeyGen](https://help.heygen.com/en/articles/15001510-hyperframes-x-heygen) · [HyperFrames, guía de prompting](https://hyperframes.heygen.com/prompting/overview) · [checkthat, precios de Storyblocks](https://checkthat.ai/brands/storyblocks/pricing)

**Automatización y skills:** [Parseur, n8n vs Zapier vs Make](https://parseur.com/blog/zapier-n8n-make) · [Cipher Projects, comparativa 2026](https://www.cipherprojects.com/blog/posts/n8n-vs-zapier-vs-make-automation-comparison/) · [kellyoconor/last30days-skills](https://github.com/kellyoconor/last30days-skills) · [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · [TripleDart, cómo Corey Haines usa Claude Skills](https://www.tripledart.com/playbooks/corey-haines-claude-skills-marketing) · [jordanrendric/claude-video-vision](https://github.com/jordanrendric/claude-video-vision) · [Claude Platform Docs, Vision](https://platform.claude.com/docs/en/build-with-claude/vision)

**Modelos de lenguaje:** [Claude Platform Docs, precios](https://platform.claude.com/docs/en/about-claude/pricing) · [BenchLM, precios de la API de Claude](https://benchlm.ai/anthropic/api-pricing) · [IntuitionLabs, comparativa de precios de APIs](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025)

**Higgsfield:** consultado directamente en tu sesión vía su conector MCP el 20/09/2026. **[OBSERVADO]**

**Thumbnails:** [CapCut, generadores de thumbnails 2026](https://www.capcut.com/resource/best-7-ai-thumbnail-generators-for-youtube) · [Hooksnap, 8 herramientas probadas](https://www.hooksnap.io/blog/best-ai-thumbnail-makers-2026)
