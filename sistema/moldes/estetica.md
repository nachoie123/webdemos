# Molde: estética y uñas

Escrito el 20/09/2026 para **Colora Estética** (Castellana, Costa Fleming).
Sirve para centros de uñas, estética y depilación. Para peluquería de caballero
está `barberia.md`, que es otro negocio aunque lo parezca.

Las clases `u-*` están en `sistema/base.css`.

---

## Qué hay que entender del sector, en una frase

**La clienta no compara centros: compara huecos en su día.** Una manicura se
mete entre dos cosas —la hora de comer, después de dejar a los niños, el sábado
antes de cenar—, así que lo que decide no es el catálogo: es **cuánto dura la
cita** y **si hay hueco cuando ella puede**.

---

## Los tres frenos reales (en este orden)

1. **«¿Cuánto tardo?»** Hay que poner **los minutos de cada servicio**. Sin eso
   no se puede encajar en una agenda, y si no se puede encajar, no se pide.
2. **«¿Cuánto me va a durar?»** «Larga duración» no significa nada. **«Tres
   semanas»** sí. Es el dato que justifica el precio entero.
3. **«¿Cuánto es de verdad?»** Éste es el grande. La queja número uno del sector
   es el precio que cambia al llegar: se anuncia la semipermanente a 15 € y
   luego **la retirada del esmalte anterior se cobra aparte**. Decir «el precio
   ya lleva la retirada dentro» gana la cita sin bajar el precio.

Y una cuarta que no se pregunta en voz alta, como en `reparaciones.md`:
**«¿está limpio el material?»**. Se contesta **describiendo lo que se hace**
—qué es de un solo uso, qué se esteriliza y cómo— y **nunca prometiendo que no
va a pasar nada**. Es estética, no medicina.

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera pegajosa** | `.cab` + `u-nav` | Marca, menú y **móvil clicable**: aquí la cita se pide por WhatsApp, no por teléfono. |
| 2 | **Hero** | `u-sangrado u-seccion` | El titular ataca el truco del sector de frente: el precio ya lleva la retirada dentro. |
| 3 | **Tira de datos** | `u-tira` | Calle · barrio · horario (**y el domingo, si abre**) · teléfono. |
| 4 | **Minutos y semanas** | `u-grid u-3 u-numerada` | Los dos números que no pone nadie: lo que tarda y lo que dura. |
| 5 | **Precios con la letra pequeña dentro** | `u-precios` + `u-desigual-inv` | Y debajo, escrito: qué incluye y qué no. |
| 6 | **Qué se hace con el material** | `u-grid u-desigual` | La pregunta muda. Describir, nunca prometer. |
| 7 | **Qué se hace** | `u-grid u-2` | Servicios con el nombre que usa la clienta delante. |
| 8 | **Dónde y horario** | `u-grid u-desigual-inv` | Horario día a día. **Si abre domingo, va destacado**: es la ventaja más barata que existe en este sector. |
| 9 | **Opiniones** | `u-grid u-3` + `u-cita` | Tres de ejemplo. Aquí sí se pueden poner: es estética, no salud. |
| 10 | **Quién eres + pie legal** | — | Las 5 piezas obligatorias del README. |

---

## Lo que este molde PROHÍBE

- **Rosa, dorado y mármol.** Es el uniforme del sector entero y hace que todos
  los centros parezcan el mismo.
- **Fotos de manos de banco de imágenes.** Se huelen. Marcos vacíos rotulados
  mientras no haya fotos suyas, como en `floristeria.md`.
- **Cualquier promesa sobre la piel o las uñas.** Ni «uñas sanas», ni «sin
  dañar la uña natural», ni resultados. Se describe lo que se hace y ya.
- **Precios sin decir qué incluyen.** Es el pecado del sector: poner el número
  suelto y cobrar la retirada aparte.
- **«Larga duración».** O van las semanas, o no va nada.

---

## La receta visual

Concepto: **esmalte.** Blanco tiza, topo y un jade profundo. El jade es un
color de esmalte de verdad, no un pastel de catálogo, y es exactamente lo
contrario del rosa-y-dorado que usa todo el sector.

```css
:root{
  --fondo:#f7f6f3;  --fondo-2:#eae6df;   /* tiza, nunca blanco puro */
  --tinta:#1a1b19;  --tinta-2:#5f5d55;
  --acento:#0f5c4f; --acento-tinta:#f2fbf8;  /* jade profundo */
  --linea:#d8d2c9;  --topo:#b9ada1;
  --display:'Gloock', Georgia, serif;          /* serif de contraste alto */
  --texto:'Epilogue', 'Helvetica Neue', Arial, sans-serif;
  --radio:0px;
}
```

Tres cosas que hacen el look:

1. **Serif de contraste altísimo, en 400 y muy grande.** Gloock a
   `clamp(3rem,7.5vw,6rem)`. El contraste hace el trabajo que en otros sitios
   hace el dorado.
2. **El jade solo en lo que se pulsa y en los números.** Nunca de fondo.
3. **Filetes de topo, no cajas.** Las secciones se separan con una línea fina
   color topo, no con tarjetas. Es lo que le quita el aire de catálogo.

---

## Las fórmulas de texto

- **El titular contra el truco.** *«El precio de aquí / ya lleva la retirada
  dentro.»* Ataca la queja número uno sin nombrar a nadie.
- **Minutos y semanas juntos.** *«45 minutos · te dura unas 3 semanas.»*
- **La respuesta muda, en concreto.** *«La lima y el palito son de un solo uso y
  se tiran delante de ti. El resto se esteriliza en autoclave entre clienta y
  clienta.»* Describe; no promete.
- **El domingo, como titular propio.** *«Abrimos también el domingo.»* Si es
  cierto, es la frase que más citas trae de toda la página.

---

## El JS

El mismo de `restaurante.md` (IntersectionObserver) más `#toggle-marcas`.
