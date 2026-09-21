# Molde: escuela infantil (guardería 0-3)

Duodécimo molde. Vale para **escuelas infantiles de primer ciclo, guarderías
privadas y centros de conciliación**: todo sitio donde alguien deja a un hijo
que todavía no habla y se va a trabajar.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se vende un servicio, se entrega un hijo

El cliente de una escuela infantil no compara pedagogías. Compara **su vida**.
Tiene que volver a la oficina en tres semanas, la baja se acaba, los abuelos no
pueden todos los días y hay que decidir ya. Llega agotado y con culpa.

Y llega con dos preguntas que no se atreve a hacer por teléfono, porque suenan
frías cuando se habla de un bebé:

> **«¿Hay plaza para mi hijo, y cuánto pago a fin de mes con todo dentro?»**

Eso es lo que decide. No el proyecto educativo. El sector entero contesta
«consúltanos» a las dos, y el padre cuelga y llama a la siguiente.

Tres diferencias con los demás moldes, que son las que impiden que salga otra
página igual:

1. **La web no cierra la venta: cierra la visita.** Nadie matricula a un niño
   sin ver el aula. Todo el diseño empuja a una cosa —pedir la visita— y el
   texto dice cuánto dura y si se puede ir con el niño.
2. **El comprador está cansado, no ilusionado.** La página no celebra la
   infancia: resuelve una logística. Hora de entrada, hora de salida, qué pasa
   si llego tarde, qué pasa si tiene fiebre.
3. **Lo que tranquiliza es un número, no un adjetivo.** «Ambiente familiar» no
   dice nada. «Catorce niños como máximo en el aula de 1-2 años, que es el tope
   que fija la Comunidad de Madrid» sí.

### Lo que nadie del sector publica y aquí va escrito

| Lo que el padre necesita | Lo que suele encontrar |
|---|---|
| Si hay plaza **en el aula de su edad** y desde cuándo | «Plazas limitadas» |
| La cuenta de fin de mes, concepto a concepto | «Consúltanos» |
| Cuántos niños hay por aula | «Grupos reducidos» |
| Qué pasa si el niño tiene 38 de fiebre a las once | Nada |
| Cuántos días dura la adaptación y si puede quedarse | Nada |
| El **código de centro** y que está autorizado | Nada |

El código de centro de la Comunidad de Madrid es el equivalente aquí al número
de colegiado del molde de salud: ocho dígitos que cualquiera puede comprobar y
que separan una escuela autorizada de un piso con niños.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: la plaza, no la pedagogía** | «Quedan plazas en el aula de 1-2 años» vence a cualquier lema. Botón único: pedir la visita por WhatsApp. |
| 2 | **Tira** | Calle con portal · horario de puertas · teléfono · código de centro. |
| 3 | **Las plazas, por aula y por edad** | Tres aulas, tres edades, tope legal de cada una y si queda sitio. La sección que decide. |
| 4 | **Un día normal, hora a hora** | De la puerta de las 7:30 a la de las 18:00. El padre necesita poder imaginárselo. |
| 5 | **La cuenta de fin de mes** | Matrícula, cuota, comedor, horario ampliado, material. Concepto a concepto y con el total sumado. |
| 6 | **La adaptación** | Cuántos días, en qué orden, si el padre puede quedarse y qué pasa si el niño llora. |
| 7 | **Cuando se pone malo** | Décimas, fiebre, a quién se llama y en cuánto. El miedo logístico número uno. |
| 8 | **El centro por dentro** | Planta del local: aulas, patio, cocina, sala de descanso. Dibujo, nunca foto. |
| 9 | **Pedir la visita** | Horario día a día, teléfono, WhatsApp y qué dura la visita. |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** fotos de niños —ni de banco ni propias, que además de copyright
son datos de menores—, ni testimonios de familias inventados, ni «los mejores
profesionales», ni una nota de Google sin recuento. **Y no lleva ni un nombre
de educadora que no haya dado el centro.**

> Regla dura del molde: **ninguna promesa sobre el niño.** Ni «aprenderá
> inglés», ni «dejará el pañal», ni «se adaptará en una semana». Se describe lo
> que hace el centro, nunca lo que le va a pasar al niño. Un padre que lee una
> promesa así se pone en guardia, y con razón.

---

## La receta visual

```css
:root{
  --fondo:#fbf7f0;  --fondo-2:#efe6d8;   /* papel crudo, no blanco */
  --tinta:#24201c;  --tinta-2:#6b6257;   /* marrón oscuro, nunca negro */
  --acento:#2f6b57;                       /* verde musgo: patio, calma */
  --acento-tinta:#f4faf7;
  --calido:#c4622f;                       /* terracota, solo para lo urgente */
  --linea:#ddd2c1;
  --radio:14px;                           /* amable, sin llegar a globo */
}
```

Tres reglas del sector, todas contra lo mismo:

1. **Nada de colores primarios ni arcoíris.** Rojo-amarillo-azul con globos es
   el uniforme visual de las 400 guarderías de Madrid, y encima está dirigido al
   niño, que no es quien paga ni quien lee. Paleta de adulto, cálida y mate.
2. **Nada de tipografías redondeadas de cuento.** Ni Comic, ni las geométricas
   infantiles. Un display con carácter y un texto humanista de cuerpo grande:
   esta página se lee de noche, con el niño ya dormido y la batería al 8%.
3. **Esquinas blandas y mucho aire, pero información densa.** La calma la dan
   los márgenes; la confianza la dan los datos. Las dos cosas a la vez.

Y una regla de dibujo: **se dibuja el sitio y el día, nunca al niño.** La planta
del local, la cinta horaria, el casillero de la entrada. Un muñeco dibujado es
clipart; un plano del local con el patio marcado no lo tiene nadie más.

---

## Los textos

- **El titular es la plaza.** *«Quedan dos plazas en el aula de un año. Y aquí
  está lo que cuesta.»* Nunca «bienvenidos a nuestra escuela».
- **Números donde el sector pone adjetivos.** No «grupos reducidos»: «14 niños
  como máximo, que es el tope legal».
- **El horario como promesa operativa.** *«La puerta se abre a las 7:30 y la
  última salida es a las 18:00.»* Eso es lo que decide si el padre llega a
  trabajar.
- **La cuenta sumada.** Poner cuota y comedor por separado no sirve: el padre
  quiere el total. Se suma delante de él.
- **Sin diminutivos.** «Los peques», «la seño», «los papis». Habla con el padre
  como con un adulto que tiene un problema de agenda y una responsabilidad.
- **La frase de cierre pide la visita, no la matrícula.** *«Venga a verlo con el
  niño: son veinte minutos y no hay que decidir nada ese día.»*

---

## El JSON-LD

`@type`: **`ChildCare`** (está bajo `LocalBusiness`). Para 3-6 años o si el
centro da segundo ciclo, `Preschool` bajo `EducationalOrganization`.

Lleva `openingHours` con el horario de puertas —el ampliado incluido, que es el
que se busca—, `address` con portal, `geo` y `telephone`. Si el centro tiene
código de la Comunidad de Madrid, va como `identifier`: es el dato verificable
del sector.

**Sin `aggregateRating`** salvo nota **y** recuento verificados, y sin `review`
jamás: una reseña inventada de una familia sobre una guardería es lo más feo
que se puede publicar.
