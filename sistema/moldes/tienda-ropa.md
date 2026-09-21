# Molde: tienda de ropa de barrio

Duodécimo molde. Vale para **boutique de moda, complementos, mercería de ropa,
zapatería pequeña**: todo comercio que vende prendas de pocas unidades y que
compite, sin poder ganar, contra un catálogo infinito.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se vende ropa, se vende «he encontrado algo»

La tentación del sector es montar un catálogo. Es la decisión equivocada y se
pierde siempre: Zara tiene más modelos, Shein tiene más baratos y el Instagram
de la competencia tiene mejores fotos. Una tienda de barrio con doce metros de
escaparate no puede ganar esa comparación y no debe entrar en ella.

Lo que esta tienda tiene y el catálogo no es **escasez**: dos unidades por
talla, una remesa nueva cada semana, y la pieza buena volada en tres días. Eso,
que parece una debilidad, es justo el argumento.

Pero la escasez tiene un precio para el cliente, y ese precio es **el miedo a
gastar el viaje**. Bajar a la tienda, subir la cuesta, aparcar, y que no haya
nada. O que haya, pero no en su talla.

> Regla: la sección más importante no es la lista de marcas. Es **«qué ha
> entrado esta semana y en qué tallas queda»**, seguida de **«te lo aparto»**.
> La página no vende prendas: vende la certeza de que el viaje merece la pena.

El segundo freno llega después de la compra: **«¿y si en casa no me vale?»**.
En una tienda grande la devolución se da por hecha; en una pequeña, nadie sabe
si existe. Escribir la política de cambios —aunque sea restrictiva— convierte
una duda en una decisión.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: el ritmo, no la marca** | «Lo bueno entra el martes» vende más que «Moda y complementos». Botón de WhatsApp, que es donde se aparta. |
| 2 | **Tira** | Dónde está exactamente (planta y local, si está en galería) · horario · teléfono. |
| 3 | **Lo que ha entrado esta semana** | Tres o cuatro piezas **con las tallas que quedan**. La pieza clave. Sin precio no sirve de nada. |
| 4 | **Te lo aparto** | Tres pasos numerados: foto por WhatsApp, se reserva, hasta qué día aguanta. Es el único mecanismo que una tienda pequeña tiene y una cadena no. |
| 5 | **Si no te vale** | Cambios y plazo, en una frase sin letra pequeña. Y las medidas reales, que las tallas mienten entre marcas. |
| 6 | **Dónde está de verdad** | El sector pierde clientes en el último tramo: la tienda está dentro de una galería, en un patio, en un primero. Dibujar el plano vale más que el mapa. |
| 7 | **Horario día a día** | Con el domingo aparte: abrir domingo por la mañana es un argumento, no un detalle. |
| 8 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** catálogo completo, carrito, «síguenos en redes» como sección, ni
lista de marcas en logotipos. Tampoco tallas con nombre de mujer famosa ni
lenguaje de revista («must have», «total look»): el cliente de barrio lo lee
como que la tienda no es para él.

---

## La receta visual

```css
:root{
  --fondo:#f7f2ec;  --fondo-2:#e9dfd2;   /* papel de seda y cartón de caja */
  --tinta:#26201d;  --tinta-2:#6f625a;
  --acento:#8c3b4e;                       /* carmín oscuro, no rosa */
  --laton:#a9803c;                        /* latón: la percha, la etiqueta */
  --radio:2px;
}
```

Tres reglas del sector:

1. **Nada de rosa ni de dorado brillante.** Es el look de la tienda de bolsos
   del centro comercial. Aquí se compite por lo contrario: que la dueña sepa
   quién eres y qué te pusiste el año pasado.
2. **Una didona en titulares** (Bodoni y familia). Es la letra de las revistas
   de moda desde hace dos siglos y hace que doce metros de escaparate parezcan
   una tienda seria. Con una didona, `line-height` nunca por debajo de `1.0`:
   los remates finos y las tildes se cortan.
3. **La etiqueta colgante como motivo.** Una tienda de ropa tiene un objeto que
   ninguna otra tiene: la etiqueta atada con hilo. Sirve de dibujo, de marco de
   precio y de sello de «apartado». Repetirlo cose la página entera.

---

## Los textos

- **El titular es el ritmo de la tienda.** *«Lo bueno entra el martes y el
  sábado ya no está.»* Dice escasez, novedad y urgencia sin prometer nada.
- **La talla, siempre delante.** *«Quedan dos: una M y una L.»* Es el dato que
  decide el viaje; ponerlo detrás del precio es tirarlo.
- **El precio, en euros y sin «desde».** Una prenda con «desde 29 €» no se va a
  ver; una con «34 €» sí.
- **La reserva, con fecha.** No «te lo guardamos», sino *«te lo aparto hasta el
  sábado a las dos»*. Un plazo concreto es lo que hace que el cliente venga.
- **Los cambios, sin letra pequeña.** *«Catorce días, con el tique, y se cambia
  por otra cosa.»* Si no hay devolución en dinero, se dice; disimularlo es peor.

---

## El JSON-LD

`@type` **`ClothingStore`** (bajo `Store` → `LocalBusiness`). Lleva
`openingHours` día a día y `currenciesAccepted` si se declara precio.
**Sin `aggregateRating`** salvo nota **y** recuento verificados. Si la tienda
está dentro de una galería, el `streetAddress` lleva el local: sin él, el mapa
deja al cliente en el portal y la venta se pierde en el último tramo.
