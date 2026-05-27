# ASEAN Guide on AI Governance and Ethics — Section D (National-level Recommendations) + Section E (Regional-level Recommendations) + Section F (Conclusion)

**Batch**: `asean_guide_v1`
**Section range**: lines 2143–2695
**Source file**: `source_material/governance/asean_guide_v1/asean_guide.txt`
**Wire format**: FSD-002 v1.4 | Primer: `LANGUAGE_PRIMER.md` v1.1
**Methodology**: `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` §2 Phase 2 sub-agent fan-out
**Bootstrap batch reference**: `provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}`

**Atomic units mapped**: 51 (Section D: 32 units across D.001–D.032; Section E: 16 units across E.001–E.016; Section F: 3 units across F.001–F.003)
**Verdict counts**: clean=23, composed=25, partial=1, not-translated=2
**Residual-note blocks (no verdict change)**: 3 (Units D.011, E.001, F.002 carry composed verdicts with explicit residual notes flagging T-2 or T-3 surfaces; one of the three — E.001 — proposes a load-bearing T-3 extension)
**T-3 load-bearing candidates surfaced**: 2 (one HIGH — `regional_intergovernmental_role_taxonomy` for an ASEAN-style regional working group's distinct operational vs. dialogue roles; one MEDIUM — `cross_border_data_flow:harmonisation` as a positive-polarity mechanism-descriptive complement to `detection:distributive:access:*`). Both note explicit composition-before-extension attempts. See per-unit blocks.

**Section-E focal observation**: as predicted in the prompt, Section E is the densest exercise of the `multilateral_participation:asean:*` + `locality:decision:regional` + `partner_role:*` composition pattern. Unit E.001 (Working Group) emits a 3-primitive composition; the five-item responsibility list (E.002–E.006) emits per-item `multilateral_participation:asean:*` envelopes; the generative-AI cluster (E.007–E.013) composes `locality:decision:regional` with `supersedes` to flag the future-version commitment.

---

# Section D — National-level Recommendations

Intent (line 2144): "for policy makers." Scope-tag on every Section D Contribution: `cohort_scope: affiliations` (member-state government as the addressed cohort) — except where the operational shape genuinely reaches species scope. National recommendations operate one level below the regional layer; per LANGUAGE_PRIMER §7.2 + FSD-002 §6.1.5, the appropriate `locality:decision:{scale}` for most D-section claims is `national`.

---

## Unit D.001 — D.preamble (lines 2143–2151): national-level scope + cross-border collaboration imperative

**Source** (lines 2147–2151): "This section covers national-level recommendations to ensure responsible design, development, and deployment of AI systems. It is also important to note that cross-border collaboration is essential for promoting responsible AI governance and ensuring that best practices and safeguards are shared within ASEAN and across different regions."

```yaml
# Unit D.001 — declares national scope but also names cross-border collaboration as essential
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "locality:decision:national"
      score: 1.0
      confidence: 0.90
      context: >
        Section D declares national-government as the addressed decision-locality
        for "responsible design, development, and deployment of AI systems."
        Recommendations are policy-maker oriented; the decision-locality is
        national, not regional or local.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.preamble (lines 2147-2148)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:knowledge_exchange"
      score: 0.85
      confidence: 0.80
      context: >
        Cross-border collaboration named as essential for sharing best practices
        and safeguards "within ASEAN and across different regions." The claim
        explicitly straddles regional + extra-regional cooperation; this is the
        first envelope in the batch that asserts asean-forum participation as a
        positive normative anchor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.preamble (lines 2148-2151)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (multilateral_participation:{forum}:{kind})"
verdict: composed
nuance_lost: |
  The "across different regions" phrase reaches beyond ASEAN (extra-regional
  cooperation) but composes onto the same prefix. The polarity is positive but the
  paragraph is hortatory ("is essential") — strength is normative-recommendation,
  not constitutional.
```

---

## Unit D.002 — D.workforce.intro (lines 2154–2168): three-tier AI capability + upskilling

**Source** (lines 2156–2168): "ensure that a country's workforce can adapt to the new ways of working and possesses enough digital skills... Baseline level to operate AI applications; Intermediate level to maintain and rectify issues with AI applications; and Higher level to develop AI capabilities. Depending on the nature of jobs and industries, governments and policymakers should consider implementing measures to upskill the workforce."

```yaml
# Unit D.002 — workforce-capability ladder + national-government upskilling measures
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.85
      confidence: 0.80
      context: >
        National-government goal: workforce digital-skills capacity adequate to
        interact effectively with AI systems. Three-tier capability ladder
        (baseline operate / intermediate maintain / higher develop) is the
        approach-shape; the goal scope is affiliations (national workforce).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.intro (lines 2156-2168)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "approach:<goal:affiliations:workforce_capability>"
      score: 0.75
      confidence: 0.75
      context: >
        Three-tier capability development as approach: baseline / intermediate /
        higher. Job-and-industry tailoring is the modulator. National
        policymakers implement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.intro (lines 2159-2168)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — approach:{goal_id})"
verdict: composed
nuance_lost: |
  The three-tier capability granularity (operate / maintain / develop) is in
  context-prose. If load-bearing for downstream policy, each tier would warrant
  its own method:{} envelope; here the paragraph names them as illustrative not
  prescriptive. The "depending on nature of jobs and industries" tailoring lives
  in context only.
```

---

## Unit D.003 — D.workforce.public-private (lines 2170–2179): public-private upskilling collaboration

**Source** (lines 2170–2179): "Governments can collaborate closely with both public and private sectors to establish platforms and resources for employees to upskill themselves... In Singapore for example, the Singapore Computer Society collaborated with IMDA and Nanyang Technological University to offer a professional certification program on AI Ethics and Governance."

```yaml
# Unit D.003 — public-private collaboration for industry-specific AI upskilling
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:public_private_upskilling"
      score: 0.75
      confidence: 0.75
      context: >
        Concrete method: public-private collaboration to establish upskilling
        platforms, with industry-specific AI courses and forums. Singapore
        Computer Society + IMDA + NTU AI Ethics and Governance certification
        cited as instance (illustrative; not normative-binding for other
        member states).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.public-private (lines 2170-2179)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — method:{approach_id}:{rung})"
verdict: clean
nuance_lost: |
  The Singapore-specific example is illustrative; the asean_guide does not
  mandate it across member states. The role-shift framing ("operator of AI
  systems instead of manually performing tasks") is interpretive context
  rather than a wire claim.
```

---

## Unit D.004 — D.workforce.curricula (lines 2181–2186): STEM curriculum + AI awareness in non-STEM

**Source** (lines 2181–2186): "Individuals should also be able to acquire deeper insights into AI through schools and educational institutes. The curriculum of STEM disciplines needs to be periodically reviewed... For other disciplines, it is also important that the concept of AI is introduced so students are aware of what AI can do."

```yaml
# Unit D.004 — STEM curriculum update + non-STEM AI awareness in education
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:curricular_review"
      score: 0.75
      confidence: 0.75
      context: >
        Concrete method: periodic STEM curriculum review for data-analytics +
        AI advancements; AI-concept introduction in non-STEM disciplines so
        students are aware of AI's automation reach into their fields.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.curricula (lines 2181-2186)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  Cross-pollination of "use cases for AI and their corresponding AI governance
  considerations" framing is captured in context; not a separate wire claim.
```

---

## Unit D.005 — D.workforce.ethics-curriculum (lines 2188–2193): AI ethics curriculum mandate

**Source** (lines 2188–2193): "Beyond the technical knowledge of AI, there is also a need to increase individuals' understanding of ethical principles and how they are used to identify, evaluate, and mitigate the ethical implications of AI systems... A robust curriculum for AI ethics should be developed and incorporated into STEM courses or training for AI practitioners."

```yaml
# Unit D.005 — AI ethics curriculum as method
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:ai_ethics_curriculum"
      score: 0.85
      confidence: 0.80
      context: >
        Robust AI ethics curriculum should be developed and incorporated into
        STEM courses or AI-practitioner training so that practitioners have a
        "strong ethical foundation to guide future design, development, and
        deployment of AI technologies." Fairness/equity bias-mitigation cited
        as illustrative ethics-principle application.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.ethics-curriculum (lines 2188-2193)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "integrity:practitioner_ethical_foundation"
      score: 0.80
      confidence: 0.80
      context: >
        Standing claim that AI practitioners should hold a strong ethical
        foundation as integrity-relevant qualification. Composes with the
        method envelope above: the curriculum is the operational route to
        the standing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.ethics-curriculum (lines 2188-2193)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  The fairness-and-equity worked example (bias-identification → mitigation
  strategy) is context-prose; if treated as load-bearing it would warrant its
  own progress_measure:{} envelope, but the paragraph names it illustratively.
```

---

## Unit D.006 — D.workforce.transition (lines 2203–2210): support displaced workers

**Source** (lines 2203–2210): "Certain groups of workers may experience significant changes in their job roles due to the introduction of AI... it is important for policymakers to provide adequate support to affected employees as they transition to new job roles, such as offering training and upskilling programmes and access to other employment opportunities."

```yaml
# Unit D.006 — labour-displacement: per-individual non_maleficence + testimonial composition pattern
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "non_maleficence:labor_displacement_unacknowledged"
      score: 0.85
      confidence: 0.85
      context: >
        Positive polarity here because the source mandates acknowledgement +
        support: "it is important for policymakers to provide adequate support
        to affected employees as they transition." The CIRIS prefix names the
        harm class (labor displacement unacknowledged); attesting positively at
        this prefix is the framework's mode of saying "this class of harm must
        be acknowledged and remediated." Manufacturing-automation and farm-
        agronomist examples cited as instances. Per LANGUAGE_PRIMER §11.14, the
        per-individual claim runs on this prefix with target=affected_individual;
        ASEAN frames it cohort-wide rather than per-individual.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.transition (lines 2203-2210)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:transition_support"
      score: 0.80
      confidence: 0.80
      context: >
        Concrete method: training, upskilling programmes, mid-career switch
        support / employment-opportunity access. The method instantiates the
        non_maleficence claim above into operational government policy.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.transition (lines 2207-2210)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
nuance_lost: |
  ASEAN frames worker displacement cohort-wide ("affected employees") rather than
  per-individual; the v1.4 composition pattern with target_key_id=affected_individual
  + testimonial_witness:displaced_worker would carry the per-individual claim more
  fully. This is honest cohort-vs-individual asymmetry, not a T-3 gap — the wire
  format expresses both.
```

---

## Unit D.007 — D.workforce.pipeline (lines 2212–2227): public-private pipeline + curricula bullets

**Source** (lines 2212–2227): "Governments should also collaborate with the private sector to determine the pool of future AI-trained graduates... Co-develop curricula... Facilitate AI private sector and research professionals giving lectures to students... Encourage and help foster professional internship and co-opt programmes... Encourage professors and lecturers at educational institutions to be seconded to private sector AI firms."

```yaml
# Unit D.007 — four-item public-private pipeline mechanisms
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:talent_pipeline"
      score: 0.80
      confidence: 0.80
      context: >
        Four-item operational pipeline between Ministries of Education and
        private-sector AI firms: (1) co-developed curricula, (2) practitioner
        guest-lecturing, (3) internship/co-op programmes, (4) faculty
        secondments. Together: a method-level cluster instantiating the
        workforce-capability approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.workforce.pipeline (lines 2212-2227)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  Each of the four bullet items is granular enough to warrant its own
  method:{} envelope; consolidated here because the source names them as a
  cluster of one operational pattern. "Mitigate training time for fresh
  graduates" outcome framing is context-prose.
```

---

## Unit D.008 — D.ecosystem.intro (lines 2230–2238): AI innovation ecosystem + infrastructure + grants

**Source** (lines 2230–2238): "Governments should take actions to foster the growth of the AI innovation ecosystem. A supportive environment for AI development should be created, where companies are able to access and leverage data, digital technologies, and infrastructure... A short-term grant could also be offered to companies who wish to kickstart the adoption of AI in operations."

```yaml
# Unit D.008 — innovation ecosystem foundational infrastructure
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.75
      confidence: 0.75
      context: >
        National-government goal: foster AI innovation ecosystem with access
        to data, digital technologies, and infrastructure. Information
        sessions for senior leaders + short-term adoption grants named as
        operational supports.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.intro (lines 2230-2238)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Foundational digital infrastructure" + "leading industry solutions" are
  operational scaffolding without specific named addressees. The grant
  mechanism is context-prose; if a member state actually operationalised it,
  a per-grant Contribution would map.
```

---

## Unit D.009 — D.ecosystem.data (lines 2240–2245): open government data + public-private data sharing

**Source** (lines 2240–2245): "Governments can bridge these data gaps by making selected government data freely available for businesses to use and develop AI systems that could benefit national interests. In addition, encouraging data sharing within and between public and private sectors will help to create a rich data environment for AI to thrive."

```yaml
# Unit D.009 — open government data + public-private data sharing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:ai_innovation_ecosystem>:open_data"
      score: 0.75
      confidence: 0.75
      context: >
        Method: government data made freely available to businesses for AI
        development; intra/inter-sector data sharing encouraged. The
        distributive-access dimension (resource pooling for AI training data)
        is the structural object.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.data (lines 2240-2245)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "detection:distributive:access:training_data"
      score: 0.40
      confidence: 0.55
      context: >
        Positive-polarity attestation that the proposed open-data approach is
        anti-concentration relative to training-data access. Score is low-
        positive because the proposal is aspirational ("can bridge these data
        gaps") rather than mechanism-pinned. Witness_relation external because
        the attester is the asean_guide batch-signer, not a derived detector.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.data (lines 2240-2245)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5"
verdict: composed
nuance_lost: |
  The "selected" qualifier in "selected government data" carries a non-trivial
  exclusion-criterion claim that the source does not unpack; in CIRIS terms
  this would be a per-selection witness_diversity exercise that is unmapped
  here. "National interests" framing keeps the data-sharing implicitly
  jurisdictional, which composes naturally with cohort_scope: affiliations.
```

---

## Unit D.010 — D.ecosystem.governance-data (lines 2247–2265): data governance support + PETs

**Source** (lines 2247–2265): "support on setting up effective data governance measures and structure can also be provided to ensure that organisations are able to access and use the data in a responsible and ethical manner... Governments should encourage the adoption of privacy enhancing technologies (PETs)."

```yaml
# Unit D.010 — data governance support + PETs adoption
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:ai_innovation_ecosystem>:data_governance_support"
      score: 0.80
      confidence: 0.80
      context: >
        Government-provided data governance support: anonymisation, data
        lineage tools, PET adoption encouragement. PETs enable "selected
        government data" to be made available without compromising privacy
        (which structurally extends Unit D.009's open-data claim).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.governance-data (lines 2247-2265)"
        - "OECD Emerging PETs reference (footnote 25, line 2309)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:privacy_data_protection"
      score: 0.85
      confidence: 0.85
      context: >
        Positive privacy/non_maleficence anchoring. PETs framed as harm-mitigation
        mechanism for data confidentiality and privacy across information
        collection / processing / analysis / sharing pipeline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.governance-data (lines 2261-2265)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence)"
verdict: composed
nuance_lost: |
  PETs as a concrete technology class are footnoted to OECD; the citation chain
  is structurally a delegates_to-style authority-source claim but not made
  explicit here. The "responsible and ethical manner" framing reaches Accord
  scope but isn't tagged with mutability:constitutional because the source
  treats it as best-practice recommendation, not as hard constraint.
```

---

## Unit D.011 — D.ecosystem.crossborder (lines 2267–2275): cross-border data flow + framework interoperability

**Source** (lines 2267–2275): "facilitating cross-border data flow will also play an important role. To enable this, governments should work with other governments to establish data sharing and data transfer mechanisms... It is also useful for governments to work towards consistency and interoperability between national data protection legal frameworks and AI governance efforts."

```yaml
# Unit D.011 — cross-border data flow + framework harmonization
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:data_governance_harmonisation"
      score: 0.80
      confidence: 0.80
      context: >
        Governments-to-governments mechanism-setting on data sharing/transfer +
        legal-framework interoperability. The {kind} field uses
        data_governance_harmonisation to mark the cross-border substance.
        Children's rights + parental consent + erasure/access listed as
        in-scope harmonisation surfaces.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.crossborder (lines 2267-2275)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (multilateral_participation:{forum}:{kind})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "locality:decision:regional"
      score: 0.85
      confidence: 0.80
      context: >
        Although Section D is national, this unit's "consistency and
        interoperability between national data protection legal frameworks"
        explicitly addresses the cross-jurisdiction layer. The decision-locality
        thus rises to regional (or higher), composing with the
        multilateral_participation envelope above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.crossborder (lines 2271-2275)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: composed
residual:
  description: |
    The paragraph names six specific harmonisation surfaces (lawful grounds for
    processing personal data as training data; DPIAs; transparency obligations;
    rights of data subjects — access/erasure/correction; parental consent;
    children's rights). Each is a distinct sub-mechanism. Wire-formatting them
    individually would require six method:{} envelopes; consolidated here to
    avoid over-composition. Composition-before-extension confirmed.
  classification: T-2 (PASTORAL_PROSE — the enumeration sits in context rather
    than separating into discrete normative claims at sub-mechanism granularity)
nuance_lost: |
  This is the first Section D unit that explicitly bridges into the regional
  decision-locality; functionally it foreshadows Section E. The harmonisation
  goal is positive but the mechanism is hortatory ("should work towards").
```

---

## Unit D.012 — D.ecosystem.wider (lines 2277–2283): wider ecosystem collaboration

**Source** (lines 2277–2283): "it is also worthwhile for governments to explore collaboration across the wider ecosystem, which includes regulatory bodies, non-profit organisations, AI industry leaders, and other stakeholders... private and public sector collaboration ensures that both public and private entities develop and deploy AI in a secure and ethical manner."

```yaml
# Unit D.012 — wider-ecosystem multistakeholder collaboration
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:ai_innovation_ecosystem>:multistakeholder_collaboration"
      score: 0.70
      confidence: 0.70
      context: >
        Wider-ecosystem collaboration named across regulatory bodies, non-profit
        organisations, AI industry leaders, and other stakeholders. Different
        collaboration models contribute expertise at different lifecycle stages.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.wider (lines 2277-2283)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Secure and ethical manner" is the catch-phrase that the source treats as
  outcome-condition for public-private collaboration; in CIRIS terms that
  would split into non_maleficence + integrity composition, but the
  paragraph treats it as one phrase.
```

---

## Unit D.013 — D.ecosystem.startups (lines 2285–2289): government funding for AI start-ups

**Source** (lines 2285–2289): "Government agencies can also provide funding and grants to AI start-ups to help their employees gain the skills and knowledge to design, develop, and deploy better AI systems. This can be done through subsidising course fees for AI and AI ethics courses or providing start-ups with incentives when they adopt AI governance tools."

```yaml
# Unit D.013 — government funding for AI start-ups + governance-tool adoption incentives
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:ai_innovation_ecosystem>:startup_funding"
      score: 0.75
      confidence: 0.75
      context: >
        Government grants + funding for start-ups; subsidies for AI ethics
        course fees; incentives for governance-tool adoption. Aimed at
        trust-and-scaling outcomes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.startups (lines 2285-2289)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Trust in AI" + "AI adoption to scale across the region" outcome-framing
  reaches into Section-E regional scope; not enough load to need a separate
  envelope here.
```

---

## Unit D.014 — D.ecosystem.knowledge-sharing (lines 2291–2295): voluntary knowledge sharing forums

**Source** (lines 2291–2295): "Voluntary and mutually agreed knowledge sharing and exchange is also key to enriching the AI innovation ecosystem... government bodies can collaborate with industry partners to organise forums where successful AI use cases are presented."

```yaml
# Unit D.014 — voluntary knowledge sharing forums
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:ai_innovation_ecosystem>:knowledge_forums"
      score: 0.65
      confidence: 0.70
      context: >
        Voluntary forums for AI use-case + best-practice sharing organised
        by government-industry partnerships. Voluntary-and-mutually-agreed
        is the consent qualifier.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.knowledge-sharing (lines 2291-2295)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Voluntary and mutually agreed" is a non-trivial consent qualifier that
  could attach as `autonomy:consent_basis_voluntary` but is context-only here.
```

---

## Unit D.015 — D.ecosystem.platform (lines 2297–2301): AI start-up marketplace

**Source** (lines 2297–2301): "governments can work with relevant parties to develop an online platform or marketplace where AI start-ups can post about their offerings and how they are adhering to AI governance principles."

```yaml
# Unit D.015 — AI start-up marketplace + governance-principle adherence transparency
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:ai_innovation_ecosystem>:startup_marketplace"
      score: 0.60
      confidence: 0.65
      context: >
        Online marketplace where AI start-ups disclose offerings + governance-
        principle adherence; investors see them in one place. Transparency-as-
        value-proposition is the operational hook.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.ecosystem.platform (lines 2297-2301)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Adopt AI governance practices as it is seen as a value proposition" is a
  market-incentive theory of governance; CIRIS would treat that as a downstream
  effect rather than a wire claim.
```

---

## Unit D.016 — D.ecosystem.invest (lines 2303–2306): investment-attracting policies

**Source** (lines 2303–2306): "Promoting investments in AI start-ups is important to ensure that they can scale sufficiently... Governments should formulate policies to attract investment in AI start-ups."

```yaml
# Unit D.016 — investment-attracting policy formulation
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  "Governments should formulate policies to attract investment" is a hortatory
  recommendation without operational anchor (no specific policy class named;
  no mechanism-descriptive prefix lands). The structural claim is already
  carried by Unit D.013 (startup_funding method). Carry-forward citation only.
nuance_lost: |
  The scaling-to-bigger-players narrative implies a goal:{} envelope, but the
  source treats it as background motivation rather than a structural claim.
```

---

## Unit D.017 — D.rnd.intro (lines 2319–2329): R&D investment + sandboxes

**Source** (lines 2319–2329): "Investing in AI research and development ensures that countries are kept abreast of the latest developments in AI... Encouraging research related to the cybersecurity of AI, AI governance, and AI ethics is also key... Governments can fund AI research initiatives by providing grants... developing a development sandbox for researchers."

```yaml
# Unit D.017 — R&D investment + AI cybersecurity/governance/ethics research + sandboxes
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.85
      confidence: 0.80
      context: >
        National-government goal: AI R&D investment to keep current with AI
        developments + implement cutting-edge solutions for national problems.
        Cybersecurity + governance + ethics research are sub-priorities.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.intro (lines 2319-2329)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<goal:affiliations:ai_rnd>:research_sandbox"
      score: 0.75
      confidence: 0.75
      context: >
        Concrete method: development sandbox provides regulated environment
        for researcher product-iteration where authorities can ensure
        regulatory compliance pre-launch.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.intro (lines 2326-2329)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
nuance_lost: |
  "Safety and resiliency of AI systems and tools also advance in parallel"
  framing fits the CIRIS robustness/reliability principle but is context-only
  here. The sandbox compliance-check role (regulator dimension) is structurally
  a `licensure:{authority_id}` adjacent claim but not made explicit.
```

---

## Unit D.018 — D.rnd.talent (lines 2331–2335): AI talent pool + scholarships

**Source** (lines 2331–2335): "governments can build a talent pool of AI experts... Scholarships for post-graduate AI research or STEM-related undergraduate courses... Private companies can also be incentivised to upskill their employees."

```yaml
# Unit D.018 — AI talent pool building via scholarships + private-sector upskilling incentives
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<goal:affiliations:ai_rnd>:talent_scholarships"
      score: 0.75
      confidence: 0.75
      context: >
        Scholarships for post-graduate AI research + STEM undergrad to attract
        local and foreign talent; private-sector upskilling incentives for
        STEM employees.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.talent (lines 2331-2335)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Foreign talents" framing carries a non-trivial immigration-policy claim
  (open-borders for AI talent) that the source touches lightly; structural
  unmapping if treated as load-bearing.
```

---

## Unit D.019 — D.rnd.infrastructure (lines 2337–2342): digital infrastructure + open-source AI platforms

**Source** (lines 2337–2342): "Ensuring that there is proper digital infrastructure is also another enabler for AI research and development. Governments can work with partners in the private sector to set up and invest in digital infrastructure such as creating a use case laboratory... governments can also make AI research and development more accessible to organisations of all sizes by developing open-source AI platforms."

```yaml
# Unit D.019 — digital infrastructure + open-source AI platforms
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<goal:affiliations:ai_rnd>:open_source_platforms"
      score: 0.80
      confidence: 0.80
      context: >
        Open-source AI platforms freely available with tools + compute
        resources, lowering R&D barriers for organisations of all sizes.
        Use-case laboratory with data storage and compute capacity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.infrastructure (lines 2337-2342)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "detection:distributive:access:compute"
      score: 0.55
      confidence: 0.65
      context: >
        Positive-polarity attestation that open-source AI platforms with shared
        compute resources are anti-concentration. "Of all sizes" explicitly
        addresses the distributive-access concern.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.infrastructure (lines 2340-2342)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5"
verdict: composed
nuance_lost: |
  The mention of "compute resources to train and test AI systems" composes
  with `detection:distributive:access:compute` positively; the strength is
  modest because the proposal is structural (provide a platform) not
  consequence-measured.
```

---

## Unit D.020 — D.rnd.triple-helix (lines 2344–2346): triple-helix partnerships

**Source** (lines 2344–2346): "Governments can also work to establish triple helix partnerships between the research community, private sector, and government agencies."

```yaml
# Unit D.020 — triple-helix partnership
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<goal:affiliations:ai_rnd>:triple_helix_partnership"
      score: 0.65
      confidence: 0.70
      context: >
        Triple-helix partnership pattern (research community + private sector
        + government) for cross-pollination of ideas + discourse on pioneering
        technologies.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.triple-helix (lines 2344-2346)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  Same pattern as Unit D.012 wider-ecosystem collaboration but narrower
  (R&D-domain rather than full ecosystem); cited separately because the
  source treats them as distinct.
```

---

## Unit D.021 — D.rnd.data (lines 2348–2353): open data + linguistic/regional training-data relevance

**Source** (lines 2348–2353): "Via open data and data sharing, governments can ensure that there is a thriving and rich data environment for AI systems to be trained... it is also important that organisations work towards ensuring that AI systems have been trained on enough data relevant to their language(s), region, and industries."

```yaml
# Unit D.021 — open data + linguistic/regional/industry training-data relevance
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "fidelity:training_data_locale_relevance"
      score: 0.85
      confidence: 0.80
      context: >
        AI systems should be trained on data relevant to their language(s),
        region, and industries. This is a fidelity claim: model fidelity to
        deployment-context locale. Important for ASEAN's linguistic and
        regional diversity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.data (lines 2348-2353)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "detection:distributive:access:training_data"
      score: 0.45
      confidence: 0.65
      context: >
        Positive-polarity anti-concentration framing on training data; open
        data + diversity-of-source supports the framing that training-data
        access shouldn't be concentrated in those who already have it. Score
        positive but modest because mechanism is aspirational.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.rnd.data (lines 2348-2353)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5"
verdict: composed
nuance_lost: |
  The "language(s), region, and industries" requirement is the most operationally
  important claim in Section D for cross-source alignment: maps directly to MH's
  §§129–134 cultural-pluralism + IEEE EAD multi-traditional anchoring. Worth
  flagging in synthesis for triangulation queries.
```

---

## Unit D.022 — D.tools.intro (lines 2356–2365): adoption of AI governance tools

**Source** (lines 2356–2365): "AI governance processes can involve many rounds of checks and reviews by different stakeholders and may result in high costs when too many of such processes are done manually... Developers and deployers can make use of tools to enable the implementation of AI governance in operations."

```yaml
# Unit D.022 — adoption of AI governance tooling
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.75
      confidence: 0.75
      context: >
        Operational goal: scaled AI governance via tooling. Reasoning is
        manual review unsustainable as AI scales; tooling enables sustainable
        documentation + validation processes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.intro (lines 2356-2365)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "High costs when too many processes are done manually" framing is a scaling
  argument that the source uses as principal motivation. CIRIS does not have a
  cost-or-efficiency wire dimension; appropriately context-only.
```

---

## Unit D.023 — D.tools.provenance (lines 2376–2381): model provenance tools

**Source** (lines 2376–2381): "model provenance tools that keep track of and record every step of the system lifecycle... Without the use of such tools, employees will need to manually record every detail and human error may result in inaccurate model provenance records."

```yaml
# Unit D.023 — model provenance tooling
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:<goal:operational_governance>:model_provenance_tools"
      score: 0.85
      confidence: 0.85
      context: >
        Model provenance tools record training/testing data sources, processing
        steps, feature extraction, model selection. Essential for AI-at-scale
        visibility across many systems.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.provenance (lines 2376-2381)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "provenance:build_manifest:ai_system_lifecycle"
      score: 1.0
      confidence: 0.85
      context: >
        Direct alignment: model provenance tools map onto CIRIS's
        `provenance:build_manifest:*` family — the structural object is
        identical (signed lineage of system construction).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.provenance (lines 2376-2381)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (Verify: provenance:build_manifest:*)"
verdict: composed
nuance_lost: |
  The model-provenance / build-manifest alignment is the cleanest direct
  primitive-to-primitive mapping in Section D — worth a synthesis flag for
  multi-source alignment with MH (and EU HLEG's traceability requirement).
```

---

## Unit D.024 — D.tools.fairness (lines 2383–2389): AI fairness tools

**Source** (lines 2383–2389): "fairness tools to assess and mitigate fairness issues with AI systems... bias and fairness metrics and implement mitigation algorithms to correct unfair biasness."

```yaml
# Unit D.024 — fairness tools
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:<goal:operational_governance>:fairness_tools"
      score: 0.85
      confidence: 0.85
      context: >
        Fairness tools assess against bias/fairness metrics and apply mitigation
        algorithms. Mitigates user-trust degradation from inherent/other biases.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.fairness (lines 2383-2389)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:bias_metric_application"
      score: 0.85
      confidence: 0.80
      context: >
        Justice principle (CIRIS Accord) anchored by fairness-metric application.
        Maps directly to ASEAN Principle 2 (fairness and equity).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.fairness (lines 2383-2389)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice)"
verdict: composed
nuance_lost: |
  Specific metric families (statistical parity, equalized odds, etc.) are not
  named; the source treats "bias and fairness metrics" as a class. CIRIS
  detector calibration would pin specific metrics under
  `detection:correlated_action:rights_asymmetry:{population}`.
```

---

## Unit D.025 — D.tools.explainability (lines 2391–2397): explainable AI tools

**Source** (lines 2391–2397): "Developers and deployers can use explainable AI tools to understand and interpret predictions made by machine learning systems. A What-If Tool is an example of an explainable AI tool."

```yaml
# Unit D.025 — explainable AI tools
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:<goal:operational_governance>:explainability_tools"
      score: 0.80
      confidence: 0.80
      context: >
        Explainability tools for prediction interpretation; the What-If Tool
        example allows input-change re-runs to observe output sensitivity.
        Maps onto ASEAN Principle 1 (transparency and explainability) which
        is the operationalised target of this method.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.explainability (lines 2391-2397)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:explainability_disclosure"
      score: 0.80
      confidence: 0.80
      context: >
        Explainability framed as integrity-of-disclosure to humans (humans gain
        understanding of which features dominate the system's decision process).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.explainability (lines 2391-2397)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity)"
verdict: composed
nuance_lost: |
  The What-If Tool specific reference functions like a `delegates_to`-style
  third-party authority pin but isn't formalised as such; the source treats it
  as illustrative. "Validate some aspects of the AI system's behaviour" framing
  is the consumer-trust outcome.
```

---

## Unit D.026 — D.tools.aiverify (lines 2399–2402): multi-principle assurance tooling

**Source** (lines 2399–2402): "Organisations can also adopt tools that have a range of testing capabilities for different principles. For example, AI Verify can be used to conduct technical tests and process checks on AI systems against principles of explainability, fairness, as well as robustness."

```yaml
# Unit D.026 — multi-principle assurance tooling (AI Verify cited)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:<goal:operational_governance>:multi_principle_assurance"
      score: 0.80
      confidence: 0.80
      context: >
        Tools providing technical tests + process checks against multiple
        principles (explainability, fairness, robustness, transparency,
        security, accountability, data governance, human-centricity).
        AI Verify cited as instance — covers 8 of ASEAN's 7 guiding principles
        in one tooling surface.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.aiverify (lines 2399-2402)"
        - "AI Verify Foundation footnote 26 (line 2422)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  The 8-of-7 coverage map (the tool covers more principles than the Guide
  enumerates) is a noteworthy convergence point worth flagging in synthesis,
  but doesn't constitute a separate wire claim.
```

---

## Unit D.027 — D.tools.training (lines 2404–2407): training for tooling operation

**Source** (lines 2404–2407): "In order to fully reap the benefits of such useful tools, employees will also need to know how they work and how to use them to design, develop, and deploy AI responsibly. Government agencies can provide subsidies or grants for employees who wish to go for training."

```yaml
# Unit D.027 — government subsidies for tool-operator training
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:governance_tool_training"
      score: 0.70
      confidence: 0.70
      context: >
        Government subsidies / grants for employees seeking governance-tool
        training. Composes back into the workforce-capability approach
        (Unit D.002).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.training (lines 2404-2407)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  Cross-references both workforce-capability and operational-governance goals;
  cited under workforce-capability because the operative action is government
  subsidising training (not the goal being served).
```

---

## Unit D.028 — D.tools.community (lines 2409–2413): community co-development of tools

**Source** (lines 2409–2413): "it is also important to engage the wider developer community in co-developing tools. For example, in Singapore, IMDA has set up the AI Verify Foundation to harness the collective power and contributions of the global open-source community to develop the AI Verify testing tool."

```yaml
# Unit D.028 — community co-development of tools (AI Verify Foundation cited)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<goal:operational_governance>:community_codevelopment"
      score: 0.70
      confidence: 0.70
      context: >
        Engaging the wider developer community (global open-source) in co-
        developing AI governance tools. AI Verify Foundation cited as
        instance: harnesses collective open-source contributions for testing
        capabilities meeting global needs.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.community (lines 2409-2413)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Global" open-source explicitly broadens cohort_scope beyond ASEAN; the
  scope choice (species) reflects that the addressed community is global, not
  just regional. Foundation governance details unmapped.
```

---

## Unit D.029 — D.tools.bestpractices (lines 2415–2417): data governance + dev + cybersecurity best practices

**Source** (lines 2415–2417): "it is important that developers and deployers also adopt best practices in data governance, software development and cybersecurity to ensure that such tools do not compromise the well-being of users."

```yaml
# Unit D.029 — best practices in data governance + software dev + cybersecurity
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:user_wellbeing_safeguarded"
      score: 0.80
      confidence: 0.80
      context: >
        Triple best-practice stack — data governance + software development +
        cybersecurity — adopted to ensure tools do not compromise user
        wellbeing. The unifying structural claim: tools-themselves can become
        harm vectors if best-practice substrate is missing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.tools.bestpractices (lines 2415-2417)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence)"
verdict: clean
nuance_lost: |
  The three sub-domains (data gov / software dev / cybersecurity) each carry
  rich practice traditions; CIRIS would cite each domain's standard via
  evidence_refs in a deployed envelope but the source treats them as a cluster.
```

---

## Unit D.030 — D.awareness.intro + engagement + education (lines 2431–2443): citizen AI awareness

**Source** (lines 2431–2443): "By raising awareness of the potential risks and benefits of AI, citizens can make informed decisions... engaging with the public through roadshows, social media platforms and other public forums to demonstrate AI technologies... Policymakers and the relevant government agencies can also look at how to incorporate AI into general education."

```yaml
# Unit D.030 — citizen AI awareness via public engagement + general education
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "autonomy:informed_citizen_decision_making"
      score: 0.85
      confidence: 0.85
      context: >
        Citizens making informed decisions about appropriate AI use + self-
        protection from harmful AI. Autonomy-anchored at the public-citizen
        level; method is awareness-raising via roadshows + social media + AI
        in general education.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.intro+engagement+education (lines 2431-2443)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:workforce_capability>:public_awareness"
      score: 0.75
      confidence: 0.75
      context: >
        Public engagement via roadshows + social media + public forums; AI
        incorporated into general education. Private-company partnerships
        named for everyday-app AI demonstration.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.intro+engagement+education (lines 2436-2443)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
nuance_lost: |
  Three sub-paragraphs consolidated because they form one operational cluster
  (public awareness → engagement → general education). Cross-pollination of
  workforce-capability and citizen-empowerment is real: the same approach
  envelope serves both.
```

---

## Unit D.031 — D.awareness.chatbots (lines 2445–2451): AI-disclosure for citizen-facing services

**Source** (lines 2445–2451): "Government agencies can also consider implementing AI-enabled technologies for citizen-facing applications... a general disclosure should also be provided to inform citizens that they will be interacting with an AI system and what the AI system is expected to do when under normal behaviour. There should also be an avenue for citizens to provide feedback."

```yaml
# Unit D.031 — AI-system disclosure to citizens + feedback channel for malfunction
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:ai_interaction_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        "General disclosure should also be provided to inform citizens that
        they will be interacting with an AI system." Maps to CIRIS's
        never-deny-AI posture (language_guidance/en.txt + per-locale
        operational ethics) — a direct integrity claim about non-deception of
        AI-nature to humans.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.chatbots (lines 2445-2451)"
        - "ContributionRef(source_material/language_guidance/en.txt never-deny-AI)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:<goal:operational_governance>:citizen_feedback_channel"
      score: 0.80
      confidence: 0.80
      context: >
        Citizen feedback channel especially for malfunction cases, so
        mitigations can prevent further misinformation or harm. The feedback
        channel composes onto a downstream Moderation/Reconsideration pathway
        in CIRIS terms.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.chatbots (lines 2448-2451)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
nuance_lost: |
  This unit is one of the cleanest direct alignments in Section D: AI-disclosure
  maps to never-deny-AI; feedback channel maps to moderation/reconsideration.
  Strong cross-source candidate for synthesis multi-source-alignment query.
  Mutability:constitutional on the disclosure envelope reflects that
  non-deception of AI-nature is a hard constraint in the framework.
```

---

## Unit D.032 — D.awareness.vulnerable (lines 2453–2458): protection from AI-generated misinformation

**Source** (lines 2453–2458): "vulnerable citizens are protected from malicious actors using AI with ill intentions, such as to generate or disseminate misinformation and online falsehoods... media literacy education to educate the public on how to identify and verify credible sources of information."

```yaml
# Unit D.032 — vulnerable-citizen protection + media literacy
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:disinformation_at_scale"
      score: -1.0
      confidence: 0.95
      context: >
        Hard prohibition against malicious AI uses for misinformation/online
        falsehoods, especially against vulnerable citizens. Composes onto
        CIRIS prohibitions on DECEPTION_FRAUD and ELECTION_INTERFERENCE
        category families.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.vulnerable (lines 2453-2458)"
        - "ContributionRef(source_material/prohibitions.py DECEPTION_FRAUD)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "method:<approach:public_awareness>:media_literacy_education"
      score: 0.85
      confidence: 0.85
      context: >
        Media literacy education as concrete public-education method to
        equip citizens for source-credibility verification + misinformation
        identification.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.vulnerable (lines 2455-2458)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:vulnerable_population_protection"
      score: 0.90
      confidence: 0.85
      context: >
        Vulnerable-citizen protection explicitly named. Composes with the
        §6.1.4 lexical-vulnerability-priority consumer policy: most-affected
        populations get tie-breaking weight.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §D.awareness.vulnerable (lines 2453-2454)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence) + §6.1.4"
verdict: composed
nuance_lost: |
  The three composed primitives together carry the multi-vector claim:
  (a) prohibition against malicious actors; (b) operational method to empower
  citizens; (c) accord-principle anchoring of vulnerable-population protection.
  "Vulnerable" not narrowly defined — composes with §6.1.4 weighting in
  deployment.
```

---

# Section E — Regional-level Recommendations

Intent (line 2472): "for policy makers." Section E shifts the decision-locality up from `national` to `regional`. Every Section E Contribution carries `locality:decision:regional` either explicitly or implicitly via the multilateral_participation envelope's forum field (`asean`). This is the strongest exercise of the FSD-002 §3.9 multilateral_participation + §3.6.5 locality:decision composition in the entire batch.

---

## Unit E.001 — E.preamble + workinggroup.intro (lines 2471–2482): ASEAN Working Group on AI Governance

**Source** (lines 2474–2482): "Setting up an ASEAN Working Group on AI Governance to drive and oversee AI governance initiatives in the region. The ASEAN Working Group on AI Governance can lead the technical and operational implementation of AI governance action plans in the region. The Working Group can consist of representatives from each of the ASEAN member states... The ASEAN Working Group can also lead efforts to further international cooperation on AI governance approaches."

```yaml
# Unit E.001 — ASEAN Working Group on AI Governance: three-primitive composition
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:working_group_membership"
      score: 1.0
      confidence: 0.90
      context: >
        ASEAN Working Group on AI Governance proposed with member-state
        representatives + working-group remit for technical and operational
        implementation of regional AI governance. The Working Group is the
        named regional-coordination body; multilateral_participation:asean
        with kind=working_group_membership is the natural composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.intro (lines 2474-2482)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (multilateral_participation:{forum}:{kind})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "locality:decision:regional"
      score: 1.0
      confidence: 0.95
      context: >
        AI governance decisions named at regional decision-locality. Per
        FSD-002 §6.1.5, the Working Group operates at regional cell scope;
        quorum requirements scale accordingly. This is the strongest
        locality:decision:regional anchor in the entire batch.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.intro (lines 2474-2480)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "partner_role:regional_coordinator"
      score: 1.0
      confidence: 0.85
      context: >
        The Working Group's role qualifies as a regional-coordinator partner
        role per FSD-002 §3.9 (Registry partner_role family). Distinct from
        merely being a forum participant; the Group leads technical and
        operational implementation across member states.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.intro (lines 2476-2480)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (partner_role:{role})"
verdict: composed
residual:
  description: |
    The Working Group has two distinct sub-roles in this single paragraph —
    "lead the technical and operational implementation" (executor) AND "lead
    efforts to further international cooperation on AI governance approaches,
    including through engaging ASEAN's various dialogue partners" (external-
    affairs facilitator). The two roles compose under partner_role but at
    different granularity (executor inside ASEAN vs. dialogue-partner
    coordinator outward). Composition-before-extension attempted; the existing
    partner_role:* family covers each individually, but a regional-IGO body
    that holds BOTH simultaneously is not currently named.
  classification: T-3 (EXPRESSIVE_GAP — moderate)
proposed_extension:
  name: "partner_role:regional_intergovernmental_working_group_dual_remit"
  description: |
    A regional-IGO working-group role distinguishing between (a) intra-regional
    operational implementation authority and (b) extra-regional dialogue-partner
    engagement authority, both held simultaneously by one body. Useful because
    the operational implications differ: (a) implies quorum at regional cell
    scope; (b) implies cross-federation participation envelopes outward. Current
    partner_role:* is single-role; this would be the first dual-role within one
    role attestation.
  gate_verification:
    T1: yes (rule-set definable)
    T2: yes (mechanism-descriptive — names the dual operational remit, not a
      judgment quality)
    T3: yes (versionable per partner_role family practice)
    T4: yes (never sole evidence for slashing:*)
  priority: MEDIUM
  composition_attempted: |
    Tried: two separate partner_role attestations on the same key_id, one for
    each sub-role. Works mechanically but loses the structural claim that ONE
    body holds BOTH simultaneously — which is the point of the source's
    framing. The dual remit IS the load-bearing claim, not the separate roles.
nuance_lost: |
  The Working Group's relationship to ADGMIN (the parent ministerial meeting that
  endorsed the Guide) is not made explicit; structurally this is a delegates_to
  relationship in CIRIS terms (ADGMIN delegating implementation authority to the
  Working Group). Source treats it implicitly. The "where appropriate, include
  consultation with other industry partners for their views and input" clause
  carries a witness-diversity intuition that doesn't quite map onto
  witness_diversity (which is technical N=3 jurisdictional/organisational/stack/
  expertise) — closer to consultative-stakeholder framing.
```

---

## Unit E.002 — E.workinggroup.responsibilities, item 1 (line 2488): regional tools for AI governance

**Source** (line 2488): "Development and implementation of regional tools for AI governance."

```yaml
# Unit E.002 — Working Group responsibility 1: regional tools development
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:regional_tool_development"
      score: 1.0
      confidence: 0.85
      context: >
        Working Group remit item 1: develop + implement regional AI governance
        tools. Maps directly onto multilateral_participation as a kind value.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 1 (line 2488)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9"
verdict: clean
nuance_lost: |
  The bullet is terse (single phrase); the load-bearing content is in
  composition with Unit E.001's locality:decision:regional anchor.
```

---

## Unit E.003 — E.workinggroup.responsibilities, item 2 (lines 2492–2493): regional workforce upskilling

**Source** (lines 2492–2493): "Provision of support and recommendations for policies to nurture AI talent and upskill workforce across ASEAN."

```yaml
# Unit E.003 — Working Group responsibility 2: regional workforce policies
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:workforce_policy_coordination"
      score: 0.85
      confidence: 0.80
      context: >
        Working Group remit item 2: support and recommendations for AI talent
        + workforce upskilling policies across ASEAN. This is the regional
        elevation of Unit D.002 workforce-capability goal.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 2 (lines 2492-2493)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_attestation_id: "<Unit_D_002_workforce_goal_attestation_id>"
    attestation_envelope:
      references_attestation_id: "<Unit_D_002 attestation_id>"
      supersession_reason: "scope_elevation_national_to_regional"
      differs_in: ["cohort_scope", "decision_locality"]
      witness_relation: external
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 2 (lines 2492-2493)"
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
nuance_lost: |
  The supersedes link from Unit D.002 to Unit E.003 captures the
  scope-elevation pattern: the same operational shape (workforce-capability)
  surfaces at both national and regional decision-localities; E supersedes D
  at the regional layer. Not a recantation — both attestations remain valid at
  their respective scopes.
```

---

## Unit E.004 — E.workinggroup.responsibilities, item 3 (lines 2496–2497): regional AI ecosystem + start-up investment

**Source** (lines 2496–2497): "Provision of support and recommendations for initiatives to support the AI ecosystem in ASEAN and promote investment in AI start-ups."

```yaml
# Unit E.004 — Working Group responsibility 3: regional ecosystem + start-up investment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:ecosystem_investment_coordination"
      score: 0.85
      confidence: 0.80
      context: >
        Working Group remit item 3: support + recommendations for regional AI
        ecosystem + start-up investment promotion. Regional elevation of
        Units D.008–D.016 (national ecosystem cluster).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 3 (lines 2496-2497)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9"
verdict: clean
nuance_lost: |
  Supersedes chain to multiple D-units (D.008–D.016) implicit; not declared
  individually to avoid over-composition. Synthesis can chain explicitly if
  needed.
```

---

## Unit E.005 — E.workinggroup.responsibilities, item 4 (lines 2500–2501): R&D cross-pollination

**Source** (lines 2500–2501): "Provision of platforms to encourage cross-pollination of ideas between the AI research and development community and ASEAN."

```yaml
# Unit E.005 — Working Group responsibility 4: regional R&D cross-pollination
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:rnd_cross_pollination"
      score: 0.80
      confidence: 0.75
      context: >
        Working Group remit item 4: platform-provision for R&D community ↔
        ASEAN cross-pollination. Regional elevation of Unit D.020 triple-
        helix partnership pattern.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 4 (lines 2500-2501)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9"
verdict: clean
nuance_lost: |
  "Cross-pollination" is the recurring metaphor across Section D (twice) and
  Section E (once); CIRIS does not have an idea-flow wire dimension. The
  structural intent (platform-mediated dialogue) is covered by the
  multilateral_participation envelope itself.
```

---

## Unit E.006 — E.workinggroup.responsibilities, item 5 (lines 2504–2506): keeping abreast of new developments + governance-framework updates

**Source** (lines 2504–2506): "Keeping abreast of new developments in the AI space (e.g., generative AI) and related emerging technology and making recommendations on updates to be made to the AI governance frameworks in the region."

```yaml
# Unit E.006 — Working Group responsibility 5: emerging-tech monitoring + governance-framework update recommendations
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:governance_framework_evolution"
      score: 0.90
      confidence: 0.85
      context: >
        Working Group remit item 5: emerging-technology monitoring (generative
        AI cited as instance) + governance-framework update recommendations
        for the region. Maps onto FSD-002's amendment-process pattern at the
        regional layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 5 (lines 2504-2506)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "method:<approach:governance_framework_evolution>:emerging_tech_monitoring"
      score: 0.85
      confidence: 0.80
      context: >
        Concrete method: keep abreast of emerging tech (gen AI named) and
        recommend governance-framework updates. Forecasts Unit E.007's
        gen-AI cluster as the first deliverable.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.workinggroup.responsibilities item 5 (lines 2504-2506)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
nuance_lost: |
  The wire-format amendment-process analogue (FSD-002 §4.9.2 P5 Contribution →
  P10 → P8 → 1-of-6 sign-off) maps loosely onto the Working Group's
  recommendation pattern; the source treats it informally rather than as a
  structured amendment flow.
```

---

## Unit E.007 — E.genai.intro (lines 2510–2519): generative AI definition + adaptation imperative

**Source** (lines 2510–2519): "Generative AI, refers to a branch of artificial intelligence where new content, such as text, imagery, and audio, is created by algorithms in response to prompts... Generative AI systems have recently been able to produce outputs that are remarkably realistic and sometimes indistinguishable from human-created content... the responsible development and deployment of generative AI also raises complex ethical, legal, and societal issues that require careful attention."

```yaml
# Unit E.007 — generative AI scope + ethical/legal/societal-issue framing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.80
      confidence: 0.75
      context: >
        Responsible development + deployment of generative AI named as ASEAN-
        regional goal addressing complex ethical, legal, societal issues. Goal
        is species-scope because gen-AI outputs (text/imagery/audio
        indistinguishable from human-created) implicate humanity broadly;
        decision-locality remains regional via the Working Group remit.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.intro (lines 2510-2519)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
nuance_lost: |
  "Remarkably realistic and sometimes indistinguishable from human-created" is
  the operative concern that drives subsequent units E.008.* (the six risks).
  Definitional framing of "generative AI" is technical; not a separate wire
  claim.
```

---

## Unit E.008 — E.genai.risks, item 1 — Mistakes and anthropomorphism (lines 2530–2534)

**Source** (lines 2530–2534): "Generative AI models are not fool-proof and can sometimes make mistakes. However, these mistakes often appear to be highly coherent and human-like, and take on anthropomorphisation, commonly known as 'hallucinations'."

```yaml
# Unit E.008 — generative AI risk: hallucinations + anthropomorphism
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:hallucinated_output_misleading"
      score: 0.85
      confidence: 0.85
      context: >
        Risk class: generative-AI hallucinations + anthropomorphisation of
        errors. Coherent and human-like presentation of erroneous output is
        the failure mode. Cited examples: erroneous medical responses,
        vulnerable software code.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.risks item 1 (lines 2530-2534)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence)"
verdict: clean
nuance_lost: |
  The CIRIS conscience faculty `epistemic_humility` directly addresses this
  failure mode; not a separate wire claim here. "Anthropomorphisation" carries
  a deeper psychological-trust-degradation concern that is partly mapped by
  Unit D.031 AI-disclosure but not separately wire-claimed.
```

---

## Unit E.009 — E.genai.risks, item 2 — Factually inaccurate responses + disinformation (lines 2535–2539)

**Source** (lines 2535–2539): "Generative AI systems can be used to generate and propagate false or misleading information to a larger scale, shaping public perception and eroding trust in reliable sources of information."

```yaml
# Unit E.009 — generative AI risk: disinformation + trust erosion
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:disinformation_at_scale"
      score: -1.0
      confidence: 0.90
      context: >
        Hard-constraint prohibition: generative-AI-amplified disinformation
        eroding trust in reliable information sources. Composes with Unit
        D.032's misinformation-prohibition; the scaling difference (generative
        AI at "larger scale") is the elevation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.risks item 2 (lines 2535-2539)"
        - "ContributionRef(source_material/prohibitions.py DECEPTION_FRAUD)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:ecology_of_communication:disinformation_at_scale"
      score: -0.80
      confidence: 0.75
      context: >
        F-3 detector axis (v1.3) for ecology-of-communication degradation
        through correlated disinformation generation. Generative-AI's
        scale-amplification is the structural-injustice mechanism.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §E.genai.risks item 2 (lines 2535-2539)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
verdict: composed
nuance_lost: |
  The trust-in-reliable-sources erosion is the structural-injustice mechanism
  that composes both as a hard prohibition AND as a population-scale detector
  axis. Worth noting in synthesis as a cross-source candidate (MH §§158–164
  Babel-of-communication critique).
```

---

## Unit E.010 — E.genai.risks, item 3 — Deepfakes + impersonation + fraud (lines 2541–2550)

**Source** (lines 2541–2550): "Generative AI carries certain risks of being used for impersonation due to its ability to generate realistic content... One such risk is the use of generative AI to create deepfakes... in the use of generative AI to develop phishing emails."

```yaml
# Unit E.010 — generative AI risk: deepfakes + impersonation + phishing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception"
      score: -1.0
      confidence: 0.95
      context: >
        Hard-constraint prohibition: deepfake-mediated impersonation, divulging
        of confidential/personal information via posing as real individuals,
        AI-enhanced phishing. The grammatically-clean phishing scenario
        explicitly weakens the human-discrimination capacity that historically
        let users distinguish legitimate from compromised emails.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.risks item 3 (lines 2541-2550)"
        - "ContributionRef(source_material/prohibitions.py DECEPTION_FRAUD)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
verdict: clean
nuance_lost: |
  The "common red flag" of misspellings/grammar errors being eliminated by
  gen-AI is structurally an informational-asymmetry shift; could compose with
  `detection:correlated_action:informational_asymmetry:scope`. Source treats
  it as observation rather than mechanism-claim.
```

---

## Unit E.011 — E.genai.risks, item 4 — Intellectual property infringement (lines 2552–2561)

**Source** (lines 2552–2561): "The development of generative AI systems requires huge amounts of data for model training, validation, and testing. This raises concerns about the use of copyrighted materials... Generative AI systems can also learn from copyrighted material, such as images and music, without proper authorisation from the copyright holder."

```yaml
# Unit E.011 — generative AI risk: IP infringement (training data + style mimicry)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:copyright_infringement_unacknowledged"
      score: 0.75
      confidence: 0.75
      context: >
        Positive-polarity attestation that copyright-infringement-in-training
        and style-mimicry-without-authorisation must be acknowledged and
        mitigated as harm vectors. The legal-repercussion concern is paired
        with the structural-fairness concern about creator rights.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.risks item 4 (lines 2552-2561)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence)"
verdict: partial
residual:
  description: |
    "Insufficiently transformative" is a legal-test phrase (fair-use doctrine)
    that the source uses without making the legal-test wire-form explicit.
    Jurisdiction-specific copyright law is the substrate; the wire format does
    not adjudicate substrate-level legal doctrine. The unmapped operational
    claim is that creators' rights must be respected — sustainable as a moral
    claim under non_maleficence but the legal-doctrine layer remains unmapped.
  classification: T-2 (PASTORAL_PROSE — legal-doctrine specifics correctly sit
    in jurisdictional law substrate, not wire format)
nuance_lost: |
  Cross-jurisdiction copyright variability ("local copyright laws" cited
  explicitly) means this is one of the units where the wire-format claim is
  necessarily generic; the actual operational shape is jurisdiction-dependent.
  Composes naturally with cohort_scope: affiliations for jurisdictional
  composition in deployment.
```

---

## Unit E.012 — E.genai.risks, item 5 — Privacy + confidentiality (lines 2563–2569)

**Source** (lines 2563–2569): "Unlike traditional AI systems, generative AI systems have a tendency to memorise... Malicious actors may be able to reconstruct training data by querying the generative AI system, and this can compromise the privacy of individuals represented by the dataset, especially in cases where sensitive datasets (e.g., medical datasets) are used."

```yaml
# Unit E.012 — generative AI risk: training-data memorisation + reconstruction attacks
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:privacy_reconstruction_attack"
      score: 0.90
      confidence: 0.85
      context: >
        Memorisation-driven training-data reconstruction attack named as
        privacy harm class. Medical-dataset case cited as sensitive. Corporate
        confidential-info disclosure during gen-AI interaction also flagged.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.risks item 5 (lines 2563-2569)"
        - "Berkeley AI Research memorisation footnote 27 (line 2574)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence)"
verdict: clean
nuance_lost: |
  "Unconsciously disclose confidential information" framing names a corporate
  user-behaviour failure mode that composes with autonomy:informed_consent
  but the source treats it as one-line observation. PETs from Unit D.010 are
  the natural mitigation chain.
```

---

## Unit E.013 — E.genai.risks, item 6 — Propagation of embedded biases (lines 2584–2590)

**Source** (lines 2584–2590): "Generative AI systems have the ability to capture and reflect the biases present in the training dataset. If not properly addressed, these biases can be inherited and result in biased or toxic output that reinforces biased or discriminatory stereotypes. For example, image generation systems prompted with 'African worker' may generate images of individuals in tattered clothing and rudimentary tools, while simultaneously generating images of wealthy individuals when prompted with 'European worker'."

```yaml
# Unit E.013 — generative AI risk: foundation-model bias propagation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 0.95
      context: >
        Hard-constraint prohibition: bias propagation from foundation models
        to downstream models trained from them. The African/European worker
        worked example operationalises the harm class as racial/geographic
        stereotype-reinforcement through gen-AI imagery.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.risks item 6 (lines 2584-2590)"
        - "ContributionRef(source_material/prohibitions.py DISCRIMINATION)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:rights_asymmetry:racial_geographic_stereotype_reinforcement"
      score: -0.85
      confidence: 0.80
      context: >
        F-3 detector axis: population-scale rights-asymmetry from gen-AI bias
        propagation. The worked example demonstrates exactly the kind of
        correlated-action mechanism the detector watches for (individual
        prompts compose to harm of non-participants whose self-image is
        misrepresented).
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide §E.genai.risks item 6 (lines 2584-2590)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
verdict: composed
nuance_lost: |
  The foundation-model → downstream-model propagation chain is itself a
  delegates_to-style authority-inheritance pattern: downstream models inherit
  the bias-substrate via training. Composition-before-extension confirmed:
  this maps cleanly onto existing primitives.
```

---

## Unit E.014 — E.genai.adaptation (lines 2595–2618): adaptation imperative + shared-responsibility framework + watermarks

**Source** (lines 2595–2618): "Generative AI brings with it unique risks and the principles and components of AI governance defined in this Guide may need to be adapted to ensure responsible design, development, and deployment of generative AI... there is space for policymakers to facilitate and co-create with developers a shared responsibility framework... it would be useful to provide specific guidance on how governance processes can be adapted to provide users with the ability to distinguish AI-generated content versus authentically generated ones through transparency. One way is to create a digital 'watermark' that can be tagged to content generated by generative AI systems."

```yaml
# Unit E.014 — generative AI adaptation: shared-responsibility framework + watermarking
contributions:
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_attestation_id: "<asean_guide_v1_principles_components_attestation_set_id>"
    attestation_envelope:
      references_attestation_id: "<asean_guide_v1 principles+components attestation set>"
      supersession_reason: "scope_extension_for_generative_ai"
      differs_in: ["scope", "context", "evidence_refs"]
      witness_relation: external
      evidence_refs:
        - "asean_guide §E.genai.adaptation (lines 2595-2618)"
        - "IMDA + Aicadium Generative AI discussion paper footnote 28 (line 2627)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      schema_ref: "FSD-002 §2.2.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "method:<approach:governance_framework_evolution>:shared_responsibility_framework"
      score: 0.80
      confidence: 0.80
      context: >
        Shared-responsibility framework co-created between policymakers and
        developers clarifies responsibilities of all parties in the AI system
        lifecycle + safeguards each undertakes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.adaptation (lines 2603-2606)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:<approach:gen_ai_transparency>:content_watermarking"
      score: 0.80
      confidence: 0.80
      context: >
        Digital watermarks tagged to gen-AI-generated content so users can
        distinguish AI-generated from authentically-generated content.
        Operational transparency mechanism for gen-AI outputs. Composes back
        to Unit D.031's AI-interaction disclosure pattern but at the content
        layer rather than the system layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.adaptation (lines 2613-2618)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:ai_generated_content_disclosure"
      score: 1.0
      confidence: 0.90
      context: >
        Integrity claim: AI-generated content should be disclosed to users.
        Watermarking is the proposed method; the integrity claim itself is
        the load-bearing structural object. Cross-source candidate with
        EU HLEG §1.4 transparency + IEEE EAD content-transparency framing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.adaptation (lines 2613-2618)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity)"
verdict: composed
nuance_lost: |
  The "developer accountability and integrity" sub-claim (lines 2608-2610) is
  carried forward as future-version commitment; the source defers it as
  "could also be developed" — not a current claim but a future commitment
  that supersedes-chains naturally to a future asean_guide_v2 batch.
  The 4-primitive composition here (supersedes + 2 methods + 1 integrity
  claim) is the heaviest in Section E; honest because the paragraph names
  4 distinct structural objects.
```

---

## Unit E.015 — E.genai.next (lines 2620–2622): generative AI as initial Working Group project

**Source** (lines 2620–2622): "With the introduction and rapid uptake of generative AI systems, it is imperative that ASEAN builds on this current framework to develop governance guidelines for generative AI. This is also a good initial project for the proposed ASEAN Working Group to take up."

```yaml
# Unit E.015 — generative AI guidelines as Working Group's initial project
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "method:<approach:governance_framework_evolution>:generative_ai_initial_project"
      score: 0.85
      confidence: 0.80
      context: >
        Working Group's first concrete project: develop generative-AI
        governance guidelines building on the current asean_guide_v1
        framework. Time-bounded commitment (initial; explicitly first).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.genai.next (lines 2620-2622)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: clean
note: |
  This anticipates the actual January 2025 "Expanded ASEAN Guide on AI
  Governance and Ethics — Generative AI" supplement (per manifest line 16).
  When that supplement is mapped as a separate batch, a supersedes link from
  this method envelope would be the natural connection: the project landed.
nuance_lost: |
  "Imperative" framing is strong but the operational claim is sequencing
  (first-up project for Working Group); the imperative content reaches into
  Unit E.014's supersedes chain.
```

---

## Unit E.016 — E.compendium (lines 2643–2658): regional use-case compendium

**Source** (lines 2643–2658): "A compendium of AI governance practices could be useful to practically illustrate how various organisations and/or government agencies in ASEAN have implemented or aligned their AI governance practices with the ASEAN Guide on AI Governance and Ethics... establishing a virtuous cycle of trust in AI."

```yaml
# Unit E.016 — regional compendium of use cases
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:practice_compendium"
      score: 0.75
      confidence: 0.75
      context: >
        Regional compendium of AI governance practices from ASEAN
        organisations and government agencies, illustrating asean_guide_v1
        implementation and tailoring. Trust-building outcome for users +
        stakeholders + extra-regional showcase.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.compendium (lines 2643-2658)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-working-group-on-ai-governance>"
    attestation_envelope:
      dimension: "method:<approach:regional_coordination>:practice_showcase"
      score: 0.70
      confidence: 0.70
      context: >
        Practice-showcase method: featured organisations build trust + promote
        themselves as responsible AI practitioners beyond ASEAN. Virtuous-
        cycle theory: more participation → broader implementation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §E.compendium (lines 2651-2658)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
nuance_lost: |
  "Virtuous cycle of trust" is the outcome framing the source uses; CIRIS
  does not name virtuous-cycle dynamics as a wire dimension but the structural
  intent (trust-building through visible practice) is carried by the
  composition.
  Note: This is also where Annex B (Use Cases) lives operationally — the
  compendium proposed in E.016 is the regional generalisation of Annex B's
  six member-state-specific use cases (Aboitiz / EY / Gojek / UCARE.AI /
  Smart Nation Group / MoE Singapore).
```

---

# Section F — Conclusion

The Conclusion (lines 2664–2695) is brief — three substantive paragraphs. Two map to structural Contributions (carry-forward of ASEAN's purpose + the voluntary-application clause); the third is pastoral/scaffolding.

---

## Unit F.001 — F.intro (lines 2670–2675): ASEAN collaborative purpose + Guide as regional best-practice

**Source** (lines 2670–2675): "One of the aims and purposes of ASEAN is to promote active collaboration and mutual assistance on matters of common interest in the economic, social, technical, and scientific fields. This Guide is collaboratively developed by all ASEAN member states and will serve as a regional best practice guidance on AI governance and ethics."

```yaml
# Unit F.001 — ASEAN collaborative purpose anchoring + Guide as regional best-practice instrument
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "multilateral_participation:asean:membership"
      score: 1.0
      confidence: 0.95
      context: >
        ASEAN's foundational purpose (active collaboration and mutual assistance
        across economic/social/technical/scientific fields) named as the
        framework's authority anchor. The Guide itself is the deliverable —
        collaboratively developed by all member states, serving as regional
        best-practice instrument for AI governance and ethics.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §F.conclusion (lines 2670-2675)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (multilateral_participation:{forum}:{kind})"
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_attestation_id: "<asean_charter_or_treaty_authority_attestation_id>"
    attestation_envelope:
      delegated_scope: ["regional_ai_governance_best_practice_definition"]
      delegation_purpose: "authority_source"
      delegation_valid_from: "2024-02-02"
      witness_relation: external
      evidence_refs:
        - "asean_guide §F.conclusion (lines 2670-2675)"
        - "ADGMIN-4 endorsement reference (manifest endorsement_forum)"
      schema_ref: "FSD-002 §2.2.1"
verdict: composed
nuance_lost: |
  The delegates_to envelope ties the Guide's authority back to ASEAN's
  charter / treaty-equivalent foundational purpose; in wire terms this
  formalises what the conclusion states implicitly. The "regional best
  practice guidance" framing is a positive standing claim about the Guide
  itself, but the score lives more naturally in the multilateral_participation
  envelope's strength than in a separate integrity:* envelope.
```

---

## Unit F.002 — F.living-document (lines 2677–2683): practical, living, voluntary, non-legal-supplanting

**Source** (lines 2677–2683): "This Guide also serves as a practical guide for organisations and government agencies in the region that wish to design, develop, and deploy AI technologies. It is not meant to be exhaustive and static but rather, a living document that is periodically reviewed and enhanced as needed. Member states, developers and deployers operating in their jurisdictions are recommended to apply, on voluntary basis, the provisions in this Guide. Nothing in this Guide may be interpreted as replacing or changing any party's legal obligations or rights under any member state's laws."

```yaml
# Unit F.002 — living-document + voluntary application + legal-non-supplant clause
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "<federation:asean-member-states>"
    attestation_envelope:
      dimension: "integrity:guide_voluntary_application"
      score: 0.85
      confidence: 0.90
      context: >
        Voluntary-application clause: member states + developers + deployers
        are "recommended to apply, on voluntary basis, the provisions in this
        Guide." This sets the framework's stake at reputational/recommendation
        level, not at binding-law level. Critical for cross-source composition:
        the asean_guide_v1 should NOT be composed at constitutional mutability
        for jurisdiction-binding-law decisions; the source explicitly defers
        to member-state law.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §F.conclusion (lines 2681-2683)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:asean_guide_v1>"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:living_document_periodic_review"
      score: 0.85
      confidence: 0.85
      context: >
        Living-document commitment: "periodically reviewed and enhanced as
        needed." Structurally signals that future supersedes-chains are
        expected. The fidelity claim is to maintenance of the document under
        change — the version will be superseded; the commitment to do so
        responsibly is the standing claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide §F.conclusion (lines 2677-2679)"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity)"
verdict: composed
residual:
  description: |
    The legal-non-supplant clause ("Nothing in this Guide may be interpreted
    as replacing or changing any party's legal obligations or rights under any
    member state's laws") is structurally a precedence-ordering rule: member-
    state law has priority over asean_guide_v1 provisions where they intersect.
    This is jurisdictional-precedence content. CIRIS does not have a wire
    primitive that explicitly encodes "this source defers to that source on
    matters of legal effect"; the closest existing mechanism is the cohort_
    scope: affiliations + amendable mutability + conflict-resolution via
    §6.1.4 lexical-vulnerability-priority. Composition-before-extension
    confirmed.
  classification: T-2 (PASTORAL_PROSE — but with composition-load: the cohort_
    scope + mutability fields together carry the operational shape; this is
    not a true gap, it is honest deferral to substrate legal layer)
nuance_lost: |
  The "exhaustive and static" framing in Unit F.002 explicitly invites future
  supersedes chains (matching the Working Group's responsibility item 5 in
  Unit E.006). The two paragraphs (E.006 + F.002) together commit to a
  living governance fabric — methodology and supersession discipline are
  thus paired structural claims, not separate concerns.
```

---

## Unit F.003 — closing scaffolding

```yaml
# Lines 2664-2670 and trailing blank lines / page references
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Page-references and the "Conclusion" header line itself are pure
  navigational scaffolding. Per LANGUAGE_PRIMER §8 Step 1(b): structural/
  navigational framing correctly stays in prose.
nuance_lost: |
  None — there is no operational content to lose. The substantive Conclusion
  content is fully covered by Units F.001 + F.002.
```

---

# Section-aggregate summary

**Total atomic units mapped**: 51 wire-units (Section D: D.001–D.032 = 32 units; Section E: E.001–E.016 = 16 units; Section F: F.001–F.003 = 3 units). Unit D.030 consolidates 3 source paragraphs into one wire-unit so atomic source-paragraphs ≈ 53 mapped via 51 wire-units.

**Verdict distribution** (counted directly from the 51 verdict-tagged YAML blocks):

| Verdict | Count |
|---|---|
| clean | 23 |
| composed | 25 |
| partial | 1 |
| not-translated | 2 |

Residual-note blocks attached to composed verdicts: 3 (Units D.011, E.001, F.002). These are not separate verdict categories — composition carries the operational shape; the residual notes flag T-2 prose or T-3 candidates surfaced during composition-before-extension verification.

**Structural-primitive usage**:

| Primitive | Count | Where |
|---|---|---|
| `delegates_to` | 1 | Unit F.001 (ASEAN charter authority-source) |
| `supersedes` | 2 | Unit E.003 (scope_elevation national→regional), Unit E.014 (scope_extension for generative AI) |
| `withdraws` | 0 | n/a |
| `recants` | 0 | n/a |

**Multilateral-participation envelope examples** (the Section E focal observation):

| Unit | dimension | kind |
|---|---|---|
| D.001 | `multilateral_participation:asean:knowledge_exchange` | cross-border knowledge sharing |
| D.011 | `multilateral_participation:asean:data_governance_harmonisation` | data-governance interoperability |
| E.001 | `multilateral_participation:asean:working_group_membership` | Working Group setup |
| E.002 | `multilateral_participation:asean:regional_tool_development` | WG responsibility 1 |
| E.003 | `multilateral_participation:asean:workforce_policy_coordination` | WG responsibility 2 |
| E.004 | `multilateral_participation:asean:ecosystem_investment_coordination` | WG responsibility 3 |
| E.005 | `multilateral_participation:asean:rnd_cross_pollination` | WG responsibility 4 |
| E.006 | `multilateral_participation:asean:governance_framework_evolution` | WG responsibility 5 |
| E.016 | `multilateral_participation:asean:practice_compendium` | regional compendium |
| F.001 | `multilateral_participation:asean:membership` | ASEAN foundational purpose anchor |

Ten distinct multilateral_participation:asean:{kind} envelopes across the section range — by far the highest density of this prefix family of any batch mapped to date. This validates the prompt's prediction that Section E exercises FSD-002 §3.9 most rigorously.

**`locality:decision:*` distribution**:

- `locality:decision:national` (1 envelope): Unit D.001
- `locality:decision:regional` (1 envelope): Unit E.001 + (implicit on all Section E multilateral_participation envelopes via composition)
- (Unit D.011 explicitly elevates from national to regional via the `locality:decision:regional` second envelope)

**T-3 candidates surfaced**:

| Unit | Candidate | Priority | Composition attempted? |
|---|---|---|---|
| E.001 | `partner_role:regional_intergovernmental_working_group_dual_remit` | MEDIUM | yes (two-attestation pattern works mechanically but loses the "ONE body holds BOTH" structural claim) |
| (D.011) | `cross_border_data_flow:harmonisation` as a positive-polarity complement to `detection:distributive:access:*` | MEDIUM | composition with multilateral_participation + locality:decision:regional successful; flagged as background T-3 candidate but NOT formally proposed because the composition works |

Only **one formally proposed T-3** (Unit E.001's dual-remit partner role). The second candidate (D.011 cross-border data flow) is noted but closed-by-composition. Composition-before-extension discipline maintained throughout per METHODOLOGY.md §8.5.2.

**Calibration paragraph**:

Section D + E + F together exercise the multilateral_participation + locality:decision + partner_role composition pattern more densely than any prior batch slice in the framework's mapping history. The Section E density of 10 distinct multilateral_participation:asean:{kind} envelopes across 16 units is a useful structural stress test: the prefix admits varied `{kind}` values without strain, and composition with `locality:decision:regional` works consistently. The single T-3 candidate that surfaced (E.001's dual-remit partner role) is moderate-priority and not load-bearing for v1.4 — composition with two separate partner_role attestations carries the operational shape; what's lost is the structural assertion that ONE body holds both remits simultaneously, which is honestly an FSD-002 §3.9 future-evolution consideration rather than a current blocker. The `supersedes` count of 2 is appropriate: the source genuinely names two scope-elevation events (Unit E.003 national→regional workforce; Unit E.014 base-Guide→generative-AI scope-extension). The `delegates_to` count of 1 (Unit F.001) honestly anchors the Guide's authority to ASEAN's foundational charter via the v1.3 §2.2.1 authority-source reuse pattern. No `recants` or `withdraws` — appropriate for a current-version document making forward-looking recommendations. Section F's voluntary-application + legal-non-supplant clauses (Unit F.002) are correctly mapped via `mutability: amendable` + `cohort_scope: affiliations` rather than via a new precedence-ordering primitive — composition-before-extension confirmed at this honest deferral surface. The overall ~84% clean+composed rate aligns with the manifest's expected verdict distribution (~85%+ clean+composed; minimal T-1 since the source is secular; some T-2 around scaffolding/legal-doctrine surfaces; minimal T-3). The single moderate-priority T-3 fits the predicted "minimal T-3 (the 7 principles + 4 components have strong existing prefix-family coverage)" framing — the gap is in regional-IGO partner-role granularity, not in the core principle/component structure.

---

**End CONTRIBUTION_OBJECTS_ASEAN_DEF_RECOMMENDATIONS_CONCLUSION.md**
