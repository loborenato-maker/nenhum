# GEO / AI-Search Analysis — Clínica Sculpté

**Site:** https://www.clinicasculpte.com.br
**Date:** 2026-06-01
**Framework:** GEO = SEO fundamentals applied to AI-search surfaces (per Google's AI optimization guidance — AEO/GEO are rebranded SEO, not a separate discipline).
**Entity in focus:** Dr. Renato Lobo (CRM-SP 181069, USP) + Clínica Sculpté (longevity / weight-loss / medical aesthetics, Jardim Paulista, SP).

---

## ⚠️ Data-Access Note
Direct fetches are blocked: the site returns **HTTP 403 to non-browser requests** (homepage, `robots.txt`, `llms.txt`) from this environment's IP range, and the container network is allowlist-locked. **However, ~20 pages are live in Google's index** — proof that **Googlebot is NOT blocked**; the 403 is an IP/ASN/geo rule catching datacenter/non-BR traffic. This distinction drives the central GEO finding below. Crawler-access for AI bots and `llms.txt`/`robots.txt` contents are therefore **inferred, not directly verified** — confirm via server logs or `curl` from a Brazilian browser/IP.

---

## GEO Readiness Score: **59 / 100** *(moderate; one critical unknown)*

| Criterion | Weight | Score | Notes |
|-----------|-------:|------:|-------|
| Citability | 25% | 15/25 | Question-format titles + ultra-high-demand GLP-1 topics; passage blocks/dates/sources unverifiable |
| Structural readability | 20% | 13/20 | WordPress, likely question-headings; structure not directly inspectable |
| Multi-modal | 15% | 10/15 | Founder YouTube channel + aesthetic imagery; not confirmed embedded in articles |
| Authority & brand signals | 20% | 13/20 | **Strong personal entity**, weak org entity, **no Wikipedia/Reddit** |
| Technical accessibility | 20% | 8/20 | **403 to datacenter crawlers** = likely blocks GPTBot/PerplexityBot; SSR good; no verifiable llms.txt |

---

## 1. Platform Breakdown

| Platform | Est. Readiness | Rationale |
|----------|---------------:|-----------|
| **Google AI Overviews** | 🟢 ~65/100 | Site is indexed → Googlebot access confirmed. GLP-1 queries trigger AIO heavily. Wins ride on ranking + passage quality. *Best near-term opportunity.* |
| **ChatGPT (search)** | 🔴 ~35/100 | ChatGPT leans Wikipedia (47.9%) — **brand has none**. Plus likely GPTBot/OAI-SearchBot 403. Founder press mentions help marginally. |
| **Perplexity** | 🔴 ~30/100 | Perplexity leans Reddit (46.7%) — **zero Reddit presence**. Likely PerplexityBot 403. |
| **Bing Copilot** | 🟡 ~45/100 | Depends on Bing index + IndexNow (unverified). Confirm Bing Webmaster Tools submission. |

> Only ~11% of domains are cited by both ChatGPT and Google AIO for the same query, so these gaps must be closed platform by platform.

---

## 2. AI Crawler Access Status — ⚠️ CRITICAL UNKNOWN

Could not read `robots.txt` (403). Inferred state:

| Crawler | Likely Status | Impact |
|---------|--------------|--------|
| Googlebot / Google-Extended | 🟢 Allowed (pages indexed) | AIO eligible |
| GPTBot, OAI-SearchBot, ChatGPT-User | 🔴 Likely blocked by IP/ASN WAF rule | No ChatGPT ingestion |
| PerplexityBot | 🔴 Likely blocked | No Perplexity ingestion |
| ClaudeBot | 🔴 Likely blocked | No Claude ingestion |
| Bingbot | 🟡 Unknown | Verify in BWT |

**Action #1 (highest impact):** From a Brazilian IP/browser, run `curl -A "GPTBot" https://clinicasculpte.com.br/` and repeat for PerplexityBot, OAI-SearchBot, ClaudeBot, Bingbot. If any return 403, **explicitly allowlist legitimate AI/search bots in the WAF/Cloudflare** (by verified UA + published IP ranges). A geo/ASN rule that blocks all non-BR datacenter traffic will silently exclude every US-hosted AI crawler — the single biggest GEO blocker here.

---

## 3. llms.txt Status
Could not verify (403); assume **absent**. Note: per primary-source evidence (Mueller/Illyés, SE Ranking 300k-domain study), `llms.txt` is **not currently a citation lever** for major AI search — low priority. A ready template is in Appendix A; implement it for completeness, not as a ranking tactic.

---

## 4. Brand Mention Analysis — the GEO heart (mentions correlate 3× > backlinks)

**Personal entity "Dr. Renato Lobo" — STRONG:**
- ✅ **YouTube** — own channel (`UCLsAy3vnRappWzK4P6jj7NQ`) + "ENTREVISTA COMPLETA" + *Pérola Negra Podcast #24*. YouTube mentions are the **single strongest AI-citation correlate (~0.737)**. This is the brand's biggest GEO asset.
- ✅ **TikTok** — featured by Chupim Metropolitana (media outlet).
- ✅ **Press/PR** — Terra.com.br (major BR portal), Esporte News Mundo, Observatório dos Famosos, Drogaraia health blog. Real third-party authority mentions.
- ✅ **LinkedIn** — profile (500+ connections).
- ✅ **Instagram** — @dr.rlobo. ✅ **Facebook** — /dr.rlobo.
- ✅ **Medical directories** — Doctoralia (reviews), Intermedicos, O2Corre, Crossfight, sis-medicos.
- ✅ **Verifiable credential** — CRM-SP 181069, USP, ABRAN, sports-medicine postgrad → excellent E-E-A-T anchor.

**Critical gaps:**
- ❌ **No Wikipedia / Wikidata** entry → directly suppresses ChatGPT citability (Wikipedia = 47.9% of ChatGPT sources).
- ❌ **No Reddit presence** → directly suppresses Perplexity citability (Reddit = 46.7%).
- ⚠️ **Org entity ("Clínica Sculpté") is weaker than the personal entity.** AI systems will recognise the doctor before the clinic. Strengthen the clinic as a distinct entity (Wikidata item, consistent `sameAs`, GBP).

---

## 5. Passage-Level Citability

Indexed titles show **strong query-matching, question-format intent** — ideal for AI extraction:
- "É possível perder 10kg em 1 mês? Médico responde"
- "Mounjaro quanto tempo para fazer efeito"
- "Semaglutida contraindicações" / "interações medicamentosas"

These map exactly to high-volume AI prompts. **But** actual passage structure (the 134–167-word self-contained answer blocks, the 40–60-word direct answer, dates, source citations) **could not be verified**. Recommendation: ensure each article opens with a direct 40–60-word answer, then a 134–167-word quotable block with a specific stat + cited source (ANVISA/bula/study).

---

## 6. Server-Side Rendering
WordPress renders server-side → ✅ good (AI crawlers don't execute JS). The blocker is **access (403), not rendering**. Once crawler access is confirmed, content is ingestible as-is.

---

## 7. Schema Recommendations for AI Discoverability
- `Physician` (Renato Lobo) with `identifier` = CRM-SP 181069, `alumniOf` USP, and `sameAs` → YouTube channel, LinkedIn, Instagram, Doctoralia, drrenatolobo.com.br.
- `MedicalClinic` (Clínica Sculpté) with NAP, geo, hours, `sameAs`.
- `MedicalWebPage` + `author`(Physician) + `reviewedBy` + `datePublished`/`dateModified` on every drug/weight-loss article.
- `FAQPage` on question-format posts.
- `VideoObject` for embedded YouTube interviews (multi-modal boost — 156% higher selection).

---

## 8. Top 5 Highest-Impact Changes
1. **Verify & fix AI-crawler access** (curl-test UAs from BR IP; allowlist GPTBot/OAI-SearchBot/PerplexityBot/ClaudeBot/Bingbot). *Without this, GEO work on ChatGPT/Perplexity is wasted.*
2. **Build Wikipedia/Wikidata presence** for Dr. Renato Lobo (notability is plausible: USP, press coverage, podcasts) → unlocks ChatGPT.
3. **Seed authentic Reddit presence** (Brazilian health/emagrecimento/r/brasil-adjacent communities; expert AMAs, genuine answers) → unlocks Perplexity.
4. **Embed the existing YouTube interviews into relevant articles** + add `VideoObject` schema — leverage the strongest AI signal you already own.
5. **Add per-article direct-answer blocks + author/review/date + sourced stats** (Physician schema with CRM) → boosts Google AIO citability on the high-demand GLP-1 cluster.

---

## 9. Content Reformatting Suggestions (specific)
- **`/perder-10kg-em-1-mes/`** — open with a 40–60-word direct medical answer ("Perder 10 kg em 1 mês é possível em casos específicos e supervisionados, mas…"), then a 134–167-word block citing safe-loss ranges with a source. Add `FAQPage`.
- **`/mounjaro-quanto-tempo-para-fazer-efeito/`** — lead with a one-sentence timeframe answer + a comparison table (week-by-week). Tables raise AI selection.
- **Semaglutida/Tirzepatida cluster** — add a standardized "Pontos-chave" bullet box (3–5 quotable facts with ANVISA/bula citation) near the top of each.
- **All articles** — visible author byline "Dr. Renato Lobo — CRM-SP 181069" + "Atualizado em [date]" + "Revisão médica".

---

## Appendix A — llms.txt Template (low priority)
```
# Clínica Sculpté
> Clínica de longevidade, emagrecimento e nutrologia em Jardim Paulista, São Paulo.
> Fundada pelo Dr. Renato Lobo (CRM-SP 181069, USP). +5.000 pacientes atendidos.

## Sobre
- [Quem somos](https://clinicasculpte.com.br/quem-somos/): A clínica e sua proposta.
- [Corpo Clínico](https://clinicasculpte.com.br/corpo-clinico/): Equipe médica.

## Serviços
- [Medicina Estética e Dermatologia](https://clinicasculpte.com.br/services/medicina-estetica-e-dermatologia/)
- [Medicina Regenerativa](https://clinicasculpte.com.br/services/medicina-regenerativa/)
- [3S Shape Slim Sculpté](https://clinicasculpte.com.br/3s-shape-slim-sculpte/): Programa de emagrecimento.

## Conteúdo de referência (emagrecimento / GLP-1)
- Semaglutida, Tirzepatida, Ozempic, Mounjaro: efeitos, contraindicações, segurança.

## Contato
- Rua Bento de Andrade, 289 — Jardim Paulista, São Paulo/SP, CEP 04503-011
- WhatsApp: (11) 93925-8411 · Seg–Sex 08:00–20:00
```

---
*Scores for citability/structure/multi-modal are constrained by the 403 access block — re-run from a Brazil-reachable, unrestricted environment (or after WAF allowlisting) to verify passage structure, schema, and confirmed crawler access.*
