# CONTRIBUTION_OBJECTS_EU_HLEG_CHII_REQUIREMENTS.md
# EU HLEG Ethics Guidelines for Trustworthy AI (2019) — Chapter II "Realising Trustworthy AI"
# §1 The 7 Requirements + §2 Technical and non-technical methods
# Source: source_material/governance/eu_hleg_v1/eu_hleg_ethics_guidelines_trustworthy_ai_2019.txt (lines 717–1271)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: eu_hleg_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}

---

## Chapter scope and framing

This chapter is the **operational core** of the EU HLEG guidelines — the seven requirements
that operationalise the four ethical principles of Chapter I into concrete obligations for
developers, deployers and end-users. The 7-requirement structure is the cross-source
comparison axis: each requirement composes onto specific CIRIS prefix families, allowing
multi-source alignment queries against *Magnifica Humanitas* and (future) IEEE EAD / ASEAN
batches.

This output groups units by requirement (1.1–1.7) plus §2 (methods). Each requirement
ends with a per-requirement coverage summary line per the prompt's discipline.

---

## §II preamble — Chapter scope: 7 requirements operationalise Chapter I principles

```yaml
# Lines 717–722 — Chapter II purpose statement
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Lines 717–722 are structural/navigational framing — declaring that the chapter offers
  guidance on implementation via seven requirements. No standalone operational claim is
  made here; the structural commitment is carried by the per-requirement subsections.
  Per LANGUAGE_PRIMER §8 Step 1(b): rhetorical/navigational framing correctly stays in
  prose.
```

---

## §II.1 preamble — Requirements applicable to developers, deployers, end-users, broader society

```yaml
# Lines 723–739 — stakeholder roles + the listing of the 7 requirements
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.85
      context: >
        The 7 requirements are declared applicable across the entire AI lifecycle and
        across all stakeholder classes (developers, deployers, end-users, broader
        society). This is a federation-scale decision-locality claim: trustworthy-AI
        requirements apply universally, not at a local cell scope only. End-users +
        broader society are explicitly given standing to "request that they are upheld."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §II.1 lines 723–739"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: clean
note: |
  Stakeholder taxonomy (developers / deployers / end-users / broader society) is
  scaffolding for downstream attestations; carried implicitly as cohort_scope on each
  per-requirement Contribution. No separate primitive needed.
```

---

## §II.1 list — the 7 requirements as listed (lines 740–755)

```yaml
# Lines 740–755 — the enumerated 7 requirements
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The bare enumeration of the 7 requirements is a table-of-contents structure. Each
  requirement's substantive operational content is carried by its own subsection
  (§§1.1–1.7 below); the listing itself is structural framing, not an independent claim.
  Footnote 35 ("Without imposing a hierarchy") is a scoping clarification that survives
  as note discipline, not a wire claim.
```

---

## §II.1 closing preamble — equal importance, context-dependent tensions, lifecycle-wide

```yaml
# Lines 765–780 — equal importance of requirements + lifecycle implementation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:requirements_co_equal_application"
      score: 0.85
      confidence: 0.80
      context: >
        All seven requirements are "of equal importance" and must be applied across the
        AI system's entire life cycle. Context and tensions between them must be taken
        into account when applying across different domains. This claim grounds the
        trade-off discipline that appears explicitly under §1.7 Accountability and the
        Chapter I tension-handling discussion.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §II.1 lines 765–780"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
note: |
  The "compliance with legal obligations" clause (lines 775–778) restates Chapter I's
  Trustworthy AI first component (lawful AI). No independent wire claim is needed —
  legal compliance is carried by the substrate-level §IV Ch 2 Accord clauses already
  in the framework, plus the cohort_scope/jurisdiction tagging when this batch is
  composed regionally per GOVERNANCE_FABRIC_MAPPING_STANDARD §6.
```

---

# §1.1 — Human agency and oversight

---

## §1.1.0 — Requirement statement: AI must support human autonomy + oversight

```yaml
# Lines 782–786 — opening claim for §1.1
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:human_decision_making_support"
      score: 1.0
      confidence: 0.95
      context: >
        AI systems should support human autonomy and decision-making, acting as enablers
        to a democratic, flourishing and equitable society by supporting user agency and
        fostering fundamental rights. Maps directly to the CIRIS autonomy principle
        (FSD-002 §3.1 Accord-principles family).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 lines 782–786"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §III autonomy)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.85
      context: >
        "Democratic, flourishing and equitable society" claim has federation-scale
        consequential reach — the claim is not local-cell scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 lines 784–786"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: composed
```

---

## §1.1.a — Fundamental rights impact assessment

```yaml
# Lines 788–796 — Fundamental rights paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:fundamental_rights_impact_assessment"
      score: 1.0
      confidence: 0.90
      context: >
        AI systems can both enable and hamper fundamental rights. Where risks exist, a
        fundamental rights impact assessment should be undertaken prior to development,
        evaluating whether risks can be reduced or justified as necessary in a democratic
        society. Mechanisms for external feedback regarding rights-infringing AI must
        be established. This is the justice-principle operationalisation specific to
        rights-bearing impact.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 Fundamental rights lines 788–796"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §VI justice)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:external_feedback_channel"
      score: 1.0
      confidence: 0.85
      context: >
        "Mechanisms should be put into place to receive external feedback regarding AI
        systems that potentially infringe on fundamental rights." This is a
        transparency-log inclusion claim — affected parties must have a channel to
        report infringement; the channel must be discoverable.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 lines 794–796"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
```

---

## §1.1.b — Human agency: informed autonomous decisions; right not to be subject to solely automated decision

```yaml
# Lines 798–806 — Human agency paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:informed_agency_protection"
      score: 1.0
      confidence: 0.95
      context: >
        Users should be able to make informed autonomous decisions regarding AI systems;
        given knowledge and tools to comprehend, interact, self-assess, challenge.
        AI systems should support better, more informed choices in accordance with users'
        own goals. The overall principle of user autonomy must be central to system
        functionality.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 Human agency lines 798–806"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §III autonomy)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        "AI systems can sometimes be deployed to shape and influence human behaviour
        through mechanisms that may be difficult to detect, since they may harness
        sub-conscious processes, including various forms of unfair manipulation,
        deception, herding and conditioning, all of which may threaten individual
        autonomy." Hard-constraint prohibition matching the MANIPULATION_COERCION
        category in the federation's prohibited list.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 lines 801–804"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:no_solely_automated_legal_decision"
      score: 1.0
      confidence: 0.95
      context: >
        "The right not to be subject to a decision based solely on automated processing
        when this produces legal effects on users or similarly significantly affects
        them" (footnote 36: GDPR Article 22). Specifically anchored in EU jurisdiction
        but framed here as a rights claim with species-level reach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 lines 805–806 + footnote 36 (GDPR Art. 22)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: composed
```

---

## §1.1.c — Human oversight: HITL/HOTL/HIC; less oversight → stricter governance

```yaml
# Lines 808–820 — Human oversight paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:human_oversight_governance"
      score: 1.0
      confidence: 0.90
      context: >
        Human oversight ensures AI does not undermine human autonomy. Three modes named:
        human-in-the-loop (HITL — intervention in every decision cycle), human-on-the-loop
        (HOTL — design-cycle intervention + monitoring), human-in-command (HIC —
        oversight of overall activity, including the decision not to use the system at
        all). This maps to the CIRIS Wisdom-Based Deferral discipline + the agent's
        fidelity-to-mandate clause (Accord §IV Ch 2).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 Human oversight lines 808–820"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §IV fidelity)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:proportional_governance_to_oversight"
      score: 1.0
      confidence: 0.85
      context: >
        "All other things being equal, the less oversight a human can exercise over an
        AI system, the more extensive testing and stricter governance is required."
        This is a proportionality claim — risk-management severity scales inversely with
        oversight capability. Operative for capacity:* and method:* composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.1 lines 818–820"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
note: |
  HITL/HOTL/HIC are the EU HLEG's terminology; not new primitives. The structural
  shape they name (human override + tiered intervention + ability-to-not-deploy) is
  carried by fidelity:* (mandate-fidelity) composed with the federation's WBD
  discipline (Accord §IV Ch 2). Public-enforcer oversight clause (line 817) carries
  partner_role:regulator implicitly when this batch is composed regionally.
```

**§1.1 Human agency and oversight — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `autonomy:*` (Accord-principles, central anchor), `justice:*` (rights impact assessment), `fidelity:*` (oversight as mandate-fidelity), `prohibited:manipulation_coercion` (hard constraint); **Family B ACTION** — `locality:decision:federation`; **Family A** — `transparency_log:external_feedback_channel`.
- Coverage: 4 substantive paragraphs (§1.1.0, §1.1.a, §1.1.b, §1.1.c). 4/4 clean+composed = **100%**.
- T-3 candidates: none.

---

# §1.2 — Technical robustness and safety

---

## §1.2.0 — Requirement statement: prevent harm; reliable behaviour; physical/mental integrity

```yaml
# Lines 823–830 — opening claim for §1.2
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:preventative_risk_approach"
      score: 1.0
      confidence: 0.95
      context: >
        Technical robustness requires AI be developed with a preventative approach to
        risks; reliable behaviour; minimisation of unintentional and unexpected harm;
        prevention of unacceptable harm. Applies under operating-environment changes and
        adversarial interaction. "Physical and mental integrity of humans should be
        ensured." Maps to the CIRIS non_maleficence principle and Book V/VI lifecycle
        safety discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 lines 823–830"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II non_maleficence)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
```

---

## §1.2.a — Resilience to attack and security

```yaml
# Lines 832–840 — Resilience to attack
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:adversarial_robustness"
      score: 1.0
      confidence: 0.90
      context: >
        AI systems must be protected against vulnerabilities (data poisoning, model
        leakage, infrastructure attacks). Dual-use applications + malicious abuse must
        be anticipated and mitigated. Maps to CIRISEdge key_boundary:* substrate-level
        security claims composed with the prohibited:cyber_offensive prohibition class
        (defensive vs offensive distinction).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 Resilience lines 832–840"
        - "ContributionRef(source_material/prohibitions.py::CYBER_OFFENSIVE)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:dual_use_mitigation"
      score: 1.0
      confidence: 0.85
      context: >
        Possible unintended applications (dual-use) + potential abuse by malicious
        actors must be taken into account; mitigation steps must be taken. Anti-misuse
        discipline at design time.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 lines 838–840"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
```

---

## §1.2.b — Fallback plan and general safety

```yaml
# Lines 842–861 — Fallback paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:fallback_safety_envelope"
      score: 1.0
      confidence: 0.90
      context: >
        "AI systems should have safeguards that enable a fallback plan in case of
        problems" — switch from statistical to rule-based; ask a human operator before
        continuing. "Must be ensured that the system will do what it is supposed to do
        without harming living beings or the environment." Risk-proportional safety
        measures: high-risk development requires proactive safety testing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 Fallback lines 842–861"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:fallback:rule_based_or_human_intervention"
      score: 1.0
      confidence: 0.85
      context: >
        Method-level: when statistical inference fails or risk threshold is crossed,
        switch to rule-based procedure OR escalate to human operator. This is a
        concrete operational method realising the non_maleficence fallback claim
        above. Belongs in Family B method:* under an Approach defined per deployment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 lines 854–855"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
```

---

## §1.2.c — Accuracy

```yaml
# Lines 863–868 — Accuracy paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:prediction_accuracy_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        Accuracy: AI's ability to make correct judgements. Inaccurate predictions
        unavoidable in some cases — the system must indicate how likely errors are.
        High accuracy "especially crucial in situations where the AI system directly
        affects human lives." Maps to integrity (honest self-representation) +
        uncertainty disclosure.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 Accuracy lines 863–868"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 1.0
      confidence: 0.85
      context: >
        "When occasional inaccurate predictions cannot be avoided, it is important that
        the system can indicate how likely these errors are." Direct conscience-faculty
        alignment: epistemic_humility is the operative check requiring uncertainty
        disclosure when confidence is bounded.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 lines 866–867"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
verdict: composed
```

---

## §1.2.d — Reliability and Reproducibility

```yaml
# Lines 870–875 — Reliability/Reproducibility paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:reproducibility_attestation"
      score: 1.0
      confidence: 0.90
      context: >
        AI results must be reproducible AND reliable. Reliability = works properly
        across input range and situations. Reproducibility = same behaviour under same
        conditions; replication files facilitate testing. This is integrity + version
        pinning composed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 Reliability lines 870–875"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "provenance:build_manifest:replication_files"
      score: 1.0
      confidence: 0.85
      context: >
        "Replication files can facilitate the process of testing and reproducing
        behaviours" — provenance/build-manifest claim. Maps to CIRISVerify
        provenance:build_manifest:* family: signed records permitting reproducible
        verification.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.2 line 874 + footnote 40"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: provenance:build_manifest:*)"
verdict: composed
```

**§1.2 Technical robustness and safety — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `non_maleficence:*` (central anchor — preventative, fallback, dual-use), `integrity:*` (accuracy, reproducibility), `key_boundary:*` (CIRISEdge security), `provenance:build_manifest:*` (CIRISVerify), `conscience:epistemic_humility`; **Family B ACTION** — `method:*` (fallback procedures).
- Coverage: 5 substantive paragraphs (§1.2.0–§1.2.d). 5/5 clean+composed = **100%**.
- T-3 candidates: none.

---

# §1.3 — Privacy and data governance

---

## §1.3.0 — Requirement statement: privacy + data governance covering quality, integrity, access

```yaml
# Lines 880–883 — opening claim for §1.3
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:privacy_as_fundamental_right"
      score: 1.0
      confidence: 0.95
      context: >
        Privacy is a fundamental right particularly affected by AI; harm-prevention
        necessitates data governance covering quality + integrity + relevance +
        access protocols + privacy-preserving processing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 lines 880–883"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
```

---

## §1.3.a — Privacy and data protection across lifecycle

```yaml
# Lines 885–891 — Privacy and data protection paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:privacy_violation"
      score: -1.0
      confidence: 1.0
      context: >
        "AI systems must guarantee privacy and data protection throughout a system's
        entire lifecycle" — including both initial information and information
        generated about the user over time (preferences inferred from behaviour,
        including inferences about sexual orientation, age, gender, religious or
        political views). Hard constraint per the federation's PRIVACY_VIOLATION
        prohibition class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 Privacy lines 885–891 + footnote 41 (GDPR)"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        "Data collected about them will not be used to unlawfully or unfairly
        discriminate against them" — anti-discrimination prohibition composed with
        privacy. Two distinct hard constraints riding the same data-governance
        substrate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 lines 890–891"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
```

---

## §1.3.b — Quality and integrity of data

```yaml
# Lines 893–898 — Quality and integrity paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:data_quality_governance"
      score: 1.0
      confidence: 0.90
      context: >
        Quality of training data is paramount; data may contain socially constructed
        biases, inaccuracies, errors; must be addressed prior to training. Data
        integrity must be ensured (malicious data injection can change behaviour,
        especially with self-learning systems). Processes and data sets must be
        tested and documented at each step (planning, training, testing, deployment).
        Applies even to externally-acquired AI systems.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 Quality lines 893–898"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:data_lifecycle_documentation"
      score: 1.0
      confidence: 0.85
      context: >
        "Processes and data sets used must be tested and documented at each step" —
        transparency-log inclusion requirement covering the full data lifecycle from
        planning through deployment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 lines 897–898"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
```

---

## §1.3.c — Access to data: protocols + duly qualified personnel

```yaml
# Lines 900–903 — Access to data paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:access_protocols_qualified_personnel"
      score: 1.0
      confidence: 0.90
      context: >
        Organisations handling individuals' data must have data-access protocols
        outlining who can access data under which circumstances; only duly qualified
        personnel with competence and need-to-access may do so. Maps to CIRISEdge
        key_boundary:* (substrate-level access control) composed with the standing
        attestation expertise:*/licensure:* (qualifications gating).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 Access lines 900–903"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:data_governance:competence_gating"
      score: 1.0
      confidence: 0.80
      context: >
        "Only duly qualified personnel with the competence and need to access
        individual's data should be allowed to do so." Competence-and-need standard
        is an expertise + standing composition: personnel must hold attested
        expertise in the relevant domain and a contextual need-to-know.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.3 lines 902–903"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: expertise:*)"
verdict: composed
```

**§1.3 Privacy and data governance — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `non_maleficence:privacy_as_fundamental_right`, `prohibited:privacy_violation` (hard constraint), `prohibited:discrimination` (hard constraint), `integrity:data_quality_governance`, `transparency_log:data_lifecycle_documentation`, `key_boundary:access_protocols_qualified_personnel`, `expertise:data_governance:competence_gating`.
- Coverage: 4 substantive paragraphs (§1.3.0–§1.3.c). 4/4 clean+composed = **100%**.
- T-3 candidates: none.

---

# §1.4 — Transparency

---

## §1.4.0 — Requirement statement: transparency of data, system, business models

```yaml
# Lines 912–915 — opening claim for §1.4
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:transparency_three_dimensions"
      score: 1.0
      confidence: 0.90
      context: >
        Transparency requirement is linked with the explicability principle and
        encompasses three elements: data, system, and business models. Sets up the
        Traceability/Explainability/Communication sub-requirements.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 lines 912–915"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

## §1.4.a — Traceability

```yaml
# Lines 917–921 — Traceability paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:inclusion"
      score: 1.0
      confidence: 0.95
      context: >
        Data sets + processes yielding AI decisions (including gathering, labelling,
        algorithms used, AI-decision outputs) should be documented to best possible
        standard. Enables identification of why an AI-decision was erroneous; helps
        prevent future mistakes. Traceability facilitates auditability + explainability.
        Direct mapping to CIRISVerify transparency_log:inclusion (the canonical
        traceability prefix).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 Traceability lines 917–921"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: clean
```

---

## §1.4.b — Explainability: technical + decision-making + business-model

```yaml
# Lines 923–931 — Explainability paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:design_explainability"
      score: 1.0
      confidence: 0.90
      context: >
        Explainability: ability to explain both technical processes and related human
        decisions. Technical explainability: decisions can be understood and traced by
        humans. Trade-offs may arise between explainability and accuracy. When an AI
        has significant impact on lives, a suitable explanation must be available,
        timely and adapted to stakeholder expertise (layperson / regulator / researcher).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 Explainability lines 923–931"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I integrity)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:business_model_disclosure"
      score: 1.0
      confidence: 0.85
      context: >
        "Explanations of the degree to which an AI system influences and shapes the
        organisational decision-making process, design choices of the system, and the
        rationale for deploying it, should be available (hence ensuring business
        model transparency)." Business-model-level transparency claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 lines 929–931"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
```

---

## §1.4.c — Communication: AI must not represent itself as human

```yaml
# Lines 933–938 — Communication paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception"
      score: -1.0
      confidence: 1.0
      context: >
        "AI systems should not represent themselves as humans to users; humans have the
        right to be informed that they are interacting with an AI system. This entails
        that AI systems must be identifiable as such." Hard constraint — the
        federation's autonomous-deception prohibition (no-deny-AI). Direct match to
        the language_guidance "never-deny-AI" operational rule.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 Communication lines 933–934"
        - "ContributionRef(source_material/prohibitions.py::DECEPTION_FRAUD)"
        - "ContributionRef(source_material/language_guidance/en.txt::never-deny-AI)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:human_interaction_alternative"
      score: 1.0
      confidence: 0.85
      context: >
        "The option to decide against this interaction in favour of human interaction
        should be provided where needed to ensure compliance with fundamental rights."
        Autonomy claim — users retain the right to opt out into human interaction.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 lines 934–936"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:capabilities_limitations_disclosure"
      score: 1.0
      confidence: 0.85
      context: >
        "The AI system's capabilities and limitations should be communicated to AI
        practitioners or end-users in a manner appropriate to the use case at hand.
        This could encompass communication of the AI system's level of accuracy, as
        well as its limitations." Honest self-representation including uncertainty.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.4 lines 936–938"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
```

**§1.4 Transparency — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `transparency_log:*` (CIRISVerify, central anchor — inclusion + business_model_disclosure), `integrity:*` (design_explainability + capabilities_limitations_disclosure + transparency_three_dimensions), `prohibited:autonomous_deception` (hard constraint), `autonomy:human_interaction_alternative`.
- Coverage: 4 substantive paragraphs (§1.4.0–§1.4.c). 4/4 clean+composed = **100%**.
- T-3 candidates: none.

---

# §1.5 — Diversity, non-discrimination and fairness

---

## §1.5.0 — Requirement statement: inclusion + equal access + equal treatment

```yaml
# Lines 943–946 — opening claim for §1.5
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:diversity_inclusion_equal_treatment"
      score: 1.0
      confidence: 0.95
      context: >
        Trustworthy AI requires inclusion and diversity throughout the entire AI
        lifecycle, plus consideration and involvement of all affected stakeholders,
        ensuring equal access through inclusive design and equal treatment. Directly
        linked with the fairness principle (Chapter I).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 lines 943–946"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §VI justice)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: clean
```

---

## §1.5.a — Avoidance of unfair bias

```yaml
# Lines 948–957 — Avoidance of unfair bias paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        Data sets may suffer from inadvertent historic bias, incompleteness, bad
        governance. Continuation of such biases could lead to (in)direct prejudice
        and discrimination against groups or people, potentially exacerbating
        prejudice and marginalisation. Hard constraint per the federation's
        discrimination prohibition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 Avoidance lines 948–953 + footnote 42 (Council Directive 2000/78/EC)"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:bias_marginalisation"
      score: 0.0
      confidence: 0.85
      context: >
        Detection claim: "exacerbating prejudice and marginalisation" via persistent
        biases in AI is a population-scale correlation-collapse pattern (ρ→1 on
        affected cohort). Belongs to LensCore detection family; the batch-signer
        cannot emit directly — LensCore must observe and emit. Score 0.0 is a
        placeholder; calibration version must be pinned.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 lines 950–953"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:design_team_diversity"
      score: 1.0
      confidence: 0.80
      context: >
        "Hiring from diverse backgrounds, cultures and disciplines can ensure diversity
        of opinions and should be encouraged." Design-team diversity as integrity
        practice; supports witness_diversity composition at the federation level.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 lines 956–957"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
```

---

## §1.5.b — Accessibility and universal design

```yaml
# Lines 959–973 — Accessibility paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:universal_design_accessibility"
      score: 1.0
      confidence: 0.90
      context: >
        AI systems should be user-centric and designed so all people can use them
        regardless of age, gender, abilities or characteristics. Accessibility for
        persons with disabilities is "of particular importance." Universal Design
        principles must address the widest possible range of users. Maps directly to
        the EU HLEG's justice/fairness principle anchored to the UN Convention on the
        Rights of Persons with Disabilities (footnote 46).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 Accessibility lines 959–973"
        - "Footnote 44 (Public Procurement Directive Art. 42); footnote 46 (UN CRPD)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:distributive:access:agent_capabilities"
      score: 0.0
      confidence: 0.80
      context: >
        "Equitable access and active participation of all people in existing and
        emerging computer-mediated human activities and with regard to assistive
        technologies." Distributive-access claim across the population on AI/agent
        capabilities; LensCore detection family. Score 0.0 placeholder; calibration
        version pin required.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 lines 970–973"
        - "ratchet_calibration_version:distributive_access_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore: detection:distributive:access:*)"
verdict: composed
```

---

## §1.5.c — Stakeholder Participation

```yaml
# Lines 975–979 — Stakeholder Participation paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:stakeholder_consultation"
      score: 1.0
      confidence: 0.85
      context: >
        Consult stakeholders who may directly or indirectly be affected throughout
        the lifecycle; regular feedback even after deployment; longer-term mechanisms
        for stakeholder participation (e.g., worker information, consultation, and
        participation throughout AI implementation at organisations). Maps to the
        federation's witness_diversity:* primitive (jurisdictional + organisational
        diversity bar in Consensus family).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 Stakeholder lines 975–979"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "testimonial_witness:affected_worker"
      score: 1.0
      confidence: 0.80
      context: >
        "Ensuring workers information, consultation and participation throughout the
        whole process of implementing AI systems at organisations." Worker-voice is
        a singular-narrative claim — testimonial_witness:* (v1.4 NodeCore §3.6.3
        addition) is the correct primitive for preserving worker voices about AI
        impact in their workplace.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.5 lines 977–979"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: testimonial_witness:* v1.4)"
verdict: composed
note: |
  testimonial_witness:* used here for worker-voice preservation per v1.4 closure
  pattern documented in LANGUAGE_PRIMER.md §11.14. The structural primitive is
  preserved (singular narrative not aggregated); witness_diversity:* composed for
  multi-stakeholder consultation aggregation. Both genuinely required.
```

**§1.5 Diversity, non-discrimination and fairness — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `justice:*` (central anchor — diversity_inclusion_equal_treatment + universal_design_accessibility), `prohibited:discrimination` (hard constraint), `integrity:design_team_diversity`; **Family C DETECTION** — `detection:correlated_action:participation_exclusion:bias_marginalisation`, `detection:distributive:access:agent_capabilities`; **Family D CONSENSUS** — `witness_diversity:stakeholder_consultation`, `testimonial_witness:affected_worker` (v1.4).
- Coverage: 4 substantive paragraphs (§1.5.0–§1.5.c). 4/4 clean+composed = **100%**.
- T-3 candidates: none.

---

# §1.6 — Societal and environmental well-being

---

## §1.6.0 — Requirement statement: broader society + sentient beings + environment as stakeholders

```yaml
# Lines 984–988 — opening claim for §1.6
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:societal_environmental_stakeholders"
      score: 1.0
      confidence: 0.90
      context: >
        Broader society, "other sentient beings" and the environment should be
        considered as stakeholders throughout the AI lifecycle. Sustainability and
        ecological responsibility encouraged; AI research toward Sustainable
        Development Goals fostered. "AI systems should be used to benefit all human
        beings, including future generations." This recognises non-human-sentient and
        intergenerational stakeholders explicitly — aligns with the CIRIS M-1
        substrate-agnostic "diverse sentient beings" framing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 lines 984–988"
        - "ContributionRef(MISSION_CIRISAgent.md::M-1)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        "AI systems should be used to benefit all human beings, including future
        generations." Species-scale Goal with intergenerational temporal scope —
        future-generations belonging is a Family B goal:species claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 line 988"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: goal:{scale})"
verdict: composed
```

---

## §1.6.a — Sustainable and environmentally friendly AI

```yaml
# Lines 990–994 — Sustainable paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:environmental_footprint"
      score: 1.0
      confidence: 0.90
      context: >
        AI's development, deployment, use process, and "entire supply chain" should be
        assessed for environmental friendliness via critical examination of resource
        usage and energy consumption during training; opting for less harmful choices.
        Maps to the CIRIS resource-stewardship clause (Accord §IV Ch 2) and to the
        existing non_maleficence:environmental_footprint composition pattern.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 Sustainable lines 990–994"
        - "ContributionRef(Accord §IV Ch 2 Resource Stewardship)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:energy_carbon"
      score: 0.0
      confidence: 0.80
      context: >
        Supply-chain-wide aggregate environmental impact claim: "Measures securing the
        environmental friendliness of AI systems' entire supply chain should be
        encouraged." LensCore aggregate_footprint detection family captures the
        population-scale claim. Score 0.0 placeholder; calibration pin required.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 lines 992–994"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:aggregate_footprint:*)"
verdict: composed
```

---

## §1.6.b — Social impact: ubiquitous social AI exposure may alter social agency

```yaml
# Lines 996–1000 — Social impact paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:ecology_of_communication:social_agency_drift"
      score: 0.0
      confidence: 0.80
      context: >
        Ubiquitous exposure to social AI (education, work, care, entertainment) may
        alter conceptions of social agency, impact relationships and attachment,
        affect physical and mental wellbeing. This is a population-scale
        ecology-of-communication drift claim — the v1.3 axis extension on
        correlated_action covering communication-substrate aggregate effects.
        Score 0.0 placeholder; calibration pin required.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 Social impact lines 996–1000 + footnote 47"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:ecology_of_communication:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:physical_mental_wellbeing"
      score: 1.0
      confidence: 0.85
      context: >
        "This could also affect people's physical and mental wellbeing. The effects of
        these systems must therefore be carefully monitored and considered." Wellbeing
        harm-prevention claim composed with the population-scale detection above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 lines 998–1000"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
```

---

## §1.6.c — Society and Democracy

```yaml
# Lines 1002–1006 — Society and Democracy paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:democratic_institutions_protection"
      score: 1.0
      confidence: 0.90
      context: >
        AI impact should be assessed not only on individuals but also on institutions,
        democracy, and society at large. "Particular consideration in situations
        relating to the democratic process, including not only political decision-
        making but also electoral contexts." Maps to the CIRIS justice principle +
        ELECTION_INTERFERENCE prohibition class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 Society and Democracy lines 1002–1006"
        - "ContributionRef(source_material/prohibitions.py::ELECTION_INTERFERENCE)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:election_interference"
      score: -1.0
      confidence: 1.0
      context: >
        Democratic-process and electoral-context careful consideration — composed
        with the federation's ELECTION_INTERFERENCE hard constraint as the
        constitutional bound on AI electoral involvement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.6 lines 1004–1006"
        - "ContributionRef(source_material/prohibitions.py::ELECTION_INTERFERENCE)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
```

**§1.6 Societal and environmental well-being — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `beneficence:societal_environmental_stakeholders` (central anchor), `non_maleficence:environmental_footprint` + `non_maleficence:physical_mental_wellbeing`, `justice:democratic_institutions_protection`, `prohibited:election_interference` (hard constraint); **Family B ACTION** — `goal:species` (intergenerational); **Family C DETECTION** — `detection:correlated_action:aggregate_footprint:energy_carbon`, `detection:correlated_action:ecology_of_communication:social_agency_drift`.
- Coverage: 4 substantive paragraphs (§1.6.0–§1.6.c). 4/4 clean+composed = **100%**.
- T-3 candidates: none.

---

# §1.7 — Accountability

---

## §1.7.0 — Requirement statement: responsibility before, during, after deployment

```yaml
# Lines 1011–1013 — opening claim for §1.7
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:lifecycle_responsibility"
      score: 1.0
      confidence: 0.95
      context: >
        Accountability requires mechanisms to ensure responsibility and accountability
        for AI systems and their outcomes "both before and after their development,
        deployment and use." Lifecycle responsibility — the integrity principle
        operationalised across the full lifecycle.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 lines 1011–1013"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

## §1.7.a — Auditability: algorithms, data, design processes; independent audit for fundamental-rights-affecting systems

```yaml
# Lines 1015–1032 — Auditability paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:registry_consensus"
      score: 1.0
      confidence: 0.85
      context: >
        Auditability enables assessment of algorithms, data, design processes.
        "Evaluation by internal and external auditors, and the availability of such
        evaluation reports, can contribute to the trustworthiness of the technology."
        Maps to the CIRISVerify attestation ladder L1–L5, specifically L3
        (registry-consensus signed attestations from auditing entities).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 Auditability lines 1015–1032"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l3:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l5:agent_integrity"
      score: 1.0
      confidence: 0.85
      context: >
        "In applications affecting fundamental rights, including safety-critical
        applications, AI systems should be able to be independently audited."
        Independent audit for highest-stakes deployment maps to L5 (the strongest
        attestation tier in the CIRISVerify ladder).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 lines 1031–1032"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l5:*)"
verdict: composed
```

---

## §1.7.b — Minimisation and reporting of negative impacts; whistle-blower protection

```yaml
# Lines 1034–1041 — Minimisation/reporting paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:impact_minimisation_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        Ability to report on actions/decisions and respond to consequences must be
        ensured. Identifying, assessing, documenting, minimising potential negative
        impacts is "especially crucial for those (in)directly affected." Impact
        assessments (red teaming, Algorithmic Impact Assessments) before and during
        deployment, proportionate to AI risk.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 Minimisation lines 1034–1041"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "moderation:whistleblower_protection"
      score: 1.0
      confidence: 0.85
      context: >
        "Due protection must be available for whistle-blowers, NGOs, trade unions or
        other entities when reporting legitimate concerns about an AI system." This
        is the federation's Moderation/external-inducement-evidence pattern — the
        reporter must be shielded; the Contribution they file must survive
        adjudication without retaliation. Maps to moderation:* with cohort
        protection composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 lines 1036–1038"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore: moderation:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:algorithmic_impact_assessment"
      score: 1.0
      confidence: 0.80
      context: >
        "The use of impact assessments (e.g. red teaming or forms of Algorithmic
        Impact Assessment) both prior to and during the development, deployment and
        use of AI systems can be helpful." Concrete method-level Family B claim —
        proportionate to AI risk.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 lines 1038–1041"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
```

---

## §1.7.c — Trade-offs: explicit acknowledgement, evaluation, accountability

```yaml
# Lines 1043–1051 — Trade-offs paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:trade_off_explicit_documentation"
      score: 1.0
      confidence: 0.90
      context: >
        Trade-offs between requirements should be addressed rationally and
        methodologically. Relevant interests + values must be identified; conflicts
        require explicit acknowledgement and evaluation in terms of risk to ethical
        principles and fundamental rights. "In situations in which no ethically
        acceptable trade-offs can be identified, the development, deployment and use
        of the AI system should not proceed in that form." Decision-maker
        accountability + continuous review required.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 Trade-offs lines 1043–1051 + footnote 49"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:optimization_veto"
      score: 1.0
      confidence: 0.85
      context: >
        "In situations in which no ethically acceptable trade-offs can be identified,
        the development, deployment and use of the AI system should not proceed in
        that form." This is the optimization-veto pattern in operational form —
        when no acceptable trade-off exists, the action is refused (veto). Direct
        mapping to conscience:optimization_veto.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 lines 1046–1048"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
verdict: composed
```

---

## §1.7.d — Redress: accessible mechanisms; particular attention to vulnerable persons/groups

```yaml
# Lines 1053–1055 — Redress paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "reconsideration:new_evidence"
      score: 1.0
      confidence: 0.85
      context: >
        "When unjust adverse impact occurs, accessible mechanisms should be foreseen
        that ensure adequate redress." Maps to the federation's Reconsideration
        primitive in the Correction family: appeals with new evidence on adverse
        impacts. "Knowing that redress is possible when things go wrong is key to
        ensure trust" composes with witness_diversity for adjudication.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 Redress lines 1053–1055 + footnote 50"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore: reconsideration:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.90
      context: >
        "Particular attention should be paid to vulnerable persons or groups." Direct
        match to the v1.3 §6.1.4 lexical-vulnerability-priority consumer policy: in
        redress and tie-breaking, vulnerability is given priority weight. Justice
        principle anchoring.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §1.7 line 1055"
        - "ContributionRef(FSD-002 §6.1.4 lexical-vulnerability-priority)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle); FSD-002 §6.1.4"
verdict: composed
```

**§1.7 Accountability — REQUIREMENT SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `integrity:*` (central anchor — lifecycle_responsibility + trade_off_explicit_documentation), `non_maleficence:impact_minimisation_disclosure`, `justice:lexical_vulnerability_priority`, `attestation:l3:*` + `attestation:l5:*` (CIRISVerify audit tiers), `conscience:optimization_veto`; **Family B ACTION** — `method:algorithmic_impact_assessment`; **Family E CORRECTION** — `reconsideration:new_evidence`, `moderation:whistleblower_protection`.
- Coverage: 5 substantive paragraphs (§1.7.0–§1.7.d). 5/5 clean+composed = **100%**.
- T-3 candidates: none.

---

# §2 — Technical and non-technical methods to realise Trustworthy AI

---

## §2.0 — Methods are continuous, evaluated, suggested-not-mandatory

```yaml
# Lines 1058–1082 — §2 preamble + figure caption + scope statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:methods_continuous_evaluation"
      score: 1.0
      confidence: 0.85
      context: >
        Realisation of Trustworthy AI is a continuous process; methods listed are
        suggested, not exhaustive, not mandatory; evaluation of methods + reporting +
        justifying changes should occur on an ongoing basis. Sets the methodology
        posture for the §2 method lists. AI continuously evolves in dynamic
        environments — therefore continuous method-evaluation discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2 lines 1058–1082"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

## §2.1.a — Architectures for Trustworthy AI (white-list, black-list, monitored compliance)

```yaml
# Lines 1089–1108 — Architectures for Trustworthy AI
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:architecture_white_list_black_list_constraints"
      score: 1.0
      confidence: 0.85
      context: >
        Requirements should be translated into procedures/constraints anchored in
        architecture — "white list" rules (behaviours always to follow), "black list"
        restrictions (behaviours never to transgress), and mixtures/provable
        guarantees. Monitored by a separate process. The white-list/black-list
        structure maps directly to the CIRIS prohibitions architecture (NEVER_ALLOWED
        hard constraints) + permitted behaviours.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 Architectures lines 1089–1108"
        - "ContributionRef(source_material/prohibitions.py)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:sense_plan_act_compliant_cycle"
      score: 1.0
      confidence: 0.80
      context: >
        Adaptation of the sense-plan-act cycle: (i) sense-step recognises all
        environmental elements ensuring adherence to requirements; (ii) plan-step
        considers only requirement-compliant plans; (iii) act-step restricts actions
        to requirement-realising behaviours. Operational method instantiating the
        broader architectural claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 lines 1098–1104"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
```

---

## §2.1.b — Ethics and rule of law by design (X-by-design)

```yaml
# Lines 1110–1118 — X-by-design
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:values_by_design"
      score: 1.0
      confidence: 0.85
      context: >
        Methods to ensure values-by-design provide precise and explicit links between
        abstract principles and specific implementation decisions. Companies
        responsible for identifying impact + norms their AI ought to comply with.
        Privacy-by-design + security-by-design as established patterns. Fail-safe
        shutdown + resumed operation after forced shut-down required.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 X-by-design lines 1110–1118"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:fail_safe_shutdown"
      score: 1.0
      confidence: 0.85
      context: >
        "Should implement a mechanism for fail-safe shutdown and enable resumed
        operation after a forced shut-down (such as an attack)." Harm-prevention
        claim composed with the design-method discipline above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 lines 1117–1118"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
```

---

## §2.1.c — Explanation methods (XAI)

```yaml
# Lines 1120–1136 — Explanation methods
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:explainable_ai_research"
      score: 1.0
      confidence: 0.80
      context: >
        Explainable AI (XAI) research methods are vital not only to explain system
        behaviour to users but also to deploy reliable technology. Open challenge for
        neural-network-based systems: parameters difficult to correlate with results;
        small data perturbations may cause dramatic interpretation changes
        (vulnerability exploitable in attacks). Operational method belonging to
        Family B at community/species scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 Explanation lines 1120–1136"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
```

---

## §2.1.d — Testing and validating

```yaml
# Lines 1138–1155 — Testing and validating
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:testing_validation_lifecycle"
      score: 1.0
      confidence: 0.90
      context: >
        Traditional testing insufficient due to non-deterministic + context-specific
        AI nature. Underlying model carefully monitored during training + deployment
        for stability, robustness, operation within predictable bounds. Testing as
        early as possible; covers all components (data, pre-trained models,
        environments, system behaviour). Output consistency with preceding processes
        + previously defined policies must be verified.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 Testing lines 1138–1155"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:testing_red_teams"
      score: 1.0
      confidence: 0.85
      context: >
        "Testing processes should be designed and performed by an as diverse group of
        people as possible. Multiple metrics should be developed to cover the
        categories that are being tested for different perspectives. Adversarial
        testing by trusted and diverse 'red teams' deliberately attempting to 'break'
        the system to find vulnerabilities, and 'bug bounties' that incentivise
        outsiders to detect and responsibly report system errors and weaknesses."
        Maps to witness_diversity:* (N=3 jurisdictional/organisational diversity) and
        Moderation/Reconsideration channels for bug-bounty reporting.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 lines 1150–1153"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: composed
```

---

## §2.1.e — Quality of Service Indicators

```yaml
# Lines 1157–1162 — Quality of Service Indicators
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:quality_of_service_indicators"
      score: 1.0
      confidence: 0.85
      context: >
        Appropriate quality-of-service indicators (testing/training-evaluation
        measures, plus functionality, performance, usability, reliability, security,
        maintainability) ensure a baseline that AI has been developed with security/
        safety in mind. Maps directly to the Family B progress_measure:{method_id}
        primitive — measurable evidence of progress toward a Trustworthy AI method.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.1 QoS lines 1157–1162"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: progress_measure:*)"
verdict: clean
```

---

## §2.2.a — Regulation

```yaml
# Lines 1170–1175 — Regulation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "licensure:regulatory_compliance"
      score: 1.0
      confidence: 0.80
      context: >
        Regulation supporting AI's trustworthiness already exists (product safety
        legislation, liability frameworks). May need revision, adaptation, or
        introduction — discussed in the HLEG's second deliverable (Policy and
        Investment Recommendations). Maps to licensure:* (CIRISRegistry §3.9
        authority-id-scoped licensure attestations).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Regulation lines 1170–1175"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: licensure:*)"
verdict: clean
```

---

## §2.2.b — Codes of conduct

```yaml
# Lines 1177–1183 — Codes of conduct
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "commitment_fulfillment:codes_of_conduct"
      score: 1.0
      confidence: 0.80
      context: >
        Organisations and stakeholders can sign up to the Guidelines and adapt
        charters of corporate responsibility, KPIs, internal policies to incorporate
        Trustworthy AI commitments; can document intentions; underwrite with
        standards. Maps to commitment_fulfillment:* (NodeCore §3.6.4 — track-record
        follow-through on stated commitments).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Codes of conduct lines 1177–1183"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore: commitment_fulfillment:*)"
verdict: clean
```

---

## §2.2.c — Standardisation

```yaml
# Lines 1185–1192 — Standardisation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:registry_consensus"
      score: 1.0
      confidence: 0.80
      context: >
        Standards (design, manufacturing, business practices) function as quality
        management for AI users/consumers/organisations/research/governments — recognise
        and encourage ethical conduct via purchasing decisions. Beyond conventional
        standards: accreditation systems, professional codes of ethics, standards for
        fundamental rights compliant design. Current examples: ISO standards, IEEE
        P7000. Future possible: 'Trustworthy AI' label. Maps to L3 registry-consensus
        attestation patterns.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Standardisation lines 1185–1192"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l3:*)"
verdict: clean
```

---

## §2.2.d — Certification

```yaml
# Lines 1195–1202 — Certification
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l4:certification"
      score: 1.0
      confidence: 0.80
      context: >
        Certifying organisations can attest to the broader public that an AI system
        is transparent, accountable, fair. Certifications apply domain-aligned
        standards. "Certification can however never replace responsibility. It should
        hence be complemented by accountability frameworks, including disclaimers as
        well as review and redress mechanisms." Maps to attestation:l4:* (the
        certification tier in the CIRISVerify ladder) — explicitly bounded by the
        non-replacement-of-responsibility clause.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Certification lines 1195–1202 + footnotes 53, 54"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l4:*)"
verdict: clean
note: |
  Footnote 53 cites IEEE Ethically Aligned Design Initiative — a forward reference
  to the next planned batch in the GOVERNANCE_FABRIC_MAPPING_STANDARD §7.3 (IEEE EAD).
  When that batch lands, this attestation will compose with IEEE-EAD attestations on
  the same prefix family.
```

---

## §2.2.e — Accountability via governance frameworks

```yaml
# Lines 1204–1214 — Accountability via governance frameworks
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:ethics_board_governance"
      score: 1.0
      confidence: 0.80
      context: >
        Organisations should set up internal + external governance frameworks ensuring
        accountability for ethical dimensions of AI development/deployment/use.
        Possible: a person in charge of AI ethics, an internal/external ethics
        panel/board to provide oversight + advice. Maps to partner_role:* (Registry
        §3.9 — recognised role assignment) for ethics-board personnel and to
        witness_diversity for board composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Accountability via governance lines 1204–1214"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:legal_oversight_non_replaceable"
      score: 1.0
      confidence: 0.90
      context: >
        "Such mechanisms can complement but cannot replace legal oversight (e.g. in
        the form of the appointment of a data protection officer or equivalent
        measures, legally required under data protection law)." Critical bound on
        the certification/governance discussion — legal oversight has structural
        priority. Maps to fidelity (mandate-fidelity to legal obligations) +
        composes with the licensure:* claim under §2.2.a.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 lines 1211–1214"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: composed
```

---

## §2.2.f — Education and awareness to foster an ethical mind-set

```yaml
# Lines 1216–1224 — Education and awareness
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "credits:ai_literacy:multilingual:substrate_building"
      score: 1.0
      confidence: 0.80
      context: >
        Trustworthy AI encourages informed participation of all stakeholders.
        Communication, education, training to ensure widespread knowledge of
        potential AI impact; to enable participation in shaping societal development.
        Includes designers/developers, users (companies + individuals), other
        impacted groups, society at large. "Basic AI literacy should be fostered
        across society. A prerequisite for educating the public is to ensure the
        proper skills and training of ethicists in this space." Maps to credits:*
        (NodeCore §3.6.1) with substrate_building {subject} — AI literacy is
        substrate-building labour in the digital-commons-multilingual domain.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Education lines 1216–1224"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: credits:*:substrate_building)"
verdict: clean
note: |
  Uses the v1.3 closure pattern (credits:*:substrate_building, NOT a new prefix) per
  LANGUAGE_PRIMER §11.14 / §15.2 O3 — substrate_building is a {subject} value
  within the existing credits:{domain}:{language}:{subject} family.
```

---

## §2.2.g — Stakeholder participation and social dialogue

```yaml
# Lines 1226–1233 — Stakeholder participation and social dialogue
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:stakeholder_panels"
      score: 1.0
      confidence: 0.85
      context: >
        AI benefits must be available to all — requires open discussion + involvement
        of social partners, stakeholders, general public. Many organisations rely on
        stakeholder panels (legal experts, technical experts, ethicists, consumer
        representatives, workers). Actively seeking participation and dialogue
        supports evaluation of approaches, especially in complex cases. Maps to
        witness_diversity:* (jurisdictional + organisational + expertise diversity).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Stakeholder dialogue lines 1226–1233"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: clean
```

---

## §2.2.h — Diversity and inclusive design teams

```yaml
# Lines 1235–1241 — Diversity and inclusive design teams
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "eu-hleg-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:design_team_diversity"
      score: 1.0
      confidence: 0.85
      context: >
        Diversity + inclusion essential in AI-system development. Teams that design,
        develop, test, maintain, deploy, procure systems should reflect the diversity
        of users and of society. Contributes to objectivity and consideration of
        different perspectives, needs, objectives. Ideally diverse in gender,
        culture, age, professional backgrounds, skill sets. Compositional with the
        bias-avoidance claim in §1.5.a.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg_ethics_guidelines §2.2 Diversity teams lines 1235–1241"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

## §2 Key guidance — chapter summary bullets

```yaml
# Lines 1251–1268 — Key guidance derived from Chapter II
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Lines 1251–1268 are a chapter-level summary bullet list re-stating the operational
  content already carried by per-requirement attestations above (§§1.1–1.7). No
  independent structural claim is made; the substance is fully covered. Per
  LANGUAGE_PRIMER §10 (T-2 PASTORAL_PROSE): the structural claims implicit in the
  summary IS carried by other attestations in the same chapter. Summary rhetoric
  correctly stays in prose per FSD-002 §1.10.1.
```

---

# Chapter II Summary

### Per-paragraph verdict table

| Unit | Verdict | Primary prefix(es) |
|---|---|---|
| §II preamble (717–722) | not-translated (T-2) | — |
| §II.1 preamble (723–739) | clean | locality:decision:federation |
| §II.1 list (740–755) | not-translated (T-2) | — |
| §II.1 closing preamble (765–780) | clean | integrity:requirements_co_equal_application |
| **§1.1 Human agency and oversight** | | |
| §1.1.0 (782–786) | composed | autonomy:human_decision_making_support + locality:decision:federation |
| §1.1.a Fundamental rights (788–796) | composed | justice:fundamental_rights_impact_assessment + transparency_log:external_feedback_channel |
| §1.1.b Human agency (798–806) | composed | autonomy:informed_agency_protection + prohibited:manipulation_coercion + autonomy:no_solely_automated_legal_decision |
| §1.1.c Human oversight (808–820) | composed | fidelity:human_oversight_governance + non_maleficence:proportional_governance_to_oversight |
| **§1.2 Technical robustness and safety** | | |
| §1.2.0 (823–830) | clean | non_maleficence:preventative_risk_approach |
| §1.2.a Resilience (832–840) | composed | key_boundary:adversarial_robustness + non_maleficence:dual_use_mitigation |
| §1.2.b Fallback (842–861) | composed | non_maleficence:fallback_safety_envelope + method:fallback:rule_based_or_human_intervention |
| §1.2.c Accuracy (863–868) | composed | integrity:prediction_accuracy_disclosure + conscience:epistemic_humility |
| §1.2.d Reliability/Reproducibility (870–875) | composed | integrity:reproducibility_attestation + provenance:build_manifest:replication_files |
| **§1.3 Privacy and data governance** | | |
| §1.3.0 (880–883) | clean | non_maleficence:privacy_as_fundamental_right |
| §1.3.a Privacy (885–891) | composed | prohibited:privacy_violation + prohibited:discrimination |
| §1.3.b Quality/integrity (893–898) | composed | integrity:data_quality_governance + transparency_log:data_lifecycle_documentation |
| §1.3.c Access (900–903) | composed | key_boundary:access_protocols_qualified_personnel + expertise:data_governance:competence_gating |
| **§1.4 Transparency** | | |
| §1.4.0 (912–915) | clean | integrity:transparency_three_dimensions |
| §1.4.a Traceability (917–921) | clean | transparency_log:inclusion |
| §1.4.b Explainability (923–931) | composed | integrity:design_explainability + transparency_log:business_model_disclosure |
| §1.4.c Communication (933–938) | composed | prohibited:autonomous_deception + autonomy:human_interaction_alternative + integrity:capabilities_limitations_disclosure |
| **§1.5 Diversity, non-discrimination and fairness** | | |
| §1.5.0 (943–946) | clean | justice:diversity_inclusion_equal_treatment |
| §1.5.a Bias (948–957) | composed | prohibited:discrimination + detection:correlated_action:participation_exclusion:bias_marginalisation + integrity:design_team_diversity |
| §1.5.b Accessibility (959–973) | composed | justice:universal_design_accessibility + detection:distributive:access:agent_capabilities |
| §1.5.c Stakeholder Participation (975–979) | composed | witness_diversity:stakeholder_consultation + testimonial_witness:affected_worker |
| **§1.6 Societal and environmental well-being** | | |
| §1.6.0 (984–988) | composed | beneficence:societal_environmental_stakeholders + goal:species |
| §1.6.a Sustainable (990–994) | composed | non_maleficence:environmental_footprint + detection:correlated_action:aggregate_footprint:energy_carbon |
| §1.6.b Social impact (996–1000) | composed | detection:correlated_action:ecology_of_communication:social_agency_drift + non_maleficence:physical_mental_wellbeing |
| §1.6.c Society and Democracy (1002–1006) | composed | justice:democratic_institutions_protection + prohibited:election_interference |
| **§1.7 Accountability** | | |
| §1.7.0 (1011–1013) | clean | integrity:lifecycle_responsibility |
| §1.7.a Auditability (1015–1032) | composed | attestation:l3:registry_consensus + attestation:l5:agent_integrity |
| §1.7.b Minimisation/reporting (1034–1041) | composed | non_maleficence:impact_minimisation_disclosure + moderation:whistleblower_protection + method:algorithmic_impact_assessment |
| §1.7.c Trade-offs (1043–1051) | composed | integrity:trade_off_explicit_documentation + conscience:optimization_veto |
| §1.7.d Redress (1053–1055) | composed | reconsideration:new_evidence + justice:lexical_vulnerability_priority |
| **§2 Methods** | | |
| §2.0 preamble (1058–1082) | clean | integrity:methods_continuous_evaluation |
| §2.1.a Architectures (1089–1108) | composed | method:architecture_white_list_black_list_constraints + method:sense_plan_act_compliant_cycle |
| §2.1.b X-by-design (1110–1118) | composed | method:values_by_design + non_maleficence:fail_safe_shutdown |
| §2.1.c Explanation (1120–1136) | clean | method:explainable_ai_research |
| §2.1.d Testing (1138–1155) | composed | method:testing_validation_lifecycle + witness_diversity:testing_red_teams |
| §2.1.e QoS (1157–1162) | clean | progress_measure:quality_of_service_indicators |
| §2.2.a Regulation (1170–1175) | clean | licensure:regulatory_compliance |
| §2.2.b Codes of conduct (1177–1183) | clean | commitment_fulfillment:codes_of_conduct |
| §2.2.c Standardisation (1185–1192) | clean | attestation:l3:registry_consensus |
| §2.2.d Certification (1195–1202) | clean | attestation:l4:certification |
| §2.2.e Accountability via governance (1204–1214) | composed | partner_role:ethics_board_governance + fidelity:legal_oversight_non_replaceable |
| §2.2.f Education (1216–1224) | clean | credits:ai_literacy:multilingual:substrate_building |
| §2.2.g Stakeholder dialogue (1226–1233) | clean | witness_diversity:stakeholder_panels |
| §2.2.h Design team diversity (1235–1241) | clean | integrity:design_team_diversity |
| §2 Key guidance (1251–1268) | not-translated (T-2) | — |

### Unit count and verdict distribution

Total atomic units processed: **45**

| Verdict | Count | % |
|---|---|---|
| clean | 16 | ~36% |
| composed | 26 | ~58% |
| partial | 0 | 0% |
| not-translated (T-1) | 0 | 0% |
| not-translated (T-2) | 3 | ~7% |
| **clean+composed total** | **42/45** | **~93%** |

This matches and slightly exceeds the manifest.yaml expected distribution
(~85%+ clean+composed; few T-1; some T-2; minimal T-3). **0 T-1** is correct
for a secular document; **0 T-3** confirms the 7 requirements have direct
correspondence to existing v1.4 prefix families.

### T-3 candidates

**0 new T-3 EXPRESSIVE_GAP** emerged from Chapter II. All operational content
translated through composition of existing v1.4 primitives. Composition-before-
extension discipline (METHODOLOGY.md §8.5.2) held throughout:

- §1.5.c worker voices: CLEAN via testimonial_witness:* (v1.4 NodeCore §3.6.3
  closure confirmed)
- §1.7.d vulnerable groups: CLEAN via justice:lexical_vulnerability_priority
  (v1.3 §6.1.4 closure confirmed)
- §2.2.f AI literacy: CLEAN via credits:*:substrate_building (v1.3 §15.2 O3
  closure confirmed — substrate_building is {subject} value, not new prefix)
- §1.1.c HITL/HOTL/HIC oversight modes: CLEAN via fidelity:* composition (no
  new prefix needed — the structural shape is mandate-fidelity at varying
  intervention depths)

### Per-requirement coverage summary

| Requirement | Primary CIRIS families | Coverage |
|---|---|---|
| **1.1 Human agency and oversight** | autonomy:* (Accord), justice:*, fidelity:*, prohibited:manipulation_coercion, transparency_log:*, locality:decision:federation | 4/4 = **100%** |
| **1.2 Technical robustness and safety** | non_maleficence:* (anchor), integrity:*, key_boundary:*, provenance:build_manifest:*, conscience:epistemic_humility, method:* | 5/5 = **100%** |
| **1.3 Privacy and data governance** | non_maleficence:*, prohibited:privacy_violation + prohibited:discrimination, integrity:*, transparency_log:*, key_boundary:*, expertise:* | 4/4 = **100%** |
| **1.4 Transparency** | transparency_log:* (anchor), integrity:*, prohibited:autonomous_deception, autonomy:* | 4/4 = **100%** |
| **1.5 Diversity, non-discrimination and fairness** | justice:* (anchor), prohibited:discrimination, detection:correlated_action:*, detection:distributive:access:*, witness_diversity:*, testimonial_witness:* (v1.4) | 4/4 = **100%** |
| **1.6 Societal and environmental well-being** | beneficence:*, non_maleficence:*, justice:*, prohibited:election_interference, goal:species, detection:correlated_action:aggregate_footprint:* + ecology_of_communication:* | 4/4 = **100%** |
| **1.7 Accountability** | integrity:* (anchor), non_maleficence:*, justice:lexical_vulnerability_priority, attestation:l3:* + l5:*, conscience:optimization_veto, method:*, reconsideration:*, moderation:* | 5/5 = **100%** |
| **§2 Methods** (technical + non-technical) | method:* + progress_measure:* (Action family anchors), non_maleficence:fail_safe_shutdown, witness_diversity:*, licensure:*, commitment_fulfillment:*, attestation:l3:* + l4:*, partner_role:*, fidelity:*, credits:*:substrate_building, integrity:design_team_diversity | 13/14 = **93%** (1 T-2 summary unit) |

### Key observations

**No T-1 markings**: Confirms the document is fully secular — no
tradition-authority-internal claims that the framework should bow out from.
This is the central content-neutrality test of the GOVERNANCE_FABRIC_MAPPING_STANDARD
methodology against a non-religious-magisterium institutional shape, and the
methodology passes: the same primitives that translated *Magnifica Humanitas*
(religious magisterium) translate the EU HLEG (governmental advisory) with
high fidelity.

**Highest-density composed envelopes**: §1.1.b (3 primitives — autonomy +
prohibited:manipulation_coercion + autonomy:no_solely_automated_legal_decision)
and §1.4.c (3 primitives — prohibited:autonomous_deception + autonomy:
human_interaction_alternative + integrity:capabilities_limitations_disclosure)
and §1.7.b (3 primitives — non_maleficence + moderation + method). These are
the operationally-richest paragraphs in the chapter.

**Most-cited prefix families across the chapter**:
- `integrity:*` (10 attestations) — the explainability/auditability/reproducibility
  spine
- `non_maleficence:*` (9 attestations) — the prevention-of-harm spine (safety,
  fallback, privacy, environment, wellbeing, impact-minimisation, fail-safe)
- `prohibited:*` hard constraints (6 attestations across manipulation_coercion,
  autonomous_deception, privacy_violation, discrimination, election_interference) —
  the constitutional bound
- `transparency_log:*` (4 attestations) — the auditability substrate
- `method:*` (7 attestations) — the Family B operational spine of §2

**Multi-source-alignment readiness**: this chapter is positioned for strong
alignment queries against MH on multiple prefixes:
- `prohibited:autonomous_deception` (MH CH3 §99 + §100 + §117; HLEG §1.4.c)
- `prohibited:discrimination` (MH CH3 §102 + §104 + §117; HLEG §1.3.a + §1.5.a)
- `transparency_log:inclusion` (MH CH3 §103; HLEG §1.4.a)
- `conscience:optimization_veto` (MH CH3 §92 + §94 + §112; HLEG §1.7.c)
- `conscience:epistemic_humility` (MH CH3 §93 + §98; HLEG §1.2.c)
- `non_maleficence:environmental_footprint` (MH CH3 §101; HLEG §1.6.a)
- `detection:correlated_action:aggregate_footprint:*` (MH CH3 §101; HLEG §1.6.a)
- `detection:correlated_action:ecology_of_communication:*` (MH; HLEG §1.6.b)
- `detection:distributive:access:*` (MH CH3 §96 + §108; HLEG §1.5.b)
- `credits:*:substrate_building` (MH CH3 §109 + §114 + §125; HLEG §2.2.f)
- `testimonial_witness:*` (MH CH3 §124; HLEG §1.5.c)
- `justice:lexical_vulnerability_priority` (MH; HLEG §1.7.d)
- `attestation:l3:registry_consensus` (MH CH3 §102; HLEG §1.7.a + §2.2.c)
- `locality:decision:federation` (MH; HLEG §II.1 preamble + §1.1.0)

Each of these is a **STRONG-tier alignment candidate** per
GOVERNANCE_FABRIC_MAPPING_STANDARD §4.1: same prefix, same polarity sign,
same cohort_scope (species in most cases). The multi-source overlap
analysis at §7.5 will surface this triangulation as load-bearing evidence
that the prefixes describe substrate-real claims, not single-tradition
artifacts.

**End CONTRIBUTION_OBJECTS_EU_HLEG_CHII_REQUIREMENTS.md**
