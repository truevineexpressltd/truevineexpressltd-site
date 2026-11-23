"""Static QA for the built site: links, assets, SEO tags, structured data, accessibility basics.
Usage: python3 tests/check.py site"""
import sys, os, re, json
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = sys.argv[1] if len(sys.argv) > 1 else "site"
fails, titles, descs = [], {}, {}

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.anchors=[]; s._a=None; s.links=[]; s.imgs=[]; s.ids=set(); s.title=""; s._t=False; s.meta={}; s.ld=[]; s._ld=False; s.h1=0; s.lang=None; s.labels=set(); s.inputs=[]
    def handle_starttag(s, t, a):
        a=dict(a)
        if "id" in a: s.ids.add(a["id"])
        if t=="html": s.lang=a.get("lang")
        if t=="a" and "href" in a:
            s.links.append(a["href"]); s._a={"href":a["href"],"text":""}
        if t=="img" and s._a is not None: s._a["text"]+=a.get("alt","")
        if t=="link" and a.get("rel") in ("stylesheet","icon","apple-touch-icon","manifest","canonical"): s.links.append(a["href"])
        if t=="script" and "src" in a: s.links.append(a["src"])
        if t=="img": s.imgs.append(a); s.links.append(a.get("src",""))
        if t=="image" and "href" in a: s.links.append(a["href"])
        if t=="title": s._t=True
        if t=="meta": s.meta[a.get("name") or a.get("property")]=a.get("content")
        if t=="script" and a.get("type")=="application/ld+json": s._ld=True
        if t=="h1": s.h1+=1
        if t=="label" and "for" in a: s.labels.add(a["for"])
        if t in ("input","select","textarea") and a.get("type") not in ("hidden","checkbox") and "hp" not in (a.get("class") or ""): s.inputs.append(a.get("id"))
    def handle_endtag(s,t):
        if t=="a" and s._a is not None: s.anchors.append(s._a); s._a=None
        if t=="title": s._t=False
        if t=="script": s._ld=False
    def handle_data(s,d):
        if s._a is not None: s._a["text"]+=d
        if s._t: s.title+=d
        if s._ld: s.ld.append(d)

def resolve(page, href):
    u=urlparse(href)
    if u.scheme or href.startswith(("mailto:","tel:","#","//")): return None
    path=u.path
    if not path.startswith("/"): path=os.path.join(os.path.dirname(page.replace(ROOT,"",1)), path)
    f=ROOT+path
    if path.endswith("/"): f+="index.html"
    return f

pages=[os.path.join(d,f) for d,_,fs in os.walk(ROOT) for f in fs if f.endswith(".html")]
for pg in pages:
    p=P(); p.feed(open(pg,encoding="utf-8").read()); rel=pg.replace(ROOT,"")
    for h in p.links:
        f=resolve(pg,h)
        if f and not os.path.exists(f): fails.append(f"{rel}: broken link {h}")
    for i in p.imgs:
        if not (i.get("alt") or "").strip(): fails.append(f"{rel}: img without alt text {i.get('src')}")
    for a in p.anchors:
        if not a["text"].strip(): fails.append(f"{rel}: link without text {a['href']}")
    if p.h1!=1: fails.append(f"{rel}: {p.h1} h1 elements")
    if not p.lang: fails.append(f"{rel}: missing lang")
    t=p.title.strip(); d=p.meta.get("description","")
    if not (10<len(t)<=75): fails.append(f"{rel}: title length {len(t)}")
    if not (50<len(d)<=170): fails.append(f"{rel}: description length {len(d)}")
    if t in titles: fails.append(f"{rel}: duplicate title with {titles[t]}")
    titles[t]=rel
    for k in ("og:image","og:title","twitter:card"):
        if not p.meta.get(k): fails.append(f"{rel}: missing {k}")
    for block in p.ld:
        try: json.loads(block)
        except Exception as e: fails.append(f"{rel}: bad JSON-LD {e}")
    for iid in p.inputs:
        if iid and iid not in p.labels: fails.append(f"{rel}: input #{iid} has no label")

sm=open(os.path.join(ROOT,"sitemap.xml")).read()
for loc in re.findall(r"<loc>https://truevineexpressltd.com(.*?)</loc>",sm):
    f=ROOT+loc+("index.html" if loc.endswith("/") else "")
    if not os.path.exists(f): fails.append(f"sitemap: missing {loc}")
for need in ("CNAME","robots.txt","favicon.ico","404.html",".nojekyll"):
    if not os.path.exists(os.path.join(ROOT,need)): fails.append(f"missing {need}")
# brand facts must appear site-wide
home=open(os.path.join(ROOT,"index.html")).read()
for fact in ("0703&nbsp;590&nbsp;9781","+2347035909781","info@truevineexpressltd.com","ERP implementation","Warehouse management systems","Procurement software","Accion Microfinance Bank","RC 1848110","2021","92 Obafemi Awolowo Way"):
    if fact not in home: fails.append(f"home missing fact {fact}")
about=open(os.path.join(ROOT,"about","index.html")).read()
for fact in ("Bankole Adebayo","Attah Augustine Stephen","Temitope Benson","Francis Onyima","Eniola Dada",'id="leadership"'):
    if fact not in about: fails.append(f"about missing {fact}")
for pg in pages:
    txt=open(pg).read().replace("formsubmit.co/ajax/truevineexpressltd@gmail.com","").replace("formsubmit.co/truevineexpressltd@gmail.com","")
    if "truevineexpressltd@gmail.com" in txt: fails.append(f"{pg}: old Gmail address shown publicly")
for pg in pages:
    txt=open(pg).read()
    for banned in ("seven client","7 client","team of 20","20-person","20 specialists","(ERP, WMS)","Fields marked optional","Three practices","three belong together"):
        if banned in txt: fails.append(f"{pg}: contains '{banned}'")
home_txt=open(os.path.join(ROOT,"index.html")).read()
if home_txt.count('class="practice ')!=4: fails.append("home: expected 4 practice cards")
if "Team of 20" not in home_txt: fails.append("home: Team of 20 credential missing")
# Service ownership: software lives under Business Systems only
import html as _h
def section(txt, start, end):
    i=txt.find(start); return txt[i:txt.find(end,i)] if i>=0 else ""
cards={m.group(1):m.group(2) for m in re.finditer(r'<article class="practice[^"]*">.*?<h3>(.*?)</h3>.*?<ul>(.*?)</ul>', home_txt, re.S)}
if re.search(r"ERP|procurement software", cards.get("IT Consulting",""), re.I): fails.append("home IT card lists ERP/procurement software")
if re.search(r"warehouse management|WMS", cards.get("Logistics Consulting",""), re.I): fails.append("home Logistics card lists WMS")
for page, pat in (("it-consulting", r"ERP|procurement software"), ("logistics-consulting", r"warehouse management system|WMS")):
    t=open(os.path.join(ROOT,page,"index.html")).read()
    heads=" ".join(re.findall(r'<article class="svc[^"]*">.*?<h3>(.*?)</h3>.*?</ul>', t, re.S)+re.findall(r'<article class="svc[^"]*">.*?<ul>(.*?)</ul>', t, re.S))
    if re.search(pat, heads, re.I): fails.append(f"{page}: service cards overlap Business Systems ({pat})")
# Address always includes 2nd Floor in visible text
for pg in pages:
    t=_h.unescape(re.sub(r"<[^>]+>"," ",open(pg).read()))
    for m in re.finditer(r"92 Obafemi Awolowo Way(?!,?\s*2nd Floor)", t):
        fails.append(f"{pg}: address without 2nd Floor: ...{t[m.start():m.start()+60]!r}")
print(f"{len(pages)} pages checked")
print("\n".join(fails) if fails else "ALL CHECKS PASSED")
sys.exit(1 if fails else 0)
