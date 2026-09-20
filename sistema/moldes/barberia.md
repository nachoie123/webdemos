# Molde: barbería

Tercer molde. Ni restaurante ni cerrajería: aquí el cliente **no tiene prisa y
no tiene hambre**. Está decidiendo a quién le deja la cabeza, y eso se decide
mirando fotos de cortes, no leyendo texto.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: el portfolio ya existe, y no está en Google

Casi todas las barberías del barrio **ya tienen Instagram y lo llevan bien**:
fotos de cortes, antes y después, reels. Lo que no tienen es web. Y eso rompe
la cadena por dos sitios:

1. **Nadie busca barbería en Instagram.** Se busca «barbería Tetuán» en Google,
   y ahí el perfil no sale. Sale el mapa, y punto.
2. **Desde Instagram no se reserva.** «Escríbenos por DM» pierde al que mira a
   las once de la noche y no quiere dar conversación.

> El argumento de venta no es «le hago una web». Es **«su trabajo ya está
> fotografiado; lo que falta es que alguien lo encuentre y pueda pedir hora»**.

La web no sustituye el Instagram: lo **enmarca**. La galería de la página son sus
propias fotos, y el pie de cada sección lleva el enlace al perfil.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero con el trabajo, no con el nombre** | Molde de hero nº4 de `patrones.md`: posicionamiento + escasez. Nombre mediano, una frase que diga a quién corta, y **el botón de pedir hora**. |
| 2 | **Tira** | Calle · horario · teléfono · Instagram. |
| 3 | **Galería de cortes** | La sección más grande de la página. Rejilla irregular, no cuadrícula uniforme. Sin fotos propias: marcos vacíos rotulados que digan qué foto va ahí. **Nunca banco de imágenes.** |
| 4 | **Precios** | Cortos y en euros redondos. En este sector el precio es argumento, no vergüenza: un corte de 8 € se pone bien grande. |
| 5 | **Quién corta** | Nombre del barbero. Una barbería se elige por la persona, no por el local. |
| 6 | **Cómo se pide hora** | Tres caminos: WhatsApp, llamar, o entrar sin cita. Decir si se puede entrar sin cita es media venta. |
| 7 | **Horario día a día** | El sector cierra lunes o domingo y la gente nunca se acuerda. |
| 8 | **Opiniones** | Sin firma si no están verificadas, y diciéndolo. |
| 9 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** «nuestra filosofía», ni historia de la barbería desde 1920, ni
iconos de tijeras. Ese es el look de plantilla del sector.

---

## La receta visual

```css
:root{
  --fondo:#f3efe7;  --fondo-2:#e4dccd;    /* crema, papel de toalla caliente */
  --tinta:#1c1815;  --tinta-2:#6b6157;
  --acento:#8c4a2f;                        /* cuero del sillón */
  --azul:#27506b;                          /* el azul del poste, de apoyo */
  --radio:3px;
}
```

Tres reglas del sector:

1. **Nada de blanco y negro puro con dorado.** Es el uniforme de las plantillas
   de barbería: el cliente ha visto esa web cuarenta veces.
2. **Una slab o una serif con peso en los titulares.** Es el rótulo pintado del
   escaparate, no una tipografía de app.
3. **La galería manda el tamaño.** Si las fotos ocupan menos que el texto, la
   página está mal repartida.

---

## Los textos

- **El titular dice para quién es, no qué se hace.** No «Barbería y estética
  masculina», sino *«Sale usted a la calle y se le nota»*.
- **El precio, entero y sin "desde".** *«Corte, 8 €»* vale más que cualquier
  párrafo sobre calidad.
- **La frase de la cita.** *«Se puede entrar sin hora. Si prefiere no esperar,
  escriba por WhatsApp.»* Las dos puertas abiertas, dicha en una línea.
- **El Instagram, con lo que hay dentro.** No «Síguenos», sino *«Cada corte que
  hace está en su Instagram: @cuenta»*.

---

## El JSON-LD

`@type` es **`HairSalon`**. Lleva `sameAs` con la URL del Instagram —es el dato
que más fácil enlaza Google con el negocio— y `openingHours` día a día.

**Sin `aggregateRating`** salvo que haya nota **y** número de reseñas
verificados. La nota sola la penaliza Google.
