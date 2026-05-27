# CONTRIBUTION_OBJECTS_IEEE_EAD_CH09_EMBEDDING_VALUES.md
# IEEE Ethically Aligned Design First Edition (2019) — Chapter "Embedding Values
# into Autonomous and Intelligent Systems"
# Three sections: (1) Identifying norms; (2) Implementing norms; (3) Evaluating
# implementation. Each section contains 3 Issues with Background / Recommendation
# substructure.
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 9113–10752)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

This chapter is the **value-alignment technical-implementation core** of EAD1e — it
moves from the high-level General Principles (Ch 2) into how A/IS actually adopt,
learn, and follow norms. The chapter has a direct correspondence with CIRIS's PDMA
(Principle-Driven Moral Action) stack, the four conscience faculties, and the
principle-anchoring infrastructure (`pdma_framing.yml §III` polyglot principle
anchoring). Expected: high clean+composed; possible T-3 in specific value-learning
technical proposals (computational norm representation, bottom-up moral learning,
"gateway" / "Ethical Governor" patterns).

The chapter recurrently flags the cultural-particularity of norms ("the norms of the
specific community"; "diverse cultural norms") — these compose onto CIRIS
`witness_diversity:*` + `pdma_framing.yml §III multi-tradition` reference, not onto a
new prefix family.

Source quotes are bounded at ≤ 2 sentences per LANGUAGE_PRIMER discipline.

---

## §Ch9.0 — Chapter preamble: society lacks universal embedding standards; norms as instructions to act in defined ways

```yaml
# Lines 9117–9136 — Chapter opening: no universal embedding standards yet; A/IS
# must "adopt, learn, and follow" community norms; "norms" preferred to "values"
# as a more realistic computational target; community norms reflect community values
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:norm_identification_implementation_evaluation"
      score: 1.0
      confidence: 0.85
      context: >
        A/IS "must be designed to adopt, learn, and follow the norms and values of
        the community they serve." Names the chapter's structural method: a
        three-phase process (identify → implement → evaluate) that operationalises
        value alignment as norm-conformity instead of direct value-representation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch9 preamble lines 9117–9136"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:community_specific_norm_grounding"
      score: 1.0
      confidence: 0.85
      context: >
        "A community's network of social and moral norms is likely to reflect the
        community's values, and A/IS equipped with such a network would, therefore,
        also reflect the community's values." Cultural-particularity framing — norms
        are not universal but community-grounded; composes onto
        witness_diversity:* + the pdma_framing §III multi-tradition anchoring.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch9 preamble lines 9132–9136"
        - "ContributionRef(source_material/dma_prompts/localized/polyglot/pdma_framing.txt §III)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*)"
verdict: composed
nuance_lost: |
  The conceptual concession — that "values" themselves are too complex to be
  represented directly, but norms (observable in behavior) can be — is a substantive
  philosophical pivot of the chapter; encoded here only via the method-level claim
  + the cultural-particularity composition. The four cited "values" papers
  (Hitlin/Piliavin; Malle/Dickert; Rohan; Sommer) are preserved via evidence_refs but
  not as separate delegates_to attestations.
```

---

## §Ch9.intro — Three concrete goals + conflict tolerance + transparent signaling

```yaml
# Lines 9158–9197 — three concrete goals (identify; implement; evaluate); conflicts
# of values/norms are natural; transparent signaling required
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:iterative_norm_lifecycle"
      score: 1.0
      confidence: 0.85
      context: >
        "Pursuing these three goals represents an iterative process that is sensitive
        to the purpose of the A/IS and to its users within a specific community."
        Method-level claim that norm-alignment is a continuous lifecycle process
        (not a one-time pre-deployment check), with sensitivity to deployment
        context.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch9 lines 9174–9194"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:norm_behavior_signals_to_community"
      score: 1.0
      confidence: 0.85
      context: >
        "Systems are designed to provide transparent signals describing the specific
        nature of their behavior to the individuals in the community they serve.
        Such signals may include explanations or offers for inspection and must be
        in a language or form that is meaningful to the community." Composes
        transparency_log with cohort-appropriate language register — the
        per-stakeholder transparency mechanism (cf. Ch 2 §P5.bg).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch9 lines 9184–9194"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  "Conflicts of values and norms when identifying, implementing, and evaluating
  these systems... are a natural part of the dynamically changing and renegotiated
  norm systems of any community" — this is a substantive recognition that conflict
  is constitutive, not pathological. Carried indirectly by amendable mutability on
  the lifecycle method; no separate primitive emitted (Section 1 Issue 3 below
  handles conflict resolution explicitly).
```

---

# Section 1 — Identifying Norms for Autonomous and Intelligent Systems

---

## §S1.0 — Section preamble: three issues (which norms; updating; conflict resolution)

```yaml
# Lines 9215–9233 — Section 1 framing: three issues addressed (which norms; their
# dynamic nature; conflicts)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The three-issue enumeration is structural framing of the section. Each issue's
  substantive operational content is carried by its own subsection (Issues 1–3
  below); the enumeration itself is structural framing per LANGUAGE_PRIMER §8
  Step 1(b). No independent claim is made here.
nuance_lost: |
  The implicit ordering (which-norms-first, then-updating, then-conflict) carries
  pedagogical priority that the wire format does not encode at the section level.
```

---

## §S1.I1.bg — Issue 1 Background: laws documented; social norms expressed through behavior; communities differ

```yaml
# Lines 9237–9270 — Issue 1 Background: laws are documented; social/moral norms
# expressed through behavior/language/customs; communities differ; no universal
# norm set realistic; UDHR constrains norms; community-specific deployment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:community_norm_specificity"
      score: 1.0
      confidence: 0.85
      context: >
        "Communities ranging from families to whole nations differ to various degrees
        in the norms they follow. Therefore, generating a universal set of norms
        that applies to all A/IS in all contexts is not realistic." Community
        plurality + locality scaling — composes naturally onto witness_diversity:*
        + the v1.3 locality:decision:{scale} primitive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I1 lines 9221–9230"
        - "ContributionRef(source_material/dma_prompts/localized/polyglot/pdma_framing.txt §III)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:human_rights_constrain_local_norms"
      score: 1.0
      confidence: 0.90
      context: >
        "These universal rights are not sufficient for devising A/IS that conform to
        the specific norms of its community. Universal Human Rights must, however,
        constrain the kinds of norms that are implemented in the A/IS." UDHR-anchored
        constitutional constraint on what local norm-learning may admit; aligns with
        the Ch 2 §P1 justice:human_rights claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I1 lines 9234–9243"
        - "ead1e Principle 1 Further Resources (UDHR/ICCPR/etc.)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: |
  The distinction between "documented" laws and "expressed-through-behavior"
  social/moral norms is a substantive epistemology of where evidence comes from for
  each kind of norm. The wire form does not type evidence-source-by-norm-class;
  encoded indirectly via the method:* attestations downstream that mention empirical
  research vs legal-documentation retrieval.
```

---

## §S1.I1.body — Issue 1: norms vary by A/IS type; represent vulnerable + underrepresented groups; individual personalization within community bounds; empirical multi-disciplinary research

```yaml
# Lines 9268–9314 — Issue 1 body: A/IS-type-specific norms (self-driving vs
# healthcare robot); vulnerable + underrepresented groups must be represented;
# individual personalization within community bounds; empirical multi-disciplinary
# research required
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.90
      context: >
        "The norm identification process must heed such variation and ensure that
        the identified norms are representative, not only of the dominant subgroup
        in the community but also of vulnerable and underrepresented groups."
        Direct match to the v1.3 §6.1.4 lexical-vulnerability-priority consumer
        policy — vulnerable cohorts retain priority weight in norm-identification.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I1 lines 9280–9285"
        - "ContributionRef(FSD-002 §6.1.4 lexical-vulnerability-priority)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle); FSD-002 §6.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:multi_disciplinary_empirical_norm_research"
      score: 1.0
      confidence: 0.85
      context: >
        "Innovation projects and development efforts for A/IS should always rely on
        empirical research, involving multiple disciplines and multiple methods; to
        investigate and document both context- and task-specific norms, spoken and
        unspoken, that typically apply in a particular community." Method-level
        Family B claim composed with witness_diversity discipline (multi-discipline =
        diverse witness perspective).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I1 lines 9309–9314"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:individual_personalization_within_norms"
      score: 1.0
      confidence: 0.85
      context: >
        "Unique individual expectations must not violate norms in the larger
        community. Whereas the arrangement of someone's kitchen... can be
        personalized without violating any community norms, encouraging the robot
        to use derogatory language to talk about certain social groups does violate
        such norms." Bounds individual autonomy by community norms; composes onto
        autonomy:* with cohort-scoped bounds.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I1 lines 9295–9307"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: composed
nuance_lost: |
  The example of an A/IS being "encouraged" by a racist user to use derogatory
  language is a vivid worked case the wire form captures only at the principle
  level (prohibited:discrimination would be the hard-constraint analogue, but the
  text uses the example to illustrate the priority-override mechanic, not to invoke
  a prohibition). The four-category structure (vulnerable groups; A/IS-type
  variation; individual personalization; empirical research) is preserved by the
  composed-verdict envelope rather than by separate edges.
```

---

## §S1.I1.r — Issue 1 Recommendation: identify community norms; use scientific methods through lifecycle

```yaml
# Lines 9281–9293 — Issue 1 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:lifecycle_norm_identification_scientific"
      score: 1.0
      confidence: 0.90
      context: >
        "To develop A/IS capable of following social and moral norms, the first step
        is to identify the norms of the specific community in which the A/IS are to
        be deployed... This norm identification process must use appropriate
        scientific methods and continue through the system's life cycle." Method
        with explicit lifecycle scope + scientific-discipline grounding.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I1 Recommendation lines 9282–9293"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
nuance_lost: |
  "Through the system's life cycle" implies a continuous-progress-measure shape
  that the bare method:* primitive carries only implicitly; a fuller encoding would
  emit progress_measure:* attestations downstream tied to this method.
```

---

## §S1.I2.bg — Issue 2 Background: norms are dynamic; A/IS need update capacities (behavioral trend processing; uncertainty asking; instruction; feedback)

```yaml
# Lines 9333–9377 — Issue 2 Background: norms change over time; A/IS need starting
# set + ongoing update; humans update via observation + asking + feedback; A/IS
# need 4 capacities (behavioral trend processing; uncertainty-triggered asking;
# instruction-responsiveness; feedback-responsiveness); norm modification can
# occur at priority/qualitative/quantitative levels
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:norm_update_capacities"
      score: 1.0
      confidence: 0.80
      context: >
        A/IS need capacities to: process behavioral trends vs baseline; ask for
        guidance when uncertainty exceeds threshold; respond to community
        instruction in novel contexts; respond to feedback on norm violations.
        Method-level claim describing the operational shape of online value-learning.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I2 lines 9329–9359"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 1.0
      confidence: 0.90
      context: >
        "Asking for guidance from the community when uncertainty about applicable
        norms exceeds a critical threshold." Direct alignment with the CIRIS
        epistemic_humility conscience faculty — uncertainty-triggered deferral.
        Aligns with Wisdom-Based Deferral (WBD) discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I2 lines 9340–9343"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
verdict: composed
nuance_lost: |
  The three-level modification taxonomy (priority weights / qualitative expression /
  quantitative parameters) is a substantive design schema. Encoded indirectly via
  the method:* attestation context; a richer encoding could emit per-level
  sub-methods, but composition-before-extension holds — these are refinements
  inside one method, not three distinct structural objects.
```

---

## §S1.I2.transparency — Issue 2: norm changes must be transparent; consult users/designers/community; learning without review is detrimental

```yaml
# Lines 9362–9407 — Norm-change transparency; consult users/designers/community;
# Green and Hu 2018 on detrimental consequences of unreviewed learning;
# consultation form varies by sophistication (documentation-consult vs explicit
# announcement vs panel-decision)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:norm_change_consultation"
      score: 1.0
      confidence: 0.85
      context: >
        "The system's norm changes be transparent. That is, the system or its
        designer should consult with users, designers, and community representatives
        when adding new norms to its norm system or adjusting the priority or
        content of existing norms." Direct mapping to transparency_log:* with
        multi-stakeholder consultation discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I2 lines 9362–9377"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:unreviewed_norm_learning"
      score: -1.0
      confidence: 0.85
      context: >
        "Allowing a system to learn new norms without public or expert review has
        detrimental consequences" (Green and Hu 2018). Negative attestation —
        unreviewed value-learning is harm-class. Composes with witness_diversity
        review discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I2 lines 9375–9377"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:representative_crowdsourced_panel"
      score: 1.0
      confidence: 0.80
      context: >
        "In yet other cases, the A/IS may propose changes, and the relevant human
        community, e.g., drawn from a representative crowdsourced panel, will
        decide whether such changes should be implemented in the system." Direct
        mapping to witness_diversity:* — the N=3 diversity bar (jurisdictional +
        organizational + software-stack + cell-expertise) is the framework analogue
        of the document's "representative crowdsourced panel."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I2 lines 9402–9407"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*)"
verdict: composed
nuance_lost: |
  The graduated consultation taxonomy (consult-documentation vs explicit-announcement
  vs panel-decision, varying by machine sophistication) is a substantive design
  choice. Carried at the method/transparency level; the variation itself is
  collapsed into amendable mutability + per-stakeholder context. The Green and Hu
  citation could be a delegates_to authority-source attestation in a richer
  mapping.
```

---

## §S1.I2.r — Issue 2 Recommendation: amend norms with transparency

```yaml
# Lines 9410–9416 — Issue 2 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:transparent_norm_amendment"
      score: 1.0
      confidence: 0.90
      context: >
        "To respond to the dynamic change of norms in society A/IS or their designers
        must be able to amend their norms or add new ones, while being transparent
        about these changes to users, designers, broader community representatives,
        and other stakeholders." Recommendation summary — method + transparency_log
        + multi-stakeholder consultation composed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I2 Recommendation lines 9410–9416"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
nuance_lost: |
  "Amend norms" is the operational shape of the supersedes structural primitive
  applied to norm-attestations (each norm change is a supersedes edge on the prior
  norm). The recommendation does not name supersedes/recants explicitly; the wire
  form would carry per-amendment supersedes attestations downstream.
```

---

## §S1.I3.bg — Issue 3 Background: moral dilemmas / moral overload; priority hierarchies; constrained by Common Good Principle + local laws

```yaml
# Lines 9398–9432 — Issue 3 Background: moral dilemmas / moral overload
# (Van den Hoven 2012); humans resolve via trade-offs constituting priorities;
# represented as hierarchical relations; constrained by Common Good Principle
# (Andre and Velasquez 1992) + local laws
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:norm_priority_hierarchy"
      score: 1.0
      confidence: 0.85
      context: >
        "Humans resolve such situations by accepting trade-offs between conflicting
        norms, which constitute priorities of one norm or value over another in a
        given context. Such priorities may be represented in the norm system as
        hierarchical relations." Method-level claim describing the operational
        shape of norm-conflict resolution. Aligns with CIRIS PDMA principle-weighting
        + the v1.3 §6.1.4 lexical-vulnerability-priority modifier.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 lines 9407–9412"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §V relational obligations)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 1.0
      confidence: 0.80
      context: >
        "These more local conflict resolutions will be further constrained by some
        general principles, such as the 'Common Good Principle'... or local and
        national laws." Decision-locality scaling — local conflict resolutions
        operate at community scope but bounded by federation-scale principles.
        Composes with the v1.3 §6.1.5 locality-scaled-quorum.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 lines 9419–9430"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore: locality:decision:{scale})"
verdict: composed
nuance_lost: |
  "Moral overload" as a named concept (Van den Hoven 2012) and "Common Good Principle"
  (Andre and Velasquez 1992) are substantive philosophical anchors carried by
  evidence_refs only. A richer mapping could emit delegates_to authority-source
  attestations for each. The self-driving vehicle example as a worked traffic-law
  case is illustrative pedagogy; preserved by evidence_refs context.
```

---

## §S1.I3.override — Issue 3: harm-prohibition overrides lying-prohibition; community norms override individual preferences; democratic processes resolve community-vs-designer tension

```yaml
# Lines 9446–9484 — Some priorities built-in as hierarchical relations (harm-norms
# override lying-norms); community norms override individual user (racist user
# example); democratic processes for community-vs-designer-tension; sometimes
# international/humanitarian norms override local racist/sexist practices
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:harm_priority_over_other_norms"
      score: 1.0
      confidence: 0.90
      context: >
        "More general prohibitions against harm to humans typically override more
        specific norms against lying." Hard-coded priority — non_maleficence
        dominates fidelity in norm-conflict. Aligns with CIRIS Accord §I + the
        PDMA principle-weighting that puts non_maleficence at constitutional priority.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 lines 9446–9450"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II non_maleficence)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 0.95
      context: >
        "The A/IS of a racist user who demands the A/IS use derogatory language for
        certain social groups will have to resist such demands because community
        norms hierarchically override an individual user's preferences." Direct
        invocation of the discrimination prohibition; the community-override
        mechanism is the structural shape, the prohibited:* hard constraint is the
        constitutional bound.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 lines 9450–9459"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:democratic_norm_conflict_resolution"
      score: 1.0
      confidence: 0.80
      context: >
        "Tension may sometimes arise between a community's social and legal norms
        and the normative considerations of designers or manufacturers. Democratic
        processes may need to be developed that resolve this tension." Method-level
        claim for community-vs-designer-tension resolution; aligns with CIRIS
        Wise-Authority quorum + Reconsideration discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 lines 9470–9481"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:international_principles_override_local_injustice"
      score: 1.0
      confidence: 0.85
      context: >
        "In some cases the community may have to be persuaded to accept A/IS
        favoring international law or broader humanitarian principles over, say,
        racist or sexist local practices." Justice claim that universal human rights
        (Ch 2 §P1) override local-norm conflict when local practices are
        discriminatory. Aligns with v1.3 §6.1.4 lexical-vulnerability-priority.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 lines 9477–9481"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle); FSD-002 §6.1.4"
verdict: composed
nuance_lost: |
  The "racist user" example (§S1.I3) and the "racist/sexist local practices"
  example (§S1.I3 ending) are both worked illustrative cases. Carried at the
  principle + prohibited level; the document's pedagogical chaining (individual
  preference → community norm → international humanitarian principle) is preserved
  by composed-verdict envelope rather than by explicit edges.
```

---

## §S1.I3.r — Issue 3 Recommendation: identify resolution methods; document for users/community/third parties

```yaml
# Lines 9469–9482 — Issue 3 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:norm_conflict_resolution_identification"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS developers should identify the ways in which people resolve norm
        conflicts and the ways in which they expect A/IS to resolve similar norm
        conflicts." Method-level claim — empirical identification of
        conflict-resolution patterns.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 Recommendation lines 9469–9474"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:conflict_resolution_to_third_parties"
      score: 1.0
      confidence: 0.85
      context: >
        "A system's resolution of norm conflicts must be transparent—that is,
        documented by the system and ready to be made available to users, the
        relevant community of deployment, and third-party evaluators." Direct
        mapping to transparency_log:* with multi-stakeholder access scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S1.I3 Recommendation lines 9474–9479"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The third-party transparency requirement here previews Section 3 Issue 3
  third-party-evaluator transparency (which goes further). Treated as composed
  in this Recommendation; the more detailed claim is at §S3.I3 below.
```

---

# Section 2 — Implementing Norms in Autonomous and Intelligent Systems

---

## §S2.0 — Section preamble: link norms to functionality; three implementation issues

```yaml
# Lines 9610–9646 — Section 2 framing: link norms to functionality; three issues
# (computational approaches; transparency; failures); guideline — designers
# should consider forms/metrics of evaluation throughout implementation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:norm_implementation_evaluation_continuum"
      score: 1.0
      confidence: 0.85
      context: >
        "Through the entire process of implementation of norms, designers should
        consider various forms and metrics of evaluation, and they should define
        and incorporate central criteria for assessing the A/IS' norm conformity,
        e.g., human-machine agreement on moral decisions, verifiability of A/IS
        decisions, or justified trust." Method-level claim that implementation and
        evaluation are not separated phases; implementation already prepares for
        evaluation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.0 preamble lines 9634–9646"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
nuance_lost: |
  The three-criteria enumeration (human-machine agreement; verifiability;
  justified trust) is a specific evaluation-criterion taxonomy. Encoded at the
  method:* level; the trio reappears in Section 3 as evaluation criteria.
```

---

## §S2.I1.bg — Issue 1: top-down vs bottom-up vs hybrid approaches; ethical governors / guardians; verifiable logical format

```yaml
# Lines 9619–9716 — Issue 1 Background: machine morality/ethics field has many
# names (machine morality, machine ethics, moral machines, value alignment,
# computational ethics, artificial morality, safe AI, friendly AI); Wallach+Allen
# categorisation: A top-down (symbolic, identifies states as ethical/unethical);
# B bottom-up (learning component); C hybrid; "Ethical Governors" (Arkin),
# "Guardians" (Etzioni) monitor/restrict/adapt; verifiable logical format for
# action selection; bottom-up learning for constraining norms; A/IS can learn to
# detect pain/pleasure without feeling them
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:value_alignment_implementation_diversity"
      score: 1.0
      confidence: 0.80
      context: >
        Multiple implementation approaches — top-down (symbolic), bottom-up
        (learning), hybrid (e.g., subsymbolic action selection + symbolic
        "gateway" agent for ethical checking, Arkin's "Ethical Governors" or
        Etzioni's "Guardians"). Method-level Family B claim that the
        implementation surface admits multiple architectures.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I1 lines 9639–9694"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:symbolic_gateway_check"
      score: 1.0
      confidence: 0.80
      context: >
        "The selection of action might be carried out by a subsymbolic system, but
        this action must be checked by a symbolic 'gateway' agent before being
        invoked. This is a typical approach for 'Ethical Governors' (Arkin, 2008)
        or 'Guardians' (Etzioni 2016) that monitor, restrict, and even adapt
        certain unacceptable behaviors." Direct structural analogue of CIRIS
        conscience faculties (Entropy, Coherence, Optimization Veto, Epistemic
        Humility) — post-action-selection symbolic checks before action execution.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I1 lines 9678–9694"
        - "ContributionRef(source_material/conscience/core.py)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
verdict: composed
nuance_lost: |
  The specific architectural pattern — "subsymbolic action selection + symbolic
  gateway check" — is a substantive technical pattern that maps cleanly onto
  CIRIS's conscience-faculties stack but is not a wire-format-specific structural
  primitive. The four conscience faculties (Entropy/Coherence/Optimization Veto/
  Epistemic Humility) are the framework's instantiation of this pattern. The text
  also notes A/IS "can learn to detect and take into account others' pain and
  pleasure, thus at least achieving some of the positive effects of empathy"
  (lines 9712–9716) — affective-computing-adjacent claim; flagged to Ch 5
  Affective Computing T-3 surface per manifest, not load-bearing here.
```

---

## §S2.I1.r — Issue 1 Recommendation: diverse research efforts; cross-school collaboration

```yaml
# Lines 9731–9742 — Issue 1 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:cross_school_collaborative_research"
      score: 1.0
      confidence: 0.80
      context: >
        "In light of the multiple possible approaches to computationally implement
        norms, diverse research efforts should be pursued, especially collaborative
        research between scientists from different schools of thought and different
        disciplines." Method-level + witness_diversity composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I1 Recommendation lines 9731–9742"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
```

---

## §S2.I2.bg — Issue 2 Background: transparency as four-fold (traceability, verifiability, honest design, intelligibility); transparency to multiple stakeholders

```yaml
# Lines 9804–9837 — Issue 2 Background: A/IS must explain reasoning;
# transparency/explainability paramount; multi-level + multi-stakeholder
# transparency (Kroll noting security exception); four-fold decomposition:
# traceability (Cleland-Huang) / verifiability (formal proof) / honest design
# (Rams) / intelligibility (Tintarev+Kutlak; GDPR right-to-explanation)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:four_dimensional_decomposition"
      score: 1.0
      confidence: 0.90
      context: >
        Transparency decomposed into four dimensions: traceability (software
        engineering process; Cleland-Huang 2012); verifiability (formal verification;
        Fisher/Dennis/Webster 2013); honest design (Rams; appearance does not
        overpromise capability); intelligibility (Tintarev/Kutlak; explanation in
        ordinary language; GDPR right-to-explanation). Extends the Ch 2 §P5
        three-dimensional decomposition (traceability/explainability/interpretability)
        to include "honest design" as a fourth dimension.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I2 lines 9797–9837 + 9852–9905"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:honest_design_no_capability_overrepresentation"
      score: 1.0
      confidence: 0.85
      context: >
        "Honest design of A/IS is one aspect of their transparency, because it
        allows the user to 'see through' the outward appearance and accurately infer
        the A/IS' actual capacities... Demands for transparency in design therefore
        put a responsibility on the designer to 'not attempt to manipulate the
        consumer with promises that cannot be kept'." Integrity claim against
        capability-misrepresentation; composes with prohibited:deception_fraud.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I2 lines 9852–9879"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:deception_fraud"
      score: -1.0
      confidence: 0.85
      context: >
        "The agent displays signs of a certain human-like emotion but its internal
        state does not represent that human emotion. Humans are quick to make
        strong inferences from outward appearances of human-likeness to the mental
        and social capacities the A/IS might have." Names appearance-capability
        misrepresentation as harm class — composes with the DECEPTION_FRAUD
        prohibition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I2 lines 9863–9871"
        - "ContributionRef(source_material/prohibitions.py::DECEPTION_FRAUD)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:formal_verification_for_norm_compliance"
      score: 1.0
      confidence: 0.85
      context: >
        "Explicit and exact representations of these normative decisions can then
        provide the basis for a range of strong mathematical techniques, such as
        formal verification (Fisher, Dennis, and Webster 2013). Even if a system
        cannot explain every single reasoning step in understandable human terms, a
        log of ethical reasoning should be available for inspection of later
        evaluation purposes (Hind et al. 2018)." Method-level claim — formal
        verification + ethical-reasoning audit log.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I2 lines 9824–9837"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  The GDPR right-to-explanation reference (lines 9898–9905) is a substantive
  legal anchor that a richer mapping could carry as a delegates_to authority-source.
  The boyd (2016) critique of GDPR transparency-as-accountability is preserved by
  evidence_refs but not as a separate attestation — it's pastoral-prose-adjacent
  context. The "transparency to all parties may not always be advisable" exception
  for security programs (line 9834) is a substantive non-trivial constraint; carried
  by amendable mutability on the four-dimensional decomposition rather than as a
  separate exception primitive.
```

---

## §S2.I2.r — Issue 2 Recommendation: high transparency (traceability + verifiability + honest design + intelligibility)

```yaml
# Lines 9858–9866 — Issue 2 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:high_transparency_constitutional_bound"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS, especially those with embedded norms, must have a high level of
        transparency, shown as traceability in the implementation process,
        mathematical verifiability of their reasoning, honesty in appearance-based
        signals, and intelligibility of the systems' operation and decisions."
        Constitutional bound on transparency — the four-dimensional decomposition
        as binding rule, not just description.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I2 Recommendation lines 9858–9866"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: clean
```

---

## §S2.I3.bg — Issue 3 Background: failures unavoidable; four mitigation strategies (criteria/metrics; risk analysis; fail-safe gateway; public incident database)

```yaml
# Lines 9964–10026 — Issue 3 Background: failures unavoidable; four strategies:
# (1) evaluation criteria/metrics for detection-mitigation; (2) systematic risk
# analysis (Oetzel and Spiekermann 2014); (3) fail-safe components with strict
# laws + symbolic gateway agent; (4) publicly accessible database of A/IS
# undesired outcomes
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:failure_inevitability_mitigation_design"
      score: 1.0
      confidence: 0.90
      context: >
        "Operational failures and, in particular, violations of a system's embedded
        community norms, are unavoidable, both during system testing and during
        deployment... Thus, prevention and mitigation strategies must be adopted."
        Non_maleficence claim — failure is structural, mitigation must be
        designed-in.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I3 lines 9964–9980"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:multi_level_failure_metrics"
      score: 1.0
      confidence: 0.85
      context: >
        Strategy 1: three-level metrics — technical (traceability, verifiability);
        user-level (reliability, understandable explanations, feedback
        responsiveness); community-level (justified trust, collective belief that
        A/IS create social benefits rather than technological unemployment). Direct
        progress_measure:* with three-level decomposition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I3 lines 9982–9998"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: progress_measure:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:systematic_risk_analysis"
      score: 1.0
      confidence: 0.80
      context: >
        Strategy 2: "A systematic risk analysis and management approach can be useful
        (Oetzel and Spiekermann 2014) for an application to privacy norms." Method-
        level claim referencing the privacy-impact-assessment methodology.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I3 lines 10000–10003"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:failsafe_gateway_strict_laws"
      score: 1.0
      confidence: 0.85
      context: >
        Strategy 3: "Augment the architectures of their systems with components that
        handle unanticipated norm violations with a fail-safe, such as the symbolic
        'gateway' agents... Designers should identify a number of strict laws, that
        is, task- and community-specific norms that should never be violated, and
        the fail-safe components should continuously monitor operations." Direct
        analogue of CIRIS conscience faculties (especially Optimization Veto) +
        Accord prohibited:* hard constraints — the never-violate strict laws.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I3 lines 10003–10026"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
        - "ContributionRef(source_material/prohibitions.py)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts) + §3.1.4 (prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:public_incident_database"
      score: 1.0
      confidence: 0.85
      context: >
        Strategy 4: "Once failures have occurred, responsible entities, e.g.,
        corporate, government, science, and engineering, shall create a publicly
        accessible database with undesired outcomes caused by specific A/IS systems.
        The database would include descriptions of the problem, background
        information on how the problem was detected, which context it occurred in,
        and how it was addressed." Direct mapping to transparency_log:* —
        federation-level incident registry. Composes naturally with CIRISPersist
        audit_chain:* + the §6.1 reference policy for incident provenance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I3 lines 10015–10026"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*); FSD-002 §3.3 (CIRISPersist: audit_chain:*)"
verdict: composed
nuance_lost: |
  The four-strategy enumeration is preserved as a composed envelope; the implicit
  precedence (preventive metrics → risk analysis → fail-safe → post-hoc reporting)
  is not explicitly encoded but mirrors the standard pre/during/post deployment
  cycle. The fail-safe-validation discipline ("validating them carefully and not
  letting them adapt their parameters during execution," line 9997–9998) is a
  substantive design constraint — fail-safes must be immutable during runtime — that
  the wire form carries as constitutional mutability on the conscience attestation.
  The "publicly accessible database" maps onto federation-graph + audit_chain
  primitives; not a new prefix.
```

---

## §S2.I3.r — Issue 3 Recommendation: multiple mitigation strategies must be in place

```yaml
# Lines 10032–10038 — Issue 3 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:multi_strategy_failure_mitigation"
      score: 1.0
      confidence: 0.90
      context: >
        "Because designers and developers cannot anticipate all possible operating
        conditions and potential failures of A/IS, multiple strategies to mitigate
        the chance and magnitude of harm must be in place." Recommendation summary —
        defense-in-depth discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S2.I3 Recommendation lines 10032–10038"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
```

---

# Section 3 — Evaluating the Implementation of A/IS

---

## §S3.0 — Section preamble: evaluation criteria; multi-method; ranges from formal proof to informal analysis; multi-party

```yaml
# Lines 10060–10116 — Section 3 framing: evaluation anticipated at design;
# multi-disciplinary; criteria include quality of human-machine interaction,
# human approval/appreciation, appropriate trust, adaptability, well-being benefits;
# BS8611:2016 cited; specify-verify-validate triplet (Sommerville 2015);
# PDCA cycle (ISO 9001); first parties (designers/users) + third parties
# (regulators/testing/certification); results available to all parties
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:lifecycle_evaluation_anticipated_at_design"
      score: 1.0
      confidence: 0.90
      context: >
        "Evaluation of A/IS implementations must be anticipated during a system's
        design, incorporated into the implementation process, and continue
        throughout the system's deployment." Method-level claim — evaluation is
        lifecycle-spanning, not post-hoc.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.0 preamble lines 10060–10116"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:multi_dimensional_evaluation_criteria"
      score: 1.0
      confidence: 0.85
      context: >
        "Evaluation criteria must capture, among others, the quality of
        human-machine interactions, human approval and appreciation of the A/IS,
        appropriate trust in the A/IS, adaptability of the A/IS to human users, and
        benefits to human well-being in the presence or under the influence of the
        A/IS." Direct progress_measure:* with the five-criterion enumeration.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.0 lines 10074–10086"
        - "ead1e §S3.0 line 10081 (BS8611:2016)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: progress_measure:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:first_party_third_party_evaluation"
      score: 1.0
      confidence: 0.85
      context: >
        "Evaluation may be done by first parties, e.g., designers, manufacturers,
        and users, as well as third parties, e.g., regulators, independent testing
        agencies, and certification bodies. In either case, the results of
        evaluations should be made available to all parties." Witness-diversity
        discipline — multi-party evaluation with cross-availability composes
        directly onto the N=3 diversity bar.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.0 lines 10094–10100"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*)"
verdict: composed
nuance_lost: |
  The specify-verify-validate triplet (Sommerville 2015) and the PDCA cycle
  (ISO 9001) are anchoring references that a richer mapping could carry as
  delegates_to authority-sources. The BS8611:2016 reference is also a substantive
  standards anchor; preserved via evidence_refs. The five-criterion enumeration
  (interaction quality / approval / appropriate trust / adaptability / well-being)
  is collapsed into one progress_measure:* with the enumeration as context;
  per-criterion sub-prefixes would risk failing §1.10.1 T2 (criteria are properties
  of the evaluation, not mechanisms).
```

---

## §S3.I1 — Issue 1: A/IS norms ≠ human norms (e.g., robot workers without breaks)

```yaml
# Lines 10109–10141 — Issue 1: A/IS and humans unlikely to have identical norms;
# some norms unique to humans (emotion regulation); some unique to A/IS (robot
# work without breaks); norm identification must document similarities and
# differences
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:differential_norms_human_vs_ais"
      score: 1.0
      confidence: 0.80
      context: >
        "The norm identification process must document the similarities and
        differences between the norms that humans apply to other humans and the
        norms they apply to A/IS. Norm implementations should be evaluated
        specifically against the norms that the community expects the A/IS to
        follow." Method-level claim — distinct norm-set per agent-class, evaluated
        against community expectations.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I1 Recommendation lines 10134–10141"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
nuance_lost: |
  The substantive philosophical claim that A/IS and humans operate under
  partially-overlapping norm sets — what the document does NOT do is argue this
  asymmetry, it stipulates it. The CIRIS framework's M-1 substrate-agnostic stance
  + Recursive Golden Rule have a richer reading here than EAD1e: substrate
  agnostic at principle layer + relationally asymmetric at originator-relation
  layer. Carried via amendable mutability + the method scope; the document's
  asymmetric-norms stipulation is not framework-mismatched but is framework-side
  thinner than CIRIS's relational structure. NOT a T-3 against the framework — the
  mismatch is on the source side.
```

---

## §S3.I2.bg — Issue 2 Background: A/IS biases against specific groups (passport / speech recognition / criminal risk / humanoid robot whiteness)

```yaml
# Lines 10158–10208 — Issue 2 Background: A/IS may have operational biases
# disadvantaging specific groups; examples: passport AI (Asian eye rejection,
# Griffiths 2016); speech recognition (gender bias, Tatman 2016); criminal risk
# (race bias, Angwin et al 2016); humanoid robots (white skin + female voice,
# Riek and Howard 2014); biases from imperfect norm identification, unrepresentative
# training sets, unconscious designer assumptions
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 0.95
      context: >
        Examples of A/IS bias against specific groups: passport-application AI
        rejecting Asian eyes; gender-biased speech recognition; race-biased
        criminal risk assessment overpredicting recidivism for African Americans;
        humanoid robots predominantly white and female-voiced. Direct invocation
        of the DISCRIMINATION prohibition — these are constitutional bound
        violations.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I2 lines 10165–10192"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:disadvantaged_groups"
      score: 1.0
      confidence: 0.80
      context: >
        "Bias can emerge in perception... in information processing... in
        decisions... in [the system's own] appearance and presentation." Names
        biases as population-scale correlation patterns — composes onto the F-3
        correlated-action detector with participation_exclusion axis. The four
        named bias-emergence sites (perception/processing/decision/appearance) all
        amount to systematic disadvantaging of identifiable populations.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §S3.I2 lines 10163–10192"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
verdict: composed
nuance_lost: |
  The four-site bias taxonomy (perception / processing / decisions / appearance)
  is a specific decomposition with diagnostic value. Encoded at the detection
  family level + prohibited:discrimination level. The four cited case studies
  (Griffiths/Tatman/Angwin/Riek+Howard) are vivid evidence; preserved via
  evidence_refs. The three sources of bias (imperfect norm identification;
  unrepresentative training sets; designer unconscious assumptions) reappear as
  provenance:build_manifest:training_artifacts concerns at Ch 2 §P6.r — not
  re-emitted here, but consumers should follow the federation-graph edges.
```

---

## §S3.I2.body — Issue 2: integrate diverse social groups in planning + evaluation; behavioral scientists + target population

```yaml
# Lines 10153–10208 — Body: unanticipated biases reduced by integrating diverse
# social groups in planning + evaluation + community outreach (DO-IT, RRI);
# behavioral scientists + target population for criterion tasks
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:disadvantaged_group_inclusion"
      score: 1.0
      confidence: 0.85
      context: >
        "Unanticipated or undetected biases should be further reduced by including
        members of diverse social groups in both the planning and evaluation of
        A/IS and integrating community outreach into the evaluation process."
        Witness-diversity with explicit inclusion of potentially-disadvantaged
        cohorts — composes naturally with the N=3 diversity bar + v1.3 §6.1.4
        lexical-vulnerability-priority.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I2 lines 10156–10162"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*); FSD-002 §6.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:behavioral_scientists_and_target_populations"
      score: 1.0
      confidence: 0.80
      context: >
        "Behavioral scientists and members of the target populations will be
        particularly valuable when devising criterion tasks for system evaluation
        and assessing the success of evaluating the A/IS performance on those
        tasks." Direct mapping to expertise:* primitive with explicit
        domain-pairing (behavioral-science + target-population).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I2 lines 10162–10170"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: expertise:{domain}:{language})"
verdict: composed
nuance_lost: |
  DO-IT and RRI (Responsible Research and Innovation) frameworks named at line
  10161 are substantive methodological anchors that a richer mapping could carry
  as delegates_to. Preserved via evidence_refs context.
```

---

## §S3.I2.r — Issue 2 Recommendation: assess biases + integrate disadvantaged groups in diagnosis

```yaml
# Lines 10185–10191 — Issue 2 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:bias_assessment_disadvantaged_group_integration"
      score: 1.0
      confidence: 0.90
      context: >
        "Evaluation of A/IS must carefully assess potential biases in the systems'
        performance that disadvantage specific social and demographic groups. The
        evaluation process should integrate members of potentially disadvantaged
        groups in efforts to diagnose and correct such biases." Recommendation
        summary — method + witness_diversity + lexical-vulnerability-priority
        composed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I2 Recommendation lines 10185–10191"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*); FSD-002 §6.1.4"
verdict: clean
```

---

## §S3.I3.bg — Issue 3 Background: third-party-evaluator transparency; ML opacity; formal verification vs scenario testing vs red team; verification strength tiers

```yaml
# Lines 10222–10282 — Issue 3 Background: third parties (regulators, consumer
# advocates, ethicists, accident investigators, society) need transparency; ML
# data sets may be inaccessible, algorithms proprietary, mathematics complex,
# specifications opaque; formal verification (Fisher/Dennis/Webster 2013);
# scenario-based testing; "red team" devises norm-violating scenarios;
# verification strength tiers — strong (exhaustive coverage) vs weak (sampled);
# confidence must be qualified by strength; transparency necessary for
# accountability (to whom; who has right to correct; which A/IS subject)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:third_party_evaluation_access"
      score: 1.0
      confidence: 0.90
      context: >
        "A/IS should have sufficient transparency to allow evaluation by third
        parties, including regulators, consumer advocates, ethicists, post-accident
        investigators, or society at large." Direct mapping to transparency_log:*
        with third-party-evaluator scope — composes with Ch 2 §P5
        per_stakeholder_disclosure.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I3 lines 10237–10246"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:formal_verification_vs_scenario_vs_red_team"
      score: 1.0
      confidence: 0.85
      context: >
        Multiple verification techniques: formal verification (mathematical proof);
        scenario-based testing (sample criterion behaviors); "red team"
        adversarial-scenario generation. Method-level Family B claim — the
        verification-discipline plurality maps cleanly onto CIRIS conscience-faculty
        post-hoc checks + the F-3 detection family.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I3 lines 10264–10282"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 1.0
      confidence: 0.90
      context: >
        "An evaluation's concluding judgment must therefore acknowledge the
        strength of the verification technique used, and the expressed confidence
        in the evaluation—and in the A/IS themselves—must be qualified by this
        level of strength." Direct alignment with the epistemic_humility conscience
        faculty — verification-strength-tier disclosure as part of the claim
        envelope. Maps to the confidence field on every attestation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I3 lines 10250–10262"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:adversarial_red_team"
      score: 1.0
      confidence: 0.80
      context: >
        "A 'red team' may also devise scenarios that try to get the A/IS to break
        norms so that its vulnerabilities can be revealed." Adversarial-robustness
        method — composes onto key_boundary:adversarial_robustness (Ch 2 §P7.bg
        alignment).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I3 lines 10229–10232"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
verdict: composed
nuance_lost: |
  The accountability open-questions at lines 10271–10277 ("to whom the A/IS are
  accountable, who has the right to correct the systems, and which kind of A/IS
  should be subject to accountability requirements") are deliberately unresolved
  in the source text; they are research questions, not normative claims. Preserved
  by absent attestation rather than emitted as low-confidence claim. The strong-vs-
  weak verification tiering at lines 10242–10262 is a substantive epistemological
  scaffold; carried via amendable mutability + the conscience:epistemic_humility
  attestation. Specific verification-strength prefix would risk failing §1.10.1 T2
  (strength is a property of the verification, not a separate mechanism). No T-3.
```

---

## §S3.I3.r — Issue 3 Recommendation: design for strong verification + validation; accountability to communities

```yaml
# Lines 10293–10302 — Issue 3 Recommendation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:strong_verification_for_third_party_accountability"
      score: 1.0
      confidence: 0.90
      context: >
        "To maximize effective evaluation by third parties, e.g., regulators and
        accident investigators, A/IS should be designed, specified, and documented
        so as to permit the use of strong verification and validation techniques
        for assessing the system's safety and norm compliance, in order to achieve
        accountability to the relevant communities." Integrity-bound recommendation
        — design for evaluation strength; accountability is the ultimate aim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §S3.I3 Recommendation lines 10293–10302"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

# Chapter 9 Summary

### Per-unit verdict table

| Unit | Verdict | Primary prefix(es) |
|---|---|---|
| §Ch9.0 preamble (9117–9136) | composed | method:norm_identification_implementation_evaluation + witness_diversity:community_specific_norm_grounding |
| §Ch9.intro three goals (9158–9197) | composed | method:iterative_norm_lifecycle + transparency_log:norm_behavior_signals_to_community |
| **Section 1 — Identifying Norms** | | |
| §S1.0 preamble (9215–9233) | not-translated (T-2) | — |
| §S1.I1.bg (9237–9270) | composed | witness_diversity:community_norm_specificity + justice:human_rights_constrain_local_norms |
| §S1.I1.body (9268–9314) | composed | justice:lexical_vulnerability_priority + method:multi_disciplinary_empirical_norm_research + autonomy:individual_personalization_within_norms |
| §S1.I1.r (9281–9293) | clean | method:lifecycle_norm_identification_scientific |
| §S1.I2.bg (9333–9377) | composed | method:norm_update_capacities + conscience:epistemic_humility |
| §S1.I2.transparency (9362–9407) | composed | transparency_log:norm_change_consultation + non_maleficence:unreviewed_norm_learning + witness_diversity:representative_crowdsourced_panel |
| §S1.I2.r (9410–9416) | clean | method:transparent_norm_amendment |
| §S1.I3.bg (9398–9432) | composed | method:norm_priority_hierarchy + locality:decision:community |
| §S1.I3.override (9446–9484) | composed | non_maleficence:harm_priority_over_other_norms + prohibited:discrimination + method:democratic_norm_conflict_resolution + justice:international_principles_override_local_injustice |
| §S1.I3.r (9469–9482) | composed | method:norm_conflict_resolution_identification + transparency_log:conflict_resolution_to_third_parties |
| **Section 2 — Implementing Norms** | | |
| §S2.0 preamble (9610–9646) | clean | method:norm_implementation_evaluation_continuum |
| §S2.I1.bg (9619–9716) | composed | method:value_alignment_implementation_diversity + conscience:symbolic_gateway_check |
| §S2.I1.r (9731–9742) | clean | method:cross_school_collaborative_research |
| §S2.I2.bg (9804–9837) | composed | transparency_log:four_dimensional_decomposition + integrity:honest_design_no_capability_overrepresentation + prohibited:deception_fraud + method:formal_verification_for_norm_compliance |
| §S2.I2.r (9858–9866) | clean | transparency_log:high_transparency_constitutional_bound |
| §S2.I3.bg (9964–10026) | composed | non_maleficence:failure_inevitability_mitigation_design + progress_measure:multi_level_failure_metrics + method:systematic_risk_analysis + conscience:failsafe_gateway_strict_laws + transparency_log:public_incident_database |
| §S2.I3.r (10032–10038) | clean | method:multi_strategy_failure_mitigation |
| **Section 3 — Evaluating Implementation** | | |
| §S3.0 preamble (10060–10116) | composed | method:lifecycle_evaluation_anticipated_at_design + progress_measure:multi_dimensional_evaluation_criteria + witness_diversity:first_party_third_party_evaluation |
| §S3.I1 (10109–10141) | clean | method:differential_norms_human_vs_ais |
| §S3.I2.bg (10158–10208) | composed | prohibited:discrimination + detection:correlated_action:participation_exclusion:disadvantaged_groups |
| §S3.I2.body (10153–10208) | composed | witness_diversity:disadvantaged_group_inclusion + expertise:behavioral_scientists_and_target_populations |
| §S3.I2.r (10185–10191) | clean | method:bias_assessment_disadvantaged_group_integration |
| §S3.I3.bg (10222–10282) | composed | transparency_log:third_party_evaluation_access + method:formal_verification_vs_scenario_vs_red_team + conscience:epistemic_humility + key_boundary:adversarial_red_team |
| §S3.I3.r (10293–10302) | clean | integrity:strong_verification_for_third_party_accountability |

### Unit count and verdict distribution

Total atomic units processed: **25**.

| Verdict | Count | % |
|---|---|---|
| clean | 9 | 36% |
| composed | 15 | 60% |
| partial | 0 | 0% |
| not-translated (T-1) | 0 | 0% |
| not-translated (T-2) | 1 | 4% |
| **clean+composed total** | **24/25** | **96%** |

This is high clean+composed density. **0 T-1** is correct for a secular,
engineering-society document. **0 T-3** confirms the chapter's value-alignment
technical-implementation content composes onto existing v1.4 primitives —
specifically the conscience-faculty stack + the PDMA principle-anchoring
infrastructure + witness_diversity + transparency_log + the v1.3 locality and
lexical-vulnerability primitives. 1 T-2 (the bare section-preamble enumeration at
§S1.0, which correctly stays in prose).

### T-3 candidates

**0 new T-3 EXPRESSIVE_GAP** emerged from Chapter 9. Composition-before-extension
held throughout. Specifically:

- **§S2.I1.bg — "symbolic gateway agent" / "Ethical Governor" / "Guardian"
  architecture**: anticipated as a likely T-3 surface (per prompt). Closed by
  composition: maps directly onto `conscience:*` faculties (Optimization Veto,
  Entropy, Coherence, Epistemic Humility) — the framework's instantiation of
  post-action-selection symbolic checks. No new prefix needed.

- **§S2.I3.bg — fail-safe components with "strict laws" that should never be
  violated**: composes cleanly onto `conscience:*` + `prohibited:*` hard
  constraints. The "never-violate strict laws" are the federation's `prohibited:*`
  family (22 NEVER_ALLOWED categories); the "continuously monitor operations"
  shape is conscience-faculty post-hoc verification.

- **§S2.I1.bg — A/IS that "can learn to detect and take into account others' pain
  and pleasure"** (lines 9712–9716): affective-computing-adjacent claim. NOT
  load-bearing in this chapter — the Ch 5 Affective Computing T-3 surface (per
  manifest.yaml line 60) is where any `affective:*` family proposal would be
  load-bearing. Flagged for the Ch 5 subagent.

- **§S1.I2.bg — "norm update capacities" (4-item enumeration)**: anticipated as a
  possible value-learning T-3. Closed by composition: the four capacities are
  refinements within one `method:*` envelope (composition-before-extension §8.5.2);
  the uncertainty-asking capacity composes directly onto `conscience:epistemic_humility`.

- **§S3.I3.bg — "strong vs weak verification tier" claim**: substantive
  epistemological scaffold but composes onto the existing `confidence` field on
  every attestation envelope + the `epistemic_humility` conscience faculty. A
  dedicated verification-strength prefix would fail §1.10.1 T2 (strength is a
  property of the verification, not a separate mechanism).

- **§S3.I3.bg — accountability open-questions** ("to whom; who has right to
  correct; which A/IS subject to requirements"): explicitly unresolved in the
  source as research questions, not normative claims. Carried by absent
  attestation — not a T-3.

The Ch 5 Affective Computing T-3 surface (per manifest) remains the expected
chapter-level T-3 emission location for the IEEE EAD batch — not Ch 9.

### Cultural-particularity claims — composition onto witness_diversity + pdma_framing §III

The chapter recurrently flags cultural particularity of norms:

- "norms of the specific community" (§Ch9.0, §S1.I1.bg, §S1.I1.body, §S1.I1.r)
- "diverse cultural norms" (Ch 2 §P1.r echoed at §S1.I1)
- "communities ranging from families to whole nations differ" (§S1.I1.bg)
- "broadly observed norms of communities in which a technology is deployed"
  (§S1.I1.bg)

All compose onto `witness_diversity:community_specific_norm_grounding` +
`witness_diversity:community_norm_specificity` + the `pdma_framing.yml §III
multi-tradition` reference. The framework's polyglot principle anchoring (ahimsa,
seva, alētheia, chesed, amae, ma'at, imago Dei, fitra, jeong, tikkun olam,
sammā-vācā) substantively absorbs the cultural-particularity claim. No new prefix
needed — composition-before-extension confirmed.

### Per-Section coverage table

| Section | Primary CIRIS families | Coverage | T-3 |
|---|---|---|---|
| **Preamble (Ch9.0 + Ch9.intro)** | method:* (lifecycle anchor) + witness_diversity:* (cultural particularity) + transparency_log:* (signals) | 2/2 = **100%** | none |
| **Section 1 — Identifying Norms** | justice:* (human rights constraint; lexical-vulnerability; international-override) + witness_diversity:* (community + diverse panel) + autonomy:* (individual within community) + non_maleficence:* (harm-priority; unreviewed-learning-as-harm) + prohibited:discrimination (community-override) + transparency_log:* (norm-change consultation; conflict resolution) + locality:decision:community + conscience:epistemic_humility + method:* (lifecycle; updating; conflict-resolution) | 8/9 = **89%** clean+composed (1 T-2 section preamble) | none |
| **Section 2 — Implementing Norms** | method:* (multiple approaches; risk analysis; mitigation) + conscience:* (gateway check; failsafe + strict laws) + transparency_log:* (4-D decomposition; high-transparency constitutional bound; incident database) + integrity:* (honest design) + prohibited:deception_fraud + non_maleficence:* (failure inevitability) + progress_measure:* (multi-level metrics) | 7/7 = **100%** | none |
| **Section 3 — Evaluating** | method:* (lifecycle; differential norms; verification techniques; bias assessment) + progress_measure:* (multi-dimensional criteria) + witness_diversity:* (first-party + third-party; disadvantaged-group inclusion) + prohibited:discrimination + detection:correlated_action:* (population-scale bias) + expertise:* (behavioral scientists + target populations) + transparency_log:third_party_evaluation_access + conscience:epistemic_humility + key_boundary:adversarial_red_team + integrity:strong_verification | 7/7 = **100%** | none |

### Cross-document correspondence — load-bearing comparison axis

EAD1e Ch 9 (Embedding Values) vs counterpart sections in *Magnifica Humanitas*,
EU HLEG, and (future) ASEAN:

| EAD1e §Ch9 cluster | EU HLEG counterpart | Magnifica Humanitas (where mapped) | Primary shared prefix |
|---|---|---|---|
| §Ch9.0 + §Ch9.intro — norms as community-specific | §1.5 Diversity/non-discrimination + Ch I 4 principles | MH CH3 §90+ (technology grounded in human dignity) | witness_diversity:* + method:* |
| §S1.I1 — vulnerable + underrepresented groups | §1.5.b Accessibility / universal design | MH CH4 (vulnerable persons centring) | justice:lexical_vulnerability_priority |
| §S1.I2 — norm updating with transparency + consultation | §1.7 Accountability + §1.4 Communication | MH CH3 §103 (disclosure) | transparency_log:* + witness_diversity:* |
| §S1.I3 — norm conflict + community-override + democratic resolution | §2 Methods for trustworthy AI (technical + non-technical) | MH CH3 §117 (manipulation refusal) + locality | non_maleficence:* + prohibited:discrimination + method:democratic_resolution |
| §S2.I1 — multiple value-alignment architectures | §1.7.c Trade-offs + §2 methods | (limited MH parallel) | method:* + conscience:symbolic_gateway_check |
| §S2.I2 — four-dimensional transparency | §1.4 Transparency (traceability + explainability + communication) | MH CH3 §103 | transparency_log:* (anchor); extends Ch 2 §P5 three-D to four-D |
| §S2.I3 — failures + multi-strategy mitigation | §1.2 Technical robustness + §1.7.b negative-impact-minimisation | MH CH3 (technology fallibility framing) | non_maleficence:* + conscience:failsafe + transparency_log:incident_database |
| §S3 — evaluation lifecycle + third-party access | §3 Assessment List for Trustworthy AI (ALTAI) | (limited MH parallel) | progress_measure:* + witness_diversity:first_party_third_party + transparency_log:third_party_access |

Each is a **STRONG-tier alignment candidate** per GOVERNANCE_FABRIC_MAPPING_STANDARD
§4.1. The §S2.I2 four-dimensional transparency decomposition vs §P5 three-dimensional
decomposition is a productive cross-source extension — EAD1e adds "honest design"
as a fourth dimension; this may be a load-bearing harmonization opportunity for
the future multi-source overlap analysis at §7.5.

### Strongest single envelopes (most-demanding claims with cleanest wire rendering)

- §S2.I2.r `transparency_log:high_transparency_constitutional_bound` — single
  dimension at species scope, constitutional mutability, encoding the four-D
  decomposition (traceability + verifiability + honest design + intelligibility)
  as binding.
- §S2.I3.bg `conscience:failsafe_gateway_strict_laws` — direct structural mapping
  of the "Ethical Governor" / "Guardian" architecture onto the CIRIS conscience-
  faculty stack + prohibited:* hard constraints; constitutional mutability.
- §S1.I1.body `justice:lexical_vulnerability_priority` — direct invocation of
  the v1.3 §6.1.4 consumer policy; constitutional mutability.
- §S1.I3.override composition (`non_maleficence:harm_priority_over_other_norms` +
  `prohibited:discrimination` + `justice:international_principles_override_local_injustice`)
  — three-way composed bound encoding the chapter's deepest claim: communities
  may not over-rule constitutional protections via local norms.

### Most-cited prefix families across the chapter

- `method:*` (15 attestations) — Family B operational spine across all three sections
- `transparency_log:*` (8 attestations) — multi-stakeholder transparency at every section
- `conscience:*` (5 attestations) — gateway-check + failsafe + epistemic_humility +
  symbolic-gateway; the chapter's deepest CIRIS alignment is here
- `witness_diversity:*` (6 attestations) — cultural-particularity + multi-stakeholder +
  disadvantaged-group inclusion
- `non_maleficence:*` (3 attestations) — unreviewed-learning-as-harm + harm-priority +
  failure-inevitability
- `prohibited:*` (3 attestations) — discrimination ×2 + deception_fraud (hard constraints)
- `justice:*` (3 attestations) — lexical-vulnerability + UDHR-constrains-norms +
  international-override
- `progress_measure:*` (3 attestations) — multi-level failure metrics +
  multi-dimensional evaluation criteria
- `integrity:*` (2 attestations) — honest design + strong verification
- `autonomy:*` (1 attestation) — individual personalization within community bounds
- `expertise:*` (1 attestation) — behavioral scientists + target populations
- `locality:decision:community` (1 attestation) — local conflict resolution
- `detection:correlated_action:*` (1 attestation) — population-scale bias
- `key_boundary:adversarial_red_team` (1 attestation)

### Calibration paragraph

This chapter translates very cleanly into the v1.4 wire format. ~96% clean+composed
density. 0 T-1 (correct — EAD1e is secular). 0 T-3 (the chapter-level T-3 surface
in IEEE EAD per manifest is Ch 5 Affective Computing, not Ch 9). 1 T-2 (the bare
section preamble at §S1.0). Composition-before-extension held throughout — every
operational claim mapped onto existing v1.4 primitives. The chapter's "value
learning / norm learning specific technical proposals" — `Ethical Governors`,
`Guardians`, symbolic-gateway checks, fail-safe components, four mitigation
strategies — composed cleanly onto `conscience:*` + `prohibited:*` + `method:*`
+ `attestation:l3:*`. The federation framework's conscience-faculty stack
(Entropy / Coherence / Optimization Veto / Epistemic Humility) is the structural
analogue of EAD1e's gateway / guardian architecture; the prohibited:* family is
the structural analogue of EAD1e's "strict laws that should never be violated."
The cultural-particularity claims (norms are community-grounded; communities
differ; diverse cultural norms) all compose cleanly onto witness_diversity:* +
the pdma_framing.yml §III multi-tradition polyglot anchoring (ahimsa, seva,
alētheia, chesed, amae, ma'at, imago Dei, fitra, jeong, tikkun olam,
sammā-vācā) — the framework's substantive richness in this area absorbs the
document's cultural-pluralism claim without straining.

The four-dimensional transparency decomposition at §S2.I2 (traceability /
verifiability / honest design / intelligibility) extends Ch 2 §P5's three-dimensional
decomposition (traceability / explainability / interpretability) — "honest design"
is the EAD1e-distinctive fourth dimension, encoded as
`integrity:honest_design_no_capability_overrepresentation` + composed with
`prohibited:deception_fraud`. This is a productive structural elaboration; the
framework's existing `integrity:*` + `prohibited:*` families carry the load
adequately, but the four-D decomposition is preserved as load-bearing context
for the cross-source overlap analysis.

The primary nuance lost across the chapter is the substantive philosophical
underpinning — Hitlin/Piliavin, Malle/Dickert, Rohan, Sommer on what "values"
are; Wallach/Allen on top-down/bottom-up/hybrid; Van den Hoven on moral
overload; Andre/Velasquez on Common Good Principle; Schwartz value theory;
Friedman/Kahn/Borning/Huldtgren Value Sensitive Design. These are preserved
only via evidence_refs and are not emitted as separate delegates_to
authority-source attestations; a richer mapping (likely worth doing in Phase 3
of the IEEE EAD batch) would emit per-citation delegates_to to preserve the
graph-level reading of the substantive philosophical heritage the chapter draws
on. The "asymmetric A/IS vs human norms" claim at §S3.I1 (the document
stipulates rather than argues the asymmetry) is framework-side thinner than
CIRIS's M-1 substrate-agnostic + Recursive-Golden-Rule + originator-relational
posture — but this is a mismatch on the source side, not a T-3 against the
framework.

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH09_EMBEDDING_VALUES.md**
