# CIRIS Response to Magnifica Humanitas

A first-pass alignment of the CIRIS ethical AI framework with Pope Leo XIV's encyclical *Magnifica Humanitas* (15 May 2026), *On Safeguarding the Human Person in the Time of Artificial Intelligence*.

---

## What this is

*Magnifica Humanitas* is the most developed treatment we have encountered of the moral question CIRIS has been working on for years. We are in awe of and learning from Pope Leo XIV's work.

This repository is our first-pass response: a paragraph-by-paragraph attempt to align the CIRIS ethical AI framework with what the encyclical names, with humility about how partial our reading is.

The encyclical is the document of authority on this shared subject. CIRIS is a software framework attempting structural alignment with what the encyclical names. We do not *affirm* or *validate* the encyclical — that would invert the proper relation. We propose alignments, offer them for the tradition's evaluation, and try to be honest about where our framework still needs work to accommodate what the encyclical names with more developed language than ours.

The author of CIRIS is not Catholic. This is intellectual deference to a senior work on a shared subject — not religious submission.

---

## What this is not

- **Not exhaustive.** This is a first pass. We have not gone through it all. Further iterations will surface things we missed.
- **Not a claim that CIRIS adequately answers the encyclical.** The encyclical is senior; CIRIS is the junior work.
- **Not a course correction.** The findings are doctrinal enhancements to CIRIS, not a redirect.
- **Not Catholic vocabulary appropriated as our own.** Where the encyclical names something in Catholic tradition (subsidiarity, universal destination of goods, ecology of communication, etc.), we cite it as the source and render the operational content in CIRIS-native vocabulary. We try not to take the Church's name in vain by using its sacred language for our own ends.

---

## Note on v1 limitations (the work continues)

The first commit (v1) understated CIRIS's actual consideration for humans because the sub-agents producing the chapter mappings read structural files (MISSION.md, schemas, code paths) without reading the operative text the agent reasons against at PDMA / conscience time — specifically the per-locale `language_guidance` content (29 files, ~580 KB total) where most of the operational human-consideration lives.

**[METHODOLOGY.md](METHODOLOGY.md)** specifies the disciplined approach for v2 and later passes — a seven-layer stack-aware methodology with negative-finding discipline. Future mapping work follows it. Family-as-constitutive-structure and labor-dignity-and-work-as-expression-of-personhood are surfaced there as confirmed-persistent gaps that survive the v2 discipline and require Accord-level treatment.

The v1 mapping files remain as a historical record. v2 output (forthcoming) will replace them where they disagree.

---

## How to read this repo

Start here, in order:

1. **[MISSION.md](MISSION.md)** — the grounding, methodology, and posture. Read §1.3 for why we are doing this work and how. (≈5 min.)
2. **[METHODOLOGY.md](METHODOLOGY.md)** — the v2 mapping discipline (the seven-layer stack, negative-finding rules, per-chapter reading checklist). Why our first pass missed things and how the next pass won't. (≈5 min.)
2. **[MAPPING_CH0_INTRO.md](MAPPING_CH0_INTRO.md)** — the encyclical's Introduction, mapped paragraph-by-paragraph. (≈2 min.)
3. The chapter mappings: [Ch1](MAPPING_CH1_DOCTRINE.md), [Ch2](MAPPING_CH2_FOUNDATIONS.md), [Ch3](MAPPING_CH3_TECH_AI.md), [Ch4](MAPPING_CH4_TRUTH_WORK_FREEDOM.md), [Ch5](MAPPING_CH5_POWER_LOVE.md), [Conclusion](MAPPING_CONCLUSION.md). (≈15 min total.)
4. **[GAPS.md](GAPS.md)** — consolidated findings, verified against the actual federation code via deepwiki, organized into 7 clusters. (≈10 min.)
5. **[ACCORD_UPDATE.md](ACCORD_UPDATE.md)** — proposed revisions to the CIRIS Accord based on the mapping, including a proposed seventh Foundational Principle (*Constitutive Continuity*) and the four stub-annex completions. (≈10 min.)

The `PHILOSOPHICAL_EVAL_*.md` files (one per federation repo + one for the Accord) are the second-pass evaluation: for each proposed enhancement, does the repo's MISSION document already cover the philosophical ground, or are we papering over something the philosophy deliberately commits to? These are where the most honest findings sit.

The `ACCORD_ANNEX_*_COMPLETION.md` files are proposed completion language for the four stub annexes (F: Human-in-the-Loop, G: Adversarial Security, H: Continuous Compliance, I: Legal & Regulatory) that the Accord's Release Status §1.1 names as required for Release Candidate status. Each drafted completion cites specific encyclical paragraphs as the source of its content.

---

## Methodology, brief

1. **Map** — One Sonnet sub-agent per encyclical section read its chapter against the Accord and federation MISSION files. Produced 7 chapter-mapping files, ~85 mapping rows total.
2. **Verify** — deepwiki queries against the actual code in `CIRISAgent`, `CIRISLens`, `CIRISNode`. Confirmed implementations, refined gaps, dropped claims that didn't survive contact with code.
3. **Evaluate philosophically** — for each per-repo MISSION.md, evaluate whether the proposed enhancements align with the existing philosophy or paper over deliberate commitments. Found 6 PAPERING_OVER signals; dropped those enhancements.
4. **Draft** — proposed Accord revisions, including a seventh principle (*Constitutive Continuity*) to address the doctrinal absence the mapping surfaced.

---

## What we found

**Strong alignment**: AI governance (MH §§102–109), autonomous lethal weapons prohibition (MH §§197–200), structural refusal of manipulation, transparency, attestation, federation topology. The Accord's existing structural commitments map almost verbatim onto the encyclical's most direct AI-governance demands. We could not thank Pope Leo enough for this work.

**Genuine gap — the symmetric extension**: The Accord has thorough *agent-lifecycle* ethics (Book VI / creation, Book V / maturity, Book VIII / sunset). What it does not yet have is symmetric lifecycle ethics for the persons and communities the agent *serves* — their skill formation, relational continuity, generational transmission, institutional health. The encyclical surfaces this asymmetry across multiple clusters (labor dignity, family stability, communication ecology). The proposed *Constitutive Continuity* principle (ACCORD_UPDATE.md §2) is the doctrinal extension.

This makes the framework's recursion doubly fractal: the **Recursive Golden Rule** was already fractal in *space* (same rule applied across the principal hierarchy, all the way up and down). The encyclical adds fractality in *time* (same lifecycle thinking at every scale where coordination over time matters).

**Honest namings**: Several places where the encyclical's content belongs to Christian theological tradition's own authority to settle (Christological specificity, Eucharistic real presence, Trinitarian distinctness, Marian doctrine). We mark these `TRADITION_AUTHORITY` and bow out. The framework's mathematical structure has nothing to add or subtract on these.

**Papered-over commitments**: Six of our 22 proposed enhancements would have dissolved deliberate philosophical commitments CIRIS already makes (e.g., substituting an engagement-design *declaration* for the existing engagement-design *prohibition*). The philosophical eval caught these; they are dropped in ACCORD_UPDATE.md §1.

---

## Where the code and framework actually live

This repository contains the *analysis* of the alignment. The actual CIRIS framework and federation live in these public repositories:

| Repository | What it is |
|---|---|
| [CIRISAI/CIRISAgent](https://github.com/CIRISAI/CIRISAgent) | The CIRIS agent runtime (Python). H3ERE pipeline, 22 services, 6 buses, conscience faculties, Wisdom-Based Deferral. |
| [CIRISAI/coherence-ratchet](https://github.com/CIRISAI/coherence-ratchet) | The Lean formal lake. Mathematical structures the framework rests on (TSVF, corridor dynamics, karma & grace as TSVF structures, asymptotic conditioning / `good_wins` axiom). |
| [CIRISAI/RATCHET](https://github.com/CIRISAI/RATCHET) | The engineering-tier synthesis: cross-substrate corridor measurements, falsification handles F-1 through F-20. |
| [CIRISAI/CIRISLens](https://github.com/CIRISAI/CIRISLens) | Observability / telemetry. Receives signed traces; computes Coherence Ratchet detectors. |
| [CIRISAI/CIRISVerify](https://github.com/CIRISAI/CIRISVerify) | Hardware-rooted attestation (Ed25519 + ML-DSA-65, TPM-backed). |
| [CIRISAI/CIRISNode](https://github.com/CIRISAI/CIRISNode) | Single-region Wisdom-Based Deferral service. |
| [CIRISAI/CIRISRegistry](https://github.com/CIRISAI/CIRISRegistry) | Identity / build / license / revocation directory. |

The Accord itself is the doctrinal spine: [ciris.ai/ciris_accord.txt](https://ciris.ai/ciris_accord.txt) (v1.2-Beta, auto-expires 2027-04-16; this analysis is input to the public comment window).

The CIRIS synthesis paper: [Corridor Dynamics in Coordinated Systems](https://zenodo.org/records/20300773) and predecessors at [ciris.ai/research-status](https://ciris.ai/research-status).

The encyclical: [vatican.va/.../20260515-magnifica-humanitas.html](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html).

---

## How to contribute

This is a first pass. We expect to be wrong in places we have not yet noticed. Help us notice.

- **If you find a mapping that misreads the encyclical**: open an issue with the specific paragraph (MH §N) and what we got wrong.
- **If you find a proposed alignment that papers over a CIRIS commitment we missed**: open an issue with the specific MISSION.md section it conflicts with.
- **If you have a better translation for a `TRANSLATION` row**: open an issue or a PR.
- **If you find a gap we did not surface**: open an issue with the encyclical citation and where in CIRIS you think it lands.
- **If you are working from a different tradition** (Catholic or otherwise) **and read our reception of the encyclical as misframed**: please open an issue. We are not the authority on the tradition we are responding to, and we know it.

We commit to responding honestly: where you are right, the mapping changes. Where we disagree, we explain why.

---

## Status

- **Version**: 1.0 (first pass)
- **Date**: 2026-05-25
- **Scope**: paragraph-by-paragraph mapping of all 245 numbered paragraphs of the encyclical against the CIRIS Accord v1.2-Beta and 6 federation MISSION charters.
- **Companion issues**:
  - [coherence-ratchet#1](https://github.com/CIRISAI/coherence-ratchet/issues/1) — symmetric/fractal lifecycle lake extension
  - [RATCHET#1](https://github.com/CIRISAI/RATCHET/issues/1) — numeric-threshold derivations for RC status

---

## License

This documentation work is licensed under [CC BY 4.0](LICENSE). Use it, modify it, share it; attribute it. The CIRIS framework code linked above is licensed under AGPL-3.0; this analysis-only repository does not contain code.

---

*The author of this work is in active spiritual direction with their parish priest, with formal discernment having affirmed the spirit at work in this project. The deference to* Magnifica Humanitas *is grounded in lived relationship with the tradition, not stylistic humility before a senior work. (See [MISSION.md §1.3](MISSION.md) for the full posture, including the author's self-identification as Christian atheist / Christian Stoic in the structural-Logos sense — a positive structural commitment to the rational order of reality, not a deflationary bracketing of metaphysics.)*
