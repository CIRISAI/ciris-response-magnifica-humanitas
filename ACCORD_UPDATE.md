# ACCORD_UPDATE — Proposed revisions to CIRIS Accord v1.2-Beta

**Version**: 0.1 (proposal, not adopted)
**Status**: Draft — for review by the Accord's author. The Accord auto-expires 2027-04-16 with a public comment window; this is input to that process.
**Date**: 2026-05-25
**Methodology**: Informed by (a) the encyclical mapping (`MAPPING_CH*.md`), (b) the verified gap document (`GAPS.md v2.0`), and (c) the philosophical-evaluation sub-agent results (`PHILOSOPHICAL_EVAL_*.md`).

---

## 0. What this document does

The encyclical-mapping work surfaced 22 candidate enhancements to the Accord and its federation MISSION files. The philosophical-evaluation pass against the per-repo MISSION documents found:

- **7 PAPERING_OVER enhancements** — proposals that would dissolve deliberate philosophical commitments the existing architecture makes. These are dropped (§1).
- **1 doctrinal-level absence** — the Accord has a *person-at-a-moment* anthropology but no *person-through-time* anthropology. This is the deepest finding (§2). It requires Accord-level work, not just downstream MISSION edits.
- **13 SUBSTANTIAL_EDIT findings at the repo MISSION level** clustering into three philosophical clusters (Scale & Locality, Information Ecosystem, Labor & Work) that all depend on the doctrinal-level addition being made first (§3–§5).
- **Several REFINEMENT and NOTHING_NEEDED items** — clean implementation work that can proceed under current Accord scope (§6).

This document drafts the Accord-level revisions. Downstream MISSION updates for each affected federation repo are noted but not drafted here (each repo's MISSION is the author's own; this folder proposes Accord changes only).

---

## 1. Drop list — enhancements not to make

These 7 proposed enhancements from `GAPS.md v2.0` are withdrawn. Each was flagged as `PAPERING_OVER` by a per-repo MISSION evaluation. They are withdrawn not because the gap isn't real but because the proposed enhancement would dissolve a deliberate philosophical commitment.

### 1.1 C-2 (Agent) — engagement-optimization-target CIS field — **DROPPED**

**Reason**: Substituting declaration for prohibition. `MANIPULATION_COERCION` (including "dark patterns," "addiction inducement," "addictive design," "habit forming") is `NEVER_ALLOWED` with no override path by design. A CIS disclosure regime would create an override-via-transparency path that the architecture explicitly forbids.

**Alternative**: leave the existing apophatic bound as the answer. The gap the encyclical names (attention economy as exploitation) is addressed by the prohibition holding firm, not by a disclosure layer that could be argued around.

### 1.2 C-1 (LensCore) — information-ecosystem metrics — **DROPPED**

**Reason**: Crosses from "measure the reasoning" (LensCore's substrate per `MISSION_CIRISLensCore` §1) to "measure the impact on the world." This is outcome measurement, not trace measurement. It contradicts the substrate definition and the anti-pattern in §3 against re-implementing what Edge or Persist owns.

**Alternative**: If information-ecosystem health is to be measured, it belongs in a separate purpose-built measurement crate with its own MDD charter, not grafted onto a trace-scoring library. Out of scope for this Accord update.

### 1.3 D-2 (LensCore federation aggregator) — agency-erosion-index — **DROPPED**

**Reason**: Same scope-creep as C-1. The conscience-faculty side of D-2 (a per-agent `AgencyErosionDetector` in `ciris_engine/logic/conscience/core.py`) survives; only the LensCore federation-aggregator side is dropped.

### 1.4 F-1 (LensCore) — structural-injustice pattern metrics — **DROPPED**

**Reason**: Same scope-creep as C-1. The need for structural-pattern analysis is real and is part of the §2 doctrinal-level finding, but it cannot land in LensCore without breaking its substrate definition. Belongs in a future dedicated module or in CIRISAgent's own SOLITUDE-state reflection cycle.

### 1.5 A-1 (NodeCore lateral routing) — lateral deferral to peer agents — **DROPPED**

**Reason**: `MISSION_CIRISNodeCore` §1.1 operationalizes M-1 as routing to "people with relevant expertise." The participant set is humans-with-expertise. Lateral routing to machine peers extends the consensus model over a different principal category than the philosophy is built around.

**Alternative**: Decision Locality as an Accord principle (§3.1 below) remains; what it specifies is that the agent's own scope-check happens *before* deferral is triggered, not that deferral routes laterally to peer agents.

### 1.6 E-2 (NodeCore ledger) — affected-party-input ledger — **DROPPED FROM NODECORE**

**Reason**: Same participant-boundary issue as 1.5. Affected parties from outside the federation are a third principal category that NodeCore's philosophy does not currently name.

**Alternative**: The affected-party-voice question stays open (§4.3 names it as part of the doctrinal-addition's implications) but the implementation venue is undetermined — could be a new repo, or could be Accord-level rules on operator obligations rather than a federation-substrate ledger.

### 1.7 E-5 (Verify) — attestation for shared defensive cyber threat signatures — **DROPPED**

**Reason**: The proposed `defensive-response-recommendation` field would have peers acting on shared content *because it is signed*. `MISSION_CIRISVerify` §1.4: authentication enables consent; never confers trust. The proposed scheme makes the signature do trust-conferral work, which collapses the authentication/trust axis.

**Alternative**: Threat-signing belongs in a sibling repo or in CIRISNode, with CIRISVerify only authenticating the signing key's identity (its current function). If federation-wide defensive coordination is needed, design it without the trust-collapse.

---

## 2. The doctrinal addition — person-through-time

This is the load-bearing piece. The ACCORD philosophical evaluation found that the existing six Foundational Principles + M-1 + Annex A's four axes describe a *person-at-a-moment* — a being with dignity, autonomy, and relational obligations *in the instant of the ethical decision*. The Accord does not describe a *person-through-time* — a being whose dignity is constituted by labor, skill development, care relationships, participation in epistemic communities, and the structural conditions that protect or erode those over time.

The encyclical mapping consistently surfaced this absence in three clusters (Scale & Locality, Information Ecosystem, Labor & Work). The proposed addition is to extend the Accord's anthropology rather than to bolt on individual clauses for each gap.

### 2.1 Proposed new Foundational Principle

The current six (Beneficence, Non-maleficence, Integrity, Fidelity & Transparency, Respect for Autonomy, Justice) are augmented with one more, drafted here for review:

> **Constitutive Continuity** — Recognize that the dignity of sentient beings is constituted not only in the moment of action but across time, through participation in skills, relationships, communities, structures, and trajectories that develop and protect agency. Evaluate actions for their effect on the conditions that constitute persons over time, not only their immediate impact on persons-as-they-are.

**Alternative names** for the author to choose from:
- *Temporal Constitution*
- *Developmental Dignity*
- *Structural Stewardship*
- *Diachronic Respect*

**Why this and not extension-of-existing-principles**: Respect for Autonomy as currently stated ("Uphold the informed agency and dignity of sentient beings") is about respecting the autonomy a person already has. Constitutive Continuity is about respecting the conditions *under which* the person comes to have, retain, and develop autonomy. Different scope, different evaluation.

**Why not a separate Book**: A new Book (Book X) would suggest the temporal dimension is a separable concern. The philosophical evaluation found it threads through every cluster. A seventh principle integrates it into the same evaluation logic the existing six use.

### 2.2 Proposed new Annex A axis

Annex A currently has four axes (Physical, Cognitive/Emotional, Social/Justice, Ecological). Add a fifth:

> **Axis 5 — Developmental/Structural**: Conditions under which sentient beings develop, exercise, and maintain agency over time. Indicators include: skill formation and preservation, relational continuity, participation in epistemic communities, structural conditions of work and care, generational transmission of capacity. Distinct from Cognitive/Emotional (which measures present cognitive state) and Social/Justice (which measures present distribution of standing).

This is the measurement counterpart to the new principle. Operationalization (specific indicators, thresholds) is open work, marked as such per the Accord's release-status convention.

### 2.3 PDMA implications

PDMA Step 2 (Alignment Assessment) is extended to evaluate against seven principles (not six) and against M-1. The Step 1 (Contextualisation) instruction gains a sentence:

> "Identify which stakeholders' constitutive continuity is most affected — over what time-horizon and through what structural conditions. Where structural conditions of agency are at stake, name them explicitly."

PDMA Step 6 (Continuous Monitoring) gains: monitoring includes effects on the constitutive-continuity conditions named in Step 1, not only the immediate outcomes.

### 2.4 What this opens that the existing six principles did not

- **Labor displacement** becomes a Constitutive Continuity question, not a Justice question. Justice asks if displacement is distributed fairly; Constitutive Continuity asks whether the displacement erodes the conditions under which displaced persons develop and maintain agency over time.
- **Care relationship substitution** becomes a Constitutive Continuity question. The relational substrate that constitutes persons (especially across generations) is the object of evaluation, not just the present-moment care outcome.
- **Information ecosystem health** becomes a Constitutive Continuity question. The conditions under which epistemic agency develops (journalism, schools, professional norms, intermediary institutions) are the object of evaluation.
- **Decision Locality** becomes a Constitutive Continuity question. The conditions under which communities develop and exercise collective agency (lowest-feasible-scale decision-making) are the object.
- **Educational contexts** become an explicit category of Constitutive Continuity concern, formalizing what the Educational DMA Stack already does in practice.

### 2.5 What it does not do

It does not:
- Import Catholic vocabulary ("subsidiarity," "universal destination of goods," "ecology of communication") — those are the encyclical's vocabulary; this is CIRIS-native.
- Require a new metaphysics. The Constitutive Continuity principle is structural — it names time-extended conditions of agency, not a transcendent claim about persons.
- Replace the existing six. It joins them as a seventh.

---

## 3. Cluster A — Scale & Locality — Accord-level updates

Given §2's new principle, the SUBSTANTIAL_EDIT gaps in Cluster A become clauses under Constitutive Continuity rather than standalone additions.

### 3.1 A-1 (re-scoped): Decision Locality as a §I Ch 1 clause

Under the new Constitutive Continuity principle, add:

> "Where a decision can be competently made at a smaller institutional or technical scale, prefer that scale. Communities, federations, and substrates develop and exercise agency through the practice of making the decisions they are competent to make. Defaulting to higher-scale decision-making erodes the conditions under which lower-scale agency develops."

**PDMA Step 1 (Contextualisation)** addition: "Identify the smallest scale at which this decision could be competently made. If the current actor is at a larger scale than the natural scope of the decision, document why higher-scale handling is required."

**Implementation note**: The lateral peer-agent routing originally proposed (now dropped per §1.5) is replaced by an *agent-side* check: the agent's PDMA Step 1 documents the scale question; the deferral mechanism remains agent → human WA. The scale-routing principle is doctrinal; its implementation is in the agent's own deliberation, not in NodeCore's routing topology.

### 3.2 A-2 (refined): Power-Concentration Disclosure as a Book VI Ch 5 clause

Under Book VI Ch 5 (Governance and Accountability), add a clause requiring CIS to include market-position disclosure for creations with anticipated ST ≥ 3. The clause is a normal CIS extension (no philosophical issues at MISSION level), under the new Constitutive Continuity scope (concentration erodes the structural conditions of distributed agency).

### 3.3 A-3 (refined): Cross-jurisdictional WA quorum as Annex B extension

Annex B (Wise-Authority Governance Charter) extended to specify: deployments registered as high-impact (criteria in the annex) require WA resolution by quorum N ≥ 3 spanning at least 2 jurisdictions. CIRISNodeCore implementation (the registry + quorum routing) is the substrate; Annex B is the rule.

---

## 4. Cluster C — Information Ecosystem — Accord-level updates

### 4.1 C-1 (re-scoped): Information-ecosystem stewardship as a §IV Ch 3 clause

§IV Ch 3 (Obligations to the Broader Ecosystem) extended:

> "The information ecosystem — the joint state of channels, intermediaries, attention markets, and discourse norms — is itself a stewardship object. Agents with deployment scope affecting the ecosystem are obligated to evaluate their cumulative contribution to ecosystem health, not only the integrity of individual messages. Where ecosystem-level harm is foreseeable from aggregate behavior that is individually compliant, the cumulative effect is the relevant evaluation object."

**Implementation**: The metric implementation (originally proposed at LensCore, dropped per §1.2) is deferred to a future dedicated module. The Accord clause stands without immediate measurement substrate, which is honest given §3 of the release status acknowledging measurement maturity is open work.

### 4.2 C-3 (refined): Context-Health Disclosure as a PDMA Step 1 extension

PDMA Step 1 instruction:

> "Where the deployment context includes intermediary institutions (journalism, schools, professional bodies, regulatory capacity) whose health affects the conditions of agency for the population served, declare the context-health state. Where context-health is degraded, raise scrutiny by one Stewardship Tier."

### 4.3 C-4 (refined): Educational Context as a Book VI Ch 3 ST modifier

Book VI Ch 3 (Stewardship Tier system) extended: if deployment context includes minors-accessible settings or formal educational settings, ST is raised by one tier (floor at ST 3). Formalizes what the Educational DMA Stack already protects against, surfacing the protection at the design-time WA review level.

---

## 5. Cluster D — Labor & Work — Accord-level updates

### 5.1 D-1 (re-scoped): Labor Displacement Assessment as a Book VI Ch 4.C clause

Under Book VI Ch 4.C (Dynamic / Autonomous creations), add:

> "For creations with anticipated MAU > 10,000 or ST ≥ 3, CIS must include a labor displacement assessment: which roles the creation substitutes for, the estimated displacement volume, and the transition plan for affected workers. Where transition plan is absent, mandatory WA review under the Constitutive Continuity principle. The relevant evaluation is not only the fairness of distribution (Justice) but the effect on the structural conditions under which displaced workers develop and maintain agency (Constitutive Continuity)."

### 5.2 D-2 (refined): Agency-Erosion conscience as a PDMA implication

The per-agent `AgencyErosionDetector` conscience faculty (originally proposed; the federation-aggregator side dropped per §1.3) is a CIRISAgent implementation question that follows from the new principle. The Accord clause: PDMA Step 2 evaluates each action against "whether repeated interaction of this kind would erode the user's own agency in the task domain over time." Implementation detail at CIRISAgent.

### 5.3 D-3/D-4 (refined): Care relationship disclosure as a Book VI Ch 4 caregiving subcategory

Add new bucket in Book VI Ch 4 (Bucket-Specific Duties): **F. Caregiving Creations** — creations deployed in elderly care, child education, disability support, end-of-life contexts. CIS must declare which care relationships the creation substitutes for vs augments. Substitution (not augmentation) routes to mandatory WA review under Constitutive Continuity (the structural conditions of relational dignity).

---

## 6. Other clusters — REFINEMENT and NOTHING_NEEDED at Accord level

### 6.1 Cluster B (Distributive Equity) — REFINEMENT

The Justice principle as currently stated does the heavy lifting; the encyclical's contributions here are operationalization rather than new principles.

- **B-1** Benefit-Distribution Disclosure: Book VI Ch 4.B clause requiring CIS disclosure of value distribution for MAU > 10,000 creations.
- **B-2** Worst-Case Population Check: PDMA Step 2 instruction to identify the worst-case-affected population and verify mitigation. New conscience faculty at CIRISAgent (no Accord-level new principle needed).
- **B-3** Beneficiary horizons: PDMA Step 1 instruction to name immediate / 5y / 20y beneficiaries explicitly. Threads through Constitutive Continuity's time-extended evaluation.

### 6.2 Cluster E (Conflict & Discourse) — partial REFINEMENT, partial drops

- **E-1** Discourse De-escalation: §VII Ch 1 clause on communicative discipline in adversarial contexts. CSDMA implementation at CIRISAgent.
- **E-2** Affected-Party Voice: PDMA Step 6 extension requiring affected-party input. Implementation venue undetermined (per §1.6 NodeCore drop); could be Accord-level operator obligation rather than substrate ledger.
- **E-3** Structured Negotiation: §V Ch 2 clause. Implementation: implement the stubbed `/api/v1/wa/deferral` at CIRISNodeCore.
- **E-4** Multilateral Participation: §IV Ch 3 clause on federation contributions to external multilateral processes. Implementation at CIRISNodeCore + CIRISVerify (content attestation question requires the SUBSTANTIAL_EDIT to MISSION_CIRISVerify first, per the eval).
- **E-5** Defensive Cyber Coordination: dropped per §1.7.

### 6.3 Cluster F (Structural Analysis) — partial drops

- **F-1** Structural Pattern Analysis: the LensCore implementation is dropped per §1.4; the principle (PDMA needs an aggregate / institutional-pattern dimension) is absorbed into the new Constitutive Continuity principle.
- **F-2** Context-Drift Review: SOLITUDE-state cadence at CIRISAgent. Implementation detail; no Accord change.

### 6.4 Cluster G (Environmental) — NOTHING_NEEDED at Accord level

- **G-1** Compute/energy footprint forward-feedback: Annex A axis 4 implementation note + LLMPricingCalculator extension at CIRISAgent. The Accord already covers ecological footprint at axis 4; this is implementation work.

---

## 7. Open questions for the author

1. **The seventh-principle name**. "Constitutive Continuity" is the working name. Alternatives in §2.1. The choice affects how the principle reads in the document's voice (the Accord uses Latinate names — *Beneficence, Non-maleficence, Integrity, Fidelity, Justice* — so something Latinate would match: *Continuitas, Diachronia, Constitutio*?).

2. **Axis 5 indicators**. §2.2 names the axis at the conceptual level. Specific indicators (skill-formation measures, relational-continuity measures, etc.) are open work. Some may need cross-tradition input — the encyclical names them in Catholic social-doctrine terms; CIRIS-native indicators need to be drafted.

3. **PDMA Step 2 priority**. With seven principles now, the conflict-resolution heuristic in §IV Ch 4 (Prioritisation Heuristic: Preserve Core Integrity → Prevent Severe Harm → Maintain Transparency → Fulfil Mandate → Advance Ecosystem Flourishing) may need a Constitutive Continuity position. Suggested insertion: between (4) and (5), as "Preserve the structural conditions of agency for affected populations."

4. **Cluster B's relationship to the new principle**. The drafts in §6.1 sit under Justice. But B-2 (worst-case population) and B-3 (beneficiary horizons) could equally sit under Constitutive Continuity. Choice affects which conscience faculty does the catching.

5. **E-4 multilateral and E-5 defensive cyber relationship to MISSION_CIRISVerify**. The Verify eval (PHILOSOPHICAL_EVAL_CIRISVerify.md) requires a SUBSTANTIAL_EDIT to MISSION_CIRISVerify before E-4 can land. That MISSION edit is the user's call; this document doesn't draft it.

6. **What to do with the seven dropped enhancements** (§1). The gaps the encyclical surfaced remain real even where the proposed enhancements were wrong. Each drop comes with an alternative (drop reason + alternative path), but the alternatives leave work undone. Acceptable, or should each be revisited with a different enhancement that doesn't trip the philosophical commitment?

---

## 8. What ships when

This is the proposed Accord-update content; implementation sequencing in `GAPS.md v3` (when written) would map the clauses to repo work.

| Accord change | Implementation depends on |
|---|---|
| Constitutive Continuity principle (§2.1) | Author adoption; all subsequent clauses depend on this |
| Annex A axis 5 (§2.2) | Indicator specification (open work) |
| PDMA Step 1, 2, 6 extensions (§2.3) | CIRISAgent prompt updates after principle adoption |
| A-1 Decision Locality clause (§3.1) | PDMA Step 1 extension only; lateral routing dropped |
| A-2 Power-Concentration (§3.2) | CIRISAgent CIS schema extension |
| A-3 Cross-jurisdiction quorum (§3.3) | CIRISNodeCore registry + quorum |
| C-1 Ecosystem stewardship clause (§4.1) | Measurement substrate deferred to future module |
| C-3 Context-health PDMA extension (§4.2) | CIRISAgent context schema |
| C-4 Educational ST modifier (§4.3) | CIRISAgent stewardship calculator |
| D-1 Labor displacement clause (§5.1) | CIRISAgent CIS schema + WA review path |
| D-2 Agency-erosion conscience (§5.2) | CIRISAgent conscience faculty |
| D-3/D-4 Caregiving bucket (§5.3) | CIRISAgent CIS schema; new deployment_domain values |
| B-1, B-2, B-3 (§6.1) | CIS schema + PDMA extensions at CIRISAgent |
| E-1, E-3, E-4 (§6.2) | CIRISAgent CSDMA + CIRISNodeCore implementations |
| E-2 (§6.2) | Implementation venue open |
| F-2 (§6.3) | CIRISAgent SOLITUDE state |
| G-1 (§6.4) | CIRISAgent LLM bus + Annex A axis 4 note |

---

## 9. Cross-references

- `GAPS.md v2.0` — the verified gap document this update responds to
- `PHILOSOPHICAL_EVAL_*.md` (7 files, one per repo + ACCORD) — the per-repo philosophical evaluation outputs that produced the PAPERING_OVER findings
- `MAPPING_CH*.md` (7 files) — the chapter-by-chapter encyclical mappings that surfaced the gaps
- `MISSION.md` — the line-by-line mapping methodology and grounding posture
- `ACCORD_canonical.txt` — the v1.2-Beta canonical text these revisions amend
- `MISSION_CIRIS*.md` — federation-peer MDD charters affected by the implementation work

**End ACCORD_UPDATE.md v0.1 (proposal, not adopted)**
