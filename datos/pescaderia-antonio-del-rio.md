# Pescadería Antonio del Río — VERIFICADO (21/09/2026)

Sustituto de `reformas-y-decoracion-ckn`, que se descartó por no tener canal
escribible (ver `datos/reformas-y-decoracion-ckn.md`). Salido de un barrido
propio de Overpass en la zona suroeste; está a **unos 470 m** del punto de
referencia del encargo (40.4600,-3.7020).

## a) No tiene web propia

| Comprobación | Fuente | Resultado |
|---|---|---|
| Barrido y tags OSM | API de OSM, `node/4496964050` | **Sin `website` ni `contact:website`.** Solo `contact:phone` y `contact:mobile`. |
| Búsqueda del nombre | WebSearch «Pescadería Antonio del Río Madrid San Enrique» | **Ninguna web propia.** Solo perfiles de terceros. |
| Dominios derivados del nombre | `curl` a pescaderiaantoniodelrio .es/.com, antoniodelrio .es/.com, pescaderiadelrio .es/.com | Ninguno resuelve. |
| Ficha del mercado | `mercadodesanenrique.es/puesto/pescados-y-mariscos-antonio-del-rio/` | La página del puesto **dice expresamente que no tiene web**: solo enlaza su Instagram (@pescaderiaantoniodelrio). |

Lo que sí tiene son **fichas ajenas**: la del mercado (que es del mercado, no
suya), una en `clicoleo.com` y una página de Facebook. Nada de eso es una web
propia: no hay horario suyo editable, ni forma de encargar, ni una sola línea
escrita por ellos. **Es exactamente el hueco que rellena la demo.**

## b) Es un negocio pequeño de barrio

Un solo puesto, el **número 6**, dentro del Mercado de San Enrique. Y según la
sección de pescadería del propio mercado, es la **única pescadería del
mercado**. No es cadena ni franquicia.

## c) La dirección real

Reverse de Nominatim con las coords de la ficha (`40.4559904,-3.7002768`):

> Pescadería Antonio del Río, **Calle de San Enrique**, Cuatro Caminos, Tetuán,
> Madrid, **28020**, España

**El número de portal NO se pone en la demo.** OSM y Nominatim no lo dan;
`clicoleo` dice «Calle San Enrique, 16». Solo una fuente lo afirma, así que se
deja fuera y se pregunta. En un mercado además el dato que importa es otro: el
**puesto 6**, que sí viene de la ficha oficial del mercado.

## d) Canal escribible — SÍ, WhatsApp

**Móvil `+34 606 593 936`**, confirmado por tres fuentes independientes:

1. **OSM**, campo `contact:mobile` (nodo editado el **09/11/2025**, versión 2).
2. **La web del propio mercado**, ficha del puesto 6: fijo 915700323 y móvil 606593936.
3. **clicoleo**, que además especifica «**WhatsApp disponible, 24/7, toda la
   semana**» y que se puede encargar por ahí.

No es un `+34 6xx 00 00 00` ni un placeholder de formulario: es un número
completo, repetido igual en tres sitios y coherente con el fijo del mismo
puesto. **`via: whatsapp`.** Sin correo publicado: no se inventa ninguno.

## ¿Sigue abierta?

Sí. El nodo de OSM se **editó en noviembre de 2025** (al contrario que el de
CKN, de 2014 y sin tocar), y la ficha del mercado lo lista hoy como el puesto
de pescadería en activo, con descripción y servicios propios.

## Horario — ojo, dos fuentes discrepan

- **Web del mercado (puesto 6):** L-V 9:00–14:00 y 17:00–20:00 · Sáb 9:00–14:30 · Dom cerrado.
- **clicoleo:** L-V 9:00–20:00 seguido · Sáb 9:00–15:00 · Dom cerrado.

Se ha puesto **la del mercado** (jornada partida, que es lo normal en un puesto)
y se avisa en la nota de la página de que conviene confirmarlo.

## Lo que ofrecen, según su propia ficha del mercado

«Venta de pescados y mariscos frescos y congelados SELECTOS», **reparto a
domicilio** y **cocedero propio**. Los tres datos son suyos, no inventados; lo
inventado son los surtidos concretos y los encargos.

## Sin nota de Google

No se ha encontrado recuento de opiniones verificado. **No se declara
`aggregateRating`** y la demo no lleva sección de opiniones.
