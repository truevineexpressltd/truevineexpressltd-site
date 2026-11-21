from lib import *

PAGES = {
    "it": dict(
        path="/it-consulting/", key="servers", alt="Aisle of server racks in a data centre", icon="it", form_value="IT",
        title="IT Consulting in Lagos | Truevine Express Limited",
        description="IT strategy, cybersecurity and NDPA readiness, cloud migration, networks, managed support and IT procurement for Nigerian organisations. Truevine Express, Ikeja, Lagos.",
        eyebrow="IT Consulting",
        h1='Technology that works <em class="accent">quietly</em> and stays secure.',
        lede="We plan, secure and support the systems your people use every day, from email and file sharing to networks, servers and business applications, so technology stops being the reason work stalls.",
        intro_h='Your IT should support the business, <em class="accent">not slow it down.</em>',
        intro=["Many Nigerian organisations run on technology that was set up in a hurry: shared passwords, unpatched laptops, backups nobody has tested and a network that slows down every afternoon. It works until it does not, and then it is expensive.",
               "We assess what you have, fix what is risky, and build a roadmap that matches your budget. Then we can stay on to run it, or hand it over to your team with full documentation."],
        side_key="it", side_alt="Blue network cables in a server rack",
        bullets=[("Fewer outages", "Proactive monitoring and maintenance instead of firefighting."),
                 ("Lower risk", "Security controls and backups that are tested, not assumed."),
                 ("Predictable costs", "Licences, hardware and support planned ahead, not bought in emergencies.")],
        services=[
            ("compass", "IT strategy & roadmap", "A clear picture of where your technology is today and a prioritised plan for the next 12 to 36 months.", ["Current-state assessment", "Budget and licence planning", "Board-ready roadmap"]),
            ("shield", "Cybersecurity & NDPA readiness", "Practical security that protects your data and helps you meet your obligations under the Nigeria Data Protection Act.", ["Risk and gap assessment", "Access control, MFA and endpoint security", "Data mapping and breach response plans"]),
            ("cloud", "Cloud & workplace migration", "Move email, files and applications to Microsoft 365, Google Workspace or the cloud without losing data or a working day.", ["Migration planning and cutover", "Licensing right-sized to your team", "Staff onboarding and training"]),
            ("network", "Network & infrastructure", "Office networks and server rooms designed for speed, security and Nigerian power conditions.", ["LAN, Wi-Fi and structured cabling", "Firewalls and secure remote access", "UPS, inverter and solar backup for IT"]),
            ("headset", "Managed IT support", "A responsive helpdesk and proactive maintenance, so your staff can get on with their work.", ["Helpdesk with agreed response times", "Patching, monitoring and backups", "Monthly service reports"]),
            ("box", "IT procurement & vendor management", "Genuine hardware and software at fair prices, delivered and configured, with warranties registered in your name.", ["Laptops, servers and networking gear", "Vendor comparison and negotiation", "Asset register and lifecycle tracking"]),
        ],
        faq=[
            ("Do we need to replace all our equipment to work with you?", "No. We start with what you already have, keep what is fit for purpose and only recommend replacements where the risk or cost of keeping something is higher than replacing it."),
            ("Can you help us comply with the Nigeria Data Protection Act?", "Yes. We help you understand what personal data you hold, put the right security controls and policies in place, and prepare the evidence you need. Where a formal compliance audit filing is required, we work alongside a licensed Data Protection Compliance Organisation."),
            ("Do you offer ongoing support or only projects?", "Both. Many clients start with a one-off project such as a migration or security review, then keep us on a monthly support plan with agreed response times."),
            ("Can you support offices outside Lagos?", "Yes. We support teams across Nigeria with remote support and arrange on-site visits when they are needed."),
        ],
    ),
    "telecom": dict(
        path="/telecom-consulting/", key="telecom", alt="Telecommunication towers silhouetted at sunset", icon="telecom", form_value="Telecom",
        title="Telecom Consulting in Lagos | Truevine Express Limited",
        description="Telecom network planning, site rollout, resilient enterprise connectivity, unified communications and telecom cost audits for operators and enterprises in Nigeria.",
        eyebrow="Telecom Consulting",
        h1='Networks planned for Nigeria and <em class="accent">built</em> to stay up.',
        lede="We help operators, vendors and enterprises plan, roll out and run connectivity that survives fibre cuts, power failures and rapid growth, and we make sure you are not overpaying for it.",
        intro_h='Connectivity is now <em class="accent">critical infrastructure.</em>',
        intro=["When the link goes down, sales stop, branches go dark and customers notice. Yet many organisations rely on a single provider, pay for bandwidth they do not use and have no tested failover plan.",
               "For operators and vendors, the challenge is different: rolling out sites on time while handling permits, landlords, contractors and power. We bring planning discipline and field coordination to both."],
        side_key="fibre", side_alt="Fibre optic cables connected to a network switch",
        bullets=[("Resilient links", "Primary and backup paths across different providers and technologies."),
                 ("Faster rollouts", "Permits, sites and contractors coordinated against one schedule."),
                 ("Lower telecom spend", "Contracts and bills audited against what you actually use.")],
        services=[
            ("map", "Network planning & design", "Coverage, capacity and route design for fibre, microwave and last-mile networks.", ["Survey and feasibility studies", "Fibre and microwave route design", "Capacity and growth planning"]),
            ("tower", "Site rollout & project management", "End-to-end coordination of site build and upgrade programmes, from acquisition to handover.", ["Site acquisition support", "Contractor and vendor coordination", "Progress tracking and quality checks"]),
            ("doc", "Regulatory & permit support", "Plan around NCC licensing and state right-of-way and building approvals so work is not halted midway.", ["Licence and permit mapping", "Documentation preparation", "Liaison with relevant agencies"]),
            ("network", "Enterprise connectivity & redundancy", "Reliable internet and inter-branch links with automatic failover when a provider has an outage.", ["ISP selection and SLA review", "SD-WAN and dual-link failover", "Satellite or LTE backup paths"]),
            ("headset", "Unified communications", "Business phone systems, VoIP, contact-centre lines and video meetings that work on your network.", ["IP-PBX and VoIP design", "Number porting and setup", "Call quality and network tuning"]),
            ("receipt", "Telecom cost & contract audit", "We review your telecom bills and contracts line by line to find overcharges and unused services.", ["Invoice and usage audit", "Contract renegotiation support", "Ongoing spend monitoring"]),
        ],
        faq=[
            ("Do you work with telecom operators or only businesses?", "Both. We support operators, tower companies, ISPs and equipment vendors with planning and rollout capacity, and we help enterprises and agencies get dependable connectivity."),
            ("Can you help when our internet provider keeps failing?", "Yes. We review your current service and contract, then design a setup with a second provider or technology that takes over automatically when the main link fails."),
            ("Do you handle NCC licensing directly?", "We help you understand which licences and permits apply, prepare the documentation and coordinate with the relevant bodies. Applications are made in the licence holder's name."),
            ("How much can a telecom audit save?", "It depends on your contracts and usage, so we do not promise a number in advance. We review the bills first, then show you exactly what we found before you decide anything."),
        ],
    ),
    "logistics": dict(
        path="/logistics-consulting/", key="port", alt="Aerial view of a container yard at a port", icon="logistics", form_value="Logistics",
        title="Logistics Consulting in Lagos | Truevine Express Limited",
        description="Supply chain strategy, import and customs clearance advisory, warehouse design, fleet and last-mile optimisation and logistics technology for businesses in Nigeria.",
        eyebrow="Logistics Consulting",
        h1='Supply chains that clear port and <em class="accent">reach</em> the shelf.',
        lede="We help importers, manufacturers, distributors and retailers move goods through Nigerian ports, warehouses and roads with less delay, lower cost and full visibility of where everything is.",
        intro_h='Every day in transit is <em class="accent">money on hold.</em>',
        intro=["Demurrage at Apapa and Tin Can, stock-outs in one depot while another is overstocked, trucks stuck on the same routes every day: these are not just operational headaches. They tie up cash and lose customers.",
               "We map your supply chain from supplier to customer, find where time and money are lost, and fix it with better processes, better partners and the right technology. Because we also do IT, the tracking systems we recommend actually connect to the rest of your business."],
        side_key="warehouse", side_alt="Warehouse aisle with stacked inventory",
        bullets=[("Faster clearance", "Documentation and coordination that keep cargo moving."),
                 ("Leaner inventory", "Stock where it is needed, with less tied-up cash."),
                 ("Full visibility", "Know where every order, truck and pallet is.")],
        services=[
            ("route", "Supply chain & distribution strategy", "Design the network of suppliers, warehouses and routes that best serves your customers at the lowest total cost.", ["End-to-end supply chain mapping", "Depot and distribution network design", "Cost-to-serve analysis"]),
            ("doc", "Import, export & clearance advisory", "Get documentation right for Nigeria Customs' B'Odogwu platform and keep cargo moving through the ports.", ["Form M and PAAR documentation review", "Coordination with licensed customs agents", "Demurrage and delay reduction"]),
            ("warehouse", "Warehouse design & inventory", "Layouts, processes and systems that speed up picking and keep stock counts accurate.", ["Layout and slotting design", "Inventory policy and cycle counting", "Warehouse management system selection"]),
            ("logistics", "Fleet & last-mile optimisation", "Plan routes and schedules around Lagos traffic and get more deliveries out of every vehicle.", ["Route and load planning", "Vehicle tracking and telematics", "Driver and dispatch processes"]),
            ("chart", "Logistics technology & visibility", "Connect tracking, inventory and order systems so everyone works from the same live information.", ["Shipment and order tracking", "ERP and system integration", "Dashboards and KPIs"]),
            ("users", "3PL & carrier selection", "Choose and manage freight forwarders, haulage firms and third-party warehouses that perform.", ["Tender preparation and evaluation", "SLA and contract design", "Performance scorecards"]),
        ],
        faq=[
            ("Are you a clearing agent or a haulage company?", "No. We are consultants. We advise on documentation, processes and partners, and coordinate the licensed customs agents, freight forwarders and hauliers who do the physical work. This keeps our advice independent."),
            ("Can you help reduce demurrage charges?", "Yes. We look at where delays happen, from documentation to terminal and transport scheduling, and put fixes in place for each stage."),
            ("We are a growing distributor. Is this only for large companies?", "Not at all. Many of the biggest gains come from simple changes such as better route planning, stock rules and a basic tracking system. We scale the work to your size and budget."),
            ("Do you work outside Lagos?", "Yes. We support supply chains that run across Nigeria, from port to regional depots and final delivery."),
        ],
    ),
}

MODELS = [
    ("Advisory sprint", "2 to 4 weeks", "A focused assessment that ends in a written report, a prioritised plan and a budget.", ["On-site or remote review", "Findings workshop", "Roadmap and budget"], False),
    ("Project delivery", "Fixed scope", "We plan and run a defined project from kick-off to handover, with milestones you sign off.", ["Dedicated project lead", "Vendor and contractor management", "Documentation and training"], True),
    ("Managed retainer", "Monthly", "Ongoing support and continuous improvement with agreed response times and regular reviews.", ["Helpdesk and monitoring", "Monthly reporting", "Quarterly strategy reviews"], False),
]


def build(slug):
    p = PAGES[slug]
    svcs = "".join(
        f'<article class="svc reveal reveal-d{i % 3}"><span class="ico">{icon(ic)}</span><h3>{t.replace(" & ", " &amp; ")}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></article>'
        for i, (ic, t, d, li) in enumerate(p["services"]))
    models = "".join(
        f'<div class="model{" featured" if f else ""} reveal reveal-d{i}"><span class="tag">Option 0{i+1}</span><h3>{t}</h3><div class="dur">{d}</div><p>{x}</p><ul>{"".join(f"<li>{y}</li>" for y in li)}</ul></div>'
        for i, (t, d, x, li, f) in enumerate(MODELS))
    checks = "".join(f'<li>{icon("check")}<span><b>{a}.</b> {b}</span></li>' for a, b in p["bullets"])
    others = [s for s in SERVICES_NAV if s[0] != p["path"]]
    other_links = " ".join(f'<a class="link-arrow" href="{h}">{t} {icon("arrow")}</a>' for h, _, t, _ in others)
    body = f'''
<section class="page-hero on-dark">
  {img(p["key"], p["alt"], widths=(640, 960, 1280, 1920), eager=True)}
  {BANDS.replace('class="bands"', 'class="bands bands--sm"')}
  <div class="wrap">
    <nav class="crumbs reveal" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>{p["eyebrow"]}</span></nav>
    <span class="eyebrow reveal">{p["eyebrow"]}</span>
    <h1 class="reveal reveal-d1">{p["h1"]}</h1>
    <p class="lede reveal reveal-d2">{p["lede"]}</p>
    <div class="btn-row reveal reveal-d3">
      <a class="btn" href="/contact/?service={p["form_value"]}">Discuss your project {icon("arrow")}</a>
      <a class="btn btn--ghost" href="tel:{PHONE_TEL}">{icon("phone")} {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="eyebrow reveal">The challenge</span>
      <h2 class="reveal reveal-d1">{p["intro_h"]}</h2>
      {"".join(f'<p class="lede reveal reveal-d2" style="margin-top:22px">{x}</p>' for x in p["intro"])}
      <ul class="checks reveal reveal-d3">{checks}</ul>
    </div>
    <div class="split-media reveal reveal-d1">
      <span class="deco" aria-hidden="true"></span>
      <div class="frame">{img(p["side_key"], p["side_alt"], widths=(480, 720, 960, 1280), sizes="(max-width:860px) 100vw, 50vw", ratio=(4, 5))}</div>
    </div>
  </div>
</section>

<section class="section bg-ivory">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Services</span>
        <h2 class="reveal reveal-d1">What we <em class="accent">deliver.</em></h2>
      </div>
      <p class="lede reveal reveal-d2">Take one service or combine several. Every engagement starts with a conversation about what you actually need.</p>
    </div>
    <div class="svc-grid">{svcs}</div>
  </div>
</section>

<section class="section on-dark">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Ways to work with us</span>
        <h2 class="reveal reveal-d1">Engagements that fit <em class="accent">how</em> you buy.</h2>
      </div>
      <p class="lede reveal reveal-d2">Every option comes with a written proposal, a fixed scope and pricing agreed before work starts.</p>
    </div>
    <div class="models">{models}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow reveal">Questions</span>
      <h2 class="reveal reveal-d1">Frequently <em class="accent">asked.</em></h2>
    </div>
    {faq_html(p["faq"])}
    <div class="btn-row reveal" style="justify-content:center;margin-top:56px;gap:28px">{other_links}</div>
  </div>
</section>

{cta_band()}
'''
    svc_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "name": p["eyebrow"], "serviceType": p["eyebrow"],
        "provider": {"@id": SITE + "/#org"},
        "areaServed": {"@type": "Country", "name": "Nigeria"},
        "description": p["description"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": p["eyebrow"] + " services",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "description": d}} for _, t, d, _ in p["services"]]},
    }
    return layout(path=p["path"], title=p["title"], description=p["description"], body=body, current=p["path"],
                  schema=[svc_schema, faq_schema(p["faq"]), breadcrumb_schema([("Home", "/"), (p["eyebrow"], p["path"])])])
