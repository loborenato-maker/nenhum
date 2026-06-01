# Action Plan — Clínica Sculpté SEO

**Site:** https://www.clinicasculpte.com.br · **Date:** 2026-06-01
**Note:** Prioritised from a *SERP/index-derived* audit. Items marked 🔍 require on-site/HTML access to confirm before/while fixing.

---

## 🔴 CRITICAL — fix immediately (blocks indexing / AI visibility / trust)

1. **Confirm crawlers aren't being 403-blocked.** 🔍
   - In Google Search Console run **URL Inspection → Test Live URL** on the homepage and 2–3 articles. Check Coverage for "Crawled – currently not indexed" / fetch errors.
   - Test crawler UAs (Googlebot, Bingbot, GPTBot, PerplexityBot, ClaudeBot, Google-Extended) against the WAF/Cloudflare rules. **Allowlist legitimate search & AI bots.**
   - *Why:* the site currently 403s non-browser requests; if that includes search/AI bots, nothing else matters.

2. **Delete the default `/ola-mundo/` post.** Unpublish → return 410 (or 301 to a relevant page) → resubmit sitemap. *Effort: 5 min.*

3. **Verify `robots.txt` and `sitemap.xml` return 200** and are submitted to GSC + Bing Webmaster Tools. 🔍 Ensure robots allows AI bots if AI visibility is desired.

4. **Measure Core Web Vitals.** Configure `GOOGLE_API_KEY`, then `python3 scripts/pagespeed_check.py https://clinicasculpte.com.br -s both`, or run PageSpeed Insights in-browser. Fix LCP/CLS issues found. 🔍

---

## 🟠 HIGH — within 1 week (significant ranking impact)

5. **Per-article YMYL/E-E-A-T pass on all drug/weight-loss content.** 🔍 Add to each: named physician byline + CRM, "Revisado por Dr. … (CRM)," `datePublished`/`dateModified`, references to ANVISA/bula/peer-reviewed sources, and a medical disclaimer.

6. **Implement structured data** (JSON-LD): `MedicalClinic` + `LocalBusiness` (NAP, geo, hours, `priceRange`, `sameAs`), `Physician` for each clinician, `MedicalWebPage`/`Article` with `author`+`reviewedBy` on articles, `FAQPage` on question-style posts, `BreadcrumbList`. Validate in Rich Results Test.

7. **Trim over-length title tags** (≤ 60 chars, keyword front-loaded). Specific offenders: lipo-enzimatica, mounjaro-quanto-tempo, tirzepatida-efeitos-colaterais, semaglutida-interacoes-medicamentosas, tirzepatida-caneta-aplicadora.

8. **Review transactional drug-price content** ("onde comprar barato", "preço e onde comprar"). 🔍 Reframe toward medical guidance + supervised-treatment CTAs to protect YMYL trust and avoid policy issues; keep the informational value, drop the price-shopping angle.

9. **Optimise Google Business Profile.** 🔍 Verify ownership, correct category (Medical clinic / Nutritionist), complete services, photos, hours, and website link; start a review-generation flow.

---

## 🟡 MEDIUM — within 1 month

10. **NAP consistency sweep** across Doctoralia, doutor.net.br, RankLevel, CNES, GBP — byte-for-byte identical name/address/phone. 🔍

11. **Image optimisation** — WebP/AVIF, explicit width/height (CLS), descriptive Portuguese alt text, lazy-loading. 🔍

12. **Standardise URL taxonomy** — use `/servicos/...` for *new* service pages (Portuguese, consistent). 301 only if migrating existing `/services/...` URLs. 🔍

13. **Add `llms.txt`** summarising the clinic, services, location, and key article URLs to aid AI-search citation.

14. **Internal linking** — link the GLP-1 article cluster to the relevant service/consultation pages and to each other (hub-and-spoke), driving authority to conversion pages. 🔍

15. **Meta descriptions** — confirm each indexed page has a unique, compelling, ≤155-char description with a CTA. 🔍

---

## 🟢 LOW — backlog

16. Add `FAQPage`-backed FAQ blocks to top service pages.
17. Build topical hub/pillar pages ("Emagrecimento com GLP-1", "Longevidade") linking the cluster.
18. Pursue authoritative health/local backlinks (medical associations, local press, partner clinics).
19. Add breadcrumb UI navigation.
20. Set up SEO drift baseline (`scripts/drift_baseline.py`) once the site is crawlable, to catch future regressions.

---

## Re-run checklist (to complete the un-assessed sections)
- [ ] Allowlist this region/UA in the WAF **or** run the audit from a Brazil-reachable, unrestricted-network environment.
- [ ] Set `GOOGLE_API_KEY` for PageSpeed + CrUX field data.
- [ ] Then re-run: technical (robots/sitemap/canonicals/headers), schema detection, performance, images, and internal-linking analysis.
