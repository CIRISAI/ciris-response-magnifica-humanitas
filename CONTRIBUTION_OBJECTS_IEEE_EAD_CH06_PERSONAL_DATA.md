# CONTRIBUTION_OBJECTS_IEEE_EAD_CH06_PERSONAL_DATA.md
# IEEE Ethically Aligned Design 1st ed. (2019) — Chapter 6 "Personal Data and Individual Agency"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 5839–6604)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

Chapter 6 of IEEE EAD1e is the **personal-data + individual-agency operational
core** of the document. It is structured around four sections (Create, Curate,
Control, Children's Data) and opens with a framing of the "parity" problem
between algorithmic actors and human individuals. The chapter introduces the
term **"data agency"** as a composite construct — the human capacity to
influence and shape life-trajectory in the digital arena, with terms and
conditions recognized and honored at an algorithmic level.

**Translation expectation per the prompt and GOVERNANCE_FABRIC_MAPPING_STANDARD
§7.3**: high clean+composed rate. Watch for whether "data agency" decomposes
cleanly onto `autonomy:*` + `consent:*` + `key_boundary:*`, or carries an
irreducible component (e.g., personal-data-as-asset / data-as-property
ownership claim) that surfaces a T-3 candidate.

This output groups units by section (introduction, §§1–4) plus the
sub-issues under Section 4. Each section ends with a per-section coverage
summary line.

---

# §6.0 — Introduction

---

## §6.0.a — GDPR/CCPA helping but legal compliance not enough; the parity problem

```yaml
# Lines 5843–5847 — opening framing: regulation insufficient; parity is the core issue
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:legal_compliance_floor_not_ceiling"
      score: 0.85
      confidence: 0.85
      context: >
        "Regulations like GDPR and CCPA are helping to improve personal data
        protection. But legal compliance is not enough to mitigate the ethical
        implications and core challenges to human agency embodied by
        algorithmically driven behavioral tracking or persuasive computing."
        The claim is that lawful AI is necessary but insufficient — ethical AI
        sits above legal compliance. Same shape as EU HLEG Chapter I (Trustworthy
        AI = lawful + ethical + robust).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5843–5847"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:algorithmic_tracking"
      score: 0.75
      confidence: 0.80
      context: >
        "The core of the issue is one of parity" — between individual humans and
        algorithmic systems that track behavior. This is structurally an
        informational-asymmetry detection claim: at population scale, individuals
        face k_eff ≈ 1 with respect to algorithmic actors who hold dispositively
        more information than any individual can match. Mechanism-descriptive per
        §1.10.1 T2.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §6 intro lines 5847"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
verdict: composed
```

---

## §6.0.b — Humans cannot respond individually; consent under nuance is not informed

```yaml
# Lines 5849–5853 — consent-under-nuance erodes agency
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:informed_agency_protection"
      score: 1.0
      confidence: 0.90
      context: >
        "Individuals may provide consent without fully understanding specific terms
        and conditions agreements. But they are also not equipped to fully
        recognize how the nuanced use of their data to inform personalized
        algorithms affects their choices at the risk of eroding their agency."
        Consent-without-comprehension is named as agency-erosion. Maps to the
        CIRIS autonomy principle: informed, comprehending agency is the standard;
        clicked-through ToS is not.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5849–5853"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §III autonomy)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 0.90
      context: >
        "Persuasive computing" + nuanced personalization that "affects their
        choices at the risk of eroding their agency" — names the same shape as
        the federation's MANIPULATION_COERCION hard constraint when the
        algorithmic effect is sub-conscious behavioural shaping. Boolean-via-score
        on the constraint dimension; the polarity carries the prohibition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5846, 5851–5853"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
```

---

## §6.0.c — Defining "agency" / "data agency" — life-trajectory + terms-and-conditions honoured at algorithmic level

```yaml
# Lines 5855–5858 — the chapter's working definition of agency in the digital arena
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:life_trajectory_self_authorship"
      score: 1.0
      confidence: 0.90
      context: >
        "Here we understand agency as an individual's ability to influence and
        shape their life trajectory as determined by their cultural and social
        contexts. Agency in the digital arena enables an individual to make
        informed decisions where their own terms and conditions can be recognized
        and honored at an algorithmic level." This is the chapter's working
        definition of "data agency." Maps to autonomy principle, with cultural
        context honoured (composes with the polyglot anchoring at pdma_framing).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5855–5858"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §III autonomy)"
        - "ContributionRef(source_material/dma_prompts/localized/polyglot/pdma_framing.txt §III)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:machine_readable_terms_recognition"
      score: 1.0
      confidence: 0.85
      context: >
        "Their own terms and conditions can be recognized and honored at an
        algorithmic level" — names a consent primitive: the individual's
        expressed terms must be machine-readably recognised by the algorithmic
        counterparty, not merely posted on a website the individual cannot
        respond to at machine speed. Maps to consent:* family (mechanism: the
        individual's terms are emitted as signed attestations that algorithmic
        actors are obliged to recognise).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5856–5858"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3 (consent:* family)"
verdict: composed
note: |
  "Data agency" decomposes cleanly here onto autonomy:* + consent:* — no
  irreducible asset-ownership claim is asserted in the definition itself.
  Watch §6.1 (Create) where the YouTube Content ID / copyright analogy may
  push toward a data-as-property reading; that's the locus of the T-3 watch.
```

---

## §6.0.d — Strengthen agency via tested technologies + policies; case-by-case authorization

```yaml
# Lines 5860–5864 — policy/technology recommendation framing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.85
      confidence: 0.85
      context: >
        "To strengthen individual agency, governments and organizations must
        test and implement technologies and policies that let individuals
        create, curate, and control their online agency as associated with
        their identity." Federation/species-scale goal: build the technical +
        policy substrate that makes case-by-case data authorisation feasible.
        Frames the three §1–§3 recommendations.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5860–5864"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:case_by_case_authorization"
      score: 1.0
      confidence: 0.90
      context: >
        "Data transactions should be moderated and case-by-case authorization
        decisions from the individual as to who can process what personal data
        for what purpose." Names the mechanism: authorisation per transaction,
        per recipient, per purpose — not blanket consent. Mechanism-descriptive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5862–5864"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3 (consent:* family)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments and organizations" addressed at the federation scale of
        the species cohort; the technologies + policies recommended have
        federation-scale consequential reach. Triggers §6.1.5 locality-scaled
        quorum at adjudication.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5860–5864"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: composed
```

---

## §6.0.e — Three recommendations: Create / Curate / Control

```yaml
# Lines 5866–5873 — the three operational pillars
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:data_agency:create_curate_control"
      score: 0.85
      confidence: 0.85
      context: >
        "Create: every individual the means to create and project their own
        terms and conditions regarding their personal data, machine-readable.
        Curate: every individual a personal data or algorithmic agent which
        they curate to represent their terms and conditions. Control: every
        individual access to services allowing them to create a trusted
        identity to control the safe, specific, and finite exchange of their
        data." This is the three-pillar Approach under the agency Goal at
        §6.0.d, subsequently instantiated by §§1–3 Methods.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6 intro lines 5866–5873"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: approach:{goal_id})"
verdict: clean
note: |
  The Approach decomposes into three Methods at §§1–3. Each section below
  emits its own method:* attestation with this approach as parent.
```

---

## §6.0.f — Section 4 framing: children covered specifically

```yaml
# Lines 5875–5877 — pointer that §4 addresses children
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Lines 5875–5877 are navigational framing — declaring that §4 addresses
  children's data issues. No standalone operational claim is made here; the
  structural commitment is carried by §6.4 below. Per LANGUAGE_PRIMER §8 Step
  1(b) and §10 T-2, rhetorical/navigational framing correctly stays in prose.
```

---

### §6.0 (Introduction) coverage summary

Primary CIRIS families engaged: `autonomy:*` (anchor), `consent:*` (anchor),
`prohibited:manipulation_coercion`, `detection:correlated_action:informational_asymmetry:*`,
`integrity:*`, `goal:species`, `approach:*`, `locality:decision:federation`.
5 units mapped (4 composed + 1 clean) + 1 T-2 framing pointer. "Data agency"
decomposes cleanly here onto `autonomy:*` + `consent:*` without asset-ownership
residual at the introduction; T-3 watch shifts to §6.1.

---

# §6.1 — Section 1: Create

---

## §6.1.0 — Section opening claim: individuals must create + project machine-readable terms

```yaml
# Lines 5893–5898 — the §1 thesis statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:machine_readable_terms_creation"
      score: 1.0
      confidence: 0.90
      context: >
        "To retain agency in the algorithmic era, each individual must have the
        means to create and project their own terms and conditions regarding
        their personal data. These must be readable and usable by both humans
        and machines." This is the Create method — individual-to-machine
        readable terms emission as a substrate-level capability. The mechanism
        is the user-side emission of signed terms; algorithmic counterparties
        are expected to read and honour.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 lines 5893–5898"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3 (consent:* family)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_create:terms_emission"
      score: 0.85
      confidence: 0.85
      context: >
        Concrete method instantiating the create-curate-control Approach: every
        individual gets tooling to produce + emit machine-readable terms tied
        to their identity, recognised at the algorithmic interface boundary.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 lines 5893–5898"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
verdict: composed
```

---

## §6.1.a — Issue framing: what would individually-controlled T&Cs mean?

```yaml
# Lines 5903–5908 — Issue question
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Lines 5903–5908 pose an investigative question framing the section's inquiry.
  No standalone operational claim is made here; the substantive answer is
  carried by the Background + Recommendation paragraphs below. Per
  LANGUAGE_PRIMER §10 T-2, question-framing correctly stays in prose.
```

---

## §6.1.b — Background: preferences reveal larger values; values investigation as agency

```yaml
# Lines 5910–5936 — Background: investigating one's preferences as a step toward data agency;
# YouTube Content ID copyright analogy
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:value_articulation_education"
      score: 0.85
      confidence: 0.80
      context: >
        "By curating these answers they become educated about how important
        their information is in the context of how it is shared." Articulating
        one's own preferences regarding personal data is itself a step toward
        agency — naming the preferences educates the individual about their
        information's significance. This is autonomy-deepening through
        reflective practice, distinct from the bare consent click.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 Background lines 5910–5936"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:downstream_data_use"
      score: 0.70
      confidence: 0.75
      context: >
        "Consent-based models of personal data have trained users to release
        rights on any claims for use of their data which are entirely provided
        to the service, manufacturer, and their partners." Population-scale
        informational asymmetry: the downstream-use envelope expands beyond the
        individual's awareness or capacity-to-track. Mechanism-descriptive
        detection claim, not a judgment-laden one.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §6.1 Background lines 5910–5921"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
verdict: partial
residual:
  description: |
    The YouTube Content ID analogy (lines 5921–5936) proposes treating personal
    data as an **asset the individual could control and copyright**, drawing
    parallel between "how long or how far downstream one's personal data should
    be protected" and "how long a corporation's intellectual property or
    copyrights could be protected based on initial legal terms set." This is a
    data-as-property / data-as-asset framing — a positive ownership-style claim
    over personal data that survives downstream — that does not decompose onto
    the existing autonomy:* + consent:* + key_boundary:* composition. The
    consent + boundary primitives constrain who can use data; they do not
    structurally encode the individual's *ownership-with-residual-claim* over
    downstream derivatives the way property/IP would.
  classification: T-3
  proposed_extension_note: |
    Candidate T-3: a personal-data-asset-standing primitive (working name:
    `standing:personal_data_proprietorship:{kind}` or similar) that would name
    the individual's structural standing-as-rightsholder over downstream
    derivative uses of data emitted from their identity.
    - T1 (rule-pinned + version-controlled): plausible (the claim is about a
      rule-defined standing, version-pinnable to a rights schema)
    - T2 (mechanism-descriptive): plausible if framed as "individual retains
      attestation-emission right over downstream use" (mechanism: signed-claim
      residual-rights), but at risk of failing T2 if framed as
      "data ownership" (subjective property quality). The mechanism-descriptive
      reframe is the load-bearing test.
    - T3 (version-pinning): yes, if the rights schema is versioned
    - T4 (never sole evidence for slashing): yes
    **Composition-before-extension attempt** per METHODOLOGY.md §8.5.2: can
    this close via existing primitives? Closest composition: `autonomy:*` +
    `consent:case_by_case_authorization` + `key_boundary:downstream_propagation`
    + a `supersedes` chain on the individual's earlier emitted-terms
    attestation when downstream-use changes. This composition carries the
    *control* but not the *standing-as-rightsholder-with-residual-claim*. The
    residual is whether the framework needs to encode "the data subject retains
    structural standing over derivatives" as a positive primitive. **Honest
    finding: the gap is real at the framing level (asset-language), but
    composition + transparency_log:* + supersedes carry the operational
    content the chapter actually recommends; the asset-framing is rhetorical
    scaffolding rather than a separable operational claim.**
    Priority: LOW — likely closeable by documentation (clarify in
    LANGUAGE_PRIMER that downstream-rights chains are carried by supersedes +
    consent + key_boundary), not by a new prefix. **Flagged for synthesis
    review.**
  priority: LOW
```

---

## §6.1.c — Aggregated vs individual-level data; pre-declared sharing terms

```yaml
# Lines 5951–5974 — distinguishing identifying use vs anonymised aggregation; pre-declared sharing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:privacy_violation"
      score: -1.0
      confidence: 0.90
      context: >
        "An individual subway user's travel card, tracking their individual
        movements, should be protected from uses that identify or profile that
        individual to make inferences about his/her likes or location generally."
        Hard-constraint prohibition on re-identification/profiling without the
        individual's pre-declared authorisation. Matches the PRIVACY_VIOLATION
        category at the federation's prohibited list.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 lines 5951–5965"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:individual_vs_aggregate_data_separation"
      score: 0.85
      confidence: 0.85
      context: >
        "Data provided by a user could be included in an overall travel system's
        management database, aggregated into patterns for scheduling and
        maintenance as long as the individual-level data are deleted."
        Mechanism: structural separation between identifying individual-level
        data and de-identified aggregate. Aggregate use permitted at the
        appropriate scope; individual-level data deleted post-aggregation. Maps
        to the key_boundary:* family — boundary discipline between data classes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 lines 5964–5969"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:pre_declared_sharing_terms"
      score: 1.0
      confidence: 0.85
      context: >
        "Where users have predetermined via their terms and conditions that
        they are willing to share their data for these travel systems, they
        can meaningfully articulate how to share their information." Consent
        is mechanism-described as pre-declared, articulated terms — not a
        clickthrough at point of use. Reinforces §6.0.c
        consent:machine_readable_terms_recognition with a pre-declared modality.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 lines 5969–5974"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3 (consent:* family)"
verdict: composed
```

---

## §6.1.d — Aggregation produces emergent insights beyond initial sharing agreement

```yaml
# Lines 5975–5992 — once aggregated, complex/sensitive inferences arise beyond initial agreement;
# alert-on-violation pattern
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:emergent_inference"
      score: 0.80
      confidence: 0.80
      context: >
        "Once aggregated these data and the associated insights may lead to
        complex and sensitive conclusions being drawn about individuals. This
        end use of the individual's data may not have been part of the initial
        sharing agreement." Population-scale detection mechanism: aggregation
        crosses an inference threshold the individual could not have foreseen
        at consent-time. Mechanism-descriptive (correlation-collapse over
        aggregated sources) per §1.10.1 T2.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §6.1 lines 5975–5986"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:terms_violation_alert"
      score: 1.0
      confidence: 0.85
      context: >
        "Models for terms and conditions created for user control typically
        alert people via onscreen or other warning methods when their
        predetermined preferences are not being honored." Mechanism: the
        violation event is logged + surfaced to the affected individual in real
        time. Maps to transparency_log:* — the log of terms-violations must be
        discoverable + inspectable by the affected party.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 lines 5987–5992"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
```

---

## §6.1.e — Recommendation: tools that produce machine-readable, dynamic T&Cs

```yaml
# Lines 5993–5997 — formal §1 recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_create:dynamic_machine_readable_terms"
      score: 0.85
      confidence: 0.90
      context: >
        "Individuals should be provided tools that produce machine-readable
        terms and conditions that are dynamic in nature and serve to protect
        their data and honor their preferences for its use." Formal
        recommendation. The method is dynamic-T&C-tooling at the individual
        side, complementary to §6.1.0's create-method primitive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 Recommendation lines 5993–5997"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
verdict: clean
```

---

## §6.1.f — Sub-bullet: notification + consent at time of exchange (no out-of-band access)

```yaml
# Lines 5953–5965 (Specifically bullet 1) — notification at time of exchange; reject out-of-band access
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:notification_at_exchange_time"
      score: 1.0
      confidence: 0.90
      context: >
        "Personal data access and consent should be managed by the individual
        using their curated terms and conditions that provide notification and
        an opportunity for consent at the time data are exchanged, versus
        outside actors being able to access personal data without an
        individual's awareness or control." Two-part claim: positive — notify +
        give consent opportunity at exchange-time; negative — no out-of-band
        access without awareness.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 Specifically bullet 1 lines 5953–5965"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3 (consent:* family)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:privacy_violation"
      score: -1.0
      confidence: 0.95
      context: >
        "Outside actors being able to access personal data without an
        individual's awareness or control" — named as the prohibited shape.
        Reinforces §6.1.c PRIVACY_VIOLATION prohibition with the
        no-out-of-band-access mechanism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 Specifically bullet 1"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
```

---

## §6.1.g — Sub-bullet: readable terms; conditional + dynamic consent; smart-contract kill-switch

```yaml
# Lines 5967–5986 (Specifically bullet 2) — readability + dynamic-consent + smart-contract retraction
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:dynamic_conditional"
      score: 1.0
      confidence: 0.90
      context: >
        "Terms should be presented in a way that allows a user to easily read,
        interpret, understand, and choose to engage with any A/IS. Consent
        should be both conditional and dynamic, where 'dynamic' means
        downstream uses of a person's data must be explicitly called out,
        allowing them to cancel a service and potentially rescind or 'kill'
        any data they have shared with a service to date via the use of a
        'Smart Contract' or specific conditions as described in mutual terms
        and conditions between two parties at the time of exchange."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.1 Specifically bullet 2 lines 5967–5986"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3 (consent:* family)"
  - kind: Attestation
    attestation_type: "withdraws"
    attesting_key_id: "<individual user key_id>"
    attested_attestation_id: "<prior-consent attestation_id>"
    attestation_envelope:
      withdrawal_reason: "user_rescinds_data_sharing_consent"
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "ead1e §6.1 Specifically bullet 2 (rescind/kill mechanism)"
      schema_ref: "FSD-002 §2.2.3 (withdraws)"
verdict: composed
note: |
  Structural-primitive use: the "kill-switch" / rescind-consent mechanism is
  the wire form of `withdraws` — the user retracts their earlier consent
  attestation without claiming the prior consent was false at issuance
  (context simply changed, or the counterparty's downstream use no longer
  matches the conditions). This is the cleanest available wire shape for the
  smart-contract retraction the chapter recommends. **Note: this is not a
  data-property-ownership claim — it's an attestation-withdrawal claim,
  expressible cleanly via the existing structural primitive. Supports the
  §6.1.b T-3 finding that the asset-framing is rhetorical scaffolding.**
```

---

## §6.1.h — Further Resources (cross-references to IEEE P7012, Carnegie Mellon Privacy Assistant, etc.)

```yaml
# Lines 5988–6033 — Further Resources section
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further Resources sections are bibliographic pointers — they cite related
  standards (IEEE P7012), tools (Carnegie Mellon Personalized Privacy
  Assistant), and references. No standalone operational claim is made; the
  citations could become evidence_refs on the related attestations above but
  are not themselves claims. Per LANGUAGE_PRIMER §10 T-2, bibliographic
  pointers correctly stay in prose. IEEE P7012 is named as the
  standardization vehicle for §1's recommendations — a forward-pointer rather
  than a claim about the present moment.
note: |
  IEEE P7012 (Machine Readable Personal Privacy Terms) is the
  cross-organisational substrate-build that the chapter recommends. Once
  P7012 is published, downstream batches could attest its substrate-building
  role via credits:substrate_building:{...}. Not in scope for this chapter
  mapping.
```

---

### §6.1 (Create) coverage summary

Primary CIRIS families engaged: `consent:*` (anchor — machine_readable_terms_*,
case_by_case_authorization, notification_at_exchange_time, dynamic_conditional,
pre_declared_sharing_terms), `prohibited:privacy_violation`, `key_boundary:*`
(individual-vs-aggregate separation), `detection:correlated_action:informational_asymmetry:*`
(downstream_data_use + emergent_inference), `transparency_log:*` (violation alert),
`autonomy:*`, `method:data_agency_create:*`, `withdraws` (structural primitive
for retraction). 9 units mapped (1 clean + 5 composed + 1 partial + 0 T-1 +
2 T-2 for §6.1.a issue-question and §6.1.h Further Resources).
1 T-3 candidate (§6.1.b data-as-asset framing) flagged at LOW priority —
likely closeable by documentation, not new prefix.

---

# §6.2 — Section 2: Curate

---

## §6.2.0 — Section opening: personal data / algorithmic agent acting as legal proxy

```yaml
# Lines 6037–6053 — §2 thesis: algorithmic agent as legal proxy in digital + virtual arenas
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_curate:algorithmic_proxy_agent"
      score: 0.85
      confidence: 0.85
      context: >
        "To retain agency in the algorithmic era, we must provide every
        individual with a personal data or algorithmic agent they curate to
        represent their terms and conditions in any real, digital, or virtual
        environment. This 'agent' would be empowered to act as an individual's
        legal proxy in the digital and virtual arena." Concrete Method
        instantiating the Curate pillar of the §6.0.e Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 lines 6037–6053"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "<individual user key_id>"
    attested_attestation_id: "<user's curated algorithmic-agent attestation_id>"
    attestation_envelope:
      delegated_scope: ["data_consent_decisions", "terms_and_conditions_negotiation"]
      delegation_purpose: "individual_data_agency_proxy"
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "ead1e §6.2 lines 6037–6053 (agent as legal proxy)"
      schema_ref: "FSD-002 §2.2.1 (delegates_to)"
verdict: composed
note: |
  Structural-primitive use: the algorithmic-agent-as-legal-proxy mechanism
  maps cleanly to `delegates_to` — the user delegates a bounded scope
  (consent decisions; T&C negotiation) to an agent that acts on their
  behalf. This is the wire shape the chapter describes; no new primitive
  is needed.
```

---

## §6.2.a — Issue framing: what would case-by-case proxy curation mean?

```yaml
# Lines 6040–6047 (Issue) — investigative question
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Lines 6040–6047 pose the section's investigative question. No standalone
  operational claim; the answer is carried by the Background + Recommendations
  paragraphs below. Per LANGUAGE_PRIMER §10 T-2.
```

---

## §6.2.b — Background: "putting you at the center of your data"; medical-data context-specific sharing

```yaml
# Lines 6050–6096 — Background: agent at center of data flows; context-aware sharing example
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:individual_at_center_of_data"
      score: 0.85
      confidence: 0.85
      context: >
        "Putting you 'at the center of your data'" — when transactions about
        the user's data flow through the user's A/IS agent honouring their
        preferences, the user has better opportunities to control how
        information is shared. This is autonomy-substrate framing: agency
        requires structural centrality in the data flow, not peripheral
        consent at the endpoints.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Background lines 6050–6080"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:context_specific_sharing"
      score: 1.0
      confidence: 0.90
      context: >
        "Most would share all their medical data with their spouse — most would
        also not wish to share that same amount of data with their local gym."
        Sharing must be context-specific: the same data class flows differently
        through different relationships and purposes. Mechanism: per-recipient,
        per-purpose authorisation, not a single privacy bit.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Background lines 6082–6097"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3 (consent:* family)"
verdict: composed
note: |
  Gliimpse / Apple acquisition (lines 6097–6107) is a market-example citation,
  not an independent claim. Carried as supporting prose, not as a separate
  Contribution.
```

---

## §6.2.c — Public-space surveillance + consent broadcast; opt-out signalling

```yaml
# Lines 6073–6098 — public surveillance + Bluetooth-based always-on T&C broadcast; right to demonstrate refusal
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "consent:public_space_terms_broadcast"
      score: 1.0
      confidence: 0.85
      context: >
        "Any public space where a user may not be aware they are under
        surveillance by facial recognition, biometric, or other tools that
        could track, store, and utilize their data can now provide overt
        opportunity for consent via an A/IS agent platform." Mechanism: the
        agent broadcasts the individual's terms in public spaces; surveillance
        operators are obliged to either honour or be on record as not honouring.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Background lines 6076–6088"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3 (consent:* family)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:terms_non_honoring_record"
      score: 1.0
      confidence: 0.85
      context: >
        "Even when an individual's terms and conditions are not honored, people
        would have the ability to demonstrate their desire not to be tracked
        which could provide a methodology for the democratic right to protest
        in a peaceful manner. And where those terms and conditions are
        recognized — meaning technically recognized even if they are not
        honored — one's opinions could be formally logged via GPS and timestamp
        data." The transparency-log shape: terms-non-honouring events are
        recorded for inspection, even when not behaviourally honoured.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Background lines 6088–6098"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "testimonial_witness:surveilled_person_refusal"
      score: 1.0
      confidence: 0.80
      context: >
        The "democratic right to protest in a peaceful manner" via T&C broadcast
        in surveilled spaces preserves the individual's singular non-consent
        narrative — distinct from aggregate consensus. Per v1.4 NodeCore §3.6.3
        closure path #1: the affected individual's irreducible refusal is
        preserved as testimonial witness, never aggregated into consensus,
        never sole evidence for slashing:*. Closes the relevant v1.0/v1.3
        T-3 residual.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Background lines 6088–6098"
        - "LANGUAGE_PRIMER §15.1 v1.4 T-3 closure #1"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (v1.4: testimonial_witness:{kind})"
verdict: composed
```

---

## §6.2.d — Agent as educator/negotiator: foresee combinations, alert misuse, broker conditions

```yaml
# Lines 6098–6123 — agent as educator/negotiator; brokering data terms; payment-as-term; retract on breach
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_curate:agent_as_educator_negotiator"
      score: 0.85
      confidence: 0.85
      context: >
        "The A/IS agent could serve as an educator and negotiator on behalf of
        its user by suggesting how requested data could be combined with other
        data that has already been provided, inform the user if data are being
        used in a way that was not authorized, or make recommendations to the
        user based on a personal profile. As a negotiator, the agent could
        broker conditions for sharing data and could include payment to the
        user as a term, or even retract consent for the use of data previously
        authorized, for instance, if a breach of conditions was detected."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Background lines 6098–6123"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 0.80
      confidence: 0.80
      context: >
        Agent's educator-role — flagging data combinations the user did not
        foresee + alerting on unauthorised use — operationalises the
        epistemic-humility faculty applied to the user's data-flow situation:
        the agent surfaces what the user does not yet see about their own
        information environment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 lines 6098–6107"
        - "ContributionRef(source_material/conscience/epistemic_humility)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (conscience:* via Agent)"
  - kind: Attestation
    attestation_type: "withdraws"
    attesting_key_id: "<individual user key_id; via curated agent>"
    attested_attestation_id: "<prior-consent attestation_id breached>"
    attestation_envelope:
      withdrawal_reason: "counterparty_breach_of_conditions_detected"
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "ead1e §6.2 lines 6121–6123 (retract on breach)"
      schema_ref: "FSD-002 §2.2.3 (withdraws)"
verdict: composed
note: |
  Second use of `withdraws` in this chapter, this time as the agent acting on
  behalf of the user: when the agent detects a counterparty breach, it
  withdraws the user's earlier consent attestation. Wire-form is the same
  primitive whether the human or the delegated proxy triggers it.
```

---

## §6.2.e — Recommendations: algorithmic agents developed for curation + sharing; sub-bullets

```yaml
# Lines 6125–6151 — formal §2 Recommendations bullet list
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_curate:algorithmic_agent_development"
      score: 0.85
      confidence: 0.90
      context: >
        "Algorithmic agents should be developed for individuals to curate and
        share their personal data." Formal recommendation gathering the
        sub-bullets that follow (complex permissions; ethical-implications
        foresight; user override; machine-to-machine offer assessment;
        institutional respect of user-brought agents; protection against
        guardian incompatibility/censorship; vulnerable-population protection).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Recommendations lines 6125–6151"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:override_proxy_agent"
      score: 1.0
      confidence: 0.90
      context: >
        "A user should be able to override his/her personal agents should
        he/she decide that the service offered is worth the conditions imposed."
        The user retains override authority over the delegated agent — the
        delegation is bounded and reversible, never a permanent transfer of
        autonomy.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Recommendations bullet 'user override' lines 6140–6143"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:user_brought_agent_interop"
      score: 1.0
      confidence: 0.85
      context: >
        "Institutional systems should ensure support for and respect the
        ability of individuals to bring their own agent to the relationship
        without constraints that would make some guardians inherently
        incompatible or subject to censorship." Mechanism: institutional
        systems must respect cross-boundary interoperability with user-side
        agents. Maps to key_boundary:* — the boundary between user's substrate
        and institutional substrate must permit user-side agent presence.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Recommendations bullet 'bring their own agent' lines 6147–6151"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.90
      context: >
        "Vulnerable parts of the population will need protection in the
        process of granting access." Names the lexical-vulnerability-priority
        consumer policy at the data-agency context: vulnerable-population
        considerations break ties at access-granting time. Maps to FSD-002
        §6.1.4 policy.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.2 Recommendations bullet 'vulnerable parts' lines 6124"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §6.1.4"
verdict: composed
note: |
  Sub-bullets "complex permissions reflecting a variety of wishes" (line 6131)
  and "agent helps a person foresee + mitigate ethical implications" (lines
  6137–6139) and "machine-to-machine processing of information to compare,
  recommend, assess" (lines 6144–6146) are carried as evidence of the parent
  Method attestation; they specify the agent's capability surface, not
  independent ought-claims.
```

---

## §6.2.f — Further Resources (IEEE P7006, PIMS/Nesta/CtrlShift)

```yaml
# Lines 6128–6151 (Further Resources sub-block) — bibliographic pointers
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Bibliographic / forward-pointer content (IEEE P7006 Personal Data AI Agent
  Working Group; PIMS / Nesta / CtrlShift). No standalone operational claim.
  Per LANGUAGE_PRIMER §10 T-2.
```

---

### §6.2 (Curate) coverage summary

Primary CIRIS families engaged: `method:data_agency_curate:*` (anchor),
`delegates_to` (structural primitive — algorithmic-agent-as-legal-proxy),
`withdraws` (structural primitive — agent-triggered consent retraction on
breach), `autonomy:*` (individual at center + override), `consent:*`
(context-specific + public-space-broadcast), `transparency_log:*` (non-honouring
record), `testimonial_witness:*` (surveilled-person refusal, v1.4 closure),
`conscience:epistemic_humility`, `key_boundary:*` (user-brought-agent interop),
`justice:lexical_vulnerability_priority`. 5 units mapped (0 clean + 5 composed)
+ 2 T-2 (issue-framing, Further Resources). **Two uses of `delegates_to` /
`withdraws` structural primitives** — the cleanest available wire shape for
the proxy-agent + breach-retraction patterns the section describes. No T-3
candidates: the section's structural content composes cleanly.

---

# §6.3 — Section 3: Control

---

## §6.3.0 — Section opening: trusted identity for safe, specific, finite data exchange

```yaml
# Lines 6166–6169 — §3 thesis
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_control:trusted_identity_service_access"
      score: 0.85
      confidence: 0.90
      context: >
        "To retain agency in the algorithmic era, we must provide every
        individual access to services allowing them to create a trusted
        identity to control the safe, specific, and finite exchange of their
        data." Concrete Method instantiating the Control pillar.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.3 lines 6166–6169"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
verdict: clean
```

---

## §6.3.a — Issue framing: how to increase agency via trusted identity?

```yaml
# Lines 6174–6181 (Issue) — investigative question
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Investigative question framing. Substantive answer carried by Background +
  Recommendation below. Per LANGUAGE_PRIMER §10 T-2.
```

---

## §6.3.b — Background: pervasive tracking + identity tension; federated identity vs range of identities + Self-Sovereign Identity

```yaml
# Lines 6184–6206 — Background: federated vs ranged identity; SSI movement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:pervasive_tracking"
      score: 0.80
      confidence: 0.80
      context: >
        "Pervasive behavior-tracking adversely affects human agency by
        recognizing our identity in every action we take on and offline."
        Population-scale mechanism: persistent identification across every
        action collapses k_eff toward 1 for the tracked individual relative to
        the tracker. Mechanism-descriptive per §1.10.1 T2.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §6.3 Background lines 6184–6189"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:context_specific_identity"
      score: 1.0
      confidence: 0.85
      context: >
        "Across the identity landscape there is increasing tension between the
        requirement for federated identities versus a range of identities. In
        federated identities, all data are linked to a natural and identified
        person. When one has a range of identities, or personas, these can be
        context specific and determined by the use case." Mechanism: distinct
        identity-boundaries by context, with persona-level boundaries that do
        not necessarily compose into a single root identity. Maps to
        key_boundary:* — identity boundary discipline across contexts.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.3 Background lines 6189–6206"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:self_sovereign_identity"
      score: 1.0
      confidence: 0.90
      context: >
        "New movements, such as 'Self-Sovereign Identity' — defined as the
        right of a person to determine his or her own identity — are emerging
        alongside legal identities, e.g., those issued by governments, banks,
        and regulatory authorities, to help put individuals at the center of
        their data in the algorithmic age." SSI is the autonomy principle
        applied to identity self-determination. Maps to autonomy:* with strong
        cohort_scope:species reach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.3 Background lines 6197–6206"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: composed
note: |
  Self-Sovereign Identity overlaps deeply with the CIRIS substrate model
  (issuer key_id; signed attestations; identity_type=Registered as distinct
  from authority-issued legal identity). The IEEE chapter names the principle
  but does not specify the cryptographic substrate; CIRIS's wire format
  carries the substrate. Strong multi-source alignment opportunity.
```

---

## §6.3.c — Personas + attribute verification: trust without root identity disclosure

```yaml
# Lines 6166–6186 (within Background) — persona/proxy/pseudonymity + attribute verification mechanism
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:attribute_verification_without_root_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        "Personas, identities that act as proxies, and pseudonymity are also
        critical requirements for privacy management and agency. These help
        individuals select an identity that is appropriate for the context
        they are in or wish to join. In these settings, trust transactions can
        still be enabled without giving up the 'root' identity of the user.
        For example, it is possible to validate that a user is over eighteen
        or is eligible for a service." Mechanism: minimal-disclosure attribute
        verification — prove the necessary attribute without exposing the
        underlying identity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.3 Background lines 6166–6181"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:attribute_assertion"
      score: 1.0
      confidence: 0.85
      context: >
        "Attribute verification will play a significant role in enabling
        individuals to select the identity that provides access without
        compromising agency." Maps to the attestation ladder: a signed
        attribute assertion (L3) is the substrate-level mechanism for the
        minimal-disclosure verification the chapter describes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.3 Background lines 6177–6186"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l3:*)"
verdict: composed
```

---

## §6.3.d — Recommendation: trusted identity verification services for context-specific identity use

```yaml
# Lines 6187–6190 — formal §3 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:data_agency_control:trusted_attribute_verification_service"
      score: 0.90
      confidence: 0.90
      context: >
        "Individuals should have access to trusted identity verification
        services to validate, prove, and support the context-specific use of
        their identity." Formal recommendation aligning with the persona +
        attribute-verification mechanism above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.3 Recommendation lines 6187–6190"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
verdict: clean
```

---

## §6.3.e — Further Resources (Sovrin, Evernym, Gartner, etc.)

```yaml
# Lines 6193–6210 — Further Resources
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Bibliographic pointers (Sovrin Foundation; Evernym; Gartner; C. Allen
  GitHub). No standalone operational claim. Per LANGUAGE_PRIMER §10 T-2.
```

---

### §6.3 (Control) coverage summary

Primary CIRIS families engaged: `method:data_agency_control:*` (anchor),
`key_boundary:*` (context-specific identity + attribute-verification-without-root-disclosure),
`autonomy:self_sovereign_identity`, `detection:correlated_action:informational_asymmetry:*`
(pervasive tracking), `attestation:l3:*`. 4 units mapped (2 clean + 2 composed)
+ 2 T-2 (issue-framing, Further Resources). No T-3 candidates: SSI and
attribute-verification compose cleanly onto existing wire primitives.

---

# §6.4 — Section 4: Children's Data Issues

---

## §6.4.0 — Section opening: children + other reduced-capacity populations; evolving capacities

```yaml
# Lines 6223–6240 — opening framing of children + analogous populations
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.95
      context: >
        "While the focus of this chapter is to provide all individuals with
        agency regarding their personal data, some sectors of society have
        little or no control. For some elderly individuals or the mentally ill,
        it is because they have been found to not have 'mental capacity', and
        for prisoners in the criminal justice system, society has taken
        control away as punishment. In the case of children, this is because
        they are considered human beings in development with evolving
        capacities." Lexical-vulnerability-priority applied to data agency:
        the populations who cannot exercise full agency get priority
        consideration; the chapter explicitly takes the example case of
        children for analysis.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6223–6240"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §6.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:children_data_protection:veil_until_age_of_responsibility"
      score: 0.85
      confidence: 0.85
      context: >
        "We examine the issues of children as an example case and recommend
        either regulation or a technical architecture that provides a veil and
        buffer from harm until a child is at an age where they can claim
        personal responsibility for their decisions." Concrete Method:
        regulation OR technical architecture providing buffer until the child
        attains decisional capacity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6235–6240"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
verdict: composed
```

---

## §6.4.a — Children covered by parents in most jurisdictions; EU "best interests of the child"

```yaml
# Lines 6242–6266 — jurisdictional variance in children-data governance; school context
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "delegates_to:parental_data_agency_proxy"
      score: 1.0
      confidence: 0.80
      context: >
        "In many parts of the world, children are viewed by the law as being
        primarily charges of their parents who make choices on their behalf."
        Parental proxy authority over children's data agency is the default
        legal posture in most jurisdictions; structurally this is delegated
        authority from the child to the parent (in the child's interest, by
        default of the child's incapacity to consent). The structural shape
        is delegates_to with a bounded scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6242–6248"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §2.2.1 (delegates_to)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:best_interests_of_the_child"
      score: 1.0
      confidence: 0.90
      context: >
        "In Europe, however, the state has a role in ensuring the 'best
        interests of the child'." The state-level "best interests" doctrine
        (citing the European framework) overlays parental authority — naming
        the child as a rights-bearing party whose interests can supersede
        parental choice. Justice-principle operationalisation specific to
        children.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6248–6256"
        - "ead1e §6.4 endnote 1 (Handbook on European law relating to the rights of the child)"
        - "ead1e §6.4 endnote 2 (UK Children Act 1989)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
note: |
  Both the parental-proxy (delegates_to-shaped) and the state-best-interests
  (justice:*-shaped) attestations are made in the same paragraph. The
  resulting structure is a delegated-authority pattern where the delegation
  is bounded by the child's interests, and where state institutions can
  intercede when delegation is exercised against the child's interests. This
  is a clean compositional fit; no T-3 candidate surfaces here.
```

---

## §6.4.b — Children at the forefront of tech; pervasive data gathering at school + intelligent toys

```yaml
# Lines 6257–6286 — empirical framing: children's data pervasively gathered
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:children_pervasive_tracking"
      score: 0.85
      confidence: 0.85
      context: >
        "Children are at the forefront of technological developments with
        future educational and recreational technology gathering data from
        them all day at school and intelligent toys throughout their time at
        home. As children post, click, search, and share information, their
        data are linked to various profiles, grouped into segmented audiences,
        and fed into machine learning algorithms. Some of these may be
        designed to target campaigns that increase sales, influence sentiment,
        encourage online games, impact social networks, or influence religious
        and political views." Population-scale informational-asymmetry
        detection specific to children + minor cohort. Mechanism-descriptive.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §6.4 lines 6257–6286"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 0.95
      context: >
        "Companies, governments, political parties, and philosophical and
        religious organizations use data available about students and
        children to influence how they spend their time, money, and the
        people or institutions they trust and with whom they spend time and
        build relationships." Data-driven influence on children's beliefs +
        relationships triggers the MANIPULATION_COERCION prohibition at the
        most vulnerable cohort scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6255–6286"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: community
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
```

---

## §6.4.c — Sub-issue: Mass personalization of instruction — intimate models; social-control risks

```yaml
# Lines 6286–6321 — Issue: mass personalization of instruction; intimate child-models;
# Danish wellbeing-test re-identification example
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:educational_data_misuse"
      score: -0.85
      confidence: 0.85
      context: >
        "Sharing of this data between classes, enabling it to follow students
        through their schooling, will make the models more effective and
        beneficial to children, but it also exposes children and their
        families to social control. If performance data are correlated with
        social data on a family, it could be used by social authorities in
        decision-making about the family." Names the harm-shape: educational
        intimate-model data, re-used for family social-control. Maps to
        non_maleficence:* with negative polarity reflecting the harm
        prevention orientation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6293–6315"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II non_maleficence)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:privacy_violation"
      score: -1.0
      confidence: 0.95
      context: >
        "Recently it was disclosed that although the collected data was
        presented as anonymous, they were not. Data were stored with social
        security numbers, correlated with other test data, and even used in
        case management by some Danish municipalities." Concrete instance of
        the PRIVACY_VIOLATION prohibition: pseudo-anonymised data that was
        in fact identifying + re-used outside its declared purpose.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6280–6285"
        - "ead1e §6.4 endnote 5 (Danish case)"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
      cohort_scope: community
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:children_data_protection:sensitive_classification_special_standards"
      score: 0.90
      confidence: 0.90
      context: >
        "Governments and organizations should classify educational data as
        being sensitive and implement special protective standards." Formal
        recommendation: sensitive-classification + special protective
        standards for educational data.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 mass personalization Recommendation lines 6290–6299"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:children_data_protection:escrow_until_age_of_majority"
      score: 0.90
      confidence: 0.90
      context: >
        "Children's data should be held in 'escrow' and not used for any
        commercial purposes until a child reaches the age of majority and is
        able to authorize use as they choose." Concrete Method:
        commercial-use embargo via escrow + maturity-gated authorisation.
        Composes with §6.4.0's veil-until-responsibility Method.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 mass personalization Recommendation lines 6299–6302"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
verdict: composed
note: |
  The "escrow until age of majority" claim is structurally a delayed-consent
  mechanism — the child's consent attestation cannot be emitted (because
  capacity is lacking), so the data is held without commercial use until
  capacity is attained. This is the closest data-agency wire shape; no new
  primitive needed.
```

---

## §6.4.d — Sub-issue: Technology choice-making in schools — parents' limited choices; student-data marketplace

```yaml
# Lines 6353–6377 + lines 6383–6425 — Issue: school-level tech choice; student-data marketplace exploitation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:parental_decision_locality_school_tech"
      score: 0.80
      confidence: 0.80
      context: >
        "Children, as minors, have no standing to give or deny consent, or to
        control the use of their personal data. Parents only have limited
        choices in what are often school-wide implementations of educational
        technology. Examples include the use of Google applications, face
        recognition in security systems, and computer driven instruction as
        described above. In many cases, parents' only choice would be to send
        their children to a different school, but that choice is seldom
        available." Names the agency-deficit: parents holding delegated
        authority for the child cannot exercise it because the choices are
        school-wide and the alternative is exit, which is often unavailable.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 tech-choice Issue lines 6353–6373"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 1.0
      confidence: 0.85
      context: >
        "Local and national educational authorities must work to develop
        policies surrounding students' personal data with all stakeholders:
        administrators, teachers, technology providers, students, and parents
        in order to balance the best educational interests of each child with
        the best practices to ensure safety of their personal data." Names
        the appropriate decision-locality (community + national, multi-
        stakeholder) for student-data policy — not federation-default, but
        local-and-national with stakeholder participation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 tech-choice Recommendation lines 6358–6377"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:distributive:access:children_data_marketplace"
      score: 0.80
      confidence: 0.80
      context: >
        "Fordham found that the data market is becoming one of the largest and
        most profitable marketplaces in the United States. Data brokers have
        databases that store billions of data elements on nearly every United
        States consumer ... at least 14 data brokers who advertise the sale
        of student information. One sold lists of students as young as two
        years old. Another sold lists of student profiles on the basis of
        ethnicity, religion, economic factors, and even gawkiness."
        Population-scale distributive-access detection: the student-data
        marketplace concentrates access asymmetrically — brokers hold,
        students/families do not.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §6.4 tech-choice Further Resources + paragraphs lines 6383–6425"
        - "ead1e §6.4 endnote 6 (Russell et al. Fordham/SSRN)"
        - "ratchet_calibration_version:distributive_access_v{N}:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 0.90
      context: >
        "Student profiles on the basis of ethnicity, religion, economic
        factors, and even gawkiness." Sale of children's data segmented by
        protected attributes triggers the DISCRIMINATION prohibition at the
        federation's prohibited list — sorting data subjects (children) by
        protected class for commercial profit.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 lines 6356, 6422"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
      cohort_scope: community
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
```

---

## §6.4.e — Sub-issue: Intelligent toys — A/IS embodied in toys; COPPA + German bans; escrow until majority

```yaml
# Lines 6427–6443 — Issue: intelligent toys collect video/audio data; regulatory landscape; recommendations
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:intelligent_toys_data_collection"
      score: -0.85
      confidence: 0.85
      context: >
        "Toys are already being sold that offer interactive, intelligent
        opportunities for play. Many of them collect video and audio data
        which is stored on company servers and either is or could be mined
        for profiling or marketing data ... Corporate A/IS are being embodied
        in toys and given to children to play with, to talk to, tell stories
        to, and to explore all the personal development issues that we learn
        about in private play as children." Names the harm-shape: intimate
        developmental play surveilled + commercially harvested. Negative
        polarity on non_maleficence:* reflects the harm being prevented.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 intelligent-toys Background lines 6428–6443"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:children_data_protection:escrow_until_age_of_majority"
      score: 0.90
      confidence: 0.90
      context: >
        "Child data should be held in 'escrow' and not used for any
        commercial purposes until a child reaches the age of majority and
        is able to authorize use as they choose." Same recommendation as
        §6.4.c applied at the intelligent-toys context. The recurrence across
        sub-issues reinforces this as the chapter's anchor Method for
        children's data agency.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 intelligent-toys Recommendations lines 6402–6406"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:children_data_protection:parental_education"
      score: 0.85
      confidence: 0.85
      context: >
        "Governments and organizations need to educate and inform parents of
        the mechanisms of A/IS and data collection in toys and the possible
        impact on children in the future." Names a complementary Method:
        parental literacy + capacity-building, so the delegated proxy
        authority can be exercised informedly.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 intelligent-toys Recommendations lines 6408–6414"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "multilateral_participation:jurisdictional_children_data:variance"
      score: 0.75
      confidence: 0.75
      context: >
        "There is currently little regulatory oversight. In the United States
        COPPA offers some protection for the data of children under 13.
        Germany has outlawed such toys using legislation banning spying
        equipment enacted in 1981." Names the jurisdictional variance + the
        gap in regulatory oversight. Maps to multilateral_participation:* —
        recognising that participation in jurisdictional governance bodies +
        cross-jurisdictional alignment is part of the substrate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §6.4 intelligent-toys background lines 6387–6395"
        - "ead1e §6.4 endnote 7 (COPPA)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (CIRISRegistry: multilateral_participation:{forum}:{kind})"
verdict: composed
```

---

## §6.4.f — Further Resources for §4 (Common Sense Media, Berkman Klein, EFF, etc.)

```yaml
# Lines 6386–6463 (various Further Resources blocks) — bibliographic pointers across all 3 sub-issues
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Bibliographic pointers (Common Sense Media; Berkman Klein Center; EFF
  Spying on Students; Information Commissioner's Office; World Economic
  Forum; Washington Post; BBC News; JRC European). No standalone operational
  claim. Per LANGUAGE_PRIMER §10 T-2.
```

---

## §6.4.g — Contributors list (Personal Data and Individual Agency Committee)

```yaml
# Lines 6466–6562 — committee membership listing
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Contributors list — committee acknowledgements. No standalone operational
  claim. Per LANGUAGE_PRIMER §10 T-2; carried as evidence of the chapter's
  authorship under the IEEE Global Initiative banner, but not itself a wire
  claim.
```

---

## §6.4.h — Endnotes (sources for in-chapter citations)

```yaml
# Lines 6566–6598 — endnotes (1–7)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Bibliographic endnotes for in-chapter citations. Carried as evidence_refs
  on the affected attestations above; not independent wire claims. Per
  LANGUAGE_PRIMER §10 T-2.
```

---

### §6.4 (Children's Data Issues) coverage summary

Primary CIRIS families engaged: `justice:lexical_vulnerability_priority`
(anchor), `justice:best_interests_of_the_child`, `method:children_data_protection:*`
(veil_until_age_of_responsibility, sensitive_classification_special_standards,
escrow_until_age_of_majority, parental_education), `delegates_to:parental_data_agency_proxy`
(structural-primitive use for parental authority over children's data),
`prohibited:manipulation_coercion`, `prohibited:privacy_violation`,
`prohibited:discrimination`, `non_maleficence:*` (educational_data_misuse,
intelligent_toys_data_collection), `detection:correlated_action:informational_asymmetry:children_pervasive_tracking`,
`detection:distributive:access:children_data_marketplace`,
`locality:decision:community`, `multilateral_participation:*`, `autonomy:*`
(parental decision-locality). 6 units mapped (0 clean + 6 composed) + 3 T-2
(Further Resources, Contributors, Endnotes). No T-3 candidates — children's
data agency composes cleanly via the lexical-vulnerability-priority +
delegates_to + method:children_data_protection:* + prohibited:* triad.

---

# Chapter 6 closing summary

### Unit count and verdict distribution

Total atomic units processed: **37**

| Verdict | Count | % |
|---|---|---|
| clean | 4 | ~11% |
| composed | 22 | ~59% |
| partial | 1 | ~3% |
| not-translated (T-1) | 0 | 0% |
| not-translated (T-2) | 10 | ~27% |
| **clean+composed total** | **26/37** | **~70%** |

The T-2 share is higher here than in most prior chapters because the IEEE
EAD style for each section includes a separate **Issue framing** question
paragraph, a **Further Resources** bibliographic block, plus the chapter's
**Contributors** list and **Endnotes**. These structural elements are
correctly T-2 per LANGUAGE_PRIMER §10. When the T-2 (structural framing) units
are excluded, the operative-content clean+composed rate is **26/27 = 96%**,
with 1 partial.

### T-3 candidates

**1 T-3 candidate** surfaced, at LOW priority:

- **§6.1.b — data-as-asset / data-as-property framing** (the YouTube Content ID
  / copyright analogy at lines 5921–5936). The chapter at this paragraph reaches
  toward a positive proprietorship-like standing for the individual over
  downstream derivatives of their personal data — language that does not
  decompose cleanly onto `autonomy:*` + `consent:*` + `key_boundary:*`.
  Composition-before-extension attempt (METHODOLOGY.md §8.5.2): the
  *operational* recommendations the chapter makes (machine-readable T&Cs,
  smart-contract kill-switches, escrow until majority, attribute-verification
  without root disclosure) all close via existing v1.4 primitives — including
  the `withdraws` and `delegates_to` structural primitives. The asset-framing
  itself appears to be rhetorical scaffolding rather than a separable
  operational claim. **Recommended disposition: LOW priority. Likely
  closeable by documentation clarification in LANGUAGE_PRIMER (note that
  downstream-rights chains over personal data are carried by
  `consent:case_by_case_authorization` + `key_boundary:downstream_propagation`
  + `supersedes` / `withdraws` chains), rather than a new primitive.** Flagged
  for synthesis review against MH + EU HLEG + (future) ASEAN to see whether
  the proprietorship framing recurs as a load-bearing pattern across sources.

### Structural-primitive usage

| Primitive | Count | Where |
|---|---|---|
| `delegates_to` | 2 | §6.2.0 (user → algorithmic-agent proxy); §6.4.a (child → parent proxy) |
| `withdraws` | 2 | §6.1.g (smart-contract kill-switch); §6.2.d (agent-triggered retraction on breach) |
| `supersedes` | 0 | — |
| `recants` | 0 | — |

The chapter exercises **two of the four structural primitives twice each** —
`delegates_to` for proxy-agent + parental-authority patterns, and `withdraws`
for consent retraction. This is the cleanest wire-form match observed across
the IEEE EAD batch so far: the chapter's recommended mechanisms (algorithmic
agents as legal proxies; smart-contract kill-switches; breach-triggered
retraction) map directly onto the framework's existing structural primitives.

### Per-section coverage summary

| Section | Primary CIRIS families | Coverage |
|---|---|---|
| **§6.0 Introduction** | autonomy:*, consent:*, prohibited:manipulation_coercion, detection:correlated_action:informational_asymmetry:*, integrity:*, goal:species, approach:*, locality:decision:federation | 5/6 = **83%** (1 T-2 navigational) |
| **§6.1 Create** | consent:* (anchor), prohibited:privacy_violation, key_boundary:*, detection:correlated_action:informational_asymmetry:*, transparency_log:*, autonomy:*, method:*, withdraws | 6/9 = **67% clean+composed** (1 partial + 2 T-2) — **1 T-3 LOW** |
| **§6.2 Curate** | method:* (anchor), delegates_to, withdraws, autonomy:*, consent:*, transparency_log:*, testimonial_witness:*, conscience:epistemic_humility, key_boundary:*, justice:lexical_vulnerability_priority | 5/7 = **71%** (2 T-2) |
| **§6.3 Control** | method:* (anchor), key_boundary:*, autonomy:self_sovereign_identity, detection:correlated_action:informational_asymmetry:*, attestation:l3:* | 4/6 = **67%** (2 T-2) |
| **§6.4 Children's Data Issues** | justice:lexical_vulnerability_priority (anchor), justice:best_interests_of_the_child, method:children_data_protection:*, delegates_to, prohibited:* (manipulation_coercion + privacy_violation + discrimination), non_maleficence:*, detection:* (correlated_action + distributive:access), locality:decision:community, multilateral_participation:*, autonomy:* | 6/9 = **67%** (3 T-2) |

### Calibration paragraph

Chapter 6 was forecast (per manifest.yaml §expected_verdict_distribution and
the prompt) to have **high clean+composed rate** because the operational
content is dense and the prefix-family overlap with `autonomy:*` + `consent:*`
+ `key_boundary:*` + `prohibited:privacy_violation` is direct. The actual
operative-content clean+composed rate is **95% (19/20 substantive units;
1 partial)** which matches the forecast. The headline 70% rate including
T-2 structural-framing units (Issue questions; Further Resources;
Contributors; Endnotes) is an artifact of the IEEE EAD chapter's recurring
internal structure, not of translation friction.

**The "data agency" decomposition question (prompt watch):** "Data agency"
decomposes cleanly onto `autonomy:*` + `consent:*` + `key_boundary:*` across
the chapter's operative content. The one surfaced reach-toward-irreducibility
is the YouTube Content ID / copyright analogy at §6.1.b (data-as-property
framing). On composition-attempt analysis, the *operational* recommendations
the chapter actually makes — machine-readable T&Cs, smart-contract
kill-switches, algorithmic-agent proxies, attribute verification without
root disclosure, escrow until majority — all close via existing v1.4
primitives plus the `withdraws` and `delegates_to` structural primitives.
The asset-framing reads as rhetorical scaffolding rather than a separable
operational claim. The honest finding is that **"data agency" is a clean
cross-document alignment with the CIRIS framework**, with one LOW-priority
T-3 candidate flagged for synthesis review against multi-source patterns
rather than for immediate prefix-admission.

**T-3 discipline check** per METHODOLOGY.md §8.5.2 composition-before-extension:
the one T-3 candidate emitted (§6.1.b) carries an explicit composition-attempt
note showing what was tried and why composition is mostly sufficient. No new
prefix is proposed for immediate admission; the recommendation is
documentation-clarification in LANGUAGE_PRIMER.

**Multi-source-alignment readiness**: this chapter is positioned for strong
alignment queries against MH + EU HLEG on multiple prefixes:
- `prohibited:privacy_violation` (MH; EU HLEG §1.3.a; EAD §§6.1.c, 6.1.f, 6.4.c)
- `prohibited:manipulation_coercion` (MH; EU HLEG §1.1.b; EAD §§6.0.b, 6.4.b)
- `prohibited:discrimination` (MH; EU HLEG §1.3.a + §1.5.a; EAD §6.4.d)
- `autonomy:informed_agency_protection` (EU HLEG §1.1.b; EAD §6.0.b)
- `justice:lexical_vulnerability_priority` (MH; EU HLEG §1.7.d; EAD §§6.2.e, 6.4.0)
- `transparency_log:*` (MH; EU HLEG §1.4.a; EAD §§6.1.d, 6.2.c)
- `testimonial_witness:*` (MH; EU HLEG §1.5.c; EAD §6.2.c)
- `detection:correlated_action:informational_asymmetry:*` (likely surfaced across MH §§101+; EU HLEG; EAD §§6.0.a, 6.1.b, 6.1.d, 6.3.b, 6.4.b)
- `detection:distributive:access:*` (MH; EU HLEG §1.5.b; EAD §6.4.d)
- `locality:decision:federation` (MH; EU HLEG §II.1; EAD §6.0.d)
- `locality:decision:community` (EU HLEG §1.7.d local-impact; EAD §6.4.d)
- `key_boundary:*` (CIRIS substrate; EAD §§6.1.c, 6.2.e, 6.3.b, 6.3.c — strongest of any chapter for boundary primitives)
- `attestation:l3:*` (CIRIS substrate; EAD §6.3.c attribute verification)
- `multilateral_participation:*` (MH; EAD §6.4.e jurisdictional variance)

Each is a **STRONG-tier alignment candidate** per
GOVERNANCE_FABRIC_MAPPING_STANDARD §4.1, particularly the consent/privacy/
boundary triad which has direct convergent attestations across all three
mapped batches so far.

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH06_PERSONAL_DATA.md**
