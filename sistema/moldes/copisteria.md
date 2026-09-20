# Molde: copistería / imprenta

Quinto molde. El cliente de una copistería **tiene una fecha de entrega**: un
trabajo mañana, una oposición el viernes, unas tarjetas para una feria el
jueves. No compara precios ni mira galerías.

Las clases `u-*` que se citan ya están en `sistema/base.css`.

---

## Lo primero: la pregunta es «¿lo tengo hoy?»

Nadie entra en una copistería a mirar. Se entra con un archivo y una prisa. Y
la web del sector, cuando existe, está escrita al revés: una lista de veinte
servicios (offset, digital, gran formato, vinilos, roll-ups…) y ninguna
respuesta a las dos únicas preguntas que importan:

1. **«¿Puedo mandarlo sin ir hasta allí?»**
2. **«¿Para cuándo lo tengo?»**

> Regla: si la página no contesta las dos en la primera pantalla, está mal.
> Todo lo demás —el catálogo, los acabados, los gramajes— va después.

**El botón principal no es "contactar": es mandar el archivo.** Por WhatsApp,
que es donde el cliente ya tiene el PDF. Un formulario de subida propio suena
mejor pero se usa menos: obliga a rellenar campos con el móvil en la mano.

---

## Orden de secciones

| # | Sección | Qué lleva |
|---|---|---|
| 1 | **Hero: mandar el archivo** | Titular sobre el plazo, no sobre la imprenta. Botón de WhatsApp con el mensaje escrito. |
| 2 | **Tira** | Calle · horario · teléfono · «entrega el mismo día» · «envío a domicilio». |
| 3 | **Los tres caminos** | Mandarlo y recogerlo · mandarlo y que lo lleven · ir en persona. En este sector, decir que se puede hacer sin ir es media venta. |
| 4 | **Precios de lo que la gente pide de verdad** | Copia B/N, color, encuadernado, plastificado. Cuatro precios claros valen más que un catálogo entero. |
| 5 | **Qué se imprime aquí** | Lista corta y humana: trabajos y TFG, oposiciones, tarjetas, carteles, planos. Escrito por lo que ES, no por la tecnología. |
| 6 | **Cómo mandar el archivo bien** | Tres consejos —PDF, a tamaño real, con márgenes— que ahorran un viaje. Nadie los da y cuestan cero. |
| 7 | **Horario día a día** | Cierran a mediodía y en agosto. Es el dato más buscado. |
| 8 | **Opiniones** | Sin firma si no están verificadas, y diciéndolo. |
| 9 | **Quién eres + pie legal** | Las 5 piezas obligatorias del README. |

**No lleva:** el listado de maquinaria, ni «soluciones integrales de artes
gráficas», ni fotos de rotativas de banco de imágenes.

---

## La receta visual

```css
:root{
  --fondo:#f7f6f3;  --fondo-2:#eae7e0;    /* papel, literalmente */
  --tinta:#191713;  --tinta-2:#615c53;
  --acento:#1f3fa8;                        /* azul de tóner, sobrio */
  --marca:#e0483a;                          /* rojo de registro, solo acentos */
  --radio:2px;
}
```

Tres reglas del sector:

1. **La página es papel.** Fondo hueso y márgenes generosos. Una copistería con
   una web oscura y con degradados se contradice a sí misma.
2. **Cian, magenta, amarillo y negro, pero con cuentagotas.** Una franja CMYK
   como separador es suficiente guiño. Cuatro colores planos de fondo, no.
3. **Números de plazo grandes, no de precio.** «Hoy mismo» pesa más que «desde
   0,05 €».

---

## Los textos

- **El titular habla de la entrega.** *«Mándelo ahora, recójalo hoy.»*
- **La frase que quita el viaje.** *«No hace falta que venga a traerlo: mándelo
  por WhatsApp y le decimos para cuándo está.»*
- **El precio de lo común, entero.** *«Copia en blanco y negro, 0,05 €.»*
- **Los consejos del oficio.** *«Mándelo en PDF y a tamaño real; si lo manda en
  Word, puede moverse todo al imprimir.»* Es útil, gratis, y hace que guarden
  la página.

---

## El JSON-LD

`@type` es **`PrintShop`**. Lleva `openingHours` día a día. **Sin
`aggregateRating`** salvo que la nota **y** el número de reseñas estén los dos
verificados: si dos fuentes dan recuentos distintos, no se declara ninguno.
