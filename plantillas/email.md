# Plantilla de correo

Un correo frío a un negocio que no te ha pedido nada tiene ~15 segundos de atención.
Todo lo que no quepa en esos 15 segundos sobra.

## Reglas que no se negocian

| Regla | Por qué |
|---|---|
| **Sin adjuntos.** Una imagen incrustada + un enlace. | Un adjunto de un desconocido es spam automático en medio Gmail. |
| **Menos de 120 palabras.** | Lo leen de pie, detrás de la barra, en el móvil. |
| **El asunto no vende, cuenta algo.** | "Mejora tu presencia online" va a Promociones. "Busqué quién tocaba y no lo encontré" se abre. |
| **Identifícate con nombre y apellidos.** | Lo exige la LSSI (art. 21) y además es lo que te hace creíble. |
| **Línea de baja al final.** | Lo exige la ley y te ahorra denuncias. Una línea, sin drama. |
| **Un solo enlace.** | Dos o más enlaces disparan los filtros. |
| **Tuteo en hostelería y comercio, usted en salud y gestorías.** | Una dentista tuteada por un desconocido cierra el correo. |

## La plantilla

**Asunto:** `{gancho_real}`

> Ejemplos de gancho, siempre algo que te pasó de verdad:
> - `Busqué quién tocaba hoy en KMASPUES y no lo encontré`
> - `Vuestra ficha de Google lleva a la pastelería de Segovia`
> - `Os he hecho una página. No hace falta que me contestéis`

```
Hola{coma_nombre}:

Soy Nacho San Benito, desarrollador web freelance. Estudio el doble grado de
Administración de Empresas e Informática en IE University, aquí al lado en
Castellana.

{el_problema_en_una_frase}

Así que os he montado una propuesta de cómo podría ser vuestra página.
Está hecha, se puede abrir y se puede tocar:

{enlace}

Las fechas y los precios son inventados — dentro hay un botón que os
marca qué es de ejemplo. La dirección, el teléfono y el estilo salen de
vuestra ficha real.

Si os gusta, contestad a este correo y lo hablamos. Si no, no pasa nada.

Nacho San Benito
{telefono} · {email}

Si no queréis recibir nada más, responded BAJA y no os vuelvo a escribir.
```

## El bloque de imagen (HTML del correo)

Va justo debajo del enlace. Una imagen, ancho fijo, con `alt` de verdad
(si el cliente bloquea imágenes, el `alt` es todo lo que queda) y
envuelta en el mismo enlace.

```html
<a href="{enlace}" style="display:inline-block;text-decoration:none;">
  <img src="{url_mockup}" width="300" alt="La página de {negocio} en un móvil: nombre grande, agenda de conciertos y botón de reservar mesa" style="display:block;border:0;max-width:100%;border-radius:8px;">
</a>
```

`{url_mockup}` tiene que ser una URL pública (súbela al mismo sitio que la demo).
Nada de `cid:` ni base64: los dos huelen a spam.

## Ejemplo real — KMASPUES

**Asunto:** Busqué quién tocaba hoy en KMASPUES y no lo encontré

```
Hola:

Soy Nacho San Benito, desarrollador web freelance. Estudio el doble grado de
Administración de Empresas e Informática en IE University, aquí al lado en
Castellana.

El jueves quise ver quién tocaba en KMASPUES antes de acercarme y no
encontré nada: solo la ficha de Google. Eso es un cliente que no entra.

Así que os he montado una propuesta de cómo podría ser vuestra página,
con la agenda de directos delante del todo. Está hecha, se puede abrir
y se puede tocar:

https://demos.nachosanbenito.me/kmaspues

Las fechas y los precios son inventados — dentro hay un botón que os
marca qué es de ejemplo. La dirección, el teléfono y el estilo salen de
vuestra ficha real.

Si os gusta, contestad a este correo y lo hablamos. Si no, no pasa nada.

Nacho San Benito
682 02 05 47 · nsanbenitop@gmail.com

Si no queréis recibir nada más, responded BAJA y no os vuelvo a escribir.
```

108 palabras. Se lee en 20 segundos.

## Lo que NO poner

- **"Somos una empresa"** si no hay empresa. El "estudiante de IE que ya ha hecho
  esto antes" es una carta mejor: barato, cercano, y nadie espera que le
  factures 4.000 €. En cuanto dices "empresa" te comparan con una agencia.
- **Precio en el primer correo.** El primer correo solo vende la reunión.
- **"Sin compromiso", "aprovecha esta oportunidad", "solución integral".**
  Vocabulario de spam.
- **Seguimientos automáticos.** Uno solo, a mano, a los 6-7 días, de dos líneas.
  Más es acoso y quema el dominio.
