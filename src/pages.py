from lib import *


def about():
    def initials(n):
        parts = [x for x in n.split() if x[0].isalpha()]
        return parts[0][0] + parts[-1][0]
    leaders = "".join(
        f'<article class="leader reveal reveal-d{i % 3}"><span class="monogram" aria-hidden="true">{initials(n)}</span>'
        f'<h3>{n}</h3><p class="role">{t}</p><p>{b}</p></article>'
        for i, (n, t, b) in enumerate(LEADERS))
    credits = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{n}</a></li>' for _, (_, n, u) in IMAGES.items())
    body = f'''
<section class="page-hero on-dark">
  {img("lagos", "Aerial view of Lagos", widths=(640, 960, 1280, 1920), eager=True)}
  {BANDS.replace('class="bands"', 'class="bands bands--sm"')}
  <div class="wrap">
    <nav class="crumbs reveal" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>About</span></nav>
    <span class="eyebrow reveal">About Truevine Express</span>
    <h1 class="reveal reveal-d1">Deep roots in Lagos. <em class="accent">Reach</em> across Nigeria.</h1>
    <p class="lede reveal reveal-d2">Truevine Express Limited is a Nigerian consultancy founded in {FOUNDED}. We bring IT, telecom, logistics and business systems expertise together so organisations can run without the constant interruptions that hold so many back.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-media reveal">
      <span class="deco" aria-hidden="true"></span>
      <div class="frame" style="aspect-ratio:1;display:grid;place-items:center;background:var(--ivory)">
        <img src="/assets/img/logo-full.svg" alt="Truevine Express Limited logo: a tree with deep roots" width="420" height="380" style="width:72%;height:auto">
      </div>
    </div>
    <div>
      <span class="eyebrow reveal">Our story</span>
      <h2 class="reveal reveal-d1">Why a <em class="accent">tree?</em></h2>
      <p class="lede reveal reveal-d2" style="margin-top:22px">Our logo is a tree with roots as wide as its branches. A vine carries what every branch needs to grow, and that is how we see our job: we are the connection that keeps the whole organisation fed with working systems, reliable networks and goods that arrive on time.</p>
      <p class="lede reveal reveal-d3">We started in Lagos because this is where the problems are hardest: power that cannot be taken for granted, links that get cut, ports that get congested and traffic that never sleeps. Advice that works here works anywhere.</p>
      <blockquote class="quote reveal reveal-d4" style="margin-top:36px">Topnotch service, delivered with honesty.</blockquote>
    </div>
  </div>
</section>

<section class="section bg-ivory">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">What we stand for</span>
        <h2 class="reveal reveal-d1">The <em class="accent">values</em> behind the work.</h2>
      </div>
      <p class="lede reveal reveal-d2">They shape how we scope work, how we price it and how we behave when something goes wrong.</p>
    </div>
    <div class="values">
      <div class="value reveal"><b>I.</b><h3>Truth first</h3><p>We tell you what we find, even when it is not what you hoped to hear. It is in our name.</p></div>
      <div class="value reveal reveal-d1"><b>II.</b><h3>Ownership</h3><p>One team answers for the result. We do not hide behind subcontractors or fine print.</p></div>
      <div class="value reveal reveal-d2"><b>III.</b><h3>Clarity</h3><p>Plain language, written scopes and prices agreed up front. No surprises on the invoice.</p></div>
      <div class="value reveal reveal-d3"><b>IV.</b><h3>Topnotch service</h3><p>We respond quickly, finish what we start and leave every system better documented than we found it.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="eyebrow reveal">Company details</span>
      <h2 class="reveal reveal-d1">Registered, accountable and <em class="accent">easy</em> to verify.</h2>
      <p class="lede reveal reveal-d2" style="margin-top:22px">We are a limited company incorporated with Nigeria's Corporate Affairs Commission. Procurement teams can verify us directly on the CAC public search portal.</p>
      <div class="btn-row reveal reveal-d3" style="margin-top:30px"><a class="btn btn--navy" href="/contact/">Work with us {icon("arrow")}</a></div>
    </div>
    <div class="facts reveal reveal-d1">
      <div class="fact"><small>Registered name</small><b>Truevine Express Limited</b></div>
      <div class="fact"><small>CAC registration</small><b>{RC}</b></div>
      <div class="fact"><small>Established</small><b>{FOUNDED}</b></div>
      <div class="fact"><small>Head office</small><b>Ikeja, Lagos</b></div>
      <div class="fact"><small>Practices</small><b>IT, Telecom, Logistics, Business Systems</b></div>
      <div class="fact"><small>Coverage</small><b>Nationwide, Nigeria</b></div>
    </div>
  </div>
</section>

<section class="section" id="leadership">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Our leadership</span>
        <h2 class="reveal reveal-d1">The people <em class="accent">accountable</em> for your results.</h2>
      </div>
      <p class="lede reveal reveal-d2">Our leadership team brings together experience in technology, operations, finance and people management. We work closely with our teams and clients to deliver practical solutions across IT, telecom and logistics.</p>
    </div>
    <div class="leaders">{leaders}</div>
  </div>
</section>

{clients_strip(dark=True)}

{cta_band("Let&rsquo;s talk.", "Tell us about your business challenges and how we can help.", button="Contact us", eyebrow="Work with us")}

<section class="section--tight" id="credits">
  <div class="wrap prose">
    <h2 style="font-size:1rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-3);margin-top:0">Photo credits</h2>
    <p style="font-size:.9rem">Photography on this site is used under the Unsplash licence. With thanks to:</p>
    <ul style="font-size:.9rem;columns:2">{credits}</ul>
  </div>
</section>
'''
    return layout(path="/about/", title="About Us & Leadership | Truevine Express Limited",
                  description="Truevine Express Limited (RC 1848110), founded in Lagos in 2021: leadership team, values and the organisations we support across IT, telecom, logistics and ERP.",
                  body=body, current="/about/", schema=[breadcrumb_schema([("Home", "/"), ("About", "/about/")])])


def contact():
    chips = "".join(f'<label class="chip"><input type="checkbox" name="Service" value="{v}"><span>{v}</span></label>' for v in ("IT", "Telecom", "Logistics", "Business Systems", "Not sure yet"))
    body = f'''
<section class="page-hero on-dark" style="padding-bottom:200px">
  {img("lagos_night", "Lagos bridge lit up at night", widths=(640, 960, 1280, 1920), eager=True)}
  {BANDS.replace('class="bands"', 'class="bands bands--sm"')}
  <div class="wrap">
    <nav class="crumbs reveal" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>Contact</span></nav>
    <span class="eyebrow reveal">Contact</span>
    <h1 class="reveal reveal-d1">Let us talk about what you <em class="accent">need.</em></h1>
    <p class="lede reveal reveal-d2">Book a free 30-minute consultation. Tell us a little about your organisation and the problem you want solved, and we will come back to you within one business day.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap contact-grid">
    <div class="form-card reveal">
      <h2>Request a consultation</h2>
      <p>Tell us a little about your organisation and what you need. Every field except the service options is required, so we can prepare properly for the call.</p>
      <form id="consult-form" class="form" action="{FORM_POST}" method="POST" data-ajax="{FORM_AJAX}">
        <input type="hidden" name="_subject" value="New consultation request from truevineexpressltd.com">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="{SITE}/thank-you/">
        <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="field"><label for="f-name">Full name</label><input id="f-name" type="text" name="Name" autocomplete="name" required></div>
        <div class="field"><label for="f-org">Organisation</label><input id="f-org" type="text" name="Organisation" autocomplete="organization" required></div>
        <div class="field"><label for="f-email">Work email</label><input id="f-email" type="email" name="email" autocomplete="email" required></div>
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" type="tel" name="Phone" autocomplete="tel" inputmode="tel" minlength="7" maxlength="20" required></div>
        <div class="field field--full"><label>What do you need help with? <span class="opt">(optional, choose any)</span></label><div class="chips">{chips}</div></div>
        <div class="field field--full"><label for="f-type">Type of organisation</label>
          <select id="f-type" name="Organisation type" required>
            <option value="">Select one</option>
            <option>Corporate or SME</option>
            <option>Government ministry, department or agency</option>
            <option>Telecom operator, ISP or vendor</option>
            <option>International company entering Nigeria</option>
            <option>Other</option>
          </select></div>
        <div class="field field--full"><label for="f-msg">Tell us about the challenge</label><textarea id="f-msg" name="Message" required placeholder="What is not working, what you want to achieve and any timelines."></textarea></div>
        <label class="consent"><input type="checkbox" name="Consent" value="Yes" required><span>I agree that Truevine Express may use these details to respond to my request, as described in the <a href="/privacy/">privacy notice</a>.</span></label>
        <div class="form-status" aria-live="polite"></div>
        <div class="form-actions"><button class="btn btn--navy" type="submit">Send request {icon("arrow")}</button><small>We reply within one business day.</small></div>
      </form>
    </div>
    <aside class="info-stack" id="visit">
      <div class="info reveal reveal-d1"><small>Call</small><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><p class="sub">Speak to a consultant directly.</p></div>
      <div class="info reveal reveal-d2"><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a><p class="sub">Send documents, tenders or RFQs here.</p></div>
      <div class="info reveal reveal-d3"><small>Office</small><p>{ADDRESS_LINES[0]}<br>{ADDRESS_LINES[1]}</p><p class="sub"><a href="https://www.google.com/maps/dir/?api=1&amp;destination=92+Obafemi+Awolowo+Way+Ikeja+Lagos" target="_blank" rel="noopener" class="link-arrow" style="font-size:.9rem">Get directions {icon("arrow")}</a></p></div>
      <div class="map reveal reveal-d4"><iframe title="Google Map of our office at 92 Obafemi Awolowo Way, 2nd Floor, Ikeja, Lagos" src="https://maps.google.com/maps?q=92%20Obafemi%20Awolowo%20Way%2C%20Ikeja%2C%20Lagos&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </aside>
  </div>
</section>
'''
    schema = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Truevine Express Limited", "url": SITE + "/contact/",
              "mainEntity": {"@id": SITE + "/#org"}}
    return layout(path="/contact/", title="Contact Truevine Express Limited | Book a Consultation in Lagos",
                  description="Book a free 30-minute consultation with Truevine Express. Call 0703 590 9781, email info@truevineexpressltd.com or visit 92 Obafemi Awolowo Way, 2nd Floor, Ikeja.",
                  body=body, current="/contact/", schema=[schema, breadcrumb_schema([("Home", "/"), ("Contact", "/contact/")])])


def simple(path, title, desc, eyebrow, h1, lede, inner="", noindex=False, buttons=True):
    btns = f'<div class="btn-row reveal reveal-d3"><a class="btn" href="/">Back to home {icon("arrow")}</a><a class="btn btn--ghost" href="tel:{PHONE_TEL}">{icon("phone")} {PHONE_DISPLAY}</a></div>' if buttons else ""
    body = f'''
<section class="page-hero on-dark"{' style="min-height:100vh;display:flex;align-items:center"' if not inner else ""}>
  {BANDS.replace('class="bands"', 'class="bands bands--sm"')}
  <div class="wrap">
    <span class="eyebrow reveal">{eyebrow}</span>
    <h1 class="reveal reveal-d1">{h1}</h1>
    <p class="lede reveal reveal-d2">{lede}</p>
    {btns}
  </div>
</section>
{inner}'''
    return layout(path=path, title=title, description=desc, body=body, noindex=noindex)


def privacy():
    inner = f'''<section class="section"><div class="wrap prose">
<p><strong>Last updated: 20 November 2026</strong></p>
<p>This notice explains how Truevine Express Limited ({RC}), 92 Obafemi Awolowo Way, 2nd Floor, Ikeja, Lagos ("we", "us"), handles personal data collected through this website, in line with the Nigeria Data Protection Act 2023.</p>
<h2>What we collect</h2>
<p>When you submit the consultation form or contact us, we collect the details you provide: your name, organisation, email address, phone number, the type of organisation and the content of your message. We do not use advertising trackers or sell personal data.</p>
<h2>Why we use it</h2>
<ul><li>To respond to your enquiry and arrange a consultation (on the basis of your consent and to take steps at your request before entering a contract).</li><li>To prepare proposals and deliver services you engage us for (contract).</li><li>To keep basic business records required by law (legal obligation).</li></ul>
<h2>Who processes it</h2>
<p>Form submissions are delivered to our business email through FormSubmit, a form-forwarding service, and stored in our Google Workspace or Gmail account. These providers may process data outside Nigeria under their own safeguards. Embedded maps are provided by Google and images are served by Unsplash, which may receive your IP address when the page loads.</p>
<h2>How long we keep it</h2>
<p>Enquiries that do not lead to an engagement are deleted within 24 months. Client records are kept for as long as the engagement and applicable legal retention periods require.</p>
<h2>Your rights</h2>
<p>You can ask to access, correct, delete or receive a copy of your personal data, withdraw consent or object to processing. Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will respond within the time required by law. You may also complain to the Nigeria Data Protection Commission.</p>
<h2>Security</h2>
<p>This site is served over HTTPS. Access to enquiry data is limited to staff who need it to respond to you.</p>
<h2>Contact</h2>
<p>Questions about this notice: <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
</div></section>'''
    return simple("/privacy/", "Privacy Notice | Truevine Express Limited", "How Truevine Express Limited collects and uses personal data submitted through truevineexpressltd.com, in line with the Nigeria Data Protection Act 2023.",
                  "Legal", 'Privacy <em class="accent">notice.</em>', "How we handle the information you share with us through this website.", inner, buttons=False)


def thanks():
    return simple("/thank-you/", "Thank you | Truevine Express Limited", "Your consultation request has reached Truevine Express. We reply within one business day.",
                  "Request received", 'Thank you. We will be in <em class="accent">touch.</em>',
                  "Your request is with our team and we will reply within one business day. For anything urgent, call us now.", noindex=True)


def notfound():
    return simple("/404.html", "Page not found | Truevine Express Limited", "The page you are looking for could not be found. Return to the Truevine Express home page.",
                  "Error 404", 'This page took a <em class="accent">wrong</em> turn.',
                  "The link may be old or mistyped. Head back home, or call us and we will point you in the right direction.", noindex=True)
