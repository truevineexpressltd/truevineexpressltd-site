"""Build the Truevine Express static site into ../site."""
import os, re, json, shutil, datetime
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg
from PIL import Image

import lib, home, services, pages

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site")
IMG = os.path.join(OUT, "assets", "img")
FONTS = os.path.join(HERE, "static", "assets", "fonts")
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
shutil.copytree(os.path.join(HERE, "static"), OUT)
os.makedirs(IMG, exist_ok=True)

NAVY, GOLD, GOLD_WM, GOLD_LT = "#00488D", "#AF8A2C", "#D9B253", "#F8CD6D"
TREE = open(os.path.join(HERE, "tree.svg")).read()
TREE_VB = re.search(r'viewBox="([^"]+)"', TREE).group(1)
TREE_D = re.search(r' d="([^"]+)"', TREE).group(1)
TW, TH = map(float, TREE_VB.split()[2:])


def text_path(text, font_file, size, tracking=0.0):
    """Return (svg path d, width) for text set in a font, baseline at y=0."""
    f = TTFont(os.path.join(FONTS, font_file))
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    upm = f["head"].unitsPerEm
    sc = size / upm
    x = 0.0
    ds = []
    for ch in text:
        g = cmap.get(ord(ch))
        if g is None:
            continue
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x, 0)))
        ds.append(pen.getCommands())
        x += gs[g].width * sc + tracking * size
    return " ".join(ds), x - tracking * size


def write(rel, content):
    p = os.path.join(OUT, rel.lstrip("/"))
    if p.endswith("/"):
        p = os.path.join(p, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(content)
    return p


def tree_svg(color):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{TREE_VB}"><path fill="{color}" fill-rule="evenodd" d="{TREE_D}"/></svg>'


def logo_full_svg(tree_color=NAVY, word_color=GOLD_WM, ltd_color=NAVY):
    d1, w1 = text_path("TRUEVINE EXPRESS", "cinzel-latin-500-normal.ttf" if False else "cinzel-latin-500-normal.woff2", 40, 0.02)
    d2, w2 = text_path("LTD", "cinzel-latin-500-normal.woff2", 20, 0.12)
    W = max(w1, TW * 3.1) + 20
    tw = TW * 3.1
    tx = (W - tw) / 2
    y1 = TH * 3.1 + 66
    y2 = y1 + 40
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {y2 + 8:.0f}">'
            f'<g transform="translate({tx:.1f},0) scale(3.1)"><path fill="{tree_color}" fill-rule="evenodd" d="{TREE_D}"/></g>'
            f'<g transform="translate({(W - w1) / 2:.1f},{y1:.1f})"><path fill="{word_color}" d="{d1}"/></g>'
            f'<g transform="translate({(W - w2) / 2:.1f},{y2:.1f})"><path fill="{ltd_color}" d="{d2}"/></g></svg>')


def favicon_svg():
    s = 0.78 * 64 / TW
    h = TH * s
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#05192F"/>'
            f'<g transform="translate({(64 - TW * s) / 2:.2f},{(64 - h) / 2:.2f}) scale({s:.4f})"><path fill="{GOLD_LT}" fill-rule="evenodd" d="{TREE_D}"/></g></svg>')


def og_svg():
    d1, w1 = text_path("TRUEVINE EXPRESS", "cinzel-latin-600-normal.woff2", 64, 0.03)
    d2, w2 = text_path("LIMITED", "cinzel-latin-500-normal.woff2", 22, 0.5)
    d3, w3 = text_path("IT  ·  Telecom  ·  Logistics Consulting", "poppins-latin-400-normal.woff2", 30, 0.01)
    d4, w4 = text_path("Ikeja, Lagos  ·  0703 590 9781  ·  truevineexpressltd.com", "poppins-latin-300-normal.woff2", 22, 0.01)
    s = 2.0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#031123"/><stop offset=".6" stop-color="#05192F"/><stop offset="1" stop-color="#0B3466"/></linearGradient></defs>
<rect width="1200" height="630" fill="url(#bg)"/>
<g transform="translate(1010,-80) rotate(45)">
<rect x="0" y="0" width="560" height="62" rx="31" fill="{GOLD_LT}"/>
<rect x="40" y="90" width="620" height="62" rx="31" fill="{GOLD}"/>
<rect x="-60" y="-90" width="520" height="62" rx="31" fill="#3D6EB1"/></g>
<g transform="translate(90,120) scale({s})"><path fill="{GOLD_LT}" fill-rule="evenodd" d="{TREE_D}"/></g>
<g transform="translate(90,410)"><path fill="#fff" d="{d1}"/></g>
<g transform="translate(92,452)"><path fill="{GOLD_WM}" d="{d2}"/></g>
<rect x="90" y="488" width="60" height="2" fill="{GOLD_WM}"/>
<g transform="translate(90,540)"><path fill="#fff" fill-opacity=".92" d="{d3}"/></g>
<g transform="translate(90,585)"><path fill="#A3BDD6" d="{d4}"/></g>
</svg>'''


def assets():
    open(os.path.join(IMG, "tree-navy.svg"), "w").write(tree_svg(NAVY))
    open(os.path.join(IMG, "tree-gold.svg"), "w").write(tree_svg(GOLD_LT))
    open(os.path.join(IMG, "logo-full.svg"), "w").write(logo_full_svg())
    fav = favicon_svg()
    open(os.path.join(OUT, "favicon.svg"), "w").write(fav)
    for name, size in (("favicon-32.png", 32), ("apple-touch-icon.png", 180), ("assets/img/icon-192.png", 192), ("assets/img/icon-512.png", 512)):
        cairosvg.svg2png(bytestring=fav.encode(), write_to=os.path.join(OUT, name), output_width=size, output_height=size)
    # favicon.ico
    Image.open(os.path.join(OUT, "assets/img/icon-192.png")).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    # logo PNG for schema
    cairosvg.svg2png(bytestring=logo_full_svg().encode(), write_to=os.path.join(IMG, "logo-512.png"), output_width=512, background_color="white")
    # OG image
    cairosvg.svg2png(bytestring=og_svg().encode(), write_to="/tmp/og.png", output_width=1200, output_height=630)
    Image.open("/tmp/og.png").convert("RGB").save(os.path.join(IMG, "og.jpg"), quality=88, optimize=True, progressive=True)


def meta_files(paths):
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{lib.SITE}{p}</loc><lastmod>{today}</lastmod><priority>{'1.0' if p == '/' else '0.8'}</priority></url>" for p in paths)
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("/robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {lib.SITE}/sitemap.xml\n")
    write("/site.webmanifest", json.dumps({
        "name": "Truevine Express Limited", "short_name": "Truevine", "start_url": "/", "display": "standalone",
        "background_color": "#05192F", "theme_color": "#05192F",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    write("/CNAME", "truevineexpressltd.com\n")
    write("/.nojekyll", "")


def main():
    assets()
    indexed = []
    write("/", home.build()); indexed.append("/")
    for slug in ("it", "telecom", "logistics", "systems"):
        p = services.PAGES[slug]["path"]
        write(p, services.build(slug)); indexed.append(p)
    write("/about/", pages.about()); indexed.append("/about/")
    write("/contact/", pages.contact()); indexed.append("/contact/")
    write("/privacy/", pages.privacy()); indexed.append("/privacy/")
    write("/thank-you/", pages.thanks())
    write("/404.html", pages.notfound())
    meta_files(indexed)
    print("built", indexed)


if __name__ == "__main__":
    main()
