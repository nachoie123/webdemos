# Colora Estética — datos verificados

Comprobado el 20/09/2026 antes de escribir la demo.

## Lo que está verificado

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Colora Estética | ficha de Google |
| Móvil (WhatsApp) | 658 43 63 55 | ficha de Google **y** el directorio, coinciden |
| Zona | Costa Fleming · Nueva España · Chamartín | Nominatim (reverse de las coordenadas) |
| Código postal | 28046 Madrid | Nominatim y el directorio coinciden |
| Coordenadas | 40.4615682, −3.6891565 | ficha de Google |
| Qué hace | Manicura y pedicura | ficha de Google + directorio |
| Web propia | **No tiene** | `tiene_web.py` (limpio) + búsqueda: solo agregadores |

## Lo que NO está verificado — y por eso no se declara

- **El número de portal.** Un directorio dice «Paseo de la Castellana, 192».
  El reverse de Nominatim devuelve la Castellana y el edificio, pero **sin
  número**. Es **una sola fuente**, y en este proyecto un portal necesita dos.
  En la página va la calle sin número y se pregunta en el mensaje.
- **La nota.** El mismo directorio dice 4,9 con 31 opiniones. Suena razonable,
  pero es **un solo agregador de los que se copian entre sí** y no he podido
  contrastarlo. **No se declara `aggregateRating`.** Si ella confirma el
  recuento, se pone: aquí el dato probablemente es bueno, solo le falta fuente.
- **El horario.** El mismo directorio dice lunes a sábado 10:00–21:00 y
  **domingo 11:00–20:00**. Va como ejemplo. Ver abajo: si es cierto, es lo más
  importante de toda su ficha.
- **Precios y servicios.** No están publicados. Todo `data-ejemplo`.

## Gancho real

Dos cosas, y la segunda es la buena:

1. **El truco del sector.** La queja número uno en uñas es el precio que
   cambia al llegar: se anuncia la semipermanente a un precio y luego **la
   retirada del esmalte anterior se cobra aparte**. Una página que diga «el
   precio ya lleva la retirada dentro» gana la cita sin competir por precio.
2. **Si de verdad abre los domingos, es su mayor ventaja y no lo sabe nadie.**
   Casi ningún centro de uñas de la zona abre domingo. Quien busca «uñas
   domingo Madrid» es alguien decidido, con prisa y sin alternativa. Eso no
   está escrito en ningún sitio donde Google pueda leerlo. **Hay que
   preguntárselo en el mensaje.**

## Regla que hereda de salud

Es estética, no medicina, así que las opiniones de ejemplo sí se pueden poner.
Pero **ni una promesa sobre uñas, piel ni salud**, y la sección de higiene
describe lo que se hace con el material — **nunca promete que no pase nada**.
