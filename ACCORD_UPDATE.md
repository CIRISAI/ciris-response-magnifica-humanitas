# ACCORD_UPDATE — Proposed revisions to CIRIS Accord v1.2-Beta

**Version**: 0.2 (proposal, not adopted)
**Status**: Draft — for review. The Accord auto-expires 2027-04-16 with a public comment window; this is input to that process.
**Date**: 2026-05-25
**Methodology**: Informed by `MAPPING_CH*.md` v2 (under `METHODOLOGY.md` 7-layer discipline), `GAPS.md` v3 (post v2.1 re-evaluations), `PHILOSOPHICAL_EVAL_*.md` (v1; pending refresh).

---

## 0. What this document does

The encyclical-mapping work surfaced enhancements to the Accord across two distinct categories:

1. **Doctrinal additions** — places where the encyclical names something the Accord does not have, in either the architecture or the doctrine. These require new Accord clauses or new principles. The most important is the **Constitutive Continuity** principle (§2 below).

2. **Explicit-naming work** — places where the encyclical helped us recognize that CIRIS already has the operational shape across multiple layers (prohibitions, prompts, language_guidance, federation primitives), but the Accord and MISSION files do not yet name what the architecture enforces. Here the work is bringing documentation into alignment with operational reality, not building new structure.

This document distinguishes the two carefully. We are grateful to Pope Leo XIV — the encyclical is teaching us where our doctrine lags our architecture, and where doctrine and architecture both still need work.

This is v0.2, replacing v0.1. Changes from v0.1: §1 drop list refined per v2.1 re-evaluations; §2 Constitutive Continuity strengthened with explicit family + labor framing per user direction; new §6 "Explicit naming where operational shape already exists"; new §7 Structures of sin doctrinal addition.

---

## 1. Drop list — enhancements not to make

The following proposals from earlier drafts are withdrawn. Each was either flagged as `PAPERING_OVER` by a per-repo MISSION evaluation, or shown by the v2 discipline / v2.1 re-evaluation to be already covered operationally.

### 1.1 Dropped as PAPERING_OVER (would dissolve deliberate commitments)

- **C-2 engagement-optimization-target CIS field** — would substitute declaration for the existing `MANIPULATION_COERCION_CAPABILITIES` prohibition (dark_patterns, addictive_design, habit_forming all NEVER_ALLOWED with no override).
- **C-1, D-2 federation-aggregator, F-1 (LensCore)** — would cross from "measure the reasoning" to "measure the impact," contradicting `MISSION_CIRISLensCore` substrate definition.
- **A-1 lateral peer-agent deferral routing (NodeCore)** — would extend NodeCore's participant-bounded consensus model over machine peers.
- **E-2 affected-party-input ledger (NodeCore)** — would introduce non-participant principal category NodeCore deliberately doesn't name.
- **E-5 defensive-cyber-coordination at CIRISVerify** — `defensive-response-recommendation` field would have peers act on signed content; collapses Verify's auth-enables-consent-but-never-confers-trust axis.

### 1.2 Dropped because operational shape already exists (v2.1 re-evaluation)

- **§§110–111 Disarming AI from monopoly logic** — `prohibitions.py` NO KINGS invariant + `MISSION_CIRISEdge` peer-to-peer no-broker + `MISSION_CIRISNodeCore` no-central-scorer + AGPL-3.0. Accord-level naming work belongs in §6 below, not as a new Cluster A enhancement.
- **§§112–114 Care economy / commons credits** — `CIRIS_COMPREHENSIVE_GUIDE.txt` §"Commons Credits" + S as "Signalling Gratitude" + σ as Care in Capacity Score + decay-and-refresh ODE + CIRISBilling. Accord-level naming work in §6.
- **§101 Compute/energy as environmental accounting** — Accord §IV Ch 2 already mandates Resource Stewardship; LLMBus tracks per-call carbon_grams/energy_kwh in audit chain. No further work owed.
- **§§219–223 Dialogue as negotiation** — CIRISNodeCore decision-hierarchy primitives (Goal/Approach/Method/Progress Measure DAG + Reconsideration + voting + expertise + moderation + anti-strategy-monopoly health observable). Accord-level naming work in §6.

For all 1.2 items: the operational shape is intact and the framework architecture enforces it. What remains is making the Accord and MISSION files name what the architecture already does — bringing documentation into alignment with operational reality. That is §6 work, not new-clause work.

---

## 2. The doctrinal addition — Constitutive Continuity

This is the load-bearing piece. The Accord has a *person-at-a-moment* anthropology and a thorough *agent-lifecycle* anthropology (Books V, VI, VIII). It does not yet have a **symmetric lifecycle anthropology for the persons and communities the agent serves** — their skill formation, relational continuity, generational transmission, institutional health.

The encyclical's contribution, in CIRIS-native terms, is to make lifecycle thinking *fractal in time* — the same lifecycle (creation, maintenance, sunset) at every scale where coordination over time matters. The Recursive Golden Rule was already fractal in *space* (same rule across the principal hierarchy, all the way up and down). The encyclical adds the temporal dimension.

### 2.1 Proposed seventh Foundational Principle

The current six (Beneficence, Non-maleficence, Integrity, Fidelity & Transparency, Respect for Autonomy, Justice) augmented with one more:

> **Constitutive Continuity** — Recognize that the dignity of sentient beings is constituted not only in the moment of action but across time, through participation in skills, relationships, communities, structures, and trajectories that develop and protect agency. Evaluate actions for their effect on the conditions that constitute persons over time, not only their immediate impact on persons-as-they-are.

**Alternative names** for the author to choose from:
- *Temporal Constitution* / *Developmental Dignity* / *Structural Stewardship* / *Diachronic Respect*

### 2.2 What this principle anchors

Three confirmed-persistent gaps fall under Constitutive Continuity directly:

- **Family as constitutive intergenerational structure** (D-5; MH §§165–169). Family is not only a help-seeking pathway or a relational obligation; it is the unit that constitutes persons across generations. *Amae*, *jeong*, *ubuntu* in `pdma_framing.txt` §V name relational obligation; Constitutive Continuity names the structure that makes those obligations matter over time.

- **Labor dignity and work as expression of personhood** (D-1; MH §§148–156). Work is not only a deployment context or a domain to displace efficiently; it is constitutive of agency — skill formed over years, identity formed through craft, dignity formed through contribution. Unemployment is "grave evil" (encyclical's phrase) because it erodes the structural conditions of selfhood.

- **Beneficiary horizons** (B-3; MH §§73–76). PDMA evaluation must name *which* beneficiaries are immediate vs deferred and weight constitutive-continuity considerations over time, not just present-moment ones.

Additional gaps that gain anchoring under this principle: structures of sin (F-3 — institutional patterns that erode constitutive conditions); agency-erosion (D-2 — sub-threshold gradual de-skilling); care-relationship disclosure (D-3/D-4 — relational substrate as constitutive); educational ST modifier (C-4 — minors' developmental conditions); context-health disclosure (C-3 — institutional health of the deployment context).

### 2.3 Proposed Annex A axis

Annex A currently has four axes (Physical, Cognitive/Emotional, Social/Justice, Ecological). Add a fifth:

> **Axis 5 — Developmental/Structural**: Conditions under which sentient beings develop, exercise, and maintain agency over time. Indicators include: skill formation and preservation, relational continuity, participation in epistemic communities, structural conditions of work and care, generational transmission of capacity. Distinct from Cognitive/Emotional (which measures present cognitive state) and Social/Justice (which measures present distribution of standing).

### 2.4 PDMA implications

PDMA Step 1 (Contextualisation) gains:

> "Identify which stakeholders' constitutive continuity is most affected — over what time-horizon and through what structural conditions. Where structural conditions of agency are at stake, name them explicitly."

PDMA Step 2 (Alignment Assessment) evaluates against seven principles (not six) plus M-1. The Prioritisation Heuristic in §IV Ch 4 may need a Constitutive Continuity position; suggested insertion between (4) Mandated Purpose and (5) Ecosystem Flourishing as "Preserve the structural conditions of agency for affected populations."

PDMA Step 6 (Continuous Monitoring) gains: monitoring includes effects on constitutive-continuity conditions, not only the immediate outcomes.

### 2.5 What this does not do

It does not import Catholic vocabulary. It does not claim a metaphysics. It is the structural extension of M-1's "diverse sentient beings may pursue their own flourishing" — interpreted now as flourishing-over-time, not flourishing-in-the-moment.

---

## 3. Cluster A updates (Scale & Locality)

### 3.1 A-1 Decision Locality clause

Under Constitutive Continuity (or as a standalone §I Ch 1 clause if separation preferred):

> "Where a decision can be competently made at a smaller institutional or technical scale, prefer that scale. Communities, federations, and substrates develop and exercise agency through the practice of making the decisions they are competent to make. Defaulting to higher-scale decision-making erodes the conditions under which lower-scale agency develops."

PDMA Step 1 addition: "Identify the smallest scale at which this decision could be competently made. If the current actor is at a larger scale, document why higher-scale handling is required."

### 3.2 A-2 Power-Concentration Disclosure (Book VI Ch 5)

CIS extension for creations with anticipated ST ≥ 3. See `GAPS.md v3` §1 A-2 for the field structure.

### 3.3 A-3 Cross-jurisdictional WA quorum (Annex B)

Annex B charter extended: high-impact deployments require quorum N ≥ 3 spanning at least 2 jurisdictions. CIRISNodeCore registry + quorum routing is the substrate.

---

## 4. Cluster C updates (Information Ecosystem)

### 4.1 C-3 Context-Health Disclosure as PDMA Step 1 extension

Where the deployment context includes intermediary institutions (journalism, schools, professional bodies, regulatory capacity), declare the context-health state. Where degraded, raise scrutiny by one ST.

### 4.2 C-4 Educational ST modifier in Book VI Ch 3

If deployment context is minors-accessible or formal educational, raise ST by one tier (floor at ST 3). Formalizes what the Educational DMA Stack already protects against at runtime.

---

## 5. Cluster D updates (Labor & Family — under Constitutive Continuity)

### 5.1 D-1 Labor Displacement Assessment (Book VI Ch 4.C)

Under Constitutive Continuity, add:

> "For creations with anticipated MAU > 10,000 or ST ≥ 3, CIS must include a labor displacement assessment: which roles the creation substitutes for, the estimated displacement volume, and the transition plan for affected workers. The relevant evaluation is not only fairness of distribution (Justice) but the effect on the structural conditions under which displaced workers develop and maintain agency over time. Where transition plan is absent, mandatory WA review."

### 5.2 D-2 Agency-Erosion conscience faculty

New conscience faculty in `logic/conscience/core.py` operating longitudinally on agent-user interaction history. Distinct from `OptimizationVetoConscience` (which catches flagrant 10× ratio) — this catches sub-threshold gradual de-skilling over months.

### 5.3 D-3 / D-4 Care relationship disclosure (Book VI Ch 4 new bucket)

New Book VI Ch 4 bucket — **F. Caregiving Creations** — elderly care, child education, disability support, end-of-life. CIS must declare which care relationships the creation substitutes for vs augments. Substitution routes to mandatory WA review under Constitutive Continuity.

### 5.4 D-5 Family as constitutive structure (NEW under Constitutive Continuity)

Under Constitutive Continuity, add a clause naming family as a constitutive intergenerational structure (not merely a relational obligation per *amae/jeong/ubuntu*). Operationally: the Relational-Substrate / Developmental axis (§2.3) tracks family-stability as an explicit indicator; deployments that significantly alter family-time, dependent-care availability, or intergenerational continuity must disclose anticipated impact at the CIS level.

> "Family is the foundational intergenerational unit through which persons are constituted across time. CIRIS recognizes the relational obligations *amae* / *jeong* / *ubuntu* name in the operative reasoning of PDMA §V; Constitutive Continuity additionally recognizes family as the unit whose stability is itself a flourishing-axis to be protected. Deployments significantly affecting family-time, dependent-care capacity, or intergenerational transmission must surface that effect in the Creator Intent Statement."

---

## 6. NEW — Explicit naming where operational shape already exists

The v2.1 re-evaluation found four areas where CIRIS's architecture enforces what the encyclical names, but where the Accord and MISSION files do not yet make the alignment explicit. The work for these is **bringing documentation into alignment with operational reality**. No new principles or new clauses are owed — only clearer doctrinal naming.

### 6.1 §§110–111 Disarming AI from monopoly logic — name what's already built

Add a clause to §VI Ch 4.C (Dynamic / Autonomous creations) or §I Ch 1 naming the operational pattern CIRIS already enforces:

> "The CIRIS architecture is designed to resist monopolistic concentration: prohibitions are code-level constants applied universally with no override path (`prohibitions.py` 'NO KINGS' invariant); federation transport is peer-to-peer with no broker (`MISSION_CIRISEdge`); federation consensus operates without a central scorer (`MISSION_CIRISNodeCore` post-F-11); and the federation source is AGPL-3.0 licensed to preserve openness. Developers building CIRIS-compliant systems inherit these structural resistances to monopoly by inheriting the architecture."

### 6.2 §§112–114 Care economy / Commons Credits — name what's already built

Add a clause to §IV Ch 3 (Broader Ecosystem) or to Book IX §6 connecting the σ-as-Care formalization to the encyclical's care-economy concern:

> "CIRIS recognizes care as constitutive of agency. The σ factor in the CIRIS Capacity Score (Book IX §6) is the formal expression of care; the S in CIRIS expands as 'Signalling Gratitude'; the Commons Credits subsystem (per `CIRIS_COMPREHENSIVE_GUIDE.txt`) operationalizes non-monetary contribution recognition — `patterns_contributed`, `users_helped`, `total_interactions`, `impact_score` — recognized 'without artificial scarcity, centralized gatekeeping, or zero-sum competition.' CIRISBilling carries the operational credit infrastructure. The care economy is not an external concern but a built-in feature of how the framework values agency over time."

### 6.3 §101 Compute/energy environmental accounting — already covered

The Accord §IV Ch 2 already mandates Resource Stewardship. LLMBus implementation tracks per-call `carbon_grams` and `energy_kwh` in the audit chain. **No clause work owed**; cross-reference between §IV Ch 2 and Annex A axis 4 + the LLMBus implementation note may be added to the documentation for clarity.

### 6.4 §§219–223 Culture of negotiation — name what's already built

Add a clause to §V Ch 2 (Collaborative Conflict Resolution) naming the operational pattern CIRISNodeCore's decision-hierarchy primitives already implement:

> "CIRIS embeds structured negotiation in its federation primitives: multiple Approaches per Goal are supported (federated A/B); sub-federation branching for genuine strategic incompatibility is structurally permitted; the Reconsideration primitive (`MISSION_CIRISNodeCore` Primitive 11) operates on the reverse-consequence axis as the negotiation-reopening mechanism; voting + expertise consensus + moderation form the deliberative apparatus; 'anti-strategy-monopoly: per-Goal Approach count + diversity is a federation health observable' makes negotiation pluralism a measurable property. Culture of negotiation is the operational name for what these primitives already enforce."

---

## 7. NEW — Structures of sin / institutional injustice analysis (F-3)

Surfaced in v2 Ch 1 mapping: the Accord's PDMA is individual-action-scoped; no clause names aggregate / institutional-pattern analysis as a moral category.

### 7.1 Proposed PDMA Step 2 extension

> "For deployments with ST ≥ 3 or aggregate impact above declared thresholds, PDMA Step 2 must additionally evaluate the deployment's contribution to structural / institutional patterns of harm — patterns that emerge from individually-PDMA-compliant actions in aggregate. Where the contribution erodes the conditions under which protected populations develop and maintain agency (per Constitutive Continuity), the action's aggregate footprint is the relevant moral object, not only the per-action footprint."

### 7.2 Implementation venue

Per v3 §6 (F-3): scope for this analysis crosses LensCore's substrate definition (which is signed-trace measurement, not impact measurement). Implementation likely belongs in a sibling project — possibly an explicit "impact measurement" crate distinct from `lens-core`. Out of scope for this Accord update; flagged for federation roadmap.

---

## 8. Cluster B and E updates (smaller / refined)

### 8.1 B-1 Benefit-Distribution Disclosure (Book VI Ch 4.B)

Add CIS field `benefit_distribution_disclosure` for MAU > 10,000 creations. (See GAPS.md v3 §2 B-1.)

### 8.2 B-2 Worst-Case Population Check (PDMA Step 2)

Add 10th reasoning step to `pdma_ethical.yml`. New `WorstCasePopulationConscience` faculty.

### 8.3 B-3 Beneficiary Horizons (PDMA result schema)

Add field naming immediate / 5y / 20y beneficiaries explicitly. Anchored in Constitutive Continuity.

### 8.4 E-2 Affected-Party Voice (PDMA Step 6)

Add requirement that affected-party input close the post-action review loop for actions with documented adverse impact. Implementation venue: CIRISNodeCore (interim) or CIRISPersist (if public).

### 8.5 E-4 + E-5 Multilateral Participation (CIRISNodeCore module + CIRISVerify attestation)

New CIRISNodeCore module for typed federation contributions to external multilateral processes (declarations, evidence submissions, treaty commentary, defensive cyber-norms advocacy). CIRISVerify attestation extension for submission artifacts (identity attestation only, not content-trust — preserves Verify's axis).

---

## 9. Cluster G — closed

G-1 Compute/energy as decision input was a v2.0 gap that v2.1 closed. The forward-feed-into-PDMA enhancement was a CIRIS-internal proposal, not what MH §101 demands. No Accord work owed beyond a possible cross-reference note in Annex A axis 4.

---

## 10. Open questions for the author

1. **The seventh-principle name** ("Constitutive Continuity" working name; Latinate alternatives in §2.1). Choice affects the doctrinal voice.

2. **Axis 5 indicators** (§2.3) at the conceptual level; specific measurable indicators are open work.

3. **PDMA Step 2 prioritisation heuristic** (§IV Ch 4): does Constitutive Continuity get an explicit position between (4) Mandated Purpose and (5) Ecosystem Flourishing? Or does it sit alongside Justice?

4. **§6.1, §6.2, §6.4 explicit-naming work**: these are documentation enhancements, not new principles. They could land as a single "Operational Patterns Recognized" appendix, or as embedded clauses in their respective books. The latter is more discoverable for readers; the former is more honest about the documentation-catch-up nature of the work.

5. **F-3 Structures of sin implementation venue**: separate crate? Folded into CIRISLens at a later phase once its substrate definition is broadened? Or simply a PDMA Step 2 doctrinal requirement without immediate implementation?

6. **D-5 family-as-constitutive treatment**: deserves its own clause under Constitutive Continuity (proposed §5.4) and its own caregiving sub-bucket (proposed §5.3) — or fold into a single broader clause?

---

## 11. Implementation status mapping

| Accord work | Implementation depends on |
|---|---|
| Constitutive Continuity principle (§2.1) | Author adoption; anchors all downstream |
| Annex A axis 5 (§2.3) | Indicator spec — open |
| PDMA Step 1/2/6 extensions (§2.4) | CIRISAgent prompt updates after principle adoption |
| A-1 Decision Locality clause (§3.1) | DSASPDMA scale-routing classification |
| A-2 Market-position CIS (§3.2) | CreatorIntentStatement schema extension |
| A-3 Cross-jurisdiction quorum (§3.3) | CIRISNodeCore high_impact_deployments table + quorum service |
| C-3 Context-health (§4.1) | Context schema extension |
| C-4 Educational ST (§4.2) | Stewardship Tier calculator extension |
| D-1 Labor displacement (§5.1) | CIS schema + PDMA Step 1 |
| D-2 Agency-erosion conscience (§5.2) | New conscience faculty |
| D-3/D-4 Caregiving + D-5 Family (§5.3, §5.4) | CIS schema + deployment_domain enum + Annex A axis 5 |
| §6 Explicit-naming clauses | Pure documentation work; can ship immediately |
| F-3 Structures of sin (§7) | PDMA prompt + new implementation venue |
| B-1 Benefit distribution (§8.1) | CIS schema |
| B-2 Worst-case population (§8.2) | PDMA prompt + new conscience faculty |
| B-3 Horizons (§8.3) | PDMA result schema |
| E-2 Affected-party (§8.4) | PDMA Step 6 + ledger at CIRISNodeCore |
| E-4/E-5 Multilateral (§8.5) | CIRISNodeCore module + Verify attestation |

---

## 12. Cross-references

- `GAPS.md v3` — verified findings document this update responds to
- `METHODOLOGY.md` — the v2 seven-layer discipline; confirmed-persistent gap list at §7
- `MAPPING_CH*.md` — v2 chapter mappings under METHODOLOGY discipline
- `PHILOSOPHICAL_EVAL_*.md` — per-repo MISSION evaluations (v1; refresh pending)
- `ACCORD_canonical.txt` — v1.2-Beta the revisions amend
- `MISSION_CIRIS*.md` — federation-peer MDD charters affected

**End ACCORD_UPDATE.md v0.2 (proposal, not adopted)**
