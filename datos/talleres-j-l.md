# Talleres J.L. — taller de mecánica y neumáticos

Verificada el 21/09/2026. **Corrige un error de la ficha antigua.**

| Dato | Valor | Cómo se ha comprobado |
|---|---|---|
| Nombre | Talleres J.L. | Páginas Amarillas, qdq, autosmotos, talleres.me |
| Teléfono | 91 315 27 30 (**fijo**) | Páginas Amarillas y varios directorios |
| Dirección | **Calle de José, 9** | Páginas Amarillas; el reverse confirma «Calle de José» |
| Barrio | Almenara · Tetuán · 28029 Madrid | reverse |
| Coordenadas | 40.4671186, −3.6963461 | ficha |
| Especialidad | **Mecánica y neumáticos** | tutaller.tv y directorios |
| Web propia | **No tiene** | ver abajo |

**Sin WhatsApp:** fijo, no entra en `out/enviar.html`.

## CORRECCIÓN: la ficha decía que tenía web y NO la tiene

`prospectos.json` lo tenía marcado como `estado_web: propia` con la nota «Web
propia real, anticuada pero suya». **Es falso.**

`talleresjl.es` responde con un 200, pero lo que sirve es:

> `<title>Alfredo Iglesias Morales</title>` ·
> `<meta description>` «su taller de mantenimiento y reparación de vehículos en
> **Zaragoza**»

Es **otro taller, en otra ciudad**. Talleres J.L. de Madrid no tiene nada que
ver con ese dominio.

Es la trampa de La Fiorería al revés: allí dimos por «sin web» a quien tenía una
tienda entera; aquí dimos por «con web» a quien no tiene ninguna. **Moraleja:
abrir la web y leer el `<title>` siempre, no fiarse del código 200.**

Y de paso es un aviso útil para él: quien busque «talleres JL» y encuentre ese
dominio acaba en un taller de Zaragoza.

## Lo que no se declara

- **El portal:** lo da Páginas Amarillas (el 9) y el reverse solo confirma la
  calle. Una fuente directa: no se pone.
- **Nota, opiniones, precios y horario:** no verificados.
- **Ninguna marca de neumático ni de recambio.** No hay fuente de con qué
  trabaja.

## El gancho: la medida del neumático

En neumáticos todo el mundo compara precio por internet, pero **primero hay que
saber qué pedir**, y casi nadie sabe leer el `205/55 R16 91V` del flanco. Un
taller que lo explique se lleva la llamada, porque es la barrera real.

Y encima da pie a lo segundo: **cuándo hay que cambiarlos**. El mínimo legal es
1,6 mm de dibujo, pero por debajo de 3 mm la frenada en mojado ya se alarga
mucho. Eso es información de seguridad, útil y verificable, y no la da nadie.

Es un ángulo completamente distinto al de Autonorte Sáez (que iba del coche de
sustitución), así que los dos talleres del proyecto no se parecen.
