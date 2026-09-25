# Storyboard — Scalpers (v2: identidad de robot-presentador)

**Sustituye a la versión documental fotorrealista anterior.** El canal cambia de identidad visual: el robot mascota (`referencia-avatar-robot.png`, guardado en esta carpeta) pasa a ser el presentador recurrente en todos los vídeos, no solo en los gráficos.

Esto reposiciona el canal de "documental de archivo" a "explicador con mascota anfitriona" — mismo guion, mismo rigor factual, estética distinta. Detalle importante: **mezclar un personaje ilustrado con fondos fotorrealistas suele verse mal.** Por eso este storyboard cambia también los fondos: de "recreaciones fotorrealistas de 2007" a **fondos limpios de estudio + gráficos de datos**, con el robot como hilo conductor. Es más coherente visualmente y, siendo justos, más barato de producir.

## Cómo generarlo en Whisk

1. Sube `referencia-avatar-robot.png` como imagen de referencia en Whisk (no describas el robot de memoria — usa la imagen como base para que el estilo y el diseño se mantengan idénticos en las 15 escenas).
2. Para cada escena, el prompt indica **qué pose usar de la hoja de referencia** + el fondo/contexto de esa escena.
3. Guarda cada imagen como `plano-01.png`, `plano-02.png`, etc.

---

| # | Timecode | Beat del guion | Pose (de la hoja de referencia) | Fondo / contexto |
|---|---|---|---|---|
| 1 | 0:00-0:08 | "Dos amigos fracasan con el lavadero" | Brazos cruzados, seria | Fondo oscuro liso, sin elementos — el robot solo, gesto serio |
| 2 | 0:08-0:15 | "Concurso de acreedores. Liquidación." | *(sin robot — GRAFICO puro)* | Texto en pantalla: "2007 · Concurso de acreedores" |
| 3 | 0:15-0:20 | "Hoy factura 220 millones" | **Señalando gráfico ascendente** (la de la esquina inferior derecha) | Fondo con el gráfico de barras subiendo detrás, cifra "220.000.000 €" animada |
| 4 | 0:20-0:45 | Presentación de los fundadores | Saludando con la mano | Fondo limpio, cinco tarjetas de perfil (silueta+nombre+profesión) apareciendo a su lado |
| 5 | 0:45-1:20 | Capital inicial: 100.000€ entre cinco | Sosteniendo la moneda dorada | Fondo con el número "100.000 €" grande |
| 6 | 1:20-1:50 | 2007, un año antes de la crisis | Brazos cruzados | Línea de tiempo horizontal: "2007 — Scalpers" ... "2008 — Lehman Brothers", el robot junto a la línea |
| 7 | 1:50-2:20 | Segunda tienda en Madrid | Caminando con maletín | Fondo con mapa de España, dos puntos (Sevilla → Madrid) encendiéndose |
| 8 | 2:20-2:50 | La idea de la sastrería a medida | Con la bombilla de idea | Fondo limpio, icono de aguja/hilo apareciendo junto a él |
| 9 | 2:50-3:20 | El nombre "Scalpers" y la calavera | *(sin robot — GRAFICO puro)* | Animación tipográfica: "SCALPERS" letra a letra, silueta de calavera minimalista |
| 10 | 3:20-4:00 | 370 tiendas, 11 países | Señalando el gráfico ascendente | Mapa mundial con 11 países iluminándose + contador "370" |
| 11 | 4:00-4:30 | Scalpers Woman, 27% de la facturación | Con la tablet | Gráfico de dona (27%/73%) apareciendo junto a él |
| 12 | 4:30-5:00 | Scalpers LAB, canal digital 800.000 usuarios | Con el portátil, sentado en el escritorio | Icono de móvil + contador ascendente "800.000" |
| 13 | 5:00-5:30 | Grieta: 2017, cinco mercados a la vez | Pensando, con la interrogación | Mapa mundial con 5 puntos encendiéndose a la vez en países distintos |
| 14 | 5:30-6:20 | "No funciona..." — la cita del fundador | *(sin robot — GRAFICO puro)* | Cita en pantalla, estilo subtítulo grande, atribución "— Borja Vázquez" |
| 15 | 6:20-6:40 | Pararon: cerraron tiendas | Brazos cruzados, seria | Los 5 puntos del mapa apagándose uno a uno |
| 16 | 6:40-8:40 | Giro: estrategia "mancha de aceite" | Con la checklist (enfoque metódico) | **El plano más importante.** Animación de un punto en un mapa expandiéndose como una mancha, el robot con el clipboard al lado supervisando el proceso |
| 17 | 8:40-10:00 | Consecuencia: 110M→152M→200M→220M | Señalando el gráfico ascendente (repetir pose 3, distinto fondo) | Gráfico de barras con las 4 cifras apareciendo una a una |
| 18 | 10:00-10:30 | Cierre reflexivo | Sentado leyendo en el sillón | Fondo limpio, atenuado, cierre tranquilo |

## Prompts listos (Whisk, con la imagen de referencia subida)

**Escena 1:**
```
Using the attached robot character reference, generate it in the "arms
crossed" pose against a plain dark studio background, serious neutral
expression, no other elements, clean 3D render, soft studio lighting,
consistent with reference style, 8K
```

**Escena 3:**
```
Using the attached robot character reference, generate it in the "pointing
at rising bar chart" pose, with a large ascending bar chart graphic behind
it and the text "220.000.000 €" prominently displayed, clean studio
background, consistent with reference style, 8K
```

**Escena 4:**
```
Using the attached robot character reference, generate it in the "waving
hello" pose against a plain light studio background, with empty space to
the left for five profile cards to be added in post, consistent with
reference style, 8K
```

*(el resto de escenas siguen el mismo patrón: pose de la hoja + fondo descrito en la tabla — genera los 16 restantes con la misma estructura de prompt, cambiando solo pose y fondo)*

## Nota sobre el cambio de identidad

Esto **retira** el ángulo de diferenciación de "documental fotorrealista sin explotar" que identificamos en el informe general (§6C) frente al formato de mascota ilustrada, que ya usan Éxito Oculto y buena parte de los canales de finanzas en shorts. No es un error — es una decisión de identidad de marca distinta, y es tu decisión. Solo que conviene tenerlo explícito: el canal deja de competir en el hueco que habíamos detectado como menos saturado, y pasa a competir en un formato más poblado, con un asset visual genérico que otros canales probablemente ya usan. Si más adelante quieres un diseño de personaje propio (no un pack genérico), es el momento de plantearlo — antes de publicar el primer vídeo con esta cara, no después.

## Upgrade futuro: HappyHorse 1.0 (Alibaba)

Evaluado el 25/09/2026, no usado en este vídeo por decisión del usuario (coste cero por ahora). Es un modelo de vídeo real y de primer nivel (nº1 en Artificial Analysis en texto-a-vídeo e imagen-a-vídeo, abril 2026) con una función que resolvería justo el problema de este storyboard: **identidad de personaje persistente entre planos** — en vez de generar cada pose del robot por separado en Whisk (sin garantía de que salga idéntico cada vez), HappyHorse mantiene el mismo personaje coherente a lo largo de una secuencia multi-plano.

**No es gratis:** ~0,80 $/segundo vía fal.ai (partner de API oficial), 0,57-4,20 $ por vídeo según duración. **Aviso:** varios dominios (`happyhorsee.io`, `hppyhorse.com`, `happy-horse.art` y similares) se anuncian como "gratis e ilimitado" aprovechando el lanzamiento — patrón típico de webs clon/SEO-farm cuando un modelo se vuelve viral. Si en el futuro se usa, que sea vía fal.ai o Alibaba Cloud Bailian directamente, nunca por una de esas webs genéricas.

Candidato a revisar cuando el canal tenga presupuesto: sustituiría los planos con el robot (13 de las 18 escenas) por una o dos generaciones multi-plano de HappyHorse, con consistencia garantizada, en vez de 13 generaciones sueltas en Whisk.
