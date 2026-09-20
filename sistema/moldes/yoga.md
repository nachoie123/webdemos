# Molde: yoga, pilates y centros de bienestar

Escrito el 21/09/2026 para **Kushala** (General Ramírez de Madrid 14, Cuatro
Caminos). Sirve para estudios de yoga, pilates y centros de bienestar pequeños.

---

## Qué hay que entender del sector, en una frase

**Quien no ha ido nunca no teme el precio: teme hacer el ridículo.** «Es que yo
no soy nada flexible», «me van a mirar», «no sé ni qué ropa se lleva». Ninguna
web de yoga contesta a eso, y es literalmente lo único que separa a esa persona
de entrar por la puerta.

---

## El orden correcto

1. **Quitar el miedo**, antes que nada. Tres frases exactas: no hace falta ser
   flexible, nadie mira, y se viene con lo puesto. Concretas, no místicas.
2. **El horario de clases, completo y legible.** Es lo que más se busca y lo
   que peor se enseña: casi todas lo esconden en un PDF o en una app. Va en la
   página, en una rejilla, sin pulsar nada.
3. **Qué clase es para quién.** «Hatha», «vinyasa» e «hipopresivos» no
   significan nada para quien empieza. Al lado, en castellano: para quien nunca
   ha hecho nada, para quien tiene la espalda mal, para después del parto.
4. Y al final, el precio.

---

## Orden de secciones (cópialo)

| # | Sección | Clases | Qué lleva |
|---|---|---|---|
| 1 | **Cabecera** | `.cab` + `u-nav` | Marca, menú y **móvil clicable**. |
| 2 | **Hero con dibujo** | `u-sangrado u-seccion` | El dibujo grande es **lo que este centro tiene y el de al lado no** (aquí: la hamaca de yoga aéreo). |
| 3 | **Tira de datos** | `u-tira` | Calle con portal · barrio · horario · teléfono. |
| 4 | **Lo que frena a todo el mundo** | `u-grid u-3` | Los tres miedos, contestados. **La sección que gana el molde.** |
| 5 | **Las clases** | `u-grid u-3` + dibujos | Nombre llano delante, término técnico detrás, y para quién es. |
| 6 | **El horario de clases** | rejilla propia | Completo, en la página, sin PDF ni app. |
| 7 | **Precios** | `u-precios` + `u-desigual-inv` | Clase suelta, bono y mensual. Y si la primera es gratis, **eso es el titular**. |
| 8 | **Su casa, no la de la plataforma** | `u-desigual` | Si está en ClassPass / Fresha / Urban Sports Club, el argumento de la puerta propia (ver `barberia.md`, demo 15). |
| 9 | **Dónde y horario** | `u-desigual-inv` | Día a día. |
| 10 | **Opiniones** | `u-grid u-3` + `u-cita` | Tres inventadas y marcadas. |
| 11 | **Nota única + pie legal** | — | Las 5 piezas obligatorias. |

---

## Lo que este molde PROHÍBE

- **Vocabulario místico sin traducir.** «Conecta con tu esencia» no vende una
  clase: la hace sonar a secta para quien duda.
- **Fotos de gente flexible haciendo posturas imposibles.** Es exactamente lo
  que asusta a quien no ha ido nunca. Aunque hubiera fotos, ésas no.
- **El horario en PDF o «descárgate la app».** Es el pecado del sector.
- **Prometer resultados de salud.** Misma regla que `salud.md` y `entrenador.md`:
  ni dolores que desaparecen, ni kilos, ni posturas corregidas.
- **Sánscrito sin castellano al lado.**

---

## La receta visual

Concepto: **índigo y cobre sobre crudo.** Ni beige-con-salvia ni tipografía
manuscrita: eso es el uniforme del sector y hace que todos los centros parezcan
el mismo. Índigo profundo para lo que se pulsa, cobre para los acentos.

```css
:root{
  --fondo:#efece6;  --fondo-2:#e0dbd1;   /* crudo cálido */
  --tinta:#16181d;  --tinta-2:#5e6068;
  --acento:#2d3a8c; --acento-tinta:#eef0ff;  /* índigo */
  --linea:#cec7bb;  --cobre:#b5793f;
  --display:'Marcellus', Georgia, serif;
  --texto:'Figtree', 'Helvetica Neue', Arial, sans-serif;
  --radio:0px;
}
```

---

## Las fórmulas de texto

- **El miedo, dicho con sus palabras.** *«Es que yo no soy nada flexible.»* Y
  debajo, la respuesta en una línea: *«Nadie lo es el primer día. Para eso se
  viene.»*
- **El nombre llano delante.** *«Para la espalda»* y detrás *«(hipopresivos)»*.
- **La hora exacta.** *«Martes 19:30, dura una hora.»*
- **Lo que tiene y el de al lado no.** Aquí, el yoga aéreo. Va en el dibujo
  grande, no en una lista.
