# Talleres Jurado y López, C.B. — datos verificados

Comprobado el 21/09/2026.

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Talleres Jurado y López, C.B. | ASETRA Madrid, Empresite, Yelp |
| Rótulo en OSM | «Talleres Jurado» | OpenStreetMap + reverse de Nominatim |
| Dirección | **Calle de la Infanta María Teresa, 12** | dos fuentes que coinciden: reverse de Nominatim y ficha de ASETRA |
| Barrio | Hispanoamérica · Chamartín · 28016 Madrid | Nominatim |
| Coordenadas | 40.4540336, −3.6808036 | nodo de OpenStreetMap |
| Fijo | 914577637 | ASETRA, Empresite, Yelp, OSM |
| **Móvil (WhatsApp)** | **699638306** | ficha de ASETRA Madrid |
| **Correo publicado** | **antoniojurado56@gmail.com** | ficha de ASETRA Madrid |
| Servicios | Electricidad · Mecánica · Neumáticos | iconos de servicio de la ficha de ASETRA |
| CNAE | 4520 (mantenimiento y reparación de vehículos) | Empresite / einforma |
| Web propia | **No tiene** | ver abajo |

## Por qué no tiene web

1. **Ningún dominio derivado del nombre está vivo.** Probados `.com` y `.es`,
   con y sin `www`, en http y https, para `talleresjuradoylopez`,
   `juradoylopez`, `talleresjuradolopez` y `juradolopezmecanicos`. Cero
   respuestas.
2. **`talleresjurado.com` sí existe, pero es otro negocio.** Su propia página
   dice «Estamos en **Estepa (Sevilla)**» y «desde 1985, segunda generación».
   Es el homónimo clásico, el mismo tropiezo que `talleresjl.es`. No es éste.
3. **Ninguna de las fichas del sector le pone web:** ASETRA Madrid (la
   asociación de talleres de Madrid, que es quien publica sus datos de
   contacto), Empresite, einforma, Yelp, autingo, talleresdeconfianza. Todas
   dan teléfono y dirección; ninguna, dominio.
4. **OpenStreetMap** tampoco: el nodo tiene `phone` y no tiene `website`.

## El canal escribible

Es lo que salvó al candidato. **ASETRA Madrid publica móvil y correo**, los dos:
`699638306` y `antoniojurado56@gmail.com`. Se puede escribir por WhatsApp y por
correo, así que en la ficha va `"via": "ambos"`. No hay nada inventado: el fijo
por sí solo no habría valido.

## Cómo llegué aquí (el candidato asignado se descartó)

El candidato de la tanda era **Formación en la nube** (Calle de Colombia 14 C,
fijo 914169137). **Tiene web propia y viva:** `formacionenlanube.com`, WordPress
con tema Zerif Lite, menú de siete secciones y noticias de 2023. Y el teléfono
que aparece en su pie es `+34 91 416 91 37`, exactamente el de la ficha: es
ella, no un homónimo. Descartado sin gastar una línea de HTML.

Descartados también, de mi propio barrido de Overpass (700–900 m alrededor de
40.4560, −3.6790), y anotados para que nadie los vuelva a mirar:

- **Farmacia Reyes / Sagrados Corazones** (Glorieta de los Sagrados Corazones 4).
  Sin web —`farmaciareyes.es` es una página aparcada de hosting y
  `sagradoscorazones.info` no resuelve—, pero **sin correo ni móvil publicados
  en ninguna fuente**. Sin canal escribible, fuera.
- **Autoescuela Fórmula** (Chamartín). Dos direcciones distintas en dos fuentes
  (Pradillo 4 según el directorio, Calle Mantuano según el reverse) y
  `autoescuelaformula.es` vivo y sin poder confirmar de quién es. Demasiado
  turbio.
- **Instituto Kojachi** y **LinguaEstudio**: los dos tienen web propia.

## Lo que no se declara en la demo

- **Nota y opiniones:** no hay recuento verificado en ninguna fuente. Sin
  `aggregateRating` y **sin sección de opiniones**.
- **Horario:** no lo publica nadie. El de la página está inventado y marcado con
  `data-ejemplo`, igual que en el `openingHours` del JSON-LD.
- **Precios de diagnosis y de mano de obra:** inventados y marcados. Son el
  corazón de la página y hay que sustituirlos antes de enseñársela a nadie.
- **Antigüedad:** Empresite le calcula unos 30 años de actividad, pero no está
  confirmado por el propio taller. **No aparece ninguna cifra de años en la
  página.**
- **Marcas y equipos de diagnosis:** no se nombra ninguna. No hay dato.
- Sí se dice que está **asociado a ASETRA**, porque sale de su ficha en el
  directorio de la propia asociación, y va marcado como dato real.
