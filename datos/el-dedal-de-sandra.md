# El Dedal de Sandra — datos verificados

Comprobado el 21/09/2026.

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | El Dedal de Sandra (arreglos de costura) | ficha de Google vía Waze, todosbiz, lamanzanadeeva |
| Sector | Taller de arreglos de ropa (`shop=tailor` en OSM) | nodo OSM 11937579598 |
| Móvil (WhatsApp) | **686 33 89 10** | todosbiz.es y lamanzanadeeva.es, los dos con el mismo número |
| Correo | No publica ninguno | ninguna de las fichas lo trae |
| Dirección | Avenida de Ramón y Cajal, **19** | ficha de Google (Waze, todosbiz, lamanzanadeeva) |
| Barrio | Ciudad Jardín · Chamartín · 28016 Madrid | reverse de Nominatim sobre las coords del nodo |
| Coordenadas | 40.45186, −3.67353 | nodo de OSM |
| Horario | L–V 10:00–14:00 y 16:00–20:00 · S 10:00–14:00 · D cerrado | todosbiz y lamanzanadeeva, coincidentes |
| Web propia | **No tiene** | ver abajo |
| Cadena | No. Un solo local, un solo teléfono | sin más direcciones en ninguna búsqueda |
| `place_id` de Google | `ChIJH9ATy9koQg0RnMCvEG1HJVo` | sale de la URL de Waze; el enlace de Maps devuelve 200 |

## Que no tiene web

Buscado «El Dedal de Sandra», «Dedal de Sandra arreglos costura Madrid» y
«Ramón y Cajal 19 arreglos ropa». **Solo salen directorios** —Waze, todosbiz,
lamanzanadeeva, mundocostura— y ninguno enlaza a un dominio propio.
lamanzanadeeva llega a poner en el campo «web» la frase «Google My Business
listing», que es justo lo contrario de tener web. El nodo de OSM tampoco lleva
`website`.

## El canal escribible

**686 33 89 10 es móvil** (empieza por 6), así que vale para WhatsApp. Dos
fichas independientes lo dan igual. No hay correo publicado en ninguna parte,
ni fijo. `via` = `whatsapp`.

## El portal: dicho con la salvedad

Las tres fichas dan **Ramón y Cajal 19**. El nodo de OSM está en la misma
avenida pero **sin `addr:housenumber`**, y el punto cae en la acera de los
pares (los impares 23, 25, 27… quedan a unos 50 m al este, en la acera de
enfrente). No hay dos fuentes que se contradigan —una da el 19 y la otra no da
número—, así que se pone el 19, pero **la página lo dice en la nota y pide
confirmación**. Si Nacho quiere curarse en salud, que lo pregunte en el
mensaje.

## Candidato anterior: Kukos — DESCARTADO

El encargo traía «Kukos», zapatería en Calle de Puerto Rico 29. **Tiene web y
además tienda online:** `kukosspain.es` está vivo, con el mismo teléfono de la
ficha (910 587 020) y la descripción «Zapatería de calzado infantil de
calidad». Es zapatería infantil, sí, pero el hueco no existe.

Ojo con `kukos.es`: devuelve 200 y el `<title>` dice «Kukos», pero es una
**plantilla de demostración de un pub de Nueva York** («123 Demo Road»,
`mail@example.com`). Otra trampa del HTTP 200, como `talleresjl.es`.

## Reserva descartada por el camino

**Escuela Infantil Yaki** (Av. de Ramón y Cajal 49, móvil 669 62 72 16 en el
propio OSM) salió del barrido y tiene móvil, pero **tiene WordPress vivo**:
`eiyaki.com`. Descartada.

## Cómo apareció

Barrido propio de Overpass, `nwr(around:1000, 40.4575, −3.6730)` sin `website`,
después de que cayeran Kukos y su reserva improvisada. Se dejaron fuera Tesela
y Formación en la nube (son de otros agentes) y los 30 slugs que ya están en
`docs/`.
