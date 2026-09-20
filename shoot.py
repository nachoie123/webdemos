#!/usr/bin/env python3
"""
De una demo HTML a los archivos que van en el correo.

    python3 shoot.py demos/kmaspues.html

Deja en out/:
    <slug>-movil.png    captura entera de la pagina, ancho movil
    <slug>-mockup.png   la captura dentro de un movil, sobre fondo claro -> esto es lo que se pega en el email
    <slug>-scroll.gif   12 s de scroll automatico -> para WhatsApp o Instagram
    <slug>-og.png       1200x630 para la previsualizacion del enlace

Necesita: playwright (usa el Chrome del sistema, no hace falta instalar navegadores) y Pillow.
No necesita ffmpeg.
"""

import sys, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent
SALIDA = RAIZ / "out"

ANCHO_MOVIL = 390          # iPhone 15 en puntos
ALTO_MOVIL = 844
ESCALA = 3                 # retina
FRAMES_GIF = 28
ALTO_GIF = 620             # px del gif final
FONDO_MOCKUP = (243, 240, 234)


def capturar(html: Path, slug: str = None):
    from playwright.sync_api import sync_playwright

    url = html.resolve().as_uri()
    slug = slug or html.stem
    SALIDA.mkdir(exist_ok=True)

    with sync_playwright() as p:
        nav = p.chromium.launch(channel="chrome")

        # --- movil: pagina entera + frames de scroll ---
        ctx = nav.new_context(
            viewport={"width": ANCHO_MOVIL, "height": ALTO_MOVIL},
            device_scale_factor=ESCALA,
            # sin is_mobile: si el HTML no trae <meta viewport> propio, Chrome
            # lo maquetaria a 980px y la captura saldria "alejada"
            has_touch=True,
        )
        pag = ctx.new_page()
        pag.goto(url, wait_until="networkidle")
        pag.wait_for_timeout(1200)          # que carguen las fuentes de Google

        entera = SALIDA / f"{slug}-movil.png"
        pag.screenshot(path=str(entera), full_page=True)

        alto_total = pag.evaluate("document.body.scrollHeight")
        recorrido = max(0, alto_total - ALTO_MOVIL)
        frames = []
        for i in range(FRAMES_GIF):
            t = i / (FRAMES_GIF - 1)
            # ease-in-out: arranca y para suave, como un dedo de verdad
            e = 0.5 - 0.5 * math.cos(math.pi * t)
            pag.evaluate(f"window.scrollTo(0, {int(recorrido * e)})")
            pag.wait_for_timeout(60)
            frames.append(Image.open(
                __import__("io").BytesIO(pag.screenshot(scale="css"))
            ).convert("RGB"))
        ctx.close()

        # --- escritorio: imagen de previsualizacion del enlace ---
        ctx2 = nav.new_context(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pag2 = ctx2.new_page()
        pag2.goto(url, wait_until="networkidle")
        pag2.wait_for_timeout(1000)
        pag2.screenshot(path=str(SALIDA / f"{slug}-og.png"))
        ctx2.close()

        nav.close()

    return slug, entera, frames


def marco_movil(captura: Path, destino: Path):
    """Mete la captura en un movil dibujado, sobre fondo claro. Solo la primera pantalla."""
    img = Image.open(captura).convert("RGB")
    # el ancho real manda: Chrome no siempre devuelve ancho*escala exacto
    alto_px = int(img.width * ALTO_MOVIL / ANCHO_MOVIL)
    pantalla = img.crop((0, 0, img.width, min(alto_px, img.height)))
    pantalla = pantalla.resize((720, int(720 * pantalla.height / pantalla.width)), Image.LANCZOS)

    borde, radio = 14, 54
    margen = 56
    w = pantalla.width + borde * 2
    h = pantalla.height + borde * 2
    lienzo = Image.new("RGB", (w + margen * 2, h + margen * 2), FONDO_MOCKUP)

    # sombra
    sombra = Image.new("L", lienzo.size, 0)
    ImageDraw.Draw(sombra).rounded_rectangle(
        (margen, margen + 10, margen + w, margen + h + 10), radius=radio, fill=90
    )
    sombra = sombra.filter(ImageFilter.GaussianBlur(22))
    lienzo.paste(Image.new("RGB", lienzo.size, (120, 112, 100)), (0, 0), sombra)

    # cuerpo del movil
    cuerpo = Image.new("RGB", (w, h), (24, 22, 20))
    mascara = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mascara).rounded_rectangle((0, 0, w - 1, h - 1), radius=radio, fill=255)
    lienzo.paste(cuerpo, (margen, margen), mascara)

    # pantalla, con sus esquinas redondeadas
    m2 = Image.new("L", pantalla.size, 0)
    ImageDraw.Draw(m2).rounded_rectangle(
        (0, 0, pantalla.width - 1, pantalla.height - 1), radius=radio - borde, fill=255
    )
    lienzo.paste(pantalla, (margen + borde, margen + borde), m2)

    lienzo.save(destino, quality=92)
    return destino


def hacer_gif(frames, destino: Path):
    escalados = []
    for f in frames:
        w = int(ALTO_GIF * f.width / f.height)
        escalados.append(f.resize((w, ALTO_GIF), Image.LANCZOS)
                          .convert("P", palette=Image.ADAPTIVE, colors=128))
    escalados[0].save(
        destino, save_all=True, append_images=escalados[1:],
        duration=90, loop=0, optimize=True,
    )
    return destino


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    html = Path(sys.argv[1])
    if not html.exists():
        sys.exit(f"No existe: {html}")
    slug = html.parent.name if html.stem == "index" else html.stem

    # La demo de demos/ todavia no tiene base.css dentro: sale sin estilos.
    # Se fotografia siempre la version montada.
    montada = RAIZ / "docs" / html.stem / "index.html"
    if html.parent.name == "demos" and montada.exists():
        html = montada
        print(f"(fotografiando la version montada: {montada.relative_to(RAIZ)})")
    elif html.parent.name == "demos":
        sys.exit(f"Falta {montada.relative_to(RAIZ)} — corre antes sistema/montar.py")

    slug, entera, frames = capturar(html, slug)
    mockup = marco_movil(entera, SALIDA / f"{slug}-mockup.png")
    gif = hacer_gif(frames, SALIDA / f"{slug}-scroll.gif")

    for f in sorted(SALIDA.glob(f"{slug}-*")):
        print(f"{f.name:28} {f.stat().st_size/1024:7.0f} KB")


if __name__ == "__main__":
    main()
