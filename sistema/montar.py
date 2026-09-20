#!/usr/bin/env python3
"""montar.py — mete sistema/base.css dentro de la demo y la publica en docs/.

    python3 sistema/montar.py demos/pasteleria-acueducto.html

GitHub Pages solo sirve / o /docs, asi que la copia a mano se olvidaba.
Esto la hace siempre. La demo marca el hueco con:  /* @base */
"""
import sys, pathlib, re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BASE = (RAIZ / "sistema" / "base.css").read_text("utf-8")

for arg in sys.argv[1:]:
    src = pathlib.Path(arg)
    h = src.read_text("utf-8")
    if "/* @base */" not in h:
        sys.exit(f"{src}: falta el marcador /* @base */ dentro de <style>")
    out = h.replace("/* @base */", BASE)
    dst = RAIZ / "docs" / src.stem / "index.html"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, "utf-8")
    print(f"{src}  →  {dst.relative_to(RAIZ)}  ({len(out.encode())/1024:.0f} KB)")
