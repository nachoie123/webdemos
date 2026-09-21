# BM1997 S.L. — Copistería

Verificada el 21/09/2026. **Demo 30, la última.**

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | BM1997 S.L. — Copistería | Waze, esopiniones, varios directorios |
| Teléfono | 91 570 40 33 (**fijo**) | ficha **y** esopiniones |
| Calle | Calle de los Cuatro Amigos | **el reverse devuelve «BM, Calle de los Cuatro Amigos»** + Waze |
| Portal | **sin confirmar** | ninguna fuente da el número |
| Barrio | Almenara · Tetuán · **28020** Madrid | reverse (un directorio dice 28012, que es Lavapiés: está mal) |
| Coordenadas | 40.4656499, −3.6915443 | ficha |
| Servicios | Fotocopias, impresión, escaneo y **encuadernación** | directorios |
| Posicionamiento | Aparece en varias listas de **«copisterías baratas de Madrid»** | pasaenmadrid, copygrap, solicitalo |
| Web propia | **No tiene** | solo directorios |

**Sin WhatsApp conocido:** solo consta el fijo. Eso es un problema real para una
copistería —el cliente quiere mandar el PDF— y **va preguntado en la nota de la
página y en el mensaje**. No se inventa ningún número.

## Cómo se diferencia de Imprime y Más, la otra copistería del proyecto

`moldes/copisteria.md` está escrito alrededor de dos preguntas: «¿puedo mandarlo
sin ir?» y «¿para cuándo lo tengo?». Ésas ya se usaron.

BM1997 tiene otro posicionamiento y hay que atacarlo por ahí: **es barata y lo
es a propósito**, y lleva en el nombre el año en que empezó. Así que su página
va de lo que ninguna copistería publica: **el precio por copia**, y de una idea
que casi treinta años en la misma calle permiten decir sin presumir.

## La pieza nueva: una calculadora que funciona

Las otras 29 demos enseñan información. Ésta **calcula**: se meten las páginas,
si es a una o dos caras, color o blanco y negro, y el tipo de encuadernación, y
da el total.

Es la respuesta exacta a lo que se pregunta un opositor con un temario de 800
páginas o alguien con un TFG, y **no la da nadie en el sector**. Son unas 25
líneas de JavaScript sin ninguna dependencia.

Los precios que usa son inventados y están marcados, y la propia calculadora lo
dice en su pie.

## Lo que no se declara

- **El portal** (ninguna fuente lo da).
- **La nota:** un directorio dice 4,4 con 97 valoraciones. Una sola fuente.
  Sin `aggregateRating`.
- **Precios y horario:** inventados y marcados.
- **Nada sobre los dueños ni sobre qué significa «BM».** No hay fuente.
