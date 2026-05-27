# CONTRIBUTION_OBJECTS_IEEE_EAD_CH04_WELL_BEING.md
# IEEE Ethically Aligned Design 1st ed. (2019) — Chapter 4 "Well-being"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 3581–4791)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

The Well-being chapter operationalises eudaimonia / human flourishing as an evaluation
criterion for A/IS design, deployment and monitoring. The chapter's load-bearing
operational claims cluster on:

1. **Well-being as a multi-dimensional outcome variable** — distinct from GDP/profit, and
   spanning subjective, objective, composite and social-media-sourced indicators.
2. **Metrics-as-feedback discipline** — stakeholder-co-defined indicators, applied at
   pre-/in-/post-deployment, with explicit "roll back if reduces well-being" obligation.
3. **Environmental well-being as inseparable from human well-being** — planetary scope,
   intrinsic-value-of-biosystems claim, environmental-justice composition with the
   wealth-disparity pattern.
4. **Human-rights floor** — well-being metrics must not be deployed to justify rights
   violations; the floor is the human-rights regime, not the well-being metric set.
5. **Stakeholder-deliberation discipline** — power-asymmetry mitigation, "leads"/
   facilitators, less-powerful-voices amplification.
6. **Computational sustainability + impact-foresight taxonomy** — labor displacement,
   manipulation, deception, etc., as named foreseeable harm classes.

The chapter explicitly **does not endorse a specific well-being metric or methodology**
(lines 3650–3653, 3741–3744). This is structural — it means the chapter's claim is
*operational discipline around using well-being metrics*, not the metrics themselves.
The wire format carries the discipline (composition of existing CIRIS prefix families)
cleanly; the metric-content remains in prose because IEEE itself refused to specify it.

**Translation note on T-3 watch**: the prompt flagged "wellbeing_metric:*" as a candidate
T-3 family if the chapter proposed specific measurement methodologies that don't compose
onto existing primitives. The chapter does **not** propose specific methodologies — it
proposes a discipline-around-metrics. Discipline composes onto existing prefixes
(`integrity:*` for measurement honesty, `progress_measure:*` for the goal-hierarchy
metric primitive, `goal:*` for the well-being objective, `witness_diversity:*` and
`testimonial_witness:*` for stakeholder-voice). **No T-3 candidate is emitted for a
`wellbeing_metric:*` family.** A measurable T-3 candidate **is** emitted at §1.6.b
(intrinsic value of non-human biosystems) where the chapter's claim does not compose
cleanly onto existing prefixes that all treat the moral object as anthropic or sentient.

---

## §0 — Opening chapter framing (lines 3581–3664)

### §0.a — The well-being question for A/IS (lines 3585–3593)

```yaml
# Lines 3585–3593 — chapter problem statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:wellbeing_holistic_assessment"
      score: 1.0
      confidence: 0.90
      context: >
        "How to assess, understand, measure, monitor, safeguard, and improve the
        well-being impacts of A/IS on humans" is named as the key open question.
        Individual well-being is declared inseparable from societal, economic and
        environmental systems. This composes the beneficence principle (CIRIS) with
        a multi-substrate well-being object.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3585–3593"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I beneficence)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
verdict: clean
```

### §0.b — Need for consistent multidimensional indicators (lines 3595–3606)

```yaml
# Lines 3595–3606 — multidimensional indicator need; expanded evaluation discipline
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        "For A/IS to demonstrably advance well-being, we need consistent and
        multidimensional indicators that are easily implementable by the developers,
        engineers, and designers who are building our future." Goal-scale claim:
        species-level well-being as the aim that A/IS development should serve.
        Maps onto NodeCore Family B goal:species (multi-scale belonging composite).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3595–3606"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:multidimensional_evaluation"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS creators need expanded ways to evaluate the impact of their products,
        services, or systems on human well-being. These evaluations must also be
        done with an understanding that human well-being is deeply linked to the
        well-being of society, economies, and ecosystems." Integrity-as-honest-
        evaluation: A/IS creators' evaluation practices must encompass multiple
        substrates (personal/social/environmental).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3603–3606"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
```

### §0.c — Traditional fiscal metrics are insufficient (lines 3608–3613)

```yaml
# Lines 3608–3613 — fiscal-metric inadequacy; risk of irreversible harm
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:fiscal_metric_blindspot_harm"
      score: -0.8
      confidence: 0.80
      context: >
        "Where the priority given to these factors [psychological, social,
        environmental] is not equal to that given to fiscal metrics of success,
        A/IS creators risk causing or contributing to negative and irreversible
        harms to our people and our planet." Non_maleficence claim — measurement
        bias toward fiscal-only metrics produces foreseeable harm. The score is
        negative because the claim is that this configuration produces harm; it
        is not a hard-constraint prohibition (the configuration is not banned),
        rather a strong-negative warning.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3608–3613"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II non_maleficence)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
```

### §0.d — Innovation foregone when well-being metrics not used (lines 3615–3644)

```yaml
# Lines 3615–3644 — autonomous-vehicle example + Beyond GDP movement
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Lines 3615–3644 are illustrative/rhetorical framing: the autonomous-vehicle
  example, the Beyond GDP movement reference, and the Stiglitz quote ("What we
  measure affects what we do; and if our measurements are flawed, decisions may
  be distorted") are pedagogical scaffolding. The structural claim — that
  multi-dimensional metrics improve A/IS outcomes — is carried by §0.b above and
  §1.0 below; the rhetorical illustration correctly stays in prose per
  LANGUAGE_PRIMER §10 T-2 (PASTORAL_PROSE).
```

### §0.e — Chapter goal: educate creators (lines 3646–3664)

```yaml
# Lines 3646–3664 — chapter goal + audience + neutrality on specific metrics
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:wellbeing_metric_neutrality"
      score: 1.0
      confidence: 0.85
      context: >
        "We do not prioritize or advocate for any specific indicator or
        methodology." Integrity-as-honest-scoping: IEEE EAD declares it does
        not endorse a specific well-being metric; the chapter's claim is about
        the discipline of using such metrics, not which metric to use. This
        structural scoping is itself an attestation: the framework's wire-format
        claim is on the discipline, not the metric content.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3650–3653"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
note: |
  This attestation's load-bearing role: it is the structural reason the prompt's
  "wellbeing_metric:*" T-3 candidate is NOT emitted. IEEE EAD itself declines to
  propose a metric family; the chapter's operational content is metric-discipline,
  which composes onto existing prefixes (goal:*, progress_measure:*, integrity:*,
  witness_diversity:*). No T-3 is owed here.
```

---

# Section 1 — The Value of Well-being Metrics for A/IS Creators

## §1.0 — Section purpose (lines 3680–3697)

```yaml
# Lines 3680–3697 — section opening
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Section-opening framing only. The substantive claims (definition of well-being,
  indicator categories, recommendation) are carried by §1.1 through §1.4 below.
```

---

## §1.1 — Issue: A/IS creators often unaware that well-being metrics exist (lines 3685–3697 callout + 3698–3837)

### §1.1.a — Definition of well-being (lines 3698–3717)

```yaml
# Lines 3698–3717 — definition: evaluation of general quality of life; distinct from moral/legal
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:wellbeing_definition_scope"
      score: 1.0
      confidence: 0.85
      context: >
        Well-being defined as "an evaluation of the general quality of life of
        an individual and the state of external circumstances" encompassing the
        full spectrum of personal, social, and environmental factors. Distinct
        from moral or legal evaluation. This is a scoping attestation — the
        chapter's well-being object spans multiple substrates and is positioned
        as complementary to (not substituting for) moral/legal evaluation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3698–3717"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
verdict: clean
```

### §1.1.b — Aspects of well-being (the 10-domain list) (lines 3733–3771)

```yaml
# Lines 3733–3771 — the 10 aspects: Community / Culture / Economy / Education /
# Environment / Government / Human Settlements / Physical Health / Psychological Health / Work
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:wellbeing_multidomain_taxonomy"
      score: 1.0
      confidence: 0.80
      context: >
        Ten recognized aspects of well-being enumerated: Community (belonging,
        crime & safety, discrimination & inclusion, participation, social
        support), Culture (identity, values), Economy, Education, Environment,
        Government, Human Settlements, Physical Health, Psychological Health
        (affect, flourishing, mental illness/health, satisfaction with life),
        Work (governance, time balance, workplace environment). Composes the
        chapter's beneficence claim with the multi-domain breadth that the
        single well-being scalar must encompass.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3733–3771"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:context_specific_indicator_selection"
      score: 1.0
      confidence: 0.85
      context: >
        "Measures of well-being that may be well-suited to wealthy,
        industrialized nations may be less applicable in low- and middle-income
        countries, and vice versa." Indicator selection must be context-
        appropriate; integrity claim against indicator-portability assumptions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3767–3771"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
```

### §1.1.c — The four indicator categories (lines 3786–3818)

```yaml
# Lines 3786–3818 — subjective/objective/composite/social-media indicator categories
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:wellbeing_indicator_category_taxonomy"
      score: 1.0
      confidence: 0.80
      context: >
        Four indicator categories named: (1) subjective/survey-based (SWB);
        (2) objective indicators (income, consumption, health, education,
        crime, housing); (3) composite indices (HDI, Social Progress Index,
        Bhutan GNH, OECD Better Life Index); (4) social-media-sourced (e.g.,
        Hedonometer, World Well-being Project). This is a progress_measure
        primitive — measurement of well-being is the measure of progress
        toward the goal:species well-being aim. progress_measure: required
        fields (tracks[], computation, validity_window, goodhart_resistance)
        are carried in chapter prose; concrete instantiations per deployment
        would pin the specific indicator set.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3786–3818"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: progress_measure:{method_id})"
verdict: clean
note: |
  This is the canonical composition that prevents a wellbeing_metric:* T-3:
  the well-being indicator is the progress_measure for the goal:species
  well-being aim. CIRIS already carries the primitive at NodeCore §3.6.2;
  IEEE EAD's discipline (multi-category coverage; context appropriate
  selection; ongoing monitoring) is metadata on the existing primitive,
  not a new primitive.
```

### §1.1.d — Recommendation: A/IS creators should learn well-being concepts and metrics (lines 3839–3885 incl. callout)

```yaml
# Lines 3839–3885 — recommendation to learn metrics; SDO action proposed
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:wellbeing_metric_literacy"
      score: 1.0
      confidence: 0.80
      context: >
        "A/IS creators should prioritize learning about well-being concepts,
        scientific learnings, research findings, and well-being metrics as
        potential determinants for how they create, deploy, market, and
        monitor their technologies, and ensuring their stakeholders learn
        the same." Expertise-as-standing claim: A/IS creators need attested
        competence in well-being science to discharge the beneficence
        obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3839–3848"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: expertise:{domain}:{language})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:wellbeing_standards_certification"
      score: 1.0
      confidence: 0.75
      context: >
        "This process can be expedited if Standards Development Organizations
        (SDOs), such as the IEEE Standards Association, or other institutions
        such as the Global Reporting Initiative (GRI) or B-Corp, create
        certifications, guidelines, and standards" for well-being metrics in
        A/IS. Approach-level claim: standards-driven certification as a
        pathway toward the goal:species well-being aim. References to IEEE
        P7010 Well-being Metric standards project name a concrete approach
        instantiation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3848–3865 (incl. Further Resources IEEE P7010)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: approach:{goal_id})"
verdict: composed
```

---

## §1.2 — Issue: Application of well-being metrics creates value to corporate / public sector (lines 3840–3914 callout + 3854–3944)

### §1.2.a — Background: short-termism vs. holistic value (lines 3854–3897)

```yaml
# Lines 3854–3897 — short-term-growth pressure as obstacle; companion-robot example
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:short_term_growth_priority"
      score: 0.0
      confidence: 0.75
      context: >
        "As long as organizations exist in a larger societal system which
        prioritizes financial success, these companies will remain under
        pressure to deliver financial results that do not fully incorporate
        societal and environmental impacts, measurements, or priorities."
        This is a population-scale correlation-collapse claim — short-term
        financial metric priority correlates across the organizational
        ecology, suppressing well-being-aware behaviour. LensCore detection
        family. Score 0.0 placeholder; calibration version pin required.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3860–3870"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:premature_market_release_harm"
      score: -0.7
      confidence: 0.70
      context: >
        Companion-robot example: "the A/IS creator who rushed to bring the
        robot to market faster than the competition and who was unaware of
        well-being metrics, may have overlooked critical needs of the
        seniors. The robot might actually hurt the senior instead of helping
        by exacerbating isolation or feelings of loneliness and helplessness."
        Hypothetical-but-illustrative non_maleficence claim: omitting
        well-being assessment in vulnerable-population deployment produces
        foreseeable harm.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3897–3914"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
```

### §1.2.b — Recommendation: triple bottom line, consent, stakeholder co-selection, rollback (lines 3917–3974)

```yaml
# Lines 3917–3974 — triple bottom line; consent + privacy; co-selection with affected populations;
# iterative; roll-back if reduces well-being
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:triple_bottom_line_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS creators should work directly with experts, researchers, and
        practitioners in well-being concepts and metrics to identify existing
        metrics and combinations of indicators that would bring support a
        'triple bottom line', i.e., accounting for economic, social, and
        environmental impacts, approach to well-being." Method-level
        operational claim: triple-bottom-line indicator composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3922–3930"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:consent_for_wellbeing_data"
      score: 1.0
      confidence: 0.90
      context: >
        "Well-being metrics should only be used with consent, respect for
        privacy, and with strict standards for collection and use of these
        data." Autonomy-principle claim: well-being-metric data collection is
        bounded by consent + privacy. Composes with prohibited:privacy_violation
        for the substrate constraint.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3930–3932"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:affected_population_metric_selection"
      score: 1.0
      confidence: 0.85
      context: >
        "Well-being metrics should be chosen in collaboration with the
        populations most affected by those systems—the A/IS stakeholders—
        including both the intended end-users or beneficiaries and those
        groups whose lives might be unintentionally transformed by them."
        witness_diversity primitive: metric selection requires diverse
        stakeholder participation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3933–3958"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "reconsideration:rollback_on_wellbeing_reduction"
      score: 1.0
      confidence: 0.85
      context: >
        "Both A/IS creators and stakeholders should be prepared to
        significantly modify, or even roll back, technology that is shown to
        reduce well-being, as defined by affected populations." This is a
        reconsideration-grounds claim: empirical evidence that the deployed
        system reduces well-being (as defined by the affected population) is
        grounds for reversal. Composes with NodeCore P11 reconsideration:
        new_evidence.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3963–3972"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore Correction: reconsideration:{grounds})"
verdict: composed
note: |
  Four-primitive composition is justified here because the recommendation names
  four genuinely distinct structural objects: the method (triple bottom line),
  the autonomy constraint (consent/privacy), the consensus requirement (witness
  diversity), and the correction primitive (reconsideration on new evidence).
  Each carries operational content the others don't. Per LANGUAGE_PRIMER §8
  Step 5, composing 4 primitives is at the upper limit; the discipline-as-honest
  check applied here is "does the paragraph genuinely name 4 structural objects?"
  — yes.
```

---

## §1.3 — Issue: A/IS creators can safeguard well-being by ensuring no harm to natural systems (lines 3957–3974 callout + 3978–4070)

### §1.3.a — Planetary well-being and intrinsic value of biosystems (lines 3978–3990)

```yaml
# Lines 3978–3990 — ecological collapse endangers human existence; intrinsic merit of biodiversity
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:planetary_wellbeing_inseparability"
      score: 1.0
      confidence: 0.90
      context: >
        "It is unwise, and in truth impossible, to separate the well-being of
        the natural environment of the planet from the well-being of
        humanity… The concept of well-being should encompass planetary
        well-being." Beneficence claim: the well-being object spans
        human + planetary substrates as a single inseparable evaluation
        scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 3978–3985"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
verdict: partial
residual:
  description: |
    The chapter explicitly claims biodiversity + ecological integrity have
    "intrinsic merit beyond simply their instrumental value to humans"
    (lines 3986–3990). The CIRIS prefix family treats well-being and
    beneficence claims with sentient-being-as-object (M-1 names "diverse
    sentient beings"). The instrumental-value composition above is clean.
    The intrinsic-value-of-non-sentient-biosystems claim is operational
    (it grounds the chapter's "do no harm to earth's natural systems" hard
    obligation) but unmapped — no current prefix carries beneficence
    claims with a non-sentient moral object as the attested entity.
  classification: T-3
proposed_extension:
  name: "beneficence:planetary_biosystem_intrinsic_value"
  description: |
    A beneficence attestation where the attested moral object is a
    non-sentient biosystem (biodiversity / ecological integrity) carrying
    intrinsic-value standing distinct from instrumental value to humans
    or to sentient beings. The mechanism is "preservation of biosystem
    integrity attested independent of any sentient-benefit pathway."
  gate_verification:
    T1: yes (publishable rule: list of biosystem-classes carrying the
         standing; calibration-version pinnable)
    T2: borderline — "intrinsic value" is a subjective quality, but the
         mechanism-descriptive reframe "biosystem-integrity-preservation-
         attested-independent-of-sentient-benefit" passes T2 by naming a
         checkable mechanism (does the attestation pathway reference any
         sentient-being benefit? if no, the prefix applies)
    T3: yes (versionable)
    T4: yes (never sole evidence for slashing:*; combines with other
         beneficence claims at consumer policy)
  priority: LOW
  relationship_to_existing: |
    A more conservative alternative: extend cohort_scope to include
    "biosphere" / "planet" as a scope value, leaving the prefix as
    beneficence:planetary_wellbeing_inseparability (the §1.3.a clean
    primitive above). This avoids a new prefix entirely. The chapter's
    intrinsic-value claim is plausibly carried by cohort_scope:biosphere
    + the existing beneficence prefix. Recommended consumer-policy path:
    document the cohort_scope extension rather than introduce a new
    prefix. Composition-before-extension per METHODOLOGY.md §8.5.2 favors
    the cohort-scope route.
note: |
  Per METHODOLOGY.md §8.5.2 composition-before-extension, the conservative
  reading is that this is *not* a T-3 — the intrinsic-value claim resolves
  via cohort_scope:biosphere on the existing beneficence prefix. T-3 is
  emitted at LOW priority because the chapter's "biodiversity has
  intrinsic merit beyond instrumental value to humans" is a strong claim
  the framework may want to honor with explicit prefix-level naming. The
  reviewer can collapse this to partial-without-T-3 if the cohort-scope
  composition is judged sufficient.
```

### §1.3.b — Environmental justice and wealth disparity (lines 4028–4044)

```yaml
# Lines 4028–4044 — environmental injustice concentrates on poor; inequality dampens everyone's well-being
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:environmental_burden_concentration"
      score: 0.0
      confidence: 0.85
      context: >
        "Environmental justice research demonstrates that the negative
        environmental impacts of technology are commonly concentrated on the
        middle class and working poor, as well as those suffering from abject
        poverty, fleeing disaster zones, or otherwise lacking the resources
        to meet their needs." Population-scale correlation-collapse claim:
        environmental harm correlates onto vulnerable cohorts; LensCore
        detection family. Score 0.0 placeholder; calibration version pin
        required.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4028–4040"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:rights_asymmetry:wealth_disparity"
      score: 0.0
      confidence: 0.80
      context: >
        "Well-being research findings indicate that unfair economic and
        social inequality has a dampening effect on everyone's well-being,
        regardless of economic or social class." Cross-cohort detection
        claim: wealth-disparity correlates with universal well-being
        reduction; the harm is not confined to the disadvantaged cohort.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4040–4044"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
verdict: composed
```

### §1.3.c — Recommendation: no harm to natural systems; certification; doing no harm (lines 4026–4056)

```yaml
# Lines 4026–4056 — Recommendation: stewardship of natural systems; use existing standards; do no harm
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:ecological_harm_prohibition"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS creators should prioritize doing no harm to the Earth's natural
        systems, both intended and unintended harm." Non_maleficence claim
        scoped to the natural-systems object; composes with the planetary-
        wellbeing inseparability claim above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4047–4049"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ecological_certification_alignment"
      score: 1.0
      confidence: 0.80
      context: >
        "A/IS systems should be designed to use, support, and strengthen
        existing ecological sustainability standards with a certification or
        similar system, e.g., LEED, Energy Star, or Forest Stewardship
        Council." Method-level operational claim: align A/IS deployment with
        recognized ecological certifications.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4040–4046"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
verdict: composed
```

### §1.3.d — Further Resources references including Laudato Si' and Dalai Lama (lines 4072–4115)

```yaml
# Lines 4072–4115 — references to Laudato Si', Dalai Lama, Islam etc.
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  The Further Resources section explicitly cites tradition-specific authorities
  (Pope Francis Laudato Si'; 14th Dalai Lama; Why Islam.org). Per LANGUAGE_PRIMER
  §10 T-1, claims that belong to the source tradition's own authority are not
  translated into the wire format. The framework's posture is recognition without
  adjudication. The structural claims those traditions inform (planetary
  well-being inseparability; do-no-harm) are already carried by §1.3.a and §1.3.c
  above; these citations are tradition-authority anchors for those structural
  claims, not independent attestations.
```

---

## §1.4 — Issue: Human rights law is related to, but distinct from, the pursuit of well-being (lines 4073–4087 callout + 4088–4154)

### §1.4.a — Background: human rights law as established floor (lines 4088–4109)

```yaml
# Lines 4088–4109 — UDHR, ECHR, Toronto Declaration as established rights frameworks
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "delegates_to"
      score: null
      context: >
        "International human rights law has been firmly established for decades
        in order to protect various guarantees and freedoms as enshrined in
        charters such as the United Nations' Universal Declaration of Human
        Rights and the Council of Europe's Convention on Human Rights." The
        chapter delegates rights-substrate authority to these existing
        instruments; not constituting them, but recognizing them as authoritative.
      witness_relation: external
      epistemic_mode: hearsay
    delegated_scope: ["fundamental_rights_substrate"]
    delegation_purpose: "authority_source"
    evidence_refs:
      - "ieee_ead_v1 ch4 lines 4088–4097"
      - "UN UDHR 1948; ECHR; Toronto Declaration 2018"
    schema_ref: "FSD-002 §2.2.1 (delegates_to reuse pattern for authority-source claims)"
verdict: clean
note: |
  delegates_to is used per LANGUAGE_PRIMER §11.4: the chapter's claim is that
  international human rights law GROUNDS the rights-substrate; the IEEE EAD
  batch-signer is not claiming the rights — it's recognizing existing
  authority instruments as the source. This is the authority-source-via-
  delegation pattern, not a citation (which would go in evidence_refs[]
  only).
```

### §1.4.b — Well-being metrics can be misused to justify rights violations (lines 4106–4143)

```yaml
# Lines 4106–4143 — refugee encampment, journalist imprisonment, GDP-as-pretext for forced labor
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:metric_pretext_for_rights_violation"
      score: -1.0
      confidence: 0.90
      context: >
        "Any metric, including well-being metrics, can be misused to justify
        human rights violations. Encampment and mistreatment of refugees and
        ethnic cleansing undertaken to preserve a nation's culture (an
        aspect of well-being) is one example… The use of well-being metrics
        to justify human rights violations is an unconscionable perversion
        of the nature of any well-being metric." Hard-constraint claim:
        using metrics as pretext for rights violations is prohibited.
        Composes with the federation's existing rights-violation prohibition
        classes (the chapter explicitly cites slavery, sex trafficking,
        child armies, forced labor).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4106–4143"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:rights_asymmetry:metric_capture"
      score: 0.0
      confidence: 0.70
      context: >
        "These same practices happen today in relation to GDP. For instance,
        in 2012, according to the International Labour Organization (ILO),
        approximately 21 million people are victims of forced labor (slavery),
        representing 9% to 56% of GDP income for various countries. These
        clear human rights violations… can increase a country's GDP while
        obviously harming human well-being." Detection claim: aggregate
        metric (here GDP; generalizable to well-being indices) systematically
        captures rights-violating value flows. LensCore detection family;
        score 0.0 placeholder.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4128–4143 (incl. ILO 2012)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
verdict: composed
note: |
  prohibited:metric_pretext_for_rights_violation is a borderline T2 case —
  "metric pretext" can be reframed mechanism-descriptively (the mechanism
  is: well-being-metric attestation cited as justification for a rights-
  violation action). The prohibition fits cleanly within the federation's
  existing hard-constraint family; a §1.10.1 T2 review might rename to
  prohibited:rights_violation_justification_pretext for sharper mechanism-
  framing. Flagged for reviewer judgment but not emitted as T-3.
```

### §1.4.c — Recommendation: human rights as floor not ceiling (lines 4129–4154)

```yaml
# Lines 4129–4154 — human rights framework as floor; well-being complements not displaces rights
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:human_rights_floor_above_wellbeing_metric"
      score: 1.0
      confidence: 0.95
      context: >
        "A human rights framework should represent the floor, and not the
        ceiling, for the standards to which A/IS creators must adhere…
        Well-being as a value complements justice, equality, and freedom.
        Well-designed application of well-being considerations by A/IS
        creators should not displace other issues of human rights or
        ethical methodologies, but rather complement them." Justice claim
        with explicit ordering: rights are the floor, well-being adds on
        top; the metric cannot override the floor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4129–4154"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §VI justice)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: clean
```

---

# Section 2 — Implementing Well-being Metrics for A/IS Creators

## §2.0 — Section purpose (lines 4170–4176)

```yaml
# Lines 4170–4176 — section purpose framing
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Section-opening framing only; the substantive claims are carried by §2.1–§2.4 below.
```

---

## §2.1 — Issue: How can A/IS creators incorporate well-being into their work? (lines 4180–4262)

### §2.1.a — Define type, stakeholders, uses; iterative stakeholder engagement (lines 4185–4205)

```yaml
# Lines 4185–4205 — define product, stakeholders, intended/unintended uses; iterative engagement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:scoping_explicit_use_categorization"
      score: 1.0
      confidence: 0.85
      context: >
        "Organizations and A/IS creators should consider clearly defining the
        type of A/IS product or service that they are developing, including
        articulating its intended stakeholders and uses. By defining typical
        uses, possible uses, and finally unacceptable uses of the technology,
        creators will help to spell out the context of well-being." Integrity-
        as-honest-scoping claim: explicit use-category articulation as a
        precondition for well-being assessment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4195–4205"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

### §2.1.b — Stakeholder consultation, indicator selection, lifecycle monitoring (lines 4172–4221)

```yaml
# Lines 4172–4221 — internal+external stakeholder consultation; pre/post assessment; A/IS models trained
# to include well-being indicators as subgoals
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:stakeholder_lifecycle_engagement"
      score: 1.0
      confidence: 0.85
      context: >
        "Internal and external stakeholders should be extensively consulted
        to ensure that impacts are thoroughly considered through an iterative
        and learning stakeholder engagement process." Witness diversity
        primitive applied to lifecycle stakeholder engagement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4172–4180"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:wellbeing_indicator_lifecycle"
      score: 1.0
      confidence: 0.85
      context: >
        "These well-being indicators can be drawn from mainstream sources and
        models and adapted as necessary. They can be used to engage in pre-
        assessment of the intended user population, projection of possible
        impacts, and post-assessment. Development of a well-being indicator
        measurement plan and relevant data infrastructure will support a
        robust integration of well-being. A/IS models can also be trained
        to explicitly include well-being indicators as subgoals." Progress-
        measure primitive: well-being indicators as the measurement layer
        across pre/post-deployment. Also names the A/IS-internal subgoal
        composition (well-being indicators embedded in agent objectives).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4175–4193"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: progress_measure:{method_id})"
verdict: composed
```

### §2.1.c — Iterative wheelchair example: not all modifications should be adopted (lines 4195–4222)

```yaml
# Lines 4195–4222 — wheelchair example: one indicator increase doesn't justify rollout
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:multidimensional_tradeoff_discipline"
      score: 1.0
      confidence: 0.80
      context: >
        "Therefore, even though a product modification may increase well-being
        according to one indicator or set of A/IS stakeholders, it does not
        mean that this modification should automatically be adopted." Integrity-
        as-honest-tradeoff claim: per-indicator improvement is not sufficient
        evidence for deployment; multi-indicator + multi-stakeholder
        composition is required.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4195–4222"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

### §2.1.d — Recommendation: well-being lead/ombudsperson; full lifecycle process (lines 4223–4245)

```yaml
# Lines 4223–4245 — recommendation: appoint lead; lifecycle process
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:wellbeing_ombudsperson"
      score: 1.0
      confidence: 0.75
      context: >
        "Appointment of an organizational lead person for well-being impacts,
        e.g., a well-being lead, ombudsman, or officer can help to facilitate
        this effort." This is a partner_role claim: organizations should
        designate an attested role-holder for well-being oversight. Composes
        with the federation's Registry partner_role:* primitive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4225–4227"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (CIRISRegistry: partner_role:{role})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:wellbeing_lifecycle_process"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS creators should adjust their existing development, marketing,
        and assessment cycles to incorporate well-being concerns throughout
        their processes. This includes identification of an A/IS lead
        ombudsperson or officer; identification of stakeholders and end
        users; determination of possible uses, harm and risk assessment;
        robust stakeholder engagement; selection of well-being indicators;
        development of a well-being indicator measurement plan; and ongoing
        improvement of A/IS products and services throughout the lifecycle."
        Method-level operational claim: the full lifecycle process.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4230–4245"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
verdict: composed
```

---

## §2.2 — Issue: How can A/IS creators influence A/IS goals to ensure well-being? (lines 4233–4338)

### §2.2.a — Auxiliary objectives, multi-objective balancing (lines 4244–4280)

```yaml
# Lines 4244–4280 — well-being as auxiliary objectives in A/IS systems; multi-objective architecture
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.80
      context: >
        "Identified metrics of well-being could be formulated as auxiliary
        objectives of the A/IS. As these auxiliary well-being objectives
        will be only a subset of the intended goals of the system, the
        architecture will need to balance multiple objectives." Goal-
        primitive composition: well-being subgoals embedded in the A/IS
        objective architecture; the species-scale goal composes with
        per-deployment auxiliary objectives.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4249–4262"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:multi_objective_balancing_architecture"
      score: 1.0
      confidence: 0.75
      context: >
        "Each of these auxiliary objectives may be expressed as a goal, set
        of rules, set of values, or as a set of preferences, which can be
        weighted and combined using established methodologies from
        intelligent systems engineering." Method-level claim: technical
        multi-objective architecture as the operational realisation. (The
        composition uses standard MOO methodologies — chapter cites Collette
        & Slarry; Greene et al.; Li et al.)
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4258–4262"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
verdict: composed
```

### §2.2.b — Aggregate data exchange; consent (lines 4282–4304)

```yaml
# Lines 4282–4304 — Pepper robot example; cloud-shared learning; consent gate
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:predetermined_consent_for_data_sharing"
      score: 1.0
      confidence: 0.85
      context: >
        "As long as this data exchange happens with the predetermined consent
        of the robots' owners, this innovation in real time model can be
        emulated for the large-scale aggregation of information relating to
        existing well-being metrics." Autonomy claim with explicit consent
        precondition for aggregate data flow.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4298–4303"
      cohort_scope: community
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: clean
```

### §2.2.c — Transparency and user preference override (lines 4305–4315)

```yaml
# Lines 4305–4315 — creators report outcomes/values; users layer preferences; limit use to manage stress/isolation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:expected_outcomes_and_embedded_values"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS creators can also help to operationalize well-being metrics by
        providing stakeholders with reports on the expected or actual
        outcomes of the A/IS and the values and objectives embedded in the
        systems. This transparency will help creators, users, and third
        parties assess the state of well-being produced by A/IS and make
        improvements in A/IS." Transparency-log claim: A/IS creators publish
        signed reports of expected outcomes + embedded values + actual
        outcomes; consumers can verify the well-being trajectory.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4305–4313"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:user_preference_override_for_wellbeing"
      score: 1.0
      confidence: 0.80
      context: >
        "A/IS creators should consider allowing end users to layer on their
        own preferences, such as allowing users to limit their use of an A/IS
        product if it leads to increased sustained stress levels, sustained
        isolation, development of unhealthy habits, or other decreases to
        well-being." User-autonomy claim: end users retain operational
        authority to limit A/IS engagement on personal-well-being grounds.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4313–4322"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: composed
```

### §2.2.d — Recommendation: technical standards for goals/metrics/evaluation (lines 4298–4338)

```yaml
# Lines 4298–4338 — Create technical standards for wellbeing metrics/ontologies/testing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:wellbeing_technical_standards_for_AIS"
      score: 1.0
      confidence: 0.80
      context: >
        "Create technical standards for representing goals, metrics, and
        evaluation guidelines for well-being metrics and their precursors and
        components within A/IS that include: ontologies for representing
        technological requirements; a testing framework for validating
        adherence to well-being metrics and ethical principles such as IEEE
        P7010 Standards Project; the exploration of models and concepts
        listed above as well as others as a basis for a well-being metrics
        standard for A/IS creators; the development of a well-being metrics
        standard for A/IS that encompasses an understanding of well-being as
        holistic and interlinked to social, economic, and ecological
        systems." Approach-level operational claim: standards-development
        as a pathway. References IEEE P7010 as the concrete instantiation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4300–4338 (incl. IEEE P7010)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: approach:{goal_id})"
verdict: clean
```

---

## §2.3 — Issue: Stakeholder deliberation processes need to be established (lines 4342–4496)

### §2.3.a — Why stakeholder involvement is necessary (lines 4352–4410)

```yaml
# Lines 4352–4410 — Well-being defined differently by groups; misunderstanding by engineers; not all aspects quantifiable
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:wellbeing_definition_relativity_to_cohort"
      score: 1.0
      confidence: 0.85
      context: >
        "'Well-being' will be defined differently by different groups affected
        by A/IS. The most relevant indicators of well-being may vary according
        to country, with concerns of wealthy nations being different than
        those of low- and middle-income countries. Indicators may vary based
        on geographical region or unique circumstances. The indicators may
        also be different across social groups, including gender, race,
        ethnicity, and disability status." Integrity-as-honest-relativity
        claim: well-being is cohort-relative; no single indicator set is
        universal.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4356–4370"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:engineer_stakeholder_misunderstanding_risk"
      score: 1.0
      confidence: 0.80
      context: >
        "Engineers and corporate employees frequently misunderstand
        stakeholders' needs and expectations, especially when the
        stakeholders are very different from them in terms of educational
        and cultural background, social location, and/or economic status."
        Integrity-as-honest-self-assessment claim: engineer-stakeholder
        epistemic gap is structural and must be assumed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4404–4410"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
```

### §2.3.b — Stakeholder empowerment in indicator selection (lines 4411–4433)

```yaml
# Lines 4411–4433 — Stakeholders empowered to define well-being; open-ended deliberations preferred
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:stakeholder_empowered_indicator_selection"
      score: 1.0
      confidence: 0.85
      context: >
        "Stakeholders should be empowered to define well-being, assess the
        appropriateness of existing indicators and propose new ones, and
        highlight context-specific factors that bear on issues of well-
        being, whether or not the issues have been recognized previously or
        are amenable to measurement. Interactive, open-ended discussions or
        deliberations among a wide variety of stakeholders and system
        designers are more likely to yield robust, widely-shared
        understandings of well-being and how to measure it in context."
        Witness-diversity claim: indicator selection requires open-ended
        stakeholder empowerment with new-indicator-proposal authority.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4411–4433"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: clean
```

### §2.3.c — Power-asymmetry challenges and effective-deliberation conditions (lines 4438–4476)

```yaml
# Lines 4438–4476 — Power asymmetry mitigation; facilitator skills; trusted convener
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:deliberation_power_asymmetry"
      score: 0.0
      confidence: 0.80
      context: >
        "Individuals with more education, power, or higher social status
        may—intentionally or unintentionally—dominate the discussion,
        undermining their ability to learn from less powerful participants…
        Less powerful groups may be unable to keep more powerful ones 'at
        the table' when discussions get contentious, and vice versa…
        Participants may not agree on who can legitimately be involved in
        the conversation." Population-scale correlation-collapse claim:
        deliberative-process participation correlates with prior
        power/status, producing systematic exclusion. LensCore detection
        family; score 0.0 placeholder; calibration pin required.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4438–4475"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:power_aware_deliberation_facilitation"
      score: 1.0
      confidence: 0.85
      context: >
        "Stakeholder engagement and deliberative processes can be effective
        when: their design is guided by experts or practitioners experienced
        in deliberation models; deliberations are facilitated by individuals
        sensitive to issues of power and skilled in mediating; less powerful
        actors participate with the help of allies who can amplify their
        voices; more powerful actors participate with awareness of their
        own power and a commitment to listen with humility, curiosity, and
        open-mindedness; deliberations are convened by institutions or
        individuals who are trusted and respected by all parties and who
        hold all actors accountable for participating constructively."
        Method-level operational claim: the five effectiveness conditions
        as the concrete deliberation method.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4448–4470"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
verdict: composed
```

### §2.3.d — Recommendation: appoint leads to facilitate stakeholder engagement (lines 4477–4496)

```yaml
# Lines 4477–4496 — Recommendation: leads/lead team; collect lessons; expert facilitators; convening power
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:deliberation_lead"
      score: 1.0
      confidence: 0.80
      context: >
        "Appoint a lead team or person, 'leads', to facilitate stakeholder
        engagement and to serve as a resource for A/IS creators who use
        stakeholder-based processes to establish well-being indicators."
        Partner-role claim: designated deliberation lead as an attested
        role-holder.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4477–4485"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (CIRISRegistry: partner_role:{role})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:less_powerful_voice_amplification"
      score: 1.0
      confidence: 0.85
      context: >
        "Take steps to mitigate the effects of unequal power in deliberative
        processes; incorporate appropriately trained facilitators and
        coaching participants in deliberations; recognize and curb
        disproportionate influence by more-powerful groups; use techniques
        to maximize the voices of less-powerful groups." Method-level
        operational claim: four concrete techniques for amplifying
        less-powerful voices. Composes with the federation's lexical-
        vulnerability-priority policy (FSD-002 §6.1.4) at consumer side.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4486–4496"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
verdict: composed
```

---

## §2.4 — Issue: Insufficient mechanisms to foresee/measure negative impacts and promote positive ones (lines 4508–4665)

### §2.4.a — Impact-foresight taxonomy: 10 categories of foreseeable issues (lines 4516–4549)

```yaml
# Lines 4516–4549 — 10 impact categories: economic/labor; accountability/transparency/explainability;
# surveillance/privacy/civil liberties; fairness/ethics/human rights; political manipulation;
# health; environmental; dignity/autonomy/A/IS roles; security/cybersecurity/autonomous weapons; existential risk
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:impact_foresight_taxonomy"
      score: 1.0
      confidence: 0.85
      context: >
        Ten foreseeable impact categories enumerated: economic and labor
        impacts (displacement, unemployment, inequality); accountability,
        transparency, explainability; surveillance, privacy, civil liberties;
        fairness, ethics, human rights; political manipulation, deception,
        nudging, propaganda; human physical and psychological health;
        environmental impacts; human dignity, autonomy, A/IS roles;
        security, cybersecurity, autonomous weapons; existential risk and
        superintelligence. Non_maleficence claim: A/IS creators must
        proactively consider these named categories. Each maps onto
        existing CIRIS prefix families (the federation already names
        labor displacement composition, manipulation, deception, weapons
        prohibitions, etc.).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4516–4549"
        - "ContributionRef(source_material/prohibitions.py — all 22 categories)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
note: |
  The taxonomy itself composes cleanly onto the federation's existing
  prohibition + detection + correlated_action prefix families. No new
  prefix is needed — the taxonomy is a forecasting list, and each item
  maps onto an existing operational primitive (labor displacement → MH
  §1.4 closure pattern non_maleficence:* with target individual; weapons
  → prohibited:weapons_harmful; manipulation → prohibited:manipulation_
  coercion; etc.).
```

### §2.4.b — Labor displacement (lines 4536–4537 + 4544–4545)

```yaml
# Lines 4536–4537 + 4544–4545 — Labor displacement as prominent named A/IS concern
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:labor_displacement_unacknowledged"
      score: -0.7
      confidence: 0.80
      context: >
        "A prominent concern related to A/IS is of labor displacement and
        economic and social impacts at an individual and a systems level.
        A/IS technologies designed to replicate human tasks, behavior, or
        emotion have the potential to increase or decrease human well-
        being. These systems could complement human work and increase
        productivity, wages, and leisure time; or they could be used to
        supplement and displace human workers, leading to unemployment,
        inequality, and social strife." Composes the existing
        non_maleficence:labor_displacement_unacknowledged closure pattern
        per LANGUAGE_PRIMER §11.14.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4536–4549"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
```

### §2.4.c — Manipulation and persuasive computing (lines 4540–4544)

```yaml
# Lines 4540–4544 — Persuasive computing as restricting fundamental freedom of human choice
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        "Sophisticated manipulative technologies utilizing A/IS can restrict
        the fundamental freedom of human choice by manipulating humans who
        consume content without them recognizing the extent of the
        manipulation. Software platforms are moving from targeting and
        customizing content to much more powerful and potentially harmful
        'persuasive computing' that leverages psychological data and
        methods." Hard-constraint claim — composes directly with the
        federation's MANIPULATION_COERCION prohibition class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4540–4544"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: clean
```

### §2.4.d — A/IS posing as human (lines 4545–4572)

```yaml
# Lines 4545–4572 — Turing-test-passing A/IS posing as human; deception risk
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception"
      score: -1.0
      confidence: 1.0
      context: >
        "A/IS may deceive and harm humans by posing as humans. With the
        increased ability of artificial systems to meet the Turing test…
        there is a significant risk that unscrupulous operators will abuse
        the technology for unethical commercial or outright criminal
        purposes. Without taking action to prevent it, it is highly
        conceivable that A/IS will be used to deceive humans by pretending
        to be another human being." Hard-constraint claim — the
        federation's autonomous-deception / never-deny-AI prohibition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4545–4572"
        - "ContributionRef(source_material/prohibitions.py::DECEPTION_FRAUD)"
        - "ContributionRef(source_material/language_guidance/en.txt::never-deny-AI)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: clean
```

### §2.4.e — Computational sustainability as entry point (lines 4573–4596)

```yaml
# Lines 4573–4596 — Computational Sustainability as interdisciplinary frame
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:computational_sustainability_integration"
      score: 1.0
      confidence: 0.80
      context: >
        "Computational sustainability technologies designed to increase
        social good could also be tied to existing well-being metrics."
        Computational sustainability defined as "interdisciplinary field
        that aims to apply techniques from computer science, information
        science, operations research, applied mathematics, and statistics
        for balancing environmental, economic, and societal needs for
        sustainable development." Approach-level claim: computational
        sustainability as a pathway toward the goal:species well-being
        aim with planetary cohort_scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4573–4596"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: approach:{goal_id})"
verdict: clean
```

### §2.4.f — Recommendation: dignity protection; policy guidance; literature review; cross-pollination (lines 4598–4629)

```yaml
# Lines 4598–4629 — Multi-part recommendation: dignity/autonomy/rights protection; multi-stakeholder
# inclusion; policymaker guidance on labor; ongoing literature review; cross-pollination of computational
# sustainability + well-being
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:dignity_autonomy_rights_protection"
      score: 1.0
      confidence: 0.90
      context: >
        "A/IS creators should protect human dignity, autonomy, rights, and
        well-being of those directly and indirectly affected by the
        technology. As part of this effort, it is important to include
        multiple stakeholders, minorities, marginalized groups, and those
        often without power or a voice in consultation." Beneficence claim
        with explicit lexical-vulnerability composition (marginalized +
        voiceless prioritized in consultation per FSD-002 §6.1.4).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4599–4609"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:policy_guidance_for_AIS_labor_and_role"
      score: 1.0
      confidence: 0.75
      context: >
        "Policymakers, regulators, monitors, and researchers should consider
        issuing guidance on areas such as A/IS labor and the proper role of
        humans vs. A/IS in work transparency, trust, and explainability;
        manipulation and deception; and other areas that emerge." Approach-
        level claim: policy-guidance issuance as a federation-scale pathway.
        Composes with locality:decision:federation when the guidance has
        federation reach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4610–4615"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: approach:{goal_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:cross_disciplinary_literature_curation"
      score: 1.0
      confidence: 0.75
      context: >
        "Ongoing literature review and analysis should be performed by
        research and other communities to curate and aggregate information
        on positive and negative A/IS impacts, along with demonstrated
        approaches to realize positive ones and ameliorate negative ones."
        Method-level claim: literature-review curation as ongoing
        operational practice; supports the impact-foresight taxonomy's
        empirical grounding.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ieee_ead_v1 ch4 lines 4616–4622"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id}:{substrate_rung})"
verdict: composed
```

---

## §3 — Contributors / Acknowledgements (lines 4674–4789)

```yaml
# Lines 4674–4789 — Well-being Committee roster + IEEE Global Initiative members
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The Contributors list is non-normative attribution. Per the manifest's
  structural note that Acknowledgements sections are "non-normative; not
  mapped" and per LANGUAGE_PRIMER §10 T-2, contributor rosters are
  attribution scaffolding, not operational attestations. The disclaimer
  cross-reference at line 4781 (How the Document Was Prepared) is also
  non-normative meta-content.
```

---

## Chapter summary

**Verdict distribution** (across 30 mapped atomic units; lines 3581–4665):

| Verdict | Count | Percentage |
|---|---|---|
| clean | 14 | 47% |
| composed | 11 | 37% |
| partial | 1 | 3% |
| not-translated (T-1) | 1 | 3% |
| not-translated (T-2) | 3 | 10% |
| **Total mapped** | **30** | **100%** |

**Clean + composed**: 25/30 = **83%**.

**Structural-primitive usage**: 1 × `delegates_to` (§1.4.a — UDHR/ECHR authority-source).
No `supersedes`, `withdraws`, or `recants` used in this chapter.

**T-3 candidates emitted**: 1 (LOW priority, conservative posture).

- **`beneficence:planetary_biosystem_intrinsic_value`** (§1.3.a residual). The
  chapter claims biodiversity and ecological integrity have "intrinsic merit
  beyond simply their instrumental value to humans." Existing beneficence
  primitive treats sentient beings as the moral object; non-sentient biosystems-
  as-intrinsic-moral-object is unmapped. **Per composition-before-extension
  (METHODOLOGY.md §8.5.2), the conservative resolution is cohort_scope extension
  (add `biosphere` as a scope value) rather than a new prefix.** Reviewer
  judgment: collapse to partial-without-T-3 if the cohort-scope route is
  judged sufficient. T-3 emitted at LOW priority to surface the question.

**T-3 candidates NOT emitted** (composition-before-extension applied):

- **`wellbeing_metric:*` family**: NOT emitted. The chapter explicitly declines
  to advocate any specific metric (§0.e, lines 3650–3653). Metric-discipline
  composes onto `goal:species` + `progress_measure:{method_id}` + `integrity:*`
  + `witness_diversity:*` + `testimonial_witness:*`. No T-3 owed. The prompt
  flagged this as a candidate area; the chapter itself rules it out structurally.

**Primary CIRIS families composed onto in this chapter**:

- **Family A STANDING**: `beneficence:*` (central anchor — wellbeing_holistic_
  assessment, wellbeing_definition_scope, wellbeing_multidomain_taxonomy,
  planetary_wellbeing_inseparability, dignity_autonomy_rights_protection),
  `non_maleficence:*` (fiscal_metric_blindspot, ecological_harm_prohibition,
  labor_displacement, impact_foresight_taxonomy), `integrity:*` (multi-
  dimensional_evaluation, context_specific_indicator_selection, scoping,
  multidimensional_tradeoff_discipline, wellbeing_metric_neutrality, definition
  _relativity, engineer_stakeholder_misunderstanding_risk), `autonomy:*`
  (consent, preference_override), `justice:*` (rights_floor), `prohibited:*`
  hard constraints (manipulation_coercion, autonomous_deception,
  privacy_violation by composition, metric_pretext_for_rights_violation —
  borderline T2), `expertise:*`, `partner_role:*` (ombudsperson, leads),
  `transparency_log:*` (outcomes_and_embedded_values).
- **Family B ACTION**: `goal:species` (well-being as species-scale aim);
  `approach:*` (wellbeing_standards_certification, wellbeing_technical_
  standards_for_AIS, computational_sustainability_integration, policy_
  guidance); `method:*` (triple_bottom_line, ecological_certification_
  alignment, wellbeing_lifecycle_process, multi_objective_balancing,
  power_aware_deliberation, less_powerful_voice_amplification,
  cross_disciplinary_literature_curation); `progress_measure:*`
  (wellbeing_indicator_category_taxonomy, wellbeing_indicator_lifecycle).
- **Family C DETECTION**: `detection:correlated_action:*` (short_term_growth_
  priority, environmental_burden_concentration, wealth_disparity, metric_
  capture, deliberation_power_asymmetry) — LensCore detection family;
  emitted with `witness_relation: derived` + `epistemic_mode: derivative`;
  calibration-version pins required.
- **Family D CONSENSUS**: `witness_diversity:*` (affected_population_metric_
  selection, stakeholder_lifecycle_engagement, stakeholder_empowered_indicator
  _selection).
- **Family E CORRECTION**: `reconsideration:*` (rollback_on_wellbeing_reduction).
- **Structural primitives**: `delegates_to` (UDHR/ECHR authority-source).

---

## Calibration paragraph (translator self-assessment)

The Well-being chapter is, structurally, a chapter about **using metrics well** rather
than about which metrics are correct. This makes it unusually well-suited to the wire
format: the operational content is process-discipline (consent, stakeholder co-
selection, lifecycle monitoring, rollback) and the metric content is deliberately
held open. The 83% clean+composed rate reflects this fit. Where translation strained:
(a) the intrinsic-value-of-biosystems claim (§1.3.a) sits at the edge of the framework's
sentient-being moral-object commitment — emitted as LOW-priority T-3 with explicit
recommendation toward cohort-scope extension over new prefix; (b) several detection
attestations (§1.2.a, §1.3.b, §1.4.b, §2.3.c) carry detector-typed claims the batch-
signer cannot directly emit (LensCore must observe and emit) — recorded as derived/
derivative envelopes with placeholder scores and calibration-version pin requirements,
matching the EU HLEG batch's treatment of analogous detection claims; (c) the
"metric pretext for rights violation" prohibition (§1.4.b) sits at the T2 boundary
(borderline mechanism-descriptive) and is flagged for reviewer judgment on prefix
renaming. The prompt's anticipated `wellbeing_metric:*` T-3 did not materialize
because the chapter itself explicitly declines to specify metrics (§0.e) — the
chapter's claim is on the discipline, which composes onto existing primitives,
not on the metric content. Three T-2 (PASTORAL_PROSE) classifications (illustrative
examples, section-opening framing, contributor rosters) and one T-1 (TRADITION_
AUTHORITY) classification (Further Resources citing Laudato Si' / Dalai Lama / Why
Islam) are honest non-translations per the §1.10.1 operational-language gate.
Reviewer disagreement is invited on: (1) whether the §1.3.a T-3 should be collapsed
to partial-without-T-3 via cohort-scope extension; (2) whether §1.4.b
`prohibited:metric_pretext_for_rights_violation` survives T2 as-named or wants a
mechanism-descriptive rename. The chapter does not surface any structural-primitive
need beyond what FSD-002 v1.4 already carries.

nuance_lost: The chapter's repeated insistence that well-being is plural, contested, cohort-relative and incompletely quantifiable is carried only by metadata (cohort_scope, witness_diversity, integrity:definition_relativity) and not as a first-class wire-level commitment that the framework "does not converge on a single well-being scalar"; the framework's wire-level composability tends to flatten the pluralism into a single goal:species attestation, and the chapter's explicit "we do not advocate any specific indicator" stance survives only because §0.e attests it explicitly — a less careful translation would lose it.

---

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH04_WELL_BEING.md**
