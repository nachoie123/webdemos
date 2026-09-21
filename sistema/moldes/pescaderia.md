# Molde: pescadería (y puesto de mercado)

Escrito el 21/09/2026 para **Pescadería Antonio del Río** (Mercado de San
Enrique, puesto 6, Tetuán). Vale para pescadería, marisquería y, con matices,
para cualquier **puesto de mercado municipal**: un negocio que no tiene puerta
propia, ni escaparate a la calle, ni catálogo posible.

Las clases `u-*` están en `sistema/base.css`.

---

## Qué se vende aquí de verdad

No se vende pescado. **Se vende el trabajo que alguien le hace al pescado
antes de que salga del puesto**: descamarlo, destriparlo, sacarle los lomos,
quitarle las espinas, abrirlo para el horno, cocerlo. Eso es exactamente lo que
el supermercado no tiene, y es lo único que justifica cruzar el mercado en vez
de coger una bandeja de salmón del lineal.

Y ese trabajo tiene un peaje que nadie del sector escribe: **hay que pedirlo en
voz alta, con cola detrás.**

> **La pregunta del cliente es: «me van a preguntar cómo lo quiero y no voy a
> saber qué contestar».**

No es el precio. No es la frescura. Es **vergüenza**. Una generación entera ha
dejado de comprar en el mostrador porque el mostrador parece un examen: te
preguntan si lo quieres a lomos o a rodajas, tú no sabes la diferencia, hay
cinco personas esperando y acabas diciendo «lo que usted vea» con la sensación
de haber quedado mal.

La página entera existe para **quitar ese examen**. Si el dueño lee una sola
línea de la demo, que sea esta: *aquí nadie tiene que saber pedir pescado.*

### Por qué NO es el molde de la carnicería

`carniceria-nicar` ya ataca **«¿cuánto pido?»** (gramos por persona). Aquí la
cantidad es lo de menos y **repetir la tabla de gramos sería calcar la demo
12**. La diferencia es física: la carne llega ya en cortes que todo el mundo
reconoce —filete, chuleta, picada— y solo hay que decir cuánta. El pescado
llega **entero, con cabeza, ojos y espina**, y el cliente tiene que decidir qué
se le hace. Esa decisión es la que no sabe tomar.

**Cantidad = carnicería. Preparación = pescadería.** No se cruzan.

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera pegajosa** | `.cab` + `u-nav` | Marca, menú y **móvil clicable**. En pescadería manda el móvil: se encarga por WhatsApp desde la oficina. |
| 2 | **Hero** | `u-sangrado u-seccion` | El titular es **la frase que desactiva el examen**, dicha por el puesto. Nada de «pescado fresco desde 1980». |
| 3 | **Tira de datos** | `u-tira` | Mercado · número de puesto · calle · horario · móvil. En un puesto, **el número de puesto es la dirección de verdad**. |
| 4 | **Cómo se pide, en dos frases** | `u-grid u-3 u-numerada` | El guion literal: para cuántos sois · cómo lo vais a cocinar · lo demás lo decide el pescadero. **La pieza que desbloquea la visita.** |
| 5 | **Qué se le hace al pescado** | `u-grid u-desigual` + dibujo | La lista del trabajo, con **el dibujo de los cortes**. Y la frase clave: **no cuesta más, va incluido**. |
| 6 | **Lo que hay hoy no cabe en una página** | `u-grid u-desigual-inv` | La sección honesta que no tiene nadie: **no hay catálogo porque manda la lonja**. Se sustituye por una foto diaria por WhatsApp. |
| 7 | **El cocedero** | `u-grid u-2` o bloque destacado | Lo que un lineal no puede hacer: te lo devuelven cocido y al punto de sal. |
| 8 | **Fresco y congelado, sin trampa** | `u-grid u-2` | Los dos, uno al lado del otro, sin decir que uno es malo. Lo mismo que hace `reparaciones.md` con la pieza compatible. |
| 9 | **Encargos y a domicilio** | `u-grid u-desigual` | Navidad, comuniones, bandejas. El encargo es el ticket grande del año. |
| 10 | **Dónde y horario** | `u-grid u-desigual-inv` + plano | Horario **día a día**, plano del mercado con el puesto marcado, Cómo llegar. |
| 11 | **La única nota** | `.nota` | Todas las salvedades juntas, aquí y solo aquí. |
| 12 | **Quién eres + pie legal** | — | Las 5 piezas obligatorias del README. |

**Sin sección de opiniones.** Si no hay recuento verificado no se inventa una
reseña ni se declara `aggregateRating`, y montar una sección vacía solo para
rellenar es peor que no ponerla: se dice en la nota y se acabó.

---

## Lo que este molde PROHÍBE

- **El catálogo de precios fijo.** Es la mentira estructural del sector: el
  precio lo pone la lonja cada madrugada, así que toda lista publicada está
  mal al día siguiente. Quien la pone pierde credibilidad; quien explica por
  qué no la pone, la gana.
- **«Pescado fresco de la lonja»** como titular. Lo dicen los 40.000 puestos de
  España. No distingue nada.
- **Olas, anclas, timones, redes y gaviotas.** Es el clipart del sector. Si el
  dibujo vale para una marisquería de Vigo, no vale para este puesto.
- **Azul marino con cian.** El uniforme visual de la pescadería. Ver la receta.
- **Esconder el congelado.** La mayor parte del marisco se congela a bordo y a
  menudo está mejor que el «fresco» de cuatro días. Decirlo en voz alta es un
  argumento, no una confesión.
- **La tabla de gramos por persona.** Ya es de la carnicería. Aquí sobra.
- **Prometer que siempre hay de todo.** Un puesto que jura tener merluza los
  365 días está mintiendo y el cliente lo sabe.

---

## La receta visual

Concepto: **el hielo picado a las nueve de la mañana.** Gris muy claro con
matiz verde —el color del hielo bajo el fluorescente, no el del mar—, tinta casi
negra con verde, y **un solo coral cálido**: el color de la *carne* del pescado,
no del agua. Ese coral es todo el contraste de la página y va únicamente en lo
que se pulsa y en los números.

```css
:root{
  --fondo:#eef1ef;  --fondo-2:#dfe4e1;    /* hielo, verde-grisáceo, no azul */
  --tinta:#111c19;  --tinta-2:#51625c;
  --acento:#b83f2c; --acento-tinta:#fdf2ef;  /* coral: la carne, no el mar */
  --linea:#c8d0cc;  --plata:#7e8f92;          /* la escama */
  --display:'Rozha One', Georgia, serif;
  --texto:'Gantari', 'Helvetica Neue', Arial, sans-serif;
  --radio:0px;
}
```

Tres reglas del sector:

1. **Nada de azul.** Ni marino, ni cian, ni degradado de olas. El azul es el
   uniforme y además compite con el producto, que ya es plateado y azul.
2. **Una didona pesada en los titulares.** En un mercado los precios van
   escritos a mano con rotulador grueso en cartones blancos: un tipo de trazo
   muy contrastado imita ese cartel sin caricaturizarlo. Es lo contrario de la
   sans redonda y amable que usan todas las webs de pescado.
3. **Esquinas a cero.** El mostrador es una bandeja rectangular de acero. La
   página también.

---

## Los dibujos (lo que hace que no sea otra demo)

Un puesto de mercado no se puede fotografiar sin fotografiar a alguien. Se
dibuja. Y el dibujo tiene que ser de **este** oficio:

1. **Los cortes.** Un pescado de perfil con las líneas de corte punteadas
   encima: a lomos, a rodajas, abierto para el horno, en tacos. **Es el dibujo
   que contesta la pregunta del molde** y ningún otro negocio lo puede usar.
2. **El mostrador de hielo.** Alzado de la bandeja inclinada con el hielo, las
   piezas tumbadas, los cartones de precio clavados y la balanza.
3. **El plano del mercado** con el pasillo y el puesto marcado. En un mercado,
   «cómo llegar» no termina en la puerta.

---

## Las fórmulas de texto

- **El titular quita el examen.** *«Aquí nadie tiene que saber pedir pescado.»*
  Habla el puesto, en su voz, y contesta el miedo antes de que se formule.
- **El guion, literal y en dos frases.** *«Para cuántos sois y cómo lo vais a
  hacer. Lo demás lo decido yo.»* El cliente tiene que poder ensayarlo mentalmente
  en la cola.
- **El trabajo, con su precio: ninguno.** *«Sin espinas, a lomos, abierto para
  el horno: no cuesta más. Va en el kilo.»*
- **La honestidad del catálogo.** *«No pongo lista de precios porque a las cinco
  de la mañana no sé lo que voy a tener. Escríbeme y te mando lo que ha entrado
  hoy y a cómo está.»*
- **El congelado, de frente.** *«El langostino se congela en el barco, a la
  hora de subirlo. Muchas veces es mejor que el de mostrador, y cuesta menos.»*
- **La cabeza y la espina.** *«La espina y la cabeza te las envuelvo aparte para
  el caldo. No se tiran y no se cobran.»* Es el detalle que se recuerda.

---

## El JSON-LD

`@type`: **`Store`** con `additionalType` de pescadería, o `FoodEstablishment`
si hay cocedero con venta preparada. Lo importante:

- `openingHours` con **el turno partido escrito de verdad** (`Mo-Fr 09:00-14:00`
  y `Mo-Fr 17:00-20:00` son dos entradas, no una).
- `address` con la calle **del mercado**, y el número de puesto en `name` o en
  `description`: un puesto no tiene portal propio.
- **Sin `aggregateRating`** salvo nota **y** recuento verificados.

## El JS

El mismo de `restaurante.md` (IntersectionObserver para `.u-revelar`) más
`#toggle-marcas`.

## Dos parches de `base.css` que hay que repetir en cada demo

`base.css` no se toca, pero tiene dos cosas que hay que corregir en el `<style>`
de la demo:

```css
svg{display:block;}                 /* si no, margin:auto no centra (es inline) */
.u-tira .u-wrap{display:flex;flex-wrap:wrap;justify-content:center;
  gap:var(--s-2) var(--s-4);align-items:center;}  /* el flex vive en la <section> */
```
