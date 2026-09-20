# Molde: entrenador personal

Escrito el 20/09/2026 para **Fitness Feda Madrid** (Rosario Pino, Castillejos).
Sirve para entrenadores personales, preparadores físicos y estudios de una sola
persona. **No sirve para un gimnasio de cadena**: ahí la página vende
instalaciones, y aquí vende justo lo contrario.

Las clases `u-*` que se citan están en `sistema/base.css`.

---

## Qué hay que entender del sector, en una frase

**El competidor no es el otro entrenador: es la cuota de 19,99 € del gimnasio
de al lado.** Contra eso no se gana hablando de instalaciones ni de material.
Se gana con lo único que una cadena no puede ofrecer: **que alguien sepa tu
nombre, cuente tus series y se dé cuenta cuando llevas dos semanas sin ir.**

Regla: la página entera es un argumento a favor de la persona, no del sitio.

---

## Los dos frenos reales (y el orden en que hay que quitarlos)

El sector escribe sus webs como si el freno fuera la motivación. No lo es.

1. **«No sé cuánto cuesta.»** Un entrenador personal es la compra con el precio
   peor publicado del barrio: nadie lo pone. Ponerlo es la diferenciación más
   barata que existe. Si no se puede poner todo, se pone **el de la primera
   sesión** y el de **un bono**.
2. **«No voy a poder seguir el ritmo.»** Mucha gente no llama porque se imagina
   una sesión de gente en forma y ella la última. Hay que contar cómo es la
   primera sesión **minuto a minuto** y decir que la primera no se entrena: se
   mide.

Todo lo demás —material, titulaciones, fotos del local— va después.

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera pegajosa** | `.cab` + `u-nav` | Marca, menú corto y **teléfono clicable** siempre visible. |
| 2 | **Hero claro, titular enorme** | `u-sangrado u-seccion` | Condensada gigante, con **una sola frase subrayada a rotulador** (`.rotu`). El titular opone la persona a la cadena. Dos botones: llamar / cómo es la primera sesión. |
| 3 | **Tira de datos** | `u-tira` | Calle · barrio · horario · teléfono. En versalitas. |
| 4 | **La primera sesión** | `u-grid u-3 u-numerada` | Tres pasos, con **los minutos escritos**. Es la pieza que hace que alguien llame. |
| 5 | **Quién te entrena** | `u-grid u-desigual` | La persona, con nombre. Aquí va la **titulación** y, si la hay, el número de certificación: en este sector no es presumir, es lo que separa a un profesional de un influencer. |
| 6 | **Dónde se entrena** | `u-grid u-2` | Sala / a domicilio / al aire libre. Es la pregunta número dos y casi nadie la contesta en su web. |
| 7 | **Precios** | `u-precios` | Filas concepto-precio, como una carta. **Nunca «consúltanos».** |
| 8 | **Para quién sí y para quién no** | `u-grid u-desigual-inv` | La sección que nadie escribe. Decir a quién **no** se le puede ayudar es lo que hace creíble el resto de la página. |
| 9 | **Lo que aquí no vas a ver** | `.franja` oscura | Sin fotos «antes y después», sin promesas de kilos, sin suplementos. Antídoto al ruido del sector. Sustituye a la sección de testimonios. |
| 10 | **Horario y cita** | `u-grid u-desigual-inv` | Horario **día a día** en tabla, dirección, teléfono, WhatsApp, Cómo llegar. |
| 11 | **Quién eres + pie legal** | — | Las 5 piezas obligatorias del README. |

---

## Lo que este molde PROHÍBE

Son los tópicos que hacen que todas las webs de entrenador parezcan la misma:

- **Fotos «antes y después».** Ni reales ni de ejemplo. Son la razón por la que
  el sector no se cree.
- **Cualquier número de kilos, centímetros o semanas.** «−8 kg en 12 semanas»
  es una promesa de resultado, y una promesa de resultado en un cuerpo ajeno no
  se firma.
- **Testimonios inventados**, aunque estén marcados como ejemplo. Misma regla
  que en `salud.md`: si no hay opiniones reales verificadas, la sección se
  sustituye, no se rellena.
- **`aggregateRating` sin `reviewCount` verificado.** El auditor lo suspende.
- **«Transforma tu vida», «saca tu mejor versión», «sin excusas».** El tono es
  el de alguien que te abre la puerta, no el de un sargento.

---

## La receta visual

Concepto: **hormigón y lima.** Gris de obra, grafito y un verde lima que solo
aparece donde hay que mirar. Es el color de la cinta del suelo de una sala de
entrenamiento, no el negro-con-neón de todas las webs de gimnasio.

```css
:root{
  --fondo:#eaeae6;  --fondo-2:#dcdcd7;   /* hormigón, nunca blanco */
  --tinta:#16181a;  --tinta-2:#5d6268;
  --acento:#b9e021; --acento-tinta:#131709;  /* lima con tinta oscura encima */
  --linea:#c6c7c1;
  --display:'Big Shoulders Display', 'Arial Narrow', sans-serif;  /* condensada */
  --texto:'Manrope', 'Helvetica Neue', Arial, sans-serif;
  --radio:2px;
}
```

Tres cosas que hacen el look:

1. **Condensada muy grande y muy apretada.** `font-size:clamp(3rem,9vw,7rem)` y
   `line-height:.9`. La condensada deja meter una frase larga sin partirla.
2. **La lima como rotulador, no como fondo.** Un `background` de lima detrás de
   *una* frase del titular (`.rotu`). Si la lima está en todas partes, es neón
   de gimnasio; si está en un sitio, es una marca.
3. **Una sola franja oscura, a mitad de página.** La página es clara; el grafito
   aparece una vez, para la sección de «lo que aquí no vas a ver». El contraste
   hace de puntuación.

---

## Las fórmulas de texto

- **Titular por oposición.** *«Un gimnasio no te mira. / Aquí alguien cuenta las
  series.»* La primera mitad es el competidor; la segunda, la diferencia.
- **Los minutos por delante.** *«Unos 15 minutos»* debajo de cada paso. Saber
  cuánto dura es lo que convierte «me lo pienso» en una llamada.
- **El precio con su letra pequeña pegada.** *«45 € la sesión suelta · 4 sesiones
  160 € · caducan a los dos meses.»* La condición al lado da credibilidad.
- **La frase de la puerta.** *«Si llevas diez años sin hacer ejercicio, eres
  exactamente a quien mejor se le puede ayudar.»* Quita el miedo a ser el peor
  de la sala, que es el freno de verdad.

---

## El JS del revelado

El mismo de `restaurante.md` (IntersectionObserver, 7 líneas) más el botón
`#toggle-marcas`. Nada más: en este molde no hay carrusel ni contador animado.
