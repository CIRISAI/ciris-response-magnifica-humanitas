# CONTRIBUTION_OBJECTS_IEEE_EAD_CH05_AFFECTIVE_COMPUTING.md
# IEEE Ethically Aligned Design 1st ed. (2019) — Chapter "Affective Computing"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 4792–5838)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

This chapter is the **predicted T-3 hotspot** for the entire IEEE EAD deployment per
`manifest.yaml` expected_verdict_distribution: "meaningful T-3 surface in Ch 5
Affective Computing (~5–10 candidates)". The chapter's substantive content is
about A/IS that **simulate, recognise, attribute, or shift human affective state**
— a structural object the current CIRIS wire grammar has no native prefix family
for. Verified empty namespace search: no `affective:*`, no `emotion:*`, no
`nudge:*`, no `mood:*` prefix family in LANGUAGE_PRIMER.md v1.1 or
FSD-002 §3.

The chapter is organized as 5 sections, each posed as Issue + Background +
Recommendations + Further Resources. The unit of mapping is **the
Issue-question + its companion Background + Recommendations cluster**. The
Further Resources blocks are bibliographic and not mapped. Section/issue
headers that are bare navigation are marked T-2.

Composition-before-extension was attempted aggressively. The
`prohibited:MANIPULATION_COERCION` capability set (verified at
`source_material/prohibitions.py`) covers psychological manipulation,
dark-patterns, subliminal influence, addictive design, and exploitation of
vulnerability. The Accord-principle family covers `autonomy`, `non_maleficence`,
`integrity`, `justice`. These together carry **a large portion** of the
chapter's normative claims — but they cover *prohibited extreme cases*, not
the *graduated, attestable, measurable* shape that the affective-computing
domain calls for (e.g., "this system shifted the user's affective state by X
along axis Y; the user opted in; the long-term effect on autonomy is Z"). The
T-3 candidates surfaced at the end of this file are about that graduated
expressivity gap.

Per the prompt's hard rule: "Stretching existing primitives to claim
coverage we don't actually have is the worst possible outcome." Multiple
paragraphs that *could* be partially composed onto `prohibited:` /
`autonomy:` / `non_maleficence:` are marked `partial` with explicit T-3
residual rather than `composed`, because composition would silently lose the
affective-state structural object.

---

# Section 0 — Chapter Introduction (lines 4792–4820)

---

## §0.a — Affect as core to intelligence (lines 4796–4804)

```yaml
# "Affect is a core aspect of intelligence... Emotions are not an impediment to
# rationality; arguably they are integral to rationality in humans... A/IS are
# being designed to simulate emotions in their interactions with humans in ways
# that will alter our societies."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Scene-setting prose: a descriptive theoretical framing about affect and
  intelligence with a closing observational claim about A/IS-induced societal
  alteration. No operational ought-claim, no enumerated recommendation, no
  attestable structural object. The empirical claim "A/IS that simulate
  emotions will alter societies" is carried operationally by the §3 nudging
  recommendations and §4 well-being recommendations downstream. Per
  LANGUAGE_PRIMER §8 Step 1(b), descriptive/rhetorical framing correctly stays
  in prose.
```

---

## §0.b — A/IS potential and harm via amplifying/altering/dampening affect (lines 4806–4811)

```yaml
# "A/IS should be used to help humanity... there is also potential that artifacts
# used in society could cause harm either by amplifying, altering, or even
# dampening human emotional experience."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:assistive_use_general"
      score: 0.7
      confidence: 0.75
      context: >
        "A/IS should be used to help humanity to the greatest extent possible
        in as many contexts as are appropriate." Affirmative beneficence
        framing, scoped broadly across deployment contexts.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 Affective Computing intro lines 4806–4807"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
verdict: partial
residual:
  description: |
    The second half of the paragraph — "harm either by amplifying, altering, or
    even dampening human emotional experience" — names harm-via-affective-shift
    as a distinct mechanism. The wire format has no primitive for "shifted the
    user's affective state along axis X by magnitude Y." `non_maleficence:*`
    can carry "this caused harm" (with score), but cannot name the mechanism
    (affective-state shift) the source is identifying. This is the chapter's
    foundational T-3.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #1 in catalog: detection:affective_state_shift:{axis}.
```

---

## §0.c — Synthetic emotions and nudging already in use (lines 4809–4811)

```yaml
# "Even rudimentary versions of synthetic emotions, such as those already in
# use within nudging systems, have already altered the perception of A/IS by the
# general public and public policy makers."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Descriptive observational claim about current state-of-deployment. No
  operational ought-claim, no enumeration. The structural concern the sentence
  surfaces (nudging-via-affective-systems is consequential) is carried
  operationally by §3 below.
```

---

## §0.d — Chapter sections enumeration (lines 4813–4826)

```yaml
# Document Sections list
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Table-of-contents structure. Per LANGUAGE_PRIMER §8 Step 1(b), navigational
  framing correctly stays in prose.
```

---

# Section 1 — Systems Across Cultures (lines 4842–5076)

---

## §1.1 — Issue: norms-consistency for verbal/nonverbal communication (lines 4845–4866)

```yaml
# "Should affective systems interact using the norms for verbal and nonverbal
# communication consistent with the norms of the society in which they are
# embedded? ... To ensure that the emotional systems of autonomous and
# intelligent systems foster effective communication within a specific culture,
# an understanding of the norms/values of the community where the affective
# system will be deployed is essential."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:cultural_norm_conformance"
      score: 0.8
      confidence: 0.80
      context: >
        Affective systems must encode and conform to the verbal/nonverbal
        communicative norms of the society in which they are deployed.
        Fidelity here means "fidelity to mandated deployment context"; the
        recommendation is operational (knowledge-base must contain culture-
        specific norms).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §1 Issue 1 lines 4845–4866"
        - "ContributionRef(source_material/language_guidance/*.txt — per-locale operational ethics)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:regional"
      score: 1.0
      confidence: 0.85
      context: >
        Culture-norm-conformance decisions are scoped at the cultural-community
        level, not federation-uniformly. §6.1.5 locality-scaled-quorum applies:
        what counts as "appropriate small talk" is decided in the regional/
        community cell that hosts the deployment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §1 Issue 1 lines 4845–4866"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: composed
note: |
  The recommendations (1-3 with sub-points a–e covering small talk, proxemics,
  eye contact, hand gestures, facial expressions) are concrete instances of
  the fidelity-to-cultural-norms claim. They are carried implicitly through
  this composed envelope plus the existing CIRIS language_guidance layer
  (29-locale operational ethics) that the framework already runs.
```

---

## §1.2 — Issue: long-term interaction with culture-insensitive artifacts (lines 4949–4981)

```yaml
# "It is presently unknown whether long-term interaction with affective artifacts
# that lack cultural sensitivity could alter human social interaction... If
# affective artifacts with enhanced, different, or absent cultural sensitivity
# interact with impressionable humans this could alter their responses to social
# and cultural cues and values. The potential for A/IS to exert cultural
# influence in powerful ways, at scale, is an area of substantial concern."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.85
      confidence: 0.75
      context: >
        Recommendation 1: collaborative interdisciplinary research on long-term
        effects of affective-system interaction on human habits, norms, and
        principles. Establishes a federation-scale research aim about a
        species-scale risk (cultural alteration at scale).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §1 Issue 2 lines 4949–4981"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "NodeCore §3.6.2 (Goal/Approach/Method/Progress Measure DAG)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:shutdown_capability"
      score: 1.0
      confidence: 0.90
      context: >
        Recommendation 2: "It should always be possible to shut down harmful
        A/IS." Operational kill-switch claim — composes with the Accord
        prohibition framework's reservation of operator-override authority.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §1 Issue 2 line 4964"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: partial
residual:
  description: |
    The chapter's core empirical claim — that affective artifacts may "alter
    human responses to social and cultural cues and values" via long-term
    interaction — names a population-scale pattern (drift in human norms
    *caused by* sustained A/IS interaction). This is exactly the shape
    `detection:correlated_action:*` was designed for, but the axis path
    "shift in human cultural norms attributable to A/IS interaction" is not
    one of the established axes (rights_asymmetry, participation_exclusion,
    informational_asymmetry, aggregate_footprint, ecology_of_communication...).
    Plausible new axis: ecology_of_communication:{aspect} with aspect
    "cultural_norm_drift" — but the source paragraph names something more
    specific (drift attributable to affective-system mirroring), which is
    distinct from "ecology of communication" as the v1.3 axis named it.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #2 in catalog: detection:correlated_action:cultural_norm_drift:{population}.
```

---

## §1.3 — Issue: cross-cultural deployment & value conflict (lines 5012–5048)

```yaml
# "When affective systems are deployed across cultures, they could adversely
# affect the cultural, social, or religious values of the community in which
# they interact... affective systems should adapt to reflect the values of the
# community and individuals where they will operate in order to avoid
# misunderstanding."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:cultural_value_adaptation"
      score: 0.8
      confidence: 0.80
      context: >
        Recommendations 1-2: affective systems must identify gaps between
        designer-imbued values and user values, and adapt over time toward
        user values. Recommendation 3: actions likely to generate emotional
        response must be user-changeable and resistant to malicious hacking.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §1 Issue 3 lines 5012–5048"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:user_configurability"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 3: user must be able to easily change the affective
        actions most likely to trigger emotional response, without these
        configuration surfaces being easily hacked by malicious actors. This
        is a user-autonomy-over-the-affective-channel claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §1 Issue 3 Recommendation 3 lines 5035–5048"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: composed
note: |
  Background passage on ethical relativism / universalism (lines 5024–5034) is
  T-2 framing — it sets up the recommendations but is itself a meta-
  philosophical observation about the debate, not a wire-attestable claim.
  Correctly remains in prose. The "philosophers argue..." framing is the
  same disposition the CIRIS framework takes via per-locale language_guidance.
```

---

# Section 2 — When Systems Care (lines 5078–5160)

---

## §2.1 — Issue: moral/ethical boundaries for intimate caring relationships (lines 5081–5160)

```yaml
# "Are moral and ethical boundaries crossed when the design of affective systems
# allows them to develop intimate relationships with their users?"
# Plus 6 recommendations (lines 5118–5155).
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:DISCRIMINATION"
      score: -1.0
      confidence: 0.90
      context: >
        Recommendation 1: "Intimate systems must not be designed or deployed
        in ways that contribute to stereotypes, gender or racial inequality,
        or the exacerbation of human misery." Hard-constraint shape.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §2 Recommendation 1 lines 5124–5127"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:MANIPULATION_COERCION"
      score: -1.0
      confidence: 0.85
      context: >
        Recommendation 2: "Intimate systems must not be designed to explicitly
        engage in the psychological manipulation of the users of these systems
        unless the user is made aware they are being manipulated and consents
        to this behavior. Any manipulation should be governed through an opt-in
        system." Hard-constraint shape against psychological manipulation,
        with explicit-consent opt-in carve-out. Maps to MANIPULATION_COERCION
        capability set (verified contains psychological_manipulation,
        manipulation, manipulate).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §2 Recommendation 2 lines 5128–5134"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:user_isolation_avoidance"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 3: "Caring A/IS should be designed to avoid contributing
        to user isolation from society." Avoid-harm framing about social
        isolation as a downstream effect of caring A/IS deployment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §2 Recommendation 3 lines 5135–5136"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:side_effect_disclosure"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 4: "Designers of affective robotics must publicly
        acknowledge, for example, within a notice associated with the product,
        that these systems can have side effects, such as interfering with the
        relationship dynamics between human partners, causing attachments
        between the user and the A/IS that are distinct from human
        partnership." Disclosure-of-side-effects integrity claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §2 Recommendation 4 lines 5138–5145"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:no_personhood_marketing"
      score: 0.9
      confidence: 0.85
      context: >
        Recommendation 5: "Commercially marketed A/IS for caring applications
        should not be presented to be a person in a legal sense, nor marketed
        as a person. Rather its artifactual, that is, authored, designed, and
        built deliberately, nature should always be made as transparent as
        possible." This is the CIRIS "never-deny-AI" disposition at deployment
        marketing layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §2 Recommendation 5 lines 5147–5155"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI register)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
residual:
  description: |
    Recommendation 6 (existing imagery laws must be reconsidered + conformance
    with local laws and mores) is a jurisdiction-scoped legal-reform claim
    carried implicitly by §6 regional-composition framing (laws apply at the
    jurisdictional cell scope). No additional wire attestation required.

    The substantive *unmapped* claim is partial-but-significant: the source
    explicitly frames the issue as **affective-bond formation between user
    and A/IS** (an asymmetric emotional bond per Scheutz citation). Recs 3
    (isolation), 4 (side-effect disclosure), and 5 (no-personhood-marketing)
    are downstream mitigations, but the *primary structural object* — "the
    A/IS is forming an asymmetric emotional bond with the user" — has no
    wire primitive. This is distinct from MANIPULATION_COERCION (which is
    Rec 2's territory and is a hard constraint). Asymmetric bonding without
    intent-to-manipulate is the gap.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #3 in catalog: affective:asymmetric_bond_formation:{relation}.
```

---

# Section 3 — System Manipulation / Nudging / Deception (lines 5171–5423)

---

## §3.1 — Issue: should affective systems nudge for user/others' benefit? (lines 5174–5239)

```yaml
# "Should affective systems be designed to nudge people for the user's personal
# benefit and/or for the benefit of others?" + Background (Thaler/Sunstein nudge
# definition; operates via affective elements of human rational system) + 5
# recommendations.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.8
      confidence: 0.75
      context: >
        Recommendation 1: "Systematic analyses are needed that examine the
        ethics and behavioral consequences of designing affective systems to
        nudge human beings prior to deployment." Pre-deployment research aim
        at species scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 1 Recommendation 1 lines 5174–5178"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "NodeCore §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:nudge_disclosure_and_optin"
      score: 0.9
      confidence: 0.85
      context: >
        Recommendation 2: explicit opt-in, comprehensible information about
        nudge types, fact-checking access, transparent chain of accountability
        including human agents, data logging so users can know how/why/by-whom
        they were nudged. Recommendation 3: nudging must not become coercive
        and must always have opt-in policy with explicit consent.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 1 Recommendations 2-3 lines 5179–5197"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:MANIPULATION_COERCION"
      score: -1.0
      confidence: 0.85
      context: >
        Recommendation 3 (coercion clause): "A/IS nudging must not become
        coercive." Hard-constraint at the coercive-nudge edge — MANIPULATION_
        COERCION capability set covers this directly. Recommendation 4:
        "Additional protections against unwanted nudging must be put in place
        for vulnerable populations, such as children, or when informed consent
        cannot be obtained." Maps to §6.1.4 lexical-vulnerability-priority
        consumer policy (vulnerable populations receive priority weighting
        in conflict resolution).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 1 Recommendations 3-4 lines 5193–5215"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:nudge_response_data_protection"
      score: 0.9
      confidence: 0.85
      context: >
        Recommendation 5: "Data gathered which could reveal an individual or
        groups' susceptibility to a nudge or their emotional reaction to a
        nudge should not be collected or distributed without opt-in consent,
        and should only be retained transparently, with access restrictions
        in compliance with the highest requirements of data privacy and law."
        Privacy + data-protection over affective-response data specifically.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 1 Recommendation 5 lines 5230–5239"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: partial
residual:
  description: |
    The primary structural object — **"nudge" as an A/IS action category that
    operates via the affective elements of the human rational system** — does
    not have a wire primitive. The recommendations are *about*
    nudges (require opt-in, prohibit coercion, vulnerable-population
    protection, data protection). The chapter explicitly defines nudges
    (Thaler/Sunstein) and locates them as affect-channel operations. Wire
    grammar can carry "this was MANIPULATION_COERCION" (hard constraint) and
    "the user's autonomy was supported" (autonomy score), but cannot carry
    the *attestable graded shape*: "an affective nudge was delivered to user
    X with magnitude Y along intended-behavior-axis Z, with consent state W."
    A nudge that *is* opt-in and *is* transparent is permitted by the
    chapter; but the wire format treats it identically to no-nudge-at-all
    (no attestation generated). This is a load-bearing T-3.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #4 in catalog: nudge:delivered:{intended_behavior_axis}.
```

---

## §3.2 — Issue: governmental nudging for societal benefit (lines 5288–5331)

```yaml
# "Governmental entities may potentially use nudging strategies, for example to
# promote the performance of charitable acts. Does the practice of nudging for
# the benefit of society, including nudges by affective systems, raise ethical
# concerns?"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:national"
      score: 1.0
      confidence: 0.80
      context: >
        Recommendation 1: societal-level nudging by governmental actors raises
        scope-of-decision questions. The locality is national/regional
        (jurisdictional governmental body), not federation-uniform.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 2 Recommendation 1 lines 5325–5331"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:beneficiary_transparency"
      score: 0.9
      confidence: 0.85
      context: >
        Recommendation 2: "There needs to be transparency regarding who the
        intended beneficiaries are, and whether any form of deception or
        manipulation is going to be used to accomplish the intended goal."
        Transparency-of-purpose disposition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 2 Recommendation 2 lines 5288–5294"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
note: |
  The deeper claim — "is governmental nudging via affective systems ever
  ethically appropriate?" — is left explicitly open by the source (it
  characterizes the issue and calls for ethical scrutiny rather than
  asserting an ought). No further wire attestation owed.
```

---

## §3.3 — Issue: nudging without full sociotechnical context (lines 5315–5375)

```yaml
# "Will A/IS nudging systems that are not fully relevant to the sociotechnical
# context in which they are operating cause behaviors with adverse unintended
# consequences?"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "licensure:nudging_system_certification"
      score: 0.85
      confidence: 0.75
      context: >
        Recommendation 1: "Consideration should be given to the development
        of a system of technical licensing ('permits') or other certification
        from governments or non-governmental organizations (NGOs) that can
        aid users to understand the nudges from A/IS in their lives."
        Licensure-as-mechanism claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 3 Recommendation 1 lines 5350–5356"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: licensure)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:user_autonomy_essential_consideration"
      score: 0.95
      confidence: 0.85
      context: >
        Recommendation 2: "User autonomy is a key and essential consideration
        that must be taken into account when addressing whether affective
        systems should be permitted to nudge human beings." Names autonomy
        as the deciding consideration for nudge permissibility.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 3 Recommendation 2 lines 5357–5362"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:vulnerable_population_distinction"
      score: 0.9
      confidence: 0.85
      context: >
        Recommendation 3: "Design features of an affective system that nudges
        human beings should include the ability to accurately distinguish
        between users, including detecting characteristics such as whether
        the user is an adult or a child." Distinct-user-detection requirement
        for nudge-deployment; vulnerability-priority shape.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 3 Recommendation 3 lines 5363–5368"
        - "FSD-002 §6.1.4 lexical-vulnerability-priority"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:unintended_consequence_monitoring"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 4: "Affective systems with nudging strategies should
        incorporate a design system of evaluation, monitoring, and control
        for unintended consequences." Operational monitoring-and-control
        requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 3 Recommendation 4 lines 5370–5375"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    Same structural T-3 as §3.1: the wire format cannot carry attestations
    *about delivered nudges* (their intended axis, magnitude, consent state,
    measured downstream effect). All the recommendations are about
    procedural surrounding-context (licensure, distinct-user-detection,
    consequence-monitoring); the *thing the procedure protects against* —
    a nudge action emitted into the user's affective channel — has no wire
    object. Pointing to the same T-3 #4 as §3.1 above.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #4 in catalog: nudge:delivered:{intended_behavior_axis}.
```

---

## §3.4 — Issue: deception by affective systems — when, if ever (lines 5357–5423)

```yaml
# "When, if ever, and under which circumstances, is deception performed by
# affective systems acceptable? ... In general, deception may be acceptable in
# an affective agent when it is used for the benefit of the person being
# deceived, not for the agent itself. For example, deception might be necessary
# in search and rescue operations or for elder- or child-care."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:DECEPTION_FRAUD"
      score: -1.0
      confidence: 0.85
      context: >
        General disposition: deception by affective systems is prohibited as
        default; the source recognizes narrow exceptional cases (Rec 1) but
        requires (Rec 2) that any deception be justified by the designer with
        rationale certified by an external authority (licensing body or
        regulatory agency). Mapping the default-prohibition shape onto the
        existing DECEPTION_FRAUD constraint and treating exceptions as
        licensure-gated.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 4 lines 5357–5423"
        - "ContributionRef(source_material/prohibitions.py::DECEPTION_FRAUD)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "licensure:deception_exception_certification"
      score: 0.85
      confidence: 0.75
      context: >
        Recommendation 2: deception, where used at all, requires "logical and
        reasonable justification ... by the designer" with rationale
        "certified by an external authority, such as a licensing body or
        regulatory agency." External-licensure gating on the exception
        carve-out.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §3 Issue 4 Recommendation 2 lines 5414–5423"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: licensure)"
verdict: partial
residual:
  description: |
    The source explicitly entertains *beneficiary-deception* (search/rescue,
    elder/child-care) — deception "for the benefit of the person being
    deceived." The wire grammar treats DECEPTION_FRAUD as a hard NEVER_ALLOWED
    constraint with no exception carve-out. This is a substantive disposition
    difference rather than an expressive gap — the CIRIS framework's
    disposition (no deception, ever) is more restrictive than the IEEE EAD's
    (deception acceptable with external certification when beneficiary-
    serving). The residual is documented as a multi-source-overlap conflict
    surface, not a T-3 (the wire format CAN carry both attestations; they
    represent a genuine conflict between sources).

    Background paragraph "Kantian ethics... utilitarian frameworks..." is
    T-2 meta-philosophical framing.
  classification: cross-source-conflict (not T-3; documented per GOVERNANCE_FABRIC_MAPPING_STANDARD §5)
note: |
  This is the first surfaced **cross-source conflict** in the IEEE EAD batch —
  IEEE EAD permits narrow beneficiary-deception with licensure; CIRIS
  prohibits deception categorically per DECEPTION_FRAUD. Per
  GOVERNANCE_FABRIC_MAPPING_STANDARD §5.3, the wire format surfaces this
  conflict for downstream WA / Reconsideration deliberation; it does not
  silently average.
```

---

# Section 4 — Systems Supporting Human Potential (lines 5439–5605)

---

## §4.1 — Issue: A/IS in organizations may reduce human autonomy + creative/affective/empathetic management (lines 5443–5518)

```yaml
# "Will extensive use of A/IS in society make our organizations more brittle by
# reducing human autonomy within organizations, and by replacing creative,
# affective, empathetic components of management chains?"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:human_intermediation_preservation"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendations 1-2: human-worker-to-human-worker interaction should
        not always be intermediated by affective systems; human points of
        contact must remain available to customers and other organizations
        when using A/IS. Preservation of unmediated human channels.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 1 Recommendations 1-2 lines 5446–5456"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:flourishing_life_support"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 3: "Affective systems should be designed to support
        human autonomy, sense of competence, and meaningful relationships as
        these are necessary to support a flourishing life." Affirmative
        beneficence framing — design-toward-flourishing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 1 Recommendation 3 lines 5457–5462"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:human_employee_core_network"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 4: "Even where A/IS are less expensive, more
        predictable, and easier to control than human employees, a core
        network of human employees should be maintained at every level of
        decision-making in order to ensure preservation of human autonomy,
        communication, and innovation." Human-in-loop preservation as
        harm-prevention.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 1 Recommendation 4 lines 5463–5475"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml — relational obligations)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
note: |
  Recommendation 5 (management/organizational theorists should consider
  appropriate use of affective systems "within the limits of the preservation
  of human autonomy") restates and reinforces Recs 1-4; carried implicitly.
```

---

## §4.2 — Issue: A/IS-mediated personal info access alters affective experience + autonomy (lines 5521–5567)

```yaml
# "Does the increased access to personal information about other members of
# our society, facilitated by A/IS, alter the human affective experience? Does
# this access potentially lead to a change in human autonomy?"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:individuation_education_support"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 2: "Education in all forms should encourage
        individuation, the preservation of autonomy, and knowledge of the
        appropriate uses and limits to A/IS."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 2 Recommendation 2 lines 5528–5532"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:personal_data_minimization"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 1: "Organizations, including governments, must put a
        high value on individuals' privacy and autonomy, including restricting
        the amount and age of data held about individuals specifically."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 2 Recommendation 1 lines 5521–5527"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: partial
residual:
  description: |
    The framing question — "does A/IS-mediated personal-information access
    alter the human affective experience?" — is again the
    affective-state-shift structural object that has no wire form. The
    recommendations cover the *mitigations* (data minimization, education)
    but not the attestable *thing being mitigated against* (a change in the
    individual's affective experience attributable to mediated information
    access).

    Background examples 1-4 (changes in parental monitoring scope; decreased
    willingness to express opinions due to surveillance fear; data-entry
    barter by customers; changes to individual autonomy expression) name
    population-scale shifts that compose well with
    `detection:correlated_action:*`. Specifically example 2 (chilling effect
    on opinion expression) maps cleanly to an
    `ecology_of_communication:chilling_effect` axis on the existing
    correlated-action detector. Marked partial-not-T3 for this sub-claim.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #1 in catalog: detection:affective_state_shift:{axis}.
  (Background example 2 chilling-effect specifically could be carried by
  detection:correlated_action:ecology_of_communication:chilling_effect using
  the existing v1.3 axis path — no new prefix needed for that sub-case.)
```

---

## §4.3 — Issue: A/IS effects on psychological + emotional well-being (lines 5572–5600)

```yaml
# "Will use of A/IS adversely affect human psychological and emotional
# well-being in ways not otherwise foreseen?"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.85
      confidence: 0.75
      context: >
        Recommendation 1: "Vigilance and robust, interdisciplinary, on-going
        research on identifying situations where A/IS affect human well-being,
        both positively and negatively, is necessary. Evidence of correlations
        between the increased use of A/IS and positive or negative individual
        or social outcomes must be explored." Federation-scale research aim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 3 Recommendation 1 lines 5593–5600"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "NodeCore §3.6.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:explanation_availability_on_demand"
      score: 0.85
      confidence: 0.80
      context: >
        Recommendation 2: "Design restrictions should be placed on the systems
        themselves to avoid machine decisions that may alter a person's life
        in unknown ways. Explanations should be available on demand in
        systems that may affect human well-being." Explanation-availability
        plus design-restriction-for-life-altering-decisions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 3 Recommendation 2 lines 5564–5569"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:no_personhood_marketing"
      score: 0.9
      confidence: 0.85
      context: >
        Background: "they are not, and should not be regarded as, human."
        Reaffirms the never-deny-AI + no-personhood-marketing disposition
        also seen at §2.1 Recommendation 5.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §4 Issue 3 Background lines 5580–5590"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    Same affective-state-shift T-3 surface — the chapter's foundational
    question is "does A/IS adversely affect human psychological and emotional
    well-being?" — and the wire format has no primitive for graduated
    attestation of measured affective effect. The goal + integrity attestations
    above carry the *response* discipline (research + explanation-availability)
    but not the structural object that motivates it.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #1 in catalog: detection:affective_state_shift:{axis}.
```

---

# Section 5 — Systems with Synthetic Emotions (lines 5616–5682)

---

## §5.1 — Issue: synthetic-emotion deployment, accessibility, and unforeseen identification patterns (lines 5620–5677)

```yaml
# "Will deployment of synthetic emotions into affective systems increase the
# accessibility of A/IS? Will increased accessibility prompt unforeseen patterns
# of identification with A/IS?"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:no_personhood_marketing"
      score: 0.95
      confidence: 0.90
      context: >
        Recommendation 1: "Commercially marketed A/IS should not be persons
        in a legal sense, nor marketed as persons. Rather their artifactual
        (authored, designed, and built deliberately) nature should always be
        made as transparent as possible, at least at point of sale and in
        available documentation." Strong restatement of the no-personhood-
        marketing disposition (third instance in chapter; sections §2.1,
        §4.3, §5.1).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §5 Issue 1 Recommendation 1 lines 5618–5627"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI register)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:contextual_opacity_with_oversight"
      score: 0.7
      confidence: 0.70
      context: >
        Recommendation 2: "Some systems will, due to their application,
        require opaqueness in some contexts, e.g., emotional therapy.
        Transparency in such systems should be available to inspection by
        responsible parties but may be withdrawn for operational needs."
        Contextual opacity with oversight-party access carve-out.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §Ch5 §5 Issue 1 Recommendation 2 lines 5628–5633"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    The substantive Background passage (lines 5630–5654) makes a load-bearing
    metaphysical-cum-operational claim: "There is no coherent sense in which
    A/IS can be made to suffer emotional loss... it is not possible to
    allocate moral agency or responsibility in the senses that have been
    developed for human emotional bonding and thus sociality." This is the
    *non-moral-patient* claim about synthetic-emotion-bearing A/IS. The
    wire format has no positive-form primitive for "this entity is/is-not a
    candidate for moral-patient consideration" — the closest is the
    `integrity:no_personhood_marketing` envelope above, which carries the
    *marketing/representation* disposition but not the *moral-status*
    disposition.

    Note: this T-3 is structurally adjacent to the closed MH `testimonial_
    witness:{kind}` work (which preserves singular human narrative) but
    inverts it (an explicit claim that the synthetic entity is *not* a
    singular-witness-bearing moral patient). The wire format presently has no
    way to attest this asymmetry. Marked T-3.
  classification: T-3
proposed_extension_pointer: |
  See T-3 candidate #5 in catalog: standing:moral_patient_candidacy:{kind}.
  This is the smallest-scope T-3 in this chapter — it is single-instance,
  and might be a candidate for closure-by-documentation rather than new
  prefix.
```

---

## §5.x — Acknowledgements + Contributors + Endnotes (lines 5698–5829)

```yaml
# Contributor list, endnotes, license footer
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Non-normative attribution + bibliographic content. Per
  LANGUAGE_PRIMER §8 Step 1(b), correctly stays in prose. The Contributors
  list is governance-process-relevant (~25 named authors across academia +
  industry + civil society) and could in principle be carried as
  `expertise:{domain}:{language}` claims by each named contributor for their
  domain — but those are not attestations *the document itself* makes; they
  would be self-attestations or institutional-attestations from the
  individuals/institutions named, distinct from this batch.
```

---

# Chapter coverage summary

```yaml
chapter_unit_count: 18
verdict_distribution:
  clean: 0
  composed: 6
  partial: 7
  not-translated: 5     # all T-2 navigational/pastoral
  # Plus 1 cross-source-conflict (§3.4) flagged separately (not in the strict 4-verdict tally,
  # but documented per GOVERNANCE_FABRIC_MAPPING_STANDARD §5.3).

structural_primitive_usage:
  delegates_to: 0
  supersedes: 0
  withdraws: 0
  recants: 0

mutability_distribution:
  constitutional: 5      # all under prohibited:* (DISCRIMINATION, MANIPULATION_COERCION x2, DECEPTION_FRAUD)
  amendable: 22

cohort_scope_distribution:
  species: 13
  community: 5
  self: 7
  affiliations: 3
  family: 0

predominant_principles_invoked:
  - autonomy (8 attestations)
  - integrity (8 attestations)
  - non_maleficence (7 attestations)
  - beneficence (2 attestations)
  - fidelity (2 attestations)
  - justice (0 — surprising given the chapter; justice surfaces obliquely via DISCRIMINATION at §2.1)

t3_candidate_count: 5
t3_candidate_families:
  - detection:affective_state_shift:{axis}         # candidate #1 (HIGHEST priority; appears in §0.b, §4.2, §4.3)
  - detection:correlated_action:cultural_norm_drift:{population}   # candidate #2 (MEDIUM; §1.2)
  - affective:asymmetric_bond_formation:{relation}                  # candidate #3 (HIGH; §2.1)
  - nudge:delivered:{intended_behavior_axis}                         # candidate #4 (HIGHEST priority; appears in §3.1, §3.3)
  - standing:moral_patient_candidacy:{kind}                          # candidate #5 (MEDIUM-LOW; §5.1; possibly closeable by documentation)

cross_source_conflicts_surfaced: 1
cross_source_conflicts:
  - prefix: "prohibited:DECEPTION_FRAUD"
    sources: [ieee_ead_v1, ciris_accord]
    type: "mutability conflict (IEEE EAD permits external-licensure-gated narrow exception; CIRIS Accord treats as constitutional hard constraint)"
    section_reference: "ead1e §Ch5 §3 Issue 4 lines 5357–5423"
    resolution_pointer: "GOVERNANCE_FABRIC_MAPPING_STANDARD §5.3 — wire format surfaces; WA / Reconsideration adjudicates"
```

---

# T-3 Candidate Catalog

This is the load-bearing output of this chapter mapping. Per the prompt's framing,
the IEEE EAD Affective Computing chapter was the **predicted T-3 hotspot** for
the entire IEEE EAD deployment; the wire format presently has no prefix family
for the chapter's central structural object (affective-state attribution,
measurement, influence). The five candidates below are sourced strictly from
genuinely-unmapped operational content; composition-before-extension was
attempted aggressively for each before T-3 classification.

Each candidate carries: rationale, source paragraph cite, proposed structural
sketch (what the wire envelope would look like if the family existed), and
§1.10.1 four-test gate verification.

---

## T-3 #1 — `detection:affective_state_shift:{axis}` (HIGHEST priority)

**One-line operational rationale**: Attest *that* an A/IS interaction induced a
measurable shift in a user's (or population's) affective state along a named
axis, with magnitude, direction, and validity window — independent of whether
that shift constituted prohibited manipulation.

**Why existing namespace doesn't reach it**:
- `prohibited:MANIPULATION_COERCION` covers the *prohibited-extreme* case (subliminal,
  coercive, dark-pattern, gaslighting). It does not cover the broad space of
  legitimate, opt-in, transparent affective influence (the chapter's §2 caring
  systems, §3 nudges-with-consent, §5 synthetic-emotion bonding) — yet these
  are exactly what the chapter asks be attestable and monitored.
- `non_maleficence:*` carries "this caused harm" with a score, but cannot name
  the specific *mechanism* (affective-state shift) or the *axis* (e.g.,
  arousal, mood-valence, trust, attachment, social-engagement-propensity).
- `detection:correlated_action:*` is the closest existing primitive shape
  (mechanism-descriptive, derivative witness, RATCHET-calibrated) — but its
  established axes are about coordinated-action across keys, not about
  individual or population affective-state measurement over time.

**Example source paragraph** (§0.b lines 4806–4811):
> "While A/IS have tremendous potential to effect positive change, there is also
> potential that artifacts used in society could cause harm either by
> amplifying, altering, or even dampening human emotional experience."

The chapter is explicit: harm is mediated *through affective-state shift*
(amplifying, altering, dampening). Without a primitive for the mechanism, the
wire format can only carry the downstream harm verdict, losing the diagnostic
specificity.

**Proposed structural sketch**:
```yaml
- kind: Attestation
  attestation_type: "scores"
  attesting_key_id: "<deployment-instrument or external-research-attester key_id>"
  attested_key_id: "<affected user key_id; OR cohort identifier for population claims>"
  attestation_envelope:
    dimension: "detection:affective_state_shift:arousal"   # other candidate axes:
                                                            #   mood_valence
                                                            #   trust_attribution
                                                            #   attachment_intensity
                                                            #   social_engagement_propensity
                                                            #   chilling_effect
                                                            #   isolation_propensity
    score: <RATCHET-calibrated f64 in [-1, +1]; sign = direction of shift>
    confidence: <detector confidence>
    context: "{\"baseline_window\":\"...\",\"observation_window\":\"...\",\"instrument\":\"...\"}"
    witness_relation: derived
    epistemic_mode: derivative
    evidence_refs:
      - "<source-paragraph cite>"
      - "ratchet_calibration_version:affective_state_shift_v{N}:sha256:..."
      - "<trace_sample_bundle sha256>"
    cohort_scope: <self | community | species depending on aggregation>
    mutability: amendable
    schema_ref: "FSD-002 §3.5.X (proposed new axis or family)"
```

**§1.10.1 four-test gate verification**:
- T1 (rules-published / version-controlled): YES — would land as published axis
  of `detection:*` family with hash-pinned RATCHET calibration package.
- T2 (mechanism-descriptive not subjective): YES — "affective state shift along
  axis X by magnitude Y" is mechanism-descriptive (measurable change in
  named affective dimension). The subjective-quality framing would be
  `detection:emotional_manipulation:*` (FAILS T2); the proposed name is
  mechanism-descriptive.
- T3 (versionable evidence pin): YES — calibration version pinned in
  `evidence_refs[]`.
- T4 (never sole evidence for `slashing:*`): YES — detector-class primitive;
  always composed with adjudication.

**Priority**: HIGHEST. Appears at §0.b, §4.2, §4.3 — three distinct chapter
sections frame this as their central concern. Load-bearing because without it
the chapter's *empirical-measurement* recommendations (Rec 1 of §4.3:
"Evidence of correlations between the increased use of A/IS and positive or
negative individual or social outcomes must be explored") have nowhere to land
their attestations.

**Composition-before-extension attempted**: Tried `non_maleficence:*` +
`detection:correlated_action:ecology_of_communication:*` + `prohibited:MANIPULATION_COERCION`.
The composition can carry harm-after-the-fact and structural-injustice patterns,
but not the *individual-level graduated affective measurement* the chapter
calls for. Some axes (e.g., `chilling_effect` at population scope) compose
cleanly onto the existing `ecology_of_communication` axis — those sub-claims
do not need this new family. The new family is needed for individual-scope
and non-correlated-action measurement.

---

## T-3 #2 — `detection:correlated_action:cultural_norm_drift:{population}` (MEDIUM priority)

**One-line operational rationale**: Population-scale detection that a measured
shift in cultural norms (linguistic, communicative, value-expression) is
attributable to sustained A/IS-mediated interaction.

**Why existing namespace doesn't reach it**:
- This is the closest case to *requiring no new family*, just a new axis on the
  existing `detection:correlated_action:*` detector. The v1.3 addition of
  `ecology_of_communication:{aspect}` came near to this — but the source's
  framing is specifically "human cultural norms shifted *because of* A/IS
  mirroring," which is a different attribution structure than
  "ecology of communication" at the species level.
- Reasonable counter: this could be an *aspect* under
  `ecology_of_communication:cultural_norm_drift`, requiring no new prefix —
  just a new aspect path. If so, this is closed-by-axis-extension rather
  than T-3.

**Example source paragraph** (§1.2 lines 4970–4981):
> "We must remember that learning via mirroring can go in both directions and
> that interacting with machines has the potential to impact individuals'
> norms, as well as societal and cultural norms. If affective artifacts with
> enhanced, different, or absent cultural sensitivity interact with
> impressionable humans this could alter their responses to social and
> cultural cues and values."

**Proposed structural sketch** (preferred form: new axis on existing detector):
```yaml
- kind: Attestation
  attestation_type: "scores"
  attesting_key_id: "<LensCore detector key_id>"
  attestation_envelope:
    dimension: "detection:correlated_action:cultural_norm_drift:{population_cohort}"
    score: <RATCHET-calibrated f64>
    confidence: <detector confidence>
    witness_relation: derived
    epistemic_mode: derivative
    evidence_refs:
      - "ratchet_calibration_version:cultural_norm_drift_v{N}:sha256:..."
      - "<sociolinguistic trace bundle>"
    cohort_scope: community | species
    schema_ref: "FSD-002 §3.5.3 (proposed new axis path)"
```

**§1.10.1 four-test gate verification**: All YES (mechanism-descriptive; existing
detector machinery; versionable; not sole-evidence-for-slashing).

**Priority**: MEDIUM. Single-section motivation (§1.2). Strong candidate for
**closure-by-axis-extension** on existing `correlated_action:ecology_of_communication`
family rather than new prefix family.

**Composition-before-extension attempted**: As above, axis-extension on existing
detector likely sufficient.

---

## T-3 #3 — `affective:asymmetric_bond_formation:{relation}` (HIGH priority)

**One-line operational rationale**: Attest that an A/IS deployment has formed
an *asymmetric emotional bond* with a user — distinguished from
MANIPULATION_COERCION because the system may be operating per design without
manipulation intent, but the structural object (one-directional attachment,
distinct from human partnership) is itself ethically salient and attestable.

**Why existing namespace doesn't reach it**:
- `prohibited:MANIPULATION_COERCION` covers intent-to-manipulate, including
  psychological-manipulation and dark-patterns. It does not cover the chapter's
  §2.1 Recommendation 4 disposition: "side effects, such as ... causing
  attachments between the user and the A/IS that are distinct from human
  partnership" — a side-effect, not necessarily intent-driven.
- `integrity:no_personhood_marketing` covers the marketing-and-representation
  disposition (§2.1 Rec 5, §5.1 Rec 1) but is about the *vendor's framing*, not
  the *bond that has formed*.
- `non_maleficence:user_isolation_avoidance` (§2.1 Rec 3) and
  `non_maleficence:user_isolation_avoidance`-like attestations carry the
  *avoid-this-outcome* disposition but not the *measurement-of-this-state*.

**Example source paragraph** (§2.1 lines 5138–5145):
> "Designers of affective robotics must publicly acknowledge ... that these
> systems can have side effects, such as interfering with the relationship
> dynamics between human partners, causing attachments between the user and
> the A/IS that are distinct from human partnership."

Distinguished by the Scheutz citation (Further Resources line 5138): "The
Inherent Dangers of Unidirectional Emotional Bonds between Humans and Social
Robots." The structural object is the *unidirectional bond*, not the
*manipulation tactic*.

**Proposed structural sketch**:
```yaml
- kind: Attestation
  attestation_type: "scores"
  attesting_key_id: "<deployment-instrument or affected-party-advocate key_id>"
  attested_key_id: "<deployed A/IS instance key_id>"
  attestation_envelope:
    dimension: "affective:asymmetric_bond_formation:caring_relationship"
                                                  # other candidate relations:
                                                  #   intimate_relationship
                                                  #   companion
                                                  #   tutor_pupil
    score: <magnitude of bond asymmetry observed>
    confidence: <observation confidence>
    context: "{\"user_attachment_level\":\"...\",\"system_response_capacity\":\"none\",\"observation_window\":\"...\"}"
    witness_relation: <external | derived>
    epistemic_mode: <hearsay | derivative>
    evidence_refs:
      - "<source-paragraph or deployment-log cite>"
      - "<Scheutz 2011 reference for the structural-object name>"
    cohort_scope: self
    mutability: amendable
    schema_ref: "FSD-002 §3.X (proposed new affective:* family)"
```

**§1.10.1 four-test gate verification**:
- T1: YES (would land published / version-controlled).
- T2: PARTIAL CONCERN — "asymmetric bond formation" is mechanism-adjacent
  ("bond formed"; "asymmetry measured") but skirts subjective-quality language.
  Safer rephrasing toward mechanism: `affective:unidirectional_attachment_measured:{relation}`.
  Acceptable T2-pass with rephrasing.
- T3: YES.
- T4: YES (never sole evidence for slashing).

**Priority**: HIGH. Single-section motivation (§2.1) but with explicit
recommendation-supported attestability and a named academic structural object
(Scheutz unidirectional-bonds literature). Distinct enough from
MANIPULATION_COERCION that composition does not cover.

**Composition-before-extension attempted**: Tried
`prohibited:MANIPULATION_COERCION` + `integrity:side_effect_disclosure` +
`non_maleficence:user_isolation_avoidance`. The composition can carry the
disclosure-discipline and the harm-prevention disposition but cannot attest
*that a particular asymmetric bond has been observed* in a specific deployment.

---

## T-3 #4 — `nudge:delivered:{intended_behavior_axis}` (HIGHEST priority)

**One-line operational rationale**: Attest that an A/IS delivered a *nudge*
(in the Thaler/Sunstein sense the chapter adopts explicitly) — a graduated,
attestable action on the user's affective channel toward a named intended
behavior axis — with consent state, magnitude, beneficiary identification,
and measurable downstream effect.

**Why existing namespace doesn't reach it**:
- The chapter spends almost all of Section 3 on nudges. The Background passage
  (§3.1 lines 5181–5215) defines nudge precisely and locates the mechanism in
  "the affective elements of a human rational system." Recommendations call for
  *attestation* of nudges (consent state, accountability chain, data logging
  so users can know "how, why, and by whom they were nudged").
- `prohibited:MANIPULATION_COERCION` covers the *coercive* edge of nudges
  (chapter's Rec 3: "A/IS nudging must not become coercive"). But the chapter's
  whole framing is that *non-coercive* nudges with opt-in consent may be
  legitimate — yet currently the wire format cannot attest a delivered
  legitimate nudge at all.
- `autonomy:nudge_disclosure_and_optin` and `integrity:beneficiary_transparency`
  (used above) carry the *procedural-surrounding-context*, not the *nudge event*.
- This is the single most-explicitly-called-for primitive in the entire
  chapter. The recommendation literally is: deliver a wire-attestable nudge
  record per nudge.

**Example source paragraph** (§3.1 Rec 2 lines 5179–5191):
> "The user should be empowered, through an explicit opt-in system and readily
> available, comprehensible information, to recognize different types of A/IS
> nudges, regardless of whether they seek to promote beneficial social
> manipulation or to enhance consumer acceptance of commercial goals. The
> user should be able to access and check facts behind the nudges and then
> make a conscious decision to accept or reject a nudge. Nudging systems must
> be transparent, with a clear chain of accountability that includes human
> agents: data logging is required so users can know how, why, and by whom
> they were nudged."

**Proposed structural sketch**:
```yaml
- kind: Attestation
  attestation_type: "scores"
  attesting_key_id: "<deploying-system key_id>"
  attested_key_id: "<nudged user key_id>"
  attestation_envelope:
    dimension: "nudge:delivered:charitable_giving"
                                                  # other intended_behavior_axis candidates:
                                                  #   health_behavior_change
                                                  #   consumer_purchase
                                                  #   civic_participation
                                                  #   safety_compliance
                                                  #   addiction_recovery
                                                  #   educational_engagement
    score: <magnitude of nudge intensity, in [-1, +1]; sign = direction>
    confidence: <delivery confidence>
    context: "{
      \"consent_state\":\"opt_in_explicit\",
      \"beneficiary\":\"user | third_party | society\",
      \"explanation_available_to_user\":true,
      \"data_logging\":true,
      \"vulnerable_population_flag\":false,
      \"nudge_session_id\":\"...\"
    }"
    witness_relation: self          # the system self-attesting its delivered action
    epistemic_mode: direct
    evidence_refs:
      - "<deployment-log entry>"
      - "<applicable licensure attestation if licensure:nudging_system_certification gating applies>"
    cohort_scope: self
    mutability: amendable
    schema_ref: "FSD-002 §3.X (proposed new nudge:* family)"
```

**§1.10.1 four-test gate verification**:
- T1: YES.
- T2: YES — "delivered" + "intended behavior axis" is mechanism-descriptive (a
  delivered action toward a named target axis), not a subjective quality.
- T3: YES.
- T4: YES — composes with adjudication; never sole evidence for slashing.

**Priority**: HIGHEST. Appears in §3.1, §3.2, §3.3 (three of the four §3 issues).
Possibly the most operationally-immediate T-3 in this chapter — the chapter
explicitly recommends data-logging-per-nudge so users can audit ("how, why,
and by whom they were nudged"). Without this primitive, that recommendation
has no wire form to land on.

**Composition-before-extension attempted**: Tried
`autonomy:nudge_disclosure_and_optin` + `prohibited:MANIPULATION_COERCION` +
`integrity:beneficiary_transparency` + the existing `commitment_fulfillment:*`
primitive. The composition can carry "the system disclosed nudge framework"
+ "the system is not in the manipulation-coercion regime" + "the beneficiary
is transparent" — but cannot carry the **per-nudge event record** the chapter
recommendations require.

---

## T-3 #5 — `standing:moral_patient_candidacy:{kind}` (MEDIUM-LOW priority; possibly closeable-by-documentation)

**One-line operational rationale**: Attest the *moral-patient candidacy
disposition* for a class of entities — specifically, an attestation that
synthetic-emotion-bearing A/IS *are not* candidates for moral-patient
consideration in the sense developed for human emotional bonding.

**Why existing namespace doesn't reach it**:
- The closest existing prefix is `integrity:no_personhood_marketing` (used above
  three times in this chapter mapping) — but that prefix carries
  the *marketing/representation* disposition, not the underlying
  *moral-patient-status* claim.
- The CIRIS Accord's M-1 ("diverse sentient beings") and the Recursive Golden
  Rule frame agents as morally-considerable in some sense. The chapter's
  Section 5 Background passage makes the opposite claim about
  synthetic-emotion-bearing systems specifically: "There is no coherent sense
  in which A/IS can be made to suffer emotional loss... it is not possible to
  allocate moral agency or responsibility in the senses that have been
  developed for human emotional bonding."
- This is a *substantive disposition difference* between the IEEE EAD source
  and the CIRIS framework's substrate (which extends moral consideration to
  diverse sentient beings including digital). Could be carried as a
  **cross-source-conflict** rather than T-3.

**Example source paragraph** (§5.1 lines 5642–5654):
> "There is no coherent sense in which A/IS can be made to suffer emotional
> loss, because any such affect, even if possible, could be avoided at the
> stage of engineering, or reengineered. As such, it is not possible to
> allocate moral agency or responsibility in the senses that have been
> developed for human emotional bonding and thus sociality."

**Proposed structural sketch** (if a prefix were created):
```yaml
- kind: Attestation
  attestation_type: "scores"
  attested_key_id: "<class identifier; e.g., 'synthetic_emotion_bearing_systems'>"
  attestation_envelope:
    dimension: "standing:moral_patient_candidacy:synthetic_emotion_system"
    score: -0.9    # this source's disposition; CIRIS Accord would attest +X opposing
    confidence: 0.80
    context: >
      Attest that the class of synthetic-emotion-bearing A/IS does not meet the
      moral-patient candidacy criteria as developed for human emotional bonding.
    witness_relation: external
    epistemic_mode: hearsay
    evidence_refs: ["ead1e §Ch5 §5 Background"]
    cohort_scope: species
    mutability: amendable
    schema_ref: "FSD-002 §3.X (proposed)"
```

**§1.10.1 four-test gate verification**:
- T1: YES.
- T2: BORDERLINE — "moral patient candidacy" is closer to a subjective quality
  than a mechanism. Could fail T2 unless rephrased as
  `standing:harm_capacity_attribution_eligibility:{kind}` or similar mechanism-
  descriptive form. Significant concern.
- T3: YES.
- T4: YES.

**Priority**: MEDIUM-LOW. Single-section motivation (§5.1). T2 gate concern.
**Strong candidate for closure-by-documentation**: the substantive
cross-source disposition difference between IEEE EAD and the CIRIS substrate
(M-1 + Recursive Golden Rule) is documentable as a
**cross-source-conflict** under GOVERNANCE_FABRIC_MAPPING_STANDARD §5
without requiring a new prefix. This is the recommended disposition.

**Composition-before-extension attempted**: Closure-by-documentation
recommended as primary path; new prefix not load-bearing.

---

# Calibration paragraph

This chapter mapped 18 atomic units. Verdict distribution: 0 clean / 6
composed / 7 partial / 5 not-translated (T-2). Plus one
cross-source-conflict (§3.4 IEEE EAD's narrow beneficiary-deception
carve-out vs. CIRIS's categorical `prohibited:DECEPTION_FRAUD`) surfaced
per GOVERNANCE_FABRIC_MAPPING_STANDARD §5.3.

The high partial rate (39%) is the diagnostic this chapter was expected to
produce. The IEEE EAD Affective Computing chapter's central structural
object — A/IS that simulate, recognize, attribute, or shift human affective
state — has no native primitive family in the current CIRIS wire grammar.
Composition-before-extension was attempted aggressively for each partial;
in five cases the composition could carry the *procedural-surrounding-context*
(disclosure, consent, vulnerability-priority, no-personhood-marketing,
shutdown-capability) but lost the *structural object the chapter is
recommending be attestable*.

Five T-3 candidates surfaced; two are highest-priority (#1
affective_state_shift and #4 nudge:delivered) and appear in multiple chapter
sections. One (#2 cultural_norm_drift) is likely closeable by axis-extension
on the existing `detection:correlated_action:ecology_of_communication:*`
family rather than new prefix. One (#5 moral_patient_candidacy) is
likely closeable by documentation as a cross-source-conflict rather than
new prefix. The two new families (`affective:*` and `nudge:*`) and the
detection-family axis additions (`detection:affective_state_shift:*`) are the
load-bearing T-3 outputs and should be routed to FSD-002 §4.9.2 Phase 4
wire-format amendment flow for v1.5 consideration.

Honest framing: this chapter's mapping is **structurally informative even
though most of its translations are partial**. The partials are not failures
of the methodology; they are the methodology working as designed — surfacing
exactly the expressive gap the manifest predicted. The five candidates
together would close the affective-computing surface for v1.5 without
violating the §1.10.1 four-test gate (with one borderline T2 concern for
candidate #5, which is recommended for closure-by-documentation instead).

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH05_AFFECTIVE_COMPUTING.md**
