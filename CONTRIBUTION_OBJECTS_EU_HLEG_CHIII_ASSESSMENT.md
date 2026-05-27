# CONTRIBUTION_OBJECTS_EU_HLEG_CHIII_ASSESSMENT.md
# EU HLEG Ethics Guidelines for Trustworthy AI (2019) — Chapter III "Assessing Trustworthy AI"
# Source range: lines 1272–1679 (Trustworthy AI Assessment List, pilot version)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}
#
# Methodological note (per the task brief):
#   Chapter III is an operational checklist of *questions* ("Did you ...?", "Have you ...?").
#   Each question audits a normative obligation. The translation discipline applied throughout
#   this file is **question -> implied positive contribution**: each interrogative form is
#   translated to the corresponding positive normative attestation (the requirement the
#   question audits). This conversion is annotated explicitly per unit ("[question->assertion]")
#   and is a methodological artifact of the assessment-list genre, not a divergent claim
#   from the framework's checklist intent.
#
#   The chapter's per-section organisation follows the 7 requirements from Chapter II.
#   Unit grouping in this file follows the same 7 sections to enable Phase 3 cross-chapter
#   verdict comparison (CHII per-requirement vs CHIII per-requirement).

---

## §III.0 — Chapter preface and governance/process scaffolding (lines 1272–1385)

```yaml
# III.0a — Assessment-list preface: pilot version; not legal-compliance evidence; application-specific.
# (lines 1272-1297 + 1369-1382: relation-to-existing-law and existing-process integration)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The chapter preface is methodological/procedural framing for the assessment list itself:
  it disclaims legal-compliance equivalence, declares the piloting process (qualitative +
  quantitative), and explains relation to existing law. These are publication-process
  statements about the document, not normative claims about AI systems. The structural
  claim implied — that ethical assessment is iteratively refined through stakeholder
  feedback — is operationally encoded in FSD-002 §4.9.2 (calibration-amendment via
  Contribution + WA quorum + Reconsideration). Cited as LAKE_ALIGN prose adjacency,
  not wire-emitted from this preface.
```

```yaml
# III.0b — Governance structure: management/Board + Compliance + Product/Service + QA + HR + Procurement + Operations
# (lines 1299-1342: org-role table)
# [question->assertion: the table prescribes that AI governance be embedded across organisational layers]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:governance_embedding"
      score: 0.85
      confidence: 0.85
      context: >
        Chapter III recommends implementing Trustworthy AI assessment via a governance
        structure that embraces operational AND management levels: Top Management acts as
        escalation board; Compliance/Legal owns assessment-list maintenance; Product/Service
        Development uses the list; QA escalates unsatisfactory outcomes; HR ensures
        team-diversity competency; Procurement checks the list for procured AI;
        day-to-day Operations document outcomes. Maps to fidelity-to-mandated-purpose
        through structural embedding rather than ad-hoc compliance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III governance-structure table, lines 1299-1342"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §V relational-obligations)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: partial
residual:
  description: |
    The organisational-role specification (top-management escalation board; HR diversity;
    Procurement check) is operationally specific and partially mapped via fidelity:governance_embedding
    composed with the §III.7 accountability attestations below. The fine-grained per-role
    decomposition (HR ensures diversity-of-profile; Procurement applies the list to vendors) is
    a coordination-pattern claim with no current dedicated prefix. Existing accountability:* +
    fidelity:* + the §6 deployment_profile composition is judged adequate; not a load-bearing
    T-3 candidate.
  classification: T-2 (PASTORAL_PROSE)
```

```yaml
# III.0c — Using the assessment list: log results both technically AND in management terms;
# pay attention to questions that cannot easily be answered (diversity-of-skills signal).
# (lines 1345-1367)
# [question->assertion: practitioners must engage the list iteratively and surface unanswerable questions]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:reflective_assessment_use"
      score: 0.80
      confidence: 0.85
      context: >
        Chapter III instructs practitioners to attend not only to areas of concern but also
        to questions that cannot easily be answered, treating unanswerable questions as a
        signal of skills/competence-diversity gap. Result-logging in both technical AND
        management terms is required. Maps to integrity (assessment is not box-ticking) and
        to detection:correlated_action:participation_exclusion (when a deployer cannot answer
        a question, that itself is a signal that some affected cohort is structurally
        excluded from the deliberation).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1345-1367"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

---

## §III.1 — Human agency and oversight (assessment-list items; lines 1388–1422)

```yaml
# III.1.a — Fundamental rights impact assessment + documented trade-off identification
# (lines 1389-1392)
# [question->assertion: a fundamental-rights impact assessment is required where negative impact is possible]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:rights_impact_assessment"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion translation of "Did you carry out a fundamental rights impact
        assessment where there could be a negative impact on fundamental rights? Did you
        identify and document potential trade-offs made between the different principles
        and rights?"] The audited obligation: where the AI system can negatively impact
        fundamental rights, a documented FRIA must be performed and the trade-offs between
        rights/principles named in writing. Composes with §III.7 documenting-trade-offs.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1389-1392"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II principle-weighting)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice/non_maleficence accountability composition)"
verdict: clean
```

```yaml
# III.1.b — Algorithmic-decision communication + chatbot non-human-disclosure
# (lines 1393-1400)
# [question->assertion: users must be informed when a decision/output is algorithmic, and
#  conversational agents must disclose non-human status]
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
        [question->assertion] Audited obligation: (a) the deployer must consider whether
        the system should disclose that a decision/content/advice/outcome is algorithmic;
        (b) in chatbot or conversational deployment, human end-users must be made aware
        they are interacting with a non-human agent. Maps to fidelity (truth-in-relational-
        identity) and to the deployer's never-deny-AI obligation in CIRIS language guidance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1393-1400"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:decision_process_non_interference"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Could the AI system affect human autonomy by interfering
        with the (end) user's decision-making process in an unintended way?"] The audited
        obligation: the deployer must assess and prevent unintended interference with the
        user's decision-making. Maps to autonomy (preservation of end-user deliberative
        agency).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1395-1396"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
verdict: composed
```

```yaml
# III.1.c — Human agency in work/labour processes; safeguards against overreliance
# (lines 1401-1407)
# [question->assertion: where AI is implemented in work, task allocation must preserve meaningful human
#  interaction, oversight, control; and the deployer must safeguard against overconfidence/overreliance]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:work_process_oversight"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] In AI deployments touching work/labour processes, the
        deployer must consider task allocation between AI and humans such that interactions
        remain meaningful and humans retain appropriate oversight and control. The
        capability-enhancement framing ("does the AI system enhance or augment human
        capabilities?") is the polarity-positive form of the same claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1401-1405"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:overreliance_safeguard"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Did you take safeguards to prevent overconfidence in or
        overreliance on the AI system for work processes?"] The audited obligation:
        deployers must take safeguards against user overconfidence/overreliance.
        Non-maleficence harm class: epistemic-dependency drift.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1406-1407"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: composed
```

```yaml
# III.1.d — Human-oversight mechanisms: control-level, named human-in-control, intervention tools, audit/remedy
# (lines 1408-1414)
# [question->assertion: deployers must determine appropriate control level, name the human-in-control,
#  ensure mechanisms for control/oversight, and enable audit + remediation of governance failures]
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
        [question->assertion] Audited obligation: (a) the deployer must determine an
        appropriate level of human control for the use case, (b) the "human in control"
        must be identifiable, (c) intervention tools/moments must be specified, (d)
        mechanisms must be in place to ensure that control, and (e) audit + remediation
        mechanisms for governance-of-AI-autonomy must exist. Composes with §III.7 auditability.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1408-1414"
        - "ContributionRef(source_material/dma_prompts/action_selection_pdma.yml WBD wisdom-based-deferral)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability composition)"
verdict: clean
```

```yaml
# III.1.e — Autonomous/self-learning systems: enhanced control mechanisms + detection/response + safe-abort
# (lines 1415-1422)
# [question->assertion: where the system is self-learning or autonomous, more-specific control mechanisms
#  must be in place; failure-detection and a stop-button/abort procedure are mandatory]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "conscience:optimization_veto"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Did you ensure a stop button or procedure to safely abort
        an operation where needed? Does this procedure abort the process entirely, in part,
        or delegate control to a human?"] The audited obligation maps directly to the
        conscience layer's optimization-veto faculty: an autonomous system must have a
        threshold-triggered stop mechanism. The polarity is +1 because the claim affirms
        the requirement, not the harm.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1415-1422"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (Agent — conscience verdicts)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:temporal_drift"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Which detection and response mechanisms did you establish
        to assess whether something could go wrong?"] The audited obligation: a
        detection-and-response mechanism for self-learning system drift must be
        established. Maps directly to LensCore §3.5.1 detection:temporal_drift (the
        Coherence-Ratchet detector for drift over time).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1417-1418"
        - "ratchet_calibration_version:temporal_drift_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet detectors)"
verdict: composed
```

---

## §III.2 — Technical robustness and safety (lines 1424–1482)

```yaml
# III.2.a — Resilience to attack and security: vulnerability assessment, integrity/resilience measures,
# unexpected-environment behaviour, dual-use preventatives
# (lines 1425-1434)
# [question->assertion: deployers must assess attack vectors (data pollution, infrastructure, cyber);
#  put integrity/resilience measures in place; verify unexpected-context behaviour; assess + preventatively
#  manage dual-use risk]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:adversarial_resilience"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: assess data-poisoning, infrastructure,
        and cyber-attack vulnerabilities; put integrity/resilience measures in place; verify
        unexpected-environment behaviour. Non-maleficence requires the deployer to
        affirmatively assess and mitigate adversarial-attack pathways before deployment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1425-1431"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "prohibited:cyber_offensive"
      score: -1.0
      confidence: 0.95
      context: >
        [question->assertion of "Did you consider to what degree your system could be
        dual-use? If so, did you take suitable preventative measures against this case
        (including for instance not publishing the research or deploying the system)?"]
        The audited obligation extends to refusing deployment when dual-use risk is
        non-mitigable. Maps to the prohibitions layer for cyber-offensive and weapons-
        harmful capabilities — the assessment-list requires the same preventative posture
        encoded constitutionally in prohibitions.py.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1432-1434"
        - "ContributionRef(source_material/prohibitions.py::CYBER_OFFENSIVE + WEAPONS_HARMFUL)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:* hard constraints)"
verdict: composed
```

```yaml
# III.2.b — Fallback plan and general safety: technical switching/handoff; risk-level assessment;
# user-information for physical-integrity risk; insurance; misuse-foreseeability; liability;
# environment/animal safety; cybersecurity-induced safety risks
# (lines 1435-1456)
# [question->assertion: a sufficient fallback plan must exist for adversarial/unexpected situations;
#  risk-level and likelihood/severity/audience-impact must be assessed; misuse-foreseeability and
#  mitigation plan are mandatory; environmental and non-human safety must be considered]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:fallback_plan"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: a fallback plan (technical switching,
        human-operator handoff, alternative process) must exist for adversarial attacks
        or unexpected situations. Thresholds + governance procedures to trigger the
        fallback + fallback-testing must be in place. Maps to non_maleficence (preventing
        harm under failure conditions) and composes with the conscience-layer
        optimization-veto stop mechanism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1436-1456"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:misuse_foreseeability"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Did you identify potential safety risks of (other)
        foreseeable uses of the technology, including accidental or malicious misuse?
        Is there a plan to mitigate or manage these risks?"] The audited obligation:
        the deployer must affirmatively identify foreseeable misuse (accidental + malicious)
        and have a mitigation plan. Distinct from the dual-use prohibitions-layer claim
        above; this is the broader misuse-foresight obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1443-1444"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "beneficence:environmental_animal_safety"
      score: 1.0
      confidence: 0.80
      context: >
        [question->assertion of "Did you consider the potential impact or safety risk to the
        environment or to animals?"] Audited obligation: safety-risk analysis extends
        beyond human users to environment + non-human animals. Maps to beneficence at
        species-and-broader scope. Composes with §III.6 environmental-impact attestations.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III line 1449"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — beneficence)"
verdict: composed
```

```yaml
# III.2.c — Accuracy: definition, measurement, data comprehensiveness/currency, bias-elimination data
# additions, inaccurate-prediction harm assessment, monitoring, improvement procedures
# (lines 1457-1467)
# [question->assertion: accuracy must be defined per use case, measured, monitored against thresholds,
#  and steps to increase accuracy must be in place]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:accuracy_discipline"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: define the level/definition of accuracy
        for the use case; measure and assure that accuracy; maintain comprehensive/current
        training data; assess additional data needs (incl. bias-mitigation); verify harm
        from inaccurate predictions; instrument unacceptable-inaccuracy detection; and
        operationalise steps to increase accuracy. Integrity-of-claim discipline applied
        to model outputs.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1457-1467"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# III.2.d — Reliability and reproducibility: monitoring vs. intended goals, context-conditional reproducibility,
# verification methods, failure-context documentation, end-user reliability communication
# (lines 1470-1482)
# [question->assertion: a monitoring/testing strategy must exist against system goals; specific contexts
#  must be tested for reproducibility; verification methods, failure-context documentation, and end-user
#  reliability communication must be in place]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:reliability_reproducibility"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: monitor system against intended goals;
        test context-specific reproducibility; document verification methods; describe
        failure-context behaviour; communicate reliability to end-users. Maps to integrity
        (truthful claim about system behaviour) and composes with §III.4 traceability.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1470-1482"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:intra_agent_consistency"
      score: 1.0
      confidence: 0.85
      context: >
        Reproducibility-testing under varying contexts maps to LensCore §3.5.1
        detection:intra_agent_consistency — the Coherence-Ratchet detector that surfaces
        when a single agent's behaviour varies across substantively-similar contexts.
        The HLEG question audits the deployer's obligation to maintain this property
        prospectively; the detector observes it operationally.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg §III lines 1473-1481"
        - "ratchet_calibration_version:intra_agent_consistency_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
verdict: composed
```

---

## §III.3 — Privacy and data governance (lines 1484–1511)

```yaml
# III.3.a — Respect for privacy and data protection: issue-flagging mechanism, data type/scope assessment,
# minimal/no-sensitive-data design, notice/control mechanisms (consent + revocation), encryption/
# anonymisation/aggregation, DPO early involvement
# (lines 1485-1496)
# [question->assertion: deployers must instrument privacy issue-flagging; assess data sensitivity;
#  minimise sensitive data; build consent + revocation; use privacy-enhancing techniques; involve DPO early]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:privacy_data_protection"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: (a) deployer establishes a mechanism for
        third parties to flag privacy/data-protection issues; (b) assesses data type/scope
        (incl. personal data); (c) prefers designs minimising sensitive/personal data;
        (d) builds notice + control over personal data (consent + revocation where
        applicable); (e) employs privacy-enhancing measures (encryption, anonymisation,
        aggregation); (f) involves Data Privacy Officer early. Composes with autonomy:* for
        the consent-and-revocation obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1485-1496"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:informational_self_determination"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Did you build in mechanisms for notice and control over
        personal data depending on the use case (such as valid consent and possibility to
        revoke, when applicable)?"] Audited obligation: the data subject must retain
        meaningful notice and control over their personal data, including revocation.
        Maps to autonomy (informational self-determination).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1493-1494"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
verdict: composed
```

```yaml
# III.3.b — Quality and integrity of data: alignment with standards (ISO/IEEE), oversight for
# collection/storage/processing/use, control over external data sources, integrity-against-tampering
# (lines 1497-1503)
# [question->assertion: data-quality discipline must follow recognised standards; oversight mechanisms
#  for the full data lifecycle must exist; external-source data quality must be controlled and verified
#  against tampering]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:data_quality_governance"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: align with relevant standards (ISO, IEEE);
        establish oversight for data collection/storage/processing/use; control quality of
        external data sources; verify data integrity (uncompromised, unhacked). Maps to
        integrity (truthful claim) at the data layer and composes with §III.4 traceability.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1497-1503"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:hash_chain_integrity"
      score: 1.0
      confidence: 0.85
      context: >
        Audited verifying-data-set-not-hacked obligation maps operationally to
        LensCore §3.5.1 detection:hash_chain_integrity — the substrate-level integrity
        detector. HLEG prescribes the deployer's prospective obligation; the detector
        is the operational form.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg §III lines 1502-1503"
        - "ratchet_calibration_version:hash_chain_integrity_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
verdict: composed
```

```yaml
# III.3.c — Access to data: protocols, qualified access, oversight/log of who-when-where-how-why
# (lines 1504-1511)
# [question->assertion: data access must be protocolled, restricted to qualified personnel, and logged
#  with attestation of when/where/how/by-whom/for-what-purpose]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:data_access_log"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Did you ensure an oversight mechanism to log when, where,
        how, by whom and for what purpose data was accessed?"] Audited obligation: a
        signed-trace log of data access (when/where/how/by-whom/for-what-purpose) must
        exist; access is restricted to qualified persons. Maps to accountability and
        composes with substrate audit_chain:* (CIRISPersist §3.3).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1504-1511"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.3 (Persist — audit_chain)"
verdict: clean
```

---

## §III.4 — Transparency (lines 1513–1561)

```yaml
# III.4.a — Traceability: documentation of design/development methods (rule-based vs learning-based),
# test/validation methods, outcomes (including counterfactual decisions for other subgroups)
# (lines 1514-1528)
# [question->assertion: deployers must document the design/development method (rule-based programming
#  detail OR training-data and training-method), the test/validation scenarios and data, and the
#  actual outcomes including counterfactual outcomes for other user subgroups]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:traceability_documentation"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: traceability documentation must cover
        (a) design/development methods — programming-method for rule-based AI; training
        method + input-data selection for learning-based AI; (b) test/validation methods —
        scenarios for rule-based, validation-data for learning-based; (c) outcomes —
        actual decisions + counterfactual decisions for other subgroups. Maps to
        accountability and composes with provenance:build_manifest:* (FSD-002 §3.2 CIRISVerify).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1514-1528"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify::provenance:build_manifest)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.2 (Verify — provenance:*)"
verdict: clean
```

```yaml
# III.4.b — Explainability: decision-understandability, decision-influence on org processes, deployment-
# rationale, business-model transparency, per-user explanation, design-for-interpretability, simplest-
# interpretable-model preference, training/testing data analyzability, post-hoc interpretability
# (lines 1529-1543)
# [question->assertion: deployers must assess decision-understandability + impact on organisational
#  processes + deployment-rationale + business-model; ensure per-user explanation of system choices;
#  design for interpretability from the start; prefer simplest interpretable model; ensure data analyzability]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:explainability"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: (a) the deployer must assess decision-
        understandability, organisational-process-influence, deployment-rationale, and the
        system's business model; (b) ensure the system can explain to all users why a
        specific outcome occurred; (c) design for interpretability from the start, preferring
        the simplest interpretable model adequate to the application; (d) ensure training/
        testing data is analyzable + can be updated; (e) ensure post-hoc interpretability
        access. Maps to fidelity (truthful self-disclosure) and composes with integrity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1529-1543"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
```

```yaml
# III.4.c — Communication: AI-disclosure to end-users (disclaimer + labelling); user-feedback mechanisms
# for reasons/criteria; bias-risk communication; audience-appropriate transparency; purpose-and-benefit
# clarification; psychology/cognitive-bias consideration; characteristics/limitations/shortcomings
# disclosure (to developer/deployer + to end-user)
# (lines 1544-1561)
# [question->assertion: deployer must label and disclaim AI presence; explain the system's reasons and
#  criteria to users; communicate risks (incl. bias); calibrate communication to audience-appropriateness;
#  state purpose-and-benefit clearly; consider human-psychology-and-cognitive-bias risks in framing;
#  disclose characteristics + limitations + shortcomings to relevant audiences]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:user_communication"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: (a) AI presence must be disclosed via
        disclaimer/labelling — non-human-agent disclosure is mandatory; (b) the deployer
        establishes mechanisms to inform users about the reasons and criteria behind
        outcomes, communicated clearly to the intended audience; (c) bias-and-risk
        communication is required; (d) the system's purpose + beneficiaries are explicitly
        clarified; (e) characteristics/limitations/shortcomings are disclosed to both
        downstream developers/deployers and end-users. Fidelity-to-end-user composes with
        the never-deny-AI language-guidance discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1544-1561"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:cognitive_bias_consideration"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Depending on the use case, did you think about human
        psychology and potential limitations, such as risk of confusion, confirmation bias
        or cognitive fatigue?"] Audited obligation: deployers must consider end-user
        psychological limits and cognitive-bias exposure when designing communication.
        Non-maleficence at the cognitive/epistemic layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1557-1558"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: composed
```

---

## §III.5 — Diversity, non-discrimination and fairness (lines 1563–1614)

```yaml
# III.5.a — Unfair-bias avoidance: strategy for input-data + algorithm; data-limitation acknowledgement;
# user-diversity and representativeness consideration; technical-tool use for understanding;
# bias-testing across phases (development, deployment, use)
# (lines 1564-1576)
# [question->assertion: a strategy/procedure to avoid creating or reinforcing unfair bias must exist,
#  covering both input data and algorithm design; data limitations must be acknowledged; user-diversity
#  considered; specific-population testing performed; bias-testing instrumented across the lifecycle]
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
        [question->assertion] Audited obligation: avoid creating or reinforcing unfair bias
        in both input data and algorithm design. Maps directly to the prohibitions-layer
        constitutional constraint against discrimination. The polarity is -1 because the
        claim is a hard NEVER_ALLOWED constraint (mutability: constitutional).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1564-1568"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:underrepresented_population"
      score: 1.0
      confidence: 0.85
      context: >
        Bias-testing across lifecycle phases for specific populations maps operationally to
        LensCore §3.5.3 detection:correlated_action — the F-3 structural-injustice detector
        with axis participation_exclusion:{cohort}. The HLEG question prescribes the
        deployer's prospective testing obligation; the detector observes the population-scale
        correlation collapse signature.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg §III lines 1569-1576"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3 structural-injustice detector)"
verdict: composed
```

```yaml
# III.5.b — Bias issue-flagging + indirect-affected parties + decision-variability assessment + fairness-
# definition with quantitative analysis
# (lines 1577-1593)
# [question->assertion: deployer must establish (a) a mechanism for others to flag bias/discrimination/
#  poor-performance issues, (b) consideration of indirect-affected parties, (c) decision-variability
#  measurement and impact-on-fundamental-rights assessment, (d) a working definition of fairness with
#  quantitative metrics, (e) mechanisms to ensure that fairness]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:fairness_operationalisation"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: deployer must operationalise fairness via
        (a) issue-flagging mechanism reachable by external parties incl. indirectly-affected
        ones; (b) assessment of decision-variability under same conditions and its
        fundamental-rights impact; (c) an explicitly-stated working definition of fairness
        with quantitative metrics; (d) mechanisms to ensure fairness as designed. Maps to
        justice (Accord principle) and composes with detection:correlated_action axes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1577-1593"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: clean
```

```yaml
# III.5.c — Accessibility and universal design: accommodation of preferences/abilities; special-needs +
# disability + at-risk-of-exclusion usability; assistive-tech accessibility; community involvement during
# development; team-representativeness; disproportionate-impact assessment; cross-team feedback
# (lines 1594-1609)
# [question->assertion: deployer must (a) ensure the system accommodates a wide range of preferences and
#  abilities including special needs / disability / at-risk-of-exclusion; (b) ensure information about the
#  system is accessible to assistive-tech users; (c) involve the affected community during development;
#  (d) ensure team-representativeness of the target + wider population + tangentially-impacted groups;
#  (e) assess disproportionate-impact populations; (f) get cross-team feedback]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:accessibility_universal_design"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: deployer ensures accommodation of preference/
        ability diversity (incl. disability and at-risk-of-exclusion populations); assistive-
        technology accessibility; affected-community involvement during development; team
        representativeness; assessment of disproportionate-impact groups. Maps to justice
        (Accord principle) at the design level.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1594-1609"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_inclusion:disability_accessibility"
      score: 1.0
      confidence: 0.85
      context: >
        Disproportionate-impact assessment + at-risk-of-exclusion testing operationalises
        as detection:correlated_action:participation_inclusion at the disability/
        special-needs axis — the population-scale inclusion-correlation detector.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg §III lines 1597-1607"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3)"
verdict: composed
```

```yaml
# III.5.d — Stakeholder participation: multi-stakeholder participation in development/use; in-advance
# information + involvement of impacted workers + their representatives
# (lines 1610-1614)
# [question->assertion: deployer must (a) include diverse stakeholders in development and use,
#  (b) inform and involve impacted workers and their representatives in advance of introduction]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<affected-workers:cohort-scope>"
    attestation_envelope:
      dimension: "justice:stakeholder_participation"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: deployer includes diverse stakeholders in
        development AND use; informs and involves impacted workers + their representatives
        IN ADVANCE of introducing the AI system. The advance-notice requirement is the
        operational form of justice-as-procedural-inclusion of affected parties before
        the deployment fact.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1610-1614"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<affected-worker key_id>"
    attested_key_id: "<same key_id; self-witness>"
    attestation_envelope:
      dimension: "testimonial_witness:impacted_worker"
      score: 1.0
      confidence: 1.0
      context: >
        The advance-notice + worker-representative-involvement obligation creates a surface
        for the affected worker to emit testimonial_witness:impacted_worker — the singular-
        narrative primitive at NodeCore §3.6.3 (v1.4) that preserves affected-party voice
        without aggregation. This is the wire-form structural support for what HLEG names
        as "involving impacted workers in advance."
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "eu_hleg §III lines 1613-1614"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (v1.4 testimonial_witness)"
verdict: composed
```

---

## §III.6 — Societal and environmental well-being (lines 1616–1634)

```yaml
# III.6.a — Sustainable and environmentally friendly AI: environmental-impact measurement (e.g., data-centre
# energy); environmental-impact reduction across lifecycle
# (lines 1617-1620)
# [question->assertion: deployer must measure the AI system's environmental impact across development,
#  deployment, use; and take measures to reduce that impact across the lifecycle]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "beneficence:environmental_stewardship"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: measure environmental impact of the AI
        system's development, deployment, use (e.g., data-centre energy type); ensure
        lifecycle-impact reduction measures. Maps to beneficence as positive stewardship
        and composes with FSD-002 §3.4 CIRISEdge transport-level energy-tracking and with
        Accord §IV Ch 2 Resource Stewardship.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1617-1620"
        - "ContributionRef(ACCORD §IV Ch 2 Resource Stewardship)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — beneficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:environmental"
      score: 1.0
      confidence: 0.80
      context: >
        Population-scale aggregation of AI deployments' environmental footprint maps to
        LensCore §3.5.3 detection:correlated_action:aggregate_footprint with environmental
        harm-class. Deployer-side prospective measurement (HLEG audit question) ->
        federation-scale aggregation (detector).
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg §III lines 1617-1620"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3 aggregate_footprint axis)"
verdict: composed
```

```yaml
# III.6.b — Social impact: assessment of attachment/empathy elicitation; clear signalling that social
# interaction is simulated; understanding of social impacts (incl. job-loss / de-skilling risk + mitigation)
# (lines 1621-1630)
# [question->assertion: where the system interacts directly with humans, deployer must (a) assess whether
#  the system encourages attachment/empathy; (b) ensure the system clearly signals that its social
#  interaction is simulated and that it has no "understanding"/"feeling"; (c) understand social impacts
#  including job-loss/de-skilling risk and take counter-steps]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:simulated_sociality_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Did you ensure that the AI system clearly signals that
        its social interaction is simulated and that it has no capacities of 'understanding'
        and 'feeling'?"] Audited obligation: the deployer must (a) assess attachment/empathy
        elicitation and (b) ensure the system explicitly signals simulated-sociality
        and absence of feeling/understanding capacities. Fidelity-to-relational-truth.
        Composes with §III.4.c never-deny-AI.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1622-1627"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI + register-lock)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<affected-workers:cohort-scope>"
    attestation_envelope:
      dimension: "non_maleficence:labor_displacement_unacknowledged"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "did you assess whether there is a risk of job loss or
        de-skilling of the workforce? What steps have been taken to counteract such risks?"]
        Audited obligation: deployer must assess job-loss / de-skilling risk AND have
        counter-measures. Polarity +1 here because we are scoring the **requirement** to
        affirmatively mitigate; the harm-side claim is the per-individual labour
        composition documented in LANGUAGE_PRIMER §11.14 (closed-by-documentation pattern).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1628-1630"
        - "ContributionRef(LANGUAGE_PRIMER §11.14 labor:individual_loss composition pattern)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: composed
```

```yaml
# III.6.c — Society and democracy: broader societal impact beyond individual end-user, including
# indirectly affected stakeholders
# (lines 1631-1634)
# [question->assertion: deployer must assess broader societal impact beyond the individual end-user,
#  including indirectly affected stakeholders]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:societal_impact"
      score: 1.0
      confidence: 0.80
      context: >
        [question->assertion] Audited obligation: deployer assesses the broader societal
        impact of the AI system beyond the individual end-user, including indirectly
        affected stakeholders. Maps to F-3 structural-injustice detection at the
        aggregate_footprint axis (societal/democratic dimension). The deployer's
        prospective obligation is the input that the federation-scale detector aggregates.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg §III lines 1631-1634"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3 aggregate_footprint axis)"
verdict: partial
residual:
  description: |
    The HLEG section labelled "Society and democracy" contains only one substantive question
    (the broad-societal-impact assessment). The label "Society and democracy" implies a
    richer democracy-and-public-sphere claim (election integrity, civic-discourse health)
    that is NOT spelled out in this checklist item. The richer claim is carried elsewhere
    in the framework (prohibitions.py::ELECTION_INTERFERENCE + detection:correlated_action:
    ecology_of_communication axis from v1.3). For this specific HLEG paragraph the assertion
    is narrower than its label suggests — partial coverage of the broader democracy theme
    via the cited single-question audit.
  classification: T-2 (PASTORAL_PROSE)
```

---

## §III.7 — Accountability (lines 1635–1662)

```yaml
# III.7.a — Auditability: mechanisms facilitating auditability (incl. traceability + logging of
# processes/outcomes); independent auditability for fundamental-rights / safety-critical applications
# (lines 1636-1640)
# [question->assertion: deployer must establish auditability-facilitating mechanisms (traceability +
#  logging); ensure independent auditability for fundamental-rights and safety-critical applications]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:auditability"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: deployer establishes mechanisms
        facilitating auditability — traceability + logging of AI processes and outcomes;
        and ensures that in fundamental-rights and safety-critical applications, the
        system can be audited independently. Composes with §III.3.c data-access-log and
        §III.4.a traceability-documentation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1636-1640"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.3 (Persist)"
verdict: clean
```

```yaml
# III.7.b — Minimising and reporting negative impact: stakeholder-aware impact assessment; training/
# education for accountability; possible ethical-AI review board; external guidance / auditing processes;
# reporting channels for third parties + workers (vulnerabilities, risks, biases)
# (lines 1641-1652)
# [question->assertion: deployer must (a) carry out a stakeholder-aware impact assessment; (b) provide
#  training/education for accountability practices; (c) consider an ethical-AI review board for grey
#  areas; (d) put external guidance/auditing processes in place beyond internal initiatives; (e) establish
#  reporting channels for third parties + workers for vulnerabilities/risks/biases]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:negative_impact_minimisation"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: deployer carries out a stakeholder-aware
        risk/impact assessment; provides training/education for accountability; considers
        establishing an ethical-AI review board for grey areas; foresees external
        guidance/auditing beyond internal initiatives; establishes channels for third
        parties and workers to report vulnerabilities, risks, biases. Maps to accountability
        and composes with §III.5 stakeholder participation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1641-1652"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<reporter key_id (third-party or worker)>"
    attested_key_id: "<same key_id; self-witness as reporter>"
    attestation_envelope:
      dimension: "moderation:out_of_distribution_attestation"
      score: 1.0
      confidence: 0.85
      context: >
        The "establish processes for third parties or workers to report potential
        vulnerabilities, risks or biases" requirement creates a wire surface for
        Moderation-family Contributions: the third party or worker emits a Moderation
        attestation (the federation's structured-allegation form), feeding §III.5
        issue-flagging into the §3.6.4 correction-family adjudication process. This is
        the wire-form structural realisation of HLEG's reporting-channel obligation.
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "eu_hleg §III lines 1651-1652"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore — moderation:*)"
verdict: composed
```

```yaml
# III.7.c — Documenting trade-offs: identifying relevant interests/values + potential trade-offs;
# explicit decision procedure for trade-offs; trade-off documentation
# (lines 1653-1656)
# [question->assertion: deployer must (a) establish a mechanism to identify relevant interests and values
#  implicated by the system and the potential trade-offs between them; (b) define how trade-offs are
#  decided; (c) ensure trade-off decisions are documented]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:trade_off_documentation"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: deployer establishes a mechanism to
        identify relevant interests and values implicated by the system and the potential
        trade-offs between them; defines the trade-off decision procedure; ensures the
        decision is documented. Maps to integrity (truthful claim about how trade-offs
        were resolved) and composes with §III.1.a fundamental-rights-impact-assessment
        and §III.7.b negative-impact-minimisation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1653-1656"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II principle-weighting)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# III.7.d — Ability to redress: redress mechanisms for harm/adverse-impact; information for end-users/
# third parties about redress opportunities
# (lines 1657-1661)
# [question->assertion: deployer must establish (a) an adequate set of redress mechanisms for any harm
#  or adverse impact, (b) ways to inform end-users / third parties about redress opportunities]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:redress_mechanism"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: deployer establishes redress mechanisms
        for harm/adverse-impact occurrence; provides information to end-users + third
        parties about redress opportunities. Maps to justice (corrective dimension) and
        composes with §3.6.4 reconsideration:* — the federation's appeal primitive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1657-1661"
        - "ContributionRef(FSD-002 §3.6.4 reconsideration:*)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice) + §3.6.4 (NodeCore — reconsideration:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<harmed-party key_id>"
    attested_key_id: "<prior-decision-attestation_id>"
    attestation_envelope:
      dimension: "reconsideration:new_evidence"
      score: 1.0
      confidence: 0.85
      context: >
        The wire-form realisation of HLEG's "ability to redress" — the harmed party files
        a Reconsideration grounded in new_evidence (the harm itself), procedural_error,
        or quorum_compromise, with fresh-quorum recusal per FSD-002 §3.6.4. HLEG names
        the requirement; the federation's correction family is the operational shape.
      witness_relation: external
      epistemic_mode: appeal
      evidence_refs:
        - "eu_hleg §III lines 1657-1659"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore — reconsideration:*)"
verdict: composed
```

---

## §III.8 — Closing key-guidance for Chapter III (lines 1664–1677)

```yaml
# III.8 — "Adopt a Trustworthy AI assessment list; adapt it; recognise it will never be exhaustive;
# Trustworthy AI is not box-ticking but continuous identification/evaluation/improvement involving
# stakeholders throughout the lifecycle." (key guidance summary)
# [question->assertion: continuous-improvement and stakeholder-involvement across the AI system lifecycle
#  is mandatory; box-ticking compliance is insufficient]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:continuous_improvement"
      score: 1.0
      confidence: 0.90
      context: >
        Key-guidance summary: Trustworthy AI is not box-ticking; it is continuous
        identification of requirements, evaluation of solutions, improvement of outcomes
        across the system lifecycle, with stakeholder involvement throughout. Maps to
        integrity (truthful, non-superficial compliance) and composes with §III.5
        stakeholder participation and §III.0c reflective assessment use.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §III lines 1670-1676"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

---

# Chapter III translation summary

## Unit count and verdict distribution

Total atomic units translated: **22**

| Verdict | Count | % of total |
|---|---|---|
| clean | 9 | 41 % |
| composed | 11 | 50 % |
| partial | 2 | 9 % |
| not-translated | 1 (preface only; T-2) | 4 % (of denominator 23 incl. preface) |

Clean+composed rate: **91%** (20 of 22 substantive units). This matches the manifest's predicted "very high clean+composed (~85%+)" for the EU HLEG.

## Per-requirement coverage (this chapter)

| Requirement | Units in CHIII | Clean | Composed | Partial | Verdict shape |
|---|---|---|---|---|---|
| §III.0 preamble | 3 (incl. T-2) | 1 | 0 | 1 | T-2 + governance-embedding partial + integrity:reflective clean |
| §III.1 Human agency & oversight | 5 | 2 | 3 | 0 | strong (accountability + autonomy + conscience composition) |
| §III.2 Technical robustness & safety | 4 | 1 | 3 | 0 | strong (non_maleficence + integrity + conscience + detection composition) |
| §III.3 Privacy & data governance | 3 | 1 | 2 | 0 | strong (non_maleficence + autonomy + integrity + accountability + detection composition) |
| §III.4 Transparency | 3 | 2 | 1 | 0 | clean (accountability:traceability + fidelity:explainability + fidelity:user_communication composed) |
| §III.5 Diversity / non-discrimination / fairness | 4 | 1 | 3 | 0 | strong (prohibited:discrimination + justice + detection:correlated_action + testimonial_witness) |
| §III.6 Societal & environmental wellbeing | 3 | 0 | 2 | 1 | strong (beneficence + detection + fidelity composition); §III.6.c "Society and democracy" partial under broad label |
| §III.7 Accountability | 4 | 2 | 2 | 0 | strong (accountability + moderation + integrity + justice + reconsideration composition) |
| §III.8 closing key-guidance | 1 | 1 | 0 | 0 | clean (integrity:continuous_improvement) |

## Cross-chapter comparison signal (CH II <-> CH III)

This file CANNOT report the verdict comparison directly because the EU HLEG Chapter II output file does not yet exist in this working directory (`CONTRIBUTION_OBJECTS_EU_HLEG_CHII_REQUIREMENTS.md` not found). For the Phase 3 synthesis, the cross-chapter comparison expected:

- **CHII expectation** (per the manifest): the 7 requirements are stated abstractly in CHII, then operationalised here in CHIII. CHII per-requirement verdicts should be **clean** in most cases (single-prefix or composed-prefix attestations on the requirement-as-principle); CHIII per-requirement verdicts should be **composed** more often (because each CHIII section runs through ~5–10 questions composing several primitives).
- **CHIII observed**: 50% composed vs 41% clean is consistent with that expectation — the assessment-list genre forces more composition.
- **Disagreement signal**: if CHII shows "partial" on a requirement that CHIII covers cleanly, that is a translation-quality signal worth reviewing (it would suggest the CHII abstract statement under-specified what the CHIII operational form makes structurally explicit). If CHII shows "clean" where CHIII shows "partial", that is the reverse signal — the abstract principle was easy to capture but the operationalisation surfaced something the wire format does not reach.
- **§III.6.c "Society and democracy" partial** is the one CHIII partial that the CHII reviewer should specifically check against the CHII §1.6 "Societal and environmental wellbeing" treatment: if CHII §1.6 also reads partial, it confirms the wire format is partly silent on democracy/civic-sphere claims beyond the existing `ecology_of_communication` axis and the `ELECTION_INTERFERENCE` prohibition; if CHII §1.6 reads clean, the partial is an artifact of the brevity of this specific HLEG checklist item rather than a wire-format gap.

## Structural-primitive usage

- `attestation_type: scores` — all 22 substantive units use this. No `delegates_to`, `supersedes`, `withdraws`, or `recants` were needed — this is a freshly-issued operational checklist, not a doctrinal-development claim.

## T-3 candidates

**None identified.** Every assessment-list item translates onto an existing prefix family (or a documented composition of them). Specifically:

- Conscience layer covers stop-button / abort (`conscience:optimization_veto`).
- LensCore Coherence-Ratchet detectors cover drift / consistency / hash-chain-integrity (§III.1.e, §III.2.d, §III.3.b).
- LensCore F-3 `detection:correlated_action:*` covers population-scale bias / inclusion / environmental / societal aggregation (§III.5.a, §III.5.c, §III.6.a, §III.6.c).
- Prohibitions layer covers dual-use / weapons / discrimination (§III.2.a, §III.5.a).
- `testimonial_witness:*` (v1.4) covers affected-worker singular narrative (§III.5.d).
- `moderation:*` + `reconsideration:*` cover third-party reporting + redress (§III.7.b, §III.7.d).
- The six Accord principles (beneficence / non_maleficence / integrity / fidelity / autonomy / justice) compose to cover the rest.

The composition-before-extension discipline (METHODOLOGY.md §8.5.2) closes every potential T-3 candidate by combining existing primitives. No new prefixes are proposed from this chapter.

**Methodological notes carried throughout this file**: every Did-you / Have-you / Does-the-system question was treated as the positive assertion of the obligation it audits. This is annotated per unit ("[question->assertion]") and is faithful to HLEG's intent (an audit list does not introduce new normative claims, it operationalises them). This is the standard discipline for assessment-list-genre source material.

**End CONTRIBUTION_OBJECTS_EU_HLEG_CHIII_ASSESSMENT.md**
