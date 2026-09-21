# Miuna — notas de verificación (21/09/2026)

Tienda de moda y complementos, Calle de Mauricio Legendre 3, local 7, 28046
Madrid (barrio de Castilla, Chamartín).

## Por qué NO es el candidato que me asignaron

El encargo traía **grupo-sigame-24-hr** (agencia inmobiliaria, móvil 627951842).
**Descartado por dos motivos independientes:**

1. **Sí tiene web.** `sistema/tiene_web.py` la caza: `https://gruposigame24hr.es`,
   `<title>` «Home - Grupo S.I.G.A.M.E. 24 HR.». Es suya sin duda — el
   JSON-LD de Yoast declara `Organization` con ese mismo nombre, y el nodo de
   OSM lleva `info@gruposigame24hr.es`, correo del mismo dominio.
   Es un **WordPress a medio hacer y abandonado**: `article:modified_time`
   2021-06-21, el tema de plantilla con textos «Lorem ipsum», la entrada
   «Hello world!», la «Sample Page» y `/contacto` devolviendo un 404. No he
   podido confirmar el móvil 627951842 en ninguna fuente suya, porque la
   página de contacto no existe.
2. **No es una inmobiliaria.** El propio sitio dice qué son: «Servicios
   Integrales de Gestión, Administración y Mantenimiento de Edificios»
   (S.I.G.A.M.E. es el acrónimo). Es administración de fincas con
   mantenimiento 24 h, aunque OSM lo tenga etiquetado `office=estate_agent`.
   Se cumplió la sospecha del encargo con el «24 HR».

La reserva, **la-morenita** (floristería, Bravo Murillo), **también descartada**:
solo tiene fijo (915702967) y no aparece **ningún correo** suyo en Citiservi,
Páginas Amarillas, qdq ni búsqueda abierta. Sin canal escribible, fuera. Además
el sector ya tiene molde y demo (`flores-yohana-alonso-s-l`), y los directorios
la listan como mayorista.

Sustituto elegido con barrido propio de Overpass (radio 800 m sobre
40.4690,-3.6870, la zona norte que indicaba el encargo): **Miuna**.

## a) No tiene web

- `tiene_web.py` no le deriva ningún dominio.
- Búsquedas abiertas («Miuna tienda ropa Madrid Mauricio Legendre», «Miuna moda
  complementos Madrid», «"Miuna Collection" Madrid franquicia»): **ni web ni
  perfil propio**. Solo fichas de directorio con nombre, dirección, teléfono y
  horario.
- `nslookup` de los dominios evidentes: `miuna.es`, `miunacollection.com` →
  **NXDOMAIN**. No hay web caída ni aparcada.
- El nodo de OSM no tiene `website` **y** tampoco `contact:website`.

## b) Es de barrio, no cadena

Local único dentro de un pasaje comercial. La búsqueda de «franquicia» no
devuelve nada relacionado. Un solo teléfono y un solo local.

## c) La dirección

- **Nominatim (reverse 40.4689916,-3.6870263)** → «Miuna, Calle de Mauricio
  Legendre, Castilla, Chamartín, Madrid, 28046». **Sin número de portal.**
- **Nodo vecino** (Grupo Sigame, coords casi idénticas) sí resuelve a
  **número 3**.
- **Directorio** → «Calle de Mauricio Legendre, 3, local 7, 28046 Madrid».

Las dos fuentes que dan portal **coinciden en el 3**, así que el 3 va en la
página. El **«local 7» es de una sola fuente**: va en la página porque encaja
con el pasaje comercial, pero queda avisado en la nota de la demo para que lo
confirme la dueña.

## d) Canal escribible — SÍ

**Móvil +34 688 48 89 33** → WhatsApp directo.
Fuente: tag `phone` del nodo OSM 6710327292 (API de OSM, versión 3,
2021-11-19), corroborado por ficha de directorio con la misma dirección.
Empieza por 6, o sea móvil español. **No he encontrado correo**, y no hace
falta: con el móvil basta.

## Horario (REAL, dos fuentes que coinciden)

`opening_hours` de OSM: `Mo-Fr 10:00-21:00; Sa 10:00-20:00; Su 11:00-14:00`.
El directorio da exactamente lo mismo. Va tal cual en la página y en el
JSON-LD, marcado `data-real`.

## Coordenadas

40.4689916,-3.6870263 — nodo OSM 6710327292, `shop=clothes`.

## Lo que NO he podido comprobar

- Si sigue abierta hoy: el nodo de OSM se editó por última vez en 2021 y los
  directorios no fechan. No hay nada que indique cierre, pero tampoco prueba de
  actividad reciente.
- El nombre de quien atiende. **No se ha inventado ninguno**, ni aparece
  persona alguna en la página.
- Reseñas o nota de Google: no aparece ninguna, así que **no se declara
  `aggregateRating`**.
