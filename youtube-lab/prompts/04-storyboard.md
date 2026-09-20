# 04 · Storyboard

**Entrada:** guion aprobado (03).
**Salida:** 60-90 planos con fuente y prompt.
**Modelo:** Claude Opus 5.

---

Trocea este guion en planos para un documental de negocios faceless.

```
[Pegar guion aprobado]
```

## Salida: una tabla

| # | Timecode | Texto locutado | Tipo de plano | Fuente | Prompt / búsqueda | Duración |
|---|---|---|---|---|---|---|

**Tipos de fuente y cuándo usar cada una** (esto es lo que controla el coste):

| Fuente | Cuándo | Coste |
|---|---|---|
| `GRAFICO` | Cifras, evolución, comparación, cuota de mercado | ~0 (Remotion/HyperFrames) |
| `STOCK` | Ambiente genérico: oficinas, ciudad, fábrica, manos | ~0 (suscripción) |
| `ARCHIVO` | Material real de la empresa: anuncios, logos, productos, prensa | ~0 |
| `IMAGEN_IA` | Escena concreta que no existe en stock, sin movimiento | 0,03 $ |
| `VIDEO_IA` | **Solo alto impacto:** apertura, giro, momentos de tensión | 0,45 $ (5 s) |
| `CAPTURA` | Web, app, documento, titular de prensa | 0 |

## Reglas

1. **Máximo 20 planos `VIDEO_IA` en todo el vídeo.** Es el 80% del coste variable. Si necesitas más, el guion está mal troceado.
2. **Ningún plano dura más de 8 segundos.** Si el texto lo requiere, divide en dos ángulos.
3. **Los gráficos son la columna vertebral de este género, no el relleno.** Cada cifra importante del guion merece su plano de datos.
4. **Prompts de imagen/vídeo en inglés**, específicos, con estilo, iluminación y encuadre. Mantén **un mismo estilo visual** en todo el vídeo (indícalo una vez al principio y refiérete a él).
5. En `ARCHIVO`, indica **qué buscar y dónde** (hemeroteca, web archivada, informe anual), y **avisa del riesgo de derechos**.
6. Marca con ⭐ los **10 planos clave** — los que voy a revisar yo uno a uno.

## Entrega también

- Recuento por tipo de fuente y **coste estimado del vídeo**.
- **Guía de estilo visual** en 3 líneas (paleta, iluminación, tipo de encuadre) para que los planos generados no parezcan de cinco vídeos distintos.
