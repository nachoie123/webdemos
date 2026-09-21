# Reformas y decoración CKN — DESCARTADO (21/09/2026)

**Motivo: sin canal escribible. No hay correo ni móvil publicados en ninguna parte,
y no hay ni una sola huella del negocio en la web abierta.**

## Qué se comprobó

| Comprobación | Fuente | Resultado |
|---|---|---|
| ¿Tiene web? | `sistema/tiene_web.py` + WebSearch («Reformas y decoración CKN Madrid», «CKN reformas Hierbabuena Madrid teléfono») | **No.** Cero resultados del negocio. |
| Dominios derivados del nombre | `curl` a reformasckn.es/.com, cknreformas.es/.com, reformasydecoracionckn.es | Todos **sin resolver** (000). `ckn.es` sí resuelve (200) pero su `<title>` es «SERVICIO INFORMATICO»: **homónimo, no es este negocio**. |
| Dirección real | Nominatim reverse `40.46040,-3.70150` | «Reformas y decoración CKN, 16C, Calle de la Hierbabuena, Berruguete, Tetuán, Madrid, 28039». Coincide con la ficha. |
| Reverse del teléfono 914502789 | WebSearch + Bing | **Ningún negocio asociado.** |
| Correo o móvil publicado | WebSearch, Bing, Páginas Amarillas (búsqueda «CKN» en reformas Madrid), empresite/eInforma/Axesor, Facebook/Instagram | **Nada.** No aparece en ningún directorio del sector ni en redes. DuckDuckGo devolvió CAPTCHA (no se resuelve). |
| Tags OSM completos | API de OSM, `node/2935592566` | Solo `phone=+34 91 450 27 89`. **Sin `email`, sin `contact:mobile`, sin `website`.** |

## Y además: la ficha está muerta

El nodo de OSM es **version 1, creado el 2014-06-27 por el usuario `jenizaro` y
nunca tocado desde entonces**. Doce años sin una sola edición, combinado con cero
huella digital (ni Google, ni Facebook, ni Habitissimo, ni Páginas Amarillas, ni
registro mercantil), apunta a que la empresa **ya no opera**. Es exactamente el
caso que avisaba el encargo: «las empresas de reformas pequeñas cierran y la ficha
de OSM se queda».

## Conclusión

Solo fijo (91…), al que no se le manda un WhatsApp. Sin correo verificado y sin
móvil verificado **no hay canal escribible**, y no se inventa ninguno. Descartado.

Sustituto elegido: **Pescadería Antonio del Río** (puesto 6 del Mercado de San
Enrique), ver `datos/pescaderia-antonio-del-rio.md`. Salió de un barrido propio
de Overpass en la zona suroeste y está a ~470 m del punto de referencia.

## El molde de reformas queda sin escribir, y por qué

El encargo pedía `sistema/moldes/reformas.md`. **No se ha escrito**: un molde
existe para dar forma a una demo concreta, y sin candidato del sector no hay
página contra la que validarlo. En el barrido tampoco apareció ninguna otra
reformista con canal escribible: las del entorno (Reformas Castilla, RSC
Reformas y obras, Construcciones Antonio de Diego Álvaro, Tomás Bruña
Construcciones) no tienen ni teléfono en OSM ni rastro en la web abierta.

**El ángulo, apuntado para quien coja un día una reformista de verdad** (no se
pierde el razonamiento): la pregunta del cliente de reformas no es «qué hacéis»
—eso es `reparaciones.md`, y allí el miedo es una avería de 80 €—, sino
**«¿me vais a dejar la obra a medias, y el precio final va a ser el del
presupuesto?»**. Son 20.000 € y tres meses con la casa levantada, y todo el
mundo conoce a alguien a quien le pasó. Lo que nadie del sector pone por
escrito y ahí habría que poner: el **presupuesto cerrado con lo que incluye y
lo que no**, un **calendario por semanas** de una reforma tipo, **la cláusula
del imprevisto** (qué pasa, y a qué precio, si aparece algo detrás del tabique)
escrita *antes* de firmar, y el **jefe de obra con nombre y teléfono directo**.
Si además hacen decoración, la puerta de entrada es otra: «¿me ayudáis a decidir
o tengo que llevarlo yo todo elegido?».
