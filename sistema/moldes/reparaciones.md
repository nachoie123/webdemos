# Molde: reparaciones

Escrito el 20/09/2026 para **Reparaciones El Experto** (Bravo Murillo 355).
Sirve para reparación de móviles, ordenadores, electrodomésticos y pequeño
aparato: cualquier negocio al que se le lleva algo roto que importa.

Las clases `u-*` están en `sistema/base.css`.

---

## Qué hay que entender del sector, en una frase

**El cliente no llega comparando: llega en pánico.** Se le acaba de caer el
móvil, se le ha muerto la lavadora con la ropa dentro, el portátil no enciende
la víspera de entregar algo. Nadie entra en una tienda de reparaciones de buen
humor.

Por eso la página no compite por precio. Compite por **quitar miedo**, y lo
hace contestando tres preguntas en este orden exacto.

---

## Las tres preguntas (y la tercera es la que gana)

1. **«¿Cuánto tardas?»** Es la primera, siempre, por delante del precio. Hay
   que dar **tramos con tiempos escritos**: lo que se hace en el momento, lo que
   se hace en el día, lo que necesita pedir pieza.
2. **«¿Pierdo las fotos?»** La segunda. Y la respuesta honesta —«en una pantalla
   no se toca nada; si es la placa, depende, y se te dice antes»— vale más que
   cualquier promesa.
3. **«¿Van a ver lo que tengo dentro?»** **Esta nadie la pregunta en voz alta y
   todo el mundo la piensa.** Contestarla sin que te la hagan es lo que
   diferencia a esta página de las 200 webs de reparación que hay. Hay que
   decirlo llano: qué se mira, qué no, cuándo hace falta la clave y para qué.

Después de eso, el precio. Nunca antes.

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera pegajosa** | `.cab` + `u-nav` | Marca, menú y **móvil clicable**. Aquí el móvil manda: se manda foto de la pantalla rota. |
| 2 | **Hero** | `u-sangrado u-seccion` | Titular en presente y en segunda persona, escrito para alguien que lo está leyendo con el móvil roto en la mano. |
| 3 | **Tira de datos** | `u-tira` | Calle con portal · barrio · horario · teléfono. |
| 4 | **¿Cuánto tarda?** | `u-grid u-3 u-numerada` | Tres tramos con **minutos y días escritos**. La pieza que hace que alguien se acerque. |
| 5 | **Lo que nadie pregunta en voz alta** | `u-grid u-desigual` | Fotos, datos y privacidad. **La sección que gana el molde.** |
| 6 | **Precios desde** | `u-precios` + `u-desigual-inv` | Por reparación, «desde». Y la frase clave: **presupuesto antes de tocar nada**. |
| 7 | **Pieza original o compatible** | `u-grid u-2` | Las dos, con su precio y su garantía, y sin decir que una es mala. La honestidad aquí es el argumento. |
| 8 | **Qué se arregla** | `u-grid u-desigual` | Móviles **y lo demás**: casi todas estas tiendas arreglan ordenadores y nadie lo sabe. |
| 9 | **Dónde y horario** | `u-grid u-desigual-inv` | Horario **día a día**, calle con portal, Cómo llegar. |
| 10 | **Opiniones** | `u-grid u-3` + `u-cita` | Tres marcadas como ejemplo, y **por qué no se pone la nota** si el recuento no cuadra. |
| 11 | **Quién eres + pie legal** | — | Las 5 piezas obligatorias del README. |

---

## Lo que este molde PROHÍBE

- **«Reparamos tu móvil en 30 minutos»** como titular sin decir qué reparación.
  Es la frase de todas las franquicias y no se la cree nadie.
- **Logos de marcas** (la manzana, el robot verde, Samsung…). Son marcas
  registradas y además es el look de todas las tiendas del sector.
- **Prometer que no se pierden los datos.** En una placa mojada se pueden
  perder. Se dice cuándo sí y cuándo no, y ya.
- **Esconder que la pieza es compatible.** Se pone al lado de la original, con
  su precio y su garantía. Quien lo esconde pierde la reseña.
- **Declarar la nota si el recuento baila.** En El Experto una fuente decía 426
  opiniones y otra 51.

---

## La receta visual

Concepto: **mostrador.** Blanco azulado de tienda con buena luz, un violeta
eléctrico para lo que se pulsa y ámbar solo en la pieza del presupuesto. Nada
de negro con azul neón y circuitos de fondo, que es el uniforme del sector.

```css
:root{
  --fondo:#f4f4f7;  --fondo-2:#e7e7ee;   /* blanco azulado, no blanco puro */
  --tinta:#14141c;  --tinta-2:#5c5c6b;
  --acento:#4b31e8; --acento-tinta:#f3f1ff;  /* violeta eléctrico */
  --linea:#d2d2de;  --ambar:#e8930c;         /* solo en el presupuesto */
  --display:'Bricolage Grotesque', 'Arial Narrow', sans-serif;
  --texto:'Spline Sans', 'Helvetica Neue', Arial, sans-serif;
  --radio:6px;
}
```

Tres cosas que hacen el look:

1. **Esquinas de 6px en todo.** Es el único molde con radio: una pantalla
   tiene esquinas redondeadas y la página también. Coherencia barata.
2. **El violeta solo en botones y números.** Si el violeta está en los fondos,
   es una startup; si está en lo que se pulsa, es una tienda.
3. **Una ficha ámbar, una sola**, para «presupuesto antes de tocar nada». El
   color que no se repite es el que se lee.

---

## Las fórmulas de texto

- **El titular en presente y en segunda persona.** *«Se te acaba de caer. /
  Puedes tenerlo esta tarde.»* Le habla a alguien que lo está leyendo con la
  pantalla rota.
- **El tiempo por delante del precio.** *«Pantalla: en el momento, 40 minutos.»*
- **La respuesta a la pregunta muda.** *«No se mira nada de lo que hay dentro, y
  la clave solo hace falta para comprobar que la pantalla nueva responde al
  tacto. Si no quieres darla, se prueba de otra manera y tarda diez minutos
  más.»*
- **El presupuesto como promesa concreta.** *«Se mira, se te dice lo que vale y
  tú decides. Si no tiene arreglo, la revisión no se cobra.»*

---

## El JS

El mismo de `restaurante.md` (IntersectionObserver) más `#toggle-marcas`.
