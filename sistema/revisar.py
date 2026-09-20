#!/usr/bin/env python3
"""revisar.py — audita una demo contra lo que hacen las webs buenas.

    python3 sistema/revisar.py demos/pasteleria-acueducto.html

Las reglas salen de comparar 19 webs premiadas con 66 webs corrientes
(plantillas/patrones.md). FALLO = no se envia. AVISO = miralo.
"""
import re, sys, json, pathlib

GENERICAS = ["poppins","roboto","open sans","montserrat","lato","inter",
             "nunito","raleway","quicksand","jost","mulish","dm sans"]
TOPICOS = ["bienvenid", "los mejores", "la mejor calidad", "de confianza",
           "calidad y servicio", "desde siempre para ti", "tu pasteleria de confianza",
           "pasion por", "nuestra pasion", "somos un equipo de profesionales"]

def audita(p):
    h = pathlib.Path(p).read_text("utf-8"); l = h.lower()
    F, A, OK = [], [], []
    def chk(cond, ok, fallo, dur=True):
        (OK.append(ok) if cond else (F if dur else A).append(fallo))

    # --- las 5 piezas obligatorias del README ---
    chk("demobar" in l or "no es su web oficial" in l, "barra de demo",
        "FALTA la barra amarilla 'Demo, no es su web oficial'")
    chk("ver qué es de ejemplo" in l or "ver que es de ejemplo" in l,
        "boton de ejemplo", "FALTA el boton 'Ver que es de ejemplo'")
    chk(re.search(r"aviso legal|no es la web oficial|propuesta", l) is not None,
        "pie legal", "FALTA el pie legal")

    # --- el tell numero 1: columna estrecha centrada ---
    cuerpo = l.split("<body", 1)[-1]
    anchos = [int(x) for x in re.findall(r"--ancho\s*:\s*(\d+)px", l)] or \
             [int(x) for x in re.findall(r"max-width\s*:\s*(\d+)px", l)]
    principal = max(anchos) if anchos else 0
    chk(principal >= 1100, f"contenedor {principal}px",
        f"El contenedor mas ancho es {principal}px. Debajo de 1100 la pagina "
        "parece un documento, no una web. (base.css: --ancho)")

    # --- a sangre: ninguna web buena mete todo en una caja ---
    chk("u-sangrado" in l or "100vw" in l or "u-hero" in l, "hay seccion a sangre",
        "Ninguna seccion va de borde a borde. Las 19 webs buenas tienen al menos una.")

    # --- tipografia ---
    fams = " ".join(re.findall(r"font-family\s*:\s*([^;\}]+)", l)) + \
           " ".join(re.findall(r"family=([A-Za-z+0-9:,;@.]+)", l)).replace("+"," ").lower()
    usadas = sorted({g for g in GENERICAS if g in fams})
    chk(not usadas, "tipografia con caracter",
        f"Tipografia generica: {', '.join(usadas)}. Es la fuente por defecto de las "
        "plantillas — ninguna de las 19 webs buenas la usa.")

    # --- escala: titular grande de verdad ---
    grande = re.search(r"clamp\(\s*([2-9](?:\.\d+)?)rem", l) or re.search(r"font-size:\s*([4-9]\d|\d{3})px", l)
    chk(bool(grande), "titular grande",
        "No hay ningun titular por encima de ~2rem. Las webs buenas gritan una vez.")

    # --- titular con voz ---
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", h, re.S | re.I)
    t1 = re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", h1[0])).strip() if h1 else ""
    chk(bool(t1), f"h1: {t1[:60]!r}", "No hay <h1>.")
    mal = [t for t in TOPICOS if t in t1.lower()]
    chk(not mal, "titular sin topicos",
        f"El titular usa un topico ({mal}). Un titular bueno dice algo que solo "
        "puede decir ESTE negocio.", dur=False)
    chk(not re.search(r"[\U0001F300-\U0001FAFF]", " ".join(h1)), "sin emoji en titulares",
        "Hay emoji en un titular. Es el tell mas rapido de 'lo hizo una IA'.", dur=False)

    # --- contacto: el hueco del 79% ---
    cab = cuerpo[:len(cuerpo)//4]
    chk("tel:" in cab, "telefono arriba",
        "El telefono no esta en la primera cuarta parte del HTML. Solo el 21% de "
        "las webs normales lo hace: es diferenciacion gratis.")
    chk("u-movil" in l or re.search(r"position:fixed[^}]*bottom:0", l.replace(" ","")),
        "barra fija de movil", "No hay barra fija de movil (Llamar / Como llegar).", dur=False)
    chk(re.search(r"(lunes|l\s*-\s*v|lun\b)[\s\S]{0,60}?\d{1,2}[:.]\d{2}", l) is not None,
        "horario escrito", "El horario no aparece escrito dia a dia.")
    chk("google.com/maps" in l or "openstreetmap" in l, "enlace a mapa",
        "No hay enlace a Maps.", dur=False)

    # --- el argumento de venta: JSON-LD ---
    ld = "localbusiness" in l.replace(" ", "") or "bakery" in l and "@context" in l
    chk("@context" in l and "schema.org" in l, "JSON-LD",
        "FALTA el JSON-LD. Solo el 6% de las webs del barrio lo tiene y el 36% de "
        "las premiadas: es media hora de trabajo y un argumento de venta.")
    chk("openinghours" in l.replace(" ", "").lower(), "horario en JSON-LD",
        "El JSON-LD no declara openingHours.", dur=False)

    # --- pecados del sector ---
    chk(not re.search(r'href="[^"]+\.pdf"', l), "sin carta en PDF",
        "Hay un PDF enlazado. La carta en PDF es el pecado numero uno del sector.")
    chk("unsplash" not in l and "pexels" not in l, "sin banco de imagenes",
        "Hay fotos de banco de imagenes. Se huelen.", dur=False)

    # --- variedad de maquetacion ---
    rejillas = len({m for m in re.findall(r"u-(2|3|4|partida|desigual|desigual-inv)\b", l)})
    chk(rejillas >= 3 or l.count("grid-template-columns") >= 4, f"{rejillas} maquetaciones",
        "Todas las secciones se maquetan igual. Alterna: partida, desigual, rejilla.", dur=False)

    # --- peso ---
    kb = len(h.encode()) / 1024
    chk(kb < 120, f"{kb:.0f} KB", f"Pesa {kb:.0f} KB. El argumento es que carga al instante.", dur=False)
    return F, A, OK

if __name__ == "__main__":
    salida = 0
    for p in [a for a in sys.argv[1:] if not a.startswith("-")]:
        F, A, OK = audita(p)
        print(f"\n\033[1m{p}\033[0m  ·  {len(OK)} bien, {len(A)} avisos, {len(F)} fallos")
        for x in F: print("  \033[31m✗\033[0m", x)
        for x in A: print("  \033[33m!\033[0m", x)
        if "-v" in sys.argv:
            for x in OK: print("  \033[32m✓\033[0m", x)
        salida |= bool(F)
    sys.exit(salida)
