#!/usr/bin/env python3
"""og.py - genera la tarjeta que se ve al mandar la demo por WhatsApp.

    python3 sistema/og.py demos/callejon-del-bernabeu.html

Sin esto el enlace llega pelado: una linea azul de texto. Con esto llega una
tarjeta con el nombre del negocio, su calle y los colores de su propia pagina.
Es lo primero que ve el dueno, antes de decidir si pincha.

No usa fotos: tipografia y color, igual que las demos. La tarjeta se saca de
los tokens de la propia demo, asi que cada una sale distinta sin tocar nada.
"""
import re, sys, pathlib, subprocess, tempfile

def token(css, n, x=""):
    m = re.search(rf"--{n}\s*:\s*([^;]+)", css)
    return m.group(1).strip() if m else x

def tarjeta(destino):
    h = pathlib.Path(destino).read_text("utf-8")
    slug = pathlib.Path(destino).stem
    t = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
    nombre, _, calle = t.partition("·")
    fuentes = re.search(r'href="(https://fonts\.googleapis\.com/css2[^"]+)"', h)
    return slug, f"""<!doctype html><meta charset="utf-8">
{'<link rel="stylesheet" href="%s">' % fuentes.group(1) if fuentes else ''}
<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;display:flex;flex-direction:column;
 justify-content:center;padding:84px 96px;background:{token(h,'fondo') or token(h,'papel','#f5f1e8')};
 color:{token(h,'tinta','#14100c')};font-family:{token(h,'texto','system-ui')};}}
.ceja{{font:500 26px/1 var(--t);letter-spacing:.16em;text-transform:uppercase;
 color:{token(h,'brasa') or token(h,'acento','#8a3b1e')};margin-bottom:34px}}
h1{{font-family:{token(h,'display','Georgia,serif')};font-weight:400;
 font-size:{86 if len(nombre.strip())<26 else 68}px;line-height:1.02;
 letter-spacing:-.02em;margin-bottom:26px}}
p{{font-size:32px;color:{token(h,'tinta-2','#5a5048')};line-height:1.35}}
.raya{{width:132px;height:7px;margin-top:46px;border-radius:99px;
 background:{token(h,'acento','#8a3b1e')}}}
</style>
<div class="ceja">Propuesta de página web</div>
<h1>{nombre.strip()}</h1>
<p>{calle.strip() or 'Madrid'}</p>
<div class="raya"></div>"""

def main(destino):
    slug, html = tarjeta(destino)
    salida = pathlib.Path("docs") / slug / "og.png"
    salida.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                     encoding="utf-8") as f:
        f.write(html); tmp = f.name
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.goto("file://" + tmp); pg.wait_for_timeout(900)
        pg.screenshot(path=str(salida)); b.close()
    print(f"{salida}  ({salida.stat().st_size/1024:.0f} KB)")

if __name__ == "__main__":
    for d in sys.argv[1:] or sys.exit("uso: og.py demos/<slug>.html"):
        main(d)
