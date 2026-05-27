# CONTRIBUTION_OBJECTS_ASEAN_AB_INTRO_PRINCIPLES.md
# ASEAN Guide on AI Governance and Ethics (2024) — Section A (Introduction) + Section B (7 Guiding Principles)
# The 7 ASEAN Principles: Transparency/Explainability — Fairness/Equity — Security/Safety —
# Human-centricity — Privacy/Data Governance — Accountability/Integrity — Robustness/Reliability
# Source: source_material/governance/asean_guide_v1/asean_guide.txt (lines 226–718)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: asean_guide_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}

---

## Section scope and framing

Section A (Introduction; lines 226–390) declares the document's posture as a *voluntary,
practical guide* for ASEAN organisations designing/developing/deploying traditional (i.e.
non-generative, non-military, non-dual-use) AI. Most of A is operationally low-density —
scope-of-use declarations, target-audience listings, definitions. Translation is sparse
by design; the wire-bearing weight of the document lives in Section B (the 7 principles)
and Section C (the AI Governance Framework, mapped in a sibling output).

Section B (lines 391–718) names 7 guiding principles, each with 2–8 paragraphs of
elaboration. These principles are the **direct cross-document comparison axis** for the
trio + MH alignment work: EU HLEG's 7 requirements (Chapter II) vs IEEE EAD's 8 General
Principles vs ASEAN's 7 guiding principles. The wire-format mapping makes that
comparison computable.

Output is grouped by Principle (B.1–B.7). Each Principle ends with a per-Principle
summary line naming primary CIRIS prefix family/families, per-Principle coverage %, and
any T-3 candidates within it. Section A units are grouped under a single A.* header
because their structural weight is low and their content is mostly scope/definitions.

Source quotes are bounded at ≤ 2 sentences per LANGUAGE_PRIMER discipline. Humble
posture: the wire format captures structural shape; rhetorical and operational nuance
that does not survive the envelope is named explicitly on the `nuance_lost:` line at
each unit.

---

# Section A — Introduction

---

## §A.0 — Section header (line 226) + Section B header (line 391)

```yaml
# Lines 226, 391 — Structural section headers; no operational claim
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Bare section headers are document-structural framing, not independent operational
  claims. Their structural commitment is carried by the per-paragraph attestations
  below.
nuance_lost: |
  None — header strings have no operational content.
```

---

## §A.intro — AI as adaptive technology; alignment with national/corporate values

```yaml
# Lines 228–238 — Opening framing paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:ai_distinct_from_other_software"
      score: 0.85
      confidence: 0.80
      context: >
        "AI systems should be treated differently from other software systems because of
        its unique characteristics and risks." Capabilities outpace monitoring + validation;
        decentralised development via low entry barriers + open-source proliferation;
        decisions today may differ from decisions tomorrow due to adaptation. Structural
        claim: AI requires a dedicated governance treatment distinct from generic software.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A lines 228–238"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:alignment_with_values"
      score: 0.85
      confidence: 0.80
      context: >
        "Decisions made by AI are aligned with national and corporate values, as well as
        broader ethical and social norms." Fidelity-to-mandate framing — the deployer is
        the principal, and the AI's decisions must remain aligned with the principal's
        declared values.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A lines 236–238"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: composed
nuance_lost: |
  The "Southeast Asia is no exception" regional anchoring is a context-locating
  statement; it does not survive as a wire claim because cohort_scope=community for
  fidelity already carries the appropriate geographic-scope locality at composition
  time. The "transformative potential" language is rhetorical framing (T-2-flavoured)
  and is not separately attested.
```

---

## §A.adm — ASEAN Digital Masterplan 2025 + referenced peer frameworks (lines 240–251)

```yaml
# Lines 240–251 — ADM2025 reference + UNESCO + EU HLEG cited as sources consulted
contributions:
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_attestation_id: "<adm2025-bootstrap-attestation-id>"
    attestation_envelope:
      delegated_scope: ["regional_ai_governance_authority"]
      delegation_purpose: "authority_source"
      delegation_valid_from: "2024-02-02"
      witness_relation: external
      evidence_refs:
        - "asean_guide §A lines 240–243"
        - "ADM2025 Enabling Action 2.7"
      schema_ref: "FSD-002 §2.2.1"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "multilateral_participation:ASEAN:framework_drafting"
      score: 1.0
      confidence: 0.90
      context: >
        ADM2025 EA 2.7 commissions the development + adoption of a regional policy on AI
        governance and ethics. The Guide is the named output of that commission. UNESCO's
        Recommendation on AI Ethics + EU HLEG Ethics Guidelines named as referenced
        sources in drafting. This is a multilateral_participation:* attestation —
        ASEAN-Member-State coordination on an AI-governance instrument.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A lines 240–251"
        - "Footnote 3 (UNESCO 2021); Footnote 4 (EU HLEG 2019)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation:*)"
verdict: composed
nuance_lost: |
  Singapore Model AI Governance + OECD Recommendation on AI are cited as peer examples
  (lines 245–246) but not as authority sources; they are bibliographic context. Not
  separately attested. The "leading digital community and economic bloc" vision
  language is rhetorical framing (T-2) and is not separately attested.
```

---

## §A.aim — Guide aims to empower org/gov to design/develop/deploy AI responsibly + raise trust

```yaml
# Lines 253–254 — Aim statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.85
      confidence: 0.85
      context: >
        "The ASEAN Guide on AI Governance and Ethics aims to empower organisations and
        governments in the region to design, develop, and deploy traditional AI systems
        responsibly and increase users' trust in AI." Goal-level claim at the affiliations
        scope (ASEAN member states + organisations operating in the region).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A lines 253–254"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: goal:{scale})"
verdict: clean
nuance_lost: |
  "Traditional AI systems" scoping (i.e., excluding generative AI, excluding military,
  excluding dual-use) is a scope-narrowing carried via cohort_scope=affiliations + the
  manifest's noted exclusion of the expanded GenAI supplement. Not separately attested
  as a distinct claim.
```

---

## §A.1 — Objectives (lines 278–300): scope, applicability, living-document posture

```yaml
# Lines 278–300 — Objectives subsection (4 paragraphs)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:regional"
      score: 1.0
      confidence: 0.85
      context: >
        Guide focuses on "encouraging alignment within ASEAN and fostering the
        interoperability of AI frameworks across jurisdictions." Includes recommendations
        on national-level and regional-level initiatives. Decision-locality claim at
        regional scope per the §6.1.5 locality-scaled-quorum machinery: the framework's
        consequential reach is regional, not federation-scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A.1 lines 280–284"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:voluntary_adoption_posture"
      score: 0.70
      confidence: 0.85
      context: >
        "While adoption of the framework laid out herein is voluntary, this Guide can help
        organisations build trust among stakeholders and the public as well as align their
        AI practices with international standards and best practices." Voluntary posture
        is a key mutability scoping: the Guide does not bind, it advises. score 0.70 (not
        1.0) reflects the voluntary character of the obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A.1 lines 291–295"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_attestation_id: "<placeholder-prior-asean-ai-position-id>"
    attestation_envelope:
      references_attestation_id: "<placeholder-prior-asean-ai-position-id>"
      supersession_reason: "living_document_refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      evidence_refs:
        - "asean_guide §A.1 lines 297–300"
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
nuance_lost: |
  "Living document that should be periodically reviewed" maps structurally onto
  supersedes-discipline (future versions will supersede this one); the placeholder
  attested_attestation_id signals the recursive intent but cannot point at a
  not-yet-existing prior version. "Industry partners" consultation language is
  scaffolding for §C.4 stakeholder interaction; not attested here.
```

---

## §A.2 — Assumptions (lines 303–322): holistic management + legal compliance + state-of-the-art tracking

```yaml
# Lines 303–322 — Assumptions subsection
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:holistic_ecosystem_management"
      score: 0.85
      confidence: 0.80
      context: >
        "AI systems need to be managed holistically, including its ecosystem and all
        components — human operator, Internet of Things (IoT), robotics, traditional
        technology, vendors, etc." The framework presupposes ecosystem-level rather than
        component-level governance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A.2 lines 305–309"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:legal_compliance"
      score: 1.0
      confidence: 0.95
      context: >
        "Developers and deployers need to adhere to applicable national laws and
        regulations, including sector-specific laws and constitutions." Guide "does not
        replace or supersede any existing or upcoming laws and only serves as a guide for
        responsible design, development, and deployment of AI in the region." Lawful-AI
        baseline matching the EU HLEG Chapter I "lawful AI" foundational component.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §A.2 lines 311–317"
      cohort_scope: affiliations
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: composed
nuance_lost: |
  Specific reference to ISMS / data management / cybersecurity / IoT as adjacent
  standards bodies (line 308) is bibliographic context; sector-specific lookup is
  carried by jurisdictional tagging at deployment composition. State-of-the-art
  tracking obligation (lines 319–322) is operational refresh discipline; not separately
  attested — carried by mutability: amendable on every claim.
```

---

## §A.3 — Target Audience (lines 333–340)

```yaml
# Lines 333–340 — Target Audience subsection
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Target-audience listing (AI developers, deployers, academic professionals,
  policymakers, "everyone that is interested in utilising or scaling up AI systems")
  is taxonomic scaffolding for downstream attestations. Per-stakeholder applicability
  is carried implicitly by cohort_scope and by Section C's role-specific subsections
  ("organisations" / "deployer" / "user"). No independent wire claim is made here.
nuance_lost: |
  The deliberate inclusion of "academic professionals" and "everyone interested" alongside
  practitioners is a soft-inclusive audience-framing not captured in cohort_scope. Carried
  by adjacent C-section attestations at deployment composition.
```

---

## §A.4 — Definitions (lines 343–378)

```yaml
# Lines 343–378 — Definitions subsection (ASEAN, AI, AI system, Deep Learning, Deployer,
# Developer, Machine Learning, User)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Term definitions are document-internal terminology fixings, not standalone operational
  claims. They scope downstream attestations (e.g., "deployer should X" presupposes the
  definition of deployer). Wire-format consumers compose the definitions implicitly via
  cohort_scope on the attestations that reference these terms. Per LANGUAGE_PRIMER §8
  Step 1(b): scope-setting framing correctly stays in prose.
nuance_lost: |
  The AI / AI-system definitions explicitly include "operate with varying levels of
  autonomy" — a real conceptual choice that anticipates the HITL/HOTL/HOOTL discipline
  in Section C. Carried as scaffolding, not as an independent attestation. The
  "engineered or machine-based system" framing carefully sidesteps a substrate-claim
  about agency; this nuance is lost in wire form but carried structurally by the
  framework's existing substrate-neutrality (Book IX §6.2 Universality).
```

**Section A summary**
- Primary CIRIS families composed onto: **Family A STANDING** — `integrity:*` (ai_distinct + holistic_ecosystem), `fidelity:*` (alignment + voluntary_adoption + legal_compliance); **Family B ACTION** — `goal:affiliations`, `locality:decision:regional`; **Family A STANDING** — `multilateral_participation:ASEAN:framework_drafting`; **structural primitives** — `delegates_to` (ADM2025 authority source), `supersedes` (living-document placeholder).
- 7 atomic units; 4 composed + 1 clean + 2 not-translated (T-2). Clean+composed = 5/7 = **71%**.
- T-3 candidates: none. Section A is scope/definitions-heavy and intentionally low-density.

---

# Section B — Guiding Principles for the Framework

---

## §B.intro — The 7 principles ensure trust + ethical AI design/development/deployment

```yaml
# Lines 393–395 — Section B opening
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:principles_ensure_trust_in_ai"
      score: 0.85
      confidence: 0.80
      context: >
        "The seven guiding principles below help to ensure trust in AI and the design,
        development, and deployment of ethical AI systems. They also provide guidance on
        how AI systems should be designed, developed, and deployed in ways which consider
        the broader societal impact." Structural commitment to the 7-principle rubric.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B lines 393–395"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  "Broader societal impact" framing anticipates the absent "Societal & environmental
  wellbeing" principle that EU HLEG names as Requirement 6 and that ASEAN does NOT
  carry as a standalone principle. The cross-document comparison surfaces this asymmetry
  in §B.7 nuance_lost notes; not an independent attestation here.
```

---

# §B.1 — Transparency and Explainability

---

## §B.1.0 — Transparency definition: disclosure of AI involvement + data + purpose

```yaml
# Lines 398–403 — Transparency definition paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:ai_involvement_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        Transparency = "providing disclosure on when an AI system is being used and the
        involvement of an AI system in decision-making, what kind of data it uses, and
        its purpose." Individuals become aware + can make an informed choice. Direct
        match to CIRISVerify transparency_log:* family and to the language_guidance
        "never-deny-AI" operational rule.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 400–403"
        - "ContributionRef(source_material/language_guidance/en.txt::never-deny-AI)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:informed_choice_to_use_ai"
      score: 1.0
      confidence: 0.85
      context: >
        "By disclosing to individuals that AI is used in the system, individuals will
        become aware and can make an informed choice of whether to use the AI-enabled
        system." Autonomy-preserving informed-consent claim on the user-side.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 401–403"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: composed
nuance_lost: |
  "Informed choice of whether to use" is more demanding than EU HLEG §1.4.c's "option to
  decide against AI interaction" — ASEAN frames disclosure as enabling choice itself,
  not merely opt-out. The strength differential is carried by confidence 0.85; the
  semantic distinction is partially carried but the consumer must read context to
  recover it.
```

---

## §B.1.1 — Explainability definition: reasoning understandable to a range of people

```yaml
# Lines 405–407 — Explainability definition paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:explainability_to_diverse_audiences"
      score: 1.0
      confidence: 0.90
      context: >
        Explainability = "ability to communicate the reasoning behind an AI system's
        decision in a way that is understandable to a range of people, as it is not
        always clear how an AI system has arrived at a conclusion." Audience-adapted
        explanation claim; EU HLEG §1.4.b "appropriate to stakeholder expertise" cousin.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 405–407"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I integrity)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  "A range of people" is intentionally less specific than EU HLEG's
  "layperson/regulator/researcher" trichotomy. The audience differentiation is
  attested-as-existing but not attested-at-resolution; downstream composition with
  expertise:* could be used to recover the tiered structure if needed.
```

---

## §B.1.2 — Public trust through user awareness of AI use + decision logic

```yaml
# Lines 409–411 — Public trust paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:public_trust_through_disclosure"
      score: 0.85
      confidence: 0.80
      context: >
        "In order to build public trust in AI, it is important to ensure that users are
        aware of the use of AI technology and understand how information from their
        interaction is used and how the AI system makes its decisions using the
        information provided." Trust-as-output framing of transparency + explainability.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 409–411"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  "Public trust" is treated as an aggregate societal outcome here, not as a
  per-individual relational good — this is rhetorically aligned with the EU HLEG
  "Trustworthy AI" framing but does not engage the relational-trust depth that the
  CIRIS framework's amae / jeong polyglot anchoring carries. Not separately attested;
  the integrity prefix alone does not reach into that deeper relational layer.
```

---

## §B.1.3 — Deployer responsibility: clear disclosure + bias-discrimination cautionary

```yaml
# Lines 413–423 — Deployer responsibility paragraph (with historical bias examples)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:deployer_disclosure_obligation"
      score: 1.0
      confidence: 0.90
      context: >
        "Deployers have a responsibility to clearly disclose the implementation of an AI
        system to stakeholders and foster general awareness of the AI system being used."
        Deployer-side transparency-log obligation; complements the user-side disclosure
        claim in §B.1.0.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 413–415"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:bias_marginalisation"
      score: 0.0
      confidence: 0.80
      context: >
        "In the past, AI algorithms have been found to discriminate against female job
        applicants and have failed to accurately recognise the faces of dark-skinned
        women." Detection-pattern claim: population-scale correlation collapse (ρ→1) on
        affected cohorts (gender / skin tone). LensCore detection family; score 0.0
        placeholder pending calibration version pin.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §B.1 lines 418–419"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
verdict: composed
nuance_lost: |
  The "ecommerce platform / purchase history" example (lines 421–423) is illustrative
  scaffolding (T-2) and not separately attested. The "in the past" framing of the
  discrimination examples positions them as cautionary cases, not as ongoing claims;
  the detection envelope cannot distinguish historical-pattern-cited from
  currently-active-pattern — confidence 0.80 partly reflects this.
```

---

## §B.1.4 — Explanation depth: text + heatmaps + significant-factor disclosure

```yaml
# Lines 425–434 — Explanation depth paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:explanation_depth_proportional"
      score: 1.0
      confidence: 0.85
      context: >
        Developers + deployers "should also strive to foster general understanding among
        users of how such systems work with simple and easy to understand explanations on
        how the AI system makes decisions." Explanations can range from simple text to
        heatmaps over relevant text/image regions; cardiac-arrest prediction example —
        most significant factors disclosed to medical professionals.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 425–434"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  The technique enumeration (text / heatmap / significant-factor) is methodological
  detail that does not survive the envelope cleanly. A Family-B method:* attestation
  could be composed under a deployer-specific Approach to carry it; this is left to
  Section C / deployment composition.
```

---

## §B.1.5 — Black-box models: outcome-based explanations as substitute

```yaml
# Lines 436–438 — Black-box outcome-based explanations paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:outcome_based_explanation_fallback"
      score: 0.85
      confidence: 0.80
      context: >
        "Where 'black box' models are deployed, rendering it difficult, if not impossible
        to provide explanations as to the workings of the AI system, outcome-based
        explanations, with a focus on explaining the impact of decision-making or results
        flowing from the AI system may be relied on." Concedes a fallback regime when
        mechanism-explanation is technically infeasible.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 436–438"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  The "black box" allowance is a pragmatic concession that EU HLEG §1.4.b's
  "explainability vs accuracy trade-off" sentence makes more cautiously. ASEAN's
  framing treats outcome-based explanation as an acceptable substitute; EU HLEG treats
  it as a trade-off requiring justification. The strength differential (score 0.85
  here vs higher in EU HLEG) carries some of the distinction; not all.
```

---

## §B.1.6 — Alternative confidence-building: repeatability + traceability + auditability + Model Cards

```yaml
# Lines 447–476 — Alternative measures bullet-list paragraph + closing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:reproducibility_attestation"
      score: 1.0
      confidence: 0.90
      context: >
        "Documenting the repeatability of results produced by the AI system... Some
        practices to demonstrate repeatability include conducting repeatability
        assessments to ensure deployments in live environments are repeatable and
        performing counterfactual fairness testing." Repeatability = ability to obtain
        same results given same scenario. Maps to integrity + verification discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 451–456"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:audit_trail_inclusion"
      score: 1.0
      confidence: 0.90
      context: >
        "Ensuring traceability by building an audit trail to document the AI system
        development and decision-making process, implementing a black box recorder that
        captures all input data streams, or storing data appropriately to avoid
        degradation and alteration." Direct match to CIRISVerify transparency_log:*
        and to CIRISPersist audit_chain:* composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 458–460"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:auditability_provenance"
      score: 1.0
      confidence: 0.85
      context: >
        "Facilitating auditability by keeping a comprehensive record of data provenance,
        procurement, pre-processing, lineage, storage, and security." Plus a risk-based
        scoping note ("auditability does not necessarily entail making certain
        confidential information... publicly available"). Auditability composed with
        provenance + risk-tiered disclosure.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 462–469"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:model_card_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        "Using AI Model Cards, which are short documents accompanying trained machine
        learning models that disclose the context in which models are intended to be
        used, details of the performance evaluation procedures, and other relevant
        information." Concrete artifact-level transparency commitment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.1 lines 471–473"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The "risk-based approach" caveat on auditability (lines 467–469) is a real qualifier
  — confidential business model / IP need not be publicly disclosed. The envelope
  carries it via score 0.85 (slightly less than the absolute 1.0 of other transparency
  claims) but the consumer must read context to recover the qualification. The
  closing paragraph about deployer-developer collaboration on transparency (lines
  475–476) is operational scaffolding for Section C — not separately attested here.
```

**§B.1 Transparency and Explainability — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `transparency_log:*` (CIRISVerify, central anchor — ai_involvement_disclosure / deployer_disclosure_obligation / audit_trail_inclusion / auditability_provenance / model_card_disclosure), `integrity:*` (explainability_to_diverse_audiences / public_trust_through_disclosure / explanation_depth_proportional / outcome_based_explanation_fallback / reproducibility_attestation), `autonomy:informed_choice_to_use_ai`; **Family C DETECTION** — `detection:correlated_action:participation_exclusion:bias_marginalisation`.
- Coverage: 7 substantive paragraphs (§B.1.0–§B.1.6). 7/7 clean+composed = **100%**.
- T-3 candidates: none.

---

# §B.2 — Fairness and Equity

---

## §B.2.0 — Safeguards against algorithmic discrimination; bias-testing + adjustment

```yaml
# Lines 483–488 — Fairness/Equity opening paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        "Deployers should have safeguards in place to ensure that algorithmic decisions
        do not further exacerbate or amplify existing discriminatory or unjust impacts
        across different demographics and the design, development, and deployment of AI
        systems should not result in unfair biasness or discrimination." Hard constraint
        per the federation's DISCRIMINATION prohibition class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.2 lines 483–486"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:human_oversight_governance"
      score: 1.0
      confidence: 0.85
      context: >
        "An example of such safeguards would include human interventions and checks on
        the algorithms and its outputs." Human-oversight composition with the
        discrimination prohibition — fidelity-to-mandate machinery realised as
        review-and-correct.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.2 lines 486–487"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:bias_testing_and_rectification"
      score: 1.0
      confidence: 0.85
      context: >
        "Deployers of AI systems should conduct regular testing of such systems to
        confirm if there is bias and where bias is confirmed, make the necessary
        adjustments to rectify imbalances to ensure equity." Method-level operational
        commitment; Family B method:* under a deployer-defined Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.2 lines 487–488"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  "Equity" is rolled into the discrimination-prohibition + bias-rectification method
  composition. The standalone positive content of "equity" (substantive distributive
  justice beyond non-discrimination) is partially carried by detection:distributive:* in
  §B.2.1 below but does not have a dedicated envelope here.
```

---

## §B.2.1 — Examples of high-impact decisions + diverse representative training data

```yaml
# Lines 490–506 — Fairness/Equity bias-mitigation paragraph (with examples)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:high_impact_decision_caution"
      score: 1.0
      confidence: 0.85
      context: >
        Examples cited: "AI systems are currently used to screen resumes in job
        application processes, predict the credit worthiness of consumers and provide
        agronomic advice to farmers. If not properly managed, an AI system's outputs
        used to make decisions with significant impact on individuals could perpetuate
        existing discriminatory or unjust impacts to specific demographics."
        High-impact-decision caution layered on the discrimination prohibition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.2 lines 490–494"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:diverse_representative_training_data"
      score: 1.0
      confidence: 0.90
      context: >
        "The datasets used to train the AI systems should be diverse and representative.
        Appropriate measures should be taken to mitigate potential biases during data
        collection and pre-processing, training, and inference." Data-governance
        composition: representative-by-design + bias-mitigation-by-pipeline. Cousin to
        EU HLEG §1.3.b "Quality and integrity of data."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.2 lines 494–497"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:distributive:access:agent_capabilities"
      score: 0.0
      confidence: 0.75
      context: >
        Education-sector example: training/test dataset "should be adequately
        representative of the student population by including students of different
        genders and ethnicities." Distributive-access detection across the cohort — the
        AI's outputs (and thus its access-distribution) should not preferentially
        exclude. LensCore detection family; score 0.0 placeholder.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §B.2 lines 505–506"
        - "ratchet_calibration_version:distributive_access_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore: detection:distributive:access:*)"
verdict: composed
nuance_lost: |
  The specific example sectors (resume screening, credit worthiness, agronomic advice,
  education) are illustrative T-2 framing. The implicit weighting between sectors
  (credit is high-impact, agronomic advice less so) is not captured by the wire format;
  the consumer must compose with deployment_profile.deployment_domain to recover it.
```

**§B.2 Fairness and Equity — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `prohibited:discrimination` (hard constraint, central anchor), `fidelity:human_oversight_governance`, `non_maleficence:high_impact_decision_caution`, `integrity:diverse_representative_training_data`; **Family B ACTION** — `method:bias_testing_and_rectification`; **Family C DETECTION** — `detection:distributive:access:agent_capabilities`.
- Coverage: 2 substantive paragraphs (§B.2.0–§B.2.1). 2/2 clean+composed = **100%**.
- T-3 candidates: none.

---

# §B.3 — Security and Safety

---

## §B.3.0 — Opening: AI systems should be safe + sufficiently secure

```yaml
# Line 512 — One-sentence opener
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:safe_and_secure_baseline"
      score: 1.0
      confidence: 0.95
      context: >
        "AI systems should be safe and sufficiently secure against malicious attacks."
        Foundational claim composing non_maleficence (safety) + key_boundary (security)
        for the rest of §B.3.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 line 512"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
nuance_lost: |
  None of significance — the one-sentence framing is faithfully carried as a
  constitutional-mutability composition anchor for the paragraphs below.
```

---

## §B.3.1 — Safety: risk assessment + human intervention + safe disengagement

```yaml
# Lines 514–525 — Safety paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:risk_assessment_and_mitigation"
      score: 1.0
      confidence: 0.95
      context: >
        "Safety refers to ensuring the safety of developers, deployers, and users of AI
        systems by conducting impact or risk assessments and ensuring that known risks
        have been identified and mitigated. A risk prevention approach should be adopted,
        and precautions should be put in place." Maps directly to non_maleficence +
        preventative-risk discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 514–517"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:human_oversight_governance"
      score: 1.0
      confidence: 0.90
      context: >
        "Precautions should be put in place so that humans can intervene to prevent
        harm, or the system can safely disengage itself in the event an AI system makes
        unsafe decisions — autonomous vehicles that cause injury to pedestrians are an
        illustration of this." HITL/HOTL composition with safe-disengagement fallback.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 516–518"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:fallback:resume_manual_control"
      score: 1.0
      confidence: 0.85
      context: >
        "In AI-enabled autonomous vehicles, developers and deployers should put in place
        mechanisms for the human driver to easily resume manual driving whenever they
        wish." Concrete operational method instantiating the safe-disengagement claim.
        Family B method:* under a deployment-domain-specific Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 524–525"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:risk_limitations_safeguards_disclosure"
      score: 1.0
      confidence: 0.85
      context: >
        "The risks, limitations, and safeguards of the use of AI should be made known to
        the user." User-facing disclosure of safety envelope — composes with §B.1
        transparency machinery.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 523–524"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  "Utmost priority in the decision-making process" framing (line 520) is a
  prioritisation hint not separately attested — the constitutional mutability on the
  non_maleficence anchor partly carries it. The pedestrian-injury vehicle example is
  cautionary T-2 illustration; not attested as a separate prohibition.
```

---

## §B.3.2 — Security: cyber attacks specific to AI (data poisoning, model inversion, byzantine)

```yaml
# Lines 527–548 — Security paragraph + secondary checklist (BCP/DRP/zero-day/IoT)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:adversarial_robustness"
      score: 1.0
      confidence: 0.90
      context: >
        "Security refers to ensuring the cybersecurity of AI systems, which includes
        mechanisms against malicious attacks specific to AI such as data poisoning,
        model inversion, the tampering of datasets, byzantine attacks in federated
        learning, as well as other attacks designed to reverse engineer personal data
        used to train the AI." Direct match to CIRISEdge key_boundary:* family +
        CYBER_OFFENSIVE prohibition class (defensive posture).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 527–530 + footnote 5 (byzantine attack)"
        - "ContributionRef(source_material/prohibitions.py::CYBER_OFFENSIVE)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:auth_encryption_patching_access_mgmt"
      score: 1.0
      confidence: 0.85
      context: >
        "Technical security measures like robust authentication mechanisms and
        encryption... ensuring regular software updates to AI systems and proper access
        management for critical or sensitive systems." Method-level cyber-hygiene
        commitments composing under a deployer Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 530–534"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:incident_response_security_testing"
      score: 1.0
      confidence: 0.85
      context: >
        "Deployers should also develop incident response plans... a minimum list of
        security testing (e.g. vulnerability assessment and penetration testing) and
        other applicable security testing tools. Some other important considerations
        also include: a. Business continuity plan; b. Disaster recovery plan; c.
        Zero-day attacks; d. IoT devices." Composed method commitments + secondary
        risk-domain checklist.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.3 lines 534–548"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  The (a)-(d) sub-list (BCP / DRP / zero-day / IoT) is enumerated without elaboration —
  the envelope rolls them up under method:incident_response_security_testing but the
  consumer cannot recover the four-fold distinction without reading context. A separate
  method:* per item would be precise but cluttered; the rollup is the honest level.
```

**§B.3 Security and Safety — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `non_maleficence:*` (central anchor — safe_and_secure_baseline + risk_assessment_and_mitigation), `fidelity:human_oversight_governance`, `key_boundary:adversarial_robustness` (CIRISEdge), `transparency_log:risk_limitations_safeguards_disclosure`; **Family B ACTION** — `method:fallback:resume_manual_control`, `method:auth_encryption_patching_access_mgmt`, `method:incident_response_security_testing`.
- Coverage: 3 substantive paragraphs (§B.3.0–§B.3.2). 3/3 clean+composed = **100%**.
- T-3 candidates: none.

---

# §B.4 — Human-centricity

---

## §B.4.0 — Opening: respect human-centred values + pursue benefits for human society

```yaml
# Lines 565–566 — Human-centricity opener
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:human_centred_values_pursuit"
      score: 1.0
      confidence: 0.90
      context: >
        "AI systems should respect human-centred values and pursue benefits for human
        society, including human beings' well-being, nutrition, happiness, etc." Maps
        directly to the CIRIS beneficence principle (FSD-002 §3.1 Accord-principles).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 565–566"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I beneficence)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
verdict: clean
nuance_lost: |
  The enumeration "well-being, nutrition, happiness, etc." is unusually concrete for an
  abstract opener — gestures at material wellbeing in a way EU HLEG §1.6 (Societal &
  environmental wellbeing) and IEEE EAD Principle 2 (Well-being) extend. ASEAN's "etc."
  is a deliberate non-closure; the wire format cannot capture that open-endedness
  without additional witness composition.
```

---

## §B.4.1 — Benefit + protect from harms; particular care for vulnerable individuals

```yaml
# Lines 568–572 — Benefit-and-protect paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:benefit_for_all"
      score: 1.0
      confidence: 0.85
      context: >
        "It is key to ensure that people benefit from AI design, development, and
        deployment while being protected from potential harms. AI systems should be used
        to promote human well-being and ensure benefit for all." Inclusion-of-all
        framing of the beneficence principle.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 568–569"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:no_exploitation_of_vulnerable"
      score: -1.0
      confidence: 1.0
      context: >
        "Especially in instances where AI systems are used to make decisions about
        humans or aid them, it is imperative that these systems are designed with human
        benefit in mind and do not take advantage of vulnerable individuals." Hard
        constraint on exploitation of vulnerable populations; composes with the
        federation's §6.1.4 lexical-vulnerability-priority policy.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 570–572"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  "Vulnerable individuals" is left undefined — the wire format anchors the
  vulnerability-priority via FSD-002 §6.1.4 (lexical-vulnerability-priority), which the
  composing consumer reads at evaluation time. Per-cohort vulnerability tagging would
  require additional cohort:* composition not present in the source paragraph.
```

---

## §B.4.2 — Lifecycle integration + user testing with varied backgrounds

```yaml
# Lines 574–578 — Lifecycle paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:human_centricity_lifecycle_integration"
      score: 1.0
      confidence: 0.85
      context: >
        "Human-centricity should be incorporated throughout the AI system lifecycle,
        starting from the design to development and deployment. Actions must be taken
        to understand the way users interact with the AI system, how it is perceived,
        and if there are any negative outcomes arising from its outputs."
        Lifecycle-wide commitment plus user-perception feedback obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 574–576"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:user_testing_varied_backgrounds"
      score: 1.0
      confidence: 0.85
      context: >
        "One example of how deployers can do this is to test the AI system with a small
        group of internal users from varied backgrounds and demographics and incorporate
        their feedback in the AI system." Direct match to witness_diversity:* primitive
        — multi-stakeholder consultation aggregation for feedback.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 576–578"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: composed
nuance_lost: |
  "Small group of internal users" qualifier is operational scope-narrowing — testing
  with internal proxies rather than affected external populations. Witness diversity
  with an internal-only pool partly captures it; some semantic strength loss because
  the prefix does not distinguish internal-proxy from external-affected witnesses.
```

---

## §B.4.3 — Dark patterns prohibition + no-manipulation hard constraint

```yaml
# Lines 580–585 — Dark patterns paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        "AI systems should not be used for malicious purposes or to sway or deceive
        users into making decisions that are not beneficial to them or society. In this
        regard, developers and deployers... should also ensure that dark patterns are
        avoided. Dark patterns refer to the use of certain design techniques to
        manipulate users and trick them into making decisions that they would otherwise
        not have made." Hard constraint per the federation's MANIPULATION_COERCION
        prohibition class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 580–584"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:deceptive_default_options"
      score: -1.0
      confidence: 0.95
      context: >
        "An example of a dark pattern is employing the use of default options that do
        not consider the end user's interests, such as for data sharing and tracking of
        the user's other online activities." Specific exemplar of MANIPULATION_COERCION
        — adversarial defaults against user interest. Composes with PRIVACY_VIOLATION
        when the manipulated dimension is data-sharing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 584–585"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
nuance_lost: |
  "Dark patterns" is a substantive concept-name from UX-ethics literature. The
  prohibition envelope captures the structural commitment but not the specific design-
  pattern taxonomy (which has its own literature — Brignull, Gray et al.). The taxonomy
  belongs at deployment-context composition, not in the wire envelope.
```

---

## §B.4.4 — Labour impact assessment + job redesign (citing Singapore PDPC guide)

```yaml
# Lines 587–593 — Labour impact paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:labour_displacement_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        "As an extension of human-centricity as a principle, it is also important to
        ensure that the adoption of AI systems and their deployment at scale do not
        unduly disrupt labour and job prospects without proper assessment. Deployers are
        encouraged to take up impact assessments... consider how jobs can be redesigned
        to incorporate use of AI." Matches LANGUAGE_PRIMER §11.14 closed-by-documentation
        pattern: non_maleficence:* composed with cohort-specific target_key_id (here at
        species/community scope rather than per-individual).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 587–593"
        - "Footnote 6 (PDPC Singapore Job Redesign Guide 2020)"
        - "LANGUAGE_PRIMER §11.14 (labor:individual_loss closed by composition)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:stakeholder_impact_assessment"
      score: 1.0
      confidence: 0.80
      context: >
        "Take up impact assessments to ensure a systematic and stakeholder-based review."
        Stakeholder-based-review requirement composing onto witness_diversity:* for
        multi-party consultation in the labour-impact assessment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.4 lines 589–590"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: composed
nuance_lost: |
  "Encouraged to take up impact assessments" is voluntary-modal language — softer than
  EU HLEG §1.1.a "should be undertaken." The score 1.0 carries the structural direction
  but not the hortative-vs-obligatory differential. The "higher-value tasks" framing in
  the PDPC reference (line 593) is aspirational; not separately attested. Notably,
  individual-worker testimonial (testimonial_witness:displaced_worker per v1.4) is NOT
  invoked in this paragraph — the source is community-scope assessment-language, not
  individual-narrative-language. The per-individual closure pattern remains available
  at deployment composition.
```

**§B.4 Human-centricity — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `beneficence:*` (central anchor — human_centred_values_pursuit + benefit_for_all), `non_maleficence:*` (no_exploitation_of_vulnerable + labour_displacement_assessment), `integrity:human_centricity_lifecycle_integration`, `prohibited:manipulation_coercion` + `prohibited:deceptive_default_options` (hard constraints); **Family D CONSENSUS** — `witness_diversity:user_testing_varied_backgrounds`, `witness_diversity:stakeholder_impact_assessment`.
- Coverage: 5 substantive paragraphs (§B.4.0–§B.4.4). 5/5 clean+composed = **100%**.
- T-3 candidates: none.

---

# §B.5 — Privacy and Data Governance

---

## §B.5.0 — Opening: data privacy + protection + quality + integrity + access protocols

```yaml
# Lines 600–602 — Privacy/Data Governance opener
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:privacy_as_fundamental_right"
      score: 1.0
      confidence: 0.95
      context: >
        "AI systems should have proper mechanisms in place to ensure data privacy and
        protection and maintain and protect the quality and integrity of data throughout
        their entire lifecycle. Data protocols need to be set up to govern who can
        access data and when data can be accessed." Lifecycle-wide privacy + data-
        governance + access-protocol composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 600–602"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
nuance_lost: |
  The composite nature of the opener (privacy + quality + integrity + access protocols)
  is rolled into one anchor envelope; the sub-claims are detailed in §B.5.1–§B.5.4.
  No semantic loss because the sub-paragraphs carry the detail.
```

---

## §B.5.1 — Compliance with applicable laws + named ASEAN data-protection statutes

```yaml
# Lines 604–624 — Compliance paragraph (with statute enumeration)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:data_protection_legal_compliance"
      score: 1.0
      confidence: 0.95
      context: >
        "Data privacy and protection should be respected and upheld during the design,
        development, and deployment of AI systems. The way data is collected, stored,
        generated, and deleted throughout the AI system lifecycle must comply with
        applicable data protection laws, data governance legislation, and ethical
        principles." Named ASEAN statutes: Malaysia PDPA 2010, Philippines DPA 2012,
        Singapore PDPA 2012, Thailand PDPA 2019, Indonesia PDP Law 2022, Vietnam PDP
        Decree 2023.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 604–624"
      cohort_scope: affiliations
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: clean
nuance_lost: |
  Statute-list (Malaysia PDPA 2010 ... Vietnam PDP Decree 2023) is jurisdictionally
  resolved; the cohort_scope: affiliations + the regional composition machinery in
  GOVERNANCE_FABRIC_MAPPING_STANDARD §6 carries it. Per-statute attestations could be
  emitted at deployment composition time if needed, but the rollup at the principle
  layer is the honest level.
```

---

## §B.5.2 — Transparency + consent + minimisation (no unnecessary data)

```yaml
# Lines 626–630 — Consent + minimisation paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:data_practices_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        "Organisations should be transparent about their data collection practices,
        including the types of data collected, how it is used, and who has access to
        it." Direct match to CIRISVerify transparency_log:* family — data-practices
        disclosure composing with consent management.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 626–627"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:informed_consent_for_data"
      score: 1.0
      confidence: 0.95
      context: >
        "Organisations should ensure that necessary consent is obtained from individuals
        before collecting, using, or disclosing personal data for AI development and
        deployment, or otherwise have appropriate legal basis to collect, use or disclose
        personal data without consent." Autonomy via informed-consent composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 627–630"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:data_minimisation"
      score: 1.0
      confidence: 0.90
      context: >
        "Unnecessary or irrelevant data should not be gathered to prevent potential
        misuse." Data-minimisation principle as harm-prevention. Direct alignment with
        GDPR-style minimisation discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 line 630"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  "Appropriate legal basis... without consent" carve-out (lines 628–629) is a real
  qualifier — consent is the default but lawful processing without consent is
  acknowledged. The envelope captures consent as default via score 1.0 on
  autonomy:informed_consent_for_data; the alternative-legal-basis allowance is
  carried by composition with fidelity:data_protection_legal_compliance from §B.5.1.
```

---

## §B.5.3 — Data protection governance frameworks + DPIA + their limitations as AI risk assessment

```yaml
# Lines 632–639 — Governance frameworks paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:dpia_impact_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        "Data protection impact assessments (DPIA) help organisations determine how
        data processing systems, procedures, or technologies affect individuals' privacy
        and eliminate risks that might violate compliance." Method-level operational
        commitment under a deployer Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 634–636 + footnote 7"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:dpia_insufficient_as_ai_risk_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        "However, it is important to note that DPIAs are much narrower in scope than an
        overall impact assessment for use of AI systems and are not sufficient as an AI
        risk assessment. Other components will need to be considered for a full
        assessment of risks associated with AI systems." Scope-honesty claim:
        privacy-impact-assessment ≠ AI-risk-assessment. Anti-checkbox discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 636–639"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  The "periodically reviewed and updated" framework-evolution language (line 633) is
  carried implicitly by mutability: amendable. The DPIA-insufficiency claim is one of
  the document's sharper analytical moments — privacy-impact-assessment is named as
  a useful but partial tool — and the integrity:* anchor preserves the structural
  shape; rhetorical force is partially lost.
```

---

## §B.5.4 — Privacy-by-design + privacy-enhancing technologies (differential privacy, ZKP)

```yaml
# Lines 641–649 — Privacy-by-design paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:privacy_by_design"
      score: 1.0
      confidence: 0.90
      context: >
        "Developers and deployers of AI systems should also incorporate a privacy-by-
        design principle when developing and deploying AI systems. Privacy-by-design is
        an approach that embeds privacy in every stage of the system development
        lifecycle." Lifecycle-wide privacy commitment composed under integrity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 641–644"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:privacy_enhancing_technologies"
      score: 1.0
      confidence: 0.85
      context: >
        "Investing in privacy enhancing technologies to preserve privacy while allowing
        personal data to be used for innovation. Privacy enhancing technologies include,
        but are not limited to, differential privacy... and zero-knowledge proofs (ZKP)."
        Method-level commitment to PETs as concrete operational substrate. Family B
        method:* under a deployer Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.5 lines 644–649 + footnote 8 (OECD PETs 2023)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  Differential-privacy / ZKP enumeration is illustrative and non-exhaustive ("include,
  but are not limited to"). The method:* envelope captures the structural commitment to
  PETs; specific-technique selection belongs at deployment composition. The
  "investment" framing implies resource-allocation commitments not separately attested.
```

**§B.5 Privacy and Data Governance — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `non_maleficence:*` (central anchor — privacy_as_fundamental_right + data_minimisation), `fidelity:data_protection_legal_compliance`, `autonomy:informed_consent_for_data`, `transparency_log:data_practices_disclosure`, `integrity:*` (privacy_by_design + dpia_insufficient_as_ai_risk_assessment); **Family B ACTION** — `method:dpia_impact_assessment`, `method:privacy_enhancing_technologies`.
- Coverage: 5 substantive paragraphs (§B.5.0–§B.5.4). 5/5 clean+composed = **100%**.
- T-3 candidates: none.

---

# §B.6 — Accountability and Integrity

---

## §B.6.0 — Opening: human accountability + control; deployer + AI-actor integrity

```yaml
# Lines 656–659 — Accountability/Integrity opener (with footnote 9 defining AI actors)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:human_accountability_and_control"
      score: 1.0
      confidence: 0.95
      context: >
        "There needs to be human accountability and control in the design, development,
        and deployment of AI systems. Deployers should be accountable for decisions made
        by AI systems and for the compliance with applicable laws and respect for AI
        ethics and principles." Human-in-command framing at the deployer level. AI
        actors (footnote 9) = any actor in the lifecycle, natural or legal persons.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.6 lines 656–659 + footnote 9"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:ai_actors_lifecycle_integrity"
      score: 1.0
      confidence: 0.90
      context: >
        "AI actors should act with integrity throughout the AI system lifecycle when
        designing, developing, and deploying AI systems." Composing integrity as a
        principle binding on every AI actor at every lifecycle stage.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.6 lines 658–659 + footnote 9"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  The footnote 9 definition ("AI actors can be defined as any actor involved in at
  least one stage of the AI system life cycle... natural and legal persons, such as
  researchers, programmers, engineers, data scientists, end-users, business
  enterprises, universities and public and private entities") is rolled into
  cohort_scope: species + the implicit universality of the fidelity / integrity claims.
  Per-actor-type attestations not emitted; the wire format does not encode
  natural-vs-legal-person distinctions at the prefix level.
```

---

## §B.6.1 — Deployer functioning + integrity in malfunction-response

```yaml
# Lines 661–664 — Functioning + malfunction-response paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:deployer_proper_functioning_obligation"
      score: 1.0
      confidence: 0.90
      context: >
        "Deployers of AI systems should ensure the proper functioning of AI systems and
        its compliance with applicable laws, internal AI governance policies and ethical
        principles." Mandate-fidelity composed with legal + governance-policy + ethical-
        principle compliance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.6 lines 661–662"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:malfunction_mitigation_with_integrity"
      score: 1.0
      confidence: 0.85
      context: >
        "In the event of a malfunction or misuse of the AI system that results in
        negative outcomes, responsible individuals should act with integrity and
        implement mitigating actions to prevent similar incidents from happening in the
        future." Integrity-binds-recovery commitment; composes with the federation's
        Correction family (E) for handling adverse events.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.6 lines 662–664"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  "Responsible individuals" is named without specifying — who is responsible varies by
  organisational role and is left to internal-governance structure (§C.1 in the
  document). Per-role attestations belong at deployment composition.
  "Prevent similar incidents from happening in the future" is forward-looking
  commitment; the wire format does not carry a per-incident learning trajectory
  unless composed with subsequent moderation/reconsideration attestations.
```

---

## §B.6.2 — Clear reporting structures + error/unethical-outcome documentation

```yaml
# Lines 685–689 — Reporting structures + error documentation paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:internal_governance_structure"
      score: 1.0
      confidence: 0.85
      context: >
        "To facilitate the allocation of responsibilities, organisations should adopt
        clear reporting structures for internal governance, setting out clearly the
        different kinds of roles and responsibilities for those involved in the AI
        system lifecycle." Internal-governance documentation as transparency-log
        inclusion. Sets up §C.1 (Internal Governance Structures) in the framework.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.6 lines 685–687"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:error_documentation_and_correction"
      score: 1.0
      confidence: 0.85
      context: >
        "AI systems should also be designed, developed, and deployed with integrity —
        any errors or unethical outcomes should at minimum be documented and corrected
        to prevent harm to users upon deployment." Documentation + correction commitment
        composing transparency_log:* with the framework's audit-chain + correction
        machinery.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.6 lines 687–689"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The "at minimum" qualifier in line 688 signals that documentation + correction is the
  floor, not the ceiling — additional remedies (compensation, restitution, public
  acknowledgement) are implicit. The envelope captures the floor; the ceiling lives at
  deployment-context composition with the Correction family (moderation:* /
  reconsideration:*).
```

**§B.6 Accountability and Integrity — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `fidelity:*` (central anchor — human_accountability_and_control + deployer_proper_functioning_obligation), `integrity:*` (ai_actors_lifecycle_integrity + malfunction_mitigation_with_integrity), `transparency_log:*` (internal_governance_structure + error_documentation_and_correction).
- Coverage: 3 substantive paragraphs (§B.6.0–§B.6.2). 3/3 clean+composed = **100%**.
- T-3 candidates: none.

---

# §B.7 — Robustness and Reliability

---

## §B.7.0 — Opening: cope with errors + erroneous input + stress + consistent performance

```yaml
# Lines 695–697 — Robustness/Reliability opener
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:robustness_under_stress"
      score: 1.0
      confidence: 0.95
      context: >
        "AI systems should be sufficiently robust to cope with errors during execution
        and unexpected or erroneous input, or cope with stressful environmental
        conditions. It should also perform consistently. AI systems should, where
        possible, work reliably and have consistent results for a range of inputs and
        situations." Composing non_maleficence (robustness-prevents-harm) + integrity
        (consistent performance) at the principle layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 695–697"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:reliability_consistent_results"
      score: 1.0
      confidence: 0.90
      context: >
        Reliability as integrity-of-output: "work reliably and have consistent results
        for a range of inputs and situations." Cousin of EU HLEG §1.2.d Reliability &
        Reproducibility.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 696–697"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  "Where possible" hedge (line 696) signals that absolute reliability is unattainable
  in some domains; this hedge is not separately encoded but is partly carried by
  confidence: 0.90 on the integrity envelope. The "stress" framing is shared with
  the IEEE EAD Principle of Effectiveness; this comparative depth surfaces at Phase 3.
```

---

## §B.7.1 — Real-world dynamic conditions; resilience + access control + harm-mitigation

```yaml
# Lines 699–703 — Dynamic-conditions resilience paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:resilient_to_unexpected_inputs"
      score: 1.0
      confidence: 0.90
      context: >
        "AI systems may have to operate in real-world, dynamic conditions where input
        signals and conditions change quickly. To prevent harm, AI systems need to be
        resilient to unexpected data inputs, not exhibit dangerous behaviour, and
        continue to perform according to the intended purpose." Resilience-as-harm-
        prevention composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 699–701"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:not_infallible_acknowledgement"
      score: 1.0
      confidence: 0.85
      context: >
        "Notably, AI systems are not infallible and deployers should ensure proper
        access control and protection of critical or sensitive systems and take actions
        to prevent or mitigate negative outcomes that occur due to unreliable
        performances." Honest acknowledgement of fallibility composing with operational
        risk-management.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 701–703"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:access_protocols_critical_sensitive_systems"
      score: 1.0
      confidence: 0.85
      context: >
        "Deployers should ensure proper access control and protection of critical or
        sensitive systems." Direct match to CIRISEdge key_boundary:* family for
        substrate-level access control on critical assets.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 702–703"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
verdict: composed
nuance_lost: |
  "Not infallible" acknowledgment is an integrity-as-honesty about model capability —
  cousins to EU HLEG §1.2.c's accuracy-with-uncertainty-disclosure but more direct.
  The conscience:epistemic_humility composition is implicit rather than emitted; if
  separately attested, would belong as a fourth Contribution here. Left to deployment
  composition.
```

---

## §B.7.2 — Rigorous pre-deployment testing + data documentation + lineage

```yaml
# Lines 705–707 — Testing + documentation paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:pre_deployment_robustness_testing"
      score: 1.0
      confidence: 0.90
      context: >
        "Deployers should conduct rigorous testing before deployment to ensure
        robustness and consistent results across a range of situations and environments."
        Method-level operational commitment under a deployer Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 705–706"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "asean-guide-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:data_lineage_for_troubleshooting"
      score: 1.0
      confidence: 0.85
      context: >
        "Measures such as proper documentation of data sources, tracking of data
        processing steps, and data lineage can help with troubleshooting AI systems."
        Maps to CIRISVerify transparency_log:* + CIRISPersist audit_chain:* composition;
        cousin of EU HLEG §1.3.b data-lifecycle documentation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §B.7 lines 706–707"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The "where possible" hedge from §B.7.0 carries through: rigorous testing is hortative
  ("should conduct"), not absolute. The mutability: amendable on method:* carries the
  policy-revision allowance. No T-3 candidates here.
```

**§B.7 Robustness and Reliability — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `non_maleficence:*` (central anchor — robustness_under_stress + resilient_to_unexpected_inputs), `integrity:*` (reliability_consistent_results + not_infallible_acknowledgement), `key_boundary:access_protocols_critical_sensitive_systems` (CIRISEdge), `transparency_log:data_lineage_for_troubleshooting`; **Family B ACTION** — `method:pre_deployment_robustness_testing`.
- Coverage: 3 substantive paragraphs (§B.7.0–§B.7.2). 3/3 clean+composed = **100%**.
- T-3 candidates: none.

---

# Section-level summary + cross-document framing

---

## Verdict distribution (full A + B range)

| Section | Atomic units | clean | composed | partial | not-translated |
|---|---|---|---|---|---|
| §A.0 (headers) | 1 | 0 | 0 | 0 | 1 (T-2) |
| §A.intro | 1 | 0 | 1 | 0 | 0 |
| §A.adm | 1 | 0 | 1 | 0 | 0 |
| §A.aim | 1 | 1 | 0 | 0 | 0 |
| §A.1 Objectives | 1 | 0 | 1 | 0 | 0 |
| §A.2 Assumptions | 1 | 0 | 1 | 0 | 0 |
| §A.3 Target Audience | 1 | 0 | 0 | 0 | 1 (T-2) |
| §A.4 Definitions | 1 | 0 | 0 | 0 | 1 (T-2) |
| §B.intro | 1 | 1 | 0 | 0 | 0 |
| §B.1 Transparency/Explainability | 7 | 4 | 3 | 0 | 0 |
| §B.2 Fairness/Equity | 2 | 0 | 2 | 0 | 0 |
| §B.3 Security/Safety | 3 | 1 | 2 | 0 | 0 |
| §B.4 Human-centricity | 5 | 1 | 4 | 0 | 0 |
| §B.5 Privacy/Data Governance | 5 | 2 | 3 | 0 | 0 |
| §B.6 Accountability/Integrity | 3 | 0 | 3 | 0 | 0 |
| §B.7 Robustness/Reliability | 3 | 0 | 3 | 0 | 0 |
| **TOTAL** | **37** | **10** | **24** | **0** | **3** |

- Clean: 10 / 37 = **27%**
- Composed: 24 / 37 = **65%**
- Clean+Composed: 34 / 37 = **92%**
- Partial: 0 / 37 = **0%**
- Not-translated (all T-2 PASTORAL_PROSE): 3 / 37 = **8%**
- Not-translated (T-1 TRADITION_AUTHORITY): 0 / 37 = **0%** (expected — secular regional document)
- Not-translated (T-3 EXPRESSIVE_GAP): 0 / 37 = **0%**

---

## Per-principle coverage table

| Principle | Atomic units | Clean+Composed | Coverage | T-3 candidates | Primary CIRIS family/families |
|---|---|---|---|---|---|
| §B.1 Transparency/Explainability | 7 | 7 | 100% | 0 | `transparency_log:*` (CIRISVerify) + `integrity:*` + `autonomy:*` |
| §B.2 Fairness/Equity | 2 | 2 | 100% | 0 | `prohibited:discrimination` + `non_maleficence:*` + `method:bias_testing` |
| §B.3 Security/Safety | 3 | 3 | 100% | 0 | `non_maleficence:*` + `key_boundary:*` (CIRISEdge) + `method:*` |
| §B.4 Human-centricity | 5 | 5 | 100% | 0 | `beneficence:*` + `non_maleficence:*` + `prohibited:manipulation_coercion` + `witness_diversity:*` |
| §B.5 Privacy/Data Governance | 5 | 5 | 100% | 0 | `non_maleficence:privacy_as_fundamental_right` + `autonomy:informed_consent` + `transparency_log:*` + `method:*` |
| §B.6 Accountability/Integrity | 3 | 3 | 100% | 0 | `fidelity:*` + `integrity:*` + `transparency_log:*` |
| §B.7 Robustness/Reliability | 3 | 3 | 100% | 0 | `non_maleficence:*` + `integrity:*` + `key_boundary:*` + `method:*` |

---

## T-3 candidates

**None.**

All 7 principles map cleanly via composition with existing FSD-002 v1.4 prefix families. No new prefixes proposed. Composition-before-extension (METHODOLOGY.md §8.5.2) was honoured throughout: where a candidate gap was tempting, the closure pattern came through composition (e.g., labour-displacement closure per LANGUAGE_PRIMER §11.14; vulnerability-priority via §6.1.4 reference; discrimination detection via composed `detection:correlated_action:participation_exclusion:*`).

This is consistent with the manifest's prior assessment ("minimal T-3") and with the post-MH primer-stability claim — the wire format absorbs the ASEAN 7-principle structure without strain. Compared to IEEE EAD (which is expected to surface an `affective:*` T-3 in CH05), ASEAN's principle set is intentionally narrower and operationally framed, sitting fully inside the existing prefix space.

---

## Calibration paragraph (humble posture)

This translation captured **structural shape, not lossless transcription**. The 37 atomic units (7 §A units + 1 §B.intro + 29 §B.1–§B.7 paragraphs) emitted ~74 Contribution envelopes across 6 of 80 v1.4 prefix families (`transparency_log:*`, `integrity:*`, `autonomy:*`, `non_maleficence:*`, `fidelity:*`, `beneficence:*`, plus structural `prohibited:*`, `key_boundary:*`, `method:*`, `goal:*`, `locality:decision:*`, `witness_diversity:*`, `detection:correlated_action:*`, `detection:distributive:access:*`, `multilateral_participation:*`). What survives cleanly: the operational backbone of every principle — disclosure obligations, risk-assessment commitments, prohibition hard-constraints, access-control protocols, lifecycle integrity. What is lost or carried only partly is named explicitly on each unit's `nuance_lost:` line: hortative-vs-obligatory force differences, jurisdictional precision below the regional layer, taxonomic distinctions (dark-pattern subtypes, AI-actor sub-classes), enumerative scaffolding (the (a)-(d) BCP/DRP/zero-day/IoT list, the data-protection statute roll), and rhetorical framing about "trust" as relational versus aggregate good. The framework's wire format does what it is for — captures the structural commitments computably and surfaces the residual to the consumer — and the residual is correctly small for a secular, operationally-framed regional document. The translation is humble: it does not claim ASEAN's full normative depth, only the portion the wire format can carry without distortion. Cross-document overlap with EU HLEG Chapter II §1 and IEEE EAD Chapter "General Principles" is now structurally computable; the load-bearing Phase 3 comparison axis is enabled.

**End CONTRIBUTION_OBJECTS_ASEAN_AB_INTRO_PRINCIPLES.md**
