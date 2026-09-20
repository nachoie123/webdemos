# Barbería Cholo y Peluquería de Caballero — datos verificados

Comprobado el 21/09/2026.

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Barbería Cholo y Peluquería de Caballero | ficha de Google |
| Móvil (WhatsApp) | 640 86 23 27 | ficha de Google **y** su página de Fresha |
| Calle | Avenida de Asturias, junto a Plaza de Castilla | Fresha + Nominatim |
| Portal | **3 según Fresha · sin confirmar** | Nominatim cae en el nº 7, que es otra tienda |
| Barrio | Almenara / Castillejos · Tetuán · 28029 | Nominatim |
| Coordenadas | 40.4664671, −3.6907783 | ficha de Google |
| Horario | L–V 9:30–14:00 y 16:30–20:00 · S 9:30–14:00 | **su propia página de Fresha** |
| Web propia | **No tiene** | `tiene_web.py` + búsqueda |

## El hallazgo: tiene Fresha

`fresha.com/lvp/barberia-cholo-y-peluqueria-de-caballero-...`

No es una web, pero **no es lo mismo que no tener nada**, y cambia el mensaje
entero. Lo que hay que contarle no es «no tienes web», sino esto:

- **Quien le busca en Google llega a la casa de Fresha, no a la suya.** El
  nombre que sale grande arriba es Fresha. La foto de cabecera es de Fresha. Y
  al lado aparecen las otras veinte barberías de Tetuán que también están allí.
- **Fresha se queda con la relación.** El correo del cliente, el recordatorio y
  la reseña son de Fresha.
- **La solución no es irse de Fresha.** Es tener puerta propia y que el botón
  de reservar lleve a Fresha. La reserva sigue funcionando igual; lo que cambia
  es de quién es la puerta.

Ese es el argumento entero de esta demo, y es distinto al de las otras trece.

## Lo que no se declara

- **El portal.** Fresha dice 3, el reverse de Nominatim cae en el 7 (que es
  otro comercio). Dos fuentes, dos números: no se pone.
- **La nota.** `prospectos.json` decía 5,0 con 121 opiniones. Una sola fuente y
  sin contrastar. Sin `aggregateRating`.
- **Precios y servicios.** No publicados. Inventados y marcados.

## El otro gancho: el sitio

Está a un paso de **Plaza de Castilla**, con las torres inclinadas enfrente. El
dibujo grande de la página son esas torres: es un sitio que solo puede ser ése,
y ningún dibujo de tijeras genérico dice dónde estás.

Y el nombre lo dice todo: **«peluquería de caballero»**, no «barber shop». No es
una barbería de moda, es la de toda la vida. Esa diferencia es la identidad y
hay que escribirla, no disimularla.
