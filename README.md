# truevineexpressltd.com

Website for **Truevine Express Limited** (RC 1848110, est. 2021), an IT, telecom and logistics consultancy at 92 Obafemi Awolowo Way, 2nd Floor, Ikeja, Lagos.

It is a hand-built static site with no CMS, no monthly fee and nothing to patch. It is hosted free on GitHub Pages with HTTPS, and the domain is registered at Squarespace Domains.

## Pages

| URL | Purpose |
|---|---|
| `/` | Home: hero, three practices, the convergence pitch, audiences, process, Nigeria-ready, CTA |
| `/it-consulting/` | IT services, engagement models, FAQ |
| `/telecom-consulting/` | Telecom services, engagement models, FAQ |
| `/logistics-consulting/` | Logistics services, engagement models, FAQ |
| `/about/` | Story, values, company details, photo credits |
| `/contact/` | Consultation form, phone, email, map |
| `/privacy/` | NDPA 2023 privacy notice |
| `/thank-you/`, `/404.html` | Form fallback and not-found pages (not indexed) |

## How to change something

All content lives in `src/`. **Never edit `site/`**, because it is regenerated on every build.

| To change | Edit |
|---|---|
| Phone, email, address, RC number | `src/lib.py` (constants at the top) |
| Header, footer, CTA band, SEO tags | `src/lib.py` |
| Home page copy | `src/home.py` |
| Service pages (services, FAQs, engagement models) | `src/services.py` (`PAGES` and `MODELS`) |
| About, contact, privacy, 404 | `src/pages.py` |
| Photos | `IMAGES` in `src/lib.py` (Unsplash photo IDs) |
| Colours, spacing, typography | `src/static/assets/css/site.css` (variables at the top) |
| Menu and form behaviour | `src/static/assets/js/site.js` |

After changing CSS or JS, bump `ASSET_V` in `src/lib.py` so browsers fetch the new file.

### Build and test locally

```bash
pip install -r requirements.txt
npm ci
python src/build.py              # writes ./site
python tests/check.py site       # links, alt text, titles, descriptions, JSON-LD, sitemap, key facts
npx html-validate "site/**/*.html"
python -m http.server 8000 -d site   # preview at http://localhost:8000
```

### Deploy

Push to `main`. The GitHub Actions workflow builds, runs both test suites and publishes to GitHub Pages. If a check fails, nothing is deployed and the live site stays as it was.

## Brand

Taken from the Truevine Express LTD Canva brand kit and letterhead.

- Navy `#00488D`, gold `#AF8A2C`, light gold `#F8CD6D`, wordmark gold `#D9B253`, blue `#3D6EB1`
- Fonts (self-hosted): Poppins for UI and body, Cinzel for the wordmark, Cormorant Garamond Italic for accent words
- The letterhead's diagonal bands and triple diamonds are reused as site motifs
- `tree-*.svg` and `logo-full.svg` are vector versions of the letterhead tree, so they stay sharp at any size

## Contact form

The form posts to [FormSubmit](https://formsubmit.co), which forwards each submission to truevineexpressltd@gmail.com. There is no account and no fee. Spam is filtered by a honeypot field.

**One-time activation:** the first submission triggers an "Activate Form" email to truevineexpressltd@gmail.com. Click it once and every later submission is delivered. If JavaScript is off, the form falls back to a normal POST and redirects to `/thank-you/`.

## DNS (Squarespace Domains → GitHub Pages)

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<github-username>.github.io` |

Remove Squarespace's default parking records for `@` and `www` first. Then go to GitHub → repo Settings → Pages, set the custom domain to `truevineexpressltd.com` and tick **Enforce HTTPS** once the certificate is issued (usually within an hour). Leave Squarespace's MX/email records as they are.

## Credits

Photography via Unsplash (licence allows free commercial use). Photographers are listed on `/about/#credits`.
