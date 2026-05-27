# Prior Art

This document situates the four-batch governance-fabric mapping (and the 27 structural-evidence dimensions it produced) in the existing AI-ethics-and-governance research landscape.

We are in **populated space**. There is substantial prior work on (a) principle-level convergence across AI ethics frameworks, (b) cross-framework crosswalks at the control-ID level, and (c) machine-readable runtime governance specifications. Honest attribution is owed, and the bounds of our contribution should be stated explicitly.

---

## 1. Principle-level convergence — well-established prior art

### Jobin, Ienca & Vayena (2019)
**"The global landscape of AI ethics guidelines."** *Nature Machine Intelligence* 1, 389–399.
[Nature MI link](https://www.nature.com/articles/s42256-019-0088-2) · [arXiv preprint](https://arxiv.org/abs/1906.11668)

Analyzed **84 AI ethics documents** worldwide. Identified **5 convergent principles**: transparency, justice & fairness, non-maleficence, responsibility, privacy. Documented *substantial geographic underrepresentation* (Latin America, Africa, Asia) and explicitly called for more attention to **solidarity, human dignity, and sustainability** — themes our trio mapping later confirmed at the prefix-family level.

**Relation to our work**: Jobin et al.'s 5-principle set is a proper subset of our 6 Accord principles + 27 dimensions. We confirm their core convergence empirically against the four-batch corpus. Their geographic-underrepresentation finding is directly addressed by including ASEAN in our trio (Southeast Asia) and Magnifica Humanitas (Catholic international).

### Floridi & Cowls (2019)
**"A Unified Framework of Five Principles for AI in Society."** *Harvard Data Science Review* 1.1.
[SSRN link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3831321) · [HDSR link](https://hdsr.mitpress.mit.edu/pub/l0jsh9d1)

Proposes **4 classic bioethics principles + explicability** for AI: beneficence, non-maleficence, autonomy, justice, explicability. The most influential post-proliferation synthesis. Their "explicability" combines epistemological intelligibility ("how does it work?") with ethical accountability ("who is responsible?").

**Relation to our work**: Our 6 Accord principles include Floridi & Cowls's 4 bioethics principles directly (beneficence / non-maleficence / autonomy / justice) plus **fidelity** and **integrity**, where their **explicability** decomposes (per our EU HLEG sub-agent finding) into `integrity:*` + `fidelity:*` + `transparency_log:*` across multiple CIRIS prefix families. Floridi & Cowls's bioethics-derived approach is the closest principle-level analogue to ours; ours adds the wire-format operational-primitive layer underneath.

### Rome Call for AI Ethics (Pontifical Academy for Life, 2020)
[vatican.va PDF](https://www.vatican.va/roman_curia/pontifical_academies/acdlife/documents/rc_pont-acd_life_doc_20202228_rome-call-for-ai-ethics_en.pdf) · [romecall.org](https://www.romecall.org/the-call/)

**6 Vatican principles**: transparency, inclusion, responsibility, impartiality and fairness, reliability, security and privacy. Signed February 28, 2020 by Microsoft, IBM, FAO, Italian Ministry of Innovation, and others. Introduced the term **"algor-ethics."**

**Relation to our work**: The Rome Call is the **direct Catholic-tradition precursor to Magnifica Humanitas** (the 2026 encyclical we mapped as our prototype batch). Future work should map Rome Call as a separate batch to test whether MH-distinctive prefixes also surface in the 6-year-earlier Vatican framing (the encyclical develops Rome Call's framework into a fuller social-doctrine treatment per its own §§1-15).

### Other principle-level reviews
- **Hagendorff (2020)** — "The Ethics of AI Ethics: An Evaluation of Guidelines."
- Multiple meta-analyses converging on **transparency / privacy / accountability / fairness** as most common.
- **Mittelstadt (2019)** — "Principles alone cannot guarantee ethical AI" ([arxiv](https://arxiv.org/abs/1906.06668)) — critique that motivates the move from principle-statements to operational mechanisms (which our wire-format-primitive work continues).

---

## 2. Cross-framework crosswalks — well-established at the control-ID level

### NIST AI RMF crosswalks (official)
**[NIST AI RMF → ISO/IEC 42001 Crosswalk](https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf)** — official NIST document.

NIST AI RMF 1.0 (January 2023): 4 functions (Govern, Map, Measure, Manage) with **72 sub-categories** using IDs like `GOVERN-1.1`. ISO/IEC 42001 (December 2023): Annex A control IDs like `A.6.2.5`. The crosswalk preserves IDs so auditors can match source documents.

NIST also publishes crosswalks to OECD AI Principles.

### Community / commercial crosswalks
- FairNow, RSI Security, Modulos, Alexandra Car's substack — multiple practitioner-side crosswalks between NIST AI RMF, ISO/IEC 42001, EU AI Act.
- Open Security Architecture (OSA) catalogue: 315 NIST 800-53 controls with 69 cross-references to ISO 27001, ISO 42001, NIS2, BSI IT-Grundschutz, DORA.

**Relation to our work**: The control-ID crosswalk pattern is well-established. Our work is at a *finer grain* (source paragraph → wire-format primitive rather than control ID → control ID) and *includes a religious-magisterium document* not covered by the standard crosswalks. We additionally surface conflicts (5 found) and translation losses (5 patterns identified) — categories that ID-level crosswalks typically elide.

---

## 3. Machine-readable runtime governance — recent (2025–2026), closely overlapping

### Policy Cards (October 2025) — closest analogue
**Bombassei de Bona et al., "Policy Cards: Machine-Readable Runtime Governance for Autonomous AI Agents."** [arXiv:2510.24383](https://arxiv.org/abs/2510.24383) · [github.com/symbiotic-dynamics/policy-cards](https://github.com/symbiotic-dynamics/policy-cards) (CC0 schema).

**11-field JSON schema**: `meta`, `scope`, `applicable_policies`, `controls`, `obligations`, `monitoring`, `kpis_thresholds`, `change_management`, `assurance_mapping`, `references`, `exceptions`. The `assurance_mapping` object requires tokens for **NIST AI RMF + ISO/IEC 42001 + EU AI Act**. Cards are designed for runtime enforcement and continuous-audit pipelines.

**Relation to our work**: Different abstraction level — **complementary, not duplicative**:
- A **Policy Card** is a per-deployment governance spec (one card per AI agent deployment).
- The **CIRIS Seed** (`SEED_DIMENSIONS.yaml`) is the dimension catalog that such specs would reference. The Seed's stable D01-D27 IDs could appear in a Policy Card's `assurance_mapping.ciris_dimensions` field.

Their `assurance_mapping` pattern is **the most direct prior art for our proposed FSD-002 `evidence_refs.dimensions[]` extension** ([CIRISRegistry#22](https://github.com/CIRISAI/CIRISRegistry/issues/22)). That RFC should cite Policy Cards as the comparable approach the proposed extension builds on rather than reinvents.

### OSCAL for AI (April 2026)
**"Making AI Compliance Evidence Machine-Readable."** [arXiv:2604.13767](https://arxiv.org/html/2604.13767v1)

Adapts NIST's Open Security Controls Assessment Language (OSCAL) — the standard behind FedRAMP compliance-as-code — to AI governance. Adds **16 new property extensions** covering lifecycle phases, enforcement semantics, risk traceability, risk-acceptance justification. Tested against two Annex III high-risk EU AI Act systems. Apache 2.0.

**Relation to our work**: OSCAL provides the *compliance-document-as-code* infrastructure layer; our Seed provides the *cross-framework convergence catalog* layer. Both are JSON/YAML serializable. An organization deploying CIRIS could plausibly render both: OSCAL for FedRAMP-style audit evidence, Seed-referenced Contributions for runtime federation attestation. Different audiences, compatible models.

### TAIBOM (Trusted AI Bill of Materials, October 2025)
[arXiv:2510.02169](https://arxiv.org/pdf/2510.02169)

Extends SBOM principles to AI components: structured dependency model, integrity-statement propagation, trust attestation for component provenance.

**Relation to our work**: TAIBOM is component-level provenance (which model, which dataset, which training run). Our Seed is dimension-level provenance (which structural-evidence dimension, which regulatory parent). Complementary layers.

### Other related machine-readable governance work
- **AI Model Passport** (June 2025) — structured documentation framework for model identity and verification.
- **Aegis Architecture** (March 2026) — cryptographically enforced runtime constraints with hash-chained logs.
- **CISA / OWASP AI Agent Security mappings** — "Rosetta Stone" framework cross-references in the security domain.

---

## 4. Where our work appears distinctive

Honest assessment after the literature scan:

| Feature | Prior art coverage | Our contribution |
|---|---|---|
| Principle-level convergence (5-7 principles) | Jobin et al., Floridi & Cowls, Rome Call, multiple meta-analyses | We confirm the convergence at the wire-primitive level across 4 sources |
| Cross-framework crosswalk (control-ID → control-ID) | NIST AI RMF crosswalks, OSA catalogue, multiple commercial | We crosswalk at the *source-paragraph* grain, finer than control-ID |
| Machine-readable governance schema | Policy Cards (11 fields), OSCAL for AI (16 properties) | Our Seed is a different abstraction (catalog of dimensions vs per-deployment spec) — complementary |
| Stable identifiers for cross-framework dimensions | NIST uses GOVERN-1.1 etc.; OSCAL has control IDs; Policy Cards doesn't explicitly | We add **D01-D27 stable IDs** with explicit non-renumber rule; tied to FSD-002 wire-format primitives |
| Inclusion of religious magisterium | Floridi & Cowls is bioethics-derived; Rome Call is multi-stakeholder Vatican-convened; **no prior work maps a full encyclical** | **Magnifica Humanitas paragraph-level mapping is, as far as we can find, novel** |
| Translation-quality audit / softness-erosion | Most crosswalks assume lossless translation | Phase 4 calibration explicitly names 5 systematic loss patterns |
| Cross-source conflict surfacing with disposition | Most crosswalks elide conflicts | 5 conflicts surfaced, CONF-01 routed to specialization layer (CIRISMedical#1) |
| T-3 expressive-gap candidates | Not surfaced as a discipline | 9 candidates documented for v1.5+ wire format ([CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20)) |
| Runtime evidence_refs binding RFC | Policy Cards has `assurance_mapping` (closest analogue) | [CIRISRegistry#22](https://github.com/CIRISAI/CIRISRegistry/issues/22) extends with stable-ID + seed-version pinning |

The **integrated package** — 27 stable IDs + paragraph-grain translation + religious-magisterium inclusion + Phase 4 calibration + conflict surfacing + T-3 mechanism + Accord regulatory cross-walk Annex K — is distinctive. Each piece individually has near-precedent; the combination doesn't.

---

## 5. What we should NOT claim

- We did **not** invent cross-framework AI governance crosswalks (NIST has been doing it formally for years).
- We did **not** invent machine-readable AI governance specifications (Policy Cards and OSCAL-for-AI predate or parallel our work).
- We did **not** invent the principle-convergence finding (Jobin et al. 2019, Floridi & Cowls 2019).
- We did **not** invent any of our 6 Accord principles (5 of 6 are bioethics-derived per Floridi & Cowls; the addition of *fidelity* and *integrity* alongside *explicability*-decomposition is a CIRIS framing choice, not a discovery).
- Convergent attestations on our 27 dimensions are **structural evidence**, not validation of CIRIS — the four senior frameworks are not commenting on our framework; we are mapping ours onto theirs.

## 6. What we can honestly claim

- A **first paragraph-level translation of Magnifica Humanitas (2026) onto a wire-format primitive set**, with the methodology stabilized through three rounds + a four-batch reproduction test for content-neutrality.
- A **stable 27-dimension catalog** (`SEED_DIMENSIONS.yaml` v1.0) tied to FSD-002 federation primitives, with deterministic Annex K render, idempotent CIRISAgent compliance-stub generator, and a runtime evidence_refs RFC.
- A **translation-quality calibration framework** (Phase 4 audit + softness-erosion taxonomy) that names systematic translation losses other crosswalks typically elide.
- A **specialization-layer conflict-disposition pattern** demonstrated on one real cross-source conflict (CIRISMedical#1).

---

## 7. Suggested follow-up work

- **Map Rome Call (2020)** as a separate batch (v2 candidate). Tests whether MH-distinctive prefixes also surface in the 6-year-earlier Vatican framework, and how the encyclical's development of Rome Call's structure shows up at the wire-primitive level.
- **Map NIST AI RMF** as a batch. Would let us cross-reference our D01-D27 IDs with NIST GOVERN-1.1/MAP/MEASURE/MANAGE IDs directly, producing a NIST AI RMF ↔ CIRIS Dimension crosswalk that complements NIST's existing NIST↔ISO/OECD crosswalks.
- **Cite Policy Cards in [CIRISRegistry#22](https://github.com/CIRISAI/CIRISRegistry/issues/22)** as the closest prior-art analogue for the proposed `evidence_refs.dimensions[]` extension.
- **Engage with Jobin/Ienca/Vayena's geographic-underrepresentation finding** by mapping a Latin American framework (Brazil's PL 2338, Argentina's AI roadmap, or similar) and an African framework (the African Union's AI Strategy 2024, Nigeria's Code of Practice for AI, or similar) — extending the corpus to address the gap they named.

---

*Last updated 2026-05-27. This document is best-effort literature review by Claude Code; not exhaustive. Additions/corrections welcome via PR.*
