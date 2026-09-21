# Escuela Infantil Vaiana — verificado 21/09/2026

Sustituto de **AEP Mantenimiento e Instalaciones** (descartado: tiene tienda
online viva, ver `datos/aep-mantenimiento-e-instalaciones.md`). No había reserva
asignada, así que salió de un barrido propio de Overpass en la zona
noroeste (`around:700, 40.4700,-3.6930`, nodos y ways con `phone` y sin
`website`).

- **Slug:** `escuela-infantil-vaiana`
- **Sector:** escuela infantil privada de primer ciclo (0-3). **Molde nuevo:**
  `sistema/moldes/guarderia.md`.

## a) Que no tenga web propia — CONFIRMADO

La escuela **no tiene ninguna web viva**. Tiene tres dominios asociados y los
tres están caídos o en venta:

| Dominio | De dónde sale | Estado (21/09/2026) |
|---|---|---|
| `betaria.com` | ficha del **Ayuntamiento de Madrid** | **EN VENTA**: «The premium domain name betaria.com is for sale» |
| `betaria.es` | ficha de **buscocolegio** (datos del registro de centros) | sin registro A, no resuelve |
| `vaianaescuelainfantil.com` | email de la ficha OSM | sin registro A **ni MX** |
| `escuelainfantilvaiana.com` | email citado por infoguarderia | sin registro A **ni MX** |

Comprobado con `dig +short <dominio> A / MX` y `curl -L`. micole.net declara
explícitamente «Website: not provided». `tiene_web.py` no la marca.

**Consecuencia práctica (y es el gancho):** quien busca la escuela encuentra
directorios y una página de «dominio en venta». Además las fichas oficiales
siguen usando el **nombre anterior, Betaria**.

## b) Negocio pequeño de barrio — CONFIRMADO

Un solo centro. Titular **EUROALINA NEGOCIOS, S.L.** (buscocolegio).
Titularidad **privada**, dicho explícitamente por madrid.es («Privado», no «de
titularidad del Ayuntamiento»). No confundir con *Vaiana Espacio Infantil y
Familiar* de Mijas (Málaga), que es otra empresa sin relación.

## c) Dirección real — CONFIRMADA, con portal

**Calle del Padre Rubio, 14 · 28029 Madrid** (barrio de Almenara, distrito
Tetuán). Cuatro fuentes coinciden en el portal 14:

1. Reverse de Nominatim sobre 40.4704066,-3.6920236 → «Escuela Infantil Privada
   Vaiana, 14, Calle del Padre Rubio, Almenara, Tetuán, 28029».
2. OSM node: `addr:street=Calle del Padre Rubio`, `addr:housenumber=14`.
3. madrid.es (ficha «Escuela Infantil Betaria») → «CALLE PADRE RUBIO, 14 28029».
4. buscocolegio → «C/ del Padre Rubio 14. 28029».

Se puede publicar el número.

## d) Canal escribible — CONFIRMADO: móvil (WhatsApp)

**616 86 44 17.** Publicado en tres sitios independientes:

- ficha OSM: `phone=+34913149804;+34616864417`
- buscocolegio (ficha del centro 28065577): «913149804 y 616864417»
- infoguarderia.es: «913149804/616864417»

`via: whatsapp`. El fijo **913149804** (madrid.es, buscocolegio, OSM) queda como
teléfono secundario de la página.

**Email: NO hay uno que funcione.** Los dos que circulan por los directorios
—`info@vaianaescuelainfantil.com` y `info@escuelainfantilvaiana.com`— están en
dominios **sin registro MX**: rebotarían. Los de la ficha municipal
(`info@betaria.es`, `info@betaria.com`) son del nombre viejo y tampoco tienen
MX. No se pone ninguno en la ficha.

## Datos REALES que van en la página

- Nombre: Escuela Infantil Vaiana (OSM: «Escuela Infantil Privada Vaiana»).
- **Código de centro de la Comunidad de Madrid: 28065577** (OSM
  `ref:ES:educamadrid` + buscocolegio). Es el dato verificable del sector, el
  equivalente al número de colegiado.
- Primer ciclo, 0-3 años (madrid.es: «Educación infantil (Primer Ciclo)»).
- Accesible para personas con movilidad reducida (madrid.es; OSM
  `wheelchair=yes`).
- Topes legales de niños por aula en primer ciclo en la Comunidad de Madrid:
  8 (0-1), 14 (1-2), 20 (2-3). Normativa, no datos del centro.

## Datos INVENTADOS (todos marcados con `data-ejemplo`)

Plazas libres por aula, todas las cifras de la cuenta de fin de mes, el plano
del local, el desglose del día hora a hora, el protocolo de fiebre, los pasos de
la adaptación, lo que se deja en la percha y la duración de la visita.

**El horario (7:30-18:00, abierto todo el año) también va marcado**: sale de
infoguarderia, que es un directorio de terceros, no del centro. En OSM no hay
`opening_hours` para este nodo.

**Sin nota de Google y sin `aggregateRating`.** micole declara 4,9 sobre 52
reseñas, pero el mismo buscador devolvió «4,2 sobre 52» para otro negocio
distinto de la misma tanda: número no fiable, no se declara. Sin fotos de
ningún tipo: es un centro infantil.
