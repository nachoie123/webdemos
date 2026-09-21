# Novelor Joyeros — verificación (21/09/2026)

Entró en la lista como **`pedro-duran`** («Pedro Durán», joyería, tel. 913142154,
coords 40.46938,-3.68693). **No es la marca nacional Pedro Durán.** Es otro
negocio: el rótulo lleva el nombre de la platería que distribuyen.

## a) ¿Es la marca nacional Pedro Durán? NO

| Fuente | Qué dice |
|---|---|
| pedroduran.com + duranjoyeros.com | Tiendas de la marca: **Goya 30**, oficina Bárbara de Braganza 2, outlet Camino de las Hormigueras 160, córner en El Corte Inglés Pozuelo. **Ninguna en Mauricio Legendre.** |
| DuckDuckGo del teléfono `913142154` | Un solo resultado de empresa: **NOVELOR IMPORT EXPORT SL**. Ninguno de la marca. |
| sedinfo.es / iberinform.es | NOVELOR IMPORT EXPORT SL, **CIF B82278706**, C/ Mauricio Legendre 7, tel. 913142154, constituida 17/02/1999, admin. José Luis Navarro Vicente. CNAE de joyería/relojería. |
| Páginas Amarillas | «Joyería - Relojería **Novelor**», Calle Mauricio Legendre, tel. 913142154. |
| qdq.com | «**DISENJOYA**», Calle Mauricio Legendre 7, tel. 913142154. |
| **Su propia web archivada** (ver abajo) | **«Somos distribuidores oficiales de relojes MAURICE LACROIX, SANDOZ, VICEROY, BASSEL, TIME FORCE. Platería PEDRO DURAN, MAJORICA y de la prestigiosa marca de brillantería GAYUBO.»** |

Esa última línea cierra el caso: **Pedro Durán es una de las marcas que
distribuyen**, no el nombre del negocio. El que censó la calle en OSM
(usuario *Hugoren Martinako*, 18-19/11/2021, changesets 113962670 / 113991498)
apuntó lo que ponía el rótulo del escaparate.

Horario del censo OSM: `Mo-Fr 10:00-14:00,17:00-20:00; Sa 10:00-14:00`. Cierre
al mediodía y sábado por la mañana: horario de tienda de barrio, no de boutique
de marca.

## b) ¿Negocio pequeño? SÍ

Un solo local, dentro de la galería comercial de Mauricio Legendre 7 (la misma
donde están la carnicería Nicar, DietFlash, Fotocopias Edy y Tamarindo Express).
Su propia web: *«Empresa familiar ubicada en el barrio desde hace 30 años.
Somos profesionales del sector con talleres propios en el mismo domicilio.»*

## c) Dirección — **Mauricio Legendre 7, 28046 Madrid**

Cuatro fuentes coinciden en el portal 7, sin discrepancia:
- Su propia web: «NOVELOR IMPORT-EXPORT S.L. C/ Mauricio Legendre nº 7, 28046
  Madrid (zona Plaza de Castilla)».
- sedinfo / iberinform / einforma: Cl. Mauricio Legendre 7.
- qdq: Calle Mauricio Legendre 7, 28046.
- Nominatim sobre las coords vecinas de la misma galería (Nicar y DietFlash,
  nodos OSM 9264927899 / 9264927898) devuelve `7, Calle de Mauricio Legendre,
  Castilla, Chamartín, 28046`.

## d) ¿Tiene web? **LA TUVO Y SE CAYÓ — hoy no tiene**

```
novelor.es            → no resuelve (sin DNS)
www.novelor.es        → no resuelve
joyeria-novelor.com   → no resuelve   (es la web que qdq sigue enlazando)
disenjoya.es/.com     → no resuelve
```

`tiene_web.py` marcaba `pedro-duran → pedroduran.com`: es el **falso positivo
del homónimo**, el dominio de la marca nacional, no suyo.

Internet Archive (`web.archive.org/cdx`): novelor.es vivió **de 2013 a ~2015**
y desde entonces nada. Snapshot leído: `20130607232026`. La web tenía
INICIO · EMPRESA · JOYERÍA · RELOJERÍA · **TALLER DE JOYERÍA** · BRILLANTES ·
OUTLET · PLATA · CONTACTO, y la página del taller todavía llevaba **Lorem Ipsum**
debajo del texto bueno.

Texto real de su página de taller, que es de donde sale el ángulo de la demo:

> «Hacemos todo tipo de trabajos de joyería. Arreglos, restauración de joyas,
> diseños personalizados, engastados con todo tipo de piedras preciosas y
> semipreciosas, baños de rodio, oro y plata, grabados, enfilados de collares y
> pulseras, etc.»

→ `estado_web: "caida"`, `web_actual: "http://www.novelor.es"` (muerta).

## e) Canal escribible — **correo, sí**

- Fijo **913142154** (no sirve para WhatsApp).
- **No hay móvil** en ninguna fuente.
- **Correo: `novelorimport@yahoo.es`** — publicado **por ellos mismos** en la
  portada de novelor.es, junto al nombre, la dirección y el teléfono. Recuperado
  del Internet Archive (snapshot 20130607). No está inventado.

**Aviso para quien escriba:** el correo es antiguo (la web murió hacia 2015).
Un Yahoo de una tienda familiar suele sobrevivir, pero puede rebotar. Si rebota,
solo queda el fijo.

## Cosas que conviene saber antes de enviar

- **Tres nombres en circulación:** OSM dice «Pedro Durán», Páginas Amarillas
  «Novelor», qdq «Disenjoya». El nombre que ellos usan en su propia web es
  **Novelor Joyeros** (cabecera: «Novelor Joyeros – C/ Mauricio Lejandre 7»),
  con razón social Novelor Import-Export S.L. Ese es el que lleva la demo.
  Es, de hecho, medio argumento de venta: en Google su negocio aparece partido
  en tres fichas con tres nombres distintos.
- **Iberinform marca las dos sociedades como «Inactiva»** (Novelor Import Export
  SL y Joyerías Novelor SL). Suele significar cuentas sin depositar, no puerta
  cerrada; el censo OSM de noviembre de 2021 la registró abierta y con horario.
  Aun así, **no está verificado que sigan abiertos hoy**: conviene llamar al
  913142154 antes de mandar nada.
- **No hay opiniones verificadas** en ninguna parte: la demo no declara
  `aggregateRating` ni lleva sección de reseñas.

## Reserva descartada

**DietFlash** (fijo 913148551, Mauricio Legendre 7) es **DietFlash Medical**,
franquicia con **más de 50 centros** (10 propios, 43 franquiciados) y web propia
en `dietflash.es`. Descartada por cadena, tal y como avisaba el encargo.
