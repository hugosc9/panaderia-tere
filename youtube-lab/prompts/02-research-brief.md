# 02 · Investigación → tabla de hechos

**Entrada:** una idea validada.
**Salida:** tabla de hechos con cita y fecha. Es el contrato del resto del pipeline: **nada entra en el guion si no está aquí.**
**Modelo:** Gemini 3.1 Pro (ventana larga) o Claude con las fuentes pegadas.

---

Vas a preparar el material factual para un vídeo documental sobre [TEMA].

## Fuentes que te doy

```
[Pegar: cuentas anuales, artículos de hemeroteca, informes regulatorios,
transcripciones, comunicados. AL MENOS UNA la has abierto tú: es el
requisito de autenticidad y no se delega.]
```

## Tarea

Construye una **tabla de hechos**:

| # | Hecho | Cifra exacta | Fecha | Fuente | Confianza |
|---|---|---|---|---|---|

Reglas de la tabla:

1. **Una fila = una afirmación verificable.** Nada de "la empresa creció mucho": «facturación de 412 M€ en 2019 frente a 180 M€ en 2016».
2. **Confianza:** `primaria` (documento oficial de la empresa o del regulador) · `secundaria` (prensa económica) · `terciaria` (blog, wiki) · `disputada` (las fuentes no coinciden — indica las dos versiones).
3. **Si no encuentras una cifra, escribe `NO ENCONTRADO`.** No estimes, no interpoles, no redondees hacia lo dramático. Un hueco declarado es información; una cifra inventada destruye el canal.
4. Marca las cifras que **cambian según la fuente**. Suelen ser las más citadas y las más equivocadas.
5. Señala qué está **traducido o convertido** (moneda, cifras ajustadas a inflación) y con qué tipo de cambio y fecha.

## Además, entrega

- **Cronología** en 10-15 hitos con fecha.
- **Los 3 huecos de información** más importantes que no has podido cerrar, y dónde habría que buscar.
- **Los 2 datos contraintuitivos** más fuertes. Normalmente uno de ellos es el hook.
- **Riesgo legal:** ¿hay acusaciones, causas abiertas, personas vivas señaladas? ¿Qué hay que formular como «según la sentencia / según la demanda» y no como hecho?
