#!/usr/bin/env python3
"""enviar.py — monta out/enviar.html, el panel para mandar las demos.

    python3 sistema/enviar.py

Los .txt de out/ no son clicables. Esta pagina si, y **el que le da a enviar
es Nacho**, nunca el programa.

Hasta el 20/09/2026 este fichero se reescribia con trozos de codigo sueltos
metidos a mano en la terminal, y cada vez salia de un color. Ahora vive aqui.

21/09/2026 — Nacho: «solo hay 21 enlaces, no 30». Tenia razon y la culpa era
de aqui: la lista se sacaba de los `wa-*.txt`, o sea que un negocio sin movil
desaparecia de la pagina aunque su demo estuviera publicada. Ahora la lista
sale de `prospectos.json` (todo el que tenga `demo` aparece) y cada negocio
lleva la via que se puede usar con el:

  · movil  -> enlace de WhatsApp con el mensaje ya escrito
  · fijo   -> boton de llamar + el mensaje listo para copiar (a un fijo no se
              le manda un WhatsApp; se le llama o se le lleva impreso)
  · correo -> si hay `email-<slug>.txt`, tambien el enlace de Gmail

Dos colores a proposito: la tanda vieja en ciruela y la nueva en lima, para
distinguir de un vistazo lo que ya estaba de lo que se hizo esta noche.
"""
import html, json, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "out"

# La tanda 1 son las 9 demos que ya estaban hechas el 20/09/2026.
# Todo prospecto con demo que no este aqui es tanda 2.
TANDA_1 = [
    "autonorte-saez", "bar-de-palmero", "callejon-del-bernabeu",
    "imprime-y-mas-s-l", "jb-cerrajeros-madrid", "kali-barber-shop",
    "kmaspues", "pasteleria-acueducto", "podologia-milagros-chana-lopez",
]

# La tanda 2 son las 21 que estaban el 21/09/2026 por la manana. Se congela
# aqui a proposito: si se dejara como «todo lo que no es tanda 1», cada demo
# nueva caeria dentro de ella y la tanda 3 saldria siempre vacia.
TANDA_2 = [
    "asesoria-madrid-centro", "barberia-cholo-y-peluqueria-de-caballero",
    "bm1997-sl-copisteria", "cafeteria-el-espinar", "carniceria-nicar",
    "cesar-reparaciones", "clinica-dental-castellana", "colora-estetica",
    "fitness-feda-madrid", "flores-yohana-alonso-s-l",
    "kushala-centro-de-yoga-y-bienestar", "pablo-albalate",
    "persianas-redondo", "reparaciones-el-experto", "shyba-peluqueria-canina",
    "sigma", "slay", "superfruta-valencia", "talleres-j-l",
    "tintoreria-alvarez", "veterinario-madvetel",
]

# ciruela · lima oscurecida · naranja. El naranja es la tanda del 21/09/2026 de
# noche, y esa lleva una regla que las otras dos no tenian: **solo entra el
# negocio al que se le puede ESCRIBIR**, o sea movil con WhatsApp o correo
# publicado. A un fijo no se le manda un mensaje, y Nacho pidio esta tanda
# entera para escribir, no para llamar.
COLOR = {1: "#6d4b76", 2: "#4a7a12", 3: "#c2410c"}


def leer(nombre):
    f = OUT / nombre
    return f.read_text("utf-8").strip() if f.exists() else None


def fila(p, textos, solo_escribir=False):
    """Una linea de la lista. Devuelve (html, tiene_via).

    `solo_escribir` es para la tanda 3: ahi entra unicamente el negocio al que
    se le puede mandar un mensaje, asi que ofrecer «Llamar» sobraria. Es la
    diferencia entre una lista para trabajar de noche y una para trabajar a
    las once de la manana, que son dos tardes distintas.
    """
    slug, nom = p["slug"], p["nombre"]
    wa, correo = leer(f"wa-{slug}.txt"), leer(f"email-{slug}.txt")
    texto = leer(f"texto-{slug}.txt")
    tel = (p.get("telefono") or "").strip()

    vias, via = [], False
    if wa:
        n = re.search(r"wa\.me/(\d+)", wa)
        vias.append(f'<a class="wa" href="{html.escape(wa, quote=True)}">WhatsApp</a>'
                    f'<span class="tel">{n.group(1) if n else tel}</span>')
        via = True
    elif tel and not solo_escribir:
        # Fijo: no hay WhatsApp que abrir. Se llama, y el mensaje se copia
        # para leerlo por telefono o mandarlo por correo.
        vias.append(f'<a class="tel-a" href="tel:+34{tel}">Llamar {tel}</a>')
        via = True
        if texto:
            textos[slug] = texto
            vias.append(f'<button type="button" data-slug="{slug}">Copiar mensaje</button>')
    if correo:
        vias.append(f'<a class="mail" href="{html.escape(correo, quote=True)}">Correo</a>')
        via = True

    if not vias:
        vias.append('<span class="sin">sin via de contacto</span>')

    demo = p.get("demo")
    ver = f'<a class="ver" href="{html.escape(demo, quote=True)}">ver demo</a>' if demo else ""
    marca = ' <b class="env">· enviado</b>' if p.get("enviado") else ""

    return (f'<li><span class="n">{html.escape(nom)}</span>{marca}{ver}'
            f'<span class="vias">{" ".join(vias)}</span></li>'), via


def main():
    datos = json.loads((RAIZ / "prospectos.json").read_text("utf-8"))
    con_demo = [p for p in datos if p.get("demo")]

    publicadas = {d.stem for d in (RAIZ / "demos").glob("*.html")}
    huerfanas = sorted(publicadas - {p["slug"] for p in con_demo})

    tandas = {1: [p for p in con_demo if p["slug"] in TANDA_1],
              2: [p for p in con_demo if p["slug"] in TANDA_2],
              3: [p for p in con_demo
                  if p["slug"] not in TANDA_1 and p["slug"] not in TANDA_2]}

    textos, bloques, sin_via = {}, [], []
    for n, titulo in ((1, "Las de antes"), (2, "Segunda tanda"),
                      (3, "Tanda del 21/09 · solo para escribir")):
        if not tandas[n]:
            continue
        filas = []
        for p in tandas[n]:
            f, via = fila(p, textos, solo_escribir=(n == 3))
            filas.append(f)
            if not via:
                sin_via.append(p["slug"])
        bloques.append(f'<h2 class="t{n}">{titulo} · {len(tandas[n])}</h2>'
                       f'<ul class="t{n}">{"".join(filas)}</ul>')

    js_textos = json.dumps(textos, ensure_ascii=False).replace("</", "<\\/")

    html_doc = f"""<!doctype html><meta charset="utf-8"><title>Enviar demos</title>
<style>
body{{font:17px/1.7 system-ui;margin:3rem auto;max-width:42rem;padding:0 1rem}}
h1{{font-size:1.5rem;margin-bottom:.2rem}}
h2{{font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;
   margin:2.4rem 0 .4rem;padding-bottom:.3rem;border-bottom:2px solid}}
ul{{margin:0;padding:0;list-style:none}}
li{{margin:.9rem 0;padding-bottom:.9rem;border-bottom:1px solid #eee}}
.n{{font-weight:600}}
.vias{{display:block;font-size:.9rem;margin-top:.15rem}}
.vias a,.vias button{{margin-right:.9rem}}
.vias button{{font:inherit;font-size:.9rem;border:1px solid #bbb;background:#fafafa;
   border-radius:.3rem;padding:.05rem .5rem;cursor:pointer}}
.tel{{color:#888;font-size:.8rem;font-variant-numeric:tabular-nums}}
.ver{{color:#888;font-size:.8rem;margin-left:.6rem;text-decoration:none}}
.ver:hover{{text-decoration:underline}}
.sin{{color:#b23}}
.env{{color:#1f7a4c;font-size:.8rem}}
h2.t1,ul.t1 .vias a{{color:{COLOR[1]}}}
h2.t2,ul.t2 .vias a{{color:{COLOR[2]}}}
h2.t3,ul.t3 .vias a{{color:{COLOR[3]}}}
ul.t3 .vias a{{font-weight:600}}
.aviso{{color:#666;font-size:.92rem}}
.pie{{color:#999;font-size:.82rem;margin-top:2.5rem}}
textarea{{position:fixed;left:-9999px;top:0}}
</style>
<h1>Mandar las demos · {len(con_demo)}</h1>
<p class="aviso">Con móvil, el enlace abre el chat con el mensaje ya escrito.
Con fijo no hay WhatsApp: se llama, y «copiar mensaje» te deja el texto en el
portapapeles. <b>Tú le das a enviar.</b> Los colores separan las de antes
(<span style="color:{COLOR[1]}">ciruela</span>) de la tanda nueva
(<span style="color:{COLOR[2]}">lima</span>) y la del 21/09 por la noche
(<span style="color:{COLOR[3]}">naranja</span>), que son las diez elegidas
porque a todas se les puede <b>escribir</b>: WhatsApp o correo, sin llamar.</p>
{''.join(bloques)}
<p class="pie">Generado por <code>sistema/enviar.py</code> desde
<code>prospectos.json</code>. Cuando mandes una, pon <code>"enviado"</code> en
su ficha y vuelve a correrlo.</p>
<textarea id="buz" readonly></textarea>
<script>
var T = {js_textos};
var buz = document.getElementById('buz');
document.addEventListener('click', function(e){{
  var b = e.target.closest('button[data-slug]');
  if (!b) return;
  buz.value = T[b.dataset.slug] || '';
  buz.select();
  var ok = false;
  try {{ ok = document.execCommand('copy'); }} catch (err) {{ ok = false; }}
  if (!ok && navigator.clipboard) {{
    navigator.clipboard.writeText(buz.value).then(function(){{ b.textContent = 'Copiado'; }});
    return;
  }}
  b.textContent = ok ? 'Copiado' : 'No se pudo copiar';
  setTimeout(function(){{ b.textContent = 'Copiar mensaje'; }}, 2000);
}});
</script>
"""
    (OUT / "enviar.html").write_text(html_doc, "utf-8")
    print(f"out/enviar.html  ·  {len(con_demo)} demos  ·  "
          f"tanda 1: {len(tandas[1])}  ·  tanda 2: {len(tandas[2])}  ·  "
          f"mensajes para copiar: {len(textos)}")
    if sin_via:
        print("  sin via de contacto:", ", ".join(sin_via), file=sys.stderr)
    if huerfanas:
        print("  demos/ sin ficha en prospectos.json:", ", ".join(huerfanas), file=sys.stderr)


if __name__ == "__main__":
    main()
