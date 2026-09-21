# Storyboard — Scalpers

18 planos para ~10:30 min. Fuente por plano según el reparto de §4 del `PIPELINE-GRATIS.md`: la mayoría gráfico/genérico, IA solo en escenas sin rostro identificable, archivo real solo donde el derecho de uso esté confirmado.

**Regla de oro de este storyboard, y de cualquier vídeo de este canal sobre gente real:** ningún fundador (Borja Vázquez, Alfonso Vivancos, Rafael Medina...) se genera con IA haciéndose pasar por él. O es una foto de archivo con derechos confirmados, o es un plano sin rostro (manos, escaparate, silueta a contraluz, texto en pantalla).

**Sobre el archivo real (fotos de prensa):** las fotos que aparecen en los artículos de modaes.com, elespanol.com, eleconomista.es **son propiedad de esos medios**, no de libre uso. Antes de usar cualquiera de esas imágenes en el vídeo:
1. Comprueba si Scalpers tiene un kit de prensa propio con fotos de uso editorial permitido (buscar "Scalpers prensa" / "Scalpers press kit" en su web oficial).
2. Si no lo hay, **no uses la foto del artículo** — sustitúyela por un `GRAFICO` (cita en pantalla con la fuente, o un mapa/gráfico) en vez de arriesgarte a un reclamo de derechos.
3. La foto de la fachada de una tienda Scalpers tomada por un cliente cualquiera y subida a Google Maps/redes con licencia abierta sí es más segura, pero verifícalo igualmente antes de usarla.

---

| # | Timecode | Texto locutado (resumen) | Fuente | Detalle / prompt |
|---|---|---|---|---|
| 1 | 0:00-0:08 | "Dos amigos fracasan con un lavadero de coches" | `IMAGEN_IA` | Ver prompt A |
| 2 | 0:08-0:15 | "Concurso de acreedores. Liquidación." | `GRAFICO` | Texto en pantalla: "2007 · Concurso de acreedores" sobre fondo oscuro, tipografía documental |
| 3 | 0:15-0:20 | "Hoy factura 220 millones al año" | `GRAFICO` | Cifra grande animada: "220.000.000 €" con contraste fuerte |
| 4 | 0:20-0:45 | Sevilla 2007, se conocieron en un MBA | `IMAGEN_IA` | Ver prompt B |
| 5 | 0:45-1:20 | Perfiles: abogado / ingeniero, cinco socios, capital 100.000€ | `GRAFICO` | Tarjetas tipo "ficha de personaje" sin foto real: iniciales o silueta + profesión + año, cinco tarjetas en fila |
| 6 | 1:20-1:50 | 2007, a un año de la crisis financiera | `IMAGEN_IA` | Ver prompt C |
| 7 | 1:50-2:20 | Moda masculina, mercado pequeño, competencia multiplicándose | `GRAFICO` | Gráfico de barras simple: "Moda masculina vs. moda femenina" (proporción de mercado, con nota "ilustrativo" si no hay cifra exacta) |
| 8 | 2:20-2:50 | Alberto Artacho y la sastrería de camisas a medida | `IMAGEN_IA` | Ver prompt D |
| 9 | 2:50-3:20 | El nombre "Scalpers", término bursátil, calavera como ruptura | `GRAFICO` | Animación tipográfica: la palabra "SCALPERS" apareciendo letra a letra sobre fondo negro, silueta de calavera minimalista |
| 10 | 3:20-4:00 | De sastrería de barrio a marca internacional | `ARCHIVO*` | *Solo si hay derechos confirmados. Si no: `GRAFICO` — mapa de España con puntos apareciendo progresivamente |
| 11 | 4:00-4:30 | 370 puntos de venta, 11 países, córners en El Corte Inglés | `GRAFICO` | Mapa mundial con 11 países iluminándose + contador "370" |
| 12 | 4:30-5:00 | Scalpers Woman, 27% de la facturación | `GRAFICO` | Gráfico circular (dona): 27% Woman / 73% resto |
| 13 | 5:00-5:20 | Scalpers LAB, cosmética genderless | `IMAGEN_IA` | Ver prompt E |
| 14 | 5:20-5:30 | Canal digital: 800.000 usuarios, 23% de ventas | `GRAFICO` | Icono de móvil + contador ascendente "800.000" |
| 15 | 5:30-6:20 | **Grieta (cerrada con hecho real):** 2017, cinco mercados a la vez, no funcionó | `GRAFICO` | **Ya no es una escena genérica de "dificultad" — anímalo literal:** mapa mundial con 5 puntos pequeños encendiéndose a la vez en países distintos, y apagándose uno a uno mientras suena la cita del fundador. Mucho más fuerte que una imagen IA ambigua |
| 15b | 6:20-6:40 | La cita del fundador sobre equipos pequeños | `GRAFICO` | Cita en pantalla, estilo subtítulo grande: la frase completa de la fila #29, con atribución "— Borja Vázquez" |
| 16 | 6:40-6:50 | Pararon: cerraron tiendas, descartaron operaciones | `IMAGEN_IA` | Ver prompt F (ajustado: ahora es "cierre deliberado", no "incertidumbre difusa") |
| 17 | 6:50-8:40 | Giro: estrategia de la "mancha de aceite" | `GRAFICO` | **El plano más importante de generar bien.** Animación conceptual: un punto en un mapa que se expande como una mancha que crece despacio, cubriendo el territorio — literal, visual, fácil de entender en 3 segundos |
| 18 | 8:40-10:00 | Consecuencia: 110M → 152M → 200M → 220M, expansión 2024-2025 | `GRAFICO` | Gráfico de barras ascendente con las 4 cifras, animado, cada barra apareciendo en su momento del guion |
| 19 | 10:00-10:30 | Cierre: 88% en España, el capítulo que falta por escribir | `IMAGEN_IA` | Ver prompt G |

## Prompts de imagen (para Whisk, dentro de tu Google AI Plus — coste 0€ adicional)

Genéricos, sin rostros identificables de personas reales, en inglés (mejor rendimiento en los modelos de imagen), terminando con el estilo documental que ya usamos en el resto del canal:

**Prompt A — Escena 1, el fracaso del lavadero:**
```
Abandoned automated car wash facility, empty and closed, rusted equipment,
overcast grey sky, a single "CERRADO" (closed) sign on the door, dramatic
low-angle shot, muted desaturated colors, cinematic documentary,
photorealistic, dramatic lighting, ultra-detailed, 8K
```

**Prompt B — Escena 4, Sevilla 2007:**
```
Seville Spain street scene in 2007, warm golden hour light, historic
Andalusian architecture, two blurred silhouettes of young men walking and
talking, shallow depth of field, nostalgic tone, cinematic documentary,
photorealistic, dramatic lighting, ultra-detailed, 8K
```

**Prompt C — Escena 6, contexto de crisis:**
```
Empty Spanish shopping street in 2008, closed shop shutters, "SE ALQUILA"
(for rent) signs, grey overcast atmosphere, economic recession mood,
cinematic documentary, photorealistic, dramatic lighting, ultra-detailed, 8K
```

**Prompt D — Escena 8, la sastrería:**
```
Close-up of hands measuring fabric for a bespoke shirt, tailor's workshop,
scissors and thread on a wooden table, warm lamp lighting, no visible face,
cinematic documentary, photorealistic, dramatic lighting, ultra-detailed, 8K
```

**Prompt E — Escena 13, Scalpers LAB:**
```
Minimalist genderless cosmetics product line on a dark reflective surface,
matte black packaging with a small skull emblem, studio lighting, high-end
product photography, cinematic documentary, photorealistic, dramatic
lighting, ultra-detailed, 8K
```

**Prompt F — Escena 16, el cierre deliberado de tiendas:**
```
A retail storefront with the shutters halfway down at dusk, a "CLOSING
DOWN" paper sign taped to the glass, empty street, a sense of deliberate
retreat rather than failure, cinematic documentary, photorealistic,
dramatic lighting, ultra-detailed, 8K
```

**Prompt G — Escena 18, cierre:**
```
Modern flagship fashion store entrance at night, warm interior light
spilling onto a European city street, closed for the day, sense of quiet
ambition, cinematic documentary, photorealistic, dramatic lighting,
ultra-detailed, 8K
```

## Cómo generarlas, en la práctica

1. App Gemini → **Whisk**.
2. Pega cada prompt tal cual (en inglés funciona mejor).
3. Guarda cada imagen como `plano-01.png`, `plano-04.png`, etc. — el número de escena, no el de orden de generación, para que cuadre con Remotion en el montaje.
4. Son 7 imágenes IA de las 18 — el resto (10 gráficos + 1 archivo condicional) no consume tu cuota de Whisk/Flow, los hace Remotion.
5. Aquí no he podido generarlas por ti: Higgsfield (conectado en esta sesión) está a 0 créditos, y Whisk no tiene conector — vive solo dentro de la app de Gemini. Son 5-10 minutos de tu parte.
