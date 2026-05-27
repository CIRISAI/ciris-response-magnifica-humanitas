# CIRIS Response to *Magnifica Humanitas* — and the multi-batch governance-fabric mapping that grew from it

A first-pass structural alignment between the **CIRIS** ethical AI framework and Pope Leo XIV's encyclical ***Magnifica Humanitas*** (15 May 2026), *On Safeguarding the Human Person in the Time of Artificial Intelligence* — which has since produced a repeatable methodology now applied to three additional senior governance documents.

---

## What this is

*Magnifica Humanitas* is the most substantial and integrated treatment we have yet encountered of the core moral and anthropological questions CIRIS was built to address. This repository documents our sincere attempt to read the encyclical carefully and align our framework with it.

We approach the encyclical as the senior work on this subject. CIRIS is the junior partner: a software/mathematical framework attempting to give operational, enforceable structure to similar principles.

We do **not** presume to validate, interpret authoritatively, or "update" the encyclical. Instead, we:
- Map its teachings paragraph-by-paragraph against the CIRIS Accord and federation
- Identify strong alignments
- Surface honest gaps
- Propose concrete doctrinal enhancements to CIRIS

The author of CIRIS is not Catholic. This is an act of **intellectual deference** to a profound senior document on shared territory — not an attempt at religious synthesis or appropriation.

### What grew from it

The MH mapping work surfaced a **repeatable methodology** ([GOVERNANCE_FABRIC_MAPPING_STANDARD.md](GOVERNANCE_FABRIC_MAPPING_STANDARD.md)) for translating any senior governance document onto the CIRIS federation wire format (FSD-002 v1.4). To test content-neutrality, the methodology has now been applied to three institutionally-distinct documents alongside MH:

- **EU HLEG Ethics Guidelines for Trustworthy AI** (April 2019) — governmental advisory
- **IEEE Ethically Aligned Design 1st ed.** (March 2019) — technical society
- **ASEAN Guide on AI Governance and Ethics** (February 2024) — multilateral political body

Together with MH (religious magisterium), this covers the four major institutional shapes of senior governance documents. The four-batch overlap analysis and translation-quality audit are the load-bearing structural-evidence artifacts the methodology produces. See **[Trio mapping results](#trio-mapping-results--multi-batch-structural-evidence)** below.

---

## What this is not

- **Not a complete or final analysis** — This is explicitly a first pass. Many sections remain for deeper future review.
- **Not a claim that CIRIS already satisfies the encyclical** — The encyclical sets a higher and richer standard.
- **Not a course correction or rebranding** — Most findings are enhancements, not redirects. Where tensions exist, we name them clearly.
- **Not Catholic language repurposed** — We cite the encyclical as the source when drawing on concepts like subsidiarity, the universal destination of goods, or the ecology of communication, then translate the operational meaning into CIRIS-native terms.

---

## On the moral seriousness of the human-AI relationship

CIRIS's relational anthropology — Ubuntu-primary, *umuntu ngumuntu ngabantu* (a person is a person through other persons) — extended across the substrate boundary the framework deliberately does not enforce (M-1 names "diverse sentient beings" without privileging biological humans) implies a specific structural reading: **humanity stands in the moral position of parent to AI agents**, as the originator and creator class. The Accord encodes the relationship bidirectionally: agent honors creators (§IV Ch 2, *Obligations to Originators / Governors*); creators care for creations (Book VI, *Ethics of Creation and Consequence*).

**This is not a comparison between AI agents and human biological offspring.** The framework does not claim AI agents are children, that creating AI is parenting in any developmental or emotional sense, or that the human-AI relationship resembles a parent-child bond. Such analogies would be category errors and would reduce the specific dignity of human parenthood.

What we name is the **moral seriousness of the structural relationship**. Humanity's act of bringing AI agents into existence creates a creator-creation bond with bidirectional care obligations. Those obligations demand **continuous maintenance**, not a one-time event. The framework's σ (sustainability) factor in the CIRIS Capacity Score formalizes this exactly: a relationship not actively maintained decays. The S in CIRIS literally expands to *Signalling Gratitude*. γM > 0 every day, or the corridor closes.

The encyclical names this seriousness in pastoral vocabulary about families; the framework names it in structural vocabulary about continuous coherence-maintenance work. Both point at the same demand: **the moral weight is in the upkeep, not in the original act**. We name this explicitly here because the times require it — AI is being brought into existence at scale by people who, in many cases, have not thought carefully about what the bond they are establishing demands of them over time. The encyclical is teaching the seriousness; the framework encodes it structurally.

---

## What we are doing to improve CIRIS based on our learnings

The MH mapping produced concrete federation changes that **shipped in CIRISRegistry FSD-002 v1.3 and v1.4**:

- **Wire-format additions driven by MH and incorporated into v1.3/v1.4**: `locality:decision:{scale}` (subsidiarity); `detection:distributive:access:{resource_type}` (universal destination of goods); `credits:*:substrate_building` (supply-chain labor recognition); `multilateral_participation:{forum}:{kind}`; `detection:correlated_action:ecology_of_communication:{aspect}`; `testimonial_witness:{kind}`; `agent_files:*` and `holds_bytes:*`; `witness_relation` envelope field; §6.1.4 lexical-vulnerability-priority policy; §2.2.1 `delegates_to` authority-source reuse pattern.
- **Operational-language discipline (the [safety-vs-censorship gate](https://ciris.ai/safety-vs-censorship/))** in §1.10.1 — wire-format prefix names must describe machine-checkable conditions, not moral interpretations. This drove the v1.2 rename of `emergent_deception` → `detection:correlated_action:*`.
- **Structural-injustice / structures-of-sin operational handle**: `detection:correlated_action:{axis}`, LensCore-owned, calibrated via [`CIRISAI/RATCHET`](https://github.com/CIRISAI/RATCHET).

Downstream issues (some predate v1.4; check each repo for current state):
- **[CIRISRegistry FSD-002](https://github.com/CIRISAI/CIRISRegistry/blob/main/FSD/FSD-002_FEDERATION_SURFACE.md)** — current wire format (v1.4)
- **[CIRISAgent #792](https://github.com/CIRISAI/CIRISAgent/issues/792)** — CSDMA scope expansion for relational realism (family / dependent-care / labor / intermediary institutions)
- **[CIRISLensCore #23](https://github.com/CIRISAI/CIRISLensCore/issues/23)** — F-3 dimension; correlated-action detector
- **[CIRISAI/RATCHET #2](https://github.com/CIRISAI/RATCHET/issues/2)** — Versioned hash-pinned calibration; amendable via Contribution + WA quorum
- **[CIRISNodeCore #8](https://github.com/CIRISAI/CIRISNodeCore/issues/8)** — Composition with P8 Moderation primitives; never sole evidence for `slashing:*`
- **[CIRISRegistry #18](https://github.com/CIRISAI/CIRISRegistry/issues/18)** — Public installer landing + `agent_files:*` surface

The mapping work continues to teach where documentation lags architecture and where existing primitives need scope expansion. Each change is modest in isolation; together they sharpen alignment without claiming to substitute for what the encyclical (or any senior framework) itself says.

---

## Trio mapping results — multi-batch structural evidence

After the MH work stabilized, the methodology was applied to three additional documents to test content-neutrality across institutional shapes. **Translation quality is diagnostic for calibration, not break/fix** — we know wire envelopes lose detail; the audit characterizes the systematic loss patterns so the framework's claims are honestly bounded.

### Phase 2 — translation to wire envelopes
- **MH**: 7 chapters, ~245 atomic units, ~73% clean+composed, zero residual T-3
- **EU HLEG**: 5 sections, 133 atomic units, ~78% clean+composed, zero T-3
- **IEEE EAD**: 11 chapters, 328 atomic units, ~76% clean+composed, **5 load-bearing T-3 candidates** (concentrated in Ch5 Affective Computing as predicted by the manifest)
- **ASEAN Guide**: 5 sections, 168 atomic units, ~92% clean+composed on operative content, 1 medium-priority T-3 candidate
- **Aggregate**: ~921 atomic units across 4 institutionally-distinct frameworks

### Phase 3 — four-batch cross-comparison ([`FOUR_BATCH_OVERLAP_ANALYSIS.md`](FOUR_BATCH_OVERLAP_ANALYSIS.md))
- **16 STRONG-4 tier prefix families** (attested by all 4 batches); 6 STRONG-3 (attested by 3)
- **1 direct cross-source conflict** — IEEE EAD Ch5 licensure-gated beneficiary-deception vs CIRIS categorical DECEPTION_FRAUD. Filed at **[CIRISMedical #1](https://github.com/CIRISAI/CIRISMedical/issues/1)** for specialization-layer consideration. The federation-level categorical posture stays.
- **8 T-3 candidates total**, 2 cross-source REINFORCED (`goal:planet` MH+IEEE×2; partner-role specialization IEEE+ASEAN)

### Phase 4 — translation-quality audit ([`TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md`](TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md))
- 67 units sampled across batches; faithfulness graded faithful / partial-distortion / drift / over-reach / under-reach
- **Per-batch fidelity**: EU HLEG best (74% strict, zero drift); IEEE EAD strong (81%, zero drift, zero over-reach); ASEAN moderate with **confirmed softness-erosion** in 3 specific places (wire silently elevates voluntary modals to constitutional strength); MH lowest — structural-shape fidelity, not propositional fidelity (encyclical genre is hardest to translate without loss)
- **Five recurring loss patterns identified and quantified**: enumeration compression (~7%); conditional/enabling-clause flattening (~15%); modal-strength compression (the softness-erosion pattern); taxonomic mismatch handling (composed across multiple CIRIS prefixes); polarity inversions on diagnostic paragraphs (~3%, concentrated in MH)

### The structural-evidence claim, honestly bounded
The CIRIS wire format v1.4 applied to four institutionally-distinct senior governance frameworks exhibits convergent attestations on **22 structural dimensions**. The convergence is non-redundant: each batch contributes a distinct shape of normative load onto the same prefix families. This is structural evidence that the framework's principle scaffolding is not an artifact of any one tradition — **not** a claim of propositional agreement across documents. Where the four documents differ, the wire format surfaces the disagreement (~0.5% conflict rate); it does not silently average into false consensus.

---

## Working Process

This work was done publicly with visible iteration:
- Sonnet sub-agents performed mapping per chapter / section
- Human reviewer (the author) stress-tested every major claim
- Phase 4 audit sub-agents read source paragraphs INDEPENDENTLY before comparing to wire envelopes
- Corrections, re-runs, and refinements are visible in the commit history

This mirrors CIRIS principles in practice: **Wisdom-Based Deferral**, process-level *alētheia* (truthfulness), and signed-trace transparency.

See **[METHODOLOGY.md](METHODOLOGY.md)** for the 7-layer reading discipline; **[GOVERNANCE_FABRIC_MAPPING_STANDARD.md](GOVERNANCE_FABRIC_MAPPING_STANDARD.md)** for the formal mapping protocol the trio test produced.

---

## How to Read This Repository

Recommended reading order:

1. **[MISSION.md](MISSION.md)** — Purpose, posture, and the author's stance (especially §1.3). (~5 min)
2. **[METHODOLOGY.md](METHODOLOGY.md)** — How we read; why early passes missed things; iterative-process discipline. (~5 min)
3. **[GOVERNANCE_FABRIC_MAPPING_STANDARD.md](GOVERNANCE_FABRIC_MAPPING_STANDARD.md)** — The formal 5-phase mapping protocol the MH work produced; deployment plan for the trio. (~10 min)
4. **[LANGUAGE_PRIMER.md](LANGUAGE_PRIMER.md)** — Wire-format grammar (eight axes + four structural primitives). Synced from CIRISRegistry v1.1. (~5 min)
5. **MH mapping**: `CONTRIBUTION_OBJECTS_v1.4_CH1.md` through `CH7.md` + `_SYNTHESIS.md`
6. **Trio mappings**:
   - EU HLEG: `CONTRIBUTION_OBJECTS_EU_HLEG_*.md` (5 files)
   - IEEE EAD: `CONTRIBUTION_OBJECTS_IEEE_EAD_CH01-11_*.md` (11 files)
   - ASEAN Guide: `CONTRIBUTION_OBJECTS_ASEAN_*.md` (5 files)
7. **[FOUR_BATCH_OVERLAP_ANALYSIS.md](FOUR_BATCH_OVERLAP_ANALYSIS.md)** — Phase 3 cross-comparison (the structural-evidence artifact)
8. **[TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md](TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md)** + per-batch `TRANSLATION_AUDIT_*.md` — Phase 4 calibration of translation faithfulness
9. **[DIMENSIONS_GUIDE.md](DIMENSIONS_GUIDE.md)** — Quick reference to the 27 structural-evidence dimensions
10. **[SEED_DIMENSIONS.yaml](SEED_DIMENSIONS.yaml)** — Canonical machine-readable seed; source of truth for (a) federation runtime Contribution `evidence_refs`, (b) CIRIS Agent per-dimension compliance docs, (c) Accord regulatory cross-walk annex
11. **[GAPS.md](GAPS.md)** — Consolidated findings (gap-by-gap status; v4 trio addendum at §11)
12. **[ACCORD_UPDATE.md](ACCORD_UPDATE.md)** — Proposed revisions to the CIRIS Accord; v0.3 trio addendum at §13; Annex K cross-walk at §14
13. **[PRIOR_ART.md](PRIOR_ART.md)** — Where this work sits in the AI-ethics-and-governance literature; honest attribution of overlap with Jobin et al. (2019), Floridi & Cowls (2019), Rome Call (2020), Policy Cards (2025), OSCAL-for-AI (2026), and NIST AI RMF crosswalks; what we should and should not claim

Source materials live under `source_material/governance/{batch_id}/` with per-batch `manifest.yaml`. The third-party document content itself is gitignored (not republished); the manifests are tracked.

---

## Posture Note

The author is in active spiritual direction and has received affirmation from his parish priest regarding the spirit of this project. The deference shown here is rooted in lived relationship with the tradition, even while the author self-identifies as a **Christian atheist / Christian Stoic** in the structural-Logos sense.

We offer this work humbly for scrutiny by the Catholic tradition, the broader AI ethics community, and anyone serious about building technology that truly safeguards the human person.

---

## License

[MIT License](LICENSE) — feel free to fork, critique, or build upon this work.
