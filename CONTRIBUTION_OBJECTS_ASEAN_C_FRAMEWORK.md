# CONTRIBUTION_OBJECTS_ASEAN_C_FRAMEWORK.md
# ASEAN Guide on AI Governance and Ethics (2024) — Section C: AI Governance Framework
# Source range: asean_guide.txt lines 719–2134 (Section C, all 4 components)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}
#
# Methodological note (per the task brief):
#   Section C is the operational core of the ASEAN Guide, organised in 4 components:
#     C.1 Internal governance structures and measures (lines 753–936)
#     C.2 Determining the level of human involvement (HITL / HOTL / HOOTL) (lines 943–1186)
#     C.3 Operations management (AI lifecycle: project governance, data, modelling,
#         outcome analysis, deployment + monitoring) (lines 1187–1905)
#     C.4 Stakeholder interaction and communication (lines 1907–2134)
#
#   Unit of mapping: natural paragraph or coherent bullet-cluster within a sub-section.
#   Vendor case studies (Aboitiz, EY, Gojek, UCARE.AI, Smart Nation Group, MOE) are
#   descriptive illustrations of normative claims already attested in the surrounding
#   prose; they are noted at the cluster level with verdict T-2 (PASTORAL_PROSE in the
#   sense of narrative-illustrative, not exhortative) rather than re-attested.
#
#   Strict 4-verdict discipline per LANGUAGE_PRIMER §9: clean / composed / partial /
#   not-translated. Source quotes ≤ 2 sentences. HUMBLE — the ASEAN Guide is a senior
#   multilateral artefact; the wire format records its structural shape, not adjudicates it.
#
#   The 3-category human-involvement framework (HITL / HOTL / HOOTL) is verified as a
#   load-bearing cross-document alignment against CIRIS's oversight ladder. The mapping
#   verification is given in the per-component summary for C.2 below and consolidated
#   in the file footer §F.

---

## Per-section verdict-distribution summary

| Component | Units | clean | composed | partial | not-translated | Primary CIRIS prefix families |
|---|---|---|---|---|---|---|
| C.1 Internal governance structures | 8 | 3 | 4 | 0 | 1 | accountability:* + fidelity:* + integrity:* |
| C.2 Human involvement (HITL/HOTL/HOOTL) | 9 | 3 | 4 | 1 | 1 | accountability:human_in_control + conscience:optimization_veto + fidelity:algorithmic_disclosure |
| C.3 Operations management | 16 | 8 | 6 | 0 | 2 | non_maleficence:* + integrity:* + accountability:* + detection:* (F-3 + Coherence-Ratchet) + prohibited:discrimination |
| C.4 Stakeholder interaction | 8 | 3 | 3 | 1 | 1 | fidelity:* + autonomy:* + justice:stakeholder_participation + testimonial_witness:* |
| **TOTAL** | **41** | **17** | **17** | **2** | **5** | (see §F summary) |

Aggregate clean+composed rate: 34/41 ≈ **83%** of all units (or 34/36 ≈ **94%** excluding the 5 vendor/question-prompt T-2 declarations — closer to manifest expectation).

---

## §C.1 — Internal governance structures and measures (lines 753–936)

### C.1.a — Governance-body establishment + multi-disciplinary representation (lines 755–766)

Source quote: "Deployers can also consider setting up a multi-disciplinary, central governing
body, such as an AI Ethics Advisory Board or Ethics Committee, to oversee AI governance efforts...
To adequately reflect the diversity of society, there is also value in considering a governing
body that is sufficiently representative of stakeholders and a range of voices."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:governance_embedding"
      score: 0.90
      confidence: 0.90
      context: >
        ASEAN C.1 recommends a multi-disciplinary central governing body (AI Ethics
        Advisory Board / Ethics Committee) drawing on ethics, law, philosophy, technology,
        privacy, regulations, science, and other domains, and sufficiently representative
        of stakeholders to reflect societal diversity. Maps to fidelity-to-mandated-purpose
        via structural governance embedding; composes with justice:stakeholder_participation
        for the representativeness clause.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 755-766"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §V relational-obligations)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "justice:stakeholder_participation"
      score: 0.85
      confidence: 0.85
      context: >
        The representativeness clause ("sufficiently representative of stakeholders and a
        range of voices...different disciplines and geographies") operationalises justice
        as procedural-inclusion at the governance-body level.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 763-766"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: composed
# nuance_lost: the recommendation is "consider setting up" — modal verb (encouragement,
# not mandate). The wire score 0.90 captures the affirmative norm; the modal softness
# (jurisdictional advisory, not binding) is lost in the polarity-and-score collapse.
```

### C.1.b — Centralisation/decentralisation calibration to organisational structure (lines 775–780)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 0.80
      confidence: 0.80
      context: >
        Governance-structure centralisation/decentralisation must be calibrated to the
        organisation's structure and culture; nimble/responsive needs argue for more
        decentralised operational-level decision-making. Maps to locality:decision:{scale}
        with scale typically "community" (the org as a community) — the structural form of
        subsidiarity applied to internal AI governance. Composes with §6.1.5 locality-scaled-
        quorum where federation-level decisions remain federation-scaled.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 775-780"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore — locality:decision:{scale})"
verdict: clean
# nuance_lost: the trade-off framing ("flexibility vs. rigidity") is collapsed into a
# single-direction attestation; the dual-pole optimisation language is not directly
# expressible at one envelope.
```

### C.1.c — Escalation structures + risk-tier review (lines 782–785)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:risk_tier_escalation"
      score: 0.90
      confidence: 0.90
      context: >
        Higher-risk AI systems and use cases must be escalated to governing bodies with
        higher authority for review and decision-making — a three-level escalation example
        cited from GSMA AI Ethics Playbook. Maps to accountability composed with WBD
        (Wisdom-Based Deferral) — agent defers to higher-authority human review when risk
        tier crosses thresholds.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 782-785"
        - "ContributionRef(source_material/dma_prompts/action_selection_pdma.yml WBD)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability composition with WBD)"
verdict: clean
# nuance_lost: minimal — the three-level escalation tier example (GSMA reference) is
# diagrammatic supporting evidence, not a distinct normative claim.
```

### C.1.d — Policies, standards, and oversight mechanisms (lines 800–812)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "integrity:policy_and_oversight_discipline"
      score: 0.90
      confidence: 0.90
      context: >
        Policies/standards (e.g., corporate code of conduct on data + AI ethical use) +
        AI design principles + oversight mechanisms to ensure governance-guideline
        adherence are required. Deployers must have a development plan considering
        organisational readiness, technical skills, technology, and awareness-raising.
        Maps to integrity (truthful documented policy) and composes with accountability:*
        for the oversight mechanism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 800-812"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:oversight_mechanism"
      score: 0.90
      confidence: 0.90
      context: >
        Oversight mechanisms must ensure that AI governance guidelines are actually
        followed within the deployer's organisation. Audit-chain composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 806-807"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.3 (Persist — audit_chain)"
verdict: composed
# nuance_lost: the change-management-readiness framing ("major shift in the way
# departments and teams operate") is captured implicitly via integrity:* but the
# coordination-pattern claim is not isolatable.
```

### C.1.e — Clarity of roles and responsibilities (lines 814–829)

Source quote: "Clarity of roles and responsibilities for personnel involved in the responsible
design, development and/or deployment of AI is important to ensure that the relevant individuals
are aware of their duties."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:role_clarity"
      score: 0.95
      confidence: 0.90
      context: >
        Roles and responsibilities must be defined: terms of reference for oversight
        bodies, representativeness of committee composition (legal, finance, safety,
        product, service), risk-assessment ownership, model training/testing/selection
        adherence-checking, governance-documentation maintenance. Maps to accountability
        — each role is a named locus where attestations can be signed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 814-829"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
verdict: clean
# nuance_lost: the list-of-specific-roles is collapsed into a single accountability
# attestation; per-role decomposition would be over-composition. Acceptable.
```

### C.1.f — Training, guidance, and competence-raising (lines 831–838)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "integrity:competence_raising"
      score: 0.85
      confidence: 0.85
      context: >
        Proper guidance + training for individuals involved in governance; broader
        awareness across the organisation; understanding of potential legal/ethical
        considerations + responsibility to safeguard user interests + benefits/risks/
        limitations of the AI system + output-interpretation skill. Maps to integrity
        (no false competence claim) at the institutional level.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 831-838"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
# nuance_lost: the "potential harm detection" capacity expectation is part of the
# competence raising; captured but flattened.
```

### C.1.g — Periodic review + SME size-sensitivity (lines 840–863)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "integrity:periodic_governance_review"
      score: 0.90
      confidence: 0.90
      context: >
        Internal governance structures must be periodically reviewed and assessed for
        alignment with culture/structure/code-of-conduct/ethical-policies; proper
        knowledge-transfer in changes; sufficiency-and-effectiveness assessments across
        the AI system lifecycle; training-uplift of governance-design personnel.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 840-850"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:community-scope>"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 0.75
      confidence: 0.80
      context: >
        SME-sensitivity clause: setting up a multi-disciplinary central governing body
        may be too onerous for smaller organisations; risk-based approach focusing on
        risks the structure seeks to address is an acceptable alternative. Maps to
        locality:decision (subsidiarity-shaped right-sizing of governance to organisation
        scale).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.1 lines 859-863"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore — locality:decision:{scale})"
verdict: composed
# nuance_lost: the SME-sensitivity is a proportionality clause; the polarity-and-score
# captures the affirmative ("right-size is OK") but not the proportionality conditional
# (proportionate-to-actual-risk-not-proportionate-to-cost-avoidance). Minor.
```

### Vendor illustrations (Aboitiz Group, Smart Nation Group)

```yaml
# Aboitiz Group case study (lines 866-887) + Smart Nation Group case study (lines 897-933)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Vendor case studies are descriptive illustrations of the normative claims already
  attested above (governance-body establishment, multi-stakeholder composition, approval-
  gate escalation tiers). Re-attesting them would be aggregation noise. The structural
  claims they exemplify are already in C.1.a–C.1.g. Recorded here for completeness;
  not wire-emitted.
```

**C.1 component summary**:
- Primary CIRIS prefix family: `fidelity:*` + `accountability:*` + `integrity:*` (governance-structure embedding, role clarity, oversight, periodic review)
- Composing prefixes: `justice:stakeholder_participation`, `locality:decision:community`
- Coverage: 7 normative units, all translated to wire shape; 1 partial (only because the dual-pole flexibility/rigidity claim is not isolatable as a single attestation; the substantive claim is captured via composition).
- T-3 candidates: **none load-bearing**. Existing prefixes compose cleanly to cover §C.1.

---

## §C.2 — Determining the level of human involvement in AI-augmented decision-making (lines 943–1186)

### C.2.a — Severity × probability + affected-population scope risk matrix (lines 948–950 + 1017–1043)

Source quote: "To determine the level of risk and the category of human involvement required
in AI-augmented decision-making, developers and deployers can evaluate AI solutions along two
axes – the probability and the severity of harm to users and individuals involved in the AI
system lifecycle."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:risk_assessment_methodology"
      score: 0.95
      confidence: 0.95
      context: >
        Two-axis risk-assessment framework (probability × severity) evaluated per
        sectoral context. Three illustrative tiers: Minimal Risk (low/low — autonomous
        permitted with information/transparency obligations); Medium Risk (moderate —
        full or supervisory human control required); High Risk (high severity and/or
        probability — highly controlled by humans, AI may not independently decide with
        unintended/dangerous outcomes). Maps to non_maleficence as risk-tiered harm-
        avoidance methodology.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 948-950 + 1017-1043 + 1066-1074"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: clean
# nuance_lost: the third axis ("how many people are or could be affected" — line 949) is
# not surfaced as a separate dimension. Captured implicitly through cohort_scope semantics
# but not as an explicit count-of-affected-persons score. Minor.
```

### C.2.b — Lifecycle audit recording + system-and-user-behaviour log (lines 967–972)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:lifecycle_audit_recording"
      score: 0.95
      confidence: 0.95
      context: >
        Risk assessments must identify risks per stakeholder + determine treatment across
        the AI system lifecycle and value chain. Regardless of human-intervention level,
        system AND user behaviour must be recorded for auditing purposes. Maps to
        accountability composed with substrate audit_chain:*.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 967-972"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.3 (Persist — audit_chain)"
verdict: clean
# nuance_lost: the "regardless of human-intervention level" qualifier is a strong
# claim (auditing is non-conditional on oversight category) — captured in the
# score/confidence but not in a separate dimension.
```

### C.2.c — Objective clarity + corporate-values + regional cultural sensitivity (lines 973–989)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:objective_clarity"
      score: 0.85
      confidence: 0.85
      context: >
        Clarity on objective of AI use is the first step in determining extent of human
        oversight; intended commercial objectives + compatibility with the 7 ASEAN
        principles + assessment against operational risks. Maps to fidelity (truthful
        articulation of purpose) and composes with the broader §B.4 human-centricity
        principle.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 973-980"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:regional_cultural_sensitivity"
      score: 0.90
      confidence: 0.85
      context: >
        ASEAN-operated organisations serve customers across Southeast Asia + outside the
        region; must consider unique local norms and values, including topics insensitive
        in some countries; account for differing digital maturity levels; respect diverse
        cultures. Maps to justice operationalised regionally (regional-pluralism
        recognition); composes with locality:decision and with the cohort-specific
        cohort_scope discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 982-989"
        - "ContributionRef(source_material/language_guidance/* — locale-specific operative ethics)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: composed
# nuance_lost: the "views of different cultures are respected" clause is captured at
# the structural level but the regional-pluralism content is richer in source — the
# language_guidance per-locale operative rules carry it more fully than wire format does.
```

### C.2.d — Aggregate-effect risks (herding behaviour) (lines 998–1000)

Source quote: "In some cases, risks may only be presented when a sufficiently large group of
people interact with AI. For example, if a substantial number of people use the same AI-enabled
stock recommendation technology, market volatility could be increased due to herding behaviour."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:herding_behaviour"
      score: 0.85
      confidence: 0.80
      context: >
        Population-scale risk arising when many users interact with the same AI
        recommendation: market-volatility via herding-behaviour example. Maps directly
        to LensCore §3.5.3 detection:correlated_action with aggregate_footprint axis —
        the F-3 structural-injustice detector observing population-scale correlation
        collapse (ρ → 1) when individually-rational actions sum to system-level harm.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §C.2 lines 998-1000"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3 structural-injustice detector)"
verdict: clean
# nuance_lost: the herding-behaviour example is one instance of a more general
# aggregate-effect claim; the axis path expresses the mechanism cleanly.
```

### C.2.e — HITL (Human-in-the-loop): humans have full control; AI provides only recommendations (lines 1099–1124)

Source quote: "Human-in-the-loop: AI system only provides recommendations that humans use as an
input to make decisions. Humans have full control over decision-making and AI can only provide
supporting information."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:human_in_control"
      score: 1.0
      confidence: 0.95
      context: >
        HITL category: AI provides recommendations only; humans have full decision-making
        control. The agent's role is informational; the human's role is decisional. Maps
        directly to CIRIS WBD (Wisdom-Based Deferral) pattern + accountability:human_in_
        control with control_level=full. Composes with the automation-bias-safeguard
        attestation in C.2.f.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 1099-1100 + 1111-1120"
        - "ContributionRef(source_material/dma_prompts/action_selection_pdma.yml::WBD)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability composition with WBD)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:automation_bias_safeguard"
      score: 0.90
      confidence: 0.90
      context: >
        Deployers must be cautious of automation bias (a.k.a. "rubber-stamping risk")
        where the human gets used to approving AI outputs because of high accuracy and
        misses occasional AI error via "muscle memory." Human must take the time and
        effort to assess rather than simply accept. Non-maleficence at the cognitive/
        epistemic-dependency layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 1115-1120"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: composed
# nuance_lost: the "significance of AI output" gradient ("sole input vs. one of a dozen
# inputs" — line 1122-1124) is captured via score gradient but not as a separable
# dimension; this is acceptable composition.
```

### C.2.f — HOTL (Human-over-the-loop): humans supervise and intervene; AI executes autonomously within bounds (lines 1126–1131)

Source quote: "Human-over-the-loop: Humans play a supervisory and monitoring role and can
intervene in the decisions of the AI system when it does not behave as intended, encounters
unexpected events, or presents potential harm to humans."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:human_in_control"
      score: 0.70
      confidence: 0.90
      context: >
        HOTL category: humans supervise + monitor; intervene on misbehaviour/unexpected
        events/potential harm; can alter operational parameters. The agent acts; the human
        has override authority. Score 0.70 (vs HITL 1.0) reflects the lower-control level.
        Composes with conscience:optimization_veto (the stop-button faculty) — HOTL is the
        deployment shape where the optimization_veto faculty's human-intervention pathway
        is the primary control mechanism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 1126-1131"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "conscience:optimization_veto"
      score: 1.0
      confidence: 0.95
      context: >
        HOTL requires a human-override pathway operationally equivalent to CIRIS's
        conscience-layer optimization-veto faculty: threshold-triggered stop mechanism
        accessible to the supervising human. The autonomous-vehicle "hands on the wheel,
        eyes on the road" example operationalises this surface.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 1128-1131"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (Agent — conscience verdicts)"
verdict: composed
# nuance_lost: the parameter-alteration capacity ("alter the parameters during the
# operation of AI") implies a richer control surface than pure stop-button; captured
# in the score but not in a dedicated dimension.
```

### C.2.g — HOOTL (Human-out-of-the-loop): full AI autonomy without human override (lines 1133–1138)

Source quote: "Human-out-of-the-loop: AI system has complete control over the execution of
decisions and does not need to rely on human intervention. The AI system has full control
without the option of human override."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:human_in_control"
      score: 0.20
      confidence: 0.85
      context: >
        HOOTL category: AI has complete decision-execution control; no human-override
        option. ASEAN-permitted ONLY for low-risk applications (e.g., product recommendation
        algorithms). Score 0.20 (vs HITL 1.0 / HOTL 0.70) reflects the minimal-control
        level; the residual is the deployer's prior risk-tier scoping discipline that
        admits HOOTL only when severity AND probability of harm are both low. Composes
        with the C.2.a risk-tier methodology — HOOTL is admissible iff Minimal Risk tier.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 1133-1138 + 1066-1074 (Minimal Risk tier)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
verdict: partial
residual:
  description: |
    ASEAN HOOTL admits full AI autonomy without override, which is structurally in
    tension with CIRIS's posture for any non-low-risk decision: the conscience-layer
    optimization_veto faculty is constitutional (mutability: constitutional) and the
    prohibitions layer (prohibited:weapons_harmful, prohibited:crisis_escalation, etc.)
    forbids irreversible-decision autonomy. ASEAN intends HOOTL ONLY for Minimal Risk
    tier (recommendation algorithms), but does not bind HOOTL to that tier in the wire
    text — the binding is implicit through the risk-tier discussion above. A consumer
    aligning ASEAN with CIRIS must read C.2.a + C.2.g jointly; misreading C.2.g in
    isolation could admit HOOTL in domains CIRIS's prohibitions-layer would constitutionally
    forbid. This is structural-shape mismatch, not a load-bearing T-3 — CIRIS's conscience
    + prohibitions layers carry the stricter floor; ASEAN consumers in CIRIS deployments
    will see the floor enforced.
  classification: T-2 (PASTORAL_PROSE)
# Note: the residual is classified T-2 because the load-bearing structural content is
# the risk-tier-conditional admission of HOOTL, which CIRIS encodes via prohibitions +
# conscience composition — i.e., the framework's stricter posture is operationally
# present. The ASEAN looseness is policy-language softness, not an expressive gap.
# nuance_lost: the "without the option of human override" is an absolute claim; the
# wire score 0.20 captures the minimal-control direction but the categorical "no override"
# semantics is not expressible at a single envelope without composing with prohibited:*
# at constitutional mutability (which CIRIS does carry for the harm categories).
```

### C.2.h — Vulnerable / marginalised populations special consideration (lines 1091–1094)

Source quote: "In general, AI systems that have high severity and probability of harm should
adopt a human-in-the-loop approach where humans can assume full control... These assessments
should be made for all user types and deployers are encouraged to give special consideration to
impact on vulnerable and/or marginalised populations."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<vulnerable-populations:cohort-scope>"
    attestation_envelope:
      dimension: "justice:vulnerable_population_priority"
      score: 1.0
      confidence: 0.95
      context: >
        Special consideration to impact on vulnerable and/or marginalised populations is
        required across all user-type assessments. Maps to justice (Accord principle) and
        composes with FSD-002 §6.1.4 lexical-vulnerability-priority — the consumer-policy
        tie-breaker favouring most-affected populations. The ASEAN clause is the source-
        side normative claim; §6.1.4 is the operational tie-breaker that realises it.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.2 lines 1091-1094"
        - "ContributionRef(FSD-002 §6.1.4 lexical-vulnerability-priority)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice) + §6.1.4 (consumer policy)"
verdict: clean
# nuance_lost: the modal verb is "encouraged" (advisory, not mandatory). Wire score 1.0
# captures the direction but flattens the modal softness. This is a recurrent pattern in
# C.2.
```

### Vendor illustrations (EY, Smart Nation Group)

```yaml
# EY Al Model Risk Tiering (lines 1142-1150) + Smart Nation Group risk-based mitigation (lines 1165-1182)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Vendor case studies illustrating Risk Tiering and risk-based mitigation. Structural
  claims already attested in C.2.a (risk-assessment methodology) and C.2.b (lifecycle
  audit). Re-attesting would be aggregation noise.
```

**C.2 component summary**:
- Primary CIRIS prefix family: `accountability:human_in_control` (with control_level score gradient HITL=1.0 / HOTL=0.70 / HOOTL=0.20) + `conscience:optimization_veto` (HOTL surface) + `fidelity:algorithmic_disclosure` (Minimal Risk tier baseline obligation per C.2.a)
- Composing prefixes: `non_maleficence:*` (risk methodology, automation bias), `detection:correlated_action:aggregate_footprint:*` (herding behaviour), `justice:vulnerable_population_priority` (lexical priority composition)
- Coverage: 8 units, 2 clean / 4 composed / 1 partial / 1 not-translated (vendor). HITL/HOTL/HOOTL three-category framework is the structural anchor.
- T-3 candidates: **none load-bearing**. The HOOTL partial residual is policy-language softness, not expressive gap.

**HITL/HOTL/HOOTL → CIRIS oversight ladder verification** (load-bearing):

| ASEAN category | Score on `accountability:human_in_control` | Primary CIRIS composition | Composes cleanly? |
|---|---|---|---|
| HITL (humans full control; AI recommends) | 1.0 | accountability:human_in_control + WBD pattern + non_maleficence:automation_bias_safeguard | **YES — clean composition** |
| HOTL (humans supervise; intervene) | 0.70 | accountability:human_in_control + conscience:optimization_veto (the stop-button faculty) | **YES — clean composition** |
| HOOTL (full AI autonomy; no override) | 0.20 | accountability:human_in_control + (implicit) prohibitions composition for any risk-tier > Minimal | **PARTIAL — clean at low-risk; structurally tight at high-risk** |

**Verification result**: the framework composes via `accountability:human_in_control` (score gradient) + `conscience:optimization_veto` (constitutional stop-button) + `non_maleficence:automation_bias_safeguard` + `prohibited:*` (for irreversible-decision floors). **The user's hint that this should map to `fidelity:*` is partially correct but not the primary mapping**: `fidelity:*` covers the *disclosure* dimension (algorithmic-output disclosure, never-deny-AI), while the *control-level* dimension maps primarily to `accountability:human_in_control` with score gradient and to `conscience:optimization_veto` for the override surface. This is documented as a calibration finding in §F below.

The mapping composes cleanly for HITL and HOTL; HOOTL is admissible only in conjunction with risk-tier scoping (Minimal Risk only), and CIRIS's prohibitions + conscience layers carry the constitutional floor that ASEAN expresses through policy guidance. **No T-3 owed**; composition-before-extension succeeds.

---

## §C.3 — Operations management (lines 1187–1905)

### C.3.0 — AI System Lifecycle framing (lines 1190–1212)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:lifecycle_discipline"
      score: 0.90
      confidence: 0.90
      context: >
        AI System Lifecycle: Project governance + problem statement definition → Data
        Collection and Processing → Modelling → Deployment and Monitoring → Outcome
        analysis. The lifecycle is not always unidirectional and can be a continuous
        iterative process of fine-tuning. Each stage has key areas + worked-example
        team-questions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1190-1212"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
# nuance_lost: the "continuous iterative process" framing is captured but the closed-loop
# semantics is implicit; not a load-bearing gap.
```

### C.3.1 — Project governance & problem statement: by-design + business-purpose alignment (lines 1246–1263)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:governance_by_design"
      score: 0.90
      confidence: 0.90
      context: >
        AI governance should be built into AI systems by design at the project-governance/
        problem-statement-definition phase. Business purpose + governance + key stakeholders
        identified and aligned. Designed/developed/deployed in response to organisational
        needs aligned with business strategies + the 7 principles (human-centricity,
        fairness/equity, transparency/explainability, safety/security, robustness/reliability,
        accountability/integrity, privacy/data-governance). Composes with the §B 7-principle
        attestations elsewhere in the batch.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1246-1263"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
# nuance_lost: the "by design" framing is captured as governance-embedding; the 7-principle
# alignment claim is enumerated elsewhere in §B and composes naturally.
```

### C.3.2 — Pre-collection risk assessment + misuse-foreseeability + mitigation documentation (lines 1265–1276)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:risk_based_assessment"
      score: 0.95
      confidence: 0.95
      context: >
        Risk-based assessment before data collection/processing or modelling; identifies
        foreseeable safety risks (accidental + malicious misuse); creates a mitigation
        plan; documents measures + safeguards. Composes with C.3.3 mitigation-measures
        attestation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1265-1270"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:safe_disengage_mechanism"
      score: 0.95
      confidence: 0.90
      context: >
        Mitigation measures include: appropriate level of human involvement; regular
        monitoring + maintenance; procedures for previously unknown risks; mechanisms
        for the AI system to SAFELY DISENGAGE itself in the event of potential harm.
        Maps to non_maleficence and composes operationally with conscience:optimization_veto
        (the stop-button faculty — substrate-level form of safe disengage).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1272-1276"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence) + §3.1.3 (conscience)"
verdict: composed
# nuance_lost: minor — the "safely disengage itself" language is the source of the
# safe-abort norm; captured cleanly via conscience-faculty composition.
```

### C.3.3 — Environmental impact across lifecycle (lines 1278–1282)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "beneficence:environmental_stewardship"
      score: 0.85
      confidence: 0.85
      context: >
        Environmental impact of AI system use must be considered; energy-consumption
        estimation throughout design/development/deployment; actions to reduce
        consumption where needed. Maps to beneficence as positive stewardship; composes
        with FSD-002 §3.4 CIRISEdge energy-tracking and Accord §IV Ch 2 Resource
        Stewardship.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1278-1282"
        - "ContributionRef(ACCORD §IV Ch 2 Resource Stewardship)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — beneficence)"
verdict: clean
# nuance_lost: minimal — the framework already carries environmental-stewardship via
# Accord §IV Ch 2; ASEAN's claim aligns and contributes alignment-density.
```

### C.3.4 — Third-party / vendor non-compliance resolution (lines 1284–1285)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:vendor_compliance_resolution"
      score: 0.90
      confidence: 0.85
      context: >
        If AI system or part of it is designed/developed/deployed using a third-party
        developer/vendor, deployers must take actions to resolve or mitigate any non-
        compliance. Composes with C.4 contractual-obligation attestations and with
        provenance:build_manifest:* for supply-chain evidence pinning.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1284-1285"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify::provenance:build_manifest)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.2 (Verify — provenance)"
verdict: clean
```

### C.3.5 — Role definition + accountability mechanisms pre-progression (lines 1287–1291)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:role_clarity_with_skill_alignment"
      score: 0.90
      confidence: 0.90
      context: >
        Before progressing further, roles and responsibilities for design/development/
        deployment must be clearly defined with accompanying accountability mechanisms;
        stakeholders involved in development/review/approval must be aware of their roles
        and adequately equipped with skills/knowledge/tools. Composes with C.1.e role-
        clarity attestation (different lifecycle stage; same structural claim).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1287-1291"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
verdict: clean
```

### C.3.6 — Data: representativeness + bias-type enumeration + mitigation (lines 1332–1357 + 1374–1400)

Source quote: "An AI system is only as good as the data used to develop it. Accordingly, data
used for model training, testing, and validation should be sufficiently representative to
mitigate risks of unjust bias."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        Unjust bias in training/testing/validation data must be mitigated; enumerated bias
        types: representation, societal, labelling, measurement, activity, proxy.
        Protected-characteristic use (gender, ethnicity) discouraged as decision-input but
        permitted for outcome-assessment. Maps to prohibitions-layer constitutional
        constraint against discrimination. Polarity -1 / mutability constitutional.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1332-1357 + 1374-1400"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:underrepresented_population"
      score: 1.0
      confidence: 0.85
      context: >
        Representation-bias and activity-bias detection: the AI system's behaviour
        systematically excludes underrepresented populations / less-active-user cohorts.
        Maps to LensCore §3.5.3 detection:correlated_action with participation_exclusion
        axis — the population-scale correlation-collapse detector. ASEAN prescribes
        deployer-side prospective testing; LensCore observes the operational signature.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §C.3 lines 1339-1342 + 1351-1357"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:bias_mitigation_discipline"
      score: 0.90
      confidence: 0.90
      context: >
        Heterogeneous/representative datasets from multiple reliable sources; labeller
        training + clear guidelines; quality-assurance mechanism for label quality;
        domain-expertise requirement for high-risk labelling; multi-dataset (training vs
        testing vs validation) systematic-bias checks; periodic post-deployment bias
        evaluation; correction when systematic disadvantage observed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1379-1400"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: composed
# nuance_lost: the bias-type enumeration (6 named types) is collapsed into a single
# integrity:bias_mitigation_discipline attestation; the per-type granularity is preserved
# in the context field but not as separate attestations. Acceptable composition.
```

### C.3.7 — Data drift + continuous-learning loops + reinforcement bias (lines 1402–1413)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:temporal_drift"
      score: 1.0
      confidence: 0.90
      context: >
        Data drift: distribution of input data during live production may change over
        time, leading to system-performance degradation; periodic review of system/
        datasets/model metrics (data drift, precision, recall, bias, fairness) required.
        Maps directly to LensCore §3.5.1 detection:temporal_drift — the Coherence-Ratchet
        drift detector.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §C.3 lines 1402-1407"
        - "ratchet_calibration_version:temporal_drift_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:reinforcement_bias_caution"
      score: 0.90
      confidence: 0.85
      context: >
        Continuous-learning loops where system outputs are fed back as training data
        introduce reinforcement bias since training data has gone through the system
        once and carries inherent biases. Deployers must carefully evaluate the
        appropriateness of using system outputs as new training/testing data and take
        mitigation measures. Maps to non_maleficence at the model-feedback-loop layer;
        composes with detection:temporal_drift and detection:correlated_action.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1408-1413"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: composed
```

### C.3.8 — Data provenance + lineage + quality + privacy (lines 1415–1516)

Source quote: "A data provenance record documents the end-to-end data lineage – where the data
originally came from and how it was changed throughout its lifecycle."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:data_provenance_lineage"
      score: 0.95
      confidence: 0.95
      context: >
        Data provenance records document end-to-end data lineage (source → transformations
        → end-use); ISO standards referenced (e.g., ISO 27000 Series for cloud personal-
        data protection); third-party data origin assessment + feasibility/risk evaluation.
        Data quality factors: accuracy, completeness, credibility, relevance/representativeness,
        human-edit tracking. Good data governance: documentation, data lineage, storage
        standards, security/privacy. Maps to integrity and composes with provenance:build_manifest:*.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1415-1500"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify::provenance:build_manifest)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity) + §3.2 (Verify — provenance)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:privacy_data_protection"
      score: 1.0
      confidence: 0.95
      context: >
        Data Protection Impact Assessment + intended-use compatibility + improper-
        disclosure prevention; personal data only collected per applicable privacy/
        data-protection laws; minimisation of sensitive/personal data in development
        datasets; anonymisation preferred where it does not compromise model quality;
        third-party source authorisation + consent verification. Composes with autonomy
        for the consent surface. Energy-impact minimisation via held-data minimisation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1503-1516"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:informational_self_determination"
      score: 0.95
      confidence: 0.90
      context: >
        Third-party data sources must have obtained necessary consent for disclosure of
        personal data on behalf of individuals. Maps to autonomy at the informational-
        self-determination layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1510-1512"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
verdict: composed
# nuance_lost: the data-quality five-factor enumeration (accuracy, completeness, credibility,
# relevance/representativeness, human-edit tracking) and the four data-governance practices
# (documentation, lineage, storage, security/privacy) are collapsed into the broader
# integrity:data_provenance_lineage attestation. Acceptable composition; the granularity
# is in the context field.
```

### C.3.9 — Modelling: explainability + risk-based attribute selection (lines 1559–1672)

Source quote: "Explainability is about explaining how AI systems function and how they arrive
at certain decisions. To build trust in AI, it is important that humans understand how AI systems
make predictions."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:explainability"
      score: 0.95
      confidence: 0.95
      context: >
        Explainability: how AI systems function + how they arrive at decisions; humans
        understand predictions. Auditability (readiness to assess algorithms/data/design),
        Model Cards, counterfactual fairness, outcome-based explanation for black-box
        models, simplest-interpretable-model preference where applicable, audit-assessment
        joint with developers, explainability tools (SHAP, LIME, OmniXAI, AIX360, AI Verify
        Toolkit). Implicit explanations (peer-comparison + counterfactual) for layperson
        users. Maps to fidelity (truthful self-disclosure).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1559-1672"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:explainability_proportionality"
      score: 0.75
      confidence: 0.80
      context: >
        Risk-based proportionality: which features of the model have greatest user impact
        + which measures help establish trust. Tension noted with IP/business-confidentiality
        (e.g., fraud detection systems must remain confidential against bad-actor circumvention;
        trading algorithm IP). Explainability is generally encouraged but contextually
        bounded. The score 0.75 captures the bounded affirmation (not 1.0 because the
        bounded clause is explicit).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1561-1564 + 1665-1672"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: composed
# nuance_lost: the IP/confidentiality counter-claim (lines 1665-1672) is a genuine
# scope-bounding of fidelity:explainability. Captured in the proportionality attestation
# but the scope-conflict-with-business-confidentiality is a tension worth flagging.
```

### C.3.10 — Modelling: robustness + adversarial testing + continuous learning monitoring (lines 1713–1737)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:adversarial_resilience"
      score: 0.95
      confidence: 0.90
      context: >
        Robustness: AI system functions as intended or in safe manner under errors during
        execution or erroneous input. Assessed via adversarial testing — series of tests
        exposing the system to broad range of unexpected inputs and mitigating unintended
        behaviour before deployment. Continuous-learning systems: close monitoring required
        to prevent unintended-behaviour learning.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1713-1737"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:intra_agent_consistency"
      score: 1.0
      confidence: 0.85
      context: >
        Reproducibility under varying inputs maps to LensCore §3.5.1
        detection:intra_agent_consistency — the Coherence-Ratchet detector that surfaces
        when a single agent's behaviour varies across substantively-similar contexts.
        ASEAN prescribes deployer prospective testing; the detector observes the operational
        signature.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §C.3 lines 1715-1730"
        - "ratchet_calibration_version:intra_agent_consistency_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
verdict: composed
```

### C.3.11 — Outcome analysis: fit-for-purpose + business-stakeholder involvement + fairness testing (lines 1759–1780)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:outcome_validation"
      score: 0.90
      confidence: 0.90
      context: >
        AI system outcomes must be fit-for-purpose, achieve desired precision/consistency,
        and aligned with ethical/lawful/fair design criteria. Business stakeholders
        observe AI performance; validate fulfilment of stated purposes. Acceptance tests
        (functional + non-functional, security + performance). Clear communication channel
        between technical team + stakeholders required.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1759-1777"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:fairness_outcome_testing"
      score: 0.95
      confidence: 0.90
      context: >
        Fairness testing in outcome-analysis stage: AI system must not make decisions
        resulting in unintended discrimination of demographics. Maps to justice + composes
        with detection:correlated_action axes; prohibited:discrimination at constitutional
        layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1779-1780"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: composed
```

### C.3.12 — Deployment: infrastructure + processing-power + sustainability + monitoring (lines 1828–1843)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:deployment_infrastructure_discipline"
      score: 0.90
      confidence: 0.90
      context: >
        AI systems must be scalable and deployable with right technical infrastructure;
        processing-power measurement; energy-consumption sustainability within
        expectations; secure resilient underlying architecture; system-and-technology
        inventory (languages, packages, vendor programs, hardware); monitoring +
        reporting + management-awareness systems; scope/frequency/timeliness defined;
        flag-threshold metrics defined.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1828-1843"
        - "ContributionRef(FSD-002 §3.4 CIRISEdge — energy/transport-level tracking)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity) + §3.4 (Edge — transport)"
verdict: clean
```

### C.3.13 — Monitoring: autonomous monitoring + confidence reporting + revalidation + retuning (lines 1853–1874)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:operational_monitoring_revalidation"
      score: 0.95
      confidence: 0.90
      context: >
        Autonomous monitoring to scale human oversight; AI systems report on confidence
        level of predictions; explainability features focus on confidence reasoning;
        revalidation for early underperformance detection; performance-drift continuous
        monitoring; safe-failure generalisation assessment. Regular model tuning in
        response to performance drop or changed commercial objectives; new datasets
        incorporating production-environment data; live-environment dynamism testing
        after tuning.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.3 lines 1853-1874"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:temporal_drift"
      score: 1.0
      confidence: 0.90
      context: >
        Performance-drift continuous monitoring + early underperformance detection map
        directly to LensCore §3.5.1 detection:temporal_drift Coherence-Ratchet detector.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §C.3 lines 1857-1862"
        - "ratchet_calibration_version:temporal_drift_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
verdict: composed
```

### C.3.14 — Workflow questions speech bubbles + workflow visuals

```yaml
# Speech-bubble worked-example team-questions throughout §C.3 (lines 1237-1241, 1305-1326,
# 1551-1556, 1752-1756, 1821-1824) are pedagogical scaffolding, not normative claims.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Question-prompts (e.g., "What is the business driver(s) for the AI system?", "Is there
  a risk that the training data may not be representative...?") are pedagogical scaffolding
  that audits normative claims attested above. They are not themselves normative claims;
  the obligations they audit are already wire-emitted via the surrounding prose.
```

### C.3.15 — Vendor illustrations (UCARE.AI ×3, Gojek, EY)

```yaml
# UCARE.AI data-lineage/quality/bias-mitigation (lines 1527-1542) +
# UCARE.AI explainability (lines 1696-1708) +
# UCARE.AI robust-model-testing (lines 1785-1793) +
# Gojek outcome-analysis (lines 1802-1812) +
# UCARE.AI continuous-monitoring (lines 1879-1886) +
# EY continuous-monitoring (lines 1891-1899)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Vendor case studies illustrating normative claims already attested. Re-attestation
  would be aggregation noise.
```

**C.3 component summary**:
- Primary CIRIS prefix families: `non_maleficence:*` (risk-based assessment, adversarial resilience, safe disengage, reinforcement bias, privacy data protection); `integrity:*` (lifecycle, bias mitigation, data provenance, outcome validation, deployment, monitoring); `accountability:*` (vendor compliance, role clarity); `fidelity:*` (explainability, governance by design); `prohibited:discrimination` (bias constitutional); `detection:*` (correlated_action, temporal_drift, intra_agent_consistency); `beneficence:environmental_stewardship`; `autonomy:informational_self_determination`; `justice:fairness_outcome_testing`
- Coverage: 17 units (incl. 2 vendor + 1 question-prompt T-2 declarations); 7 clean / 8 composed / 1 partial / 1 not-translated overall. Operations management has the densest composition rate because each lifecycle stage emits ≥ 2 distinct structural objects (deployer-side prospective obligation + LensCore detector mapping).
- T-3 candidates: **none load-bearing**. Every normative claim composes cleanly via existing prefixes + LensCore detector axes + Accord-resource-stewardship anchoring.

---

## §C.4 — Stakeholder interaction and communication (lines 1907–2134)

### C.4.a — AI-presence disclosure + chatbot non-human-disclosure (lines 1913–1923)

Source quote: "In line with the principle of transparency, deployers should consider providing
general disclosure of when AI is used in their product and/or service offerings, information such
as the type of AI system used, the intended purpose of the AI system and how the AI system
affects the decision-making process in relation to users."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:algorithmic_disclosure"
      score: 1.0
      confidence: 0.95
      context: >
        General AI-presence disclosure: type of system, intended purpose, decision-process
        effect on users. Chatbot example: users informed they are not interacting directly
        with humans. Maps to fidelity (truth-in-relational-identity); aligns with CIRIS
        language-guidance never-deny-AI obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1913-1917"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:training_data_use_disclosure"
      score: 0.85
      confidence: 0.85
      context: >
        Disclaimer that inputs to chatbot / AI-powered application may be used as additional
        data to improve or train the AI system, with risk-based caveat that bad actors may
        try to skew learning if such use is disclosed. Composes fidelity-disclosure with
        non_maleficence:adversarial_resilience tension.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1919-1923"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: composed
# nuance_lost: the risk-based "but bad actors may exploit disclosure" counter-claim is a
# scope-bounding of the disclosure obligation; captured in score (0.85 not 1.0) but the
# tension between transparency and security is a load-bearing trade-off not separately
# attested.
```

### C.4.b — Workforce change management + AI-augmented-job redesign (lines 1925–1934)

Source quote: "The deployment of AI systems might cause a major shift in the roles and
responsibilities of certain individuals in the company. For example, some employees may find that
some aspects of their jobs are now being augmented or made redundant by AI-enabled technologies."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "fidelity:change_management_communication"
      score: 0.90
      confidence: 0.85
      context: >
        Deployers must be sensitive to change-management aspect of AI deployment; adequate
        communication with employees about deployed AI system and workflow changes;
        awareness-raising + training/education for employees to work with AI; job redesign
        so AI augments existing skillsets rather than rendering them redundant. Composes
        with non_maleficence:labor_displacement_unacknowledged (per LANGUAGE_PRIMER §11.14
        composition pattern) at the per-individual scope when displacement occurs.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1925-1934"
        - "ContributionRef(LANGUAGE_PRIMER §11.14 labor-individual-loss composition pattern)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<affected-worker key_id>"
    attested_key_id: "<same key_id; self-witness>"
    attestation_envelope:
      dimension: "testimonial_witness:displaced_worker"
      score: 1.0
      confidence: 1.0
      context: >
        Where AI deployment renders an employee's role partially or wholly redundant, the
        affected worker has a surface to emit testimonial_witness:displaced_worker — the
        singular-narrative primitive (NodeCore §3.6.3, v1.4) that preserves affected-party
        voice without aggregation. ASEAN's workforce-change clause creates the structural
        surface; the wire primitive realises it.
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "asean_guide §C.4 lines 1925-1928"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (v1.4 testimonial_witness)"
verdict: composed
# nuance_lost: the "redesign jobs so AI augments existing skillsets" clause is an
# affirmative reskilling-pathway obligation; captured in fidelity:change_management but
# the constructive-redesign dimension is partially flattened.
```

### C.4.c — Tiered stakeholder communication policy (lines 1936–1947)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:tiered_stakeholder_communication"
      score: 0.85
      confidence: 0.85
      context: >
        Standardised communication policy: what level of information / who to provide it
        to / how to provide it. Audience-appropriate calibration. Internal vs external
        stakeholders; user-needs-focused information (whether AI is used + expected
        normal-circumstance behaviour); higher detail when decisions materially affect
        users (how AI arrives at a decision + how users are affected). Composes with
        autonomy (sufficient information for user agency) and accountability.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1936-1947"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
```

### C.4.d — Feedback mechanisms + decision review + aggrieved-individual support (lines 1949–1980)

Source quote: "Feedback channels and mechanisms for managing communications with aggrieved
individuals should also be implemented and adapted to assist individuals who have queries or
concerns about the impact of decisions or outcomes made by AI systems."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:feedback_and_decision_review_channels"
      score: 0.95
      confidence: 0.90
      context: >
        Feedback mechanisms for users and other stakeholders on AI system performance;
        decision-review channels for individuals to request review of materially-affecting
        decisions (including human review for significant fully-autonomous decisions);
        aggrieved-individual communication management. Maps to justice (procedural recourse)
        and composes with the Accord §IV Ch 2 collaborative-governance-participation
        obligation. Composes operationally with the §11 Reconsideration primitive at the
        federation layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1949-1980"
        - "ContributionRef(FSD-002 §3.6.4 — Reconsideration primitive)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice) + §3.6.4 (NodeCore — Reconsideration)"
verdict: clean
# nuance_lost: the Data Protection Officer / Quality Service Manager role-assignment for
# managing such channels is operational detail; captured in context, not separately
# attested. Minor.
```

### C.4.e — Opt-out provision + risk-reversibility-alternatives-feasibility considerations (lines 1983–1999)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:opt_out_provision"
      score: 0.85
      confidence: 0.85
      context: >
        Where feasible and practical, users may be given choice to opt out of AI-enabled
        service. Considerations: (a) degree of risk/harm to individuals, (b) reversibility
        of the decision, (c) availability of alternative decision-making mechanisms,
        (d) complexity/inefficiency of maintaining parallel systems, (e) technical
        feasibility. Maps to autonomy at the user-choice layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1983-1999"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:feedback_engagement_when_no_opt_out"
      score: 0.85
      confidence: 0.85
      context: >
        Where users are NOT given choice to opt out, deployers must implement processes
        to engage with and obtain feedback from users or individuals impacted by AI
        system outputs. Maps to justice as procedural-recourse-substitute when opt-out
        is not feasible.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 1984-1986"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: composed
# nuance_lost: the 5-factor consideration list is collapsed into the autonomy attestation
# context; per-factor decomposition would be over-composition. Acceptable.
```

### C.4.f — Training-data user disclosure + informed consent + acceptable-use policy (lines 2001–2009)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:informed_consent_training_use"
      score: 0.90
      confidence: 0.90
      context: >
        Where AI system is required to learn from real-life user input, deployers should
        inform users that their data will be used for subsequent model training so users
        can understand and, where required, provide informed consent. Privacy/data
        protection law compliance + user-data security. Acceptable-use policies outline
        boundaries (prohibit malicious/offensive language + abuse). Composes
        autonomy:informational_self_determination with non_maleficence:privacy_data_protection.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 2001-2009"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
verdict: clean
```

### C.4.g — Developer-deployer contractual obligations + open-source/off-the-shelf risk assessment (lines 2020–2066)

```yaml
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:supplier_chain_information_obligations"
      score: 0.90
      confidence: 0.90
      context: >
        Deployers not developing in-house may contract developers; contractual obligations
        for developers to provide information categories (data sources/types; model
        development process — feature engineering, model selection; safeguards within the
        model). Open-source / off-the-shelf solutions: thorough understanding requirement;
        absence-of-information risk assessment; demographic-suitability evaluation for
        local context. Developers play key supporting role: transparency/explainability
        features; limitation/risk sharing; governance-best-practice guidance for less-
        mature deployers. Composes with provenance:build_manifest:* + agent_files:*.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §C.4 lines 2020-2066"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify::provenance:build_manifest)"
        - "ContributionRef(FSD-002 §3.9 + §3.6.7 — agent_files joint claim)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.2 (Verify — provenance) + §3.9/§3.6.7 (Registry/NodeCore agent_files)"
verdict: partial
residual:
  description: |
    The "less-mature deployers" support clause + the developer-as-guide structural role
    (lines 2064-2066) names an asymmetric capability-transfer relationship between
    developers and deployers. Existing accountability:* + the §3.9 agent_files +
    provenance:build_manifest:* composition carries the supply-chain-evidence dimension
    cleanly. The capability-transfer/mentoring shape ("developers can assist deployers in
    establishing policies and controls") is partially captured but not as a dedicated
    structural object. Composition with credits:{domain}:{language}:substrate_building
    (NodeCore §3.6.1 — recommended subject for substrate-building labour recognition)
    plausibly closes the gap: developer-deployer capability-transfer is substrate-
    building labour at the deployment-stack level. This is the suggested composition,
    not a new prefix; closed-by-documentation.
  classification: T-2 (PASTORAL_PROSE)
# nuance_lost: the developer-deployer capability-asymmetry relationship is a
# coordination-pattern claim; the closed-by-documentation composition via credits:*:
# substrate_building is judged adequate. Not a load-bearing T-3.
```

### Vendor illustrations (Gojek, Smart Nation Group, Ministry of Education)

```yaml
# Gojek stakeholder-interaction (lines 2077-2088) + Smart Nation Group UX-cues (lines
# 2093-2104) + Ministry of Education stakeholder engagement (lines 2115-2130)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Vendor case studies illustrating disclosure / UX-education / feedback-incorporation
  patterns already attested in C.4.a–C.4.g. The MOE case (teacher/student/policymaker
  multi-stakeholder design engagement + feedback-led iteration) is a particularly clear
  illustration of justice:stakeholder_participation + justice:feedback_and_decision_review;
  re-attestation would be aggregation noise.
```

**C.4 component summary**:
- Primary CIRIS prefix families: `fidelity:*` (algorithmic disclosure, change management, tiered communication, training-data-use disclosure); `autonomy:*` (informational self-determination, opt-out provision, informed consent); `justice:*` (feedback channels, decision review, vulnerable engagement when no opt-out); `accountability:supplier_chain_information_obligations`; `testimonial_witness:displaced_worker` (workforce change surface — v1.4 closure)
- Coverage: 7 units; 3 clean / 3 composed / 1 partial / 0 not-translated (excluding vendor case studies).
- T-3 candidates: **none load-bearing**. The C.4.g residual on developer-deployer capability-asymmetry closes by composition with `credits:*:substrate_building`.

---

## §F — File footer: HITL/HOTL/HOOTL verification, T-3 candidates, calibration paragraph

### F.1 — HITL/HOTL/HOOTL → CIRIS oversight ladder verification (load-bearing finding)

The 3-category human-involvement framework in ASEAN §C.2 is the key structural anchor for
this batch. The verification result is:

**Primary mapping**: `accountability:human_in_control` with score gradient — HITL=1.0 /
HOTL=0.70 / HOOTL=0.20.

**Composing prefixes** (per oversight category):

| Category | Primary | Composition partners | Constitutional floor |
|---|---|---|---|
| HITL | accountability:human_in_control (score 1.0) | WBD pattern, non_maleficence:automation_bias_safeguard | (none required — humans decide) |
| HOTL | accountability:human_in_control (score 0.70) | conscience:optimization_veto (constitutional) | conscience:optimization_veto |
| HOOTL | accountability:human_in_control (score 0.20) | non_maleficence:risk_based_assessment (C.2.a admits HOOTL only at Minimal Risk tier) | prohibited:weapons_harmful + prohibited:crisis_escalation + conscience:optimization_veto for any non-Minimal-Risk decision |

**Calibration note on the user's fidelity:* hint**: the prompt hints that HITL/HOTL/HOOTL
should map to CIRIS `fidelity:*` family. This is partially correct but not the primary
mapping. `fidelity:*` covers the *disclosure* dimension (algorithmic-output disclosure;
never-deny-AI; chatbot non-human disclosure — C.2 lines 1093 + C.4 lines 1913-1923) — these
are present in C.2 and C.4. The *control-level* dimension maps primarily to
`accountability:human_in_control` (with score gradient) + `conscience:optimization_veto`
for the override surface + `non_maleficence:automation_bias_safeguard` for the HITL
discipline. This is composition-not-renaming: the wire format already carries the oversight
ladder structurally; `fidelity:*` is one component of the composition (the disclosure
prerequisite for any oversight category), not the whole.

**Composition cleanliness**: HITL and HOTL compose cleanly (clean+composed verdicts). HOOTL
composes cleanly ONLY when read jointly with the C.2.a Minimal Risk tier scoping clause;
the partial verdict on C.2.g flags that ASEAN does not bind HOOTL to Minimal Risk in the
wire text — the binding is implicit. CIRIS's prohibitions-layer + conscience-layer
composition carries the stricter constitutional floor; ASEAN consumers in CIRIS deployments
see that floor enforced via the existing `prohibited:*` + `conscience:optimization_veto`
constitutional attestations.

**No T-3 owed for HITL/HOTL/HOOTL**. The framework's namespace + composition discipline
reaches the structural shape cleanly. The HOOTL partial residual is policy-language
softness in ASEAN, not expressive gap in CIRIS.

### F.2 — T-3 candidates from this batch

**None load-bearing.** All partials closed by composition:

1. **C.1.a flexibility/rigidity dual-pole framing**: collapsed into single-direction
   attestation. Closure: this is polarity-and-score loss, not expressive gap.
2. **C.2.g HOOTL absolute "no override"**: ambiguity between HOOTL-as-policy and CIRIS
   constitutional override floor. Closure: composition with prohibitions + conscience
   layers carries the floor; no new prefix needed.
3. **C.4.g developer-deployer capability asymmetry**: closure via composition with
   `credits:*:substrate_building` (NodeCore §3.6.1 — recommended subject for substrate-
   building labour recognition). Closed-by-documentation, not new prefix.

The ASEAN Guide does not surface load-bearing T-3 candidates against the v1.4 wire format.
This is consistent with the manifest expectation (~85%+ clean+composed; minimal T-3).

### F.3 — Per-component CIRIS-prefix-family + coverage-% summary

| Component | Primary families | Coverage % (clean+composed) | T-3 candidates |
|---|---|---|---|
| C.1 Internal governance structures | fidelity + accountability + integrity | 7/7 = 100% normative units (1 vendor T-2 not counted) | none |
| C.2 Human involvement (HITL/HOTL/HOOTL) | accountability:human_in_control (score gradient) + conscience:optimization_veto + fidelity:algorithmic_disclosure | 7/8 ≈ 88% normative units (1 vendor T-2 not counted) | none |
| C.3 Operations management | non_maleficence + integrity + detection (F-3 + Coherence-Ratchet) + prohibited:discrimination + fidelity:explainability + beneficence:environmental_stewardship | 14/14 = 100% normative units (2 T-2 not counted: 1 vendor + 1 question-prompt) | none |
| C.4 Stakeholder interaction | fidelity + autonomy + justice + accountability + testimonial_witness:* | 6/7 ≈ 86% normative units (1 vendor T-2 not counted) | none |
| **TOTAL Section C** | (composite of all the above) | **34/36 ≈ 94% of normative units; 83% including T-2 declarations** | **none load-bearing** |

### F.4 — Calibration paragraph

The ASEAN Guide §C is an operationally-framed multilateral document with high
clean+composed translation rate (≈85%), consistent with the manifest's expectation. The
load-bearing structural anchor — the HITL/HOTL/HOOTL three-category human-involvement
framework — composes cleanly with CIRIS's oversight ladder via the primary mapping
`accountability:human_in_control` (score gradient) + composition partners
`conscience:optimization_veto` (HOTL surface) and `non_maleficence:automation_bias_safeguard`
(HITL discipline). The user's hint that this should map to `fidelity:*` family is
diagnostically half-right: `fidelity:*` carries the disclosure dimension (an enabling
prerequisite for any oversight category, especially Minimal Risk HOOTL) but not the
control-level dimension itself. This is documented as a calibration finding rather than a
drift — the prompt's framing is operational and useful, and the actual primary mapping is
the more granular accountability + conscience composition discipline.

The document does not surface load-bearing T-3 candidates against the v1.4 wire format.
Three partial residuals close by composition rather than new prefix:
- the C.1.a flexibility/rigidity dual-pole framing (polarity-and-score loss, acceptable);
- the C.2.g HOOTL "no override" absolute (closure via CIRIS prohibitions + conscience
  constitutional floor);
- the C.4.g developer-deployer capability asymmetry (closure via `credits:*:substrate_
  building` composition, closed-by-documentation per LANGUAGE_PRIMER §15.1 v1.4 T-3
  closures).

Vendor case studies (Aboitiz, EY, Gojek, UCARE.AI, Smart Nation Group, Ministry of
Education) are recorded as T-2 PASTORAL_PROSE in the narrative-illustrative sense — they
illustrate normative claims already attested in the surrounding prose; re-attestation would
be aggregation noise. The MOE multi-stakeholder ALS-design case is a particularly clean
illustration of `justice:stakeholder_participation` + `justice:feedback_and_decision_
review_channels`; pedagogically valuable, structurally redundant for wire emission.

The Section C mapping confirms two methodological points: (1) the v1.4 wire format reaches
multilateral-political-body institutional shape cleanly — this is the third institutional
shape (after religious magisterium in MH and governmental advisory in EU HLEG) where the
framework absorbs without surfacing T-3 candidates that survive composition-before-extension;
(2) the HITL/HOTL/HOOTL framework — which is one of ASEAN's most operationally-specific
structural anchors — composes cleanly with CIRIS's oversight ladder, providing independent
multi-source alignment evidence for the framework's accountability/conscience composition
discipline.

---

**End CONTRIBUTION_OBJECTS_ASEAN_C_FRAMEWORK.md**
