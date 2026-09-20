#!/usr/bin/env python3
"""tiene_web.py — comprueba si un prospecto "sin web" tiene web de verdad.

    python3 sistema/tiene_web.py            # revisa los que ponen estado_web none

La Fioreria figuraba como "sin web" y tenia una tienda Shopify entera, con
carrito y seccion de novias. Mandarle una demo habria sido el ridiculo. Esto
prueba los dominios que saldrian de su propio nombre antes de gastar una demo.
"""
import json, re, ssl, sys, unicodedata, urllib.request, pathlib
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
ctx = ssl.create_default_context(); ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def limpia(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())

def dominios(nombre):
    base = limpia(nombre)
    corto = limpia(re.sub(r"\b(madrid|s\.?l\.?|sl)\b", "", nombre, flags=re.I))
    out = []
    for b in dict.fromkeys([base, corto]):
        if 4 <= len(b) <= 40:
            # http y www tambien: la web de la podologa solo salia por http
            # sin S, y probando solo https daba un falso "no tiene web".
            for d in (f"{b}.com", f"{b}.es"):
                out += [f"https://{d}", f"https://www.{d}",
                        f"http://{d}", f"http://www.{d}"]
    return out

def vivo(u):
    try:
        r = urllib.request.Request(u, headers={"User-Agent": UA})
        with urllib.request.urlopen(r, timeout=12, context=ctx) as f:
            if f.status != 200: return None
            h = f.read(400000).decode("utf-8", "ignore")
    except Exception:
        return None
    if len(h) < 3000: return None                      # dominio aparcado
    l = h.lower()
    if any(k in l for k in ("dominio en venta", "domain for sale",
                            "buy this domain", "godaddy.com/forsale")):
        return None
    t = re.findall(r"<title[^>]*>(.*?)</title>", h, re.S | re.I)
    return {
        "url": f.geturl(),
        "titulo": re.sub(r"\s+", " ", re.sub("<[^>]+>", "", t[0])).strip()[:70] if t else "",
        "tienda": bool(re.search(r"/products/|añadir al carrito|add to cart|woocommerce", l)),
    }

def main():
    p = pathlib.Path("prospectos.json")
    d = json.loads(p.read_text("utf-8"))
    ps = d if isinstance(d, list) else d["prospectos"]
    objetivo = [x for x in ps if (x.get("estado_web") or "none") == "none"
                and not x.get("web_actual")]
    print(f"Comprobando {len(objetivo)} prospectos marcados como «sin web»…\n")
    pares = [(x, u) for x in objetivo for u in dominios(x["nombre"])]
    with ThreadPoolExecutor(20) as ex:
        res = list(ex.map(lambda par: (par[0], vivo(par[1])), pares))
    hallado = {}
    for x, r in res:
        if r and x["slug"] not in hallado:
            hallado[x["slug"]] = (x, r)
    if not hallado:
        print("Ninguno tiene web. La lista esta limpia.")
        return
    for slug, (x, r) in sorted(hallado.items()):
        print(f"⚠ {slug}")
        print(f"   {r['url']}  {'· TIENDA ONLINE' if r['tienda'] else ''}")
        print(f"   «{r['titulo']}»\n")
    print(f"{len(hallado)} prospecto(s) SI tienen web: no mandarles una demo "
          f"sin mirarla antes.")

if __name__ == "__main__":
    main()
