# SIGMA — datos verificados

Comprobado el 21/09/2026 antes de escribir la demo.

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | SIGMA | ficha de Google |
| Móvil (WhatsApp) | 654 59 76 52 | ficha de Google |
| Calle | Paseo de la Castellana | Nominatim (reverse) |
| Portal | **123 · sin confirmar** | solo Nominatim. Una fuente, no dos |
| Barrio | Castillejos · Tetuán · 28046 | Nominatim |
| Coordenadas | 40.4581283, −3.6907625 | ficha de Google |
| Web propia | **No tiene** | `tiene_web.py` + 2 búsquedas: ni una mención |

## Lo que no se declara

- **El portal.** El reverse devuelve el 123, pero es una sola fuente. Va la
  calle sin número y se pregunta.
- **Nota y opiniones.** No aparecen en ninguna fuente accesible.
- **Carta, precios, horario y hasta qué tipo de bar es.** No hay ni una sola
  mención de SIGMA en internet fuera de su ficha. Es el prospecto con menos
  información de todo el proyecto.

## Gancho real

Dos cosas, y las dos salen del sitio, no del sector:

1. **El nombre es el diseño.** SIGMA es Σ, el signo de sumar. Un bar que se
   llama «la suma» al pie de las torres de oficinas de la Castellana se escribe
   solo: **el mismo sitio en tres momentos del día** — el café de las ocho, el
   menú de las dos y la caña de las siete. Σ = la suma del día.
2. **El cliente es de oficina, y su pregunta es la hora.** En Cuzco, a las 14:15
   no se busca «bar»: se busca dónde queda mesa. Un bar de esta zona que ponga
   **a qué hora hay sitio** gana la comida sin bajar el precio del menú.

## Qué hay que preguntarle

Todo, literalmente. Empezando por el portal y por qué tipo de bar es: la demo
está escrita sobre una hipótesis razonable (bar de barrio en zona de oficinas),
y el mensaje lo dice con todas las letras.
