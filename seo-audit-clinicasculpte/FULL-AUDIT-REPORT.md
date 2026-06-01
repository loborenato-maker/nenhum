# Full SEO Audit — Clínica Sculpté

**Site:** https://www.clinicasculpte.com.br
**Audit date:** 2026-06-01
**Auditor:** Claude Code (seo-audit skill)
**Business type detected:** Local Service — Healthcare / Medical Aesthetics clinic (brick-and-mortar, single location, YMYL)

---

## ⚠️ Important: Audit Scope & Data-Access Limitation

A *full technical crawl could not be performed* from this environment. Two independent blocks applied:

1. **Environment network policy** — the execution container is on a strict allowlist; all outbound hosts except Google APIs return "Host not in allowlist."
2. **Site WAF / geo-block** — `clinicasculpte.com.br` returns **HTTP 403** to every non-browser request (homepage, `robots.txt`, `sitemap.xml`), including via Anthropic's WebFetch proxy and the Wayback Machine. This is consistent with a Cloudflare-style bot/geo filter that blocks non-Brazilian IPs.
3. **PageSpeed/CrUX** — reachable, but the keyless Google quota was exhausted (HTTP 429) and no `GOOGLE_API_KEY` is configured, so no lab or field Core Web Vitals could be retrieved.

**What this report IS based on:** Google's live search index (real indexed title tags, the discoverable URL inventory, content topics, snippets) plus third-party directory/citation data (Doctoralia, doutor.net.br, RankLevel, CNPJ registry).

**What could NOT be assessed** (marked *Not Assessable* below — no scores invented): Core Web Vitals, raw HTML structure, `robots.txt`/`sitemap.xml` contents, schema/JSON-LD presence, image alt text, security headers, canonical tags, internal-linking graph, and JS rendering.

> To complete the un-assessed sections, re-run this audit either (a) from an environment whose network policy allows the site, (b) after temporarily allowlisting the crawler/WebFetch user-agent or this region in the WAF, or (c) configure a `GOOGLE_API_KEY` so PageSpeed/CrUX field data can be pulled (Google fetches from its own servers and bypasses the geo-block).

---

## Executive Summary

Clínica Sculpté is a **longevity, weight-loss and medical-aesthetics clinic** in Jardim Paulista, São Paulo, founded by **Dr. Renato Lobo (USP-trained nutrologist)**. The site is built on **WordPress** and runs an active content-marketing engine targeting high-volume Brazilian weight-loss-drug queries (Ozempic, Mounjaro, semaglutida, tirzepatida).

The strategy is sound and the topical focus is commercially smart, but from the indexable surface there are clear hygiene, E-E-A-T, and architecture issues worth fixing — plus a hard accessibility problem: **if a WAF is 403-ing legitimate crawlers, indexing and AI-citation can be actively suppressed.**

### Provisional SEO Health Score: **Not fully scorable** (partial estimate ~ **62/100**, low confidence)
Scored only on assessable categories (on-page, content strategy, local signals, architecture). Performance, schema, technical and image categories are excluded for lack of data, so treat 62 as directional only.

### Top 5 Critical Issues
1. **Crawler 403 / possible bot-or-geo block.** The site returns 403 to non-browser agents. If this also hits Googlebot, Bingbot, GPTBot, PerplexityBot, or ClaudeBot it will throttle organic indexing and *eliminate* AI-search visibility. **Verify in Google Search Console (Coverage + URL Inspection / live test) immediately.**
2. **Default WordPress "Olá, mundo!" post is indexed** (`/ola-mundo/`). A live, indexed "Hello World" placeholder signals an unmaintained site and wastes crawl budget. Delete (410) or unpublish + redirect.
3. **YMYL medical content lacks verifiable on-page E-E-A-T at scale.** Dozens of articles about prescription drugs (semaglutida, tirzepatida) are YMYL. Google demands clear author identity (named physician + CRM), medical review, dates, and citations on each. Cannot confirm these are present — must be audited per-article.
4. **Could not verify `sitemap.xml` / `robots.txt`.** For a content site this size, a missing or unreachable sitemap directly hurts discovery. Confirm they exist, return 200, and are submitted to GSC + Bing Webmaster Tools.
5. **Core Web Vitals unknown.** No field or lab data available. WordPress + heavy aesthetic imagery is a classic LCP/CLS risk. Must be measured.

### Top 5 Quick Wins
1. **Delete `/ola-mundo/`** and resubmit sitemap — 5 minutes, removes an embarrassing trust signal.
2. **Trim over-length blog titles** (several run 75–90 chars and truncate in the SERP) to ≤ 60 chars with the keyword front-loaded.
3. **Add `MedicalClinic` + `Physician` + `LocalBusiness` JSON-LD** with NAP, geo, hours, and `sameAs` (Doctoralia, Instagram, GBP). High impact for local + rich results.
4. **Publish/confirm an `llms.txt`** and ensure AI crawlers are allowed — the clinic's GLP-1 content is exactly what users ask ChatGPT/Perplexity about.
5. **Standardise URL taxonomy** — services live under English `/services/...` while the site is Portuguese; new service pages should use `/servicos/...` (don't break existing URLs without 301s).

---

## 1. Technical SEO — *Mostly Not Assessable*

| Check | Status | Notes |
|-------|--------|-------|
| Crawlability (crawler access) | 🔴 **Risk** | Server returns **403** to non-browser UAs. Must confirm Googlebot is allowed via GSC live test. |
| `robots.txt` | ⚪ Not Assessable | Returned 403 to audit; verify it returns 200 and references the sitemap. |
| `sitemap.xml` | ⚪ Not Assessable | Could not fetch. Confirm presence + GSC submission. |
| Canonical tags | ⚪ Not Assessable | Requires HTML. |
| HTTPS | 🟢 OK | Site served over HTTPS; `www` is the canonical host (homepage resolves to `www`). |
| Security headers | ⚪ Not Assessable | Requires response headers. |
| Core Web Vitals | ⚪ Not Assessable | No CrUX/PSI data (no API key, quota exhausted). |
| `www` vs non-`www` | 🟡 Check | Both `www` and apex resolve; confirm one 301-redirects to the other (homepage canonical appears to be `www`). |

**Platform:** WordPress (confirmed by `/ola-mundo/` default post, `/services/` CPT structure, and post-slug permalinks).

---

## 2. Content Quality & E-E-A-T

**Strengths**
- **Clear topical authority play** around weight-loss pharmacology — a high-demand, high-intent cluster in Brazil.
- **Real author/credibility anchor:** Dr. Renato Lobo (USP, nutrologia, "+5.000 pacientes"), with a dedicated `/quem-somos/` and `/corpo-clinico/` (clinical team) page — good E-E-A-T scaffolding.
- **Active publishing cadence** (content dated Oct–Nov 2025 in snippets).

**Risks / Issues**
- **YMYL exposure.** Prescription-drug content (semaglutida, tirzepatida, Ozempic, Mounjaro) is maximally scrutinised by Google. Each article needs: named physician byline + CRM, "medically reviewed by," publish/update dates, references to primary sources (ANVISA, bulas, peer-reviewed studies), and clear disclaimers.
- **Potential thin/affiliate-style intent.** Titles like "Mounjaro preço e onde comprar: guia prático para não pagar caro" and "Semaglutida preço no Brasil… onde comprar barato" lean transactional/price-shopping on prescription drugs — reputationally and policy-sensitive for a medical brand. Review against Google medical/Your-Money-Your-Life and ad policies.
- **"É possível perder 10kg em 1 mês?"** and similar — ensure claims are medically defensible to avoid YMYL trust penalties.
- **Default content not cleaned up** (`/ola-mundo/`).

---

## 3. On-Page SEO

**Title tags observed in the SERP (real on-page data):**

| Page | Indexed Title | Length | Verdict |
|------|---------------|-------:|---------|
| Homepage | Clínica de Longevidade, Emagrecimento e Nutrologia SP Sculpté | ~58 | 🟢 Good — keyword-led, brand at end |
| Lipo enzimática | Lipo enzimática: saiba como esse método pode transformar seu corpo rapidamente | ~78 | 🔴 Truncates |
| Mounjaro tempo | Mounjaro quanto tempo para fazer efeito: descubra quando notar resultados | ~73 | 🔴 Truncates |
| Tirzepatida efeitos | Tirzepatida efeitos colaterais: o que esperar e como lidar com eles no dia a dia | ~80 | 🔴 Truncates |
| Semaglutida interações | Semaglutida interações medicamentosas: riscos e cuidados essenciais para seu uso | ~80 | 🔴 Truncates |
| /ola-mundo/ | Olá, mundo! – Clínica Sculpté | — | 🔴 Delete |

**Pattern:** Blog titles are benefit-rich but **consistently exceed ~60 characters and truncate**. Keep the primary keyword in the first 60 chars (it is — good) but trim the trailing clause.

**Heading structure, meta descriptions, internal linking:** ⚪ Not Assessable (require HTML).

---

## 4. Schema / Structured Data — *Not Assessable*

Could not inspect HTML/JSON-LD. Given the business, the following are **expected and should be implemented/verified**:
- `MedicalClinic` (or `MedicalBusiness`) with `name`, `address` (PostalAddress), `geo`, `telephone`, `openingHoursSpecification`, `priceRange`, `sameAs`.
- `Physician` for Dr. Renato Lobo and each clinician on `/corpo-clinico/`.
- `MedicalWebPage` / `Article` with `author` (Physician) + `reviewedBy` + `datePublished`/`dateModified` on the drug-education articles (strong YMYL + AI-citation signal).
- `FAQPage` on the many question-style posts ("quanto tempo para fazer efeito", "é possível perder 10kg…").
- `BreadcrumbList`.

---

## 5. Performance (Core Web Vitals) — *Not Assessable*

No CrUX field data or PSI lab run obtainable (no API key; keyless quota exhausted). **Action:** configure `GOOGLE_API_KEY` and re-run `pagespeed_check.py`, or use PageSpeed Insights in a browser. WordPress + image-heavy aesthetic pages are a typical LCP/CLS risk — prioritise measuring.

---

## 6. Images — *Not Assessable*

Alt text, formats (WebP/AVIF), sizing, and lazy-loading require HTML/asset access. For an aesthetics clinic, before/after and procedure imagery is heavy — strong likelihood of optimisation opportunities. Audit once crawlable.

---

## 7. AI Search Readiness (GEO)

- **Topical fit for AI search is excellent** — GLP-1 / weight-loss questions are among the most-asked queries on ChatGPT and Perplexity. This content *should* be highly citable.
- **But the 403/bot-block is the dominant risk:** if `GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`, `Bingbot`/`OAI-SearchBot` are blocked at the WAF, the clinic earns **zero** AI-search visibility regardless of content quality.
- **Citability levers to add:** per-article author identity + medical review + dates + sourced claims; concise definitional/answer passages near the top of each article; `FAQPage` schema; `llms.txt`.

---

## 8. Local SEO

Strong local foundation, verifiable from third-party citations:

- **NAP:** Rua Bento de Andrade, 289 — Jardim Paulista, São Paulo/SP, CEP 04503-011 · **(11) 93925-8411** · Mon–Fri 08:00–20:00.
- **Legal entity:** SCULPTE CLINICA MEDICA LTDA — CNPJ 47.215.883/0001-10.
- **Existing citations:** Doctoralia, doutor.net.br, RankLevel, CNES/DataSUS, cnpj.biz — a reasonable citation base.
- **Reviews:** positive patient testimonials surfaced (clinic site + Doctoralia).

**Actions:** verify/optimise Google Business Profile (category: *Medical clinic / Nutritionist / Weight loss service*), ensure NAP is byte-for-byte consistent across all citations, add LocalBusiness schema, build a review-generation flow, and confirm the GBP links to the site.

---

## Appendix A — Indexed URL Inventory (discovered via search)

**Core pages**
- `/` — Homepage
- `/quem-somos/`
- `/corpo-clinico/`
- `/3s-shape-slim-sculpte/` (proprietary program)
- `/services/medicina-estetica-e-dermatologia/`
- `/services/medicina-regenerativa/`

**Content / blog (weight-loss & GLP-1 cluster)**
- `/lipo-enzimatica/`
- `/acompanhamento-medico-para-emagrecer/`
- `/acompanhamento-nutricional-medico/`
- `/exames-para-emagrecimento/`
- `/perder-10kg-em-1-mes/`
- `/ozempic-aplicacao-correta/`
- `/mounjaro-quanto-tempo-para-fazer-efeito/`
- `/mounjaro-preco-e-onde-comprar/`
- `/tirzepatida-caneta-aplicadora/`
- `/tirzepatida-efeitos-colaterais/`
- `/tirzepatida-seguranca-uso/`
- `/semaglutida-efeitos-colaterais/`
- `/semaglutida-preco-no-brasil/`
- `/semaglutida-contraindicacoes/`
- `/semaglutida-interacoes-medicamentosas/`

**Hygiene**
- `/ola-mundo/` — ⚠️ default WordPress "Hello World" post (delete)

*This inventory is a discovered subset, not the full sitemap (which could not be fetched).*
