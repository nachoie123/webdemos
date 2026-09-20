# Molde: restaurante

Sacado de **shenxien.es** (Sushi Bar & Poké, Paseo de la Castellana 241), la web
que hizo el propio Nacho. Es el listón: 2.153 palabras, escrita a mano con
variables CSS propias, y no se parece a ninguna plantilla de restaurante.

Las clases `u-*` que se citan aquí ya están en `sistema/base.css`.

---

## Qué hace bien, en una frase

**No vende comida: vende la escena.** El hero es una foto a pantalla completa
muy oscurecida con el nombre flotando en el centro, y lo primero que cuenta no
es "cocina japonesa de calidad" sino que **los platos llegan a la mesa en un tren
de levitación magnética**. Eso es lo que nadie más puede decir.

Regla: busca el detalle raro del sitio y ponlo el primero. Si no lo hay, el
detalle es la persona (quién cocina, desde cuándo).

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Hero a pantalla completa** | `u-hero u-hero--pleno` + `u-descubrir` | Ceja con tracking enorme (`SUSHI BAR & POKÉ · MADRID`), nombre gigante en serif ligero, una línea con dirección + oferta, dos botones (Reservar lleno / Ver la carta de línea). |
| 2 | **Tira de datos** | `u-tira` | Oferta · horario de la oferta · nota de Google con nº de reseñas · dirección · **teléfono clicable**. Todo en versalitas. |
| 3 | **El concepto** | `u-seccion` + `u-desigual` | Titular en dos líneas partido a propósito (*"Auténticamente fresco. / Cada vez, sin excepción."*). Dos o tres párrafos cortos. Qué significa el nombre, si significa algo. |
| 4 | **Cifras** | `u-grid u-4 u-cifras` | 4,4 · 279+ · −10€ · 150+. Números reales de su ficha, nunca inventados. |
| 5 | **Una reseña suelta, grande** | `u-cita` | Una sola, en serif grande, con nombre y fecha. Vale más que cinco juntas. |
| 6 | **Lo que nos diferencia** | `u-grid u-3 u-numerada` | Tres cosas numeradas 01/02/03. Una frase de título + dos de explicación. Ni cuatro ni seis: **tres**. |
| 7 | **La carta** | `u-pestanas` + `u-precios` | Pestañas por familia (SUSHI, ROLLS, POKÉ, CALIENTES, BEBIDAS, POSTRES) y filas plato-precio. **Nunca un PDF.** |
| 8 | **Lo que dicen** | `u-grid u-3` + `u-cita` | Seis reseñas con nombre, fuente (Google / TripAdvisor / TheFork) y mes. |
| 9 | **Encuéntranos** | `u-desigual` | Titular partido (*"Paseo de la / Castellana, Madrid"*), horario **día a día** en filas, dirección, teléfono, una referencia del barrio ("junto a las Cuatro Torres"). |
| 10 | **Reserva** | formulario | Nombre, teléfono, email, personas, día, hora. Y el teléfono al lado para quien prefiera llamar. |
| 11 | **Quién eres + pie legal** | — | Las 5 piezas obligatorias del README. |

---

## La receta visual

```css
:root{
  --fondo:#e8dece;  --fondo-2:#d5c9b5;   /* arena, nunca blanco puro */
  --tinta:#181410;  --tinta-2:#7a6e60;   /* marrón casi negro, nunca #000 */
  --acento:#c8b89e; --acento-tinta:#181410;
  --linea:#c8b89e;
  --display:'Cormorant Garamond', Georgia, serif;   /* serif ligera y ancha */
  --texto:'Archivo', Arial, sans-serif;
  --radio:0px;
}
```

Tres cosas que hacen el look y no cuestan nada:

1. **Tracking enorme en todo lo pequeño.** `letter-spacing:.24em` en cejas y
   botones. Es el 80% de la sensación de "caro".
2. **Serif ligera y grande, no negrita.** El titular del hero va en `400`, no en
   `700`. La negrita es de plantilla.
3. **Fondo arena y tinta marrón.** Blanco puro sobre negro puro es lo que hace
   todo el mundo.

---

## Los textos

Cuatro fórmulas, sacadas de su web:

- **Titular partido en dos.** *"Auténticamente fresco. / Cada vez, sin excepción."*
  La segunda mitad es la que promete.
- **Diferencia con nombre propio.** No "servicio rápido", sino *"Entrega por
  cinta magnética"*.
- **La frase del habitual.** *"El restaurante al que los habituales vuelven
  semana tras semana."* Vende pertenencia, no comida.
- **La oferta con su letra pequeña pegada.** *"−10€ · Dom–Jue 20:00–23:00 ·
  consumiendo más de 50€ · válido hasta el 31/5/2026."* La condición al lado da
  credibilidad, no la quita.

---

## El JS del revelado (7 líneas)

```js
var io = new IntersectionObserver(function(es){
  es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('visible');
    io.unobserve(e.target); } });
}, {threshold:.12});
document.querySelectorAll('.u-revelar').forEach(function(el){ io.observe(el); });
```

---

## Lo que a Shenxien le falta (y a la demo no debe faltarle)

El auditor `revisar.py` la suspendería en tres cosas. Son regalo:

- **Sin JSON-LD.** No le dice a Google que es un restaurante, ni su horario, ni
  su nota. Es el argumento de venta más fácil.
- **Sin Instagram enlazado**, cuando el 74% de las webs del barrio sí lo enlaza.
- **Sin barra fija de móvil.** Tiene el teléfono en la tira de arriba, pero
  desaparece al bajar; en un restaurante, "Llamar / Cómo llegar" tiene que estar
  siempre a la vista.
