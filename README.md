# webdemos — enseñarle a un negocio la web que no tiene

## La idea en una frase

No le cuentes al dueño del bar cómo sería su escaparate: **móntale el escaparate
y mándale la foto.**

## Por qué NO un vídeo generado con IA

Era la primera idea y es la peor. Motivos, en orden de importancia:

**1. El vídeo no se puede tocar.** El dueño de KMASPUES abre el correo detrás de
la barra. Si es un vídeo, lo ve y ya. Si es un enlace, lo abre en el móvil, pulsa
"Reservar mesa" y le llega un WhatsApp a él mismo. Eso último cierra la venta; lo
otro es un anuncio.

**2. Si le gusta, hay que hacerla igual.** El vídeo no ahorra el trabajo, solo lo
aplaza — y encima lo aplaza al momento en el que ya hay un cliente esperando.

**3. La IA de vídeo no sabe escribir.** Veo, Sora y compañía renderizan texto
ilegible. Una web es 90% texto. Sale un borrón bonito con letras falsas.

**4. Cuesta dinero y tiempo.** Cada clip son minutos de espera y céntimos o euros
por intento. Una página estática la escribe Claude en 10 minutos y cuesta 0 €.

**5. El vídeo sale gratis de la página.** `shoot.py` graba el scroll de la página
real y saca un GIF. Así que haciendo la página tienes el vídeo; haciendo el vídeo
no tienes la página.

> **La frase corta:** la demo más barata de hacer es la de verdad.

## El bucle, por negocio

```
1. Elegir      →  prospectos.json  (los 30 de la zona Cuzco, 26 sin web)
2. Construir   →  Claude escribe demos/<slug>.html         ~10 min
3. Publicar    →  git push  →  demos.nachosanbenito.me/<slug>
4. Fotografiar →  python3 shoot.py demos/<slug>.html       ~20 s
5. Escribir    →  plantillas/email.md                      ~2 min
6. Enviar      →  a mano, desde tu Gmail. Nunca en masa.
7. Anotar      →  prospectos.json: enviado / respuesta
```

Unos 15 minutos por negocio. Los 30 caben en un fin de semana.

### 2. Construir

Cada demo se escribe a mano (bueno: Claude a mano). Nada de plantilla común: una
barbería y una clínica dental no se parecen en nada, y si las 30 demos son la
misma plantilla con otro logo, el dueño lo nota en dos segundos.

Lo que sí se repite, y es obligatorio:

- **Barra amarilla arriba:** "Demo · propuesta de web para X. No es su web oficial."
- **Botón «Ver qué es de ejemplo»:** marca con línea discontinua todo lo inventado.
- **Todo lo real, real:** dirección, teléfono y enlace de Maps salen de su ficha.
- **Sección final de propuesta:** quién eres, por qué les escribes, qué es mentira.
- **Pie legal:** "sin relación oficial; si prefieren que se retire, se retira hoy."

Esas cinco cosas no son burocracia. Son la diferencia entre *una propuesta* y
*una web falsa a nombre de otro*, que es un problema legal de verdad.

Ejemplo terminado: [`demos/kmaspues.html`](demos/kmaspues.html).

### 4. Fotografiar

```bash
python3 shoot.py demos/kmaspues.html
```

Deja cuatro archivos en `out/`:

| Archivo | Para qué | Tamaño típico |
|---|---|---|
| `<slug>-mockup.png` | **la imagen del correo** — la portada dentro de un móvil | ~380 KB |
| `<slug>-scroll.gif` | WhatsApp, Instagram, stories | ~1 MB |
| `<slug>-og.png` | la miniatura cuando alguien comparte el enlace | ~290 KB |
| `<slug>-movil.png` | la página entera, por si la quieres cortar | ~1,2 MB |

Usa Playwright con el Chrome que ya tienes. No hace falta ffmpeg ni instalar
navegadores.

> **En el correo va el PNG, no el GIF.** Outlook de escritorio congela los GIFs en
> el primer fotograma y un GIF de 1 MB en un correo frío es una bandera roja para
> los filtros. El GIF es para WhatsApp.

### 6. Enviar — leer esto antes

España tiene la LSSI, que es **más dura que la media europea**: el artículo 21
prohíbe el correo comercial no solicitado, sin la excepción de "interés legítimo
B2B" que sí se usa en otros países de la UE. Enviar esto no es riesgo cero.

La zona de riesgo bajo, en la práctica:

- **A la dirección pública del negocio** (`info@`, `contacto@`), nunca a una
  personal de alguien que trabaja ahí.
- **Pocos y a mano.** 30 correos escritos uno a uno no son una campaña.
- **Baja clara en el pie**, y respetarla el mismo día.
- **Nada de listas compradas ni scraping masivo.**
- **Un seguimiento como mucho**, a los 6-7 días.

**La alternativa que se salta el problema entero: el teléfono.** Tienes el móvil
de 28 de los 30. Una llamada no es comunicación comercial electrónica y en
hostelería funciona mejor que cualquier correo. El guion es el mismo: "os he
hecho una página, ¿os la mando por WhatsApp?".

(Esto no es asesoramiento legal, es lo que hay que tener en cuenta.)

### Las fotos del negocio

No te bajes sus fotos de Google Maps para meterlas en la demo: casi todas las
hizo un cliente y el copyright es suyo. Para la demo, tipografía y color — que
además queda mejor. Las fotos reales llegan cuando firman.

## De dónde salió esto

- La lista de 30: artefacto **Prospectos Cuzco** (09/09/2026), verificada en
  Google Maps → `prospectos.json`.
- El formato "le monto la web antes de que me la pida": de tu colección
  **Informaclaude** en Instagram (`~/Projects/ig-saved`), el reel de
  `gozie.okenu.backup`, "Day 27 of building Websites & AI for businesses without
  asking". Él lo hace puerta a puerta; esto es lo mismo por correo.
- El alojamiento: mismo montaje que `bote.nachosanbenito.me` — GitHub Pages con
  un CNAME en tu dominio.

## Pendiente

- [ ] Repo `webdemos-publico` en GitHub Pages con `demos.nachosanbenito.me`
- [ ] Buscar los correos de los 30 (los que tengan; muchos solo tienen móvil)
- [ ] Segunda demo: **Pastelería Acueducto** — su ficha enlaza a la pastelería
      homónima de Segovia, o sea que llevan meses mandándole clientes a otro
      negocio. Es el correo más fácil de escribir de los 30.

---

## El sistema (desde 20/09/2026)

Tres piezas en `sistema/`. Nacidas de comparar **19 webs de pastelería premiadas**
con las **66 webs de barrio** del barrido (`plantillas/patrones.md`).

| Fichero | Qué hace |
|---|---|
| `sistema/base.css` | Los huesos: rejilla, escala tipográfica, hero a sangre, barra de móvil. **Sin identidad visual.** Cada demo redefine 9 tokens y sale distinta. |
| `sistema/montar.py` | Mete `base.css` dentro de la demo y la escribe en `docs/<slug>/index.html`. Mata la trampa de copiar a mano. |
| `sistema/revisar.py` | Audita la demo contra 20 reglas. Si hay un fallo, no se envía. |

Bucle nuevo:

```bash
python3 sistema/montar.py demos/<slug>.html && python3 sistema/revisar.py docs/<slug>/index.html
```

### Lo que separa una web buena de una del montón

Dato del barrido, no opinión:

| | 19 premiadas | 66 de barrio |
|---|---|---|
| Google Fonts del top 5 (Poppins, Roboto…) | **casi ninguna** | mayoría |
| Reserva / pedido online | 63 % | 27 % |
| JSON-LD para Google | 36 % | 6 % |
| Palabras de portada (mediana) | 2.825 | 3.507 |

Las buenas **no son más grandes, son más raras**: tipografía que no viene del top 5,
una sección a sangre, un titular con voz («Our Happy Place», «Real bread, no shortcuts»)
y menos texto. Las del montón son todas la misma plantilla con otro logo.

### Los 9 tokens que define cada demo

`--fondo --fondo-2 --tinta --tinta-2 --acento --acento-tinta --linea --display --texto`
(+ `--radio`: 0 para editorial, 999px para amable).

Cambiar esos diez valores y elegir otro molde de hero (§2 de `patrones.md`) da una
demo que no se parece a la anterior aunque comparta los huesos.

## 21/09/2026 — un dibujo propio en cada demo

Nacho, mirando las 13 primeras: «se están viendo muy genéricas y muy AI».
Tenía razón, y la causa estaba localizada: **la página era un muro de texto y
le hablaba al dueño en cada sección** («esto es de ejemplo, dime el tuyo»,
hasta 13 veces en una sola demo). Eso es lo que igualaba a todas.

Tres reglas nuevas, y las tres las audita `sistema/revisar.py`:

1. **Un dibujo propio, mínimo.** Un `<svg>` con `viewBox` dentro del `<body>`,
   dibujado a mano **para ese negocio**. No se pueden usar fotos —el copyright
   es de quien las hizo y las de banco se huelen—, así que se dibuja. Si el
   dibujo sirve para otra demo, no vale: es clipart.
2. **Máximo 4 «de ejemplo» en el texto visible.** Marcar con `data-ejemplo` es
   gratis y no molesta. Escribirlo en prosa después de cada sección convierte
   la web del negocio en un correo dirigido al dueño. **Todas las salvedades
   van juntas, una vez, en un solo bloque** al final.
3. **Ningún párrafo por encima de 430 caracteres** (aviso). Se leen en
   diagonal, o sea que no se leen.

El listón sigue siendo shenxien.es: **más fotos, más fácil de leer, más
personalizada**. Sin fotos propias, lo que acerca a ese listón es dibujo,
color, cifras grandes y menos prosa.
