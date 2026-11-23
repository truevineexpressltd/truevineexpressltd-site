"""Shared layout, icons and helpers for the Truevine Express static site."""
import json, html as _html

SITE = "https://truevineexpressltd.com"
PHONE_DISPLAY = "0703&nbsp;590&nbsp;9781"
PHONE_TEL = "+2347035909781"
EMAIL = "info@truevineexpressltd.com"
# The contact form delivers through FormSubmit to the Gmail inbox it was activated for.
FORM_TO = "truevineexpressltd@gmail.com"
ADDRESS_LINES = ["92 Obafemi Awolowo Way, 2nd Floor", "Ikeja, Lagos, Nigeria"]
RC = "RC 1848110"
FOUNDED = "2021"
FORM_AJAX = "https://formsubmit.co/ajax/" + FORM_TO
FORM_POST = "https://formsubmit.co/" + FORM_TO
ASSET_V = "6"

# Unsplash imagery (free licence). key: (cdn id, photographer, photo page)
IMAGES = {
    "lagos": ("photo-1618828665011-0abd973f7bb8", "Nupo Deyon Daniel", "https://unsplash.com/photos/67ruAEYmp4c"),
    "lagos_night": ("photo-1648023200201-8fcede127835", "Opeyemi Adisa", "https://unsplash.com/photos/Ww2j734hEcA"),
    "it": ("photo-1558494949-ef010cbdcc31", "Taylor Vick", "https://unsplash.com/photos/M5tzZtFCOfs"),
    "servers": ("photo-1584169417032-d34e8d805e8b", "İsmail Enes Ayhan", "https://unsplash.com/photos/lVZjvw-u9V8"),
    "telecom": ("photo-1533664488202-6af66d26c44a", "Mario Caruso", "https://unsplash.com/photos/0C9VmZUqcT8"),
    "fibre": ("photo-1594915440248-1e419eba6611", "Kirill Sh", "https://unsplash.com/photos/eVWWr6nmDf8"),
    "port": ("photo-1494412519320-aa613dfb7738", "CHUTTERSNAP", "https://unsplash.com/photos/9cCeS9Sg6nU"),
    "warehouse": ("photo-1586528116311-ad8dd3c8310d", "Adrian Sulyok", "https://unsplash.com/photos/sczNLg6rrhQ"),
    "team": ("photo-1573164574572-cb89e39749b4", "Christina @ wocintechchat.com", "https://unsplash.com/photos/faEfWCdOKIg"),
}


LEADERS = [
    ("Bankole Adebayo", "Chief Executive Officer",
     "Mr. Adebayo leads our strategy, business development and client relationships, keeping the company focused on services that meet our clients' needs."),
    ("Attah Augustine Stephen", "Chief Operating Officer",
     "Mr. Stephen leads service delivery, quality and vendor partnerships, ensuring projects run smoothly and our solutions work well in clients' day-to-day operations. He oversees the team delivering our ERP implementation, warehouse management, procurement software and logistics consulting work."),
    ("Temitope Benson", "Chief Financial Officer",
     "Mrs. Benson oversees financial planning, budgets and financial controls, helping us manage project costs and meet our commitments to clients."),
    ("Francis Onyima", "Head of Technology",
     "Mr. Onyima leads solution design, systems integration and technical quality, helping clients adopt technology that fits their operations and supports their growth."),
    ("Eniola Dada", "HR Director",
     "Ms. Dada oversees recruitment, staff development and daily administration, ensuring our teams have the support and resources to do their work well."),
]

CLIENTS = ["Khome Global Logistics", "Accion Microfinance Bank", "Errand360", "ColdHubs", "RapidBTS Limited", "Kennie-O Cold Chain"]


def clients_strip(title="Organisations we have supported", dark=False):
    names = "".join(f'<li>{n}</li>' for n in CLIENTS)
    return f'''<section class="clients{' clients--dark on-dark' if dark else ''}" aria-label="{title}">
  <div class="wrap">
    <p class="clients-label reveal">{title}</p>
    <ul class="clients-list reveal reveal-d1">{names}</ul>
  </div>
</section>'''


def img_url(key, w, h=None, q=72):
    cid = IMAGES[key][0]
    u = f"https://images.unsplash.com/{cid}?auto=format&fit=crop&w={w}&q={q}"
    if h:
        u += f"&h={h}"
    return u


def img(key, alt, widths=(640, 960, 1280, 1920), sizes="100vw", ratio=None, cls="", eager=False):
    """Responsive Unsplash image. ratio=(w,h) crops to an aspect ratio."""
    def u(w):
        h = round(w * ratio[1] / ratio[0]) if ratio else None
        return img_url(key, w, h)
    srcset = ", ".join(f"{u(w)} {w}w" for w in widths)
    mid = widths[len(widths) // 2]
    wh = f' width="{mid}" height="{round(mid * ratio[1] / ratio[0]) if ratio else round(mid * 0.66)}"'
    load = ' loading="eager" fetchpriority="high"' if eager else ' loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    srcset = srcset.replace("&", "&amp;")
    return f'<img src="{u(mid).replace("&", "&amp;")}" srcset="{srcset}" sizes="{sizes}" alt="{alt}"{wh}{load} decoding="async"{c}>'


# Line icons (24x24, stroke currentColor)
_I = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.5 2.5L16 9.5"/>',
    "it": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><path d="m9 9 2 2-2 2M13 13h3"/>',
    "telecom": '<path d="M12 10v11M8.5 21 12 10l3.5 11M9.6 17h4.8"/><circle cx="12" cy="8" r="2"/><path d="M7.8 4.8a6 6 0 0 0 0 6.4M16.2 4.8a6 6 0 0 1 0 6.4M5 2.5a10 10 0 0 0 0 11M19 2.5a10 10 0 0 1 0 11"/>',
    "logistics": '<path d="M2 7h11v9H2zM13 10h4l3 3v3h-7z"/><circle cx="6" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "building": '<path d="M4 21V5l8-3v19M12 8l8 3v10M3 21h18"/><path d="M7 8h2M7 12h2M7 16h2M15 13h2M15 17h2"/>',
    "landmark": '<path d="M3 21h18M4 18h16M5 18V10M9 18v-8M15 18v-8M19 18v-8M2.5 9.5 12 3l9.5 6.5z"/>',
    "tower": '<path d="M12 7v14M8 21l4-14 4 14M9.2 16.5h5.6"/><circle cx="12" cy="5" r="1.5"/><path d="M8.5 2.8a5 5 0 0 0 0 4.4M15.5 2.8a5 5 0 0 1 0 4.4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6z"/><path d="m9 12 2 2 4-4"/>',
    "cloud": '<path d="M7 18a4.5 4.5 0 0 1-.6-9 6 6 0 0 1 11.4 1.6A3.8 3.8 0 0 1 17.5 18z"/>',
    "network": '<rect x="9" y="2.5" width="6" height="5" rx="1"/><rect x="2.5" y="16.5" width="6" height="5" rx="1"/><rect x="15.5" y="16.5" width="6" height="5" rx="1"/><path d="M12 7.5V12M5.5 16.5V12h13v4.5"/>',
    "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/><path d="M19 20a3 3 0 0 1-3 2h-3"/>',
    "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
    "box": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="m3 7.5 9 4.5 9-4.5M12 12v9"/>',
    "route": '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H16a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h7.5"/>',
    "doc": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
    "satellite": '<path d="M4 15a5 5 0 0 0 5 5"/><path d="M4 11a9 9 0 0 1 9 9"/><circle cx="5" cy="19" r="1"/><path d="m13 11 3-3M14 4l6 6-3 3-6-6z"/>',
    "plug": '<path d="M9 2v6M15 2v6M6 8h12v3a6 6 0 0 1-12 0zM12 17v5"/>',
    "receipt": '<path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "erp": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/><path d="M10 6.5h4M6.5 10v4M17.5 10v4M10 17.5h4"/>',
    "cart": '<path d="M3 4h2l2.4 11h11l2-8H6.3"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/><path d="m10.5 10.5 2 2 3.5-3.5"/>',
    "sync": '<path d="M4 12a8 8 0 0 1 13.7-5.7L20 8.6M20 4v4.6h-4.6"/><path d="M20 12a8 8 0 0 1-13.7 5.7L4 15.4M4 20v-4.6h4.6"/>',
    "graduation": '<path d="M2 9.5 12 5l10 4.5-10 4.5z"/><path d="M6 11.5V16c0 1.4 2.7 3 6 3s6-1.6 6-3v-4.5M22 9.5v5"/>',
    "erp": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/><path d="M10 6.5h4M6.5 10v4M17.5 10v4M10 17.5h4"/>',
    "cart": '<path d="M3 4h2l2.4 11h11l2-8H6.3"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/><path d="m10.5 10.5 2 2 3.5-3.5"/>',
    "sync": '<path d="M4 12a8 8 0 0 1 13.7-5.7L20 8.6M20 4v4.6h-4.6"/><path d="M20 12a8 8 0 0 1-13.7 5.7L4 15.4M4 20v-4.6h4.6"/>',
    "graduation": '<path d="M2 9.5 12 5l10 4.5-10 4.5z"/><path d="M6 11.5V16c0 1.4 2.7 3 6 3s6-1.6 6-3v-4.5M22 9.5v5"/>',
    "warehouse": '<path d="M2 21V8l10-5 10 5v13"/><path d="M6 21v-9h12v9M6 15h12M6 18h12"/>',
}


def icon(name, sw="1.5"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>')


DIAMONDS = ('<span class="diamonds" aria-hidden="true"><svg viewBox="0 0 62 20" fill="none" stroke="currentColor" stroke-width="1.2">'
            '<path d="M11 1 21 10 11 19 1 10z"/><path d="M31 1 41 10 31 19 21 10z"/><path d="M51 1 61 10 51 19 41 10z"/></svg></span>')
BANDS = '<div class="bands" aria-hidden="true"><i></i><i></i><i></i></div>'


def brand(light=True):
    return ('<a class="brand" href="/">'
            '<img class="tree-light" src="/assets/img/tree-gold.svg" alt="Truevine Express tree logo" width="50" height="33">'
            '<img class="tree-dark" src="/assets/img/tree-navy.svg" alt="Truevine Express tree logo" width="50" height="33">'
            '<span class="brand-text"><span class="brand-name">Truevine Express</span><span class="brand-sub">LIMITED</span></span></a>')


SERVICES_NAV = [
    ("/it-consulting/", "it", "IT Consulting", "Strategy, cybersecurity, cloud and managed support"),
    ("/telecom-consulting/", "telecom", "Telecom Consulting", "Network design, rollout and enterprise connectivity"),
    ("/logistics-consulting/", "logistics", "Logistics Consulting", "Supply chain, clearance, warehousing and fleet"),
    ("/business-systems/", "erp", "Business Systems", "ERP, warehouse management and procurement software"),
]


def header(current):
    def cur(p):
        return ' aria-current="page"' if current == p else ""
    drop = "".join(
        f'<a href="{h}"{cur(h)}><span class="ico">{icon(i)}</span><span><strong>{t}</strong><span>{d}</span></span></a>'
        for h, i, t, d in SERVICES_NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    {brand()}
    <nav class="nav" aria-label="Primary">
      <div class="nav-drop">
        <button type="button" aria-haspopup="true">Services {icon("chev", "2")}</button>
        <div class="drop">{drop}</div>
      </div>
      <a href="/about/"{cur("/about/")}>About</a>
      <a href="/contact/"{cur("/contact/")}>Contact</a>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{PHONE_TEL}">{icon("phone")}{PHONE_DISPLAY}</a>
      <a class="btn" href="/contact/">Book a consultation {icon("arrow")}</a>
      <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" inert>
  <a href="/">Home <small>01</small></a>
  <a href="/it-consulting/">IT Consulting <small>02</small></a>
  <a href="/telecom-consulting/">Telecom Consulting <small>03</small></a>
  <a href="/logistics-consulting/">Logistics Consulting <small>04</small></a>
  <a href="/business-systems/">Business Systems <small>05</small></a>
  <a href="/about/">About <small>06</small></a>
  <a href="/contact/">Contact <small>07</small></a>
  <div class="mm-foot">
    <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <span>{ADDRESS_LINES[0]}, {ADDRESS_LINES[1]}</span>
    <a class="btn" href="/contact/">Book a consultation {icon("arrow")}</a>
  </div>
</div>'''


def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        {brand()}
        <p>Lagos consultancy for IT, telecom, logistics and business systems. We implement ERP, warehouse and procurement software, and design, fix and run the infrastructure Nigerian organisations depend on.</p>
        {DIAMONDS}
      </div>
      <div class="footer-col">
        <p class="footer-h">Services</p>
        <ul>
          <li><a href="/it-consulting/">IT Consulting</a></li>
          <li><a href="/telecom-consulting/">Telecom Consulting</a></li>
          <li><a href="/logistics-consulting/">Logistics Consulting</a></li>
          <li><a href="/business-systems/">Business Systems</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-h">Company</p>
        <ul>
          <li><a href="/about/">About us</a></li>
          <li><a href="/about/#leadership">Leadership</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacy/">Privacy notice</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-h">Reach us</p>
        <address>
          {ADDRESS_LINES[0]}<br>{ADDRESS_LINES[1]}<br>
          <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </address>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Truevine Express Limited. {RC}. Incorporated in Nigeria.</span>
      <span>Photography via <a href="/about/#credits">Unsplash</a></span>
    </div>
  </div>
</footer>'''


def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": SITE + "/#org",
        "name": "Truevine Express Limited",
        "alternateName": "Truevine Express LTD",
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo-512.png",
        "image": SITE + "/assets/img/og.jpg",
        "description": "Lagos consultancy for IT, telecom, logistics and business systems (ERP, warehouse management, procurement software) serving corporates, SMEs, government agencies, telecom operators and international firms entering Nigeria.",
        "telephone": PHONE_TEL,
        "email": EMAIL,
        "foundingDate": FOUNDED,
        "identifier": {"@type": "PropertyValue", "propertyID": "CAC RC Number", "value": "1848110"},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "92 Obafemi Awolowo Way, 2nd Floor",
            "addressLocality": "Ikeja",
            "addressRegion": "Lagos",
            "addressCountry": "NG",
        },
        "areaServed": {"@type": "Country", "name": "Nigeria"},
        "employee": [{"@type": "Person", "name": n, "jobTitle": t} for n, t, _ in LEADERS],
        "knowsAbout": ["ERP implementation", "Warehouse management systems", "Procurement software", "IT consulting", "Cybersecurity", "Cloud migration", "Telecommunications network design",
                       "Enterprise connectivity", "Logistics consulting", "Supply chain management", "Customs clearance advisory"],
    }


def layout(*, path, title, description, body, current=None, schema=None, noindex=False, preload_img=None, og_type="website"):
    canonical = SITE + path
    title = _html.escape(_html.unescape(title), quote=True)
    description = _html.escape(_html.unescape(description), quote=True)
    schemas = [org_schema()] + (schema or [])
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False, separators=(",", ":"))}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    pre = f'<link rel="preload" as="image" href="{preload_img[0]}" imagesrcset="{preload_img[1]}" imagesizes="100vw" fetchpriority="high">' if preload_img else ""
    return f'''<!doctype html>
<html lang="en-NG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#05192F">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Truevine Express Limited">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_NG">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}/assets/img/og.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
<link rel="preload" href="/assets/fonts/poppins-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/poppins-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
{ld}
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/js/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''


def cta_band(title="Tell us what is slowing you down.", text="One conversation is usually enough to find the bottleneck. Book a free 30-minute consultation and leave with a clear next step, whether or not you hire us.", button="Book a consultation", eyebrow="Start here"):
    return f'''<section class="section section--tight">
  <div class="wrap">
    <div class="cta-band on-dark reveal">
      {img("lagos_night", "Lekki-Ikoyi Link Bridge in Lagos lit up at night", widths=(960, 1600), sizes="(max-width:1240px) 100vw, 1240px")}
      <div class="inner">
        <div>
          <span class="eyebrow">{eyebrow}</span>
          <h2>{title}</h2>
          <p>{text}</p>
          <div class="btn-row" style="margin-top:32px"><a class="btn" href="/contact/">{button} {icon("arrow")}</a></div>
        </div>
        <div class="cta-contacts">
          <a href="tel:{PHONE_TEL}">{icon("phone")}<span><small>Call&nbsp;us</small><b>{PHONE_DISPLAY}</b></span></a>
          <a href="mailto:{EMAIL}">{icon("mail")}<span><small>Email</small><b>{EMAIL}</b></span></a>
          <a href="/contact/#visit">{icon("pin")}<span><small>Visit</small><b>92 Obafemi Awolowo Way, 2nd Floor, Ikeja</b></span></a>
        </div>
      </div>
    </div>
  </div>
</section>'''


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)],
    }


def faq_schema(qas):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas],
    }


def faq_html(qas):
    return '<div class="faq reveal">' + "".join(
        f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in qas) + "</div>"
