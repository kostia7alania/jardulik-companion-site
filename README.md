# Jardulik Companion landing

Public static landing for an independent Telegram companion to Jardulik. The app backend and all account/profile data live outside this public repository.

## Design

- Palette: deep navy `#111b2c`, soft text `#e7eef8`, pale blue `#a4c8f5`, raised navy `#21354d`, muted rose `#e2a0b4`, slate `#a6b7cd`. The site defaults to dark, including browser-native controls, without adding a theme toggle.
- Type: self-hosted variable Onest with its bundled SIL Open Font License.
- Layout: a readable left-aligned product introduction beside a clearly fictional Telegram chat example; a folder/history illustration, a real three-step onboarding flow and native FAQ disclosures.
- The strongest visual is the chat example. Supporting content uses varied prose/list structures rather than identical feature cards.

## Local preview

No install or build is required:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Run from this directory and open `http://127.0.0.1:4173/`. Check both a desktop viewport and a narrow mobile viewport, keyboard navigation, the local favorite/next demo and native FAQ disclosures.

## Bot destination

The only real Telegram bot URL is the `data-bot-target` anchor in `bot.html`. Its destination is the project bot `@dvachers_jardulik_bot`, whose creation was verified by the parent agent on 8 November 2026. Every CTA uses that local redirect page, including its no-JavaScript fallback. The shared `start=site` parameter carries source attribution, not an individual visitor identifier. Guide links use `bot.html?source=guide_connect`; JavaScript permits only that explicit source override and otherwise keeps `site`. No bot token is present in this repository.

## Public release

Live Pages base: `https://kostia7alania.ru/jardulik-companion-site/`.

The project inherits the account-level custom domain from GitHub Pages. Its github.io address redirects to the live URL above. All assets use project-compatible paths. `.nojekyll` avoids a Jekyll build; Pages serves `main:/`. Do not change account DNS or the user-site Pages configuration for this project. The repository contains no deploy credentials, profile exports, real people or backend source. The Cloudflare Web Analytics beacon token is intentionally public; it does not grant dashboard access.

Before publication:

1. Recheck the verified bot destination in `bot.html`.
2. Confirm the advertised commands and archive/backup behavior against the deployed backend.
3. Run `python3 scripts/check_site.py` and `node --check assets/site.js`.
4. Review desktop/mobile previews and content, then publish.

## SEO and measurement

Primary intent: Jardulik profiles and archive/history in Telegram, not a separate dating network. Each indexable page has a unique title, description and canonical. The home page has Open Graph/Twitter metadata and a SoftwareApplication JSON-LD description without invented prices, reviews or ratings. `guide.html` is a substantive manual-connection guide, with local links, official Telegram background, a BreadcrumbList and its own share metadata. It does not ask visitors to execute scripts, disable browser protection, or share Telegram passwords/OTP/session files.

`sitemap.xml` lists the indexable pages. This is a GitHub **project** Pages site: a repository-local `robots.txt` would not control the host-root crawler policy, so none is presented as an effective robots configuration. Verify indexing in Search Console after publication and ownership setup. Search ranking, visits and keyword volume are not established by the site build.

`assets/social.svg` is the source-controlled share illustration. `assets/social.png` is its 1200 × 630 raster derivative for social crawlers, generated with `rsvg-convert -o assets/social.png assets/social.svg`. Both contain only product text and abstract shapes.

Cloudflare Web Analytics is installed once before `</body>` on each of the six HTML pages, using the exact official beacon URL and public property token. Manual JS installation is enabled for the property; automatic injection is disabled to avoid duplicate counting. The generated `type="module"` script uses `fetchpriority="low"` and does not block HTML parsing. No DNS or account-wide settings are managed by this repository.

The counter measures site traffic and page performance. [Cloudflare describes its analytics](https://www.cloudflare.com/web-analytics/) as using no cookies, localStorage or individual fingerprints. We add no visitor IDs, custom events, Telegram account data or profile data, and do not connect the counter to bot sessions. Google Analytics, advertising trackers and contact forms are not installed. [Official manual installation instructions](https://developers.cloudflare.com/web-analytics/get-started/) explain the beacon setup.

`scripts/check_site.py` requires exactly one approved beacon per page and rejects other external scripts or a changed token. Local checks confirm the installation markup; successful reporting still requires a live-browser Network check and the Cloudflare dashboard. Browser blockers or immediate navigation from `bot.html` may prevent a beacon from being sent. A bot start attributed to `site` measures a bot entry, not a page view or unique website visitor.

## Content limits

The demo profile, illustration and history are fictional. The site makes no claims of official affiliation, invisible automation, guaranteed account safety, matching success or one-click phone onboarding. Jardulik pricing/subscription remains separate. Backup deletion has no guaranteed automatic retention window in this beta.
