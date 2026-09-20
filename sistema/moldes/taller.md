# Molde: taller mecánico

Cuarto molde. El cliente de un taller **ya tiene el problema** —el coche hace un
ruido, o está abollado— y lo que busca no es un taller: busca **dejar de tener
el problema con el menor daño posible**.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: el miedo no es la factura

Todo el sector escribe como si el cliente eligiera por precio. No es verdad. Las
dos preguntas que de verdad se hace quien deja el coche son:

1. **«¿Cuántos días me quedo sin coche?»**
2. **«¿Me van a cobrar cosas que no hacían falta?»**

El precio es la tercera, y muy por detrás. Una web de taller que empieza por
«los mejores precios en mecánica general» está respondiendo a la pregunta que
nadie hace.

> Regla: la primera sección después del titular responde a la pregunta 1, y la
> segunda a la 2. Si el taller tiene coche de sustitución, **eso es el titular**.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: el día que recupera el coche** | Titular sobre no quedarse tirado, no sobre mecánica. Botón de WhatsApp para mandar una foto del golpe. |
| 2 | **Tira** | Calle · horario · teléfono · «multimarca» · «todas las aseguradoras». |
| 3 | **Coche de sustitución** | Si lo hay, va solo y grande. Es lo único que el cliente no espera y lo que decide la llamada. |
| 4 | **Presupuesto antes de tocar nada** | Cómo se pide, qué incluye, y la frase de que nada se hace sin aprobar. Responde a la pregunta 2. |
| 5 | **Qué se hace aquí** | Mecánica, chapa y pintura, motos… en lista corta. Y **qué no** se hace. |
| 6 | **Aseguradoras** | «Trabajamos con todas» vale más escrito que veinte logos, y no tiene problema de marcas. |
| 7 | **Cómo funciona, en tres pasos** | Manda foto → presupuesto cerrado → día de entrega. Quita el miedo a lo desconocido. |
| 8 | **Dónde y horario** | Día a día. Un taller cierra a mediodía y nadie se acuerda. |
| 9 | **Opiniones** | Sin firma si no están verificadas, y diciéndolo. |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** logos de marcas de coches (son marcas registradas y no son suyas),
fotos de motores de banco de imágenes, ni «más de X años de experiencia» sin un
número real detrás.

---

## La receta visual

```css
:root{
  --fondo:#eef0ef;  --fondo-2:#dde2e1;    /* gris taller limpio, no blanco */
  --tinta:#14191a;  --tinta-2:#5c6668;
  --acento:#0f5c5c;                        /* verde azulado: técnico, sobrio */
  --senal:#d99a00;                         /* mostaza de señal, solo para avisos */
  --radio:2px;
}
```

Tres reglas del sector:

1. **Nada de rojo carreras ni fibra de carbono.** Es el look de la plantilla de
   taller y dice «tuning», no «me arreglan el coche y me lo devuelven el jueves».
2. **Tipografía condensada en titulares.** Rótulo de nave industrial, no revista.
3. **Números grandes para los días, no para los euros.** «48 h» y «3 pasos»
   pesan más que cualquier precio.

---

## Los textos

- **El titular habla del cliente sin coche**, no del taller con herramientas.
  *«Su coche entra el lunes. Usted no se queda a pie.»*
- **La frase del presupuesto.** *«Nada se toca sin que usted diga que sí, y el
  presupuesto es cerrado: si aparece algo más, se le llama antes.»*
- **La foto por WhatsApp.** Es la acción más fácil que existe para un cliente con
  un golpe: *«Mándeme una foto del golpe por WhatsApp y le digo por dónde va.»*
- **Decir el CIF y los años en el barrio.** En este sector, parecer una empresa
  real con papeles es diferenciación: media competencia son intermediarios.

---

## El JSON-LD

`@type` es **`AutoRepair`**. Lleva `openingHours` día a día y, si aplica,
`makesOffer` con el coche de sustitución. **Sin `aggregateRating`** salvo que
haya nota **y** número de reseñas verificados.
