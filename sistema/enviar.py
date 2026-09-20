#!/usr/bin/env python3
"""enviar.py — monta out/enviar.html, la lista de enlaces de WhatsApp.

    python3 sistema/enviar.py

Los .txt de out/ no son clicables. Esta pagina si: cada enlace abre el chat con
el mensaje ya escrito, y **el que le da a enviar es Nacho**, nunca el programa.

Hasta el 20/09/2026 este fichero se reescribia con trozos de codigo sueltos
metidos a mano en la terminal, y cada vez salia de un color. Ahora vive aqui.

Dos colores a proposito: la primera tanda (las 8 demos de antes) en ciruela y
la segunda (las 10 nuevas) en lima, para distinguirlas de un vistazo y saber
cuales quedan por mandar.
"""
import json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "out"

# La tanda 1 son las demos que ya estaban en la lista el 20/09/2026.
# Todo lo que aparezca en out/ y no este aqui es tanda 2.
TANDA_1 = [
    "autonorte-saez", "bar-de-palmero", "callejon-del-bernabeu",
    "imprime-y-mas-s-l", "jb-cerrajeros-madrid", "kali-barber-shop",
    "pasteleria-acueducto", "podologia-milagros-chana-lopez",
]

COLOR = {1: "#6d4b76", 2: "#4a7a12"}   # ciruela · lima oscurecida para que lea

def nombres():
    d = json.loads((RAIZ / "prospectos.json").read_text("utf-8"))
    return {p["slug"]: (p["nombre"], p.get("enviado")) for p in d}

def fila(slug, nom, enviado):
    url = (OUT / f"wa-{slug}.txt").read_text("utf-8").strip()
    tel = re.search(r"wa\.me/(\d+)", url)
    marca = ' <b style="color:#1f7a4c">· enviado</b>' if enviado else ""
    return (f'<li><a href="{url}">{nom}</a>'
            f'<span class="tel">{tel.group(1) if tel else ""}</span>{marca}</li>')

def main():
    info = nombres()
    hay = sorted(p.stem[3:] for p in OUT.glob("wa-*.txt"))
    tandas = {1: [s for s in TANDA_1 if s in hay],
              2: [s for s in hay if s not in TANDA_1]}
    faltan = [s for s in TANDA_1 if s not in hay]

    bloques = []
    for n, titulo in ((1, "Primera tanda"), (2, "Tanda nueva")):
        if not tandas[n]:
            continue
        filas = "".join(fila(s, info.get(s, (s, None))[0], info.get(s, (s, None))[1])
                        for s in tandas[n])
        bloques.append(f'<h2 class="t{n}">{titulo} · {len(tandas[n])}</h2>'
                       f'<ul class="t{n}">{filas}</ul>')

    html = f"""<!doctype html><meta charset="utf-8"><title>Enviar demos</title>
<style>
body{{font:17px/1.7 system-ui;margin:3rem auto;max-width:36rem;padding:0 1rem}}
h1{{font-size:1.5rem;margin-bottom:.2rem}}
h2{{font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;
   margin:2.2rem 0 .4rem;padding-bottom:.3rem;border-bottom:2px solid}}
ul{{margin:0;padding-left:1.2rem}}
li{{margin:.6rem 0}}
.tel{{color:#888;font-size:.8rem;margin-left:.5rem;font-variant-numeric:tabular-nums}}
h2.t1,ul.t1 a{{color:{COLOR[1]}}}
h2.t2,ul.t2 a{{color:{COLOR[2]}}}
.aviso{{color:#666;font-size:.92rem}}
</style>
<h1>Abrir el WhatsApp de cada demo</h1>
<p class="aviso">Pincha y se abre el chat con el mensaje ya escrito.
<b>Tú le das a enviar.</b> Los colores separan la primera tanda
(<span style="color:{COLOR[1]}">ciruela</span>) de la nueva
(<span style="color:{COLOR[2]}">lima</span>).</p>
{''.join(bloques)}
"""
    (OUT / "enviar.html").write_text(html, "utf-8")
    print(f"out/enviar.html  ·  tanda 1: {len(tandas[1])}  ·  tanda 2: {len(tandas[2])}")
    if faltan:
        print("  sin wa-*.txt:", ", ".join(faltan), file=sys.stderr)

if __name__ == "__main__":
    main()
