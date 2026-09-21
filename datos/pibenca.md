# Pibenca — notas de verificación (21/09/2026)

**Candidato final.** El asignado (Tartalia) se descartó; abajo el motivo.

---

## 1. Tartalia — DESCARTADO, no se gastó demo

Dos motivos, cualquiera de los dos basta:

- **Es una cadena.** `top-tiendas.es/cadena-tiendas/230-tartalia` lista **27
  establecimientos** (11 en Madrid capital, entre ellos el de Avenida de
  Asturias 23, más Getafe, Leganés, Alcorcón, Móstoles, Guadalajara…), y
  mundofranquicia titula «Tartalia suma ya 35 establecimientos». El brief
  descarta a partir de 2-3 locales.
- **Tiene web.** `web.tartalia.es` — «Tartalia | La Pastelería de Siempre».

Extra: einforma habla de «TARTALIA SA (EN LIQUIDACIÓN)». Ni el molde
`pasteleria-encargos.md` ni la demo se llegaron a escribir: sin negocio
verificado no se escribe nada.

Las coordenadas sí eran correctas (reverse de Nominatim sobre
40.46772,-3.69356 devuelve «Tartalia, 23, Avenida de Asturias, Almenara,
Tetuán, 28029»), pero eso no salva ni la cadena ni la web.

---

## 2. Pibenca — el que sí

No había reserva asignada, así que barrido propio de Overpass
(`nwr(around:750,40.4680,-3.6950)` sobre `shop`/`office`/`craft`/`healthcare`
/`amenity`, sin `website`). 488 nodos, 58 con contacto. De los que quedaban
libres (AEP, Grupo Sígame, Pedro Durán y La Morenita son de otros agentes),
Pibenca es el único con **canal escribible confirmado por dos fuentes
independientes**.

**Nombre:** Pibenca (Pibenca S.L.). En la ficha de Google aparece como
«Piensos Pibecan / Pibenca», así que el rótulo de la calle puede decir
**Pibecan**: queda anotado en la nota de la página para que lo confirme él.
OSM, el registro mercantil y Páginas Amarillas dicen Pibenca.

### a) No tiene web — comprobado por cuatro vías

| Comprobación | Resultado |
|---|---|
| OSM | Sin `website` ni `contact:website` |
| `pibenca.es / .com / .net`, `pibecan.es / .com`, `piensospibecan.es` | **Ninguno resuelve** (DNS) |
| Empresite (eleconomista) | Campo «web» vacío |
| `pibenca.edan.io` | Listado **autogenerado** por edan.io a partir de la ficha de Google, con botón «Manage Listing / create your website». No es suya. |
| `pibenca.widl.es` (la «web oficial» que anuncia edan.io) | **No resuelve.** `getaddrinfo ENOTFOUND` |

No hay homónimo que ensucie: el único choque de nombre era «Pibecan», que
resulta ser el mismo comercio.

### b) Es de barrio, no cadena

Empresite: **Pibenca S.L.**, CIF B78013539, sociedad limitada **viva**, alta
el **25/02/1985**, **2 empleados** (dato de 2025). Un solo local. Ninguna
fuente le conoce una segunda dirección.

### c) Dirección — dos fuentes de acuerdo en el portal

- Reverse de Nominatim sobre 40.4654804,-3.6934169 →
  «Pibenca, **2**, Calle de las Aguileñas, Almenara, Tetuán, Madrid, **28029**».
- qdq: «Calle Aguileñas 2, (Edif. Bravo Murillo, 359), Tetuán-Almenara».
- Páginas Amarillas: «Calle Aguileñas, 2».

Coinciden → **el portal sí se puede escribir**: Calle de las Aguileñas 2. El
detalle del edificio (Bravo Murillo 359) explica que haga esquina.

### d) Canal escribible — **correo, confirmado dos veces**

`pibenca@yahoo.es`

1. OSM, etiqueta `contact:email` del propio nodo.
2. Empresite / elEconomista, ficha societaria de PIBENCA SL (misma dirección,
   mismo teléfono, mismo CIF).

**No tiene móvil.** El 917337488 es fijo, así que no hay WhatsApp: `via` =
`email`. Nada inventado; si el correo rebota, no hay segundo canal.

### e) Horario — las dos fuentes discrepan media hora

- edan.io (espejo de la ficha de Google, © 2026): L-V 9:30–14:30 y 17:00–20:00;
  S 10:00–14:00; D cerrado.
- esopiniones (otro espejo de Google): L-V 9:00–14:00 y 17:00–20:00;
  S 9:00–14:00.

Se usa el primero, **marcado con `data-ejemplo`** y con una línea pidiéndole
que lo confirme. Mismo criterio que el brief manda para los portales en
conflicto.

### f) Nota de Google — NO se declara

Los directorios dan 4,8 con **337**, **351** y **38** opiniones según cuál se
mire. Sin un recuento fiable no se declara `aggregateRating` ni se copia
ninguna reseña.

### g) Qué vende, según las opiniones públicas

Pienso de perro, gato, hámster y pájaro; alpiste y mixturas; collares
antiparasitarios; casitas de pájaro; suplementos; y **semillas de huerta y
jardín**. El CNAE de la sociedad es «comercio al por mayor de cereales,
tabaco en rama, simientes y alimentos para animales en general», que encaja
con lo del granel.
