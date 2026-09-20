# Fitness Feda Madrid — datos verificados

Comprobado el 20/09/2026 antes de escribir la demo.

## Lo que está verificado

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre de la ficha | Fitness Feda Madrid | `prospectos.json` (ficha de Google) |
| Teléfono | 697 17 71 16 (móvil) | ficha de Google |
| Coordenadas | 40.4622074, −3.690494 | ficha de Google |
| Calle | Calle de Rosario Pino | Nominatim, reverse con las coordenadas |
| Barrio / distrito | Castillejos · Tetuán | Nominatim |
| Código postal | 28046 Madrid | Nominatim |
| Web propia | **No tiene** | `tiene_web.py` (18 prospectos, limpio) + 4 búsquedas web |

## Lo que NO está verificado — y por eso no se declara

- **Número de portal.** El reverse de Nominatim devuelve la calle, no el portal.
  Regla del proyecto: si las fuentes no coinciden en el número, no se pone.
  Se pregunta en el mensaje.
- **Nota de Google y número de opiniones.** No aparecen en ninguna fuente
  accesible (Maps da 403). Sin recuento verificado **no se declara
  `aggregateRating`**.
- **Horario, tarifas, servicios y dónde entrena.** Nada de esto está publicado.
  Todo va marcado con `data-ejemplo`.

## El aviso importante: el nombre choca con una federación

«FEDA» es la **Federación Española de Actividades Dirigidas y Fitness**
(feda.net), que certifica entrenadores y **sí tiene web**. Se comprobó:

- La delegación de FEDA en Madrid está en **Pº de la Castellana 171, 4º izq**,
  teléfono +34 614 39 81 05. No es esta.
- La sede figura además en Pedro Teixeira 16 y en Santa Engracia 65. Ninguna en
  Rosario Pino.
- El teléfono 697 17 71 16 no aparece en ninguna página de FEDA.
- `fedamadrid.com` ni siquiera resuelve.

**Conclusión:** es un negocio independiente, con toda probabilidad de alguien
certificado por FEDA que ha metido la sigla en el nombre de su ficha. La demo
**no puede presentarse como FEDA** ni usar su identidad. En el mensaje se
pregunta si el nombre del negocio es ese o es solo la certificación.

## Gancho real

Un entrenador personal a pie de calle en Castillejos, rodeado de cadenas
(Fitness Park, Basic-Fit) que compiten por precio. Lo único que él tiene y ellas
no es **una persona que te mira**. La página tiene que vender eso, y decir el
precio: lo que frena a quien se lo está pensando no es la cuota, es no saber
cuánto cuesta ni si va a poder seguir el ritmo.
