# Molde: carpintería de aluminio

Molde nuevo del 21/09/2026, escrito para **Manuel Díaz Carpintería de Aluminio**
(Costa Rica 20, Hispanoamérica). Vale para **ventanas y cerramientos de aluminio
y PVC, cerrajería, mosquiteras y toldos**: cualquier taller que venga a tu casa,
abra un agujero en la pared y lo vuelva a cerrar.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se venden ventanas, se vende un agujero cerrado a tiempo

Todas las webs del sector enseñan lo mismo: catálogos de perfiles, secciones
técnicas, logos de marca, «RPT de 70 mm», «clase 4 de permeabilidad». Están
escritas para otro instalador, no para el vecino del cuarto.

**El vecino del cuarto no compra una ventana. Compra un día de su vida.** El día
en que alguien va a tirar abajo lo que separa su salón de la calle, con el polvo,
el ruido, el frío y los gatos sueltos que eso supone. Y por eso las dos preguntas
que trae —y que ninguna web del sector contesta— son:

1. **¿Cuánto cuesta una ventana puesta?** No el metro cuadrado de perfil: la
   ventana entera, quitando la vieja, con el sellado y llevándose el escombro.
2. **¿Cuántos días voy a tener la casa abierta?** Esta es la de verdad. La gente
   aplaza el cambio de ventanas años enteros por miedo a una obra, no por el
   precio.

> Regla del molde: la sección más importante **no** es lo que se fabrica. Es
> **«el día de la obra, hora a hora»**. Una sola ventana se cambia en una mañana
> y casi nadie lo sabe. Decirlo, con horas, desbloquea la venta entera.

Hay una tercera pregunta, más callada y carísima si se falla: **«¿puedo hacer
esto en mi piso?»**. Cambiar el color de una ventana a fachada, cerrar una
terraza o poner una mosquitera enrollable puede necesitar el visto bueno de la
comunidad y, en según qué edificio, licencia del Ayuntamiento. Un taller que lo
escribe antes de cobrar nada se gana la confianza entera de la página.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: el día, no el producto** | «Una ventana se cambia en una mañana» vende más que «carpintería de aluminio desde 1995». Botón de pedir presupuesto. Dibujo del perfil en sección. |
| 2 | **Tira** | Calle y portal · horario partido · teléfono · correo. Si cierran en agosto, aquí. |
| 3 | **El día de la obra, hora a hora** | Cuatro pasos con su hora. La pieza clave del molde. Que se vea que a la hora de comer está cerrado. |
| 4 | **Qué entra en el precio** | La lista de lo que no se cobra aparte: quitar la vieja, el premarco, el sellado, el remate por dentro, el escombro. El presupuesto del sector se compara mal justo por esto. |
| 5 | **Antes de pedir presupuesto** | Comunidad, licencia y fachada protegida; cómo medir el hueco para dar una cifra por teléfono. Útil aunque no le contraten: por eso se guarda la página. |
| 6 | **Qué se hace aquí** | Ventanas, puertas, cerramientos de terraza, anodizados, lacados, mosquiteras. En lenguaje de vecino, y el término técnico detrás entre paréntesis. |
| 7 | **Horario día a día y dónde está el taller** | Tener taller propio es el argumento: se fabrica a medida y se arregla lo que ya está puesto. |
| 8 | **La única nota** | Todo lo inventado, junto y una sola vez. |
| 9 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** catálogo de perfiles ni fichas técnicas, ni logotipos de marcas de
aluminio, ni fotos de obra de banco de imágenes, ni «presupuesto sin compromiso»
como único mensaje. **Nunca inventar un precio cerrado ni un plazo de entrega:**
en obra, un número inventado es una reclamación. Van como horquilla y marcados.

---

## La receta visual

```css
:root{
  --fondo:#f1f1ef;  --fondo-2:#e2e4e0;   /* aluminio crudo, gris sin azul */
  --tinta:#191a18;  --tinta-2:#5b5f5a;
  --acento:#374b55;                       /* grafito anodizado */
  --cobre:#b0562a;                        /* bronce y cinta de obra: solo cifras */
  --radio:0px;
}
```

Tres reglas del sector:

1. **Nada de azul corporativo ni degradados de cristal.** Es el uniforme de las
   marcas de perfil, y aquí se compite contra ellas siendo el taller de la calle.
2. **Ángulo recto en todo.** `--radio:0`. Una ventana es un rectángulo y un
   inglete: la página tiene que estar cortada a 45 grados, no redondeada.
3. **Una condensada de taller en titulares**, del tipo rótulo de persiana. Con
   condensada, `line-height` nunca por debajo de `.96`: corta las tildes.

Dibujos obligatorios, a mano y para este taller: **la sección del perfil con la
rotura de puente térmico** (dos cáscaras de aluminio, la varilla de poliamida en
medio y el doble acristalamiento con su cámara) y **la secuencia del día de obra
en cuatro viñetas**. El primero explica en un dibujo por qué una ventana buena no
gotea por dentro; ninguna página del barrio lo enseña.

---

## Los textos

- **El titular es el día.** *«Una ventana se cambia en una mañana. La cocina
  vuelve a funcionar a la hora de comer.»*
- **Horas, no adjetivos.** *«A las 9 se quita la vieja; a las 11 está puesta la
  nueva; a las 13 está sellada.»*
- **Lo que entra, en lista.** *«Quitar la vieja, el premarco, el sellado por
  fuera, el remate por dentro y llevarse el escombro.»*
- **El permiso, antes de cobrar.** *«Si se cambia el color a fachada o se cierra
  una terraza, hay que pasar por la comunidad. Se dice antes de medir.»*
- **El término llano delante.** *«Ventana que no suda por dentro (con rotura de
  puente térmico).»*
- **Nada de garantías inventadas.** Ni años, ni plazos, ni precios cerrados.

---

## El JSON-LD

`@type`: **`HomeAndConstructionBusiness`** (bajo `LocalBusiness`). Lleva
`openingHours` **partido en dos tramos** —mañana y tarde—, porque un taller que
cierra a mediodía y no lo declara recibe llamadas a las tres. `address` con el
portal y `geo` con las coordenadas de la ficha. **Sin `aggregateRating`** salvo
nota **y** recuento verificados.
