# Molde: joyería de barrio con taller

Duodécimo molde. Vale para **joyería, relojería, platería y compra de oro**:
todo negocio donde alguien entrega una cosa pequeña, cara y con historia, y se
va sin ella.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se venden joyas

Contra el escaparate de Tous, contra una tienda online y contra El Corte Inglés,
una joyería de galería **no gana enseñando producto**. Pierde siempre: menos
catálogo, menos foto, menos precio.

El cliente que sí es suyo no viene a comprar. Viene con **una cosa rota en el
bolsillo** y dos preguntas que no se atreve a hacer por teléfono:

> **«¿Me lo arregláis?»** y **«¿me lo vais a tasar sin engañarme?»**

Un cierre que se suelta, una alianza que aprieta, una cadena partida, un reloj
parado desde hace dos años, y la caja de la abuela que nadie sabe si vale 40 €
o 4.000. Eso se busca en Google a las once de la noche, y casi ninguna joyería
lo tiene escrito en ninguna parte.

> Regla: la sección más importante es **la lista de arreglos con su precio y
> los días que tarda cada uno**. No es la vitrina. La vitrina la tiene todo el
> mundo; el taller, no.

El segundo eje es la **desconfianza**. En oro y en tasación el cliente da por
hecho que le van a engañar, porque no sabe pesar ni leer un punzón. Por eso
aquí la transparencia no es un valor de marca: es el producto. Explicar cómo se
pesa, delante de quién, y con qué precio del gramo, vende más que cualquier
adjetivo.

**El taller propio es la única ventaja defendible.** Si las piezas se mandan
fuera, la joyería es una tienda más. Si el taller está detrás del mostrador,
eso se dice en el `<h1>`.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: el taller, no la vitrina** | «El taller está detrás del mostrador» gana a «joyería y relojería desde 1985». Dibujo del banco de joyero, no un anillo. |
| 2 | **Tira** | Calle y portal · galería o local · horario · teléfono. |
| 3 | **Arreglos: precio y días** | La pieza clave. Fila por arreglo: qué es, **desde cuánto** y **cuántos días**. Usa `u-precios` con una tercera columna de plazo. Mínimo ocho filas: pila de reloj, ajustar alianza, soldar cadena, cierre nuevo, enfilar collar, baño de rodio, grabado, engaste. |
| 4 | **Lo que se puede esperar en el día** | Tres o cuatro cosas que se hacen mientras el cliente espera. Desbloquea la visita de hoy: no hay que dejar la joya. |
| 5 | **Cómo se tasa** | Tres pasos numerados (`u-numerada`): se mira el punzón con lupa, se pesa, se dice un número y **se puede decir que no**. Aquí va el dibujo de la lupa sobre el punzón. |
| 6 | **Compra de oro, si la hacen** | Precio del gramo **del día**, báscula a la vista, y que el peso se hace delante. Si no compran oro, esta sección se cae entera: no se rellena con humo. |
| 7 | **Relojería** | Pilas, correas, juntas y estanqueidad. Marcas que se reparan o distribuyen, si son verificables. |
| 8 | **Horario día a día, dónde y teléfono** | Con la planta de la galería si el local está dentro de una: la gente no encuentra la puerta. |
| 9 | **Opiniones** | Solo si están verificadas y con firma. Sin recuento real, la sección no existe. |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** vitrinas de fotos de anillos genéricos, ni «alta joyería», ni
precios de venta de producto (cambian cada semana y envejecen la página en un
mes), ni el nombre de una marca que distribuyen puesto como si fuera el suyo.

---

## La receta visual

```css
:root{
  --fondo:#f4f1ea;   --fondo-2:#e7e1d4;   /* papel de joyero, no blanco tienda */
  --tinta:#191b21;   --tinta-2:#5c5d66;
  --acento:#7a5a1e;                        /* latón: el metal del taller */
  --acento-tinta:#fdfbf4;
  --linea:#cdc5b2;
  --punzon:#8c2f39;                        /* el rojo del sello, solo marcas */
  --radio:0px;
}
```

Cuatro reglas del sector:

1. **Nada de negro con dorado brillante.** Es el uniforme del lujo y aquí no se
   vende lujo: se vende que le arreglen una cosa. El negro-oro dice «caro» justo
   cuando hay que decir «pase, que esto se mira gratis».
2. **Latón mate, no oro.** El metal de un taller está oxidado y rayado. Un
   dorado saturado convierte la página en un anuncio de perfume.
3. **Una romana o inscripcional en los titulares.** El punzón de contraste se
   graba en mayúsculas romanas: esa es la letra del oficio. Con caps, `line-height`
   nunca por debajo de `1.1` y `letter-spacing` en positivo, o las tildes chocan.
4. **Las cifras, tabulares.** `font-variant-numeric:tabular-nums` en la tabla de
   arreglos: una columna de precios desalineada resta credibilidad sola.

**Los dibujos que hay que dibujar** (nunca clipart, nunca un anillo bonito):
el mandril cónico con la alianza y el maceto, la balanza de precisión con su
pesa, la trasera del reloj abierta con la junta y la pila, y la lupa sobre el
punzón grabado dentro del aro. Los cuatro son de este oficio y de ningún otro.

---

## Los textos

- **El titular es el taller.** *«El taller está detrás del mostrador. Su joya no
  sale de aquí.»* No *«joyería y relojería de confianza»*.
- **El plazo, siempre pegado al precio.** *«Soldar una cadena de oro — desde
  25 € — en 2 días.»* Un precio sin plazo no sirve para decidir.
- **La frase que desarma.** *«Mirarlo y decirle qué es no se cobra.»* Es lo que
  el cliente quiere oír antes de entrar con la caja de la abuela.
- **El derecho a irse.** *«Se le dice un número y usted decide. Si dice que no,
  se lo lleva igual de entero que vino.»* Sin esto, la compra de oro huele.
- **Nada de años inventados.** «Desde 1985» solo si está verificado. Si no, se
  dice «empresa familiar del barrio» y punto.
- **Ningún superlativo sobre piedras.** «Diamante de la mejor calidad» no
  significa nada y es la frase de todas las webs del sector.

---

## El JSON-LD

`@type`: **`JewelryStore`** (subtipo de `Store` bajo `LocalBusiness`). Lleva
`openingHours` día a día, `address` con el portal, `geo` y `telephone`.

Si el negocio hace arreglos, se declaran como `hasOfferCatalog` con un
`OfferCatalog` de `Service`: es el único sitio del sector donde eso está vacío
y es exactamente lo que se busca.

**Sin `aggregateRating`** salvo nota **y** recuento verificados. Y **sin
`priceRange` inventado**: si no se sabe, no se declara.
