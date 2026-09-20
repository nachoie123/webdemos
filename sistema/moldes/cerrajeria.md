# Molde: cerrajería de urgencias

Primer molde fuera de la hostelería. **No se parece en nada al de restaurante y
no debe parecerse**: aquí nadie navega. El cliente está en el rellano, de noche,
con el móvil al 12% y la puerta cerrada. Todo lo que no sea un teléfono grande
estorba.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: cómo es este sector por dentro

Buscando «cerrajero Tetuán» (20/09/2026) salen **más de veinte webs
prácticamente idénticas**, cada una con un número distinto:
`cerrajerostetuanmadrid.com.es`, `cerrajerotetuan.es`, `cerrajerosready2open.com`,
`cerrajeromadrid24h.madrid`… Mismo diseño, mismas promesas, mismo «60 € low
cost», ningún nombre de persona y ninguna dirección.

**Casi ninguna es un cerrajero.** Son captadoras: cogen la llamada, se llevan una
comisión y mandan a un tercero que cobra lo que quiere al llegar. Es el sector
con peor fama de internet y el cliente lo sabe: llama con miedo a que le claven.

**De ahí sale todo el molde.** El cerrajero real del barrio no compite en ser más
barato ni en gritar «24H» más fuerte. Compite en ser **el único que se identifica**.

> Regla: si la página pudiera valer para cualquier cerrajero de España,
> está mal. Tiene que valer solo para este.

---

## Orden de secciones (distinto al de restaurante)

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero = teléfono** | Nada de nombre gigante. El botón de llamar es el elemento más grande de la página, visible sin bajar. Debajo: qué cuesta y en cuánto llega. |
| 2 | **Tira** | Zona · horario real (24h o no) · teléfono · «sin intermediarios». |
| 3 | **Precio dicho antes de ir** | La sección más importante. Una tabla de precios orientativos con la letra pequeña **al lado, no escondida**. Es lo contrario de lo que hace el sector. |
| 4 | **Quién soy** | Nombre y cara. Las webs de captación no tienen ninguno de los dos. Si no hay foto, el nombre y los años en el barrio. |
| 5 | **Qué hago y qué no** | Decir lo que NO se hace da más credibilidad que la lista de servicios. |
| 6 | **Zona de cobertura** | Barrios escritos con su nombre. «Madrid» no vale: el cliente quiere saber si viene a SU calle. |
| 7 | **Qué hacer mientras llego** | Tres consejos útiles gratis. Nadie más los da y cuesta cero. |
| 8 | **Opiniones** | Sin firma si no están verificadas, y diciéndolo. |
| 9 | **Urgencia vs. cita** | Dos caminos: llamar ahora, o pedir presupuesto sin prisa. |
| 10 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** galería, «sobre nosotros» de relleno, ni formulario largo. Nadie
rellena un formulario de seis campos encerrado en el portal.

---

## La receta visual

```css
:root{
  --fondo:#f6f4f1;  --fondo-2:#e7e3dd;   /* claro: se lee de día y de noche */
  --tinta:#16181c;  --tinta-2:#5e646d;
  --acento:#0b5d3b;                       /* verde: calma, no alarma */
  --alerta:#d4622a;                       /* naranja SOLO para el teléfono */
  --radio:4px;
}
```

**El color se elige al revés que en hostelería.** Rojo y negro son lo que usan
las webs de captación para meter prisa. Un verde sobrio dice «esto es un oficio,
no una urgencia que te van a cobrar». El único elemento cálido es el teléfono.

Tres reglas propias del sector:

1. **Contraste alto y cuerpo grande.** Se lee en un rellano a oscuras con una
   mano. Nada por debajo de 17px.
2. **El teléfono, tres veces:** cabecera, hero y barra fija de móvil. Y siempre
   como `tel:`, nunca como texto suelto.
3. **Cero animación de entrada en el hero.** Un `u-revelar` que tarda 700 ms es
   medio segundo mirando una pantalla en blanco. Se revela el resto, el hero no.

---

## Los textos

- **El titular dice el problema, no el servicio.** No «Cerrajería 24 horas», sino
  *«Se ha quedado fuera de casa»*.
- **El precio va con su condición pegada.** *«Apertura de puerta desde 60 € ·
  precio cerrado por teléfono antes de salir · +20 € de 22:00 a 8:00»*. Decir el
  recargo nocturno da credibilidad, no la quita.
- **Decir lo que no se hace.** *«No abro coches ni cajas fuertes»*.
- **La frase que mata a la competencia**, y solo puede decirla el que es real:
  *«Le coge el teléfono el mismo que va a ir»*.

---

## El JSON-LD

`@type` es **`Locksmith`**, no `LocalBusiness` a secas. Y lleva `areaServed` con
los barrios, que es la consulta que de verdad hace la gente.

`openingHours` de un 24h se escribe `"Mo-Su 00:00-23:59"`.

**Sin `aggregateRating`** si no hay número de reseñas verificado, igual que en
todas las demás.
