# Molde: arreglos de ropa

Duodécimo molde. Vale para **costurera de barrio, taller de arreglos, sastre de
retoques, modista**: el local de tres metros donde entra una prenda que ya se
compró y sale puesta.

No confundir con `taller.md` (coches) ni con `reparaciones.md` (casa). Aquí lo
que se repara es algo que la persona se pone encima.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se vende costura, se vende un veredicto

Nadie entra en un taller de arreglos con ganas. Se entra con una bolsa y una
prenda dentro que lleva meses en el armario: el pantalón que sobra de cintura
desde el año pasado, la americana de la boda, la cremallera del plumífero, el
vestido que costó 200 € y no se ha puesto nunca.

La persona no pregunta «qué servicios ofrecen». Pregunta tres cosas, en este
orden y sin variar nunca:

> **1. ¿Esto tiene arreglo?**
> **2. ¿Cuánto me va a costar?**
> **3. ¿Para cuándo lo tengo?**

Y no llama para preguntarlo, porque explicar por teléfono que «me sobra tela
aquí detrás» es imposible. Así que no llama: deja la prenda en el armario otro
mes. Ese es el cliente que se pierde, y no se pierde por precio.

> Regla del molde: la sección más importante no es la lista de arreglos. Es
> **la tarifa orientativa escrita en euros**, y justo detrás **«mándeme una
> foto por WhatsApp y le digo si tiene arreglo»**. Una foto es el mostrador.
> Ninguna costurera del barrio lo publica, y es lo único que convierte el
> armario en una visita.

El segundo eje del molde es **la honestidad al revés**: decir qué NO compensa
arreglar. Un taller que escribe «esto no se lo haga, le cuesta más que la
prenda» gana la confianza entera en una frase. Es gratis y no lo hace nadie.

Si el sitio hace **prueba puesta**, va delante: es la diferencia entera con
comprar una talla menos por internet, y explica por qué no es un servicio de
un día.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: la prenda, no el oficio** | «El pantalón que no se pone porque le sobran cuatro dedos» vende; «arreglos y confección» no. Botón de WhatsApp con la foto, no de llamar. |
| 2 | **Tira** | Calle · horario · móvil. En este sector el móvil es el negocio: va entero. |
| 3 | **La tarifa, en euros** | Seis u ocho arreglos con precio orientativo y el porqué de la horquilla (vaquero con vuelta original ≠ bajo recto). Es la pieza clave. |
| 4 | **Mande una foto** | Tres pasos: foto de la prenda, foto puesta, qué le sobra o le falta. Con la frase de que responder es gratis y no compromete. |
| 5 | **Cuánto se tarda** | Plazo normal, plazo con prisa y plazo de boda/evento. Con fechas de verdad («tres días», no «plazos ajustados»). |
| 6 | **Qué no compensa arreglar** | Tres o cuatro casos, con el motivo. La sección que hace que la página se guarde. |
| 7 | **Dónde se puede meter una prenda y dónde no** | Un dibujo del mapa de costuras. Explica el oficio sin jerga y justifica el precio. |
| 8 | **La prueba** | Se prueba puesto, con el zapato que se vaya a llevar. Si no hay prueba, se dice. |
| 9 | **Horario día a día y cómo llegar** | Día a día, con el corte del mediodía escrito: en este sector el cierre de 14 a 16 es la mitad de las visitas fallidas. |
| 10 | **Quién eres + nota única + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** galería de vestidos de novia de banco de imágenes, ni «más de 20
años de experiencia» sin decir desde cuándo, ni formulario de presupuesto. El
presupuesto de un arreglo se da viendo la prenda; fingir lo contrario con un
formulario de ocho campos es perder al cliente dos veces.

---

## La receta visual

El sector tiene una paleta propia y casi nadie la usa: **jaboncillo de sastre
sobre papel de patrón**. La tiza de marcar viene en blanco, azul y amarillo, y
el papel de los patrones es crudo. Ni rosa de mercería ni dorado de alta
costura: esto es un oficio de mesa, tijera y luz.

```css
:root{
  --fondo:#f7f3ec;  --fondo-2:#e9e1d3;    /* papel de patrón, cartón de molde */
  --tinta:#221e1b;  --tinta-2:#6a6159;
  --acento:#2f5d73;                        /* azul de jaboncillo */
  --tiza:#c9a227;                          /* amarillo de jaboncillo, solo marcas */
  --linea:#d8cfbe;
  --radio:0px;
}
```

Tres reglas del sector:

1. **La línea discontinua es la firma.** Un hilván es una línea de puntos. Los
   separadores, los bordes de las tarjetas de tarifa y los subrayados del hero
   van en `dashed` o con `repeating-linear-gradient`. Es lo único que hace que
   la página se vea *de costura* sin una sola foto de tela.
2. **Nada de cursiva de boutique.** El titular va en serif de texto, con peso,
   no en script. Aquí se vende oficio, no romanticismo.
3. **Los números mandan.** Los euros y los días van grandes, tabulares
   (`font-variant-numeric:tabular-nums`) y en la tipografía de titulares. Son
   la respuesta a las tres preguntas.

---

## Los textos

- **El titular es la prenda parada en el armario.** *«Ese pantalón que no se
  pone porque le sobran cuatro dedos.»* Nunca «arreglos de ropa en Madrid».
- **El precio con su horquilla y su motivo.** *«Bajo de vaquero, 10 €. Con la
  vuelta original, 14 €: hay que descoserla y volver a montarla.»*
- **El plazo en días, no en adjetivos.** *«Tres días. Si corre, para mañana.»*
- **El no, escrito.** *«Un abrigo no se estrecha de hombros: hay que
  desmontarlo entero y sale por encima de lo que costó.»*
- **La foto como puerta.** *«Mándeme una foto de la prenda y otra puesta. Le
  digo si tiene arreglo y cuánto, sin que venga.»*
- **Sin superlativos de oficio.** Ni «manos expertas», ni «pasión por la
  costura», ni «alta costura». El auditor caza los tópicos y el cliente
  también.

---

## El JSON-LD

`@type`: **`LocalBusiness`** (schema.org no tiene un tipo de sastrería;
`ClothingStore` es una tienda y aquí no se vende ropa). Lleva `telephone` con
el móvil en formato `+34`, `address`, `geo`, `openingHours` **con el corte del
mediodía partido en dos rangos** —`Mo-Fr 10:00-14:00` y `Mo-Fr 16:00-20:00`— y
`makesOffer` con los arreglos si la tarifa es real.

**Sin `aggregateRating`** salvo nota **y** recuento verificados. En este sector
las fichas de directorio copian la nota de Google sin el recuento: no vale.
