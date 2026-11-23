from lib import *
from lib import _I


def hero_viz():
    cx, cy, R = 270, 290, 205
    nodes = [("IT", cx, cy - R, "it"), ("Telecom", cx - R, cy, "telecom"),
             ("Logistics", cx + R, cy, "logistics"), ("Business Systems", cx, cy + R, "erp")]
    out = ['<svg viewBox="0 0 540 600" role="img" aria-label="Diagram: IT, telecom, logistics and business systems connected to your operation">',
           '<defs><radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F8CD6D" stop-opacity=".35"/><stop offset="1" stop-color="#F8CD6D" stop-opacity="0"/></radialGradient>'
           '<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="#D9B253" stop-opacity=".9"/><stop offset="1" stop-color="#3D6EB1" stop-opacity=".6"/></linearGradient></defs>']
    for r in (130, 262):
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#fff" stroke-opacity=".07" stroke-dasharray="2 6"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="url(#glow)"/>')
    out.append(f'<path id="rim" d="M{cx},{cy - R} A{R},{R} 0 1,1 {cx - 0.01},{cy - R}" fill="none" stroke="#fff" stroke-opacity=".16"/>')
    bends = [(40, 0), (0, -40), (0, 40), (-40, 0)]
    for i, (_, x, y, _) in enumerate(nodes):
        mx, my = (x + cx) / 2 + bends[i][0], (y + cy) / 2 + bends[i][1]
        out.append(f'<path id="p{i}" d="M{cx},{cy} Q{mx:.0f},{my:.0f} {x},{y}" fill="none" stroke="url(#ln)" stroke-width="1.4" stroke-dasharray="4 5"><animate attributeName="stroke-dashoffset" from="0" to="-90" dur="6s" repeatCount="indefinite"/></path>')
    for i in range(4):
        for k, delay in enumerate((0, 1.6)):
            out.append(f'<circle r="3.6" fill="#F8CD6D"><animateMotion dur="3.2s" begin="{i*0.6+delay}s" repeatCount="indefinite" keyPoints="{"0;1" if k==0 else "1;0"}" keyTimes="0;1" calcMode="linear"><mpath href="#p{i}"/></animateMotion><animate attributeName="opacity" values="0;1;1;0" dur="3.2s" begin="{i*0.6+delay}s" repeatCount="indefinite"/></circle>')
    for i in range(3):
        out.append(f'<circle r="2.6" fill="#A3BDD6"><animateMotion dur="12s" begin="{i*4}s" repeatCount="indefinite"><mpath href="#rim"/></animateMotion></circle>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="none" stroke="#F8CD6D" stroke-opacity=".5"><animate attributeName="r" values="62;92" dur="3s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".55;0" dur="3s" repeatCount="indefinite"/></circle>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="#F8CD6D"/>')
    out.append(f'<image href="/assets/img/tree-navy.svg" x="{cx-34}" y="{cy-34}" width="68" height="45"/>')
    out.append(f'<text x="{cx}" y="{cy+37}" text-anchor="middle" font-family="Poppins,sans-serif" font-size="8" font-weight="600" letter-spacing="1.2" fill="#05192F">YOUR OPERATION</text>')
    for label, x, y, ic in nodes:
        ly = y + 62 if label != "IT" else y - 50
        out.append(f'<g><circle cx="{x}" cy="{y}" r="36" fill="#08254A" stroke="#D9B253" stroke-opacity=".7"/>'
                   f'<g transform="translate({x-14},{y-14}) scale(1.1667)" fill="none" stroke="#F8CD6D" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{_I[ic]}</g>'
                   f'<text x="{x}" y="{ly}" text-anchor="middle" font-family="Poppins,sans-serif" font-size="14" font-weight="500" fill="#fff" fill-opacity=".9" letter-spacing=".5">{label}</text></g>')
    out.append('</svg>')
    return "".join(out)


def converge_viz():
    return '''<svg viewBox="0 0 520 520" role="img" aria-label="Diagram: IT, telecom and logistics overlap, and Truevine works where they meet, with business systems tying them together">
<defs><radialGradient id="cg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F8CD6D" stop-opacity=".9"/><stop offset="1" stop-color="#AF8A2C" stop-opacity=".85"/></radialGradient></defs>
<g fill="none" stroke-width="1.5">
<circle cx="260" cy="190" r="140" stroke="#A3BDD6" stroke-opacity=".55" fill="#3D6EB1" fill-opacity=".10"></circle>
<circle cx="190" cy="310" r="140" stroke="#A3BDD6" stroke-opacity=".55" fill="#3D6EB1" fill-opacity=".10"></circle>
<circle cx="330" cy="310" r="140" stroke="#A3BDD6" stroke-opacity=".55" fill="#3D6EB1" fill-opacity=".10"></circle>
</g>
<circle cx="260" cy="270" r="44" fill="none" stroke="#F8CD6D" stroke-opacity=".5"><animate attributeName="r" values="44;70" dur="3.2s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".6;0" dur="3.2s" repeatCount="indefinite"/></circle><circle cx="260" cy="270" r="44" fill="url(#cg)"/>
<text x="260" y="266" text-anchor="middle" font-family="Poppins,sans-serif" font-size="11" font-weight="600" letter-spacing="1.5" fill="#05192F">UPTIME</text>
<text x="260" y="282" text-anchor="middle" font-family="Poppins,sans-serif" font-size="9" letter-spacing="1" fill="#05192F">&amp; DELIVERY</text>
<text x="260" y="118" text-anchor="middle" font-family="Poppins,sans-serif" font-size="15" font-weight="500" fill="#fff">IT</text>
<text x="128" y="372" text-anchor="middle" font-family="Poppins,sans-serif" font-size="15" font-weight="500" fill="#fff">Telecom</text>
<text x="392" y="372" text-anchor="middle" font-family="Poppins,sans-serif" font-size="15" font-weight="500" fill="#fff">Logistics</text>
<text x="260" y="470" text-anchor="middle" font-family="Cormorant Garamond,serif" font-style="italic" font-size="20" fill="#F8CD6D">one accountable partner</text>
</svg>'''


def practice_card(n, href, key, ic, title, text, items, alt):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'''<article class="practice reveal reveal-d{n}">
  {img(key, alt, widths=(480, 720, 960), sizes="(max-width:640px) 100vw, (max-width:1100px) 50vw, 33vw", ratio=(3, 4))}
  <span class="practice-num">0{n}</span>
  <span class="practice-ico">{icon(ic)}</span>
  <div class="practice-body">
    <h3>{title}</h3>
    <p>{text}</p>
    <ul>{lis}</ul>
    <span class="more" aria-hidden="true">Explore {title.split()[0] if title != "Business Systems" else "systems"} {icon("arrow")}</span>
  </div>
  <a class="cover" href="{href}"><span class="sr-only">Explore {title}</span></a>
</article>'''


def build():
    lagos_srcset = ", ".join(f"{img_url('lagos', w)} {w}w" for w in (640, 960, 1280, 1920, 2560))
    body = f'''
<section class="hero on-dark">
  <div class="hero-media">{img("lagos", "Aerial view of Lagos", widths=(640, 960, 1280, 1920, 2560), eager=True)}</div>
  {BANDS}
  <div class="wrap">
    <div>
      <span class="eyebrow reveal">IT &middot; Telecom &middot; Logistics &middot; Business Systems</span>
      <h1 class="reveal reveal-d1">We connect the systems that <em class="accent">move</em> Nigerian business.</h1>
      <p class="lede reveal reveal-d2">Truevine Express is a Lagos consultancy for IT, telecom and logistics. We implement ERP, warehouse and procurement systems, and we design, fix and run the infrastructure behind your operation, so the network stays up, the data stays safe and the goods arrive on time.</p>
      <div class="btn-row reveal reveal-d3">
        <a class="btn" href="/contact/">Book a free consultation {icon("arrow")}</a>
        <a class="btn btn--ghost" href="tel:{PHONE_TEL}">{icon("phone")} {PHONE_DISPLAY}</a>
      </div>
      <div class="hero-meta reveal reveal-d4">
        <span>Established {FOUNDED}</span><span>CAC {RC}</span><span>Ikeja, Lagos</span>
      </div>
    </div>
    <div class="hero-viz reveal reveal-d2">{hero_viz()}</div>
  </div>
  <div class="scroll-cue" aria-hidden="true">Scroll<i></i></div>
</section>

<section class="creds" aria-label="Company credentials">
  <div class="wrap">
    <div class="cred"><b>Since {FOUNDED}</b><span>Operating from Lagos</span></div>
    <div class="cred"><b>{RC}</b><span>Registered with the CAC</span></div>
    <div class="cred"><b>Team of 20</b><span>Delivery and operations specialists</span></div>
    <div class="cred"><b>ERP, WMS &amp; procurement</b><span>Implemented and supported</span></div>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">What we do</span>
        <h2 class="reveal reveal-d1">Four practices. <em class="accent">One</em> accountable partner.</h2>
      </div>
      <p class="lede reveal reveal-d2">Most organisations hire one vendor for IT, another for connectivity, a third for logistics and a fourth for their ERP, then spend their week coordinating them. We bring all four under one roof, with one plan and one team answerable for the result.</p>
    </div>
    <div class="practices">
      {practice_card(1, "/it-consulting/", "it", "it", "IT Consulting", "Technology that runs quietly in the background and stays secure.", ["IT strategy and roadmaps", "Cybersecurity and NDPA readiness", "Cloud and Microsoft 365 / Google Workspace", "Managed support and helpdesk"], "Network cables connected to a server rack")}
      {practice_card(2, "/telecom-consulting/", "telecom", "telecom", "Telecom Consulting", "Networks planned for Nigerian conditions and built to stay up.", ["Network planning and design", "Site rollout and project management", "Enterprise connectivity and redundancy", "Telecom cost and contract audits"], "Telecommunication towers at sunset")}
      {practice_card(3, "/logistics-consulting/", "port", "logistics", "Logistics Consulting", "Supply chains that clear port, reach the shelf and show you where everything is.", ["Supply chain and distribution strategy", "Warehouse design", "Import, export and clearance advisory", "Fleet and last-mile optimisation"], "Aerial view of a container port")}
      {practice_card(4, "/business-systems/", "warehouse", "erp", "Business Systems", "ERP, warehouse and procurement software, implemented and supported by our operations team.", ["ERP implementation", "Warehouse management systems", "Procurement software", "Integration, training and support"], "Warehouse aisle with shelving and stock")}
    </div>
  </div>
</section>

{clients_strip()}

<section class="section bg-ivory" id="business-systems">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Business systems</span>
        <h2 class="reveal reveal-d1">ERP, warehouse and procurement systems, <em class="accent">implemented</em> properly.</h2>
      </div>
      <p class="lede reveal reveal-d2">Our operations team implements and supports the systems that run finance, inventory, warehouses and purchasing, from planning through go-live and beyond.</p>
    </div>
    <div class="sys-grid">
      <a class="sys reveal" href="/business-systems/"><span class="ico">{icon("erp")}</span><h3>ERP implementation</h3><p>Finance, inventory, sales and operations on one system, configured around how you really work.</p><span class="link-arrow">ERP services {icon("arrow")}</span></a>
      <a class="sys reveal reveal-d1" href="/business-systems/"><span class="ico">{icon("warehouse")}</span><h3>Warehouse management systems</h3><p>Barcode accuracy and real-time stock across every warehouse, depot and cold room.</p><span class="link-arrow">WMS services {icon("arrow")}</span></a>
      <a class="sys reveal reveal-d2" href="/business-systems/"><span class="ico">{icon("cart")}</span><h3>Procurement software</h3><p>Digital requisitions, approvals and purchase orders that control spend and leave a clean audit trail.</p><span class="link-arrow">Procurement services {icon("arrow")}</span></a>
      <a class="sys reveal reveal-d3" href="/logistics-consulting/"><span class="ico">{icon("route")}</span><h3>Logistics consulting</h3><p>Supply chain design, clearance advisory and last-mile planning to go with the systems.</p><span class="link-arrow">Logistics services {icon("arrow")}</span></a>
    </div>
  </div>
</section>

<section class="section on-dark" style="overflow:hidden">
  <div class="wrap converge">
    <div class="converge-visual reveal">{converge_viz()}</div>
    <div>
      <span class="eyebrow reveal">Why one partner</span>
      <h2 class="reveal reveal-d1">In Nigeria, systems fail <em class="accent">together.</em></h2>
      <p class="lede reveal reveal-d2">A fibre cut takes down the order system. A power dip corrupts the warehouse database. A clearance delay ties up stock you already paid for. These problems cross departments, so the fix has to as well.</p>
      <div class="points">
        <div class="point reveal reveal-d2"><span class="ico">{icon("bolt")}</span><div><h3>Built around local conditions</h3><p>We plan for unstable power, fibre cuts, port congestion and Lagos traffic from day one, not as an afterthought.</p></div></div>
        <div class="point reveal reveal-d3"><span class="ico">{icon("network")}</span><div><h3>One plan across the stack</h3><p>Your connectivity, systems and supply chain are designed to back each other up, with no gaps between vendors.</p></div></div>
        <div class="point reveal reveal-d4"><span class="ico">{icon("users")}</span><div><h3>One team that owns the outcome</h3><p>No finger-pointing between contractors. You call one number, and we answer for the result.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Who we serve</span>
        <h2 class="reveal reveal-d1">Built for organisations that <em class="accent">cannot</em> afford downtime.</h2>
      </div>
      <p class="lede reveal reveal-d2">From a growing SME to a federal agency, the same rule applies: if the network, the systems or the deliveries stop, so does the business.</p>
    </div>
    <div class="audience">
      <div class="aud reveal"><span class="ico">{icon("building", "1.2")}</span><h3>Corporates &amp; SMEs</h3><p>Banks, retail, manufacturing, energy and professional firms that need dependable IT and a supply chain they can see into.</p></div>
      <div class="aud reveal reveal-d1"><span class="ico">{icon("landmark", "1.2")}</span><h3>Government &amp; agencies</h3><p>Ministries, departments and agencies modernising services, securing citizen data and procuring technology with full documentation.</p></div>
      <div class="aud reveal reveal-d2"><span class="ico">{icon("tower", "1.2")}</span><h3>Telecom operators &amp; vendors</h3><p>Operators, tower companies, ISPs and equipment vendors that need planning, rollout and field coordination capacity.</p></div>
      <div class="aud reveal reveal-d3"><span class="ico">{icon("globe", "1.2")}</span><h3>International firms entering Nigeria</h3><p>Foreign companies that need a trusted local partner to set up IT, connectivity and logistics quickly and in line with local rules.</p></div>
    </div>
  </div>
</section>

<section class="section bg-ivory">
  <div class="wrap split">
    <div class="split-media reveal">
      <span class="deco" aria-hidden="true"></span>
      <div class="frame">{img("team", "Consultants working together around a table with laptops", widths=(480, 720, 960, 1280), sizes="(max-width:860px) 100vw, 50vw", ratio=(4, 5))}</div>
      <div class="badge"><b>30 MIN</b><span>Free first consultation. You leave with a clear next step either way.</span></div>
    </div>
    <div>
      <span class="eyebrow reveal">How we work</span>
      <h2 class="reveal reveal-d1">Clear steps, <em class="accent">honest</em> advice, work you can measure.</h2>
      <p class="lede reveal reveal-d2">We start by understanding how your operation actually runs. Then we tell you what will make the biggest difference first, what it will cost and how we will measure it.</p>
      <ul class="checks reveal reveal-d3">
        <li>{icon("check")}<span><b>Vendor-neutral advice.</b> We recommend what fits your budget and your conditions, not what pays the biggest commission.</span></li>
        <li>{icon("check")}<span><b>Fixed scopes and written proposals.</b> You know what you are paying for before work starts.</span></li>
        <li>{icon("check")}<span><b>Documentation you keep.</b> Network maps, passwords, processes and runbooks are handed over, so you are never locked in.</span></li>
      </ul>
      <a class="link-arrow reveal reveal-d4" href="/about/">More about Truevine {icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow reveal">Our process</span>
      <h2 class="reveal reveal-d1">From first call to <em class="accent">steady</em> state.</h2>
    </div>
    <div class="process">
      <div class="step reveal"><span class="step-dot">01</span><h3>Diagnose</h3><p>We review your current setup, costs and pain points on site or remotely, and share findings in plain language.</p></div>
      <div class="step reveal reveal-d1"><span class="step-dot">02</span><h3>Design</h3><p>You get a prioritised plan with options, budgets and timelines, so you can decide with the full picture.</p></div>
      <div class="step reveal reveal-d2"><span class="step-dot">03</span><h3>Deliver</h3><p>We run the project, manage vendors and installers, and report progress against agreed milestones.</p></div>
      <div class="step reveal reveal-d3"><span class="step-dot">04</span><h3>Sustain</h3><p>Optional ongoing support, monitoring and quarterly reviews keep things working as you grow.</p></div>
    </div>
  </div>
</section>

<section class="section on-dark">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Nigeria-ready</span>
        <h2 class="reveal reveal-d1">We know the rules and the <em class="accent">realities.</em></h2>
      </div>
      <p class="lede reveal reveal-d2">Good advice in Nigeria has to account for regulators, ports, power and traffic. These are built into every plan we write.</p>
    </div>
    <div class="ready">
      <div class="ready-card reveal"><span class="tag">Data protection</span><h3>NDPA 2023 &amp; GAID 2025</h3><p>We help you map personal data, close security gaps and prepare for obligations under the Nigeria Data Protection Act and the NDPC's implementation directive.</p></div>
      <div class="ready-card reveal reveal-d1"><span class="tag">Telecoms</span><h3>NCC and state approvals</h3><p>We plan rollouts around licensing, right-of-way and site permits, so projects are not stopped halfway by paperwork.</p></div>
      <div class="ready-card reveal reveal-d2"><span class="tag">Trade</span><h3>Customs on B'Odogwu</h3><p>We help importers get documentation right for Nigeria Customs' B'Odogwu platform and coordinate with licensed agents to reduce demurrage.</p></div>
      <div class="ready-card reveal reveal-d3"><span class="tag">Operations</span><h3>Power &amp; last mile</h3><p>Backup power for critical IT, redundant links when fibre is cut, and delivery routes planned around Lagos congestion.</p></div>
    </div>
  </div>
</section>

{cta_band()}
'''
    return layout(
        path="/",
        title="Truevine Express Limited | IT, Telecom, Logistics & ERP Consulting, Lagos",
        description="Lagos consultancy for IT, telecom, logistics and business systems: ERP implementation, warehouse management and procurement software. Est. 2021, RC 1848110.",
        body=body, current="/",
        preload_img=(img_url("lagos", 1280), lagos_srcset),
        schema=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Truevine Express Limited", "url": SITE + "/"}],
    )
