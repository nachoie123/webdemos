# Flores Yohana Alonso S.L. — datos verificados

Comprobado el 20/09/2026 antes de escribir la demo.

## Lo que está verificado

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Flores Yohana Alonso S.L. | ficha de Google + Registro (es una S.L. real) |
| Móvil (WhatsApp) | 687 42 90 77 | ficha de Google |
| Fijo | 91 765 05 81 | Páginas Amarillas, Empresite |
| Dirección | Paseo de la Castellana, 133 | Páginas Amarillas + 2pos.es, **dos fuentes** |
| Código postal | 28046 Madrid | Páginas Amarillas |
| Dónde está | En la Plaza de Cuzco, en el Hotel AC Cuzco | Nominatim: el reverse de las coordenadas cae dentro de «AC Cuzco» |
| Coordenadas | 40.4587815, −3.690837 | ficha de Google |
| Web propia | **No tiene** | `tiene_web.py` (limpio) + búsqueda: solo directorios |

Aquí **sí hay número de portal**, al contrario que en Rosario Pino: dos fuentes
independientes dicen 133 y el reverse cae en el hotel de ese número.

## Lo que NO está verificado — y por eso no se declara

- **La nota.** `prospectos.json` decía 4,8★; un directorio dice 5,0 sobre 5
  opiniones. **Las fuentes no coinciden y el recuento no está confirmado**, así
  que no se declara `aggregateRating`. Es el mismo caso que Imprime y Más.
- **El nombre de quien atiende.** Un directorio resume opiniones que hablan de
  «Antonio», pero es un resumen de terceros, no una fuente. No se pone en la
  página: se pregunta en el mensaje.
- **Horario, precios y catálogo.** No están publicados en ningún sitio. Todo
  marcado con `data-ejemplo`.
- **Código postal.** Nominatim devuelve 28020 para el carril bici; Páginas
  Amarillas da 28046 para el portal 133, que es el que vale.

## Gancho real

Es una floristería **dentro del vestíbulo de un hotel**, en la Plaza de Cuzco,
rodeada de las torres de oficinas de la Castellana. Eso cambia el negocio
entero y no se puede leer en ninguna parte:

- **Le compra gente con prisa**: alguien que baja del hotel, alguien que sale de
  una reunión, alguien que se ha acordado a las siete de la tarde.
- **La pregunta no es «cuánto cuesta»**, es **«¿llega hoy?»**. Ninguna
  floristería del barrio contesta eso en su web, porque ninguna tiene web.
- **Y nadie busca «ramo de doce rosas»**: busca «se ha muerto el padre de un
  compañero» o «se me ha olvidado un cumpleaños». La página se ordena por
  **ocasión y por hora de entrega**, no por flor.

## Regla que hereda de Kali

**Nada de fotos de Google Maps.** El catálogo va con **marcos vacíos y
rotulados**, y el mensaje pide las fotos suyas.
