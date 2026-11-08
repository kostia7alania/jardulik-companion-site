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

## Wordstat evidence

[Yandex Wordstat](https://wordstat.yandex.ru/) was checked through its authenticated Popular queries interface on 8 November 2026. The [captured keyword-only report](docs/wordstat-2026-11-08.json) preserves the observed counts, query URLs and each report's actual date window. It contains no account credentials or profile data.

Filters: all regions; desktops, smartphones and tablets; broad matching with word forms, without query operators. The interface warned that some data could be temporarily unavailable. These are counts shown for query reports, not exact-match keyword volumes, unique people, landing-page visits or a traffic forecast. Related queries overlap and their counts must not be added. Different query reports showed different periods, so the rows are not directly comparable across date windows.

| Query report | Displayed count | Period shown |
| --- | ---: | --- |
| [jardulik](https://wordstat.yandex.ru/?region=all&view=table&words=jardulik) | 10 | 2026-09-08 to 2026-10-07 |
| [осетинские знакомства](https://wordstat.yandex.ru/?region=all&view=table&words=%D0%BE%D1%81%D0%B5%D1%82%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%B0) | 92 | 2026-09-08 to 2026-10-07 |
| [жардулик](https://wordstat.yandex.ru/?region=all&view=table&words=%D0%B6%D0%B0%D1%80%D0%B4%D1%83%D0%BB%D0%B8%D0%BA) | 55 | 2026-09-08 to 2026-10-07 |
| [знакомства осетины](https://wordstat.yandex.ru/?region=all&view=table&words=%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%B0%20%D0%BE%D1%81%D0%B5%D1%82%D0%B8%D0%BD%D1%8B) | 57 | 2026-09-08 to 2026-10-07 |
| [архив анкет](https://wordstat.yandex.ru/?region=all&view=table&words=%D0%B0%D1%80%D1%85%D0%B8%D0%B2%20%D0%B0%D0%BD%D0%BA%D0%B5%D1%82) | 687 | 2026-09-08 to 2026-10-07 |
| [автолайки знакомства](https://wordstat.yandex.ru/?region=all&view=table&words=%D0%B0%D0%B2%D1%82%D0%BE%D0%BB%D0%B0%D0%B9%D0%BA%D0%B8%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%B0) | 2 | 2026-10-07 to 2026-11-07 |
| [jardulik бот](https://wordstat.yandex.ru/?region=all&view=table&words=jardulik%20%D0%B1%D0%BE%D1%82) | 0 | 2026-10-07 to 2026-11-07 |

The Russian brand spelling is included naturally in the home-page title, H1 and explanatory FAQ; the lead adds the Ossetian app context. The companion still serves existing Jardulik accounts; it is not presented as a new dating network. The broad `архив анкет` report mostly showed unrelated intent, so its larger count does not make it the main SEO target. The `автолайки знакомства` query is not a product promise while automated likes remain disabled. Zero in the `jardulik бот` report describes that displayed period, not an absence of all future demand.

The home-page SoftwareApplication and FAQPage JSON-LD describe the visible product copy and questions. Structured data does not establish indexing, rich-result eligibility or search ranking. The existing connection guide remains the single substantive guide; no thin keyword pages were added.

## Content limits

The demo profile, illustration and history are fictional. The site makes no claims of official affiliation, invisible automation, guaranteed account safety, matching success or one-click phone onboarding. Jardulik pricing/subscription remains separate. Backup deletion has no guaranteed automatic retention window in this beta.
