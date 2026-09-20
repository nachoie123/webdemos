# Molde: consulta de salud

Sexto molde. Vale para **podología, dental, fisioterapia, veterinario**: todo
negocio donde alguien deja que le toquen algo que le importa.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí se vende vergüenza, no salud

El cliente de una consulta no llega comparando. Llega con **una molestia que
arrastra desde hace meses** y, muy a menudo, con algo de reparo: un pie feo, una
boca descuidada, un bulto que no se ha mirado. Ha aplazado la cita varias veces.

Lo que le frena no es el precio. Es no saber **qué va a pasar ahí dentro**.

> Regla: la sección más importante no es la lista de tratamientos. Es
> **«cómo es la primera visita»**, contada paso a paso y con su duración.
> Quitar el miedo a lo desconocido es la venta entera.

El segundo freno es el precio de la primera consulta. Decirlo —aunque sea
«primera visita, 35 €»— convierte una llamada incómoda en una decisión fácil.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: el síntoma, no la especialidad** | «Le duele el pie desde hace meses» vende más que «Podología integral». Botón de pedir cita. |
| 2 | **Tira** | Calle · horario · teléfono · número de colegiado si lo hay. |
| 3 | **Cómo es la primera visita** | Tres o cuatro pasos con su duración. La pieza clave del molde. |
| 4 | **Quién le atiende** | Nombre, titulación y **número de colegiado**. En salud eso no es presumir: es lo que distingue una consulta de un centro de estética. |
| 5 | **Qué se trata aquí** | En lenguaje de paciente: «durezas y callos», no «hiperqueratosis y helomas». El término técnico va detrás, entre paréntesis. |
| 6 | **Precios de la primera visita** | Aunque el resto sea «según tratamiento». Al menos uno, claro. |
| 7 | **Cuándo hay que venir** | Señales concretas para ir. Es útil, y hace que la página se guarde. |
| 8 | **Horario día a día y cómo pedir cita** | Teléfono y WhatsApp. En salud, mucha gente prefiere escribir. |
| 9 | **Opiniones** | Sin firma si no están verificadas. **Nunca inventar un testimonio médico.** |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** fotos clínicas de banco de imágenes, ni promesas de resultado, ni
«los mejores especialistas». En salud una promesa de resultado puede ser
publicidad sanitaria irregular: se describe lo que se hace, no lo que se logra.

---

## La receta visual

```css
:root{
  --fondo:#f8f6f7;  --fondo-2:#ece7ea;    /* claro y cálido, no blanco clínico */
  --tinta:#1b1720;  --tinta-2:#615a68;
  --acento:#6d4b76;                        /* ciruela: serio sin ser frío */
  --calido:#c97b5a;                        /* terracota, solo acentos */
  --radio:8px;
}
```

Tres reglas del sector:

1. **Nada de azul hospital ni cruces verdes.** Es el look de la clínica sin
   alma, y aquí se compite justo por lo contrario: que te atienda una persona.
2. **Esquinas redondeadas y respiración.** Es el único molde donde el aire
   sobra a propósito: la página tiene que dar calma.
3. **Una serif humanista en titulares.** Ni slab industrial ni condensada: se
   está hablando de un cuerpo, no de una nave.

---

## Los textos

- **El titular es el síntoma.** *«Lleva meses andando con molestias. Se arregla
  en una visita.»*
- **La duración, siempre.** *«La primera visita dura unos 40 minutos.»* Saber
  cuánto se tarda desbloquea la cita.
- **El término llano delante.** *«Durezas y callos (hiperqueratosis).»*
- **Sin promesas.** No «le quitamos el dolor», sino «se ve el pie, se explica
  qué pasa y se dice qué se puede hacer».

---

## El JSON-LD

`@type` según el caso: **`Podiatric`**, `Dentist`, `Physiotherapy`,
`VeterinaryCare` — todos válidos bajo `MedicalBusiness`. Lleva `openingHours` y
`medicalSpecialty` si aplica. **Sin `aggregateRating`** salvo nota **y**
recuento verificados.
