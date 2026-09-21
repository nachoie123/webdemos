# Molde: zapatero / arreglo de calzado

Escrito el 21/09/2026 para **Reparación de Calzado y Complementos J.T.**, un
puesto dentro del Mercado de Maravillas (Bravo Murillo 122). Sirve para
zapateros, arreglos de bolsos y marroquinería, y en general para cualquier
oficio de **puesto de mercado o local sin escaparate a la calle**.

Las clases `u-*` están en `sistema/base.css`.

---

## Qué se vende aquí de verdad

No se vende una reparación. Se vende **un permiso para no tirar algo**.

El cliente tiene unos zapatos de 90 € con la suela abierta, o un bolso con el
asa descosida que le regaló alguien. No sabe si eso se arregla. Sospecha que
sí, pero también sospecha que le va a costar 40 € y que va a quedar peor. Así
que lo mete en el armario y lo deja ahí un año, que es la forma educada de
tirarlo.

> Regla: la página no compite con otro zapatero. Compite con **el cubo de la
> basura y con Amazon**. Todo lo que escribas tiene que empujar en la misma
> dirección: *esto tiene arreglo, cuesta menos de lo que crees, y si no lo
> tiene te lo digo gratis*.

### La pregunta que trae al cliente

**«¿Esto tiene arreglo o lo tiro?»**

Y detrás, pegadas, otras dos: *«¿cuánto me va a costar comparado con unos
nuevos?»* y *«¿va a quedar como un remiendo?»*.

Fíjate en lo que **no** pregunta: no pregunta qué marcas trabajas, ni cuántos
años llevas. Eso va después, y pequeño.

### La segunda pregunta, la del puesto de mercado

**«¿Dónde estás exactamente?»** Un negocio con escaparate a la calle no tiene
este problema. Un puesto dentro de un mercado, sí: Google Maps enseña el
mercado, no el puesto, y el cliente entra por una puerta, ve doscientos
puestos y se rinde. Una página que explique **por qué puerta se entra, qué
planta y qué hay al lado** vale más que diez fotos de zapatos.

### Diferencia con `reparaciones.md`

`reparaciones.md` ataca el pánico (*«se me ha roto el móvil hoy»*) y su pregunta
estrella es «¿cuánto tardas?». Aquí **no hay pánico**: nadie llega corriendo con
un zapato. Hay duda y hay pereza. Por eso el orden es distinto: primero el
veredicto («tiene arreglo»), después el precio, y el plazo va el tercero.

---

## Orden de secciones

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera pegajosa** | `.cab` + `u-nav` | Marca, menú corto y **el móvil clicable**. Aquí el móvil es la pieza central: se manda foto. |
| 2 | **Hero: el veredicto** | `u-sangrado u-seccion` | Titular en imperativo amable («antes de tirarlos, mándeme una foto») + botón de WhatsApp con texto ya escrito + dibujo del zapato. |
| 3 | **Tira de datos** | `u-tira` | Mercado y portal · planta · horario · móvil. |
| 4 | **La foto por WhatsApp** | `u-grid u-3 u-numerada` | Tres pasos: manda foto · te contesto con precio y día · lo traes. **Es la sección que gana el molde**, porque convierte la duda en un mensaje de diez segundos. |
| 5 | **Qué tiene arreglo y qué no** | `u-grid u-2` | Dos columnas enfrentadas. La columna del «no» es la que da credibilidad: un zapatero que te dice cuándo no merece la pena es un zapatero al que vuelves. |
| 6 | **Precios desde** | `u-precios` | Media suela, tapas, cremallera, tintado, ensanchado. Con «desde» y con la comparación implícita: 18 € frente a 90 € de zapatos nuevos. |
| 7 | **El zapato por dentro** | `u-grid u-desigual` | Dibujo despiezado con las zonas que se gastan. Enseña oficio sin presumir de él, y hace que la página se guarde. |
| 8 | **Cuánto tarda** | `u-grid u-3` | En el momento / en el día / con material encargado. |
| 9 | **Cómo llegar al puesto** | `u-grid u-desigual-inv` | Croquis de la entrada, planta, horario **día a día** y enlace a Maps. En un puesto de mercado esta sección es media venta. |
| 10 | **Opiniones** | — | **Vacía o ausente** si no hay recuento verificado. Nunca inventar. |
| 11 | **La única nota + pie legal** | — | Las 5 piezas obligatorias del README, juntas al final. |

**No lleva:** fotos de zapatos de catálogo (son de la marca, no suyas), ni
logos de marcas de lujo («arreglamos Louboutin» es problema de marca ajena), ni
la palabra «artesano» repetida, ni «más de X años de experiencia» sin dato.

---

## La receta visual

Cuero, betún y un hilo rojo. Nada de gris taller ni de azul corporativo: el
material de este oficio tiene color propio y es cálido.

```css
:root{
  --fondo:#f0e8dd;        /* cartón de caja de zapatos */
  --fondo-2:#e1d2bd;      /* ante claro */
  --tinta:#211710;        /* betún negro */
  --tinta-2:#6d5c49;
  --acento:#7b3a1f;       /* cuero curtido, el color de la suela */
  --acento-tinta:#f7ece0;
  --linea:#c8b295;
  --hilo:#b4352a;         /* el hilo rojo del pespunte: solo acentos */
  --radio:2px;            /* casi recto: esto es un banco de trabajo */
}
```

Tres reglas del sector:

1. **Un pespunte como recurso gráfico.** `border: 2px dashed` en el color del
   hilo es literalmente lo que hace este oficio. Úsalo una vez, en la pieza que
   más importe, y no lo repitas en toda la página.
2. **Slab serif en los titulares.** Es una tipografía con suela. Una serif fina
   de revista aquí miente: esto es un oficio de manos.
3. **Números grandes en los precios.** El argumento entero es la comparación
   entre 18 € y unos zapatos nuevos. Si el precio está en cuerpo 15, no
   compara nadie.

---

## Los textos

- **El titular es una instrucción, no una promesa.** *«Antes de tirarlos,
  mándeme una foto.»* Se puede obedecer en diez segundos.
- **El precio con su alternativa detrás.** *«Media suela, desde 18 €. Unos
  zapatos nuevos, 90.»*
- **El «no» por escrito.** *«Una zapatilla de tela con la puntera abierta no
  la cojo: se descose al lado de la costura nueva.»* Esa frase vende más que
  cualquier lista de servicios.
- **El plazo en días de verdad**, y decir cuándo se hace en el momento.
- **Nada de «quedará como nuevo».** Un arreglo se nota, y decirlo antes es
  justo lo que hace que el cliente vuelva.
- **El enlace de WhatsApp lleva el texto ya escrito** (`?text=`): quien duda no
  redacta.

---

## El JSON-LD

Schema.org no tiene un tipo para el zapatero. Se declara `LocalBusiness` con
`isicV4` **9523** —*repair of footwear and leather goods*—, que es el código
real del oficio y hace el trabajo que haría un `@type` propio.

Lleva `telephone`, `address` con `streetAddress`, `geo`, `openingHours` día a
día y `url`. Si el negocio está dentro de un mercado, el mercado va en
`address` como referencia, no como nombre del negocio.

**Sin `aggregateRating`** salvo nota **y** recuento verificados.
