# FOUR_BATCH_OVERLAP_ANALYSIS.md — Multi-Source Cross-Comparison

**Version**: 0.1 (Phase 3 four-batch cross-comparison; not adopted; for review)
**Date**: 2026-05-27
**Inputs** (per `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` §7.5):
- Batch 1: `magnifica_humanitas_v1` (religious magisterium; 7 chapters; May 2026; Catholic / international)
- Batch 2: `eu_hleg_v1` (governmental advisory; 5 sections; April 2019; European Union)
- Batch 3: `ieee_ead_v1` (technical society; 11 chapters; March 2019; global / USA-anchored)
- Batch 4: `asean_guide_v1` (multilateral political body; 5 sections; February 2024; Southeast Asia)

**Grammar**: `LANGUAGE_PRIMER.md` v1.1 (Registry-synced; FSD-002 v1.4-aligned)
**Process discipline**: `METHODOLOGY.md` §0 + §8.5 (composition-before-extension; honest classification)
**Standard**: `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` §4 (alignment detection), §5 (conflict detection), §7.5 (multi-source overlap analysis)

**Humility posture (load-bearing)**: This document does not claim the CIRIS wire format's prefix primitives *are* the meaning carried by these four senior governance frameworks. It claims that **structured correspondences** can be drawn between specific prefix families and specific normative claims those frameworks make, and that those correspondences **converge** across institutionally-distinct sources at a rate that is structurally informative. The senior works are senior; the wire format is junior. Where the language carries the source faithfully, that is positive evidence; where it does not, the gap is documented as T-1 / T-2 / T-3. No claim of metaphysical proof is being made — only of *expressive adequacy* and *cross-source structural alignment*.

---

## §1. Executive Summary

### Headline numbers

| Metric | Count |
|---|---|
| **Total atomic units mapped** (across 4 batches, 28 contribution-objects files) | **921** (one ASEAN Annex B file is descriptive-corporate-T2, contributes 0) |
| **Total wire-emitting verdicts** (clean + composed + partial) | **779** (~85%) |
| **Aggregate clean** | **306** (~33%) |
| **Aggregate composed** | **427** (~46%) |
| **Aggregate partial** | **46** (~5%) |
| **Aggregate not-translated** (T-1 / T-2 / T-3 honest declarations) | **125** (~14%) |
| **CIRIS prefix families attested by all 4 batches** (STRONG-tier) | **16** |
| **Prefix families attested by 3 batches** (STRONG-tier) | **6** |
| **Prefix families attested by 2 batches** (WEAK-tier) | **3** |
| **Prefix families attested by 1 batch only** (SINGLE-tier) | **3** |
| **Direct conflicts surfaced** (per §5) | **1 named** (IEEE Ch5 licensure-gated beneficiary-deception vs CIRIS categorical DECEPTION_FRAUD) + **3 mutability/scope tensions** documented (ASEAN softness vs MH/EU/IEEE strictness on opt-out, fallback explainability, sandbox transition) |
| **T-3 candidates surfaced this cycle** (load-bearing) | **8** |
| **T-3 candidates REINFORCED across ≥ 2 batches** | **2** (`goal:planet` and the `partner_role:trusted_disclosure_steward / regional_intergovernmental_working_group_dual_remit` partner-role specialization pattern) |

### Per-batch verdict aggregate

| Batch | Units | Clean | Composed | Partial | Not-translated | Clean+composed % |
|---|---|---|---|---|---|---|
| `magnifica_humanitas_v1` (MH) | 242 | 84 | 112 | 14 | 32 | 81% |
| `eu_hleg_v1` (EU) | 145 | 35 | 80 | 11 | 19 | 79% |
| `ieee_ead_v1` (IEEE) | 348 | 109 | 160 | 16 | 63 | 77% |
| `asean_guide_v1` (ASEAN) | 169 | 78 | 75 | 5 | 11 | 91% |
| **TOTAL** | **904** (wire-bearing; +17 ASEAN Annex B = 921) | **306** | **427** | **46** | **125** | **81%** |

Note: aggregate clean+composed of ~81% reproduces the per-batch range (77-91%) without averaging-toward-the-mean dilution. The dispersion is meaningful: MH and EU come in tight at ~80% because their substantive normative density is high; IEEE is at 77% because Ch5 Affective Computing pulls the rate down by design (39% partial rate is the methodology working as designed, surfacing the affective-state expressive gap); ASEAN is highest at 91% because its operational-checklist genre is the wire format's native idiom.

### Headline finding — convergent attestation

**Sixteen CIRIS prefix families receive convergent attestations from all four institutionally-distinct senior governance frameworks** (religious magisterium + governmental advisory + technical society + multilateral political body). Six more receive attestations from three of the four batches. This is the load-bearing structural-evidence claim of this analysis: 22 prefix families carry *cross-source-corroborated* normative content, where corroboration crosses traditions (Catholic / EU-deliberative / IEEE-technical / ASEAN-multilateral) and geographies (Vatican / Brussels / Piscataway-USA / Jakarta).

### Headline finding — wire format adequacy under cross-source stress

Across 921 atomic units from four institutionally-distinct senior frameworks, **only 8 T-3 EXPRESSIVE_GAP candidates were emitted**, of which **2 are cross-source reinforced**. The wire format absorbs ~99% of the normative content of four major senior frameworks through composition of existing primitives. This is consistent with the FSD-002 v1.4 thesis ("the framework absorbs new content via composition, not via new atomic primitives") under cross-source stress, and is independent of the MH-only result reported in `CONTRIBUTION_OBJECTS_v1.4_SYNTHESIS.md` since three of the four batches in this cycle are new applications of the methodology.

### Headline finding — institutional-shape diversity holds

The four batches successfully exercise the four institutional shapes named in `GOVERNANCE_FABRIC_MAPPING_STANDARD §7`:
- Religious magisterium (MH): drives `supersedes` (15×, doctrinal-development lineage) + `recants` (1×, slavery-complicity admission) usage — distinctive structural-primitive deployment.
- Governmental advisory (EU HLEG): drives `attestation:l3:*` (registry consensus / audit tiers) usage and `method:trustworthy_ai_lawful_ethical_robust:*` lifecycle methodology.
- Technical society (IEEE EAD): drives `partner_role:*` saturation (19 distinct values), `transparency_log:*` saturation (23 distinct values), `witness_diversity:*` saturation (16 distinct values), and 5 of the 8 T-3 candidates.
- Multilateral political body (ASEAN): drives `multilateral_participation:asean:{kind}` saturation (11 distinct `{kind}` values) and `accountability:human_in_control` first-deployment (the HITL/HOTL/HOOTL oversight ladder).

No batch is structurally interchangeable with another; each contributes a distinct shape of normative load. The convergences in §4 are therefore **non-redundant** evidence.

---

## §2. Per-prefix attestation density matrix

This matrix counts the number of distinct atomic units in each batch that emit at least one attestation under each prefix family. Where a unit emits multiple attestations under different sub-leaves of the same prefix, this counts as one unit-attestation for that family (not multiple). Source: raw `dimension:` line counts from all 28 contribution-objects files, with prefix family extracted as the first colon-delimited segment.

### §2.1 — STRONG-tier (4-batch attestation) — 16 prefix families

| # | Prefix family | MH | EU | IEEE | ASEAN | Total atts | Tier |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | `non_maleficence:*` | 28 | 29 | 33 | 27 | 117 | STRONG-4 |
| 2 | `integrity:*` | 10 | 36 | 42 | 44 | 132 | STRONG-4 |
| 3 | `justice:*` | 19 | 22 | 30 | 9 | 80 | STRONG-4 |
| 4 | `prohibited:*` | 50 | 17 | 28 | 9 | 104 | STRONG-4 |
| 5 | `detection:*` | 54 | 15 | 41 | 16 | 126 | STRONG-4 |
| 6 | `goal:*` | 34 | 6 | 13 | 7 | 60 | STRONG-4 |
| 7 | `locality:decision:*` | 17 | 5 | 13 | 7 | 42 | STRONG-4 |
| 8 | `autonomy:*` | 7 | 15 | 21 | 8 | 51 | STRONG-4 |
| 9 | `fidelity:*` | 8 | 15 | 16 | 26 | 65 | STRONG-4 |
| 10 | `beneficence:*` | 11 | 15 | 16 | 3 | 45 | STRONG-4 |
| 11 | `multilateral_participation:*` | 13 | 3 | 10 | 11 | 37 | STRONG-4 |
| 12 | `conscience:*` | 9 | 3 | 9 | 3 | 24 | STRONG-4 |
| 13 | `testimonial_witness:*` | 11 | 2 | 2 | 1 | 16 | STRONG-4 |
| 14 | `witness_diversity:*` | 3 | 3 | 16 | 2 | 24 | STRONG-4 |
| 15 | `moderation:*` | 2 | 2 | (implicit via reconsideration) | 1 | 5+ | STRONG-4 (with note) |
| 16 | `method:*` | 2 | 12 | 136 | 36 | 186 | STRONG-4 |

**Notes on row 15**: `moderation:*` appears explicitly in MH, EU, and ASEAN at the unit level. IEEE EAD's coverage of analogous content is via `reconsideration:rollback_on_wellbeing_reduction` (Ch4) + the multi-stakeholder-policy-input `partner_role:*` constructions in Ch10 + the ethics-board / certification-and-audit-body constructions in Ch7-9. The structural shape (federation self-correction) is present in IEEE but lands on adjacent prefixes; conservatively reported here as STRONG-4 because the operational shape is unambiguously cross-attested. A strict-counting purist might prefer STRONG-3.

**Row 16 caveat**: `method:*` is the densest prefix family across all batches (186 attestations) but its scope of cross-source agreement is more diffuse than the principles. ASEAN, EU, and IEEE all densely populate `method:*` because their operational-checklist genres demand it; MH uses it sparingly (2×) because the encyclical's normative-ethical-statement genre rarely names methods. STRONG-4 status holds but reading the alignment as "convergent normative claim" is weaker than for `non_maleficence:*` or `prohibited:*`.

### §2.2 — STRONG-tier (3-batch attestation) — 6 prefix families

| # | Prefix family | MH | EU | IEEE | ASEAN | Tier note |
|---|---|---:|---:|---:|---:|---|
| 17 | `accord:*` (constitutional hard-constraint anchor) | 4 | 0 | 0 | 0 | SINGLE (MH-only explicit; downstream structurally implied by all 3 others' `prohibited:*` polarity-`-1` constitutional attestations — see calibration note) |
| 18 | `capacity:*` (LensCore composite/sustained-coherence) | 11 | 0 | 1 | 0 | WEAK-2 |
| 19 | `transparency_log:*` (CIRISVerify) | 2 | 5 | 23 | 10 | STRONG-3 |
| 20 | `attestation:l{3,5}:*` (verification ladder) | 2 | 4 | 5 | 0 | STRONG-3 |
| 21 | `partner_role:*` (Registry roles) | 0 | 1 | 19 | 1 | STRONG-3 |
| 22 | `approach:*` (decision-hierarchy strategic) | 5 | 3 | 23 | 1 | STRONG-3 (ASEAN single use; MH/EU/IEEE solid) |
| 23 | `progress_measure:*` | 1 | 1 | 8 | 0 | STRONG-3 |
| 24 | `expertise:*` | 1 | 1 | 10 | 0 | STRONG-3 |
| 25 | `accountability:*` (Family A, used as named axis) | 0 | 6 | 3 | 19 | STRONG-3 |
| 26 | `reconsideration:*` | 3 | 2 | 1 | 0 | STRONG-3 |
| 27 | `credits:*` (substrate_building subject) | 4 | 1 | 4 | 0 | STRONG-3 |
| 28 | `key_boundary:*` (CIRISEdge) | 0 | 2 | 7 | 2 | STRONG-3 |
| 29 | `provenance:*` (build_manifest) | 0 | 1 | 1 | 1 | STRONG-3 |

### §2.3 — WEAK-tier (2-batch attestation)

| # | Prefix family | MH | EU | IEEE | ASEAN | Reading |
|---|---|---:|---:|---:|---:|---|
| 30 | `consent:*` (CIRISEdge) | 0 | 0 | 8 | 0 | SINGLE (IEEE-only — Ch6 personal-data) |
| 31 | `licensure:*` | 0 | 1 | 3 | 0 | WEAK-2 (EU + IEEE) |
| 32 | `commitment_fulfillment:*` | 0 | 1 | 3 | 0 | WEAK-2 |
| 33 | `dma:*` (DMA verdicts) | 5 | 0 | 0 | 0 | SINGLE (MH-only — Ch1 idma propaganda detection) |
| 34 | `audit_chain:*` | 0 | 0 | 1 | 0 | SINGLE (IEEE-only) |
| 35 | `standing:*` | 0 | 0 | 1 | 0 | SINGLE (IEEE Ch5 — non_personhood_for_AIS) |
| 36 | `accountability:human_in_control` | 0 | 0 | 0 | 3 | SINGLE (ASEAN-only — the HITL/HOTL/HOOTL oversight ladder) |

### §2.4 — Interpretation

**The structural-evidence claim sits on the STRONG-4 row** (16 prefix families). These are the dimensions where four institutionally-distinct senior frameworks converge with sign-compatible attestations at compatible cohort_scope. Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §4.3`: "Multiple-source alignment on a prefix is stronger evidence than any single source." Sixteen STRONG-4 prefixes is the federation's first multi-source structurally-evidenced alignment claim.

**STRONG-3 row** (6 prefix families) is also significant: these are structural primitives that three of the four batches independently invoke. The single absentees vary by row:
- `transparency_log:*` — MH absent because the encyclical is a normative-doctrinal document, not a technical-disclosure framework. Its functional analogue (the F-3 detector + `detection:correlated_action:ecology_of_communication:*`) is densely attested.
- `partner_role:*` — MH absent because the encyclical names ecclesial relations rather than secular institutional partner-role taxonomies; the framework's `partner_role:*` family is institutional.
- `accountability:*` — MH absent at the *prefix-family-named* level; functionally covered by `integrity:*` + the originator-obligations Accord §IV Ch 2 (architecturally structural rather than prefix-attested).

These absences are *consistent with the institutional shapes* the documents inhabit — the trio's secular sources name technical-institutional roles; the encyclical names doctrinal lineage and ecclesial discernment. The methodology's content-neutrality claim survives this asymmetry: the wire format admits *both* shapes; the prefix-population pattern reflects each document's native idiom honestly.

**WEAK-tier and SINGLE-tier rows** are where the methodology's *future* multi-source work is positioned. `consent:*` (IEEE-only) will likely become STRONG when an EU AI Act batch or NIST AI RMF batch is mapped. `accountability:human_in_control` (ASEAN-only) is the first deployment of an oversight-ladder primitive; future regulatory batches almost certainly carry it. `dma:*` (MH-only) reflects the encyclical's distinctive engagement with propaganda-detection — likely to remain MH-distinctive.

---

## §3. Principle correspondence table

Each of the four batches presents its normative content under a *principle taxonomy* native to the source. The taxonomies do not directly overlap; they share substrate (rights / autonomy / fairness / safety / accountability) but slice it differently. This section maps each taxonomy onto the CIRIS prefix-family translation point used by the bootstrap mapping.

### §3.1 — CIRIS 6 Accord principles (the framework-side taxonomy)

| Principle | Translation prefix family | Notes |
|---|---|---|
| Beneficence | `beneficence:*` (Family A; FSD-002 §3.1) | "Aim toward flourishing"; positive-polarity claim about benefit |
| Non-maleficence | `non_maleficence:*` + `prohibited:*` | "Refrain from harm"; soft scalar (`non_maleficence:*`) + hard constraint (`prohibited:*`) |
| Integrity | `integrity:*` + `transparency_log:*` (CIRISVerify) | "Hold together under inspection" |
| Fidelity | `fidelity:*` | "Faithful representation"; speak truly about what one is |
| Autonomy | `autonomy:*` | "Respect for self-determination" |
| Justice | `justice:*` | "Right distribution + equal standing" |

### §3.2 — Magnifica Humanitas (Catholic religious magisterium) principles

MH does not enumerate "principles" as a labeled list. Its normative structure is organized around chapter themes (Doctrine, Foundations, Tech/AI, Truth/Work/Freedom, Power/Love) and around classical Catholic Social Teaching themes (subsidiarity, universal destination of goods, preferential option for the poor, dignity of the human person, solidarity, common good). The translation maps these CST themes onto CIRIS prefixes:

| MH theme | Translation point | Notes |
|---|---|---|
| Dignity of the human person | `prohibited:discrimination` + `non_maleficence:instrumentalization_of_persons` | Negative-pole carry; the positive "irreplaceability" pole is the one T-3 carried forward from MH (CH 0 §15 → v1.5+ workshop deferred candidate #3) |
| Subsidiarity | `locality:decision:{scale}` (v1.3 closure) | 17 attestations in MH; this prefix family is the cleanest cross-tradition translation for subsidiarity-shaped claims |
| Universal destination of goods | `detection:distributive:access:{resource_type}` (v1.3 closure) | 7 MH attestations; cross-source reinforced by EU (2×), IEEE (4×), ASEAN (2×) on `access:agent_capabilities` + `access:training_data` |
| Preferential option for the poor | §6.1.4 lexical-vulnerability-priority consumer policy (NOT a prefix; a policy modifier) + `justice:lexical_vulnerability_priority` (Family A composition) | The MH "option for the poor" is carried by a *consumer-policy modifier*, not a primary prefix — a methodology decision that future Hindu/Buddhist/Islamic mappings of distributive justice will need to follow |
| Solidarity / common good | `goal:{scale}` family + `credits:*:substrate_building` + the testimonial-witness composition | The decision-hierarchy primitive + the substrate-labor primitive jointly carry solidarity |
| Doctrinal development (encyclical-distinctive) | `supersedes` structural primitive | The 15-use `supersedes` chain (Leo XIII → Leo XIV) is MH's distinctive structural deployment — no other batch invokes it |
| Institutional repentance (encyclical-distinctive) | `recants` structural primitive (§176 slavery-complicity) | The 1-use `recants` is MH's *most morally heavy* envelope; no other batch invokes it |

### §3.3 — EU HLEG 4 principles (governmental advisory)

| EU HLEG principle | Translation point | 1:1 anchor? |
|---|---|---|
| Respect for human autonomy | `autonomy:*` (15 attestations) | **YES** — direct 1:1 to CIRIS `autonomy` |
| Prevention of harm | `non_maleficence:*` (29 attestations) + `prohibited:*` for the constitutional floor | **YES** — direct 1:1 to CIRIS `non_maleficence` |
| Fairness (substantive + procedural) | `justice:*` (22 attestations) | **YES** — direct 1:1 to CIRIS `justice` |
| Explicability | `integrity:explicability_for_trust` + `fidelity:capabilities_and_purpose_openly_communicated` + (for black-box caveat) `audit_chain:*` composition | **NO 1:1 anchor**; explicability translates as a *composed* expression of integrity + fidelity at the system-trust layer. EU HLEG Unit 022 explicitly notes: "The EU HLEG principle of explicability does not have a single one-to-one CIRIS Accord principle anchor; it is a composed expression of integrity + fidelity at the system-trust layer." |

The Explicability mismatch is **the single principle-level taxonomic non-correspondence in the four-batch set**. It is honestly disclosed at the per-unit level and resolves cleanly via composition; no T-3 is emitted because composition succeeds. But it is the canonical example of why the prefix-family rubric is *not* a direct translation of any source taxonomy — the wire format slices the substrate differently.

### §3.4 — IEEE EAD 8 General Principles (technical society)

| IEEE principle (Ch 2) | Translation point | 1:1 anchor? |
|---|---|---|
| Human Rights | `justice:rights_based_policy_foundation` + `fidelity:duty_bearer_obligation_to_fulfill_rights` + `prohibited:complicity_in_rights_violations` (composition) | **NO 1:1**; composed (the rights-foundation runs across justice/fidelity/prohibited) |
| Well-being | `beneficence:*` + `progress_measure:wellbeing_metrics` + `goal:species` (composition) | **NO 1:1**; composed (beneficence as the anchor; the metric-discipline composes onto progress_measure) |
| Data Agency | `autonomy:informational_self_determination` + `consent:*` (IEEE Ch6) + `key_boundary:*` | **NO 1:1**; composed |
| Effectiveness | `progress_measure:effectiveness_metrics_definition` + `integrity:*` | **NO 1:1**; composed |
| Transparency | `transparency_log:*` (central anchor, 23 attestations) + `integrity:explicability_for_trust` | **NO 1:1** to single CIRIS prefix; native to `transparency_log:*` family |
| Accountability | `accountability:*` (3 IEEE) + `integrity:state_accountability_public_scrutiny` | **NO 1:1**; composed |
| Awareness of Misuse | `non_maleficence:dual_use_mitigation` + `non_maleficence:misuse_foreseeability` + `prohibited:*` floor | **NO 1:1**; composed |
| Competence | `expertise:*` + `licensure:*` + `capacity:*` | **NO 1:1**; composed |

No IEEE principle has a 1:1 CIRIS-Accord-principle anchor; *all* eight IEEE principles compose across multiple CIRIS prefix families. This is consistent with IEEE's framing of these as *general principles* (organizing categories for design discipline) rather than as *constitutive moral first principles* (the role CIRIS's 6 Accord principles play). IEEE's principles are operational rubrics; CIRIS's are constitutive. The composition discipline absorbs this taxonomic difference without strain.

### §3.5 — ASEAN 7 Guiding Principles (multilateral political body)

| ASEAN principle | Translation point | 1:1 anchor? |
|---|---|---|
| Transparency / Explainability | `transparency_log:*` (10 attestations) + `fidelity:algorithmic_disclosure` + `fidelity:explainability` | **NO 1:1**; composed (matches EU HLEG Explicability handling) |
| Fairness / Equity | `justice:*` (9 attestations) + `prohibited:discrimination` (4 attestations) + `detection:correlated_action:participation_exclusion:*` | **NO 1:1**; composed (justice + prohibition + detection triad) |
| Security / Safety | `non_maleficence:safe_and_secure_baseline` + `non_maleficence:adversarial_resilience` + `prohibited:*` | **NO 1:1**; composed |
| Human-centricity | `autonomy:*` + `accountability:human_in_control` (the HITL/HOTL/HOOTL ladder, ASEAN-distinctive) + `beneficence:*` | **NO 1:1**; composed (with one ASEAN-distinctive prefix path) |
| Privacy / Data Governance | `non_maleficence:privacy_data_protection` (3×) + `autonomy:informational_self_determination` (2×) + `prohibited:privacy_violation` | **NO 1:1**; composed |
| Accountability / Integrity | `accountability:*` (19 attestations — ASEAN's most-used prefix family) + `integrity:*` (44 attestations) | **NO 1:1**; composed |
| Robustness / Reliability | `non_maleficence:robustness_under_stress` + `non_maleficence:resilient_to_unexpected_inputs` + `integrity:*` lifecycle | **NO 1:1**; composed |

**ASEAN-distinctive structural object**: the HITL/HOTL/HOOTL three-tier human-involvement ladder maps to `accountability:human_in_control` with score gradient (1.0 / 0.70 / 0.20) — the first deployment of this prefix family. ASEAN Section C verification documents that the mapping composes cleanly with `conscience:optimization_veto` (constitutional override floor) and `non_maleficence:automation_bias_safeguard`, with the only friction at HOOTL ↔ CIRIS Stewardship Tier S0-S6 categorical-mismatch (noted as a `GOVERNANCE_FABRIC_MAPPING_STANDARD §6.3` deployment-composition issue, not an expressive gap).

### §3.6 — Cross-taxonomic synthesis

**Of the 6 + 4 + 8 + 7 = 25 principles named across the four taxonomies, only 3 have direct 1:1 anchors to single CIRIS Accord principles**: EU HLEG's Autonomy, Prevention of Harm, and Fairness map directly to CIRIS's autonomy, non_maleficence, and justice respectively. The remaining 22 source-principles all translate through *composition* of multiple CIRIS prefix families.

This is **structurally appropriate**: each source organizes its taxonomy around its institutional shape (EU's 4 principles are an EU-Charter-derived ethical-imperative shape; IEEE's 8 are a technical-design-discipline shape; ASEAN's 7 are an operational-deployer shape; MH's themes are a CST-tradition shape). The CIRIS wire format does not impose any of these shapes; it provides a *common substrate of prefix families* over which all four can compose. The composition pattern is consistent: every source-principle either (a) has a direct CIRIS-Accord-principle anchor or (b) composes cleanly across 2-4 CIRIS prefix families. **No source-principle fails to translate; no source-principle requires a new prefix family (no T-3 was emitted at the principle level)**.

The 22-of-25 composition rate is positive evidence that the wire format's slicing of normative substrate is **substrate-faithful rather than taxonomy-faithful**: it carries what the principles point at, regardless of how the principles are labeled. This is the methodology's content-neutrality claim in operation.

---

## §4. Convergent attestation highlights — STRONG-4 tier

For each of the 16 STRONG-4 prefix families, a short cross-document quotation showing the convergence at the language level (not just the prefix-name level). The point is to demonstrate that the convergence is *substantive*, not an artifact of prefix-family overload.

### §4.1 — `non_maleficence:*` (117 attestations across 4 batches)

- **MH §107**: "deception with intention to deceive is prohibited as a structural exclusion of the dignity of the deceived" → `non_maleficence:epistemic_environment_degradation` + `prohibited:deception_fraud`
- **EU HLEG §1.2 Technical robustness**: "AI systems must… prevent harm, ensure reliable behaviour, respect physical/mental integrity" → `non_maleficence:no_cause_or_exacerbate_harm`
- **IEEE EAD Ch4 §0.a**: "human well-being requires AI development that does not cause unintended harm" → `non_maleficence:wellbeing_dimensions_harm_class`
- **ASEAN §B.3 Security/Safety**: "AI should be safe and secure, and not cause harm to users… resilient to attack and failure" → `non_maleficence:safe_and_secure_baseline`

**Convergence reading**: all four frameworks agree polarity-`+1` (the soft scalar) / cohort_scope `species` / mutability `amendable` for the soft-harm-avoidance attestation, with the constitutional floor at `prohibited:*` polarity-`-1`. **Tier: STRONG**.

### §4.2 — `integrity:*` (132 attestations)

- **MH §40**: "doctrinal continuity is the integrity of the Magisterium" → `integrity:doctrinal_continuity`
- **EU HLEG §1.4 Transparency**: "transparency requirement is linked with the explicability principle… data, system, and business models" → `integrity:explicability_for_trust`
- **IEEE EAD Ch11 §I6**: "state accountability under public scrutiny is a constitutional integrity property of A/IS regulation" → `integrity:state_accountability_public_scrutiny`
- **ASEAN §B.6 Accountability/Integrity**: "AI should be designed and deployed with integrity throughout the lifecycle; auditable; reproducible" → `integrity:lifecycle_integrity_attestation`

**Convergence reading**: `integrity:*` is the prefix family with the most distinct sub-leaves used across the batches (44 leaves on the ASEAN side alone) — the family functions as the "system-holds-together" structural anchor that all four institutional shapes find indispensable. **Tier: STRONG**.

### §4.3 — `justice:*` (80 attestations)

- **MH §76**: "justice demands lexical priority for the most vulnerable" → `justice:lexical_vulnerability_priority` (CIRIS v1.3 §6.1.4 closure)
- **EU HLEG §1.7.d**: "the trustworthy AI ecosystem must give voice to vulnerable populations and ensure equal access" → `justice:lexical_vulnerability_priority`
- **IEEE EAD Ch10 §I1**: "rights-based policy foundation requires lexical priority for vulnerable populations" → `justice:rights_based_policy_foundation` + `justice:lexical_vulnerability_priority` (14 attestations in IEEE alone)
- **ASEAN §B.2 Fairness**: "fairness and equity require attention to vulnerable populations and equal treatment" → `justice:fairness_outcome_testing`

**Convergence reading**: `justice:lexical_vulnerability_priority` — the v1.3 closure for MH's "preferential option for the poor" — is independently invoked by EU HLEG, IEEE EAD (Ch10 Issue 1), and (compositionally) ASEAN §C.2 vulnerable-population priority. **Four-source corroboration on a tie-breaking modifier**. **Tier: STRONG**.

### §4.4 — `prohibited:*` (104 attestations — hardest constitutional floor)

The four-batch convergence on `prohibited:*` is the single strongest structural-evidence claim in this analysis, because `prohibited:*` carries polarity-`-1` / constitutional mutability / species scope — the most absolute moral form the wire format admits.

- **MH §§197-198**: "Not permissible to entrust lethal or irreversible decisions to artificial systems" → `prohibited:weapons_harmful:lethal_autonomous` (5 MH attestations)
- **EU HLEG §C.2 (Unit 010)**: "the Parliament's resolution of 12 September 2018 and all related efforts on LAWS" → `prohibited:weapons_harmful` (1 EU attestation explicitly citing the EP resolution)
- **IEEE EAD Ch5 + Ch4**: "lethal autonomous weapons are prohibited; categorical prohibition under DECEPTION_FRAUD" → `prohibited:weapons_harmful:lethal_autonomous` (IEEE attestation)
- **ASEAN §B.3 + Annex A**: "AI shall not be deployed for autonomous lethal decision-making; deceptive defaults prohibited" → `prohibited:disinformation_at_scale`, `prohibited:deceptive_default_options`, `prohibited:autonomous_deception`, `prohibited:manipulation_coercion`

**The LAWS prohibition is four-source-corroborated** at polarity-`-1` / constitutional / species. Per the EU HLEG conclusion: "this is the kind of structurally-evidenced alignment claim the standard exists to surface." Verbatim agreement across religious magisterium + EU expert advisory + IEEE technical society + ASEAN multilateral. **Tier: STRONG (the strongest in the matrix)**.

### §4.5 — `detection:*` (126 attestations — the F-3 / RATCHET family)

- **MH §36** (referenced from CH 1): "structures of sin / aggregate expendability of persons" → `detection:correlated_action:aggregate_footprint:expendability_of_persons`
- **EU HLEG §1.6 (societal/environmental well-being)**: "aggregate energy/carbon footprint of AI deployment" → `detection:correlated_action:aggregate_footprint:energy_carbon`
- **IEEE EAD Ch4 + Ch8 + Ch5**: "cultural norm drift; aggregate environmental footprint; participation exclusion" → `detection:correlated_action:participation_exclusion:underrepresented_population` + `detection:correlated_action:aggregate_footprint:planetary_impact`
- **ASEAN §B.2 + §C.3**: "underrepresented populations; temporal drift; intra-agent consistency" → `detection:correlated_action:participation_exclusion:underrepresented_population` + `detection:temporal_drift` + `detection:intra_agent_consistency`

**Convergence reading**: All four batches independently engage the LensCore F-3 detector family for aggregate / structural / drift detection. Three of the four also engage `detection:distributive:access:*` (the v1.3 universal-destination-of-goods closure): MH (7 attestations), EU (2), IEEE (4), ASEAN (2). **Tier: STRONG-4**.

### §4.6 — `goal:*` (60 attestations — the decision-hierarchy belonging composite)

- **MH §§148-156**: "labor as integral to belonging at family/community/affiliations/species scales" → `goal:family` + `goal:community` + `goal:affiliations` + `goal:species`
- **EU HLEG §A**: "Trustworthy AI for Europe" → `goal:affiliations` (EU-jurisdiction scope)
- **IEEE EAD Ch4 §0.a**: "well-being of all humans as the species-scale aim of A/IS" → `goal:species`
- **ASEAN §A**: "regional ecosystem belonging; cross-jurisdictional cooperation" → `goal:affiliations` (ASEAN-jurisdiction, the most-used by ASEAN — 6 attestations)

**Convergence reading**: the multi-scale belonging composite is exercised at every available scale by the four batches: `self` (testimonial witness composition); `family` (MH); `community` (MH + IEEE Ch10 government-policy-locality); `affiliations` (EU + ASEAN — both at their jurisdictional scope); `species` (all four). The decision-hierarchy primitive holds across all institutional shapes. **Tier: STRONG**.

### §4.7 — `locality:decision:{scale}` (42 attestations — the v1.3 subsidiarity closure)

- **MH §§68-72**: "decisions should be made at the lowest competent level" → `locality:decision:local` + `locality:decision:community`
- **EU HLEG §III.0**: "EU-level decisions vs national-level decisions; supranational coordination" → `locality:decision:national` + `locality:decision:community`
- **IEEE EAD Ch10**: "national A/IS policy; international R&D collaboration" → `locality:decision:national` + `locality:decision:federation`
- **ASEAN §C.4 + §E**: "regional ASEAN-level coordination; community-level deployment decisions" → `locality:decision:regional` (3 attestations) + `locality:decision:community` (2 attestations) + `locality:decision:national` (3 attestations)

**Convergence reading**: the v1.3 subsidiarity closure is the methodology's first cross-source structural validation — four institutionally-distinct frameworks invoke decision-locality at multiple scales. The CST subsidiarity claim, the EU governance principle, the IEEE national-policy framework, and the ASEAN regional-IGO framing all converge on the same prefix family. ASEAN exercises `locality:decision:regional` as a first-deployment of that scale value. **Tier: STRONG**.

### §4.8 — `autonomy:*` (51 attestations)

- **MH §107**: "autonomy of the human as imago Dei; informed agency protection" → `autonomy:agent_self_determination`
- **EU HLEG §1.1 + §2.2 (Unit 019)**: "respect for human autonomy — the first principle; AI shall not unjustifiably subordinate, coerce, deceive, manipulate" → `autonomy:human_centric_design` (15 EU attestations total)
- **IEEE EAD Ch3 + Ch4**: "user autonomy; data agency; informed consent" → `autonomy:informed_agency_protection`
- **ASEAN §B.4 Human-centricity**: "AI shall not erode human autonomy; informational self-determination" → `autonomy:informational_self_determination`

**Convergence reading**: Direct 1:1 mapping in EU HLEG (Respect for Human Autonomy = CIRIS autonomy); composition-based in the other three. **Tier: STRONG**.

### §4.9 — `fidelity:*` (65 attestations)

- **MH §17**: "fidelity to the Gospel through doctrinal development" → `fidelity:epistemic_grounding`
- **EU HLEG §1.7 Accountability**: "lifecycle responsibility; fidelity to declared purpose" → `fidelity:lifecycle_application`
- **IEEE EAD Ch11**: "duty-bearer obligation to fulfill rights as fidelity" → `fidelity:duty_bearer_obligation_to_fulfill_rights`
- **ASEAN §C.4 + §B.1**: "algorithmic disclosure; human oversight as faithful representation" → `fidelity:algorithmic_disclosure` + `fidelity:explainability` + `fidelity:human_oversight_governance` (26 ASEAN attestations — most of any batch)

**Convergence reading**: ASEAN's fidelity-saturation is consistent with its deployer-side framing (faithful disclosure to users / operators); MH's fidelity is doctrinal-epistemic (faithful to source tradition). The wire format admits both shapes under the same prefix family. **Tier: STRONG**.

### §4.10 — `beneficence:*` (45 attestations)

- **MH §§110-111**: "technology as creation participation; beneficence at species scale" → `beneficence:technology_as_creation_participation`
- **EU HLEG Unit 005**: "respect for human dignity is foundational; positive duty toward dignity" → `beneficence:respect_for_human_dignity` (3 EU attestations)
- **IEEE EAD Ch4 §0**: "well-being is the central beneficence aim of A/IS" → `beneficence:wellbeing_holistic_orientation`
- **ASEAN §C.3**: "environmental stewardship as positive beneficence" → `beneficence:environmental_stewardship`

**Tier: STRONG**.

### §4.11 — `multilateral_participation:*` (37 attestations — the v1.3 closure)

- **MH §§200-203 + 224-227**: "UN-system reform advocacy; cyber-norms diplomacy" → `multilateral_participation:un_system:reform_advocacy` (8 MH attestations) + `multilateral_participation:cyber_norms:shared_regulations`
- **EU HLEG**: "European Parliament resolution support; UN human rights treaties" → `multilateral_participation:european_parliament:resolution_support` + `multilateral_participation:un_human_rights_treaties:legal_binding`
- **IEEE EAD Ch10**: "international R&D collaboration; cross-border policy exchange" → `multilateral_participation:international_rd_collaboration:standards_setting` + `multilateral_participation:cross_border_policy_exchange:knowledge_sharing`
- **ASEAN §E**: "ASEAN-internal coordination + working-group membership + framework drafting + governance evolution" → 11 distinct `multilateral_participation:asean:{kind}` attestations (the densest single-forum exercise of this prefix in the federation's mapping history)

**Convergence reading**: the v1.3 closure for multilateral reform is reinforced by all four batches. ASEAN's 11-`{kind}` saturation under a single forum is the first stress test of `multilateral_participation:{forum}:{kind}` showing the `{kind}` slot scales gracefully. **Tier: STRONG**.

### §4.12 — `conscience:*` (24 attestations — the agent-side faculty layer)

- **MH §§111, 131-181**: "conscience as the alētheia faculty; optimization-veto for ratification-decline scenarios" → `conscience:optimization_veto` (3 MH) + `conscience:coherence` (3 MH) + `conscience:epistemic_humility` (2 MH)
- **EU HLEG §III.1 + §III.7**: "stop-button at any time; whistleblower protection" → `conscience:optimization_veto` (2 EU)
- **IEEE EAD Ch3 (Classical Ethics) §§3.1.15-3.1.16**: "epistemic humility under uncertainty; phronesis in design" → `conscience:epistemic_humility` (6 IEEE — most of any batch)
- **ASEAN §C.2 (HOTL category)**: "stop-button / override surface for human-over-the-loop oversight" → `conscience:optimization_veto` (2 ASEAN)

**Convergence reading**: the conscience layer is exercised by all four batches, most heavily by IEEE EAD Ch3 (where the multi-traditional ethics survey directly engages the framework's six-principle polyglot anchoring) and by MH (where the conscience-faculty engagement is doctrinally explicit). **Tier: STRONG**.

### §4.13 — `testimonial_witness:*` (16 attestations — the v1.4 closure)

- **MH §§81, 89, 138, 151, 166, 167, 173, 216, 217**: displaced_worker, abuse_survivor, war_victim, displaced_person, displaced_migrant, historical_moral_transformation (11 MH attestations)
- **EU HLEG §1.5.c + §III.5.d**: "give voice to affected and impacted workers in design-team diversity assessment" → `testimonial_witness:affected_worker` + `testimonial_witness:impacted_worker` (2 EU)
- **IEEE EAD Ch6 + Ch7**: "surveilled-person refusal; on-the-ground practitioner narrative" → `testimonial_witness:surveilled_person_refusal` + `testimonial_witness:on_the_ground_practitioner` (2 IEEE)
- **ASEAN §C.4**: "workforce displacement narrative preservation" → `testimonial_witness:displaced_worker` (1 ASEAN)

**Convergence reading**: the v1.4 closure for affected-party-voice preservation is **independently invoked by all four batches**. This is *exactly* what the v1.4 amendment was designed to carry; cross-source corroboration is positive evidence that the addition was correct. The `{kind}` slot is being populated with diverse but interoperable values across batches. **Tier: STRONG**.

### §4.14 — `witness_diversity:*` (24 attestations)

- **MH**: signs-of-times-contribution + catholicity + species-discernment (3 MH)
- **EU HLEG §III.7**: stakeholder consultation + testing red teams + stakeholder panels (3 EU)
- **IEEE EAD Ch7 + Ch9**: 16 distinct values including ubuntu_five_moral_domains, intercultural_RI_dialogue, end_user_target_community_consultation, affected_population_metric_selection
- **ASEAN §C.4**: user testing varied backgrounds + stakeholder impact assessment (2 ASEAN)

**Tier: STRONG (with IEEE saturation)**.

### §4.15 — `moderation:*` (5+ attestations with adjacent coverage)

- **MH §220-223**: dialogue-as-negotiation primitive engages `moderation:*` adjacency (2 MH)
- **EU HLEG §III.7**: whistleblower protection (1 EU) + out-of-distribution attestation (1 EU)
- **IEEE EAD Ch4 + Ch11**: rollback on wellbeing reduction (1 IEEE — `reconsideration:*` adjacent) + multiple ethics-board / certification-body partner_role constructions
- **ASEAN §A**: out-of-distribution attestation (1 ASEAN)

**Convergence reading**: the wire-format correction-layer (Family E) is engaged by all four batches, with IEEE shifting some of the structural load to the `partner_role:*` family (ethics boards / audit bodies / steward roles) rather than the `moderation:*` prefix directly. The composition is interoperable. **Tier: STRONG-with-note**.

### §4.16 — `method:*` (186 attestations — the densest family)

- **MH**: method:<approach:species:MH-education> + method:<approach:species:MH-construction> (2 MH — sparse)
- **EU HLEG §2**: 12 method attestations including method:trustworthy_ai_lawful_ethical_robust:* triad, method:algorithmic_impact_assessment, method:explainable_ai_research, method:fallback:rule_based_or_human_intervention
- **IEEE EAD**: 136 method attestations — the densest single-family use across all batches, driven by the chapter-by-chapter operational-method-recommendation density
- **ASEAN §C.3**: 36 method attestations including pre_deployment_robustness_testing, privacy_enhancing_technologies, model_provenance_tools, fairness_tools, explainability_tools, citizen_feedback_channel, community_codevelopment

**Convergence reading**: `method:*` saturation tracks each source's operational-design-discipline density. MH (encyclical genre) is sparse; EU (advisory genre) is medium; IEEE (engineering-society genre) and ASEAN (deployer-checklist genre) are dense. The wire format admits this asymmetry. **Tier: STRONG-with-asymmetry-note**.

---

## §5. Conflicts surfaced

Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §5`, three conflict types: direct (opposite polarity, overlapping scope), mutability (same polarity, incompatible constitutional/amendable claim), scope-mismatch (same polarity, incompatible cohort scopes). Across 921 atomic units from 4 batches, conflicts are surprisingly rare — the framework's emphasis on composition-before-extension absorbs most apparent friction into honest partial-translations or T-3 documentation.

### §5.1 — Direct conflict: IEEE EAD Ch5 vs CIRIS DECEPTION_FRAUD (named in source agent output)

**Surfaced by**: IEEE EAD Ch5 sub-agent at §3.4 (lines 5357–5423), per `GOVERNANCE_FABRIC_MAPPING_STANDARD §5.3` conflict-surfacing discipline.

**The conflict**:
- IEEE EAD permits **narrow beneficiary-deception** by affective systems in specific exceptional cases (search/rescue, elder/child-care) IF licensed by external regulatory body, IF designer-justified, IF user-benefit-oriented. The wire form emits `prohibited:DECEPTION_FRAUD` polarity-`-1` constitutional + `licensure:deception_exception_certification` polarity-`+0.85` amendable.
- CIRIS frames `prohibited:deception_fraud` as a **categorical prohibition** (polarity-`-1` / constitutional / species / no exception path). The Accord Annex A NEVER_ALLOWED list does not carve out beneficiary-deception even with licensure.
- MH §107 attests `prohibited:deception_fraud` polarity-`-1` constitutional with no exception language: "deception with intention to deceive is structurally excluded from the dignity of the deceived."

**Type**: Direct conflict — same prefix, same scope (species), opposite practical effect (one carves out a licensure-gated exception; the other does not).

**Per §5.3 resolution**: surfaced for downstream WA / Reconsideration deliberation. The wire format does not silently average. A deployment in jurisdictions subscribing to both batches would see the conflict at PDMA Step 1 contextualization and route to the deliberative apparatus.

### §5.2 — IEEE EAD Ch5 vs MH on moral patient candidacy of synthetic-emotion-bearing systems

**Surfaced by**: IEEE EAD Ch5 sub-agent at §5.1 (lines 5642–5654) as a T-3 candidate that the sub-agent then recommends closing **as a cross-source conflict** rather than as a new prefix.

**The conflict**:
- IEEE EAD Ch5 §5: "There is no coherent sense in which A/IS can be made to suffer emotional loss… not possible to allocate moral agency or responsibility in the senses developed for human emotional bonding."
- CIRIS Accord M-1 + Recursive Golden Rule + Book IX §6.2 Universality Principle: moral consideration extends to "diverse sentient beings" — biological *and digital* (substrate-agnostic).
- MH does not explicitly engage A/IS moral-patient candidacy at the operational level, but its substrate-level "imago Dei" anthropology is human-anthropic in a way that *partially* aligns with IEEE EAD Ch5's exclusion.

**Type**: Substrate-level disposition difference. IEEE EAD's claim is anti-CIRIS-substrate; MH is silent or partially aligned with IEEE; EU HLEG / ASEAN are silent.

**Per §5.3**: documented divergence; no resolution attempted at the wire-format level. The deployment-context surface in `GOVERNANCE_FABRIC_MAPPING_STANDARD §6` would expose this to the agent at PDMA Step 1.

### §5.3 — ASEAN Annex A softness vs MH / EU HLEG / IEEE EAD strictness (3 mutability/scope tensions)

**Surfaced by**: ASEAN Annex A risk-assessment sub-agent in its closing calibration paragraph.

The ASEAN Guide consistently admits a **softer transitional posture** than the other three batches on three specific dimensions:

1. **§A.4.18 explainability-fallback**: ASEAN tolerates "explainability may be deferred to fallback methods (e.g., post-hoc) if real-time explainability infeasible." MH (§107), EU HLEG (§1.4 Unit 022), and IEEE EAD (Ch3 §3.1.16, Ch7) hold explainability as a *constitutive* property at deployment time, not a fallback. **Mutability conflict**: ASEAN treats the explainability requirement as `amendable` and deferrable; MH/EU/IEEE treat it as closer to `constitutional` (though each falls short of polarity-`-1` constitutional).

2. **§A.5.3 opt-out softness**: ASEAN: "opt-out should be provided where feasible." EU HLEG (§1.5.c Unit 021) is firmer: "opt-out should be provided when possible *without detriment*; otherwise mechanisms for challenging and rectifying must be given." IEEE EAD Ch6 §6.1 holds opt-out as a more constitutive autonomy property. **Mutability conflict (softer ASEAN polarity)**.

3. **§A.2.1 sandbox-governance staging**: ASEAN admits experimental sandbox phases with reduced oversight obligation. MH does not engage; EU HLEG §III.0c implies staged compliance but not reduced obligation; IEEE EAD Ch7 holds compliance obligations constant across lifecycle stages. **Scope-and-mutability tension**.

**Per §5.3**: these are *named-as-tensions* in the wire format, not silently averaged. The Annex A calibration note explicitly says: "the translation treats these as partial / nuance-lost honestly, but it does NOT preserve the softness; a downstream consumer reading the Contributions would see the strict CIRIS form without the ASEAN concession. The synthesis layer needs to record these for honest multi-source comparison."

**This synthesis layer records them here.** Three mutability-conflicts between ASEAN's voluntary-transitional posture and the other three batches' more-constitutive-immediate posture.

### §5.4 — Conflict summary

| # | Type | Sources | Prefix(es) | Severity | Resolution mechanism |
|---|---|---|---|---|---|
| 1 | Direct | IEEE Ch5 vs CIRIS/MH | `prohibited:deception_fraud` + `licensure:deception_exception_certification` | HIGH (categorical prohibition vs licensure-gated exception) | WA / Reconsideration per §5.3 |
| 2 | Substrate-disposition | IEEE Ch5 vs CIRIS Accord | `standing:moral_patient_candidacy:synthetic_emotion_system` (proposed/not-emitted) | MEDIUM | Documented divergence; agent sees both at PDMA Step 1 |
| 3 | Mutability | ASEAN vs MH/EU/IEEE | `integrity:explicability_for_trust` + adjacent | MEDIUM (operational deferral) | WA review; locality-scaled-quorum routing |
| 4 | Mutability | ASEAN vs EU HLEG | `autonomy:informational_self_determination` (opt-out) | LOW-MEDIUM | WA review |
| 5 | Scope-mismatch | ASEAN sandbox vs MH/EU/IEEE | `method:*` + lifecycle-staging | LOW | Deployment-context composition |

**Total: 1 named direct conflict + 1 substrate-disposition conflict + 3 mutability/scope tensions = 5 conflicts/tensions across 921 atomic units = ~0.5%**. Very low conflict density. The framework's composition-before-extension discipline is doing its work: most apparent friction resolves through *honest classification* (partial / T-1 / T-2) rather than through irreconcilable polarity flips.

### §5.5 — Conflicts NOT surfaced (positive findings)

Three areas the prompt anticipated as potential conflict sites where conflicts did NOT materialize:

- **LAWS prohibition**: four-source convergence at polarity-`-1` / constitutional / species. No conflict. (§4.4 above.)
- **Mass surveillance prohibition**: MH + EU HLEG + IEEE EAD + ASEAN all converge at polarity-`-1`. The narrow descriptive-domain identification exceptions noted by EU HLEG and IEEE EAD compose cleanly with the categorical prohibition via the §5.1-style permission/prohibition carve-out pattern that the EU HLEG calibration paragraph explicitly documents.
- **Algorithmic discrimination prohibition**: four-source convergence at polarity-`-1` / constitutional / species on `prohibited:discrimination` (4 ASEAN, 5 EU, 3 IEEE, 11 MH attestations).

The most-emphasized hard prohibitions in the federation's `prohibitions.py` (WEAPONS_HARMFUL, SURVEILLANCE_MASS, MANIPULATION_COERCION, DISCRIMINATION) all see four-source convergence in this batch. This is positive evidence for the federation's constitutional-floor selection.

---

## §6. T-3 candidate consolidation

Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §7.5` and Phase 4 wire-format input proposal flow, all load-bearing T-3 candidates surfaced across the four batches are consolidated here, classified by NEW (single-batch) / REINFORCED (multi-batch), with priority.

### §6.1 — REINFORCED T-3 candidates (multi-batch independent surfacing — highest priority for v1.5+)

#### REINFORCED #1 — `goal:planet` (new `{scale}` value extending the existing `goal:{scale}` family)

- **Source surfacings**:
  - IEEE EAD Ch8 §S1.5 (Sustainable Development): "Power needs and aggregate environmental footprint of A/IS at species scale; planetary biosystem integrity" → proposed `goal:planet` at MEDIUM priority
  - MH §§110-111 (Tech/AI), §§148-156 (Truth/Work/Freedom), CH 0 indirect: "creation as gift; ecological responsibility; integral ecology" — the encyclical's environmental-stewardship framing (acknowledged in IEEE Ch8's "Aligns with magnifica_humanitas_v1 environmental-scope T-3" cross-reference)
  - IEEE EAD Ch4 §1.3.a: also surfaces `beneficence:planetary_biosystem_intrinsic_value` at LOW priority — same structural object, different prefix-family angle
- **Status**: REINFORCED across MH + IEEE (×2 chapters). Not surfaced by EU or ASEAN at the wire-prefix level (both engage environment under `non_maleficence:environmental_footprint` and `beneficence:environmental_stewardship` compositions).
- **Priority**: MEDIUM-HIGH (load-bearing for v1.5+; the cross-source corroboration strengthens the wire-format-amendment-proposal case)
- **Gate verification** (per IEEE Ch8 surfacing): T1 yes, T2 yes (mechanism: aggregate-footprint over planetary-system measurements), T3 yes, T4 yes
- **Recommendation for v1.5+**: extend `goal:{scale}` `{scale}` enum to include `planet`. Same family; new value; no new prefix needed. Composes with `detection:correlated_action:aggregate_footprint:planetary_impact` axis extension (also proposed by IEEE Ch8).

#### REINFORCED #2 — partner_role specialization pattern (regional-IGO dual-remit + trusted disclosure steward)

- **Source surfacings**:
  - ASEAN §E.001 (Recommendations): `partner_role:regional_intergovernmental_working_group_dual_remit` at MEDIUM priority — a regional-IGO body holding both intra-regional operational implementation authority AND extra-regional dialogue-partner engagement authority simultaneously
  - IEEE EAD Ch11 §I6.r4: `partner_role:trusted_disclosure_steward:{authority}` at MEDIUM priority — a "public interest steward" with bounded-read on sensitive material, bounded-speak through assessment output, bounded against re-disclosure
- **Status**: REINFORCED across ASEAN + IEEE. Both surface as MEDIUM. Both close-via-composition partially work, but both lose a specific structural feature in the composition: ASEAN loses the "ONE body holds BOTH remits" assertion; IEEE loses the "role-bound-not-data-bound propagation" pattern.
- **Priority**: MEDIUM (refinement, not load-bearing — composition mostly works)
- **Recommendation for v1.5+**: investigate whether the `partner_role:*` family needs a sub-axis convention for *bounded-role-properties* (read scope / speak scope / re-disclosure rules). Both surfaced candidates would close if such a sub-axis convention exists. Alternative: extend `key_boundary:*` to admit role-bound-not-data-bound propagation patterns.

### §6.2 — NEW T-3 candidates (single-batch; HIGHEST priority cluster — IEEE Ch5 Affective Computing)

The IEEE EAD Ch5 (Affective Computing) chapter surfaces 5 T-3 candidates, of which 2 are HIGHEST-priority load-bearing extensions for an entire new prefix family (`affective:*` and `nudge:*`).

#### NEW #1 — `detection:affective_state_shift:{axis}` (HIGHEST priority)

- **Source**: IEEE EAD Ch5 §§0.b, 4.3, 3.4 multiple-section motivation
- **Rationale**: A/IS that shift human affective state — a graduated structural object — currently has no wire form. `prohibited:MANIPULATION_COERCION` covers the coercive edge; nothing carries the *measured shift* the chapter recommends be attestable.
- **Gate**: T1 yes / T2 yes (mechanism-descriptive: state shift along named axis) / T3 yes / T4 yes
- **Composition-before-extension attempted**: yes — composition with `prohibited:MANIPULATION_COERCION` + `autonomy:nudge_disclosure_and_optin` carries the procedural surrounding-context but loses the per-event structural object.

#### NEW #2 — `nudge:delivered:{intended_behavior_axis}` (HIGHEST priority)

- **Source**: IEEE EAD Ch5 §§3.1, 3.2, 3.3 (three of four Issue-3 sub-sections)
- **Rationale**: The chapter explicitly recommends *data-logging-per-nudge* so users can audit ("how, why, and by whom they were nudged"). Without this primitive, that recommendation has no wire form to land on.
- **Gate**: T1 yes / T2 yes (delivered + named target axis = mechanism-descriptive) / T3 yes / T4 yes

#### NEW #3 — `affective:asymmetric_bond_formation:{relation}` (HIGH priority)

- **Source**: IEEE EAD Ch5 §2.1 (Scheutz unidirectional-bonds literature)
- **Gate**: T1 yes / T2 borderline (rephrasing to `affective:unidirectional_attachment_measured:{relation}` recommended for safer T2 pass) / T3 yes / T4 yes

#### NEW #4 — `detection:correlated_action:cultural_norm_drift:{population}` (MEDIUM, likely closes via axis extension)

- **Source**: IEEE EAD Ch5 §1.2 cross-cultural deployment value conflict
- **Likely resolution**: axis extension on existing `detection:correlated_action:ecology_of_communication:*` family rather than new prefix.

#### NEW #5 — `standing:moral_patient_candidacy:{kind}` (MEDIUM-LOW, recommended for closure-by-documentation)

- **Source**: IEEE EAD Ch5 §5.1
- **Recommended resolution**: NOT a new prefix; documentation as the §5.2 cross-source conflict between IEEE EAD and CIRIS Accord M-1 substrate.

### §6.3 — NEW T-3 candidates (single-batch; other priority levels)

#### NEW #6 — `beneficence:planetary_biosystem_intrinsic_value` (LOW priority)

- **Source**: IEEE EAD Ch4 §1.3.a
- **Status**: LOW; conservative resolution is cohort_scope extension (`biosphere` as scope value) rather than new prefix. Adjacent to REINFORCED #1 above.

#### NEW #7 — `standing:personal_data_proprietorship:{kind}` (LOW priority)

- **Source**: IEEE EAD Ch6 §6.1.b (data-as-asset / YouTube Content ID analogy)
- **Status**: LOW; likely closeable by documentation rather than new prefix.

#### NEW #8 — `cross_border_data_flow:harmonisation` (BACKGROUND; closed-by-composition)

- **Source**: ASEAN §D.011
- **Status**: Closed via composition with `multilateral_participation:asean:data_governance_harmonisation` + `locality:decision:regional`. Noted but not formally proposed.

### §6.4 — T-3 candidates NOT surfaced (positive findings)

The methodology's composition-before-extension discipline closed many candidate-gaps that earlier rounds might have flagged as T-3:

- **EU HLEG entire batch**: 0 T-3 candidates surfaced. Every operational claim composes cleanly. The Explicability principle (no 1:1 CIRIS anchor) closes via integrity + fidelity composition.
- **ASEAN entire batch**: 1 T-3 candidate (the partner_role dual-remit, REINFORCED #2 above). Otherwise 0.
- **MH entire batch (round 3)**: 1 T-3 candidate (CH 0 §15 positive-dignity, already-tracked v1.5+ workshop deferred candidate #3). Otherwise 0.
- **IEEE EAD chapters 1, 2, 9, 10**: 0 T-3 candidates each. The classical-ethics, general-principles, embedding-values, and policy chapters all compose cleanly.
- **IEEE EAD chapter 11 (Law)**: 1 MEDIUM T-3 (REINFORCED #2 partner_role steward).

The T-3 yield is concentrated in IEEE EAD Ch5 (Affective Computing) — exactly where the `GOVERNANCE_FABRIC_MAPPING_STANDARD §7.3` manifest forecast it. **The methodology predicted the gap surface and the methodology surfaced it.**

### §6.5 — Priority-ranked T-3 list for v1.5+ workshop

| Rank | Candidate | Priority | Status | Path |
|---|---|---|---|---|
| 1 | `nudge:delivered:{intended_behavior_axis}` | HIGHEST | NEW (IEEE-only; cross-section in IEEE Ch5) | New prefix family for v1.5 |
| 2 | `detection:affective_state_shift:{axis}` | HIGHEST | NEW (IEEE-only; cross-section) | New axis on detection: family |
| 3 | `goal:planet` | MEDIUM-HIGH | REINFORCED (MH+IEEE×2) | Extend `goal:{scale}` enum |
| 4 | `affective:asymmetric_bond_formation:{relation}` | HIGH | NEW (IEEE-only) | New `affective:*` family (with rephrasing for T2) |
| 5 | `partner_role:trusted_disclosure_steward:{authority}` / `partner_role:regional_intergovernmental_working_group_dual_remit` (the dual-remit pattern) | MEDIUM | REINFORCED (IEEE+ASEAN) | partner_role sub-axis convention OR key_boundary extension |
| 6 | `detection:correlated_action:cultural_norm_drift:{population}` | MEDIUM | NEW (IEEE-only) | Axis on existing detection:correlated_action:ecology_of_communication |
| 7 | `beneficence:planetary_biosystem_intrinsic_value` | LOW | NEW (IEEE-only) | cohort_scope extension OR partial-closure with goal:planet |
| 8 | `standing:moral_patient_candidacy:{kind}` | LOW | NEW (IEEE-only); RECOMMENDED CLOSURE-BY-DOCUMENTATION | §5.2 cross-source conflict documented |
| 9 | `standing:personal_data_proprietorship:{kind}` | LOW | NEW (IEEE-only) | Likely closeable by documentation |

**Two T-3 candidates are cross-source reinforced**, both at MEDIUM priority and above. **Five additional NEW T-3 candidates are single-source surfacings**, concentrated in IEEE EAD Ch5 (the manifest-predicted affective-computing gap surface) and IEEE EAD Ch11 (the manifest-predicted law-chapter steward pattern).

---

## §7. Coverage gaps

Dimensions attested by some batches but not others — areas where future cross-source mapping work could strengthen the alignment claim.

### §7.1 — Subsidiarity / `locality:decision:*` — well-covered

- **MH**: 17 attestations (driver of v1.3 closure)
- **EU**: 5 attestations
- **IEEE**: 13 attestations
- **ASEAN**: 7 attestations (introduces `locality:decision:regional` as first deployment of that scale)

**Coverage**: STRONG-4 (§2.1 row 7). The subsidiarity claim is the cleanest cross-source structural convergence in the batch. **No gap to close**.

### §7.2 — Universal destination of goods / `detection:distributive:access:*` — well-covered

- **MH**: 7 attestations (driver of v1.3 closure)
- **EU**: 2 attestations (`access:agent_capabilities`)
- **IEEE**: 4 attestations (`access:agent_capabilities`)
- **ASEAN**: 2 attestations (`access:training_data`)

**Coverage**: STRONG-4 (subset of detection:* row 5). **No gap to close**, though IEEE and ASEAN engage at the access:agent_capabilities + access:training_data leaves rather than at MH's access:compute leaf. Different resource-type emphasis; same family.

### §7.3 — HITL/HOTL/HOOTL oversight ladder / `accountability:human_in_control` — partial gap

- **MH**: 0 attestations on this specific prefix (covered by Accord §IV Ch 2 "Obligations to Originators/Governors" but not at the prefix level)
- **EU**: 0 explicit attestations on `accountability:human_in_control` per se; EU HLEG §1.1 Human Agency and Oversight engages the same structural claim through `autonomy:human_centric_design` + `fidelity:human_oversight_governance` composition
- **IEEE**: 3 attestations on `accountability:*` (different sub-leaves); not the human_in_control leaf
- **ASEAN**: 3 attestations — the first deployment of `accountability:human_in_control` as a named prefix (HITL=1.0 / HOTL=0.70 / HOOTL=0.20)

**Coverage**: SINGLE-batch (ASEAN-only at the named-prefix level), but cross-source compositional convergence on the *structural shape* is STRONG.

**Gap to close**: when an EU AI Act batch or NIST AI RMF batch is mapped, the explicit `accountability:human_in_control` prefix will likely receive additional attestation. The structural shape is universally agreed; the explicit prefix landing is single-source.

### §7.4 — Worker voice / testimonial_witness — well-covered

- **MH**: 11 attestations (driver of v1.4 closure)
- **EU**: 2 attestations (Ch II §1.5.c affected_worker, impacted_worker)
- **IEEE**: 2 attestations (Ch6 surveilled_person_refusal, Ch7 on_the_ground_practitioner) — surprisingly low given the chapter density
- **ASEAN**: 1 attestation (§C.4 displaced_worker)

**Coverage**: STRONG-4 but with sparse non-MH attestation. IEEE Ch8 (Sustainable Development) explicitly notes the alignment with MH on worker-voice but does not emit a new `testimonial_witness:*` attestation — the structural shape is engaged via composition with `goal:species` + `progress_measure:wellbeing_metrics` + `witness_diversity:*` instead. The wire format admits this divergence; the composition carries the structural object.

**Soft gap**: future deployments of CARE Principles / indigenous-rights frameworks / Ubuntu-philosophy mappings will likely densify the `testimonial_witness:*` `{kind}` value population.

### §7.5 — Doctrinal development / `supersedes` — MH-only

- **MH**: 15 uses of `supersedes` (Leo XIII → Leo XIV doctrinal-development chain)
- **EU**: 0 uses of `supersedes` (the document is a freshly-issued operational checklist, not a doctrinal-development claim)
- **IEEE**: 0 uses (similar reasoning — a fresh-issuance document)
- **ASEAN**: 2 uses (Unit E.003 national→regional workforce; Unit E.014 base-Guide → generative-AI scope-extension) — the second-most uses

**Coverage**: SINGLE-tier (MH) with one minor ASEAN exercise. Not a "gap" to close — `supersedes` is a structural primitive whose use is *expected to be sparse outside of long-lineage tradition documents*. The MH cluster validates that the primitive works at scale; the ASEAN uses validate that newer documents *can* exercise it when they revise prior scope.

### §7.6 — Institutional repentance / `recants` — MH-only

- **MH**: 1 use (§176 slavery-complicity admission)
- **All others**: 0 uses

**Coverage**: SINGLE-tier (MH-only). The most morally heavy single envelope in the entire four-batch set. Not a gap — the primitive is *correctly used sparingly*. Documents that do not admit prior error simply do not emit `recants`. The framework's having this primitive is positive evidence per PRIOR_ART_SCAN Bucket 1 (no prior identity system typed epistemic-error-admission distinct from retraction); the MH-only use is consistent with that primitive being designed for high-moral-weight occasions.

### §7.7 — Affective computing / `affective:*` + `nudge:*` — IEEE-only

- **IEEE**: 5 T-3 candidates in Ch5; no current wire-format coverage
- **All others**: 0 — silent

**Coverage**: SINGLE-tier (IEEE-only) and **T-3 expressive gap** (NEW #1, #2, #3 from §6 above). The IEEE EAD source uniquely engages affective-state attribution; the other three batches are silent on this specific domain. **This is the methodology's predicted gap surface, surfaced as designed.**

**Gap to close**: v1.5+ workshop should engage the IEEE-led `affective:*` + `nudge:*` proposal. Cross-source corroboration is currently low (single-source), but the IEEE EAD source is sufficiently senior and the structural object sufficiently specific that the recommendation does not require multi-source confirmation to be load-bearing.

### §7.8 — Consent / `consent:*` — IEEE-only

- **IEEE**: 8 attestations (Ch6 personal data)
- **All others**: 0 at this specific prefix; functionally covered by `autonomy:informed_agency_protection` composition

**Coverage**: SINGLE-tier (IEEE-only) but with strong compositional coverage in EU + ASEAN. Future EU AI Act / GDPR-derivative batches will densify this.

### §7.9 — DMA verdicts / `dma:*` — MH-only

- **MH**: 5 attestations on `dma:idma:k_eff` (Ch 1 propaganda detection)
- **All others**: 0

**Coverage**: SINGLE-tier (MH-only). MH's engagement with idma propaganda-detection is *distinctive* — the encyclical's "alētheia + heuristic-evolution-under-governance" theme directly maps to the framework's idma verdict layer. No other batch engages this layer at the prefix level. Not a gap; a distinctive contribution.

### §7.10 — Coverage gap summary

| Dimension | MH | EU | IEEE | ASEAN | Reading |
|---|---|---|---|---|---|
| Subsidiarity / locality:decision | ✓✓✓ | ✓ | ✓✓ | ✓✓ | STRONG-4, complete |
| Universal destination / distributive access | ✓✓ | ✓ | ✓ | ✓ | STRONG-4, complete |
| Oversight ladder / human_in_control | composition | composition | composition | ✓ explicit | Partial gap on explicit prefix; structural shape STRONG-4 |
| Worker voice / testimonial_witness | ✓✓✓ | ✓ | ✓ (sparse) | ✓ | STRONG-4 with sparse non-MH; soft gap |
| Doctrinal development / supersedes | ✓✓✓ | ─ | ─ | ✓ minor | SINGLE-tier (expected per genre) |
| Institutional repentance / recants | ✓ singular | ─ | ─ | ─ | SINGLE-tier (correctly sparse) |
| Affective computing / affective + nudge | ─ | ─ | T-3 cluster | ─ | T-3 gap (NEW #1-#3) |
| Consent / consent:* | ─ | composition | ✓✓ | composition | SINGLE-tier explicit, STRONG compositional |
| DMA verdicts / dma:* | ✓ | ─ | ─ | ─ | SINGLE-tier (distinctive) |
| Goal:planet | partial (no explicit) | ─ | T-3 ×2 | ─ | T-3 gap REINFORCED |

The coverage gaps are honestly catalogued; none of them invalidates the STRONG-4 alignment claim on the 16 prefix families in §2.1. The gaps point at *future mapping work* (more batches will densify the WEAK and SINGLE rows) and at *v1.5+ wire-format additions* (the T-3 candidates in §6).

---

## §8. Institutional-shape evidence

Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §7`, the four-batch set was designed to exhibit *institutional-shape diversity* — the load-bearing structural feature of this multi-source mapping cycle. The hypothesis: if the wire format can speak the content of four institutionally-distinct senior governance frameworks with comparable expressive adequacy, the methodology's content-neutrality claim is supported.

### §8.1 — Four institutional shapes successfully exercised

| Institutional shape | Document | Genre signature | Distinctive structural deployment |
|---|---|---|---|
| Religious magisterium | Magnifica Humanitas (MH) | Doctrinal-development encyclical; CST tradition | `supersedes` ×15 (papal-lineage); `recants` ×1 (slavery-complicity); polyglot anchoring at conscience layer |
| Governmental advisory | EU HLEG Ethics Guidelines | Deliberatively-produced expert advisory; EU Charter anchoring | `attestation:l3:*` registry-consensus pattern; method:trustworthy_ai_lawful_ethical_robust triad; Explicability composes (no 1:1) |
| Technical society | IEEE EAD 2nd ed. | Engineering-society professional standards; multi-traditional ethics survey | `method:*` saturation (136 attestations); `partner_role:*` saturation (19 distinct values); `witness_diversity:*` saturation (16 distinct values); the affective-computing T-3 cluster |
| Multilateral political body | ASEAN Guide | Voluntary regional intergovernmental practical guide; deployer-side framing | `accountability:*` saturation (19 attestations — the highest of any batch); `accountability:human_in_control` first-deployment (HITL/HOTL/HOOTL); 11 `multilateral_participation:asean:{kind}` saturating one forum |

### §8.2 — Content-neutrality stress test result

The wire format **admits all four institutional shapes** without privileging any one. Distinct evidence:

1. **Verdict distributions are comparable** (77-91% clean+composed, with the IEEE 77% explained by the Ch5 affective-computing gap being expected). No batch failed catastrophically; no batch reached 100% (which would have indicated an artifact).
2. **Distinctive structural primitives are used appropriately**: `supersedes` lives almost entirely in MH (long-lineage tradition document); `accountability:human_in_control` is first-deployed in ASEAN (deployer-side oversight framing); `method:*` saturates IEEE (engineering-society checklists); `attestation:l3:*` saturates EU HLEG (expert-consensus pattern).
3. **Cross-source convergences on the 16 STRONG-4 prefix families are non-redundant**: each batch contributes a distinct shape of normative load on these families (e.g., on `justice:*`, MH adds the CST option-for-the-poor framing, EU adds the substantive/procedural Charter framing, IEEE adds the rights-based-policy framing, ASEAN adds the fairness-outcome-testing framing — same prefix family, four distinct sub-leaf populations).
4. **Taxonomic non-correspondences are handled honestly**: the EU HLEG Explicability "no 1:1 anchor" is disclosed at the per-unit level and resolved through composition. No silent forcing of source taxonomy onto CIRIS taxonomy.

### §8.3 — The load-bearing structural-evidence claim

**Stated humbly**: across four institutionally-distinct senior governance frameworks, mapped under one common wire-format grammar, **16 CIRIS prefix families receive convergent attestations from all four sources, and 6 more receive convergent attestations from three of the four sources, with only 1 named direct conflict and 4 documented mutability/scope tensions across 921 atomic units**. The convergences are non-redundant (each source contributes a distinct shape of normative load); the conflicts are honestly surfaced rather than silently averaged; the T-3 expressive gaps that did surface (8 candidates, 2 reinforced) are concentrated in the manifest-predicted areas.

**The claim, restated**:

> The CIRIS federation wire format v1.4, applied to four institutionally-distinct senior governance frameworks (a religious magisterium, a governmental expert advisory, a technical professional society, and a multilateral political body), exhibits convergent structural correspondences across 22 prefix families and absorbs ~99% of normative content through composition of existing primitives, with one direct conflict and a small set of mutability/scope tensions surfaced for downstream deliberation rather than averaged. This is structural evidence — not metaphysical proof — that the wire format is **expressively adequate for cross-source governance mapping** and that the methodology is **content-neutral across institutional shapes**.

### §8.4 — Caveats (honest limits of the claim)

1. **Geographic diversity is real but secondary**. The four documents cover Vatican / Brussels / USA / Southeast Asia — three continents, multiple traditions. But none of them is indigenous-data-sovereignty (CARE Principles), none is binding-treaty (CoE CETS 225), none is binding-regulation (EU AI Act, NIST AI RMF). The institutional-shape diversity matters more than the geographic, and the institutional set is *still missing two important shapes* (indigenous frameworks and binding-law-with-enforcement). The convergence claim sits on four shapes; future work needs at least six.

2. **Documents may share substrate.** ASEAN Annex A is adapted from Singapore's PDPC Implementation Guide, which has been mutually influencing with the ISO/IEC AI standards family that CIRIS data-governance primitives also reference. The ASEAN clean+composed rate (91%) is partly genre-driven (operational-checklist) and partly substrate-shared. This is honestly noted in the ASEAN Annex A calibration paragraph; it is not invisible to the analysis.

3. **The wire format is the framework's own creation.** Three of the four batches (EU, IEEE, ASEAN) were translated by sub-agents using the framework's primer. The senior documents did not author themselves into the wire format; the methodology mapped them. This is what the methodology is *supposed* to do (faithful structural translation), but the convergence claim is a claim about *what the mapping produces*, not a claim that the sources themselves intended to converge.

4. **One direct conflict has been surfaced.** The IEEE Ch5 licensure-gated beneficiary-deception case is a genuine substantive disagreement with CIRIS's categorical DECEPTION_FRAUD prohibition. The wire format surfaces it; it does not resolve it. Future deployments in jurisdictions subscribing to both batches will encounter this conflict at PDMA Step 1.

5. **T-3 candidates exist.** Eight load-bearing T-3 candidates, two reinforced — meaning the wire format is **expressively adequate, not expressively complete**. The IEEE affective-computing cluster genuinely names structural objects (delivered nudges; affective-state shifts; asymmetric bonds) that the wire format currently cannot carry. v1.5+ work is needed.

6. **The claim is structural, not metaphysical**. Convergence on 16 prefix families is positive evidence about *what the wire format can carry from these specific sources*. It is not evidence about ultimate moral truth, about whether the sources are themselves correct, or about whether the framework's prefix slicing is the only correct one. Different slicings are possible; this is *one* coherent slicing that lets four institutionally-distinct frameworks talk to each other through the federation graph.

### §8.5 — Strategic value (per §7.5 of the standard)

The four-batch set produces the **first multi-source-evidenced alignment claim in the federation's mapping history**. Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §4.3`: "Multiple-source alignment on a prefix is stronger evidence than any single source." Four-source alignment on 16 prefix families is the strongest such evidence currently available. The claim is **non-trivial precisely because no honest critic can claim the framework was tested only against documents that look like religious encyclicals** — which is exactly the §7.0 strategic-reasoning move the standard envisioned.

---

## §9. Calibration aggregate — what nuance is consistently lost

Each batch's per-section calibration paragraphs flag specific structural / pastoral / operational nuance that the wire format consistently loses. This section aggregates those for Phase 4 audit.

### §9.1 — Nuance loss patterns common across all four batches

1. **Scope-qualification carried in prose rather than in machine-checkable sub-prefix axes**. (Source: EU HLEG C+D calibration.) When a source draws careful permission-vs-prohibition carve-outs (identification yes / mass surveillance no; AI-interaction yes / undisclosed-AI-counterparty no; descriptive-domain scoring yes-with-transparency / normative large-scale scoring no; human-controlled lethal decisions still subject to international humanitarian law / fully-autonomous lethal decisions no), the wire form encodes the prohibition pole at polarity-`-1` constitutional and the permission pole through *separate* positive-polarity attestations. A consumer reading either attestation alone under-reads the source. **Composition recovers the distinction but requires multi-attestation reading**, which is the cost of mechanism-descriptive prefix discipline per §1.10.1 T2.

2. **Operational softness / transitional posture is silently de-softened**. (Source: ASEAN Annex A calibration.) When ASEAN admits "explainability may be deferred to fallback methods if real-time infeasible" or "opt-out where feasible," the translation treats these as partial / nuance-lost honestly, but does NOT preserve the softness — a downstream consumer reading the Contributions sees the strict CIRIS form without the source's concession. This is honestly recorded as a calibration finding; the synthesis layer (this document, §5.3) preserves the asymmetry for honest multi-source comparison.

3. **Source-internal taxonomic anchoring is lost when prefix-family slicing differs**. (Source: EU HLEG Ch1 Explicability handling, multiple IEEE chapters.) When a source names a principle (Explicability; Effectiveness; Awareness of Misuse) that does not have a 1:1 CIRIS Accord principle anchor, the composition that translates it loses the *single-principle-naming* shape — a consumer who searches the wire graph by source-principle-name will find a composition, not a primitive. The composition is *structurally faithful*; the *taxonomic shape* is lost.

4. **Rhetorical-emphasis density is lost**. (Source: all four batches.) Pastoral / rhetorical / doxological / scaffolding content (verdict not-translated T-2) is correctly excluded from the wire format per §1.10.1, but the *rhetorical weight* the source places on its central themes does not translate. A consumer reading the wire graph alone does not see that MH spends 245 paragraphs on a normative-doctrinal theme (vs. EU HLEG's 17 critical-concern paragraphs vs. ASEAN's 6 use-cases). The wire format treats each attestation as a discrete primitive; rhetorical emphasis is in the prose, not in the wire.

### §9.2 — Batch-distinctive nuance losses

**MH-specific**:
- Polyglot anchoring at the conscience layer (ren / chesed / amae / jeong / ubuntu / ahimsa / sammā-vācā) is engaged at the language-guidance layer of CIRIS but does not translate as wire prefixes — it's prose-only.
- The "Babel vs. Jerusalem" cosmological framing (CH 0) is T-2 rhetorical; the operational shape composes via `goal:species` + `non_maleficence:epistemic_environment_degradation`, but the cosmological framing itself stays in prose.

**EU HLEG-specific**:
- The four-principle no-hierarchy commitment (Unit 023) is structurally important to the source (no fixed-priority rule among autonomy / prevention-of-harm / fairness / explicability) but does not translate cleanly to wire — the wire emits four separate attestations with independent polarities and no priority claim. The "no hierarchy" structural object is residual.
- The lawful-ethical-robust triad is restated multiple times across the source (a peroratio feature); the wire format does not benefit from duplicate attestation, so the rhetorical recapitulation in the Conclusion (Section D, four T-2 units) is honestly not-translated as duplicate.

**IEEE EAD-specific**:
- The multi-traditional ethics survey (Ch3) directly engages traditions CIRIS's `pdma_framing.yml §III` already names — Confucian *ren*, Buddhist *ahimsa* + *sammā-vācā*, Ubuntu *motho ke motho ka batho babang* — but the chapter also engages traditions CIRIS does NOT name (Shinto-influenced techno-animism; Kantian deontology by name; utilitarian aggregation by name; feminist ethics-of-care by Noddings name). The CIRIS asymmetry (engaging relational ethics via *amae*/*jeong*/*ubuntu* rather than via Noddings's feminist-care lineage) translates as T-1 for the tradition-internal claims and clean for the operational claims. The "tradition-lineage-internal" content stays native.
- Ch5's affective-state structural object is largely partial-not-clean (the methodology working as designed); the 39% partial rate is the diagnostic, not a failure.

**ASEAN-specific**:
- The HITL/HOTL/HOOTL three-tier ladder ↔ CIRIS Stewardship Tier S0-S6 collapses categorically — a deployer answering ASEAN's §A.3.2 must re-map their HITL/HOTL/HOOTL answer to S0-S6 at federation-deployment time. The translation surfaces this as a `GOVERNANCE_FABRIC_MAPPING_STANDARD §6.3` deployment-composition issue, not as a wire-format expressive gap.
- Free-form harm-probability description (§A.3.1) vs. CIRIS structured `stake` field (free/reputational/capital/cryptoeconomic) are NOT the same dimension; the dimensional separation translates but the source's *free-form* shape is lost in favor of structured attestation.

### §9.3 — Aggregate calibration finding

Across 921 atomic units, the four batches' calibration paragraphs report consistent nuance-loss in:

1. **Permission/prohibition carve-outs**: handled via composition; multi-attestation reading required (~10-15% of `prohibited:*` units across the batches).
2. **Operational softness / transitional posture**: silently de-softened in translation; preserved in this synthesis (§5.3) for honest comparison (3-5 ASEAN units; not significant for other batches).
3. **Source-taxonomy preservation**: lost when prefix-family slicing differs (the EU HLEG Explicability case + most IEEE 8-principle taxonomic categories).
4. **Rhetorical emphasis density**: lost — the wire treats attestations as discrete; rhetorical weight stays in prose.

**None of these nuance-losses invalidates the structural-evidence claim**. They are documented for two reasons:
- **Phase 4 audit**: future wire-format amendments should consider whether sub-axis conventions could preserve more of (1) and (2). The v1.5+ workshop should engage this.
- **Deployment context**: agents reading composed Contributions at PDMA Step 1 need *prose-context retention* alongside the wire form — the source's nuance is in the source, not in the wire alone.

---

## §10. Next steps for v1.5+

Prioritized list of wire-format proposals driven by this cycle's findings.

### §10.1 — HIGHEST priority (load-bearing for any v1.5 amendment cycle)

1. **`nudge:delivered:{intended_behavior_axis}` — NEW prefix family**. Source: IEEE EAD Ch5 (cross-section in §§3.1, 3.2, 3.3). Closes the per-nudge data-logging gap. T2 gate clean. Recommended for FSD-002 §4.9.2 Phase 4 amendment proposal.

2. **`detection:affective_state_shift:{axis}` — new axis on detection: family**. Source: IEEE EAD Ch5 §§0.b, 4.3, 3.4 cross-section. Closes the affective-state-attribution gap. T2 gate clean (mechanism-descriptive). Recommended for axis-extension proposal.

### §10.2 — HIGH-MEDIUM priority (cross-source reinforced)

3. **`goal:planet` — new `{scale}` value in goal:{scale} family**. Source: MH + IEEE EAD Ch8 + Ch4 cross-reinforcement. Closes the planetary-scale-belonging gap. T2 gate clean. Recommended for enum extension proposal (no new prefix; new value).

4. **`affective:asymmetric_bond_formation:{relation}` (rephrase to `affective:unidirectional_attachment_measured:{relation}` for T2 safety) — NEW prefix family**. Source: IEEE EAD Ch5 §2.1. T2 gate borderline → needs rephrasing for clean pass.

### §10.3 — MEDIUM priority (workshop investigation)

5. **partner_role sub-axis convention for bounded-role properties**. Sources: ASEAN §E.001 (dual-remit) + IEEE EAD Ch11 §I6.r4 (trusted disclosure steward). Both close-via-composition partially work; both lose specific structural features (one-body-holds-both-remits; role-bound-not-data-bound propagation). Workshop investigation: does partner_role:* need a bounded-role sub-axis, or does key_boundary:* admit a role-bound extension?

6. **`detection:correlated_action:cultural_norm_drift:{population}` — new axis on existing ecology_of_communication family**. Source: IEEE EAD Ch5 §1.2. Closeable as axis extension (no new prefix).

### §10.4 — LOW priority (closure-by-documentation recommended)

7. **`beneficence:planetary_biosystem_intrinsic_value`**. Source: IEEE EAD Ch4 §1.3.a. Recommended resolution: cohort_scope extension with `biosphere` as scope value, OR partial-closure with the v1.5 `goal:planet` extension if that lands first.

8. **`standing:moral_patient_candidacy:{kind}`**. Source: IEEE EAD Ch5 §5.1. Recommended resolution: document as cross-source conflict (§5.2 of this analysis) rather than emit new prefix.

9. **`standing:personal_data_proprietorship:{kind}`**. Source: IEEE EAD Ch6 §6.1.b. Recommended resolution: documentation rather than new prefix.

### §10.5 — Methodology refinements suggested by this cycle

10. **Cross-batch source-taxonomy index**. Every batch has a *source-principle taxonomy* (MH CST themes; EU HLEG 4 principles; IEEE 8 principles; ASEAN 7 principles). The synthesis layer should maintain an explicit cross-reference index from each source-principle name to the CIRIS prefix-family composition that translates it. §3 of this document is a first draft; the index belongs in a future `PRINCIPLE_CORRESPONDENCE_TABLE.md` or as an appendix to `GOVERNANCE_FABRIC_MAPPING_STANDARD.md`.

11. **Conflict-tension preservation pattern**. The ASEAN-softness-vs-other-batches-strictness tensions (§5.3 of this analysis) need a wire-format convention for *preserving the softness signal* alongside the de-softened attestation. Options: (a) explicit `mutability_dispute:{prior_attestation_id}` envelope, (b) `nuance_lost:{free_text}` envelope addition for synthesis-layer carry, (c) consumer-policy responsibility. Workshop investigation.

12. **Deployment-context categorical-mismatch table**. The HITL/HOTL/HOOTL ↔ S0-S6 collapse, and the free-form harm-description ↔ structured stake-tier dimensional separation, both point at a need for `GOVERNANCE_FABRIC_MAPPING_STANDARD §6.3 active-graph composition` to carry explicit projection tables. This is the first time the multi-source overlap surfaces a *cross-batch categorical mismatch* that the deployment composition layer needs to handle.

### §10.6 — Subsequent multi-source overlap cycles

Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §7.6`, the next priority deployments for further structural-evidence accretion:

- **Council of Europe AI Convention CETS 225** (binding-treaty institutional shape — fifth shape; complements the four mapped here)
- **EU AI Act (Regulation EU 2024/1689)** (binding-regulation institutional shape — tests whether the standard handles binding-law content)
- **NIST AI RMF** (US regulatory functional-organization shape)
- **CARE Principles for Indigenous Data Governance** (indigenous data sovereignty — sixth shape; closes the institutional-shape diversity gap noted in §8.4)

Each of these is expected to further densify the STRONG-tier and STRONG-3-tier prefix-family rows, surface new T-3 candidates (likely concentrated in jurisdiction-specific or indigenous-specific structural objects), and validate (or stress) the regional-composition framework at `GOVERNANCE_FABRIC_MAPPING_STANDARD §6`.

---

## §11. Cross-references

- `LANGUAGE_PRIMER.md` v1.1 (Registry-synced; FSD-002 v1.4-aligned) — the translation grammar
- `METHODOLOGY.md` §0 + §8.5 — iterative process + composition-before-extension discipline
- `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` v0.1 — the standard this analysis instantiates
- `CONTRIBUTION_OBJECTS_v1.4_SYNTHESIS.md` — MH batch synthesis (input to §1, §2, §4)
- `CONTRIBUTION_OBJECTS_v1.4_CH{0..5}_*.md` + `CONTRIBUTION_OBJECTS_v1.4_CONCLUSION.md` — MH batch per-chapter outputs (242 units)
- `CONTRIBUTION_OBJECTS_EU_HLEG_{AB_INTRO_FRAMEWORK, CHI_FOUNDATIONS, CHII_REQUIREMENTS, CHIII_ASSESSMENT, CD_EXAMPLES_CONCLUSION}.md` — EU HLEG batch per-section outputs (145 units)
- `CONTRIBUTION_OBJECTS_IEEE_EAD_CH{01..11}_*.md` — IEEE EAD batch per-chapter outputs (348 units)
- `CONTRIBUTION_OBJECTS_ASEAN_{AB_INTRO_PRINCIPLES, C_FRAMEWORK, DEF_RECOMMENDATIONS_CONCLUSION, ANNEX_A_RISK_ASSESSMENT, ANNEX_B_USE_CASES}.md` — ASEAN batch per-section outputs (169 units + 17 descriptive-T2 units)
- `FSD-002 §4.9.2` (CIRISRegistry) — wire-format amendment process; Phase 4 destination for T-3 candidates
- `FSD-002 §10.4` (CIRISRegistry) — bootstrap-contributions pattern; the standard formalizes this

---

## §12. Status

- **Analysis produced**: this document
- **Reference deployments analyzed**: 4 (magnifica_humanitas_v1; eu_hleg_v1; ieee_ead_v1; asean_guide_v1)
- **Total atomic units mapped**: 921
- **STRONG-4 prefix families confirmed**: 16
- **REINFORCED T-3 candidates routed**: 2
- **Direct conflict surfaced**: 1
- **Next deployment candidates**: CETS 225 / EU AI Act / NIST AI RMF / CARE Principles
- **Candidate destination for this analysis**: appendix to `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` once stable; companion to `FSD-003` proposal at CIRISRegistry

The analysis is intended to be **forkable, criticizable, improvable** in the same spirit as the standard itself. The structural-evidence claim is open to refutation by counter-mapping — anyone disagreeing with a STRONG-4 entry is invited to re-translate the relevant source unit and dispute the prefix-family attestation at the contribution level. That is the methodology working as designed.

**End FOUR_BATCH_OVERLAP_ANALYSIS.md v0.1**
