# Cesar Reparaciones — datos verificados

Comprobado el 21/09/2026.

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Cesar Reparaciones | ficha de Google |
| Móvil (WhatsApp) | 646 42 44 80 | ficha de Google |
| Dirección | **Calle de Simancas, 3** | reverse de Nominatim, que devuelve el portal |
| Dónde exactamente | **Dentro de la Galería de Alimentación** | el reverse identifica el edificio del nº 3 como «Galería de Alimentación» |
| Barrio | Almenara · Tetuán · 28029 Madrid | Nominatim |
| Coordenadas | 40.4655716, −3.6948814 | ficha de Google |
| Web propia | **No tiene** | `tiene_web.py` + búsqueda: ni una mención |

## El gancho: está dentro de una galería

No es un local a pie de calle: es **un puesto dentro de una galería de
alimentación**, de las de toda la vida. Eso cambia dos cosas:

1. **Está donde la gente ya va.** No hace falta que nadie se desvíe: se deja la
   tostadora al ir a por el pan. Ninguna cadena de reparación puede decir eso.
2. **Y por eso mismo cuesta encontrarlo en Google.** Una galería no tiene
   escaparate a la calle. Quien busca «arreglar lavadora Tetuán» no lo ve, y
   una página con la dirección, el portal y el horario lo arregla.

## Lo que no se declara

- **Nota y opiniones:** no aparecen en ninguna fuente. Sin `aggregateRating`.
- **Qué arregla exactamente, precios y horario:** no publicados. Inventados y
  marcados.
- Ojo: en las búsquedas sale una «Electrodomésticos Bravo Murillo SL» cuyo
  administrador se llama César. **No se ha dado por hecho que sea el mismo.**
  No se menciona en la página ni en el mensaje.

## La idea central de la demo

En electrodomésticos la primera pregunta no es «¿cuánto tardas?» —eso era en
móviles, ver `reparaciones-el-experto`—. Es **«¿compensa arreglarlo o me compro
uno nuevo?»**.

Un taller que conteste eso por escrito, y que diga **cuándo NO compensa**, gana
la confianza antes de que nadie descuelgue el teléfono. Por eso la página lleva
la regla del 50% y una tabla con lo que cuesta cada arreglo al lado de lo que
cuesta el aparato nuevo.
