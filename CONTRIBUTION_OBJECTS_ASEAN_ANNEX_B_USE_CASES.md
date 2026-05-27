# CONTRIBUTION_OBJECTS — ASEAN Guide on AI Governance and Ethics (2024), Annex B: Use Cases

**Batch**: `asean_guide_v1`
**Scope**: Annex B, lines 3382–3858 of `source_material/governance/asean_guide_v1/asean_guide.txt`
**Source range**: 6 descriptive case studies (pages 73–86)
**Primer applied**: `LANGUAGE_PRIMER.md` v1.1 (FSD-002 v1.4-aligned)
**Methodology**: per `METHODOLOGY.md` §8.5 composition-before-extension and §1.10.1 four-test prefix-admission gate
**Phase 2 status**: complete (2026-05-27)
**Light-pass note**: this annex is **descriptive corporate communications, not normative content**. The use cases illustrate practices already named in §B (Guiding Principles) and §C (AI Governance Framework) of the main guide; they make no first-order "should" claims of their own. Per METHODOLOGY §1.10.1 operational-language gate, marketing prose about what an organisation **does** is not a wire-format Contribution about what **ought** to happen.

---

## §1 — Annex framing

Annex B presents 6 self-reported case studies submitted by Aboitiz Group (Philippines), EY (multinational), Gojek (Indonesia), UCARE.AI (Singapore), Singapore's National AI Office, and Singapore's Ministry of Education. Each follows the same structure: a brief organisational profile, then "Illustration on …" sub-sections keyed to the §C four-component framework (internal governance / human involvement levels / operations management / stakeholder interaction).

The case studies are **demonstrative**: they show how a real organisation has applied the §B/§C normative content. They do not extend or qualify the normative content; they exemplify it. This is the textbook shape of T-2 PASTORAL_PROSE in a secular-corporate register — narrative illustrative material whose moral/operational seriousness is fully carried by the upstream normative attestations the cases illustrate.

The §1.10.1 T2 mechanism-vs-judgment test bites hard here: "Aboitiz adopts appropriate strategies" / "UCARE.AI was mindful to be transparent" / "EY is committed to" are all subjective-quality phrasings. Any prefix that tried to absorb such statements would fail T2 (e.g., `corporate_commitment:transparency:*` would be a judgment-laden prefix, not a mechanism). The honest move is to mark the cases as T-2 and let the normative attestations from §B/§C of the main guide carry the actual operational claims.

---

## §2 — Per-case summaries

### §2.1 — Aboitiz Group (lines 3387–3449, pages 74–75)

**Summary**: A Philippines-based conglomerate describes its Model Governance Policy, its multi-stakeholder Model Governance Management Committee composition, its pre-development and pre-deployment risk assessments, and its lifecycle-spanning governance measures.

**Verdict for the entire case**: **not-translated**
**Classification**: **T-2 (PASTORAL_PROSE / illustrative-corporate-communications)**
**Rationale**: every paragraph reports what Aboitiz does as an institution. There are no first-order normative claims ("should") that aren't already carried by §C of the main guide (which Aboitiz is illustrating). The "core objectives" bullets ("Establishing appropriate responsibilities…", "Establishing clear risk assessment protocols…", "Regular review…") are organisation-internal policy commitments, not federation-scale normative claims. The committee-composition list (CISO, DPO, CTO, CRO, etc.) is descriptive corporate structure, not a normative claim about who should sit at AI governance tables.

**Normative units extracted**: 0.

---

### §2.2 — EY (lines 3455–3507, pages 76–77)

**Summary**: EY describes its six internal AI principles (Accountability, Data Rights, Reliability/Safety/Security, Transparency & Explainability, Fairness & Inclusiveness, Professional Responsibility), its Trusted AI Framework, its EY Fabric XOps platform, and its Model Risk Tiering approach (High/Medium/Low).

**Verdict for the entire case**: **not-translated**
**Classification**: **T-2 (PASTORAL_PROSE / illustrative-corporate-communications)**
**Rationale**: the EY principles are *aligned to* the ASEAN Guide principles (per the case's own text, line 3470–3471) — meaning the normative content is already carried by §B of the main guide. The Trusted AI Framework, EY Fabric, and Model Risk Tiering are commercial-product descriptions whose normative content (continuous monitoring, risk-tiered oversight, model lifecycle governance) is carried by §C.3 (Operations Management) of the main guide. No additional normative claim survives the §1.10.1 T2 test on its own merits here.

**Normative units extracted**: 0.

---

### §2.3 — Gojek (lines 3513–3573, pages 78–79)

**Summary**: Gojek (Indonesia) describes its automated promotion-allocation AI, its offline benchmarking pre-deployment, its online monitoring of deployed models for drift, and the Data Science / Campaign Manager role split.

**Verdict for the entire case**: **not-translated**
**Classification**: **T-2 (PASTORAL_PROSE / illustrative-corporate-communications)**
**Rationale**: every clause is a description of Gojek's own practice. The "offline benchmark prior to deployment + online monitoring for drift" sequence is the §C.3 operations-management pattern; the Data Science / Campaign Manager role split is the §C.1 internal-governance pattern. Nothing here adds a normative claim beyond what the main-guide §B/§C attestations already carry.

**Normative units extracted**: 0.

---

### §2.4 — UCARE.AI (lines 3579–3705, pages 80–82, two sub-cases)

**Summary**: Two case studies on the same organisation. Sub-case 1 covers data security/privacy/transparency (PDPA compliance, encryption, anonymisation at source, client-specific models, transparency to data managers and patients). Sub-case 2 covers oversight/validation/monitoring (primary+secondary data science lead pairing, weekly client check-ins, medical advisor review, QA review, continuous post-deployment validation, explainability features in the Cost Predictor).

**Verdict for the entire case**: **not-translated**
**Classification**: **T-2 (PASTORAL_PROSE / illustrative-corporate-communications)**
**Rationale**: descriptive throughout. UCARE.AI's PDPA adherence is compliance with an external normative regime (Singapore's PDPA 2012), not a federation-scale normative claim emitted by UCARE.AI itself. The dual-lead model-development pattern, the medical-advisor review step, the explainability-on-demand feature — all are commercial-product descriptions. Even the explicit "trust was essential" phrasing (line 3656) is rhetorical framing, not a structured claim.

One borderline candidate noted and rejected: the description "UCARE.AI made a conscious decision to declare the use of AI in its analysis and prediction of bill amounts to Parkway's data managers and its patients" (lines 3637–3638) could arguably illustrate a `goal:community` Contribution about disclosure-to-affected-parties. But the normative content (AI-use should be disclosed to data subjects) is fully carried by §B.1 (Transparency and Explainability) of the main guide; the case study is illustrative, not load-bearing.

**Normative units extracted**: 0.

---

### §2.5 — Smart Nation Group / National AI Office, Singapore (lines 3711–3785, pages 83–84)

**Summary**: Singapore's National AI Office (NAIO) describes its LLM-product governance: a tiered approval-gate structure (no approval for internal experiments / approval gate at beta / approval gate at full deployment), risk-tiering by task type and audience type, and recommended mitigations (robustness testing, red-teaming, bug bounties, rate-limiting, visual UX cues for misuse mitigation).

**Verdict for the entire case**: **not-translated**
**Classification**: **T-2 (PASTORAL_PROSE / illustrative-corporate-communications)**
**Rationale**: this is a description of Singapore-government internal policy. The risk-tiering dimensions (task: productivity tools vs factual retrieval; audience: internal vs external-facing) are operationally interesting but appear as **described practice**, not as a normative claim that "all federations should risk-tier this way." The normative shape — risk-proportionate oversight, public-facing systems require adversarial robustness, user-facing systems need misuse-mitigation UX — is already carried by §B (Guiding Principles 3 Security/Safety, 4 Human-centricity) and §C.2 (level-of-human-involvement) of the main guide.

One borderline candidate noted and rejected: the structured approval-gate diagram (lines 3727–3753) could be read as a Method-level claim instantiating a §C.1 governance Approach. But within Annex B framing it is presented as an illustration of how one government applied §C.1, not as a normative recommendation. The structural-pattern content (approval gates at experimentation → beta → deployment thresholds) is properly captured at §C.1 in the main-guide normative mapping.

**Normative units extracted**: 0.

---

### §2.6 — Ministry of Education, Singapore (lines 3791–3853, pages 85–86)

**Summary**: Singapore's Ministry of Education (MOE) describes its AI-enabled Adaptive Learning System (ALS) deployed in the Student Learning Space (SLS): personalised learning pathways, teacher-monitoring dashboard, teacher override/supplementation capability, monthly performance reports against pre-determined thresholds, multi-stakeholder engagement during design, and human-centricity considerations (learning-readiness matching, design pilots, teacher resource contributions).

**Verdict for the entire case**: **not-translated**
**Classification**: **T-2 (PASTORAL_PROSE / illustrative-corporate-communications)**
**Rationale**: descriptive throughout. The teacher-in-the-loop pattern ("teachers can monitor … and provide timely interventions"; "teachers to recommend specific subtopics … and supplement ALS' recommendations with their professional insights") illustrates §C.2 (HITL/HOTL/HOOTL involvement-level determination) but does not extend it. The continuous-monitoring-against-threshold pattern illustrates §C.3 (operations management). Stakeholder engagement during design illustrates §C.4 (stakeholder interaction). The "human-centricity" sub-section (lines 3838–3848) reports user-research practice, not a normative principle that supersedes or refines §B.4.

**Normative units extracted**: 0.

---

## §3 — Aggregate batch summary

**Total normative units extracted across all 6 case studies**: **0**

**Verdict distribution**:
- 6 cases × not-translated (T-2 PASTORAL_PROSE / illustrative-corporate-communications)
- 0 cases × clean / composed / partial

This is the expected and correct outcome for descriptive case-study material. The annex's role per the main guide is to **show how the §B/§C normative content has been operationalised by real organisations** — illustration, not first-order normative claim. The normative content the cases illustrate has already been mapped in the §B (Guiding Principles) and §C (AI Governance Framework) Contribution objects from earlier phases of `asean_guide_v1`.

---

## §4 — T-2 vs T-3 discrimination check

Per LANGUAGE_PRIMER §10: "**Distinguishing T-2 from T-3**: does naming the claim in prose + existing wire attestations carry its full moral seriousness? If yes → T-2 (pastoral; correctly in prose). If no → T-3 (gap; would benefit from wire)."

For every paragraph in Annex B: the moral/operational seriousness of the claim being illustrated is **already** carried by the main-guide §B/§C attestations. The case studies add no novel structural shape that the existing namespace cannot reach. Therefore T-2 is correct posture; no T-3 candidates are recommended from this annex.

---

## §5 — Novel claims that don't fit elsewhere in the batch

**None identified.**

A close reading was kept open for the following potentially-novel shapes that might have justified a separate emission:

| Candidate shape | Where it appeared | Why rejected |
|---|---|---|
| Sectoral risk-tiering dimensions (task × audience, per NAIO) | §2.5 (lines 3763–3772) | Reported as described practice; the normative axis (risk-proportionate oversight) is already carried by §C.2 |
| Dual-lead AI development (UCARE.AI primary + secondary data scientist) | §2.4 (line 3664) | Organisation-internal QA pattern; no federation-scale normative content |
| Approval-gate diagram (NAIO three-stage) | §2.5 (lines 3727–3753) | Visual presentation of §C.1 internal-governance pattern; no new normative shape |
| Teacher resource-contribution feedback loop (MOE ALS) | §2.6 (lines 3823–3827) | Illustrates §C.4 stakeholder-interaction iteration; no novel claim |
| Compliance with external personal-data regime (UCARE.AI / PDPA 2012) | §2.4 (lines 3596–3598) | Compliance posture toward an external authority; the federation-side normative content is `licensure:*` on the issuing jurisdiction, which is carried at the Registry layer, not at the case-study layer |

In all five cases the candidate failed because the underlying normative content is **already** carried by upstream attestations from the main-guide §B/§C mapping.

---

## §6 — Methodology notes for this light pass

Per the batch prompt's framing ("Process LIGHTLY"), no atomic-unit inflation was attempted. The lightest-possible honest output is exactly what was produced: six per-case summary paragraphs with verdict and rationale, no wire envelopes, no proposed extensions.

This pass also serves as a **negative discipline check** on the GOVERNANCE_FABRIC_MAPPING_STANDARD §2 Phase 2 process. The expected-distribution row in `manifest.yaml` line 89–90 anticipated "very high clean+composed rate (~85%+)" for the main body; the manifest correctly flagged Annex B separately (line 71: "Descriptive case studies; not normative — light mapping only or skipped") as the exception. This pass confirms the manifest's classification: zero normative-unit yield from descriptive case studies is the right result, not a failure of translation discipline.

The §1.10.1 four-test gate's T2 (mechanism-vs-judgment) is the load-bearing filter here. Subjective-quality phrasings like "committed to," "mindful to be transparent," "trust was essential," and "harness collaboration and innovation" are the canonical T-2 shape — they pass through any structural-mapping pass without leaving wire-format residue. The framework correctly absorbs the content as prose context for the §B/§C attestations and emits no Contributions of its own.

---

## §7 — Cross-references

- `manifest.yaml` line 69–78: Annex B sub-section enumeration and "light mapping only or skipped" classification (corroborated).
- `LANGUAGE_PRIMER.md` §10: T-2 PASTORAL_PROSE definition and the T-2 vs T-3 discrimination check.
- `LANGUAGE_PRIMER.md` §6: §1.10.1 four-test prefix-admission gate (T2 mechanism-vs-judgment test applied).
- `METHODOLOGY.md` §8.5.2: composition-before-extension discipline (no T-3 candidates emitted from this annex).
- `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` §7.4: ASEAN Guide batch slot.
- Upstream Phase 2 outputs (when available): §B Guiding Principles and §C AI Governance Framework Contribution objects, which carry the normative content that Annex B illustrates.

---

**End CONTRIBUTION_OBJECTS_ASEAN_ANNEX_B_USE_CASES.md**
