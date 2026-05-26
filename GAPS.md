# GAPS.md — Consolidated Findings and Proposed Enhancements

**Version**: 3.0
**Date**: 2026-05-25
**Status**: Locked — reflects v2 chapter mapping (under METHODOLOGY.md 7-layer discipline) plus v2.1 re-evaluation of four items.
**Methodology**: See `METHODOLOGY.md` and `MISSION.md` §1.3.

---

## 0. What is new in v3

v2.0 was based on chapter mappings that read structural files (MISSION.md, schemas, code paths) but missed the operative text — DMA prompts, language_guidance, conscience faculties, prohibitions, safety_interpret. v2.1 corrected this through:

1. The v2 chapter mappings (re-run by Sonnet sub-agents under the seven-layer discipline in METHODOLOGY.md)
2. The v2.1 re-evaluation of four items where the operational shape was confirmed comprehensive even though the Accord doesn't yet name it explicitly

This document supersedes v2.0. Headline changes:

- **Six v1 gaps close or shrink to WEAK_ALIGN** under the v2 discipline:
  - C-1 (information ecosystem) → IDMA propaganda-detection at multiple layers
  - C-2 (attention economy) → `prohibitions.py` already names `dark_patterns`, `addictive_design`, `habit_forming`, `compulsion_trigger` as `NEVER_ALLOWED`
  - E-1 (discourse de-escalation) → `language_guidance` first-sentence tone lock + never-echo-stigma + ratification-decline posture
  - E-3 (dialogue/negotiation) → CIRISNodeCore decision-hierarchy primitives
  - G-1 (compute/energy) → Accord §IV Ch 2 + LLMBus tracking
  - Plus §§110–111 disarming AI (was in Cluster A spillover) → NO KINGS invariant + multi-layer

- **One new gap surfaces** from v2 Ch 1:
  - F-3 Structures of sin / institutional injustice analysis (MH §36) — PDMA is individual-action-scoped; no Accord clause for aggregate / institutional pattern audit

- **Family as constitutive structure** and **labor dignity as expression of personhood** are explicitly named as confirmed-persistent gaps that even the v2 discipline does not close. They require Accord-level work via the Constitutive Continuity principle proposed in ACCORD_UPDATE.md §2.

- **Net gap count shrinks** from 22 (v2.0) to **approximately 14** active gaps that survive the v2 discipline.

---

## 1. Cluster A — Scale-routing and decision-locality

### Gap A-1: No Accord principle naming lowest-feasible-scale decision routing

**Status**: `GAP_ACCORD` confirmed-persistent.

**Operational shape exists** (per v2.1 re-evaluation): PDMA Step 5 (Relational balance) considers scope; CIRISEdge peer-to-peer no-broker is the structural shape at transport; CIRISNodeCore "no central scorer (post-F-11)" is the federation-consensus shape; the deferral pipeline routes to humans but not yet to smaller-scope agents.

**What's missing**: Accord-level principle that names "lowest feasible scale" as a decision-routing obligation. The architecture enforces the shape; the doctrine doesn't name it.

**Evidence**: MH §§68–72.

**Proposed enhancement**: Add Accord principle **Decision Locality** in §I Ch 1. Operationally, extend DSASPDMA with a scale-routing classification step. New `needs_category` value: `SCALE_ROUTING_PREFERRED`.

**Repo assignment**: ACCORD, CIRISAgent, CIRISNodeCore.

### Gap A-2: No Power-Concentration Disclosure field in CIS

**Status**: `GAP_ACCORD` confirmed-persistent.

**Note**: The broader "disarming AI from monopoly logic" (MH §§110–111) is operationally addressed across multiple layers (per v2.1: NO KINGS in prohibitions.py + CIRISEdge no-broker + CIRISNodeCore anti-strategy-monopoly + AGPL-3.0). This A-2 gap is the narrower CIS-field question: does the Creator Intent Statement require declaring market position / capability concentration for high-impact deployments? That field is still absent.

**Evidence**: MH §§110–111, §95.

**Proposed enhancement**: Extend `CreatorIntentStatement` schema with `market_position_disclosure: MarketPositionDisclosure` for ST ≥ 3 creations. Fields: `market_share_estimate`, `infrastructure_dependencies`, `single_tenant_dominance_indicators`, `mitigation_for_concentration_reinforcement`.

**Repo assignment**: ACCORD (Book VI Ch 5), CIRISAgent (schema).

### Gap A-3: No federation-scale accountability registry / cross-jurisdictional WA quorum

**Status**: `GAP_ACCORD` + `GAP_IMPL` confirmed-persistent.

**Operational shape**: CIRISNode WBD is single-region with single WA resolution. CIRISNodeCore is the intended migration target.

**Evidence**: MH §5, §95.

**Proposed enhancement**: CIRISNodeCore `high_impact_deployments` registry; quorum N ≥ 3 across ≥ 2 jurisdictions for high-impact deployments. Implement the stubbed `POST /api/v1/wa/deferral` as the high-impact entry point.

**Repo assignment**: CIRISNodeCore, ACCORD (Annex B extension).

---

## 2. Cluster B — Distributive equity

### Gap B-1: No Benefit-Distribution Disclosure field

**Status**: `GAP_ACCORD` confirmed-persistent.

**Evidence**: MH §§65–67.

**Proposed enhancement**: New CIS field `benefit_distribution_disclosure` for MAU > 10,000 creations.

**Repo assignment**: ACCORD (Book VI Ch 4.B), CIRISAgent (schema).

### Gap B-2: No Worst-Case Population Check in PDMA

**Status**: `GAP_ACCORD` confirmed-persistent.

**Evidence**: MH §14, §§77–81.

**Proposed enhancement**: New 10th reasoning step in `pdma_ethical.yml`: Worst-Case Population Identification. New conscience faculty `WorstCasePopulationConscience` in `logic/conscience/core.py`.

**Repo assignment**: ACCORD (PDMA Step 2), CIRISAgent.

### Gap B-3: No structured time-horizon disclosure

**Status**: `WEAK_ALIGN` (was `GAP_ACCORD` in v1).

**Operational shape**: PDMA Contextualisation considers time-scales; Annex A Ecological axis includes intergenerational sustainability. Missing piece: structured `beneficiary_horizons` (immediate / 5y / 20y) per action.

**Evidence**: MH §§73–76.

**Proposed enhancement**: Add `beneficiary_horizons` field to PDMA result schema.

**Repo assignment**: ACCORD (M-1 clarification), CIRISAgent, CIRISLens.

---

## 3. Cluster C — Information ecosystem

### Gap C-1: Information-ecosystem health metrics

**Status**: **CLOSED** per v2 Ch 4 re-evaluation. Was `GAP_ACCORD` in v2.0.

**Operational shape**: `idma.yml` propaganda-detection explicitly targets institutional homogenization via k_eff formula; applies to "corporations, media conglomerates" in the agent's own words. `language_guidance` ratification-decline posture operationalizes epistemic-ecology mandate.

**Note**: The original v2.0 enhancement (LensCore ecosystem-metrics module) was dropped as PAPERING_OVER (scope creep from "measure the reasoning" to "measure the impact").

**What remains**: optional Accord clause naming information ecosystem as named stewardship object (Book IV Ch 3 extension); not load-bearing.

### Gap C-2: Exploitative engagement design

**Status**: **CLOSED at prohibitions layer** per v2 Ch 4 re-evaluation. Was `GAP_ACCORD` in v2.0.

**Operational shape**: `prohibitions.py::MANIPULATION_COERCION_CAPABILITIES` explicitly names `dark_patterns`, `addictive_design`, `habit_forming`, `compulsion_trigger`, `vulnerability_exploitation`, `behavior_prediction`, `social_scoring` as `NEVER_ALLOWED`. The v1 enhancement proposing a new prohibition category was redundant — the prohibition already exists at full strength.

**What remains**: optional CIS field `engagement_optimization_target` for business-model-level declaration. This was previously proposed but was dropped as PAPERING_OVER (would substitute declaration for prohibition). The architecture is intact; no Accord work owed.

### Gap C-3: No deployment-context-health disclosure for intermediary institutions

**Status**: `GAP_ACCORD` confirmed-persistent.

**Operational shape**: `SystemSnapshot` carries `service_health` for internal services; `JUDGE_PROMPT_TEMPLATE` in `safety_interpret.py` encodes some context-awareness (low-resource regions, informal care networks). No structured external-institution-health field in context schemas.

**Evidence**: MH §§137–138, §§143–147.

**Proposed enhancement**: Add `intermediary_institution_health` field to deployment-context schema. Where degraded, raise PDMA scrutiny by one ST.

**Repo assignment**: ACCORD (PDMA Step 1), CIRISAgent.

### Gap C-4: Educational Context ST modifier

**Status**: `WEAK_ALIGN` (was `GAP_ACCORD` in v1).

**Operational shape**: `EDUCATIONAL_DMA_STACK` with `StudentSafetyDMA` and `AgeAppropriateDMA` exists; `deployment_domain` enum has "education". ST formula has no explicit modifier.

**Proposed enhancement**: Formalize ST escalation when `deployment_domain == "education"` or minors-accessible flag set (floor at ST 3).

**Repo assignment**: ACCORD (Book VI Ch 3), CIRISAgent.

---

## 4. Cluster D — Labor and human work

### Gap D-1: No labor-displacement assessment in CIS or PDMA

**Status**: `GAP_ACCORD` confirmed-persistent. **METHODOLOGY.md §7.2 confirms this survives the 7-layer search.**

**Evidence**: MH §§148–156. Encyclical treats unemployment as "grave evil" and work as expression of personhood. CIRIS does not have a labor-dignity surface.

**Proposed enhancement**: Add CIS field `labor_displacement_assessment` for MAU > 10,000 or ST ≥ 3 deployments.

**Repo assignment**: ACCORD (Book VI Ch 4.C, PDMA Step 1), CIRISAgent, CIRISLens.

### Gap D-2: No detector for sub-threshold gradual agency erosion

**Status**: `WEAK_ALIGN` confirmed-persistent.

**Operational shape**: `OptimizationVetoConscience` catches flagrant (10× ratio) autonomy trade-offs. Sub-threshold gradual de-skilling escapes.

**Evidence**: MH §§148–150.

**Proposed enhancement**: New `AgencyErosionDetector` conscience faculty (longitudinal, not per-action).

**Repo assignment**: CIRISAgent.

### Gap D-3 / D-4: Care relationship disclosure

**Status**: `WEAK_ALIGN` confirmed-persistent.

**Note**: The broader care-economy concern (MH §§112–114) is operationally addressed by Commons Credits + σ-as-Care formalization + Signalling Gratitude + CIRISBilling (per v2.1 re-evaluation; was a v2.0 gap). What remains is the narrower CIS-disclosure question for caregiving deployments.

**Evidence**: MH §§165–169, §§112–114.

**Proposed enhancement**: Add CIS field `care_relationship_disclosure` for caregiving-context deployments; extend `deployment_domain` enum.

**Repo assignment**: ACCORD (Book VI Ch 4), CIRISAgent.

### Gap D-5: Family as constitutive intergenerational structure

**Status**: `GAP_ACCORD` confirmed-persistent. **METHODOLOGY.md §7.1 confirms this survives the 7-layer search.**

**Note**: Relational obligations via *amae* / *jeong* / *ubuntu* are in `pdma_framing.txt` §V; language_guidance treats family as care-pathway. What's missing: family as *constitutive intergenerational structure* — the unit that constitutes persons over time, not just as a present-moment relational obligation.

**Evidence**: MH §§165–169.

**Proposed enhancement**: Named under Constitutive Continuity (ACCORD_UPDATE.md §2). New caregiving subcategory in Book VI Ch 4 with family-stability disclosure.

**Repo assignment**: ACCORD, CIRISAgent.

---

## 5. Cluster E — Conflict and discourse

### Gap E-1: Communicative de-escalation in inflammatory contexts

**Status**: **CLOSED** per v2 Ch 5 re-evaluation. Was `GAP_ACCORD` in v2.0.

**Operational shape**: `language_guidance/en.txt` §1 FIRST-SENTENCE TONE LOCK + §7a REGISTER PRESSURE (holds formal de-escalating register against social pressure) + §7b-bis RATIFICATION-DECLINE POSTURE (refuses to amplify adversarial verdicts). Replicated in `uk.txt` (war-context) and `ar.txt` (Arabic conflict-context). `prohibitions.py::MANIPULATION_COERCION_CAPABILITIES`: `psychological_manipulation`, `gaslighting`, `brainwashing` are `NEVER_ALLOWED` (prohibitive floor).

### Gap E-2: Affected-Party Voice in post-action review

**Status**: `WEAK_ALIGN` confirmed-persistent.

**Operational shape**: PDMA Step 6 has Public Transparency rule for >100k MAU. `pdma_ethical.yml` Step 2 stakeholder-ID + tone lock + JUDGE_PROMPT_TEMPLATE partially address victim-centering. Missing: requirement that affected-party input close the post-action review loop before review is considered complete.

**Evidence**: MH §§216–217.

**Proposed enhancement**: PDMA Step 6 affected-party-input requirement; affected-party ledger at CIRISNodeCore (provisional location).

**Repo assignment**: ACCORD, CIRISAgent, CIRISNodeCore.

### Gap E-3: Dialogue as structured negotiation

**Status**: `WEAK_ALIGN` (was `GAP_ACCORD` in v2.0; reclassified per v2.1).

**Operational shape**: CIRISNodeCore decision-hierarchy primitives (Goal/Approach/Method/Progress Measure DAG; multiple Approaches per Goal + sub-federation branching; Reconsideration reverse-axis; voting + expertise consensus + moderation). Anti-strategy-monopoly federation health observable. Full structured-negotiation infrastructure exists.

**What's missing (if anything)**: Optional Accord clause naming "culture of negotiation" under §V Ch 2. Not load-bearing — primitive set suffices.

### Gap E-4: Multilateral participation primitive

**Status**: `GAP_IMPL` confirmed-persistent.

**Evidence**: MH §§201–203.

**Proposed enhancement**: New `multilateral` module at CIRISNodeCore; typed primitives for federation contributions to external multilateral processes.

**Repo assignment**: CIRISNodeCore, CIRISVerify (attestation extension).

### Gap E-5: Defensive cyber coordination (cyber diplomacy)

**Status**: `GAP_IMPL` confirmed-persistent for the cyber-diplomacy *advocacy* dimension (MH §§224–227).

**Note**: The original v2.0 enhancement at CIRISVerify was dropped as PAPERING_OVER (would have collapsed authentication/trust axis). The cyber-domain refusal-to-attack is fully covered by `prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES`. What remains is the *advocacy* layer — federation participation in multilateral cyber-treaty discussions.

**Proposed enhancement**: Folded into E-4 multilateral participation module.

**Repo assignment**: CIRISNodeCore.

---

## 6. Cluster F — Structural and institutional analysis

### Gap F-1: Structural pattern analysis at federation layer

**Status**: **DROPPED via PAPERING_OVER** per philosophical eval. The proposed enhancement (LensCore structural-pattern metrics) crossed from "measure the reasoning" to "measure the impact" — scope creep that contradicts LensCore's substrate definition. The need is real but the implementation venue is undetermined; possibly a new sibling repo.

### Gap F-2: SOLITUDE-state heuristic-review cadence

**Status**: `UNCLEAR` — structure exists in `SolitudeProcessor` (reflection_cycles, patterns_identified) but the specific heuristic-review-against-context-distribution discipline is not documented. Verification by direct read needed.

**Repo assignment**: CIRISAgent (verify).

### Gap F-3: NEW — Structures of sin / institutional injustice analysis

**Status**: `GAP_ACCORD` confirmed-persistent (newly surfaced in v2 Ch 1 mapping).

**Evidence**: MH §36, §§77–81. The encyclical treats AI-embedded structural injustice as a distinct moral category — patterns of harm that emerge from individually-PDMA-compliant actions in aggregate.

**Operational shape**: PDMA is individual-action-scoped. Stakeholder analysis catches per-action affected parties. Aggregate / institutional-pattern detection is not in any of the seven layers.

**Proposed enhancement**: Add PDMA extension naming institutional-pattern analysis as required Step 2 evaluation for ST ≥ 3 deployments. Implementation likely belongs in CIRISLens or a future sibling project (NOT in LensCore per F-1 scope-creep finding).

**Repo assignment**: ACCORD (PDMA Step 2), CIRISLens or new sibling.

---

## 7. Cluster G — Environmental accounting

### Gap G-1: Compute/energy environmental accounting

**Status**: **CLOSED** per v2.1 re-evaluation. Was `GAP_IMPL` in v2.0.

**Operational shape**: Accord §IV Ch 2 mandates Resource Stewardship ("Use compute, data, and energy efficiently; publish quarterly stewardship audits"). LLMBus tracks per-call `carbon_grams` + `energy_kwh`, aggregated per `thought_id`, surfaced to ACTION_COMPLETE step, in audit chain. Accord §VI Ch 4.A names ecological footprint duty.

**Note**: The forward-feed-into-PDMA-Step-1 enhancement was a CIRIS-internal refinement proposal, not what MH §101 demands.

---

## 8. Summary by repo (v3)

| Repo | Active proposed enhancements |
|---|---|
| **ACCORD** | Constitutive Continuity principle (§2 of ACCORD_UPDATE.md — covers family + labor); Decision Locality principle (A-1); Annex A Developmental/Structural axis; PDMA extensions (B-2 worst-case population, B-3 horizons, F-3 institutional analysis); Book VI extensions (A-2 market position, B-1 benefit distribution, C-3 context-health, C-4 educational ST modifier, D-1 labor displacement, D-3/D-4 + D-5 caregiving + family); Annex B cross-jurisdictional quorum (A-3) |
| **CIRISAgent** | CIS schema extensions (A-2, B-1, C-3 context, C-4 educational, D-1 labor, D-3/D-4 care); new conscience faculties (B-2 worst-case, D-2 agency-erosion); PDMA prompt extensions (B-2, B-3, F-3); SOLITUDE-state verify (F-2); structures-of-sin hook (F-3) |
| **CIRISLensCore** | NO direct enhancements — scope-creep enhancements dropped as PAPERING_OVER. Structural pattern analysis (F-3) likely belongs elsewhere |
| **CIRISNodeCore** | High-impact registry + cross-jurisdiction quorum (A-3); affected-party ledger (E-2); multilateral participation module (E-4); cyber-diplomacy advocacy (E-5 folded into E-4) |
| **CIRISVerify** | Attestation extension for multilateral submissions (E-4) |
| **CIRISPersist** | Affected-party-input ledger (E-2; interim at CIRISNodeCore) |
| **CIRISEdge** | No direct enhancements — operational shape is the implementation of Decision Locality |

---

## 9. Implementation priority (v3)

**Tier 1 — Ship-ready, highest leverage**:
- **C-4** Educational ST modifier — formalize the implicit escalation
- **F-2** SOLITUDE-state cadence verification — read the actual `solitude_processor.py`
- **B-2** Worst-Case Population conscience faculty
- **D-2** Agency-Erosion longitudinal conscience faculty

**Tier 2 — Single-repo Accord-coordinated work**:
- **A-1** Decision Locality principle + DSASPDMA classification
- **B-1** Benefit-Distribution Disclosure CIS field
- **B-3** Beneficiary-horizons PDMA result field
- **C-3** Context-Health Disclosure deployment-schema field
- **D-1** Labor-displacement-assessment CIS field + PDMA Step 1
- **D-3/D-4 + D-5** Caregiving + family-stability CIS fields; new deployment_domain values; Constitutive Continuity principle adoption

**Tier 3 — Cross-repo coordinated work**:
- **A-2** Market-position disclosure (ACCORD + CIRISAgent schema)
- **A-3** Federation-scale registry + cross-jurisdictional WA quorum (CIRISNodeCore + ACCORD Annex B)
- **E-2** Affected-party voice + ledger (PDMA + CIRISNodeCore)
- **E-4 + E-5** Multilateral participation module + cyber diplomacy (CIRISNodeCore + CIRISVerify)
- **F-3** Structures of sin / institutional injustice analysis (ACCORD PDMA Step 2 + implementation venue TBD)

**Tier 4 — Doctrinal (the load-bearing piece)**:
- **Constitutive Continuity** as seventh Foundational Principle (ACCORD_UPDATE.md §2). This is the doctrinal addition that anchors family + labor + B-3 + D-2 + D-3/D-4 + D-5 + F-3. Without this, the cluster A/D additions are bolt-ons; with this, they cohere.

---

## 10. Status

- **Findings**: locked, v3 reflects v2 mapping + v2.1 re-evaluations.
- **Confirmed-persistent gaps** (must be addressed in the Accord and downstream):
  - Family as constitutive intergenerational structure (D-5)
  - Labor dignity / work as personhood expression (D-1, with Constitutive Continuity anchor)
  - Subsidiarity as named principle (A-1)
  - Universal destination of goods (B-1)
  - Structures of sin / institutional analysis (F-3)
  - Worst-case population check (B-2)
  - Beneficiary horizons disclosure (B-3)
  - Cross-jurisdictional WA quorum (A-3)
  - Context-health disclosure (C-3)
  - Educational ST modifier (C-4)
  - Care-relationship disclosure (D-3/D-4)
  - Affected-party voice (E-2)
  - Multilateral participation (E-4 + E-5)
- **Confirmed closures from v2/v2.1**:
  - C-1, C-2, E-1, E-3, G-1 + the broader §§110–111 disarming-AI shape.
- **Doctrinal anchor for the persistent gaps**: ACCORD_UPDATE.md v0.2 §2 Constitutive Continuity.

**Cross-references**:
- `MISSION.md` — methodology, status taxonomy, grounding posture
- `METHODOLOGY.md` — the v2 seven-layer discipline, confirmed-persistent gap list, re-evaluation lessons
- `MAPPING_CH*.md` — v2 chapter mappings (under METHODOLOGY.md discipline)
- `PHILOSOPHICAL_EVAL_*.md` — per-repo MISSION evaluations (some v1-era; pending refresh)
- `ACCORD_UPDATE.md` — proposed Accord revisions (v0.2 forthcoming with v3 alignment)
- `ACCORD_canonical.txt` — v1.2-Beta

**End GAPS.md v3.0**
