import re,json,sys,urllib.request,ssl,gzip,io
from concurrent.futures import ThreadPoolExecutor
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
SEC=["hero","menu","carta","reserva","reservar","horario","contacto","nosotros","sobre","galer","opinion","reseña","precio","tarifa","blog","faq","equipo","servicios","tienda","pedido","delivery","ubicaci"]
def get(u):
    try:
        r=urllib.request.Request(u,headers={"User-Agent":UA,"Accept-Language":"es-ES,es"})
        with urllib.request.urlopen(r,timeout=20,context=ctx) as f:
            b=f.read(900000)
            if f.headers.get("Content-Encoding")=="gzip": b=gzip.decompress(b)
            return f.status,f.geturl(),b.decode("utf-8","ignore")
    except Exception as e: return 0,u,str(e)[:80]
def an(u):
    st,fu,h=get(u)
    if st!=200 or len(h)<2000: return {"url":u,"ok":False,"err":h[:60] if st!=200 else "thin"}
    l=h.lower()
    heads=[re.sub(r"\s+"," ",re.sub("<[^>]+>","",m)).strip()[:60] for m in re.findall(r"<h[12][^>]*>(.*?)</h[12]>",h,re.S|re.I)]
    fonts=sorted(set(re.findall(r"fonts\.googleapis\.com/css2?\?family=([A-Za-z+0-9]+)",h)))
    ff=sorted(set(x.strip().strip("'\"") for x in re.findall(r"font-family\s*:\s*([^;\}\"]+)",h)[:40]))
    cols=[c.lower() for c in re.findall(r"#([0-9a-fA-F]{6})\b",h)]
    from collections import Counter
    top=[c for c,_ in Counter(cols).most_common(8)]
    return {"url":fu,"ok":True,"title":re.sub("<[^>]+>","",(re.findall(r"<title[^>]*>(.*?)</title>",h,re.S|re.I) or [""])[0]).strip()[:70],
     "h":heads[:12],"gfonts":fonts[:6],"ff":ff[:5],"colors":top,
     "tel_head": bool(re.search(r"tel:\+?\d",h[:len(h)//3])),
     "tel": bool(re.search(r"tel:\+?\d",h)), "wa":"wa.me" in l or "whatsapp" in l,
     "map":"google.com/maps" in l or "maps.googleapis" in l or "openstreetmap" in l,
     "booking": any(k in l for k in ["thefork","covermanager","opentable","resengo","reservas","booking","cal.com","calendly","glofox","mindbody"]),
     "delivery": any(k in l for k in ["glovo","ubereats","just-eat","justeat","deliveroo"]),
     "ig":"instagram.com" in l,"schema":'"@type":"restaurant"' in l.replace(" ","") or "localbusiness" in l.replace(" ","").lower(),
     "sticky": bool(re.search(r"position\s*:\s*(sticky|fixed)",l)),
     "video": "<video" in l, "price_eur": len(re.findall(r"\d+[,\.]\d{2}\s*&nbsp;?\s*€|€\s*\d+|\d+\s*€",h)),
     "secs":[s for s in SEC if s in l], "words": len(re.sub("<[^>]+>"," ",h).split()),
     "framework": next((f for f in ["wp-content","shopify","wix","squarespace","webflow","_next","framer","elementor","bootstrap","tailwind"] if f in l),"?")}
urls=[x.strip() for x in open(sys.argv[1]) if x.strip()]
with ThreadPoolExecutor(16) as ex: res=list(ex.map(an,urls))
json.dump(res,open(sys.argv[2],"w"),ensure_ascii=False,indent=1)
ok=[r for r in res if r["ok"]]
print("OK",len(ok),"de",len(res))
for r in res:
    if not r["ok"]: print("  x",r["url"],r["err"])
