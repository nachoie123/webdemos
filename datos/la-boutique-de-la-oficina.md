# La Boutique de la Oficina — verificación (21/09/2026)

Papelería de barrio en Costa Fleming. **Sustituye a `asanarte`**, que era mi
candidato asignado y se cayó (ver el final de esta nota).

## a) ¿Tiene web? NO

- `python3 sistema/tiene_web.py "La Boutique de la Oficina"` → no la marca.
- Dominios probados uno a uno con `curl` (https y, si falla, http):
  `laboutiquedelaoficina.es` y `laboutiquedelaoficina.com` → **no resuelven**
  (HTTP 000, sin registro A).
- Sitio automático de Google: los directorios citan
  `laboutiquedelaoficina.negocio.site` → **404 de Google**. El enlace está
  muerto, no hay ficha-web.
- Búsqueda del nombre: solo directorios (Páginas Amarillas, Citiservi, Kompass,
  anuario-horario, busqueda-local) y la ficha del barrio. Ninguna web propia.
- OSM: `shop=stationery` sin `website` ni `contact:website`.

## b) ¿Negocio pequeño? SÍ

Un solo local, sin franquicia. La razón social es **FB 7, S.A.** (Kompass y
espainfo, misma dirección: Félix Boix 7 local izq.). La ficha de la asociación
de comerciantes del barrio la describe como *papelería como las de antaño, con
más de 30 años de historia*, y dice que atiende **Fernando**. Busqué
«La Boutique de la Oficina franquicia» → nada. No hay segundo local.

## c) Dirección — tres fuentes, mismo portal

- **Reverse de Nominatim** con las coords de la ficha OSM (40.4634404,
  -3.6876017) → *«La Boutique de la Oficina, 7, Calle de Félix Boix, Costa
  Fleming, Nueva España, Chamartín, Madrid, 28036»*.
- OSM: `addr:street=Calle de Félix Boix`, `addr:housenumber=7`,
  `addr:postcode=28036`.
- Páginas Amarillas: *«Felix boix, 7 (28036)»*. Kompass: *«C/ Felix Boix 7
  Local Izq.»*.

Los tres coinciden en el **7**, así que el portal sí se pone.

## d) Canal escribible — SÍ, correo publicado

**`fb7@telefonica.net`**, publicado por la propia ficha del negocio en
**costafleming.es**, la web de la asociación de comerciantes del barrio
(`/portfolio-item/la-boutique-de-la-oficina/`). Ahí van juntos el teléfono, la
dirección, el horario y el correo. Segunda fuente: Citiservi da el mismo
correo.

- Fijo: **91 345 06 20** (misma ficha). Es fijo, así que no vale por sí solo.
- Móvil: no publican ninguno. No me lo invento.
- `via` = **email**.

## Horario (fuentes que coinciden)

OSM (`check_date:opening_hours=2026-07-29`) y costafleming.es dan lo mismo:
lunes a viernes 09:30–14:00 y 17:00–20:00; sábados 11:30–14:00; domingos
cerrado. Va tal cual en la página y en `openingHours`. **No está inventado.**

## Opiniones

No he encontrado un recuento verificado, así que **no se declara
`aggregateRating`** y no hay sección de reseñas.

---

## Por qué se cayó `asanarte` (candidato asignado)

**Tiene web propia.** `https://asanarte.es` responde 200 con
`<title>Fisioterapia en Chamartín | Asanarte</title>`: WordPress completo, con
tarifas, blog y ficha de la fisioterapeuta (Julia Utgés Blesa, colegiada 1341).
Es el mismo negocio, no un homónimo: el móvil de su web, **683 274 397**, es el
segundo teléfono del nodo de OSM (`+34910660911;+34683274397`). Además la web
da otra dirección —C. del Padre Damián 37— distinta de la que sale del reverse
de Nominatim (Calle del General Gallegos), señal de que la ficha de OSM está
vieja.

Con web propia y viva no entra. No llegué a buscarle correo: sobra.

## Los que también miré y descarté antes de llegar aquí

Barrido propio de Overpass en la zona centro-sur (40.4600,-3.6860):

| Negocio | Por qué no |
|---|---|
| Resorespy (fisio, Juan Ramón Jiménez) | `resorespy.com` responde 200 |
| Fisio for all (C. Pensamiento) | `fisioforall.com` |
| Fisiofix (Mateo Inurria 11) | `fisiofix.es` |
| Clínica Progresa | `clinicaprogresa.com` |
| Fisio Salud + | `fisioweb.com` |
| Concasa (podólogo) | sin rastro: ni teléfono ni correo que verificar |
| Fernando Cler Relojeros | `fernandoclerrelojeros.com` |
| Gala Autoescuela | cadena de más de 65 sedes |
| Irán alfombras persas | `iranalfombras.com` (503, pero servidor vivo) |
| Doña Tomasa | tienda online completa en `donatomasa.com` |
| Herbolario La Vita | los directorios le dan `e-lavita.com` |
| Old School Nutrition | `oldschoolnutrition.es` |
| Residencia Imbea | `clinicaimbea.com` |
| Elidiz (zapatero, Carlos Maurrás 9) | sin web (dominio aparcado en STRATO) y con móvil 647 686 363, pero el sector **zapatero** ya lo cogió otro agente de esta tanda (`reparacion-calzado-jt`) |
| La Modista Diana | sector ya cogido (`el-dedal-de-sandra`, molde `arreglos-de-ropa.md`) |
| Sisquibikes | no encuentro teléfono ni correo publicados en ningún sitio |
