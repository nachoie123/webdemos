# Reparación de Calzado y Complementos J.T. — verificación (21/09/2026)

**Candidato asignado (descartado): Óptica Roma**, Bravo Murillo 166.
Tiene web propia `opticaroma.com` (título «Óptica ROMA - Gafas, Lentillas,
Astronomía…», detectada por `sistema/tiene_web.py`) y además es cadena: su
propia web tiene página «Nuestras tiendas», con local en Paseo de la
Castellana 148. Doble motivo de descarte.

**Reserva: no tenía.** Barrido propio de Overpass en la zona oeste
(around:700, 40.4535,-3.7025 y around:1600 sobre 40.4570,-3.7000 para
`shop=optician`). El sector óptica está agotado en el barrio:

| Óptica | Por qué cae |
|---|---|
| Óptica Corot (BM 325) | web `opticacorot.es` |
| Óptica Gali (Jerónima Llorente 68) | web `opticagali.com` + grupo Natural Optics |
| Viva Visión (Lope de Haro 9) | web `vivavisionopticos.com` + grupo Natural Optics |
| OptiMiza (BM 140) | web `optimizavision.es` |
| Óptica EMI (Capitán Blanco Argibay 65) | agrupación Cione; además solo fijo |
| Óptica Guía (C. de Antonio 2) | **sin web**, pero solo fijo 913153039: sin canal escribible |
| Ulloa, Afflelou, Visionlab, General Óptica, Multiópticas, Soloptical, VistaÓptica, Federópticos, San Gabino (Opticalia) | cadenas o agrupaciones |

Cambio de sector con el visto bueno del coordinador: hace falta un negocio de
barrio sin web y con WhatsApp o correo, no que sea óptica.

---

## El negocio elegido

**Reparación de Calzado y Complementos J.T.** — puesto de zapatero dentro del
**Mercado de Maravillas**, Calle de Bravo Murillo 122, planta 1, Cuatro
Caminos, Tetuán, 28020 Madrid. Móvil **677 12 94 50**.

### a) No tiene web
- No hay dominio: `calzadosjt.es` y `reparacioncalzadojt.es` no resuelven.
- Búsqueda del nombre y del teléfono: solo fichas de directorios
  (Páginas Amarillas), ninguna web propia ni perfil con web.
- OSM no le pone `website` **y** la búsqueda tampoco encuentra homónimo: el
  negocio no aparece en internet más allá de una línea de directorio.

### b) Es de barrio
Un puesto dentro de un mercado municipal. Un solo local, sin franquicia. En el
mismo número 122 hay otros dos arreglos de calzado —Joel (635885347) y
Llaves y Zapatos BYM / BM (617080692)— que son puestos **distintos**: se
distinguen por el teléfono. El nuestro es el del 677129450.

### c) Dirección real
- Nominatim reverse sobre 40.448495,-3.7025736 → «Calzados, 122, Calle de
  Bravo Murillo, Cuatro Caminos, Tetuán, Madrid, 28020».
- Páginas Amarillas: «Reparación de Calzado y Complementos J.T. — Bravo
  Murillo, 122» (barrio Cuatro Caminos, distrito Tetuán).
- OSM: `craft=shoemaker`, `addr:housenumber=122`, `addr:unit=Planta 1`.
- Las tres fuentes coinciden en el portal 122. **El número de puesto dentro
  del mercado no lo publica nadie**: no se pone, se pregunta.
- El 122 es el **Mercado de Maravillas** (1942, dos plantas, más de 250
  puestos): es el mayor mercado municipal de Madrid por superficie.

### d) Canal escribible — SÍ
**Móvil 677 12 94 50** (empieza por 6 → WhatsApp). Dos fuentes independientes:
- OSM: `phone=+34 677129450` en el nodo `craft=shoemaker` del 122.
- Páginas Amarillas: ficha «Reparación de Calzado y Complementos J.T.»,
  Bravo Murillo 122, teléfono 677129450.

No se ha encontrado correo publicado. `via` = `whatsapp`.

### Lo que NO se ha podido verificar (y por eso no se afirma en la demo)
- El horario exacto del puesto.
- El número de puesto y la planta con certeza (OSM dice «Planta 1»).
- Los precios de los arreglos y los plazos.
- Quién lo lleva y desde cuándo.
- No hay reseñas con recuento fiable → **sin `aggregateRating`**.
