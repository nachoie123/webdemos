# Molde: floristería

Escrito el 20/09/2026 para **Flores Yohana Alonso** (Plaza de Cuzco, dentro del
Hotel AC Cuzco). Sirve para floristerías de barrio y puestos de mercado. **No
sirve para una tienda que vende a toda España**: ahí hace falta carrito, y aquí
lo que hace falta es justo lo contrario.

Las clases `u-*` están en `sistema/base.css`.

---

## Qué hay que entender del sector, en una frase

**Nadie compra flores con tiempo. Se acuerda.** Cumpleaños que se pasó, una
reunión que sale mal, un tanatorio a las ocho. El cliente de una floristería de
barrio casi siempre llega tarde y con algo de culpa encima.

Por eso la página no se ordena por producto. Se ordena por **cuándo lo
necesitas** y **para qué es**.

---

## Los dos frenos reales (y su orden)

1. **«¿Llega hoy?»** Es la primera pregunta y ninguna floristería la contesta.
   Hay que poner **la hora de corte escrita**: «si nos lo dices antes de las
   17:00, sale hoy». Una hora concreta vale más que diez fotos de ramos.
2. **«¿Va a quedar bien?»** Comprar flores es comprar algo que no has visto, y
   que además vas a regalar. Se quita enseñando **el trabajo suyo de verdad** —
   y mientras no haya fotos, **marcos vacíos rotulados**, nunca fotos de banco
   ni recortadas de Google Maps.

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera pegajosa** | `.cab` + `u-nav` | Marca, menú y **móvil clicable** (en floristería el móvil manda: se pide con foto). |
| 2 | **Hero** | `u-sangrado u-seccion` | Serif grande. El titular admite en voz alta que se compra con prisa; eso es lo que hace que el cliente se sienta entendido. |
| 3 | **Tira de datos** | `u-tira` | Dirección · dónde está (referencia, no calle) · horario · teléfono. |
| 4 | **¿Llega hoy?** | `u-grid u-3 u-numerada` | Tres tramos **con hora escrita**: hoy / mañana / encargo. La pieza que hace que alguien escriba. |
| 5 | **Por ocasión, no por flor** | `u-grid u-2` | Cumpleaños olvidado · pésame · empresa y hotel · «porque sí». Con el texto que diría el cliente, no el catálogo. |
| 6 | **El escaparate** | `u-grid u-3` + `.marco` | **Marcos vacíos rotulados** mientras no haya fotos suyas. Se explica por qué están vacíos: es honestidad, no dejadez. |
| 7 | **Cómo se pide** | `u-grid u-desigual` | Por WhatsApp, con foto y presupuesto antes de cobrar. Sin carrito, sin registro. |
| 8 | **Precios por tramo** | `u-precios` + `u-desigual-inv` | «Desde X» por tramos. En flores el precio exacto no existe; el tramo sí, y es lo que falta en todas. |
| 9 | **Dónde** | `u-grid u-desigual` | La referencia primero («en el vestíbulo del hotel»), la calle después. Horario **día a día**. |
| 10 | **Opiniones** | `u-grid u-3` + `u-cita` | Tres, marcadas como ejemplo. Aquí sí se pueden poner: no es un sector de salud. |
| 11 | **Quién eres + pie legal** | — | Las 5 piezas obligatorias del README. |

---

## Lo que este molde PROHÍBE

- **Fotos de banco de imágenes.** `revisar.py` las caza, y además se huelen a un
  metro: una floristería se vende con SU trabajo o no se vende.
- **Fotos sacadas de Google Maps.** El copyright es de quien las hizo.
- **Carrito y pasarela de pago.** Para veinte pedidos al día es un estorbo: el
  pedido de verdad se hace hablando, y WhatsApp es donde ya está el cliente.
- **Nombres de flores como estructura.** Rosas / Lilium / Gerberas es el índice
  de un mayorista, no la cabeza de quien compra.
- **Declarar la nota** si el recuento no cuadra entre fuentes.

---

## La receta visual

Concepto: **cubo de zinc.** El gris frío de los cubos del mercado de flores, y
un solo color fuerte —frambuesa— para lo que hay que pulsar. Nada de rosa
pastel: el pastel es lo que hace que todas las floristerías parezcan la misma
plantilla de 2011.

```css
:root{
  --fondo:#eef1f2;  --fondo-2:#dfe5e7;   /* zinc, nunca blanco ni rosa */
  --tinta:#141b1e;  --tinta-2:#59666b;
  --acento:#8e1f4f; --acento-tinta:#fdf2f6;  /* frambuesa profunda */
  --linea:#c3ccd0;  --tallo:#3f5d3a;         /* verde tallo, solo en detalles */
  --display:'Instrument Serif', Georgia, serif;   /* serif fina y grande */
  --texto:'Familjen Grotesk', 'Helvetica Neue', Arial, sans-serif;
  --radio:0px;
}
```

Tres cosas que hacen el look:

1. **Serif fina y enorme, en 400.** Instrument Serif a `clamp(3rem,8vw,6.5rem)`.
   La negrita es de plantilla; el tamaño es de floristería buena.
2. **El zinc de fondo y el verde solo en el tallo de los detalles.** Filetes,
   viñetas y subrayados en `--tallo`. Si el verde está en todas partes, es un
   vivero.
3. **Los marcos vacíos son parte del diseño**, no un hueco. Con su rótulo
   dentro, en versalitas, y proporción 4:5 como una foto de verdad.

---

## Las fórmulas de texto

- **El titular que admite la verdad.** *«Nadie compra flores con tiempo. / Se
  acuerda a las siete.»* El cliente se reconoce y deja de sentirse mal.
- **La hora de corte, escrita.** *«Antes de las 17:00, sale hoy.»* Es el dato
  que convierte una duda en un mensaje.
- **La ocasión con sus palabras.** No «arreglos fúnebres», sino *«se ha muerto
  alguien de la oficina y hay que mandar algo antes de las ocho»*.
- **El tramo, no el precio.** *«Un ramo para llevar, desde 20 €.»* Y al lado:
  *«dinos el tope y lo montamos ahí.»*

---

## El JS

El mismo de `restaurante.md` (IntersectionObserver) más `#toggle-marcas`.
