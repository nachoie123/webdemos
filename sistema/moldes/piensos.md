# Molde: tienda de piensos

Duodécimo molde. Vale para **tienda de piensos, granero, cerealista,
alimentación animal y forrajes**: el comercio que vende el saco, no la mascota.

No confundir con dos moldes que ya existen y que atacan otra cosa:
`salud.md` cubre al **veterinario** (le duele algo al animal) y la demo
`shyba-peluqueria-canina` cubre la **peluquería canina** (hay que pedir cita).
Aquí no hay cita ni diagnóstico: hay un saco y una fecha.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se vende comida, se vende no tener que cambiar de marca

El cliente de una tienda de piensos **ya sabe lo que quiere**. Lleva dos años
dándole la misma referencia a su perro, a su gato o a sus canarios, y no
piensa cambiarla: cambiar de pienso es diarrea, es un gato que deja de comer,
es empezar otra vez. No entra a que le recomienden nada.

Entra con una sola pregunta, y no es «qué vendéis»:

> **«¿Tenéis hoy el saco exacto que yo le doy, y si no lo tenéis, qué día
> lo tendréis?»**

Esa es la página entera. Todo lo demás —las marcas, los accesorios, los años
que lleva abierto— es relleno hasta que esa pregunta esté contestada.

Detrás viene la segunda, que es física y nadie la escribe:

> **«Son quince kilos. ¿Me los lleváis a casa?»**

Un saco grande no se sube andando a un cuarto sin ascensor, y esa es
exactamente la razón por la que la gente se pasa a comprar por internet
aunque prefiera la tienda del barrio. Una página que dice «se reparte, este
día, hasta aquí» recupera a ese cliente sin bajar un céntimo el precio.

> Regla: la sección más importante **no es el catálogo**. Es **«cómo se
> encarga y en cuántos días llega»**, con el plazo escrito. Una tienda de
> barrio no puede competir en catálogo con una web que tiene 9.000
> referencias. Compite en que el jueves está el saco esperando con su nombre.

**El tercer freno, el que decide el precio: el formato.** El saco de 3 kg del
supermercado y el de 15 kg de la tienda parecen lo mismo y no lo son. Poner
el **precio por kilo** de cada formato es el argumento más fuerte que tiene
este negocio y ninguna tienda de piensos lo publica.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: el saco, no la marca** | «El saco de siempre, o le decimos el día que llega.» Botón de encargar por el canal que tenga. Dibujo del saco. |
| 2 | **Tira** | Calle · horario · teléfono · correo. |
| 3 | **Cómo se encarga** | Tres pasos numerados (`u-numerada`) **con su plazo en días**. La pieza clave del molde. Qué hay que decir: marca, referencia y kilos. |
| 4 | **El reparto** | Hasta dónde llega, qué días, desde cuántos kilos o euros, y si se sube a casa. Sin esto la sección 3 queda coja. |
| 5 | **Formatos y precio por kilo** | `u-precios` con el mismo pienso en tres tamaños y **el precio por kilo al lado**. El argumento entero del negocio. |
| 6 | **Lo que no hay en el supermercado** | El granel (alpiste, mixturas, semillas de huerta), lo de los animales raros, lo de siempre que ya no fabrica nadie. Aquí se dibuja **la planta del local**. |
| 7 | **Dietas que ha mandado el veterinario** | Cómo se pide una referencia de prescripción: traer la foto de la bolsa. **Sin una palabra de salud:** ni consejos, ni «mejora», ni «recomendamos». Se busca lo que le hayan mandado, punto. |
| 8 | **Horario día a día y cómo encargar** | Tabla de siete filas y el canal escribible. |
| 9 | **Opiniones** | Solo si están verificadas con nombre y origen. Si no, **no va la sección**. |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** fotos de cachorros mirando a cámara, ni «amamos a los animales»,
ni catálogo por marcas con logotipos ajenos (esos logos no son suyos), ni
consejos de nutrición animal. Y **ningún emoji de pata**.

---

## La receta visual

El error del sector es el rosa y el celeste de *pet shop*. Esto no es una pet
shop: es **un almacén de grano**. Papel de saco, tinta de sello, letras
gordas como las que van estarcidas en la tela.

```css
:root{
  --fondo:#efe6d2;   --fondo-2:#e2d5b6;   /* papel de saco, dos tonos */
  --tinta:#22190f;   --tinta-2:#5e5240;
  --acento:#6b3a1f;                        /* castaño quemado: el sello del saco */
  --grano:#3d5226;                         /* verde alfalfa, solo acentos */
  --linea:#cfc0a0;
  --radio:2px;                             /* casi recto: esto es un almacén */
}
```

Tres reglas del sector:

1. **Un slab serif en titulares.** El rótulo de un granero nunca fue una
   geométrica fina. Peso 600-700, que pese como un saco.
2. **Cifras tabulares en todo lo que sea kilos y euros.**
   `font-variant-numeric:tabular-nums`. La sección de formatos se lee en
   columna y con cifras proporcionales no cuadra.
3. **Textura de tela, no gradientes.** Una trama de líneas diagonales muy
   suaves en `--fondo-2` hace de arpillera y cuesta 6 líneas de CSS. Nada de
   sombras difusas.

---

## Los dibujos

Este es el molde donde los dibujos hacen más trabajo, porque el producto es
un bulto físico y el cliente compra por tamaño:

- **El saco, de frente**, con la costura de arriba, el asa y la etiqueta.
- **Los tres formatos a escala real entre sí** (3 / 7,5 / 15 kg). Un dibujo
  que además es la tabla de precios: se ve de un vistazo por qué el pequeño
  sale caro.
- **La planta del local**: mostrador, pared de sacos, los cubos del granel y
  la puerta. Es lo que ningún competidor puede copiar, porque es su tienda.

---

## Los textos

- **El titular es el compromiso, no el surtido.** *«El saco de siempre, o le
  decimos el día que llega.»*
- **El plazo, con número.** *«Lo que no está, en 48 o 72 horas.»* «Pronto» no
  vale: la gente calcula si le llega antes de que se acabe el saco de casa.
- **El peso y el precio por kilo, juntos.** *«15 kg — 52 € — 3,47 €/kg.»*
- **Hablar de referencias, no de marcas.** *«Dígame marca, sabor y kilos»* es
  lo que hace falta para pedirlo; *«trabajamos con las mejores marcas»* no
  sirve para nada.
- **Cero consejo veterinario.** Se busca y se vende lo que le hayan mandado.

---

## El JSON-LD

`@type`: **`PetStore`** (bajo `LocalBusiness`). Si el negocio es más
cerealista que tienda de mascotas vale `Store`. Lleva `openingHours` día a
día, `address`, `geo` y `email` o `telephone`. **Sin `aggregateRating`** salvo
nota **y** recuento verificados — en este sector los directorios se copian
unos a otros y dan tres recuentos distintos para la misma tienda.
