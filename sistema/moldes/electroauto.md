# Molde: electricidad y diagnóstico del automóvil

Duodécimo molde. Vale para el **electricista del automóvil**: el taller pequeño
al que se va cuando se enciende un testigo, cuando el coche no arranca dos
mañanas de cada diez, o cuando la batería se muere sola cada fin de semana.

**No es el molde de `taller.md`.** Aquel es para chapa, pintura y mecánica
general, y responde a «¿cuántos días me quedo sin coche?» y «¿me van a cobrar
cosas que no hacían falta?». Aquí el cliente **ni siquiera sabe qué le pasa al
coche**, y ése es exactamente el problema que viene a comprar.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se vende una reparación, se vende un nombre

El cliente de un electricista del automóvil llega con una frase, siempre la
misma: **«hace una cosa rara, pero solo a veces»**. Un testigo que se enciende y
se apaga. Un coche que arranca todos los días menos el martes. Una luz interior
que se queda encendida y descarga la batería en tres días.

Eso tiene dos consecuencias que cambian la página entera:

1. **No puede pedir presupuesto**, porque no sabe pedir qué. Llamar a un taller
   y decir «hace un ruido» da vergüenza. Una web que empieza por una lista de
   servicios le deja igual de perdido que estaba.
2. **Ya ha estado en otro sitio.** Casi siempre. Y ahí le dijeron «no le sale el
   fallo» y le cobraron la hora igual. Llega escaldado, no indeciso.

> Regla del molde: la primera sección después del titular **no vende nada**. Le
> dice al cliente qué significa lo que está viendo en el salpicadero y si eso es
> de parar o de esperar. Se gana la llamada regalando la primera respuesta.

La segunda pregunta, la que decide de verdad, es **«¿cuánto me cuesta que me
digáis qué pasa, y me lo descontáis si lo arreglo aquí?»**. Ningún taller de
barrio lo publica. Publicarlo es la diferencia entre esta página y las otras
cuarenta del sector.

### La prueba de que el molde es distinto

Si en la página aparecen «coche de sustitución», «trabajamos con todas las
aseguradoras» o «chapa y pintura», te has ido a `taller.md`. Aquí el coche se
queda una mañana, no dos semanas, y no hay seguro que pague una avería
eléctrica: la paga el dueño de su bolsillo. Por eso el precio de la diagnosis
duele tanto y por eso hay que escribirlo.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: la frase del cliente, no el servicio** | «Lo que solo falla a veces». Dibujo del cuadro de mandos. Botón de WhatsApp para mandar la foto del testigo. |
| 2 | **Tira** | Calle · barrio · horario · teléfono. |
| 3 | **El testigo: ¿puedo seguir o paro?** | Rojo / ámbar / informativo, con el dibujo de cada luz y qué hacer. **Es la sección regalada, y va antes que cualquier precio.** Orientación, nunca diagnóstico. |
| 4 | **Qué cuesta saber qué pasa** | El precio de la diagnosis, qué incluye, cuánto dura y **si se descuenta de la reparación**. La pieza que decide la llamada. |
| 5 | **Las tres piezas del arranque** | Batería, alternador, motor de arranque, con el dibujo del circuito de carga. Enseña a distinguirlas: es lo que el cliente busca en Google a las siete de la mañana. |
| 6 | **El fallo intermitente, paso a paso** | `u-numerada`. Cómo se busca una fuga de corriente o un falso contacto. Es la prueba de que aquí sí saben, y ningún competidor lo cuenta. |
| 7 | **Neumáticos y lo que sí tiene fecha** | Lo único del taller que el cliente puede mirar solo: la profundidad del dibujo y la presión. Corto, con dibujo. |
| 8 | **Dónde y horario día a día** | Con teléfono, WhatsApp y correo. Un taller pequeño cierra a mediodía y nadie se acuerda. |
| 9 | **La nota única** | Todas las salvedades juntas. Una sola vez. |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** logos de marcas de coches ni de baterías (no son suyos), fotos de
motores de banco de imágenes, «más de X años de experiencia» sin el número
verificado detrás, ni una sola promesa de que el fallo se encuentra. Un
intermitente puede no salir, y decirlo por escrito da más confianza que
prometerlo.

---

## La receta visual

El sector entero es azul marino con un engranaje. Aquí se copia otra cosa: **el
salpicadero de noche**. Fondo oscuro, texto claro y una sola luz ámbar, que es
exactamente lo que el cliente está mirando cuando busca el taller.

```css
:root{
  --fondo:#15181d;  --fondo-2:#1e232b;     /* grafito, no negro */
  --tinta:#eef1f4;  --tinta-2:#9aa3ad;
  --acento:#ffb020;                         /* ámbar de testigo */
  --acento-tinta:#15181d;
  --linea:#2c333c;
  --rojo:#e4483d;                           /* testigo rojo: parar */
  --verde:#35c07a;                          /* comprobado / correcto */
  --radio:2px;
}
```

Tres reglas del sector:

1. **Página oscura, y es el único molde donde se recomienda.** No es estética:
   es la escena. Las tres luces de la sección 3 solo se leen como luces sobre
   fondo oscuro.
2. **Una sola fuente de color por significado.** Ámbar = atención, rojo =
   parar, verde = comprobado. Si el ámbar se usa también de decoración, la
   sección del testigo deja de funcionar.
3. **Las cifras, en monoespaciada.** `12,6 V`, `14,4 V`, `1,6 mm`. Un voltaje en
   tipografía de texto parece una opinión; en monoespaciada parece una medida.
   Tabular, alineadas por la coma.

---

## Los textos

- **El titular es la frase del cliente.** *«Lo que solo falla a veces.»* No
  «electricidad del automóvil», que es cómo lo llama el gremio.
- **El término llano delante.** *«La batería se descarga sola (fuga de
  corriente).»*
- **Nunca prometer el hallazgo.** No «encontramos cualquier avería», sino «se
  busca con la pinza puesta y se dice lo que se ha medido».
- **La cifra, siempre con su unidad y su significado.** *«En reposo, una batería
  sana marca 12,6 V. Por debajo de 12,0 V ya está a media carga.»*
- **El descuento, escrito.** *«La diagnosis se descuenta si la reparación se
  hace aquí.»* Es una frase y cambia la llamada entera.
- **La sección del testigo se escribe como orientación, no como diagnóstico.**
  «Rojo: pare en cuanto pueda hacerlo con seguridad y llame antes de seguir.»
  Nunca «rojo: no pasa nada por llegar a casa».

---

## El JSON-LD

`@type`: **`AutoRepair`** (subtipo de `AutomotiveBusiness` y de
`LocalBusiness`). Lleva `openingHours` día a día, `address` con `postalCode`,
`geo` y `telephone`. Si hay móvil, el móvil es el `telephone`: es el que se
contesta.

Se puede añadir `makesOffer` con los servicios reales del directorio del sector
(electricidad, mecánica, neumáticos) **solo si están verificados**. **Sin
`aggregateRating`** salvo nota **y** recuento comprobados.
