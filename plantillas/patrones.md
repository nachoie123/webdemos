# Repertorio de patrones — webs de comercio local

Barrido del 20/09/2026. **66 webs reales** analizadas con `../barrido.py`
(datos crudos en `barrido.json`, candidatas en `urls-candidatas.txt`) + 30 reels
de diseño de la colección Informaclaude + neuform.ai, efferd.com, superdesign.dev.

No es una plantilla. Es **una carta de platos**: cada demo elige de aquí,
igual que un cocinero elige de la despensa, y sale distinta.

---

## 1. La foto de familia: qué hacen TODOS

De los 66 sitios que respondieron (otros 21 dominios ni existían — comprobado, no
supuesto):

| Pieza | Cuántos la tienen |
|---|---|
| Instagram enlazado | 74 % |
| Sección "quiénes somos" | 79 % |
| Teléfono clicable en algún sitio | 53 % |
| WhatsApp | 54 % |
| Mapa embebido | 45 % |
| Barra pegajosa al hacer scroll | 43 % |
| Reservas / cita online | 27 % |
| **Teléfono en la primera pantalla** | **21 %** |
| Datos de negocio en JSON-LD (Google) | 6 % |

Los dos últimos son el hueco. **25 de 66 webs no tienen ni teléfono clicable ni
mapa**: el cliente tiene que buscarse la vida. Y solo 4 de 66 le cuentan a Google
quién son, dónde y a qué hora abren. Ahí se gana la demo sin pelear por gusto.

**Dato crudo de la despensa:** 44 de 66 son WordPress. La mediana es de 3.507
palabras de portada. Nacho llega con un HTML de una pieza que carga en un
suspiro — eso es una ventaja real, no un detalle.

---

## 2. El hero: cuatro maneras, no una

Ningún hero bueno decía el nombre del negocio y ya. Los cuatro moldes que salieron:

1. **Promesa + prueba.** Arteflor: *"Floristería en Madrid con entrega a domicilio
   el mismo día"* y, pegado, el 4,9/5,0 de Google con 250 reseñas.
   → Para negocios con reseñas buenas. Sacar la nota de Google al hero.
2. **Categoría + fricción resuelta.** Talleres en Madrid: *"Taller en Madrid con
   presupuesto claro y cita por WhatsApp"*. Nombra el miedo del cliente (la
   factura sorpresa) y lo mata en la misma frase.
   → Para servicios donde el cliente desconfía: talleres, dentistas, reformas.
3. **Producto concreto que da hambre.** Madreamiga: *"Hola! Prueba el Banana
   Bread — plátano maduro, canela y ese aroma a recién horneado"*. Ni logo ni
   eslogan: un producto y su olor.
   → Para panadería, pastelería, cafetería, heladería. **Es el molde de Acueducto.**
4. **Posicionamiento + escasez.** The Barba Shop: *"Alta Barbería"*, un cliente a
   la vez, reserva en 1 minuto sin registrarse.
   → Para barberías, estética, entrenamiento personal.

El reel de @polidori.dev lo resume mejor que ningún manual: *el mejor griego no
necesita carta para venderse, necesita que lo huelas*. Foto de plato sobre mantel
blanco = web genérica. Aceite cogiendo la luz = web de ESE sitio.

---

## 3. Teléfono, horario y dirección: dónde van de verdad

El patrón que repiten los que lo hacen bien (Pérez Illán es el caso de libro) es
**tres apariciones, tres formatos distintos**:

- **Cabecera:** teléfono como `tel:` + botón de acción (Reservar / Cita previa).
  Solo 1 de cada 5 lo hace. Ponerlo siempre.
- **A media página:** el CTA repetido en su propio bloque, con la objeción al
  lado. The Barba lo clava: junto al botón, *"Cancelación flexible hasta 2h
  antes"*. El botón pide, la letra pequeña tranquiliza.
- **Pie:** dirección completa, horario escrito día por día (`Lun–Vie 8:00–20:00,
  Sáb 10:00–14:00`), enlace a Maps, email.

En móvil, barra fija abajo con dos botones: **Llamar** y **Cómo llegar**
(o WhatsApp si el negocio contesta por ahí). 43 % ya usa algo pegajoso;
casi ninguno lo usa para esto.

---

## 4. Catálogo y precios: tres formatos

- **Tarjeta de servicio** (barberías, talleres, clínicas): nombre, **precio**,
  **duración**, una línea de descripción, botón de reservar. The Barba pone
  22 €–350 € a la vista. Da confianza, no la quita.
- **Rejilla de producto con precio en euros e IVA incluido** (floristerías,
  tiendas): Arteflor va de 25,00 € a 173,50 €, con categorías arriba
  (Rosas, Ramos, Plantas, Coronas, Bodas).
- **Carta como carta** (hostelería): secciones y platos, sin PDF. El PDF de la
  carta es el pecado número uno del sector — nadie lo abre en el móvil.

**Solo 8 de 66 enseñan precios en portada.** Es raro, y por eso funciona: si el
negocio tiene precios presentables, sacarlos es diferenciación gratis.

Del teardown de @shovel.studio (Yeezy vs Skims): **menos opciones venden más**
cuando el catálogo es corto, y un pop-up que aparece a los 6–10 segundos recoge
un 26 % más de emails que el que salta de golpe. Para un bar de barrio: no meter
50 platos, meter 8 y que se vean.

---

## 5. Confianza: qué usan en vez de decir "somos los mejores"

En orden de cuánto aparecen y cuánto pesan:

1. **Años en el barrio** con número ("20 años", "23 años, negocio familiar").
2. **Reseñas reales con nombre y caso concreto** — Arteflor cita *"10 ramos para
   una graduación"*. Un caso concreto vale más que cinco estrellas sueltas.
3. **Cara y nombre del equipo.** 37 de 66 tienen sección de equipo.
4. **Marcas o proveedores** (el taller nombra Bosch, Brembo, Valeo).
5. **Premios y menciones**, si los hay.

---

## 6. Tipografías y colores: lo que se repite (y por qué huir)

Lo más usado en el barrido: Roboto (6), Open Sans (6), Poppins (4),
Montserrat (4), Raleway, Jost, Lato, DM Sans, Inter.
Colores dominantes: blanco (44 de 66), negro (20) y grises de plantilla
(`#32373c` es el gris de WordPress por defecto — aparece 5 veces).

**Conclusión:** Poppins sobre blanco ES el look genérico de plantilla. Para que
una demo se note hecha a mano, la tipografía tiene que venir del negocio, no del
top 5. Combinaciones que salieron en los sitios con carácter y funcionan por tipo:

- **Panadería / pastelería:** serif de display (Abril Fatface, Playfair) + texto
  neutro. Fondo crema, no blanco.
- **Bar / pub de noche:** fondo oscuro de verdad (`#0a0a0a`), acento saturado
  único, sans condensada. Es lo que se hizo en KMASPUES.
- **Barbería / estética masculina:** negro, un dorado o azul, todo en mayúsculas
  con mucho espaciado.
- **Taller / ferretería:** fondo claro, un azul o naranja de señal, tipografía
  ancha y legible. Aquí la confianza pesa más que el gusto.
- **Floristería / clínica:** claro, mucho aire, verde o rosa palo, serif suave.

De las fuentes de Nacho: **efferd.com** da bloques shadcn ya montados (hero,
FAQ, footer, contacto) — sirve como catálogo de estructuras, no para copiar
código. **neuform.ai** son landings HTML con su prompt al lado: el prompt es lo
valioso. **superdesign.dev** es el lienzo para sacar 3 direcciones a la vez y
elegir, en vez de acertar a la primera.

---

## 7. Lo que NO hay que copiar

- Carrusel de fotos gigante que tarda en cargar (WordPress lo pone solo).
- La carta o la lista de precios en PDF.
- "Bienvenidos a nuestra web" como titular.
- Fotos de banco de imágenes: se huelen. Mejor ninguna foto y color bien puesto.
- Formulario de contacto de 6 campos cuando el negocio solo quiere que le llamen.
- Blog abandonado (47 de 66 tienen blog; la mayoría con la última entrada de 2023).

---

## 8. Receta para la próxima demo

1. Elegir **un molde de hero** de los 4 (§2) según el tipo de negocio.
2. Elegir **una paleta y una pareja de tipografías** de §6 — nunca Poppins/blanco.
3. Montar el orden: hero → prueba social → lo que vende (carta/servicios/catálogo
   con precio) → quiénes somos con cara → horario + mapa + teléfono → pie legal.
4. Poner el teléfono en la cabecera y la barra fija en móvil (§3).
5. Añadir el **JSON-LD de LocalBusiness** — lo tiene el 6 %, es media hora y es
   un argumento de venta que se explica en una frase.
6. Encima de todo eso, las **5 piezas obligatorias** del README (barra amarilla,
   botón "Ver qué es de ejemplo", datos reales de su ficha, quién eres, pie legal).

Regla de oro: si al taparle el logo la demo podría ser de cualquier otro negocio,
no está terminada.
