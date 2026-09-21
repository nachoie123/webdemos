# carpinteria-aluminio-manuel-diaz — verificación (21/09/2026)

**Manuel Díaz Carpintería de Aluminio, S.L.** · Calle de Costa Rica 20, 28016
Madrid (Chamartín, Hispanoamérica). Barrido propio de Overpass en la zona este,
a 168 m del punto de referencia 40.4570,-3.6750.

Sustituye a **tesela**, descartado (ver el final).

## a) ¿Tiene web propia? NO

- Siete dominios probables probados con `curl`. Seis no resuelven
  (`aluminiosmdiaz.es/.com`, `manueldiazaluminio.es`, `carpinteriamanueldiaz.es`,
  `manueldiazcarpinteria.es`, `aluminiosmanueldiaz.es`). El séptimo,
  `manueldiaz.es`, devuelve 200 pero su `<title>` es **«Parked Domain name on
  Hostinger DNS system»**: un dominio aparcado, no suyo. Es justo la trampa del
  200 que avisa el README.
- Fichas de terceros fetcheadas una a una — Páginas Amarillas, qdq, Citiservi,
  Empresite (eleconomista) — y **ninguna declara sitio web**. En la de Empresite
  los únicos enlaces externos del HTML son cloudflare, einforma y analytics.
- OSM (nodo 2839832732): sin `website` ni `contact:website`.

## b) ¿Es de barrio? SÍ

Sociedad limitada del **11/04/1995**, CIF B81129983, un solo local (Costa Rica 20,
bajo), **unos 3 empleados** y facturación de 0 a 500 000 € (Empresite). Ni cadena
ni franquicia: no hay ninguna otra sede.

## c) Dirección — portal 20, dos fuentes fetcheadas de acuerdo

- **Páginas Amarillas**: «Costa Rica, 20 BAJO-LOCAL, 28016, Madrid».
- **qdq**: «Calle Costa Rica 20, 28016, Chamartín-Hispanoamérica».
- **Citiservi**: «C/ Costa Rica 20, 28016 Madrid».
- **Empresite**: «Calle Costa Rica núm. 20, (28016), Madrid».
- **Nominatim reverse** de 40.4582858,-3.6739661 → «Carpintería metálica de
  aluminio Manuel Díaz, Calle de Costa Rica, Hispanoamérica, Chamartín, Madrid,
  28016». Confirma calle y código postal; no da portal.

Un resumen de buscador soltó «Costa Rica 18», pero **ninguna** de las cuatro
fichas abiertas dice 18. Se usa el **20**.

## d) Canal escribible — SÍ, correo

**aluminiosmdiaz@yahoo.es**, en el campo «Email» de la ficha de Empresite
(eleconomista/eInforma), y además como `mailto:` dentro del HTML de esa página.
Es el único correo de todo el documento y va atado a este CIF. Descargada y
comprobada a mano, no de un resumen de buscador.

No hay móvil publicado: el único teléfono es el fijo **913593657**, que aparece
en las cuatro fichas. Así que `via` es `email`, no WhatsApp.

## Lo demás que salió verificado

- Horario (Páginas Amarillas): **L-V 9:00–13:30 y 16:00–20:00**, sábado y
  domingo cerrado, y **cierra en agosto**.
- Objeto social (Empresite): «carpintería, cerrajería y terminación y decoración
  de edificios y locales; venta, distribución e instalación de ventanas y
  puertas». CNAE 2512, fabricación de puertas y ventanas metálicas.
- Rótulo de Páginas Amarillas: «PUERTAS, CERRAMIENTOS DE TERRAZAS, ANODIZADOS,
  LACADOS».
- Empresa viva: «fecha último cambio 30-8-2026» en Empresite.
- Sin opiniones con recuento verificado → **no se declara `aggregateRating`**.

---

## Por qué se descarta «tesela» (Calle de Colombia 18)

Falla la regla (d) y además huele a negocio parado:

- **Sin canal escribible.** Solo el fijo 913592375. Buscado el correo en la ficha
  de Facebook (pestaña de contacto completa, no publica correo), Páginas
  Amarillas —donde ese mismo teléfono figura como «PEDRO HERRERO», Colombia 18
  bajo—, Citiservi, Infoisinfo, Cylex, einforma, qdq y búsquedas del nombre y del
  número en Google, Bing y DuckDuckGo. Cero correos, cero móviles.
- **Señales de negocio parado.** Su Facebook (`teselascocinas2`, «Tesela Estudio
  de Decoración», 42 seguidores) no publica nada desde el 14/01/2016, y la web
  que enlaza esa ficha, `emocioncocinas.es`, devuelve el vhost por defecto de
  SiteGround y sus rutas dan 404.
- **Contexto.** La ficha dice «Estamos en el Grupo Emoción»: era una de la decena
  de tiendas asociadas a Emoción Cocinas. Tienda única, sí, pero el grupo y la
  tienda llevan una década sin rastro.

## Los otros de la zona este que se cayeron, para no repetirlos

Todos con web propia: **Magenta** (enmarcaciones, Colombia 20 →
`enmarcacionesmagenta.es` y `marcosmoldurasmadrid.com`), **Helmar 3000**
(Chile 6 → `helmar3000.com`), **Tafetán** (→ `tafetan.com`), **Fernando Cler
Relojeros** (→ `fernandoclerrelojeros.com`), **Tarimas del Mundo**, **Merino
Piscinas**, **Marca Sacra Tattoo** (→ `marcasacrattattoo.com`, y además está en
Ciudad Lineal, no aquí). **Mercería La Antigua** (Costa Rica 13) se cae por la
regla (d): solo fijo 913457605, ningún correo ni móvil publicado, y tiene una
página automática de Google (`merceria-la-antigua.negocio.site`).
