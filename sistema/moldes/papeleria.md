# Molde: papelería de barrio

Molde nuevo (21/09/2026). Vale para **papelería, tienda de material de
oficina, casa de bellas artes, mercería de escritorio**: el comercio que vende
objetos pequeños, caros de tener en stock y que el cliente busca **por su
nombre de marca**.

No confundir con el molde que ya existe y que ataca otra cosa:
`copisteria.md` cubre el **encargo con fecha** —mando un PDF, lo quiero el
jueves—. Aquí no hay archivo ni plazo: hay un objeto concreto en una
estantería, y la duda es si está.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: aquí no se vende papel, se vende no hacer el viaje en balde

El cliente de una papelería de barrio **ya sabe lo que quiere y sabe cómo se
llama**: un recambio del plumín medio, un bloc de 300 gramos, una carpeta de
cuatro anillas, un cuaderno de puntos A5. No viene a que le aconsejen entre
veinte modelos. Viene a por *ese*.

Y contra eso compite un catálogo infinito que contesta en dos segundos y se lo
deja en el portal. La tienda del barrio no puede ganar en catálogo ni en
precio. Solo puede ganar en una cosa: **decirle que sí lo tiene, hoy, antes de
que coja el metro**.

> Regla: la sección más importante no es «nuestros servicios» ni «quiénes
> somos». Es **la lista de lo que hay, escrita con los nombres con los que el
> cliente lo busca**. Marcas, gramajes, formatos, medidas. Nombres propios.

El error del sector es el opuesto y es siempre el mismo: *«amplio y variado
surtido en material de oficina y papelería»*. Esa frase no contesta nada. El
cliente que busca «recambio Lamy Madrid» no la va a encontrar nunca y, si la
encuentra, sigue sin saber si ir.

El segundo miedo, más callado: **que sea una tienda cara de las de escaparate
bonito**. Poner tres o cuatro precios de cosas corrientes —el cuaderno de
diario, el bolígrafo de siempre, la carpeta— desactiva eso en una línea.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: la promesa de no venir en balde** | El titular admite que NO hay de todo y ofrece a cambio la respuesta rápida. Botón: escribir preguntando por una cosa concreta, con el asunto ya redactado. |
| 2 | **Tira** | Calle con portal · barrio · horario de hoy · teléfono · correo. |
| 3 | **Lo que hay, por su nombre** | La pieza clave. Tres o cuatro familias (papel, cuadernos, escritura, oficina) y dentro **nombres, gramajes y medidas**, no adjetivos. Es lo que hace que la página aparezca cuando alguien busca la marca. |
| 4 | **Y si no está: el encargo** | Tres pasos numerados con su plazo. El encargo al distribuidor es el arma real contra el catálogo infinito, y nadie del sector lo cuenta. |
| 5 | **Lo que no sabe que se hace aquí** | Sellos de caucho, grabado, encuadernado, plastificado, probar el plumín antes de comprarlo. Servicios invisibles que no caben en el escaparate. |
| 6 | **Cuatro precios corrientes** | Para desactivar el «esto será carísimo». Cuatro bastan. |
| 7 | **Cómo preguntar y horario día a día** | El correo con asunto redactado, el teléfono, y la tabla de horarios. El mediodía cerrado se dice, no se esconde. |
| 8 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** carrusel de fotos de producto, «amplio surtido», categorías vacías
que no llevan a nada, ni un catálogo falso con precios que no son. Y **no lleva
sección de opiniones** si no hay recuento verificado.

---

## La receta visual

```css
:root{
  --fondo:#f7f2e7;  --fondo-2:#e9e0cd;    /* papel crudo, no blanco de pantalla */
  --tinta:#191720;  --tinta-2:#5b5561;
  --acento:#3d2b56;                        /* tinta violeta de estilográfica */
  --lapiz:#c1462f;                          /* rojo de corregir, solo marcas */
  --radio:0px;                              /* una hoja no tiene esquinas redondas */
}
```

Tres reglas del sector:

1. **El fondo es papel, no pantalla.** Un crudo cálido con una pizca de
   amarillo. El blanco puro convierte la papelería en una tienda de
   electrónica.
2. **Las listas se maquetan como una lista, no como tarjetas.** Filas con
   filete inferior, nombre a la izquierda y detalle a la derecha. Una rejilla
   de tarjetas con icono vuelve a esconder los nombres, que es justo lo que
   hay que enseñar.
3. **Reglas y filetes, nada de sombras.** La papelería es un oficio de líneas
   rectas: márgenes, pautados, cuadrículas. Una cuadrícula muy tenue de fondo
   en una sola sección basta para decirlo; en toda la página, cansa.

Los dibujos tienen que ser **de dentro de la tienda**: el escaparate con lo que
haya en él, el corte de un plumín con sus partes, el cosido de un cuaderno.
Nada de iconos de lápiz y bombilla.

---

## Los textos

- **El titular admite un límite.** *«No tenemos de todo. Tenemos esto, y se lo
  decimos antes de que venga.»* Admitir el límite es lo que hace creíble el
  resto de la página.
- **Nombres propios en las listas.** *«Blocs de acuarela de 200 y 300 g»*, no
  *«papeles especiales»*. El nombre es lo que se busca.
- **El plazo del encargo, con número.** *«Lo que no está suele llegar en 48
  horas.»* Sin número, el encargo no existe.
- **El mediodía cerrado se escribe.** Media papelería cierra de 14:00 a 17:00
  y ninguna lo dice; el cliente va a las cuatro y se encuentra la persiana.
- **Nada de superlativos.** Esta tienda no es «la mejor papelería»: es la que
  contesta.

---

## El JSON-LD

`@type`: **`OfficeEquipmentStore`** (está bajo `Store` → `LocalBusiness`). Si
es más de bellas artes que de oficina, `Store` a secas. Lleva `openingHours`
día a día con el corte del mediodía como dos tramos, `email` y `telephone`.
**Sin `aggregateRating`** salvo nota **y** recuento verificados.
