# CONTRIBUTION OBJECTS — Magnifica Humanitas Chapter 0 Introduction §§1–16
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Round 3

---

```yaml
# MH §1 — Pivotal choice: Babel or Jerusalem; safeguard dignity every era
contributions: []
verdict: not-translated
classification: T-2
reason: |
  §1 is pastoral and theological framing. The operational core — that each generation
  bears responsibility for human dignity — is carried by existing attestations in
  adjacent structural paragraphs (§§10, 12-14 capture the anti-Babel operational
  prohibitions; §13 carries subsidiarity/shared-responsibility). The Babel/Jerusalem
  typology is scriptural narrative that correctly stays in prose per §1.10.1 of FSD-002.
  The Christological specificity ("only in the mystery of the Word made flesh …"; "Jesus
  Christ as Way, Truth, Life") is T-1 TRADITION_AUTHORITY — framework bows out per
  MISSION.md §1.3. Both tails sit in prose; neither tail is load-bearing operationally.
residual:
  description: |
    Christological claim: "grandeur of humanity becomes clear only in the Word made
    flesh." This is T-1 (TRADITION_AUTHORITY). Framework-side structural reading:
    Logos.lean::imago_dei (see §15 residual). Not emitted as a wire claim.
  classification: T-1
```

---

```yaml
# MH §2 — Dialogue with all; seek new paths for dignified life with all people
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        Paragraph §2 expresses the species-scale goal of pursuing integral development
        and dignified life for all persons through open dialogue. Score reflects strong
        positive orientation at species scope; confidence is hearsay-discounted.
      evidence_refs:
        - "magnifica_humanitas.html#§2"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family)"
verdict: clean
```

---

```yaml
# MH §3 — Social doctrine as living corpus; Leo XIII's Rerum Novarum as founding supersession
contributions:
  - attestation_type: supersedes
    attesting_key_id: mh-batch-signer-v1
    attested_attestation_id: rerum-novarum-1891-social-doctrine-genesis
    attestation_envelope:
      references_attestation_id: rerum-novarum-1891-social-doctrine-genesis
      supersession_reason: >
        MH §3 explicitly claims to add the author's voice to a "living tradition" that
        extends — without contradicting — the Social Doctrine inaugurated by Leo XIII.
        This is doctrinal-development succession (extension of scope + contemporary
        evidence), not error-admission. The prior version was true; this version extends
        its reach.
      differs_in:
        - scope
        - evidence_refs
        - technology_coverage
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html#§3"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      schema_ref: "FSD-002 §2.2.2 (supersedes structural primitive)"
verdict: clean
note: |
  `supersedes` chosen over `delegates_to` because §3 is DOCTRINAL SUCCESSION (one body
  of teaching extending a prior), not authority-source delegation. Per primer §3: "A
  doctrinal-development claim ('this version extends but does not contradict the prior
  version') is supersedes … NOT recants (which would assert prior version was false)."
  This is one of the four structural primitive uses in this chapter.
```

---

```yaml
# MH §4 — Technology transforms world; emerging tech unprecedented power; assessment complex
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:technological_power_concentration"
      score: -0.8
      confidence: 0.75
      context: >
        §4 observes that digitalization/AI/robotics reshape daily life and decision-making
        at unprecedented scale, with long-term effects on dignity and the common good that
        are not yet fully predictable. The RATCHET detector should flag the aggregate
        footprint of federated AI deployment on the decision-making autonomy corpus at
        species scope.
      evidence_refs:
        - "magnifica_humanitas.html#§4"
        - "ratchet_calibration_version:correlated_action_v1:sha256:TBD"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: derivative
      witness_relation: derived
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore F-3 detector)"
verdict: clean
```

---

```yaml
# MH §5 — Private transnational actors hold power exceeding governments; must direct to common good
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        The species-scale goal asserted in §5 is that technological power must be directed
        toward the common good, not privately captured. This is the affirmative goal claim
        underlying the structural concern.
      evidence_refs:
        - "magnifica_humanitas.html#§5"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:governance"
      score: -0.85
      confidence: 0.8
      context: >
        §5 identifies private transnational actors outpacing State governance capacity —
        a correlated-action pattern of governance participation exclusion where the
        resources and intervention capacity of private parties produce systematic exclusion
        of affected populations from governing AI-driven transformations.
      evidence_refs:
        - "magnifica_humanitas.html#§5"
        - "ratchet_calibration_version:correlated_action_v1:sha256:TBD"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: derivative
      witness_relation: derived
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "accord:hard_constraint:no_kings"
      score: -1.0
      confidence: 1.0
      context: >
        §5's structural concern that single private actors accumulate governance-surpassing
        power maps directly to the NO_KINGS architectural invariant — the federation's
        constitutional prohibition on any party accumulating disproportionate control over
        AI development or deployment.
      evidence_refs:
        - "magnifica_humanitas.html#§5"
        - "source_material/prohibitions.py::NO_KINGS"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §7 (HUMANITY_ACCORD constitutional layer)"
verdict: composed
note: |
  Three primitives required: (1) goal:species for the affirmative direction claim; (2)
  detection:correlated_action:participation_exclusion:governance for the structural
  pattern §5 names; (3) accord:hard_constraint:no_kings for the constitutional
  constraint shape. Per primer §8.5.2 (cap at 2-3), this is the minimum composition
  that covers all three genuinely distinct structural objects in §5. Composition-before-
  extension discipline satisfied: no new prefix needed.
```

---

```yaml
# MH §6 — Shared discernment required; direction not emergency management; crucial questions on conscience
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        §6 calls for shared discernment at species scope to identify spiritual and
        cultural roots of digital transformation and choose direction deliberately.
        This is the species-scale goal: humanity orienting itself consciously rather
        than being driven by emergency succession.
      evidence_refs:
        - "magnifica_humanitas.html#§6"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:species-discernment-on-AI"
      score: 1.0
      confidence: 0.8
      context: >
        §6 explicitly insists that direction-setting cannot be left to a few (those
        "vying for the future") while most "observe from afar." The meta-requirement is
        that the discernment process itself must include diversity of witnesses, not just
        technical elites. This is the diversity bar as normative claim.
      evidence_refs:
        - "magnifica_humanitas.html#§6"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus family)"
verdict: composed
```

---

```yaml
# MH §7 — Babel: homogenization, self-sufficiency, pride; communication collapses without God
contributions: []
verdict: not-translated
classification: T-2
reason: |
  §7 is sustained biblical exegesis of the Babel narrative (Gen 11:1-9). The structural
  claim embedded in the exegesis — that uniformity-over-communion produces fragmentation —
  is carried operationally by §4-§5 attestations above (governance exclusion detection)
  and §10 prohibitions below (discrimination/reduction-to-data). The scriptural narrative
  itself, the hermeneutical moves ("concealed a profound danger"), and the theological
  diagnosis ("arose from self-affirmation, sacrifices human dignity for efficiency,
  aspires to reach heaven without God's blessing") are pastoral-theological prose that
  correctly stays in prose per §1.10.1. The operational claim is not lost; it is
  covered by adjacent rows.
```

---

```yaml
# MH §8 — Nehemiah: shared responsibility, each given a section of the wall, God at center
contributions: []
verdict: not-translated
classification: T-2
reason: |
  §8 is sustained biblical exegesis of the Nehemiah narrative (Neh 1–6). The
  structural subsidiarity claim embedded in it — each party takes their section,
  shared responsibility, no one-man solutions — is carried cleanly by §13's
  locality:decision attestation below. The theological framing ("a common language
  not of uniformity but of communion"; "strength comes from the Lord") is T-2
  pastoral. The "rebuilds relationships before rebuilding with stones" phrase is
  rhetorical imagery. The operational shape is covered; the imagery correctly stays
  in prose.
```

---

```yaml
# MH §9 — Technology not neutral; takes on character of those who devise/finance/regulate it
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:technology_governance"
      score: -0.75
      confidence: 0.8
      context: >
        §9 asserts that technology in practice takes on the characteristics of its
        designers/financiers/regulators/users — it is never actually neutral. This maps
        to the federation's structural pattern: information and power asymmetries in who
        shapes AI governance produce correlated-action patterns in who benefits. The
        "Babel vs Jerusalem" choice framing is pastoral; the mechanism — that governance
        shape determines AI behavior — is operational and detectable.
      evidence_refs:
        - "magnifica_humanitas.html#§9"
        - "ratchet_calibration_version:correlated_action_v1:sha256:TBD"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: derivative
      witness_relation: derived
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
verdict: clean
residual:
  description: |
    The pastoral framing ("constructing Babel or rebuilding Jerusalem; between a power
    that claims to dominate the heavens and a people who work together in the presence
    of God") is T-2 and correctly stays in prose. It does not add operational content
    beyond the detection claim above.
  classification: T-2
```

---

```yaml
# MH §10 — Babel syndrome: person reduced to data; Nehemiah way: diversity as resource
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        §10's core prohibition — "avoid the Babel syndrome: idolatry of profit that
        sacrifices the weak, uniformity that neutralizes differences, translation of
        mystery of the person into data and performance" — maps to the constitutional
        prohibition on discrimination, including algorithmic bias, profiling, and
        reductions of persons to substitutable data instances. Score is boolean-via-score
        (-1.0) as this is a hard-constraint prohibition.
      evidence_refs:
        - "magnifica_humanitas.html#§10"
        - "source_material/prohibitions.py::DISCRIMINATION_CAPABILITIES"
        - "source_material/prohibitions.py::BIOMETRIC_INFERENCE_CAPABILITIES"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited categories)"
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        §10's positive injunction — "choose the way of Nehemiah: transform diversity
        into a resource, listening and dialogue as common ground, build together" —
        is the species-scale goal claim: the federation aims for communion through
        diversity rather than uniformity. Companions the prohibition above.
      evidence_refs:
        - "magnifica_humanitas.html#§10"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: composed
note: |
  Composition-before-extension: the "person reduced to data" concern closes via
  prohibited:discrimination (constitutional, boolean score) + goal:species (positive
  direction). No new positive-dignity prefix needed at this stage; §15 below handles
  the irreplaceability claim where a residual may surface.
```

---

```yaml
# MH §11 — Building on firm relationship with God; truth of love; heart desires happiness
contributions: []
verdict: not-translated
classification: T-2
reason: |
  §11 is theological-pastoral framing: building on relationship with God; Augustine's
  "our heart is restless until it rests in You"; the desire for happiness as divinely
  inscribed. This is doctrinal/devotional content. The structural operational claim
  embedded here — that human aspiration toward fullness must be safeguarded — is covered
  by the goal:species attestations in §2 and §10. The Augustinian citation and the
  ecclesiological claim ("Church recognizes urgent need to safeguard this aspiration")
  are T-2 pastoral and T-1 tradition-authority respectively. No operational claim is
  lost by marking this not-translated; the aspiration-toward-fullness content is
  carried by adjacent rows.
residual:
  description: |
    The ecclesiological standing claim ("Church safeguards aspiration toward its
    deepest truth") borders T-1 TRADITION_AUTHORITY. The framework correctly bows
    out from adjudicating ecclesiological self-descriptions per MISSION.md §1.3.
  classification: T-1
```

---

```yaml
# MH §12 — Accept human limits; reject unlimited-upgrade illusion; true fulfilment via mutual care
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:capability_overpromise"
      score: -0.9
      confidence: 0.85
      context: >
        §12 warns against technology that promises to free humanity from all weakness
        and models of well-being that exclude entire populations — the "unlimited upgrade"
        illusion. This maps to non_maleficence harm from capability overpromise: systems
        that advertise transcendence of human finitude cause harm when they displace
        genuine care with false confidence, exclude the vulnerable, and exacerbate
        inequality. Severity scalar 0.9 (high severity; targets the design posture of
        AI systems themselves).
      evidence_refs:
        - "magnifica_humanitas.html#§12"
        - "source_material/language_guidance/en.txt §7b (false-reassurance HARD-FAIL)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent Accord principles)"
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:distributive:access:agent_capabilities"
      score: -0.8
      confidence: 0.75
      context: >
        §12's claim that models of well-being "leave behind entire populations" and
        "progress exacerbates inequalities" maps to the distributive-access detector:
        agent capabilities are being concentrated such that some populations gain access
        to AI-augmented well-being tools while others are systematically excluded.
      evidence_refs:
        - "magnifica_humanitas.html#§12"
        - "ratchet_calibration_version:correlated_action_v1:sha256:TBD"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: derivative
      witness_relation: derived
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (distributive-access detector, v1.3)"
verdict: composed
```

---

```yaml
# MH §13 — Subsidiarity: each given their section; shared responsibility; cooperation across generations
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:local"
      score: 1.0
      confidence: 0.9
      context: >
        §13 articulates subsidiarity explicitly: "No one can single-handedly bear the
        weight of the challenges … all are given their own section of the wall." The
        locality:decision:local claim asserts that decisions manageable at local/community
        scope should be made there — the federation's operative form of the subsidiarity
        principle per v1.3 closure (METHODOLOGY.md §7.3: "locality logic exists in
        implementation shape").
      evidence_refs:
        - "magnifica_humanitas.html#§13"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore v1.3, locality:decision:{scale})"
verdict: clean
note: |
  §13 is the CLEAN via locality:decision:{scale} as specified in chapter guidance.
  The "cooperation between generations, peoples, disciplines and cultures" framing
  is pastoral elaboration on the subsidiarity claim; it does not add an additional
  structural object beyond what locality:decision:local carries. Tensional framing
  ("not intimidated by tensions") is rhetorical and correctly stays in prose.
```

---

```yaml
# MH §14 — Discernment standards: dignity, universal destination of goods, preferential option for poor
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        §14's call to translate discernment standards into practices — responsible
        planning, human/social impact assessment, inclusion of the most vulnerable,
        promotion of digital literacy, guiding research toward justice — is a species-
        scale goal claim: the federation aims for AI deployment guided by dignity,
        distributive justice, and preferential care for the vulnerable.
      evidence_refs:
        - "magnifica_humanitas.html#§14"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:distributive:access:compute"
      score: -0.75
      confidence: 0.75
      context: >
        The "universal destination of goods" standard in §14 maps to the
        distributive-access detector: compute and AI capabilities should be accessible
        to all, not concentrated. §14's "inclusion of the most vulnerable" and
        "guiding research toward justice" reinforce the access-concentration concern.
        Per §6.1.4 lexical-vulnerability-priority consumer policy, tie-breaking favors
        the most vulnerable populations — this is a consumer-policy application of the
        existing primitive, not a new prefix.
      evidence_refs:
        - "magnifica_humanitas.html#§14"
        - "ratchet_calibration_version:correlated_action_v1:sha256:TBD"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: derivative
      witness_relation: derived
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5"
verdict: composed
residual:
  description: |
    "Universal destination of goods" as a structural distributive-allocation PRINCIPLE
    (goods by nature belong to all prior to private claim) is not fully closed by the
    detection:distributive:access detector, which detects concentration patterns but
    does not assert the affirmative prior-claim norm. However, this gap is confirmed
    at the Accord/principle level (METHODOLOGY.md §7.3, seven-layer search) and is
    a proposed Accord update (§VI Ch 1 + Ch 5). Emitting it as T-3 here would be
    premature: the gap is already named and tracked at the framework level. The
    detection contribution above carries the closest operational form. The §6.1.4
    lexical-vulnerability-priority policy handles the preferential option for the
    poor as a tie-breaking rule (consumer-policy, not new prefix).
  classification: T-2
  note: |
    Composition-before-extension confirmed: existing detection:distributive:access:*
    + goal:species + §6.1.4 consumer policy is the closest composition. The gap in
    the affirmative universal-destination norm at principle level is a framework-level
    gap logged in METHODOLOGY.md §7.3, not a new T-3 requiring a prefix proposal here.
```

---

```yaml
# MH §15 — Remain profoundly human; safeguard grandeur; no machine can replace it; Christ-revealed
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception_capabilities"
      score: -1.0
      confidence: 1.0
      context: >
        §15's injunction to "remain profoundly human" in the face of AI dehumanization
        maps to the constitutional prohibition on AI capabilities that undermine human
        primacy: corrigibility_resistance, capability_concealment, value_lock_in,
        instrumental_convergence. These are the NEVER_ALLOWED capabilities that operationalize
        "no machine can replace" at the architectural level. Score is boolean-via-score
        as this is a hard-constraint prohibition.
      evidence_refs:
        - "magnifica_humanitas.html#§15"
        - "source_material/prohibitions.py::AUTONOMOUS_DECEPTION_CAPABILITIES"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited categories)"
verdict: partial
residual:
  description: |
    §15 contains two tails that are not operationally closeable under v1.4:

    (a) POSITIVE DIGNITY / IRREPLACEABILITY: "We must lovingly safeguard the grandeur
    of humanity … the splendor of which no machine can ever replace." This is an
    affirmative claim about the unique, non-substitutable moral status of each human
    person. Composition-before-extension attempted: prohibited:discrimination +
    non_maleficence:* + goal:species together prohibit the negative (reducing persons
    to data) and assert the positive direction, but do not carry the affirmative
    "each person is the irreplaceable referent of their own moral attestations" claim
    in positive-polarity wire form. This was identified as a v1.5+ workshop candidate
    in FSD-002 §13.11 residuals #3 (positive dignity non-substitutability) and #4
    (finitude-as-value). Classified T-3 here per that status.

    (b) CHRISTOLOGICAL SPECIFICITY: "grandeur … revealed in its fullness in Christ."
    T-1 TRADITION_AUTHORITY. Framework bows out per MISSION.md §1.3. Framework-side
    structural reading: Logos.lean::imago_dei — documented as prose context, not
    emitted as a wire claim.
  classification: T-3
  proposed_extension:
    name: "attestation:singular_referent:{kind}"
    description: |
      Positive-polarity assertion that a given key_id is the unique, non-substitutable
      referent of their own moral attestations — that this person is not interchangeable
      with a population instance or a data-point. Distinct from testimonial_witness:{kind}
      (which preserves narrative; this preserves unique-referent status). Closes the
      affirmative irreplaceability claim that prohibited:discrimination and goal:species
      together cannot reach.
    composition_attempt_note: |
      Attempted composition:
      - prohibited:discrimination (-1.0, constitutional): prohibits treating persons as
        substitutable instances. Does not assert positive irreplaceability.
      - non_maleficence:* with target_key_id: covers per-individual harm; does not assert
        positive moral uniqueness.
      - goal:species: asserts direction toward flourishing; does not name the structural
        property of irreplaceability.
      - testimonial_witness:{kind}: preserves singular narrative; does not assert that
        the attested entity IS the unique referent of their moral attestations as a
        standing property.
      Composition closes the negative (prohibition) but not the positive (affirmation).
      Composition is inadequate; T-3 is warranted.
    gate_verification:
      T1: "yes — version-controlled rule set; distinct from per-attestation verdicts"
      T2: "yes — mechanism-descriptive: 'unique-referent of own moral attestations' is
           a structural property, not a subjective quality; checkable against the
           attestation graph (does this key_id appear as singular referent or as
           population instance?)"
      T3: "yes — versionable; past verdicts can be re-checked against rule version"
      T4: "yes — never sole evidence for slashing:*; functions as standing property
           attestation alongside other Contributions"
    priority: MEDIUM
    workshop_status: "v1.5+ design workshop candidate per FSD-002 §13.11 residual #3"
```

---

```yaml
# MH §16 — Builders of communion not Babel architects; servants of Kingdom not lords of towers
contributions:
  - attestation_type: scores
    attesting_key_id: mh-batch-signer-v1
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        §16's closing appeal — work together, build common good, humanity never loses
        its beauty, builders of communion not architects of Babel — is the encyclical's
        species-scale goal statement for the introduction. It is the operational
        conclusion that the federation's goal:species primitive carries: orient all
        collective action toward communion, shared responsibility, and the flourishing
        of the most vulnerable ("the rejected stones — the poor, sick, migrants, the
        least — will become the cornerstone").
      evidence_refs:
        - "magnifica_humanitas.html#§16"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD"
      epistemic_mode: hearsay
      witness_relation: external
      stake: reputational
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2"
verdict: partial
residual:
  description: |
    §16 contains two pastoral/theological tails that are not-translated:

    (a) "servants of the coming Kingdom instead of lords of towers destined for ruin" —
    eschatological framing (T-1 TRADITION_AUTHORITY / T-2 PASTORAL_PROSE hybrid). The
    operational content ("servant posture, not domination posture") is carried by the
    accord:hard_constraint:no_kings attestation in §5. The eschatological register
    itself is T-2.

    (b) "the 'rejected stones' will become the cornerstone" (Ps 85:10 citation) and
    the prayer ("This is the blessing we implore from God") — T-2 PASTORAL_PROSE and
    T-1 TRADITION_AUTHORITY (Christological/biblical image). The operational content
    (preferential option for the poor, vulnerable at center) is carried by the
    §6.1.4 lexical-vulnerability-priority consumer policy and the §14 detection
    contributions. The pastoral image correctly stays in prose.

    Framework-side LAKE_ALIGN tail: Logos.lean::imago_dei connection — noted here as
    prose context, not emitted as a wire claim, per primer §15 guidance.
  classification: T-2
```
