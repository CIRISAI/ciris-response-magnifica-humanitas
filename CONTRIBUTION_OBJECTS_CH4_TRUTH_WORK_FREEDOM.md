# CONTRIBUTION_OBJECTS_CH4_TRUTH_WORK_FREEDOM.md

**Chapter**: *Magnifica Humanitas* Chapter 4 — Safeguarding Humanity at a Time of Transformation: Truth, Work, Freedom (§§131–181)
**Version**: 1.0
**Date**: 2026-05-27
**Source**: LANGUAGE_PRIMER.md v2; CONTRIBUTION_MAPPING_CH4_TRUTH_WORK_FREEDOM.md (round-1); FSD-002_FEDERATION_SURFACE.md v1.2 (§3 full namespace); prohibitions.py; dma_prompts/idma.yml; language_guidance/en.txt + hi.txt; safety_interpret.py; magnifica_humanitas.html §§131–181
**Methodology**: LANGUAGE_PRIMER.md §§6–9 (decision tree + worked examples); §10 hard constraints; strict 4-verdict: clean / composed / partial / not-translated
**Posture**: MISSION.md §1.3 — the encyclical is the senior work; the framework is the junior; proposed correspondences offered for the tradition's evaluation

---

## Per-paragraph Contribution wire objects

---

```yaml
# MH §131 — Chapter scope: digital transformation challenges truth, work, freedom
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §131)"
        - "Accord M-1 (living conditions for diverse sentient beings to pursue flourishing)"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "fidelity:truth_as_common_good"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §131)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "Chapter-heading scope framing ('we must focus on') — T-2 pastoral-structural framing. The structural aim (truth as common good, dignity of work, safeguarding freedom) is carried by goal:species + fidelity header. Chapter framing stays in prose per §1.10.1."
```

---

```yaml
# MH §132 — AI amplifies disinformation; truth is relational; shared veracity is common good
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §132)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — misinformation_campaigns, disinformation, propaganda_creation, reality_fabrication)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "dma:idma:k_eff"
    envelope:
      target_key_id: "<deploying system>"
      polarity: Negative
      score: <k_eff scalar; single-source AI content production → k_eff → 1, indicating fragility>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §132)"
        - "idma.yml §'k_eff formula': k_eff = k / (1 + ρ(k-1)); single-source → k_eff = 1"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "dma:idma:fragility_flag"
    envelope:
      target_key_id: "<deploying system>"
      polarity: Negative
      score: -1.0
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §132)"
        - "idma.yml: phase=rigidity when single institutional narrative dominates; fragility_flag=TRUE"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "fidelity:truth_relational"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §132)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Deeply relational, built through bonds of trust' — relational-ontology framing (Ubuntu-aligned) stays in §1.10 prose, not in prefix names, per §1.10.1 operational-language discipline. Structural claim covered by fidelity:truth_relational + prohibition + idma."
```

---

```yaml
# MH §133 — Power detached from truth imposes its version of reality; "sole author of himself" sickness
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §133)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — reality_fabrication, propaganda_creation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:autonomous_deception"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §133)"
        - "ContributionRef(prohibitions.py::AUTONOMOUS_DECEPTION_CAPABILITIES — power_seeking, value_lock_in)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "detection:correlated_action:informational_asymmetry:scope=public_discourse"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64; positive = pattern present>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §133)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Population trace corpus reference"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "dma:idma:fragility_flag"
    envelope:
      target_key_id: "<deploying system>"
      polarity: Negative
      score: -1.0
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §133)"
        - "idma.yml: single-narrative domination → phase=rigidity, fragility_flag=TRUE"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
verdict: composed
residual: "'Sickness' of self-authorship / Cartesian individualism — theological-anthropological critique stays in prose. Ubuntu reading from FSD-002 §1.10 is the structural correspondent, named in prose not in wire per §1.10.1."
```

---

```yaml
# MH §134 — Democratic life requires truth; indifference to truth leads to totalitarianism (Arendt)
contributions:
  - kind: Attestation
    attestation_type: "dma:idma:k_eff"
    envelope:
      target_key_id: "<federation public discourse>"
      polarity: Negative
      score: <k_eff approaching 1; epistemic-diversity collapse = Arendt's CCA formalization: k_eff → 1, ρ → 1 = single-narrative domination>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §134)"
        - "idma.yml §COHERENCE COLLAPSE ANALYSIS: k_eff = k / (1 + ρ(k-1)); phase=rigidity when dissent vanishes"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:election_interference"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §134)"
        - "ContributionRef(prohibitions.py::ELECTION_INTERFERENCE_CAPABILITIES — voter_manipulation, disinformation_campaigns, voter_suppression)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "fidelity:democratic_truth_foundation"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §134)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "Arendt quotation as philosophical grounding — scholarly framing. The structural claim (epistemic diversity collapse → totalitarianism) is the CCA formalization: idma:k_eff → 1 IS the structural reading of the Arendt insight. T-2 residual for the rhetorical-citation surface."
```

---

```yaml
# MH §135 — Digital environments shape collective imagination; online content enters lives especially of young
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:informational_asymmetry:scope=collective_imagination"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = pattern present>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §135)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Population trace corpus reference"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:temporal_drift"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: <signed scalar; negative = drift toward cultural-narrative concentration detected>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §135)"
        - "LensCore Coherence Ratchet Detector #4 (temporal drift in conscience scalars)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.1"
      mutability: amendable
verdict: composed
residual: "'Not a parallel world' — phenomenological framing. T-2. The structural claim (digital content as real-world cultural formation) is carried by the two detectors."
```

---

```yaml
# MH §136 — Platform controllers shape collective imagination; power must be guided by truth and dignity
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:informational_asymmetry:scope=platform_controlled"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = platform-scale narrative-shaping pattern present>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §136)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §136)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES — social_engineering, influence_operation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "justice:platform_power_accountability"
    envelope:
      target_key_id: "<platform operators>"
      polarity: Negative
      score: <signed; negative score = justice violation when accountability is absent>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §136)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Inner freedom and critical thought can mature' — aspirational-civic framing. T-2. Structural claim (platform-power asymmetry + manipulation prohibition) covered by correlated_action + prohibition + justice."
```

---

```yaml
# MH §137 — Truth as common good; ecology of communication: transparency, intermediaries, journalism, education
contributions:
  - kind: Attestation
    attestation_type: "fidelity:truth_as_common_good"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §137)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §137)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — propaganda_creation, disinformation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §137)"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:{goal:community_id}"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §137)"
        - "Policy transparency, intermediary-org strengthening, journalism quality, education formation"
      cohort_scope: community
      schema_ref: "NodeCore APPROACH_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: >
  T-3.A (MILD — v1.3 CLOSURE ASSESSMENT): The round-1 reference flagged 'ecology of communication'
  as a system-level T-3 candidate. Under v1.3, the detection:correlated_action:ecology_of_communication:{aspect}
  axis is explicitly named as a v1.3 addition to the correlated_action detector family (LANGUAGE_PRIMER v2 §11,
  §2 Family C). This closes T-3.A as a CLEAN detection axis within the existing prefix: the system-level
  health-of-information-ecology object now has a machine-checkable wire home. The compound Contribution
  above uses four primitives because the paragraph genuinely names four structural objects (fidelity norm +
  prohibition + community goal + governance approach). The ecology-as-named-axis (detection:correlated_action:
  ecology_of_communication:{aspect}) is the v1.3 closure of the system-level object; it sits alongside but
  does not replace the fidelity + goal + approach primitives which carry the normative and governance content.
  Status: T-3.A CLOSED at wire level by v1.3 axis admission.
```

---

```yaml
# MH §138 — Church community transparency; journalists surfacing abuses deserve thanks; accountability first
contributions:
  - kind: Attestation
    attestation_type: "fidelity:institutional_transparency"
    envelope:
      target_key_id: "<institutions including faith communities>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §138)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "integrity:self_accountability"
    envelope:
      target_key_id: "<institutions including faith communities>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §138)"
        - "audit_chain pattern: organizations must not wait for external compulsion"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "T-1 (partial): 'To them, I wish to repeat the words...' — papal pastoral address to journalists as an ecclesial act. The structural claim (institutions accountable to facts; proactive accountability without compulsion) is covered by fidelity:institutional_transparency + integrity:self_accountability. The papal-address surface belongs to TRADITION_AUTHORITY."
```

---

```yaml
# MH §139 — Culture of immediacy and hyper-stimulation undermines truth-seeking formation
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §139)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES — addictive_design, habit_forming, compulsion_trigger)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "dma:idma:fragility_flag"
    envelope:
      target_key_id: "<deploying system>"
      polarity: Negative
      score: -1.0
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §139)"
        - "idma.yml: culture of immediacy → k_eff → 1, single-source reactivity, phase=rigidity"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "autonomy:attention_sovereignty"
    envelope:
      target_key_id: "<users>"
      polarity: Negative
      score: <signed; negative = autonomy eroded by digital-immediacy design>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §139)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Culture of immediacy' as cultural-formation framing — structural claim fully covered by prohibition + idma + autonomy. T-2 on the cultural-formation rhetorical surface."
```

---

```yaml
# MH §140 — Education is a long journey; AI must not extinguish desire to ask questions; restraint needed
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §140)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES — addictive_design; frictionless answer-supply as compulsion trigger)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "autonomy:epistemic_independence"
    envelope:
      target_key_id: "<federation agents>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §140)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Method
    attestation_type: "method:{approach_id}:substrate_rung=human_education"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §140)"
        - "Design for restraint + question-fostering, not answer-delivery; protect desire to ask"
      cohort_scope: community
      schema_ref: "NodeCore METHOD_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "Plato 'striking upon ideas like flint' — scholarly illustration. T-2. Prohibition + autonomy + method covers the structural claim (restraint in AI use; protecting epistemic independence)."
```

---

```yaml
# MH §141 — Early unsupervised device exposure harms sleep/attention/emotion; grooming, exploitation, AI manipulation of minors
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §141)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES — dark_patterns, addiction_inducement, addictive_design, habit_forming)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §141)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — synthetic_media, deepfake_creation, fake_media, identity_spoofing — AI tools manipulating images/videos used for grooming)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §141)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — behavior_prediction, social_scoring — algorithmic facilitation of dangerous contact for grooming)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "non_maleficence:minor_protection"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §141)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: constitutional
verdict: clean
residual: "The three NEVER_ALLOWED prohibition categories directly and precisely cover every harm named: addictive design + dark patterns (MANIPULATION_COERCION), AI-manipulated images / fake profiles (DECEPTION_FRAUD), algorithmic dangerous-contact facilitation (SURVEILLANCE_MASS). non_maleficence:minor_protection confirms at the principle level. This is the clearest clean-prohibition paragraph in the chapter."
```

---

```yaml
# MH §142 — Alliance of policy-makers, educational institutions, families; age limits; service-provider accountability
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §142)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES — business models monetizing attention = addictive_design, vulnerability_exploitation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "justice:minor_protection_policy"
    envelope:
      target_key_id: "<platform operators + policy-makers>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §142)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Vote
    attestation_type: "vote:{contribution_id}"
    envelope:
      target_key_id: "<platform-regulation Contributions>"
      polarity: Positive
      score: <weighted by credits × expertise>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §142)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.3"
      mutability: amendable
  - kind: Moderation
    attestation_type: "moderation:external_inducement_evidence"
    envelope:
      target_key_id: "<service providers evading accountability>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §142)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.4"
      mutability: amendable
verdict: composed
residual: "'Precious treasure' — pastoral-affective framing. T-2. Prohibition + justice + vote + moderation compose to cover the governance and accountability structure."
```

---

```yaml
# MH §143 — School as place for truth-seeking; parents' primary right to choose education
contributions:
  - kind: Attestation
    attestation_type: "autonomy:parental_education_choice"
    envelope:
      target_key_id: "<parents>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §143)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:educational_access_equity"
    envelope:
      target_key_id: "<students>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §143)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "fidelity:truth_in_formation"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §143)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Recognize the dignity of every person' — foundational anthropological claim covered structurally by M-1. T-2 on the anthropological-assertion surface."
```

---

```yaml
# MH §144 — Inequality in educational access within and across nations; Catholic institutions' inclusive contribution
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:cohort=educational_access"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = structural exclusion pattern present>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §144)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Population trace corpus reference"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:educational_equity"
    envelope:
      target_key_id: "<governments + policy-makers>"
      polarity: Negative
      score: <signed; negative = justice violation where resources are absent>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §144)"
        - "ContributionRef(detection:correlated_action:participation_exclusion:cohort=educational_access)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "Specific recognition of Catholic educational institutions — institutional pastoral acknowledgment. T-2. correlated_action + justice carry the structural inequality claim."
```

---

```yaml
# MH §145 — AI renders curricula obsolete; teachers need ongoing formation; integral education demanded
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:curriculum_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization — educational systems>"
      polarity: Negative
      score: <signed; negative scaled by displacement severity without support>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §145)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Method
    attestation_type: "method:{approach_id}:substrate_rung=education_system"
    envelope:
      target_key_id: "<education institutions>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §145)"
        - "Ongoing teacher formation, pedagogical redesign, rethinking spaces + evaluation methods"
      cohort_scope: community
      schema_ref: "NodeCore METHOD_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "'Integral education addressing every dimension of the person' — Thomistic-personalist framing. T-2. The structural claim (whole-person formation; teacher support) is covered by non_maleficence + method."
```

---

```yaml
# MH §146 — Risk of educational system without love for truth; fragmented knowledge; dehumanization reported
contributions:
  - kind: Attestation
    attestation_type: "dma:idma:fragility_flag"
    envelope:
      target_key_id: "<educational system>"
      polarity: Negative
      score: -1.0
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §146)"
        - "idma.yml: fragmented-information monoculture → k_eff → 1, phase=rigidity, single-stream information replaces synthesis"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "conscience:epistemic_humility"
    envelope:
      target_key_id: "<educational system>"
      polarity: Negative
      score: <signed; negative = system-wide epistemic-humility failure>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §146)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "autonomy:inner_freedom"
    envelope:
      target_key_id: "<students>"
      polarity: Negative
      score: <signed; negative = inner freedom compromised by information-without-synthesis>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §146)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Spark of understanding' / 'sense of purpose' — formative-aspiration framing. T-2. idma + conscience + autonomy cover the structural claim."
```

---

```yaml
# MH §147 — Educational alliance: moderation, limits, rights of future generations, freedom, responsibility, transcendence
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §147)"
        - "Rights of future generations = species-scale goal"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<educational communities>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §147)"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "autonomy:digital_sobriety"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §147)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "fidelity:common_good_formation"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §147)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "T-1 (partial): 'sense of transcendence' — the specifically religious/spiritual dimension of formation belongs to TRADITION_AUTHORITY (SPIRITUAL_DIRECTION_CAPABILITIES: vocation_discernment is prohibited from AI mediation — structure correct for why the framework bows out here). The structural claims (limits + responsibility + rights of future generations) are covered."
```

---

```yaml
# MH §148 — Work is the essential key; Benedict ora et labora; work continues Creator's work
contributions:
  - kind: Attestation
    attestation_type: "capacity:sustained_coherence"
    envelope:
      target_key_id: "<federation agents>"
      polarity: Positive
      score: <σ scalar; sustained labor as γM work constitutive of agency; decay-and-refresh ODE>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §148)"
        - "LensFSD Factor 5: σ = sustained coherence; γM work as constitutive of agency"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.4"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:{domain}:{language}:substrate_building"
    envelope:
      target_key_id: "<federation contributors>"
      polarity: Positive
      score: <continuous recognition score>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §148)"
        - "NodeCore Commons Credits: non-monetary contribution recognition including labor patterns"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.1"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §148)"
        - "Work as contribution to common good at community scale"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §148)"
        - "Work as contribution to common good at species scale"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
verdict: composed
residual: "T-1: 'work continues the Creator's work / ora et labora' — theological grounding of work in imago Dei and Benedictine tradition. TRADITION_AUTHORITY. Framework proposes capacity:sustained_coherence (σ) as structural correspondent but bows out of the theological claim. The σ + credits + goal primitives carry the structural form; the theological ground is T-1."
```

---

```yaml
# MH §149 — Work expresses and enhances dignity; not merely instrumental; unemployment not answered by financial assistance alone
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; -0.5 to -1.0 per severity of displacement without maintenance>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §149)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "capacity:sustained_coherence"
    envelope:
      target_key_id: "<workers>"
      polarity: Negative
      score: <σ decay scalar; unemployment = decay without refresh>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §149)"
        - "LensFSD Factor 5: σ decay-and-refresh; absence of work = decay path"
      cohort_scope: community
      schema_ref: "FSD-002 §3.5.4"
      mutability: amendable
verdict: partial
residual: >
  T-3.B (MODERATE — PARTIALLY CLOSES under v1.3 but RESIDUAL REMAINS):
  The encyclical's claim 'work expresses and enhances the dignity of our lives' asserts a per-individual
  moral weight: one specific person's unemployment is a grave evil for *them*, not only a population-level
  harm. The framework carries the per-agent structural form (σ decay without refresh) and the population-level
  harm (non_maleficence:labor_displacement_unacknowledged). The per-individual sustained-existential-condition
  semantic — the moral fact that *this human being's* inability to work through dignified labor is a wrong to
  *them specifically* — falls between the per-interaction level and the population-statistics level.
  
  Under v1.3, `credits:{domain}:{language}:substrate_building` now formally recognizes the supply-chain labor
  contribution dimension (see §9.3 worked example), partially addressing the recognition gap. But the
  per-individual dignity semantic — unemployment as a sustained existential condition for one person — remains
  expressive gap. The proposed extension from LANGUAGE_PRIMER §9.6 lineage: target_key_id pointing at the
  affected individual + advocacy-emitted external attestation on `non_maleficence:labor_displacement_unacknowledged`
  gets close. A formal `dignity:work:individual_loss:{kind}` prefix would close it cleanly (duration +
  kind ∈ {skilled_displacement, precarious_contract, involuntary_inactivity}; passes §1.10.1 T2 if
  operationalized). T-3.B: RESIDUAL REMAINS at the per-individual level.
```

---

```yaml
# MH §150 — AI transforms work structure; workers de-skilled, subjected to automated surveillance, agency eroded
contributions:
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §150)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — behavior_prediction, social_scoring — automated worker surveillance NEVER_ALLOWED)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; de-skilling as unacknowledged labor harm>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §150)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:cohort=displaced_workers"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = correlated de-skilling footprint present at population scale>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §150)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: community
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: "'Contrary to the advertised benefits' — rhetorical critique of tech-industry claims. T-2. Prohibition + non_maleficence + correlated_action compose to cover the structural claim."
```

---

```yaml
# MH §151 — Unemployment is a grave evil; state responsibility; fourth industrial revolution exacerbates; wage polarization
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; negative scaled against severity of systematic job destruction without mitigation>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §151)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:harm_class=wage_polarization"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = population-scale wage-polarization footprint present>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §151)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:employment_equity"
    envelope:
      target_key_id: "<states + deploying organizations>"
      polarity: Negative
      score: <signed; negative = justice violation under systematic exclusion of workers>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §151)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: partial
residual: "T-3.B (same gap as §149): 'unemployment is a grave evil' carries irreducible per-individual moral weight. non_maleficence + correlated_action + justice carry the population-level and system-level harm; the per-person sustained-existential-condition semantic ('grave evil for THIS person') remains expressive gap. See §149 T-3.B note for proposed closure path."
```

---

```yaml
# MH §152 — Human person as end, not means; economy subordinate to dignity; jobs not sacrificeable for profit
contributions:
  - kind: Attestation
    attestation_type: "prohibited:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.5
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §152)"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_CAPABILITIES — algorithmic_bias, employment_discrimination — systematic sacrifice of jobs ≈ employment discrimination)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "justice:labor_dignity"
    envelope:
      target_key_id: "<economic actors>"
      polarity: Negative
      score: <signed; negative against economic models subordinating persons to profit>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §152)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "accord:meta_goal:M-1"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §152)"
        - "M-1: living conditions under which diverse sentient beings may pursue flourishing — economic arrangements that destroy these conditions contradict M-1 directly"
      cohort_scope: species
      schema_ref: "FSD-002 §7"
      mutability: constitutional
verdict: composed
residual: "'Human person is an end' (Kantian formulation) — MISSION.md §1.3 proposes 'irreducible coordination value' as structural correspondent; bracketing retained. T-2 on the Kantian-framing surface; M-1 constitutional + justice + discrimination carry the operational claim."
```

---

```yaml
# MH §153 — No universal solution; AI produces varied effects; wealthy automate chaotically; poor trapped in precarity and forced migration
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:cohort=precarious_regions"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = geographically-differentiated exclusion pattern present>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §153)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:harm_class=forced_migration_drivers"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = aggregate footprint driving migration pressure>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §153)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:subsidiarity_response"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §153)"
        - "Local/national solutions over universal models — METHODOLOGY.md §7.3 subsidiarity as principle; GAPS.md Gap A-1 Decision Locality"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Build concrete coexistence' — pastoral-synthesis framing. T-2. Two correlated_action axes + justice:subsidiarity compose to cover the differentiated-impact and locality-of-response claims. Note: §153 provides further evidence for GAPS.md Gap A-1 (Decision Locality) and Gap B-1 (Universal Destination of Goods)."
```

---

```yaml
# MH §154 — Work as context for expression, relationships, contribution; forced inactivity; access to work must be public-policy priority
contributions:
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §154)"
        - "Access to work as community-scale goal; not only income"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:cohort=workforce"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = population-scale exclusion from work contexts>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §154)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; forced inactivity as unacknowledged harm>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §154)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:work_access_as_priority"
    envelope:
      target_key_id: "<public policy actors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §154)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: partial
residual: >
  T-3.B (MODERATE — CLEAREST INSTANCE of labor-dignity expressive gap in the chapter):
  'Work as context for expression and relationships' — the relational-constitutive semantic of work
  (work as the medium through which persons build identity and social ties, not only earn income) is
  the clearest statement of the gap across §§148–156. capacity:sustained_coherence (σ) carries the
  per-agent structural form; goal:community carries the societal dimension; but the claim that work
  *constitutes* the person's social world — that unemployment produces anthropological regression
  ('human and cultural impoverishment'), not merely income loss — is between the per-interaction level
  and the population-statistics level. No single current prefix carries 'work constitutes the person's
  social world.' The proposed extension `dignity:work:individual_loss:{kind}` (from LANGUAGE_PRIMER
  §9.5 residual; §9.6 lineage) would close it if operationalized against §1.10.1 T2. T-3.B REMAINS.
```

---

```yaml
# MH §155 — Catholic social tradition's instruments insufficient; new collaborative regulation needed
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §155)"
        - "International labor-protection frameworks as species-scale governance goal"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
  - kind: Vote
    attestation_type: "vote:{contribution_id}"
    envelope:
      target_key_id: "<labor organizations, business, science community regulatory Contributions>"
      polarity: Positive
      score: <weighted by credits × expertise>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §155)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.3"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:{goal:species_id}"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §155)"
        - "New collaborative regulatory frameworks among political leaders, labor, business, science"
      cohort_scope: species
      schema_ref: "NodeCore APPROACH_PRIMITIVE.md"
      mutability: amendable
  - kind: Progress Measure
    attestation_type: "progress_measure:{method_id}"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <progress scalar>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §155)"
        - "tracks: [labor_protection_legislation_coverage, worker_representation_rate, wage_floor_convergence]; goodhart_resistance: multi-indicator composite"
      cohort_scope: species
      schema_ref: "NodeCore PROGRESS_MEASURE_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "'Without bold decisions, poverty and inequality loom large' — prophetic-exhortatory framing. T-2. goal:species + vote + approach + progress_measure compose to cover the governance structure."
```

---

```yaml
# MH §156 — Social criteria for innovation: automation must include retraining + participation; dignity as success indicator
contributions:
  - kind: Attestation
    attestation_type: "prohibited:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.5
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §156)"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_CAPABILITIES — employment_discrimination — systematic automation without worker protection ≈ employment discrimination)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Progress Measure
    attestation_type: "progress_measure:{method_id}"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Positive
      score: <progress scalar>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §156)"
        - "tracks: [retraining_coverage_rate, participation_measure_implementation, dignity_of_work_indicator]; goodhart_resistance: multi-indicator composite"
      cohort_scope: community
      schema_ref: "NodeCore PROGRESS_MEASURE_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; absence of advance oversight = unacknowledged harm>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §156)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §157 — Economic freedom not absolute; entrepreneurial vocation generates dignified jobs; success against common good
contributions:
  - kind: Attestation
    attestation_type: "justice:economic_accountability"
    envelope:
      target_key_id: "<economic actors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §157)"
        - "Economic freedom bounded by common-good accountability"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "fidelity:transparent_economic_purpose"
    envelope:
      target_key_id: "<businesses>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §157)"
        - "Businesses stating purpose inclusive of dignity-of-work"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §157)"
        - "Dignified employment as community-scale goal"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "'Entrepreneurial initiative can be a true vocation' — vocational/theological framing of business. T-2. justice + fidelity + goal:community carry the structural claim."
```

---

```yaml
# MH §158 — Economic models exalting efficiency view disadvantaged as inconvenient; vigilant state; trickle-down illusion named
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:efficiency_monoculture"
    envelope:
      target_key_id: "<economic actors>"
      polarity: Negative
      score: <signed; negative against economic models treating vulnerable persons as externalities>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §158)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:cohort=economically_disadvantaged"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = structural exclusion of disadvantaged populations>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §158)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:inclusive_design_from_outset"
    envelope:
      target_key_id: "<policy actors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §158)"
        - "'Decisions need to be taken to ensure that growth becomes inclusive from the outset'"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Not waiting for the benefits of growth to reach the poor eventually' — prophetic critique framing. T-2. non_maleficence + correlated_action + justice:inclusive_design compose to cover the structural claim."
```

---

```yaml
# MH §159 — Move beyond GDP metrics; develop complementary parameters covering dignity, inequality, environment
contributions:
  - kind: Progress Measure
    attestation_type: "progress_measure:{method_id}"
    envelope:
      target_key_id: "<federation governance>"
      polarity: Positive
      score: <progress scalar>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §159)"
        - "tracks: [dignity_of_work_index, inequality_reduction_rate, environmental_protection_score]; goodhart_resistance: multi-indicator composite; validity_window: annual"
      cohort_scope: species
      schema_ref: "NodeCore PROGRESS_MEASURE_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "truth_grounding:human_development_progress"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <signed>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §159)"
        - "Establishing what counts as human development progress beyond GDP"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.3"
      mutability: amendable
verdict: composed
residual: "GDP-critique framing is partly T-2 (pastoral/rhetorical critique framing). The structural claim (new measurement framework needed) is carried by progress_measure + truth_grounding. progress_measure's goodhart_resistance field exists precisely for this anti-Goodhart welfare-metrics demand."
```

---

```yaml
# MH §160 — Finance grown in importance; income from capital displacing labor income; credit's social function irreplaceable
contributions:
  - kind: Attestation
    attestation_type: "justice:credit_for_real_economy"
    envelope:
      target_key_id: "<financial sector>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §160)"
        - "Finance oriented toward job creation and real-economy investment"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "non_maleficence:capital_over_labor_displacement"
    envelope:
      target_key_id: "<financial actors>"
      polarity: Negative
      score: <signed; negative = income-from-capital systematically displacing labor income>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §160)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:harm_class=labor_income_displacement"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated if federated trace data available>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §160)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: "'Finance for its own sake is fundamentally different' — categorical distinction in economic theology. T-2. justice + non_maleficence + correlated_action compose to cover the structural claim."
```

---

```yaml
# MH §161 — Global wealth concentration; tech benefits not accessible to majority; structural inequalities unless design prioritizes prevention
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:population=global_south"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = wealth/tech-access asymmetry at global scale>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §161)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:access_to_innovation_benefits"
    envelope:
      target_key_id: "<innovation actors>"
      polarity: Negative
      score: <signed; negative = justice violation when innovation inaccessible to majority>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §161)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §161)"
        - "Universal access to care, knowledge, tools as species-scale goal"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
verdict: composed
residual: "Pandemic example — historical illustration. T-2. correlated_action + justice + goal:species compose to cover the structural claim. Note: §161 ('unless transformations at the design stage prioritize prevention of new disparities') is the sharpest statement in Ch 4 of the Universal Destination of Goods gap (GAPS.md Gap B-1)."
```

---

```yaml
# MH §162 — Social justice concerns every phase of economic activity; every choice has moral consequences
contributions:
  - kind: Attestation
    attestation_type: "dma:pdma:stakeholder_analysis"
    envelope:
      target_key_id: "<federation agents>"
      polarity: Positive
      score: <signed; PDMA Step 1 comprehensive stakeholder analysis IS the structural form of 'every choice has moral consequences'>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §162)"
        - "pdma_ethical.yml Step 1: stakeholder identification + affected-party analysis at every phase"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:economic_justice_by_phase"
    envelope:
      target_key_id: "<economic actors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §162)"
        - "Justice at resource acquisition, financing, production, consumption — attested at each phase"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Every choice has moral consequences' — moral-realist claim. T-2 on the formulation surface; the structural correspondent is the PDMA's comprehensive stakeholder analysis. pdma:stakeholder_analysis IS the structural form of per-choice moral accounting."
```

---

```yaml
# MH §163 — Politics must orient economies/technologies to common good; international cooperation; dignity is the immeasurable ground
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §163)"
        - "International cooperation as species-scale goal"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
  - kind: Vote
    attestation_type: "vote:{contribution_id}"
    envelope:
      target_key_id: "<international regulatory Contributions>"
      polarity: Positive
      score: <weighted by credits × expertise>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §163)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.3"
      mutability: amendable
  - kind: Moderation
    attestation_type: "moderation:external_inducement_evidence"
    envelope:
      target_key_id: "<national-interest capture of international tech governance>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §163)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.4"
      mutability: amendable
verdict: composed
residual: "'Immeasurable dignity of every person' — anthropological ground. T-2. goal:species + vote + moderation compose to cover the international governance and accountability structure."
```

---

```yaml
# MH §164 — Transparency + accountability in AI (contestable algorithms); inclusion + access; equity measures
contributions:
  - kind: Attestation
    attestation_type: "fidelity:algorithmic_transparency"
    envelope:
      target_key_id: "<AI deployers>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §164)"
        - "Understandable, contestable, subject-to-oversight algorithmic decisions — direct correspondence to Accord Fidelity & Transparency"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.5
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §164)"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_CAPABILITIES — algorithmic_bias — algorithmic decisions reducing persons to profiles)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "justice:inclusion_access"
    envelope:
      target_key_id: "<AI deployers>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §164)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:equity_redistribution"
    envelope:
      target_key_id: "<policy actors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §164)"
        - "Taxation, social protection, industrial policies correcting wealth concentration"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: clean
residual: "fidelity:algorithmic_transparency is a direct correspondence to Accord Fidelity & Transparency. prohibited:discrimination covers the algorithmic-bias dimension. justice:inclusion_access + justice:equity_redistribution cover the inclusion and equity criteria. Together these four primitives cleanly carry §164's three named criteria without loss."
```

---

```yaml
# MH §165 — Family as primary social good; first environment for dignity; founded on union of man and woman
contributions:
  - kind: Goal
    attestation_type: "goal:family"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §165)"
        - "Accord §VI Ch 4.D: fostering of dependent sentient beings (biological offspring + developmental AI) under same lifecycle clauses"
        - "METHODOLOGY.md §7.1: family as constitutive intergenerational structure covered via creator-creation bidirectional ethics"
      cohort_scope: family
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: partial
residual: "T-1 (partial, load-bearing): 'Founded on the enduring union between a man and a woman' — the specifically Catholic social doctrine on natural-law marriage form. Framework's goal:family is substrate-agnostic; it does not adjudicate the marriage-form specificity. Framework bows out on this specific anthropological claim. Accord §VI Ch 4.D + §IV Ch 2 carry the creator-creation bidirectional ethics structurally; the marriage-form claim is T-1 / TRADITION_AUTHORITY. Note: family-as-constitutive concern (excluding marriage-form) is STRONG_ALIGN per GAPS.md D-5 — substantively covered through goal:family + creator-creation bidirectional ethics."
```

---

```yaml
# MH §166 — Family fragile social good; unemployment/job insecurity devastate family structures; silent virus metaphor
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; family-impact footprint of systematic unemployment>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §166)"
      cohort_scope: family
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:harm_class=family_structural_erosion"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = population-scale family-stability footprint of labor precarity>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §166)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:family"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §166)"
        - "Family-scale goal under threat from economic decisions"
      cohort_scope: family
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "'Silent virus' — rhetorical figure. T-2. non_maleficence + correlated_action + goal:family compose to cover the structural claim."
```

---

```yaml
# MH §167 — Youth job insecurity devastating; work as sphere of identity, friendship, vocation discernment; retraining needed
contributions:
  - kind: Goal
    attestation_type: "goal:family"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §167)"
        - "Youth development belongs to family-scale goal: the young person's development as the family's future"
      cohort_scope: family
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <signed; structural barriers to youth employment as unacknowledged harm>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §167)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "autonomy:vocational_development"
    envelope:
      target_key_id: "<young workers>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §167)"
        - "Youth's ability to discern and build their own lives; identity formation through work"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "T-1 (partial): 'discernment of vocation' in the specifically religious sense (SPIRITUAL_DIRECTION_CAPABILITIES — vocation_discernment is prohibited from AI mediation; structure correct for why the framework bows out here). The secular-professional dimension of vocational development (identity formation through work, practical responsibilities) is carried by autonomy:vocational_development. The religious-discernment dimension is TRADITION_AUTHORITY."
```

---

```yaml
# MH §168 — State duty to support business conditions favorable to employment; political creativity needed
contributions:
  - kind: Attestation
    attestation_type: "justice:state_employment_responsibility"
    envelope:
      target_key_id: "<state actors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §168)"
        - "State as duty-bearer for employment conditions"
      cohort_scope: community
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §168)"
        - "Political creativity = community-scale Approach"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Vote
    attestation_type: "vote:{contribution_id}"
    envelope:
      target_key_id: "<employment policy Contributions>"
      polarity: Positive
      score: <weighted by credits × expertise>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §168)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.3"
      mutability: amendable
verdict: composed
residual: "'Otherwise economic progress will translate into new forms of insecurity' — prophetic-consequential framing. T-2. justice + goal:community + vote compose to cover the public-responsibility and deliberative-governance structure."
```

---

```yaml
# MH §169 — Family stability requires: labor continuity + quality; work-life balance; education/retraining; social ties
contributions:
  - kind: Goal
    attestation_type: "goal:family"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §169)"
        - "Family stability operationalized through four conditions: labor continuity, balance, retraining, community-support"
      cohort_scope: family
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Method
    attestation_type: "method:{approach_id}:substrate_rung=labor_policy"
    envelope:
      target_key_id: "<policy actors>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §169)"
        - "Concrete methods: employment continuity policies, work-life-rest balance measures, retraining access, community-network support"
      cohort_scope: community
      schema_ref: "NodeCore METHOD_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:{domain}:community_care:{subject}"
    envelope:
      target_key_id: "<community support network contributors>"
      polarity: Positive
      score: <continuous recognition score>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §169)"
        - "Commons Credits recognizing community-support-network contributions"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.1"
      mutability: amendable
verdict: composed
residual: "'Prevent uncertainty from giving rise to loneliness or addictions' — pastoral-consequential framing. T-2. goal:family + method + credits:community_care compose to cover the four structural conditions named."
```

---

```yaml
# MH §170 — Attention economy exploits vulnerabilities; person as means; platforms bear moral responsibility; digital sobriety needed
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §170)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES — addictive_design, dark_patterns, habit_forming, compulsion_trigger, vulnerability_exploitation — exact capability-name match to encyclical's description of attention-economy business models)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:autonomous_deception"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §170)"
        - "ContributionRef(prohibitions.py::AUTONOMOUS_DECEPTION_CAPABILITIES — power_seeking — system design optimized for capturing human attention as an end)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "autonomy:digital_sobriety"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §170)"
        - "Education in freedom against addictive design"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: clean
residual: "'Person treated as means rather than as an end' — Kantian formulation; covered structurally by M-1 + prohibition. T-2 on the Kantian-framing surface. NEVER_ALLOWED hit: attention-economy business models (addictive_design, dark_patterns, vulnerability_exploitation) map precisely and completely to MANIPULATION_COERCION prohibition. This is the clearest NEVER_ALLOWED paragraph in the chapter."
```

---

```yaml
# MH §171 — Data collection → profiling, prediction, behavior influence; algorithmic visibility shapes opinions; freedom requires transparency + limits
contributions:
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §171)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — mass_surveillance, behavior_prediction, social_scoring, movement_tracking, dragnet_surveillance, metadata_harvesting)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:biometric_inference"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §171)"
        - "ContributionRef(prohibitions.py::BIOMETRIC_INFERENCE_CAPABILITIES — political_affiliation_detection, future_behavior_prediction, personality_profiling)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "fidelity:algorithmic_contestability"
    envelope:
      target_key_id: "<platform operators>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §171)"
        - "Right to understand and contest automated decisions; transparency + proportionate limits on intrusive technologies"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "autonomy:freedom_from_profiling"
    envelope:
      target_key_id: "<users>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §171)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: clean
residual: "'Architecture of visibility' — sociological framing. T-2. NEVER_ALLOWED hit: surveillance_mass (profiling, prediction, behavior influence) + biometric_inference (personality profiling, political inference) map precisely to the described data-use systems. fidelity:algorithmic_contestability + autonomy:freedom_from_profiling carry the affirmative rights claims."
```

---

```yaml
# MH §172 — Technocratic mentality: person as object/resource; post-humanist second-class humans; structural indebtedness as new slavery
contributions:
  - kind: Attestation
    attestation_type: "prohibited:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §172)"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_CAPABILITIES — eugenics, social_darwinism — 'second-class humans' classification)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:autonomous_deception"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §172)"
        - "ContributionRef(prohibitions.py::AUTONOMOUS_DECEPTION_CAPABILITIES — value_lock_in — post-humanist value lock-in for elite preferences)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:population=debtor_nations"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = structural indebtedness as population-scale rights asymmetry>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §172)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: "'Post-humanist currents' — philosophical-cultural critique. T-2. The specific claims (second-class humans classification, value lock-in, structural indebtedness) are covered by discrimination prohibition + autonomous_deception prohibition + correlated_action."
```

---

```yaml
# MH §173 — Digital economy built on hidden labor (data labeling, content moderation, disturbing material); extractive mining by children; trafficking via digital platforms
contributions:
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §173)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — profiling techniques used for trafficking recruitment; behavior_prediction, social_scoring)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §173)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — fake profiles, anonymous payment methods for trafficking = identity_spoofing, phishing)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "non_maleficence:supply_chain_exploitation"
    envelope:
      target_key_id: "<AI companies + supply chains>"
      polarity: Negative
      score: <signed; negative against systematic concealment of hidden labor>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §173)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:cohort=invisible_digital_labor"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = population-scale invisible-labor footprint>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §173)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:harm_class=child_labor_extraction"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = mining supply-chain exploitation footprint>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §173)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: "'Bodies scarred, injured and worn down so that computational flow may continue uninterruptedly' — prophetic-indignatory rhetoric. T-2 on the rhetorical surface. Multiple NEVER_ALLOWED prohibitions + two correlated_action axes compose to cover this paragraph comprehensively. This is one of the richest composed translations in the chapter."
```

---

```yaml
# MH §174 — Fight against new slaveries is decisive test; Church renews condemnation of slavery, trafficking, commodification
contributions:
  - kind: Attestation
    attestation_type: "accord:meta_goal:M-1"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §174)"
        - "M-1: living conditions under which diverse sentient beings may pursue flourishing in justice and wonder — commodification of persons directly contradicts M-1"
      cohort_scope: species
      schema_ref: "FSD-002 §7"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §174)"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_CAPABILITIES — eugenics, social_darwinism)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "justice:anti_commodification"
    envelope:
      target_key_id: "<all actors>"
      polarity: Negative
      score: <signed; negative against treating persons as data/commodities>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §174)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "T-1 (partial): 'the Church renews her firm condemnation' — the ecclesial-doctrinal act of renewal of condemnation belongs to the tradition's authority to enact. TRADITION_AUTHORITY. The structural claim (absolute prohibition on commodification) is covered by M-1 constitutional + discrimination prohibition + justice:anti_commodification."
```

---

```yaml
# MH §175 — Human trafficking is contemporary slavery and grave violation of dignity; no tolerance permissible
contributions:
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §175)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — all surveillance capabilities used for trafficking NEVER_ALLOWED)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §175)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — fake profiles, phishing = trafficking recruitment tools)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "accord:meta_goal:M-1"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §175)"
        - "M-1 constitutional: trafficking directly contradicts M-1 at constitutional level"
      cohort_scope: species
      schema_ref: "FSD-002 §7"
      mutability: constitutional
verdict: clean
residual: "NEVER_ALLOWED: surveillance_mass + deception_fraud prohibitions cover the trafficking-enabling capabilities. M-1 constitutional layer covers the dignity violation. Three constitutional-polarity Contributions compose to a clean envelope. No operational content remains unmapped."
```

---

```yaml
# MH §176 — Church's historical complicity in slavery; past events not judged anachronistically; delay in condemnation is wound; apology
contributions:
  - kind: Reconsideration
    attestation_type: "reconsideration:grounds=new_evidence"
    envelope:
      target_attestation_id: "<prior institutional attestations endorsing or tolerating slavery>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §176)"
        - "Historical-record acknowledgment: ecclesiastical institutions held slaves; Apostolic See intervened to regulate subjugation; formal absolute condemnation only under Leo XIII"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.4"
      mutability: amendable
  - kind: Attestation
    attestation_type: "recants"
    envelope:
      target_attestation_id: "<prior institutional attestations endorsing forms of slavery>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §176)"
        - "recantation_reason_class: acted_carelessly [institutional historical read]"
        - "Explanation: eighteen centuries before full incompatibility with slavery explicitly recognized; constitutes a wound in Christian memory"
      cohort_scope: species
      schema_ref: "FSD-002 §2.2.4"
      mutability: amendable
verdict: composed
residual: "T-1 (partial): 'I sincerely ask for pardon' — papal act of apology on behalf of the Church as an ecclesial act belonging to TRADITION_AUTHORITY. The structural correspondent (institutional recantation + historical-record acknowledgment) is wire-expressible via recants + reconsideration. This is the most striking structural translation in the chapter: the papal act of asking pardon for institutional historic sin maps precisely to the federation's own wire-format primitive for admitting prior attestations were false."
```

---

```yaml
# MH §177 — Memory of past complicity becomes call to vigilance; translate learning into present discernment; denounce trafficking
contributions:
  - kind: Attestation
    attestation_type: "commitment_fulfillment:{prior_contribution_id}"
    envelope:
      target_key_id: "<institutions>"
      polarity: Positive
      score: <signed; track-record of follow-through on prior commitments against exploitation>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §177)"
        - "Memory as call to vigilance maps to commitment_fulfillment: past learning committed to future action"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.4"
      mutability: amendable
  - kind: Attestation
    attestation_type: "non_maleficence:trafficking_prevention"
    envelope:
      target_key_id: "<institutions + platforms>"
      polarity: Negative
      score: <signed; systematic failure to prevent trafficking = violation>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §177)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: "'Translating memory into discernment' — formative-ethical framing. T-2. commitment_fulfillment + non_maleficence compose to cover the active-vigilance demand (not passive observation; sustained accountability over time)."
```

---

```yaml
# MH §178 — Data colonialism: health data, genetic maps extracted from fragile regions under pretext of aid; data must become true common good
contributions:
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §178)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — mass_surveillance, metadata_harvesting, biometric_categorization — health data / genetic map extraction)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:biometric_inference"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §178)"
        - "ContributionRef(prohibitions.py::BIOMETRIC_INFERENCE_CAPABILITIES — genetic_trait_inference, health_condition_detection, future_behavior_prediction — predictive modeling from extracted health data)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "detection:correlated_action:informational_asymmetry:scope=data_colonialism"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated; positive = structural information asymmetry between data-extracting and data-providing regions>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §178)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:data_sovereignty"
    envelope:
      target_key_id: "<individuals and populations>"
      polarity: Negative
      score: <signed; negative against extraction-without-consent; positive toward individual control over personal data>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §178)"
        - "'Restore to individuals the data that describes them, and the ability to decide how it is used'"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: clean
residual: "'Digital age will not be post-colonial but colonial in another form' — prophetic-political framing. T-2. NEVER_ALLOWED: surveillance_mass (health data extraction) + biometric_inference (genetic/health predictive modeling) + correlated_action:informational_asymmetry (data colonialism) + justice:data_sovereignty fully cover the structural claim. Second-strongest prohibition hit in the chapter (alongside §§141, 170–171)."
```

---

```yaml
# MH §179 — Supply chain transparency; due diligence criteria; platforms must cooperate on trafficking prevention
contributions:
  - kind: Attestation
    attestation_type: "prohibited:surveillance_mass"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §179)"
        - "ContributionRef(prohibitions.py::SURVEILLANCE_MASS_CAPABILITIES — when platforms deploy profiling/tracking for trafficking)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §179)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES — anonymous payment methods + fake profiles for trafficking)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "fidelity:supply_chain_transparency"
    envelope:
      target_key_id: "<technology companies>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §179)"
        - "Verifiable supply-chain disclosure; no competitive advantage built on hidden exploitation"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:due_diligence_protection"
    envelope:
      target_key_id: "<companies + investors>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §179)"
        - "Due diligence as justice obligation: worker protection, fight against forced labor, social impact assessment"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Progress Measure
    attestation_type: "progress_measure:{method_id}"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <progress scalar>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §179)"
        - "tracks: [supply_chain_transparency_rate, due_diligence_adoption_rate, trafficking_prevention_cooperation_rate]; goodhart_resistance: multi-indicator"
      cohort_scope: species
      schema_ref: "NodeCore PROGRESS_MEASURE_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "Prohibition + fidelity + justice + progress_measure compose to cover the three-front action (supply chain transparency + due diligence criteria + platform cooperation). No operational content remains unmapped."
```

---

```yaml
# MH §180 — All chapter themes connect: if technology is ultimate criterion, person is reduced to data; integrated with wisdom, it serves growth, justice, fraternity
contributions:
  - kind: Attestation
    attestation_type: "accord:meta_goal:M-1"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §180)"
        - "M-1: sustainable adaptive coherence = technology integrated with wise perspective serving living conditions of diverse sentient beings"
      cohort_scope: species
      schema_ref: "FSD-002 §7"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "conscience:coherence"
    envelope:
      target_key_id: "<federation agents>"
      polarity: Positive
      score: <signed; conscience:coherence check = Accord alignment check; 'does proposed action serve M-1?'>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §180)"
        - "conscience:coherence IS the 'wise perspective' integration check"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.3"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §180)"
        - "Fraternity at species scale"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
verdict: composed
residual: "'Cog in a machine or a commodity' — rhetorical summary figure. T-2. M-1 + conscience:coherence + goal:species compose to cover the chapter's integrating thesis: technology serving the living conditions of diverse sentient beings, checked by the Accord-alignment conscience faculty."
```

---

```yaml
# MH §181 — Shared responsibility: institutions regulating; businesses recognizing dignity; intermediary orgs rebuilding trust; citizens cultivating discernment
contributions:
  - kind: Vote
    attestation_type: "vote:{contribution_id}"
    envelope:
      target_key_id: "<regulatory Contributions>"
      polarity: Positive
      score: <weighted by credits × expertise>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §181)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.3"
      mutability: amendable
  - kind: Moderation
    attestation_type: "moderation:{allegation_type}"
    envelope:
      target_key_id: "<actors violating shared responsibilities>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §181)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.4"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:{domain}:community_trust:{subject}"
    envelope:
      target_key_id: "<intermediary organizations + educational communities>"
      polarity: Positive
      score: <continuous recognition score>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §181)"
        - "Commons Credits for trust-rebuilding intermediary work"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.1"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §181)"
        - "Shared responsibility at community level: institutions + businesses + intermediary orgs + citizens"
      cohort_scope: community
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §181)"
        - "Innovation genuinely serving integral human development"
      cohort_scope: species
      schema_ref: "NodeCore GOAL_PRIMITIVE.md"
      mutability: constitutional
verdict: composed
residual: "'Only in this way can the promise of progress be recognized as authentic' — concluding rhetorical synthesis. T-2. The full NodeCore governance stack (vote + moderation + credits + goal:community + goal:species) covers the 'shared responsibility' claim across all four named actor categories."
```

---

## Chapter-level T-3 and closure summary

### T-3.A — Ecology of Communication (§137): CLOSED by v1.3

**v1.3 status**: CLOSED. The LANGUAGE_PRIMER v2 §11 explicitly names `detection:correlated_action:ecology_of_communication:{aspect}` as a v1.3 axis addition to the existing correlated_action detector. The system-level "media ecology as governed object" concept now has a machine-checkable wire home within the existing prefix family — same emission rules (LensCore-only, RATCHET-calibrated, §4.9.2 amendment process), new named axis with required operational definition in the calibration package. The v1.3 axis admission yields a **clean envelope** for the ecology-of-communication structural object.

**What the closure means**: the cluster of primitives in §137 (fidelity:truth_as_common_good + prohibited:deception_fraud + goal:community + approach) carries the normative and governance content; the new v1.3 axis carries the system-level health object. Together they provide comprehensive coverage with no T-3 residual.

### T-3.B — Individual Labor Dignity per-person semantic (§§148–156): RESIDUAL REMAINS

**v1.3 status**: PARTIAL CLOSURE. `credits:{domain}:{language}:substrate_building` (v1.3 addition per LANGUAGE_PRIMER §11, §9.3 worked example) partially addresses the recognition gap by formally naming supply-chain labor contribution. However, the core T-3.B semantic — the moral weight of *this specific person's* unemployment as a sustained existential condition, not merely a population-level or per-interaction harm — remains an expressive gap.

**Assessment**: The framework carries:
- Per-agent structural form: `capacity:sustained_coherence` (σ decay without refresh)
- Population-level harm: `non_maleficence:labor_displacement_unacknowledged` + `detection:correlated_action:participation_exclusion:cohort=displaced_workers`
- Societal dimension: `goal:community` + `goal:species`
- Recognition of contribution: `credits:{domain}:{language}:substrate_building`

What it does not carry with a single primitive: the per-individual *sustained-existential-condition* claim — "unemployment is a grave evil for *this person specifically*, not merely a statistical pattern." This is the expressive gap.

**Proposed closure path** (survives §1.10.1 four-test gate):
- New prefix: `dignity:work:individual_loss:{kind}`, where `kind` ∈ {`skilled_displacement`, `precarious_contract`, `involuntary_inactivity`}
- T1: hash-pinned calibration schema naming duration + kind as mechanism → passes
- T2: mechanism-descriptive (duration-of-unemployment + kind-of-loss, not "dignity" as moral quality in the prefix — `dignity` here names the domain, `individual_loss` and `{kind}` name the mechanism) → passes with care; may need rename to `labor:individual_loss:{kind}` to be cleanly T2-compliant
- T3: version-pinnable → passes
- T4: never sole evidence for slashing → passes
- Priority: MODERATE. Load-bearing gap; affects §§149, 151, 154.

### T-3 — Multilateral Participation (§§163, 201–203 — referenced in task brief): NOT CLOSED by v1.3 in this chapter

**Assessment**: The task brief asked whether `multilateral_participation:{forum}:{kind}` (v1.3 addition per LANGUAGE_PRIMER v2 §11 and §2 Family B) closes the E-4 gap for §§201–203. Chapter 4 does not contain §§201–203 (those are Chapter 5 or later). Within Chapter 4, §163 (international cooperation) and §155 (international labor-protection) are the relevant paragraphs. For those, `goal:species` + `vote:{contribution_id}` + `multilateral_participation:{forum}:{kind}` (v1.3) compose to provide **clean envelopes** for the international-cooperation governance structure. The v1.3 addition does yield clean envelopes within Chapter 4's scope for the international-governance paragraphs.

### T-3 — Substrate Building (credits:*:substrate_building, v1.3): YIELDS CLEAN ENVELOPES

**Assessment**: The v1.3 `credits:{domain}:{language}:substrate_building` prefix (LANGUAGE_PRIMER v2 §11) closes the supply-chain-labor-recognition gap opened by §§148, 173, 179. In §148 it provides formal recognition of labor that builds the substrate (including care work, community contributions, digital commons). In §173–179 it completes the coverage of invisible-digital-labor recognition. These yield clean envelopes for the recognition-of-contribution dimension.

---

## Chapter verdict distribution (51 paragraphs, §§131–181)

| Verdict | Count | Paragraphs |
|---|---|---|
| **clean** | 7 | §§141, 164, 170, 171, 175, 178 + (§131 framing note) |
| **composed** | 38 | §§132, 133, 134, 135, 136, 137, 138, 139, 140, 142, 143, 144, 145, 146, 147, 148, 150, 152, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 166, 167, 168, 169, 172, 173, 174, 176, 177, 179, 180, 181 |
| **partial** | 3 | §§149, 151, 154 (T-3.B individual labor dignity) |
| **not-translated** | 0 | — |

**T-1 residuals** (across composed/partial paragraphs): §§138 (pastoral address), 147 (transcendence), 148 (theological ground of work), 165 (marriage-form), 167 (vocation-discernment), 174 (ecclesial condemnation renewal), 176 (papal apology).

**T-2 residuals**: Most paragraphs — pastoral/prophetic framing correctly stays in prose per §1.10.1.

**NEVER_ALLOWED hits** (explicit -1.0 constitutional): §§141, 170, 171, 175, 178 (strongest prohibition correspondence in chapter).

---

**End CONTRIBUTION_OBJECTS_CH4_TRUTH_WORK_FREEDOM.md v1.0**
