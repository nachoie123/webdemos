# AEP Mantenimiento e Instalaciones — DESCARTADO 21/09/2026

**Motivo: SÍ tiene web, viva y actual.** No gastar demo. No volver a cogerlo.

## La web

- **https://bricoaep.com** — HTTP 200, `<title>` «Brico AEP | Brico AEP - Tu
  Ferretería de Confianza en Madrid». Tienda online completa (catálogo, cesta,
  cuenta de usuario, 4 idiomas), pie «© 2026 · Desarrollado por Elektro3».
- Es **el mismo negocio**, no un homónimo: en su página de contacto figuran el
  **mismo teléfono (+34 913 159 338)** y la **misma dirección (C/ Mauricio
  Legendre, 5 - 28046 Madrid)** que la ficha OSM del prospecto.
- Su página «Empresa» cubre también la parte de instalaciones: «Realizamos todo
  tipo de trabajos de electricidad, cambios de tensión, INSTALADOR AUTORIZADO,
  proyectos eléctricos, montaje de voz/datos», y delegación de Fenie Energía.
  O sea: la web cubre las dos patas del negocio, ferretería e instalaciones.
- Email publicado: aeptienda@gmail.com (no hizo falta buscarlo).

`sistema/tiene_web.py` **no lo caza**: el dominio (bricoaep) no se deriva del
nombre del prospecto (AEP Mantenimiento e Instalaciones). Es el mismo agujero
que el de Fitness FEDA. La pista salió de una búsqueda por el nombre comercial
de la tienda, «Ferretería AEP Plaza Castilla».

## Lo demás que se verificó antes de descartarlo

- **Qué hace:** ferretería de barrio + empresa instaladora eléctrica. CNAE 4222
  «Construcción de redes eléctricas y de telecomunicaciones». No es clima ni
  contra incendios; el cliente principal es de mostrador, no un administrador
  de fincas.
- **Tamaño:** A.E.P. MANTENIMIENTO E INSTALACIONES S.L., CIF B80428543,
  constituida en 1993, **2 empleados** (Empresite / eEconomista). Un solo local.
- **Dirección real:** Mauricio Legendre 5 (su propia web y Páginas Amarillas).
  El reverse de Nominatim sobre 40.46936,-3.68709 devuelve la calle sin portal;
  los directorios discrepan del local (LOC 10B en Empresite, «local 40» en
  Waze). Da igual: descartado.
- **Segundo fijo publicado:** 913523367 (Empresite).

**Ojo con el resto de la galería de Mauricio Legendre 5-7.** La idea de
«ofrecerla en bloque» que está apuntada en `datos/carniceria-nicar.md` tiene un
agujero: al menos uno de los cinco (AEP) ya tiene tienda online.
