# REPARACIONES EL EXPERTO — datos verificados

Comprobado el 20/09/2026 antes de escribir la demo.

## Lo que está verificado

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Reparaciones El Experto | ficha de Google + Cylex + Facebook |
| Móvil (WhatsApp) | 634 13 93 01 | ficha de Google **y** esopiniones, coinciden |
| Dirección | Calle de Bravo Murillo, **355** | **Nominatim devuelve el portal 355** + esopiniones |
| Barrio / distrito | Almenara · Tetuán | Nominatim |
| Código postal | 28029 Madrid | Nominatim |
| Coordenadas | 40.4649457, −3.6942308 | ficha de Google |
| Qué arregla | Móviles **y ordenadores** | Cylex: «REPARACIÓN DE MÓVILES Y ORDENADORES» |
| Web propia | **No tiene** | `tiene_web.py` (limpio) + búsqueda: solo directorios |

Aquí el portal **sí se puede poner**: el reverse de Nominatim devuelve
`house_number: 355`, que es la fuente más fiable que hay para una calle, y un
directorio independiente dice lo mismo.

## Lo que NO está verificado — y por eso no se declara

- **La nota y el recuento.** `prospectos.json` decía «4,7★ (426 opiniones)»;
  esopiniones dice **51 opiniones**. La diferencia es enorme: uno de los dos
  está contando otra cosa. **No se declara `aggregateRating`.** Tercer caso
  después de Imprime y Más y Flores Yohana.
- **El correo.** Un directorio publica `reparacioneselexperto@gmail.com`. Es una
  sola fuente y además un dato que se copia mal entre directorios: no va en la
  página, se pregunta.
- **Horario, precios, plazos y garantía.** No están publicados. Todo marcado
  con `data-ejemplo`.

## Ojo: sí tiene Facebook

`facebook.com/p/Reparaciones-el-Experto-100063623410560`. **No es una web** —
sigue contando como «sin web»— pero cambia el mensaje: no hay que explicarle que
existe internet, hay que explicarle **por qué una página de Facebook no la
encuentra quien busca «arreglar pantalla Bravo Murillo» en Google**. Eso es un
gancho mejor que «no tienes web».

## Gancho real

No es un sitio de Cuzco: está en Bravo Murillo 355, en Almenara, arriba del
todo de Tetuán. Es una tienda de barrio de las de mostrador.

Lo que manda en este sector y no está escrito en ninguna parte:

- **El cliente llega en pánico**, con el móvil roto en la mano. La pregunta no
  es cuánto cuesta: es **«¿cuánto tardas?»** y **«¿pierdo las fotos?»**.
- **Y hay una tercera que nadie hace en voz alta**: si van a ver lo que tiene
  dentro. Todo el mundo lo piensa y nadie lo pregunta. Una página que lo
  conteste sin que se lo pidan gana la reparación antes de empezar.
- **Arregla ordenadores además de móviles**, y eso no se lee en ningún sitio.
  Es el trabajo que mejor se paga y el que menos le piden por desconocimiento.
