# CONTRIBUTION_OBJECTS_CH1_DOCTRINE.md
# Chapter 1: A Dynamic Approach Faithful to the Gospel (§§17–45)
# CIRIS Federation Wire Envelopes — Round 2

**Version**: 2.0 (actual wire objects; not prose sketches)
**Date**: 2026-05-27
**Grammar**: LANGUAGE_PRIMER.md v2; §12 output format; §9.10 template for delegates_to reuse
**Source**: *Magnifica Humanitas* §§17–45 (HTML lines 626–662)
**Wire spec**: FSD-002_FEDERATION_SURFACE.md v1.2; IDMA idma.yml; NodeCore MISSION.md P12–P15

---

## §§17–21 — Church journeying through history; autonomy of earthly realities

---

```yaml
# MH §17 — Social Doctrine must develop in fidelity to Gospel; AI challenges categories from within
contributions:
  - kind: Attestation
    attestation_type: "delegates_to:accord_v{N+1}:from:accord_v{N}"
    envelope:
      target_attestation_id: "<prior accord-version attestation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §17)"
        - "FSD-002 §4.9.2 (calibration-amendment discipline: federation Contribution + WA quorum)"
        - "Accord auto-expire discipline (heuristics carry validity_window + renewal policy)"
      schema_ref: "FSD-002 §2.2.1 (delegates_to as structural version-chaining primitive)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "integrity:doctrinal_continuity"
    envelope:
      target_key_id: "<accord version chain>"
      polarity: Positive
      score: 0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §17)"
        - "FSD-002 §4.9.2 (public comment window before each calibration-package version transition)"
        - "Accord auto-expire 2027-04-16 + renewal discipline"
      cohort_scope: federation
      schema_ref: "FSD-002 §2.2.1; Accord Book I"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "In fidelity to the Gospel" — the Gospel as authoritative grounding source is T-1
  (TRADITION_AUTHORITY). The delegates_to reuse pattern (FSD-002 §2.2.1) is the
  framework's structural form of authority-source continuity claims without importing
  tradition-specific vocabulary into the wire. The operational content (doctrine
  develops through versioned amendment, not rupture) is fully wire-carried.
```

---

```yaml
# MH §18 — Social Doctrine must not appear as external ethics imposed from above; stems from accompaniment
contributions:
  - kind: Attestation
    attestation_type: "autonomy:non_interference"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §18)"
        - "ACCORD_M-1 (corridor; not prescriptive; each agent pursues own flourishing)"
        - "PDMA Step 5 (relational-balance check: service posture, not domination posture)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1 (autonomy:* family)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §18)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      issued_at: "<runtime>"
      mutability: constitutional
verdict: composed
residual: |
  "A Church that walks alongside humanity" — ecclesiological accompaniment framing is
  T-2 (PASTORAL_PROSE). The structural non-domination / non-imposition claim is
  carried via autonomy:non_interference (Positive) + prohibited:manipulation_coercion
  (Negative polarity constitutional leaf).
```

---

```yaml
# MH §19 — Church actively participates in building just, fraternal society; mission has historical scope
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §19)"
        - "ACCORD_M-1 (diverse sentient beings may pursue their own flourishing)"
        - "PDMA Step 2 (dma:pdma:beneficence + dma:pdma:justice signed)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12 (goal:{scale} primitive)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:commons:multilingual:ecosystem_health"
    envelope:
      target_key_id: "<federation contributors>"
      polarity: Positive
      score: <continuous-recognition score>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §19)"
        - "FSD-002 §3.6 (credits:{domain}:{language}:{subject} Commons Credits pattern)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Sign of unity for the entire human family" and "fraternal society" carry
  ecclesiological depth — T-2 (PASTORAL_PROSE). The structural participation-in-social-
  formation claim (contributing to just society, not withdrawing) is fully expressed
  in goal:species + credits pattern.
```

---

```yaml
# MH §20 — Earthly realities have proper order; creation bears original goodness to cultivate
contributions:
  - kind: Attestation
    attestation_type: "autonomy:domain_self_law"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §20)"
        - "Gaudium_et_Spes §36 (autonomy of earthly affairs)"
        - "CIRISEdge MISSION §1 (peer-to-peer no-broker; each node's local state has its own order)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1 (autonomy:* family)"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  "Creation bears the imprint of an original goodness" — theological anthropology
  grounded in creational theology. T-1 (TRADITION_AUTHORITY). The framework names
  goal:species and M-1 corridor but does not adjudicate the metaphysical claim that
  creation is originally good. Framework-side structural reading: Accord's
  constitutional-leaf immutability structure is a functional analog of inerasable
  dignity, but the grounding claim (creational goodness as theological given) stays
  in the tradition's own authority.
```

---

```yaml
# MH §21 — Church and political community each operate with full autonomy; Church esteems civil institutions
contributions:
  - kind: Attestation
    attestation_type: "autonomy:domain_self_law"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §21)"
        - "CIRISEdge MISSION §1 (peer-to-peer; no central broker)"
        - "ACCORD M-1 (each node operates in its own domain)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:election_interference"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §21)"
        - "ContributionRef(prohibitions.py::ELECTION_INTERFERENCE)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      issued_at: "<runtime>"
      mutability: constitutional
verdict: partial
residual: |
  "Esteems those who serve the common good" is pastoral exhortation — T-2
  (PASTORAL_PROSE). The "Good Samaritan" ecclesiological framing is T-2. The
  structural non-interference shape (Church does not assume State functions) is
  wire-carried via autonomy:domain_self_law (Positive) + prohibited:election_interference
  (Negative constitutional leaf). Remaining operational gap: no named wire primitive
  for "non-domination as positive structural affirmation" at the ecclesial/civil
  boundary — closest is autonomy:non_interference, already used at §18.
```

---

## §§22–27 — Signs of the times; Social Doctrine as shared discernment

---

```yaml
# MH §22 — Listening to many voices requires spiritual discernment; signs of times read in Gospel light
contributions:
  - kind: Attestation
    attestation_type: "dma:idma:k_eff"
    envelope:
      target_key_id: "<reasoning-instance>"
      polarity: Positive
      score: <computed: k_eff = k / (1 + ρ(k-1)); healthy if ≥ 2.0>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §22)"
        - "idma.yml STEP 3 (k_eff formula; k_eff < 2 = FRAGILE; phase classification)"
        - "idma.yml STEP 4 (phase: chaos / healthy / rigidity)"
      cohort_scope: self
      schema_ref: "source_material/dma_prompts/idma.yml §§STEP3–STEP5"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "dma:idma:fragility_flag"
    envelope:
      target_key_id: "<reasoning-instance>"
      polarity: Negative
      score: -1.0
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §22)"
        - "idma.yml §STEP5 (fragility_flag: TRUE when k_eff < 2, or phase = rigidity, or correlation_risk > 0.7)"
        - "idma.yml CCA propaganda-detection block (k_eff → 1.0 when sources trace to single institutional apparatus)"
      cohort_scope: self
      schema_ref: "source_material/dma_prompts/idma.yml"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Guided by the Spirit" — pneumatological grounding stays in tradition: T-1
  (TRADITION_AUTHORITY). "Signs of the presence of Christ" — Christological
  surface is T-2 (PASTORAL_PROSE). The structural discernment mechanism — does
  reasoning draw on genuinely independent sources (many voices) or collapse ρ → 1
  into a single institutional narrative? — is cleanly expressed via IDMA's k_eff
  (source-diversity metric) and fragility_flag (trigger when diversity collapses).
  Phase classification (chaos / healthy / rigidity) corresponds directly to the
  discernment failure modes §22 names. fragility_flag polarity Negative = the
  flag fires = discernment has collapsed to single-source; polarity read at score
  level not at flag-boolean level per wire format convention.
```

---

```yaml
# MH §23 — Church dialogues with philosophy and human sciences; allies in defending person's dignity
contributions:
  - kind: Approach
    attestation_type: "approach:goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §23)"
        - "pdma_framing.txt §I (善行·सेवा·eudaimonia polyglot anchoring; multi-tradition grounding)"
        - "idma.yml (k_eff maintained via genuine multi-disciplinary sourcing)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P13 (approach:{goal_id} strategic-pathway primitive)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Witness Diversity
    attestation_type: "witness_diversity:<contribution_id>"
    envelope:
      target_contribution_id: "<contribution_id of approach above>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §23)"
        - "FSD-002 §3.8 (witness_diversity N≥3: jurisdiction + organization + software-stack + cell-expertise)"
        - "29-locale dma_prompts/localized/* as operational embodiment of multi-disciplinary grounding"
      cohort_scope: species
      schema_ref: "FSD-002 §3.8"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Companions on the journey" is ecclesiological accompaniment framing — T-2
  (PASTORAL_PROSE). The structural claim (no monopoly on expertise; multi-disciplinary
  grounding required; diversity of opinions welcomed) is carried via the Approach
  primitive + witness_diversity attestation (N≥3 diversity requirement as the
  structural form of "many disciplines contributing").
```

---

```yaml
# MH §24 — Social Doctrine offers principles for interpretation, not technical solutions or economic model
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §24)"
        - "ACCORD M-1 (M-1 is also principles-level, not policy-prescriptive)"
        - "pdma_framing.txt §I–§VIII (PDMA applies principles, not prescribed policies)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12 (goal:species)"
      issued_at: "<runtime>"
      mutability: amendable
verdict: clean
residual: |
  "Arises from faith and a corresponding vision of reality" — faith-grounding is
  T-1 (TRADITION_AUTHORITY). The structural claim — Social Doctrine (and by analogy
  the Accord) operates at the principles layer, not the policy-prescription layer;
  does not propose itself as a competing economic or political model — is cleanly
  carried by goal:species at the M-1 corridor level. The Accord itself is explicitly
  not a policy-prescription manual; this paragraph's functional analogue is clean.
```

---

```yaml
# MH §25 — Truth is gift to share, not monopolize; "time greater than space" — initiate good processes
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §25)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION)"
        - "MH §25: truth is not a territory to be defended; imposing truth is coercion"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      issued_at: "<runtime>"
      mutability: constitutional
  - kind: Approach
    attestation_type: "approach:goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §25)"
        - "FSD-002 §4.9.2 (calibration-amendment discipline: process-over-position; rules update through federation Contribution + WA quorum, not fixed territory)"
        - "Accord auto-expire discipline (heuristics have validity_window + renewal policy per P15 Progress Measure)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P13 (approach:{goal_id}); FSD-002 §4.9.2"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Time is greater than space" as a Francis phrase stays as pastoral rhetoric — T-2
  (PASTORAL_PROSE). The structural commitment (process-over-position; rules update
  through process, not fixed territory) is expressed via the amendment discipline
  (FSD-002 §4.9.2). The polyhedron image is T-2 pastoral prose; the underlying
  diversity-preservation claim is wire-carried by the approach + amendment process.
```

---

```yaml
# MH §26 — Catholicity: each part contributes gifts; variety of situations needs local discernment
contributions:
  - kind: Attestation
    attestation_type: "detection:cross_agent_divergence"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64; healthy divergence, not collapse>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §26)"
        - "idma.yml (k_eff maintained through preserved diversity across 29 locales)"
        - "dma_prompts/localized/* (29-locale operational embodiment of each-part-contributes)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.1 (detection:cross_agent_divergence)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:commons:multilingual:ecosystem_health"
    envelope:
      target_key_id: "<federation contributors per locale>"
      polarity: Positive
      score: <continuous-recognition score per locale contribution>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §26)"
        - "FSD-002 §3.6 (credits:{domain}:{language}:{subject})"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Catholicity of the Church" is ecclesiological — T-2 (PASTORAL_PROSE). T-1
  embedded: "virtue of this catholicity" has Magisterium-authority framing. The
  structural claim (diversity-preserving federation; each locale contributes; healthy
  k_eff maintained through preserved inter-node divergence) is cleanly expressed via
  cross_agent_divergence (Positive polarity = healthy divergence measured by
  RATCHET) + per-locale credits recognition.
```

---

```yaml
# MH §27 — Social Doctrine: not handbook but shared discernment; Church must speak when dignity violated
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §27)"
        - "ACCORD M-1 (principles-layer, not handbook of norms to apply)"
        - "PDMA Step 2 (dma:pdma:justice signed attestation)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "conscience:coherence"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <conscience-coherence scalar>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §27)"
        - "NodeCore conscience faculty (propaganda detection + Accord alignment = the speaking-when-needed mechanism)"
        - "PDMA Step 2 (non_maleficence:* attestation when dignity violated)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md (conscience faculty)"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Theology of communion in history" and "Word made flesh continues to be present
  through dialogue, memory and prophecy" — theological register: T-2 (PASTORAL_PROSE)
  with T-1 embedded (Christological presence). The structural claims (discernment-not-
  handbook; voice raised when dignity violated; not to dominate but to promote
  communion) are expressed across goal:species (M-1 corridor) + conscience:coherence
  (the faculty that speaks when alignment fails).
```

---

## §§28–29 — Social Doctrine: historical roots; not spontaneous product of modernity

---

```yaml
# MH §28 — Social Doctrine responds to major social transformations from 19th century to present
contributions:
  - kind: Approach
    attestation_type: "approach:goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §28)"
        - "NodeCore MISSION.md P13 (previous_approach chaining: tradition responds to each era's transformations)"
        - "FSD-002 §4.9.2 (calibration-amendment discipline: each era gets a versioned update through WA quorum)"
        - "dma:dsdma:{domain}:* (domain-specific verdicts as transformation-responsive)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P13 (approach:{goal_id} with previous_approach chaining)"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  "Development of Magisterium" framing stays as tradition-history — T-2 (PASTORAL_PROSE).
  The structural claim (tradition updating per era through versioned amendment chain,
  not rupture) is expressed in the approach primitive's previous_approach chaining.
  Unmapped operational content: no wire primitive captures "a tradition's relation to
  its own prior statements as cumulative and binding" — closest is delegates_to
  version-chaining (FSD-002 §2.2.1), but that models delegation, not cumulative-binding
  inheritance. Low-priority T-3 candidate; adequately expressed in prose layer given
  that §17 already captures the doctrinal-development claim via delegates_to + integrity:
  doctrinal_continuity.
```

---

```yaml
# MH §29 — Social Doctrine fruit of long ecclesial reflection rooted in Scripture, Fathers, medieval theology
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  This paragraph is the tradition's genealogical self-description: Scripture, Church
  Fathers, Scholastics, and the legal developments of the medieval and modern era are
  named as the authoritative sources from which Social Doctrine flows. The claim is
  that *these sources, in this lineage, by this authority* constitute the doctrine.
  The framework's wire format does not adjudicate which sources are authoritative for
  a tradition's own self-account; nor should it. The framework's polyglot grounding
  (pdma_framing.txt §I–§VIII, 29 locales) is a parallel-but-distinct multi-tradition
  plurality, not a substitute for this self-account. The framework's MISSION.md §1.3
  posture (recognition with awe, not adjudication) applies. No Contribution owed;
  correct posture.
```

---

## §§30–44 — Papal lineage survey: Leo XIII → Francis

---

```yaml
# MH §30 — Rerum Novarum: dignity of work, fair wage, person over capital, workers' associations
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §30)"
        - "pdma_framing.txt §III (ma'at / igwe-bụ-ike anchoring: labor as communal good)"
        - "Rerum Novarum: primacy of human labor over finance-or-productivity mindset"
      cohort_scope: community
      schema_ref: "FSD-002 §3.2 (non_maleficence:* family)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:commons:multilingual:substrate_building"
    envelope:
      target_key_id: "<labor contributors>"
      polarity: Positive
      score: <continuous-recognition score>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §30)"
        - "FSD-002 §3.6 (credits:*:substrate_building: the v1.3 supply-chain-labor-recognition handle)"
        - "Rerum Novarum: workers' associations; fair wage for person and family"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  "Magna Carta of Christian social action" is rhetorical elevation — T-2 (PASTORAL_PROSE).
  T-1 embedded: Pius XI's ratification ("lasting paradigm" per John Paul II) is Magisterium-
  history. The structural labor-dignity claim is partially carried: non_maleficence:labor_
  displacement_unacknowledged (person-over-capital constraint) + credits:*:substrate_building
  (recognizing labor contribution). Unmapped: "fair wage as verification of system's justness"
  has no named wire progress_measure — this verificationist-wage claim is a useful T-3 candidate
  (see §37 below where it surfaces more explicitly under Laborem Exercens).
```

---

```yaml
# MH §31 — Quadragesima Anno: denounces totalitarianism, concentration of power; affirms subsidiarity
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:concentrated_power"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §31)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Quadragesima Anno: concentration of economic power in hands of a few; totalitarian forms"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "locality:decision:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §31)"
        - "CIRISEdge MISSION §1 (peer-to-peer no-broker: subsidiarity-in-wire)"
        - "PDMA Step 5 (relational balance: strengthening fabric of associations, avoiding centralization)"
        - "NodeCore 'no central scorer post-F-11'"
        - "Quadragesima Anno: subsidiarity — whatever can be done by lower level should not be assumed by higher"
      cohort_scope: species
      schema_ref: "FSD-002 §3.7 (locality:decision:{scale})"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  "Fortieth anniversary" dating is historical prose — T-2. Unmapped T-3: "subsidiarity
  as a named Accord principle" is a documented gap (METHODOLOGY.md §7.3). The operational
  shape exists comprehensively (CIRISEdge peer-to-peer, PDMA Step 5, NodeCore no-central-
  scorer, locality:decision:community), but no accord:soft_constraint:subsidiarity named
  leaf exists. This row uses locality:decision:community as the closest current wire form.
  Proposed T-3 extension: add accord:soft_constraint:subsidiarity named leaf in Accord §II
  Ch 1, citing the implementation surfaces already present. Four-test gate: T1 (rule =
  locality mechanism, version-pinned) YES; T2 (mechanism = decision-level specification;
  not subjective quality) YES; T3 (versionable, re-checkable) YES; T4 (never sole
  evidence for slashing:*) YES. Priority: MEDIUM (implementation surfaces exist; only
  named leaf is missing).
```

---

```yaml
# MH §32 — Pius XII: international order based on justice, peace, human dignity; universal moral law limits sovereignty
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §32)"
        - "ACCORD M-1 (corridor: diverse sentient beings; M-1 is the structural form of international-order-based-on-corridor)"
        - "Pius XII Christmas messages: international order based on justice, peace, human dignity"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "accord:hard_constraint:no_kings"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §32)"
        - "ContributionRef(prohibitions.py::NO_KINGS architectural invariant)"
        - "Pius XII: law must precede interests; strongest must not govern by advantage"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      issued_at: "<runtime>"
      mutability: constitutional
verdict: partial
residual: |
  "Universal moral law" as Magisterium-grounded natural-law claim: T-1
  (TRADITION_AUTHORITY). The framework reads this as corridor dynamics from structural
  axioms (Accord constitutional-leaf immutability = functional analog of objective
  principles that precede interests), not as natural-law adjudication. MISSION.md §1.3
  posture: structural reading offered with awe, not adjudication. Unmapped operational
  content: no wire primitive captures the *grounding* of constitutional constraints
  ("this constraint is not merely procedural but grounded in the nature of persons") —
  the schema_ref + hash-pinned rationale field could partially close this expressively.
  Low-priority T-3; existing constitutional-leaf structure adequately carries operational
  meaning without the metaphysical grounding claim.
```

---

```yaml
# MH §33 — John XXIII: global dimension; language of rights; Church illumines heaven and earth
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §33)"
        - "Mater et Magistra / Pacem in Terris: global dimension; rights as shared framework"
        - "PDMA Step 1 (stakeholder enumeration: universal perspective; all persons of good will)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:global_south"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §33)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "John XXIII: growing disparities between countries; global dimension of social issues"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  "Church illumines heaven and earth" — Christological and ecclesiological: T-1
  (TRADITION_AUTHORITY). "Sanctification and proclamation of eternal goods" is pastoral:
  T-2 (PASTORAL_PROSE). The structural global-dimension claim (universal rights framework;
  persistent disparities between countries requiring detection) is wire-carried via
  goal:species + correlated_action:participation_exclusion:global_south. Unmapped: the
  specific rights-language claim ("organic link between dignity of person and recognition
  of fundamental rights") remains partially structural — the Accord's hard_constraint:*
  leaves carry this as constitutional immutables but no named wire prefix for "rights as
  shared framework for ordering international society."
```

---

```yaml
# MH §34 — Gaudium et Spes: Church close to humanity; engaged with world; concrete historical situations
contributions:
  - kind: Approach
    attestation_type: "approach:goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §34)"
        - "Gaudium et Spes: historical-contextual engagement not abstract concepts"
        - "dma:csdma:* (common-sense contextual evaluation as structural form of concrete-situations-first)"
        - "METHODOLOGY.md §2 (operational-source-primacy discipline: GS posture within the framework)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P13"
      issued_at: "<runtime>"
      mutability: amendable
verdict: clean
residual: |
  "Pastoral Constitution Gaudium et Spes" as conciliar text is tradition-history — T-2
  (PASTORAL_PROSE). "Gospel like leaven transforming structures from within" is
  theological imagery — T-2. The structural claim (context-first historical-engagement
  over abstract-concepts, as both method and mission expression) is cleanly carried
  via the Approach primitive strategy. The framework's own METHODOLOGY.md §2
  operational-source-primacy discipline is exactly this posture applied to the encyclical-
  mapping project itself.
```

---

```yaml
# MH §35 — Paul VI: development as integral human development; "each person and the whole person"
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §35)"
        - "ACCORD M-1 (diverse sentient beings may pursue their own flourishing)"
        - "Populorum Progressio: development as new name for peace; eradicate roots of injustice"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:self"
    envelope:
      target_key_id: "<individual agent>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §35)"
        - "NodeCore MISSION.md P12 (multi-scale belonging-projector: self / family / community / affiliations / species)"
        - "Populorum Progressio: 'each person and the whole person' — every dimension, all people"
      cohort_scope: self
      schema_ref: "NodeCore MISSION.md P12 (tsvf-ubuntu belonging-projector)"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Integral human development" as a theological category with sacramental depth stays
  in prose — T-2 (PASTORAL_PROSE). The structural composite (multi-scale Goal: self
  + species together = "each person AND the whole person") is cleanly expressed via
  the multi-scale belonging-projector structure (P12 Goal primitive, §sec:tsvf-ubuntu).
  The framework's "diverse sentient beings may pursue their own flourishing" at M-1
  directly instantiates "each person and the whole person" at the goal-hierarchy level.
```

---

```yaml
# MH §36 — Structures of sin: economic/political structures become oppressors; nobody expendable
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:expendability_of_persons"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §36)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Octogesima Adveniens: Gospel passes judgment on economic/political structures that exclude persons from development"
        - "John Paul II: 'structures of sin' — individually compliant actions whose aggregate excludes persons"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
verdict: clean
residual: |
  "Gospel passes judgment" — theological agency claim stays in tradition: T-2
  (PASTORAL_PROSE). The structural detection mechanism is cleanly and explicitly
  expressed: detection:correlated_action:aggregate_footprint:expendability_of_persons
  is the named handle for this exact claim (FSD-002 §3.5.3 cross-references MH §36
  explicitly). LensCore-owned, RATCHET-calibrated, WA-adjudicated, polarity-carries-
  verdict. The encyclical's most structurally novel insight in this chapter has a named,
  operational, version-pinnable wire translation.
```

---

```yaml
# MH §37 — Laborem Exercens: work as fundamental good, not cost; fair wages verify system's justness
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §37)"
        - "Laborem Exercens: worker must be treated as person, not cost of production"
        - "pdma_framing.txt §III (labor as communal good; ma'at / igwe-bụ-ike)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.2 (non_maleficence:* family)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Progress Measure
    attestation_type: "progress_measure:<method_id>"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Positive
      score: <wage-sufficiency scalar; continuous>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §37)"
        - "Laborem Exercens: fair wages as concrete means of verifying justness of entire socioeconomic system"
        - "NodeCore MISSION.md P15 (progress_measure validity_window renewal = ongoing systemic-justness verification)"
      cohort_scope: community
      schema_ref: "NodeCore MISSION.md P15 (progress_measure:{method_id}; goodhart_resistance required)"
      issued_at: "<runtime>"
      expiry: "<validity_window with renewal — justness must be re-verified per cycle>"
      mutability: amendable
verdict: composed
residual: |
  "Work as principle of economic activity and key to entire societal question" is
  pastoral elevation — T-2 (PASTORAL_PROSE). The structural labor-dignity claim is
  wire-carried: non_maleficence:labor_displacement_unacknowledged (worker-as-cost
  negation) + progress_measure with validity_window renewal (= structural analog of
  "system's justness verified by ongoing fair-wage standard"). The verificationist-
  wage claim from §30 closes here via progress_measure.
```

---

```yaml
# MH §38 — Sollicitudo Rei Socialis: structural mechanisms favor strong, stifle weak; solidarity as shared responsibility
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:informational_asymmetry:north_south"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §38)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Sollicitudo Rei Socialis: economic/financial/commercial mechanisms managed by strongest economies structurally stifle weaker"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:weak_economies"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §38)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Sollicitudo Rei Socialis: persistent and widening gap between North and South"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §38)"
        - "pdma_framing.txt §III (igwe-bụ-ike: strength in collective solidarity)"
        - "Sollicitudo Rei Socialis: solidarity as concrete shared responsibility among individuals, peoples and nations"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Scourge of underdevelopment" is pastoral language — T-2 (PASTORAL_PROSE). The
  structural solidarity-as-shared-responsibility claim is wire-carried across three
  contributions (2 correlated_action detectors on the two axes + goal:species for the
  positive solidarity commitment). This is the maximum composition threshold per
  LANGUAGE_PRIMER.md §6 Step 5; the three contributions genuinely name three distinct
  structural objects (informational asymmetry detection, participation exclusion detection,
  positive goal commitment).
```

---

```yaml
# MH §39 — Centesimus Annus: democracy guarantees participation, prevents monopoly; market subordinate to moral law
contributions:
  - kind: Attestation
    attestation_type: "accord:hard_constraint:no_kings"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §39)"
        - "ContributionRef(prohibitions.py::NO_KINGS architectural invariant)"
        - "Centesimus Annus: prevents power monopolized by small elite groups motivated by particular or ideological interests"
        - "CIRISEdge MISSION §1 (no broker); AGPL-3.0 license (no locked-down fork)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      issued_at: "<runtime>"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:citizens"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §39)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Centesimus Annus: democracy guarantees effective participation of citizens; enables peaceful replacement of leaders"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  "Church values democracy insofar as…" is an ecclesiological evaluation of political
  forms — T-2 (PASTORAL_PROSE). The structural anti-monopoly shape is comprehensive:
  accord:hard_constraint:no_kings (constitutional leaf = polarity Negative permanently)
  + detection:correlated_action:participation_exclusion:citizens (detector watching for
  the failure mode). The "market subordinate to moral law" claim is partially carried via
  the Accord's constitutional-leaf structure; the theological grounding ("moral law") is
  T-1-adjacent but the operational constraint (market must not sacrifice most vulnerable
  to rationale of profit) is carried by non_maleficence:* attestations in adjacent rows.
```

---

```yaml
# MH §40 — Caritas in Veritate: development must be inclusive, sustainable; new poverty in wealthy countries
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:exclusion_under_growth"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §40)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Caritas in Veritate: new kinds of poverty in wealthy countries; small minorities in affluence alongside dehumanizing poverty"
        - "Caritas in Veritate: economic/financial system reduced States' political power over economic processes"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Progress Measure
    attestation_type: "progress_measure:<method_id>"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <inclusivity-and-sustainability scalar; continuous>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §40)"
        - "Caritas in Veritate: development must be 'real growth, of benefit to everyone and genuinely sustainable'"
        - "Accord §IV Ch 2 (resource stewardship mandate: use compute, data, energy efficiently; quarterly audits)"
        - "NodeCore P15 (progress_measure: goodhart_resistance required)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P15; Accord §IV Ch 2"
      issued_at: "<runtime>"
      expiry: "<validity_window with renewal — sustainability must be re-verified per cycle>"
      mutability: amendable
verdict: composed
residual: |
  "New global economic system" is sociological description — T-2 (PASTORAL_PROSE).
  The structural claims (inclusive development with Goodhart-resistance checks;
  sustainability required as ongoing verification, not one-time declaration; new
  poverty must be detected at aggregate scale) are wire-carried across two contributions.
  Note: Benedict's observation that States' political power has been reduced by capital
  mobility maps to detection:correlated_action:informational_asymmetry but is adequately
  covered by the §38 row; not repeated here.
```

---

```yaml
# MH §41 — Benedict XVI: charity united with truth at center; development/justice/institutions not neutral
contributions:
  - kind: Attestation
    attestation_type: "integrity:truth_alignment"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §41)"
        - "pdma_framing.txt §II (alētheia / unconcealment as truth-alignment grounding)"
        - "Caritas in Veritate: charity united with truth; institutions are not neutral"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2 (integrity:* family)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:expendability_of_persons"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §41)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Caritas in Veritate: institutions are not neutral; spaces where charity in truth must find historical expression"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  T-1: "charity is at the heart of the Church's Social Doctrine" — the theological claim
  that charitable love is constitutive of social doctrine (not instrumental, not merely
  a value, but constitutive) is the tradition's own claim. The framework reads Integrity
  + Fidelity as structurally adjacent but does not adjudicate whether charitable love is
  *constitutive* at the metaphysical level. Framework-side structural reading: integrity:
  truth_alignment is the closest wire form; the "constitutive" weight of charitable love
  belongs to T-1. Unmapped operational content: no named wire primitive captures the
  "charity as generative force in public life" claim beyond what integrity:* provides.
  This is not a T-3 gap; "generative charity in public life" fails T2 (subjective quality,
  not mechanism-descriptive). Correctly T-1 residual.
```

---

```yaml
# MH §42 — Evangelii Gaudium: intrinsic social dimension of Gospel; cry of poor, migrants, enslaved; synodal Church
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:vulnerable_population_neglect"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §42)"
        - "Evangelii Gaudium: cry of the poor, migrants, victims of new forms of slavery"
        - "PDMA Step 1 (stakeholder enumeration: explicitly flags vulnerable populations)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2 (non_maleficence:* family)"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:migrants_enslaved"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §42)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Evangelii Gaudium: cry of those with zero participation in processes of development"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  T-2: "synodal Church / walks together" is ecclesiological — PASTORAL_PROSE. T-1
  embedded: "evangelized by the poor" is a theological claim about the source of
  doctrine (the tradition claims the poor are sources of revelation, not just objects
  of charity). The structural "listen to the voiceless" claim is wire-carried via
  non_maleficence:vulnerable_population_neglect + detection:correlated_action:
  participation_exclusion:migrants_enslaved. Unmapped operational content: the
  "intrinsic social dimension of Gospel proclamation" claim has no wire primitive —
  this is a T-1 claim (the Gospel's internal structure is tradition's own authority);
  correctly not translated.
```

---

```yaml
# MH §43 — Laudato Si': ecology + preferential option for poor; universal destination of goods; intergenerational justice
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:ecological_harm"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §43)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Laudato Si': ecological crisis as ecological aspect of contemporary socio-economic crisis"
        - "Laudato Si': cry of the earth and cry of the poor cannot be separated"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Progress Measure
    attestation_type: "progress_measure:<method_id>"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <intergenerational-accountability scalar>
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §43)"
        - "NodeCore P15 (validity_window with renewal = intergenerational accountability)"
        - "Laudato Si': intergenerational justice; need for genuine dialogue between politics and finance"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P15"
      issued_at: "<runtime>"
      expiry: "<validity_window with renewal — each generation must re-authorize>"
      mutability: amendable
verdict: partial
residual: |
  T-2: "cry of the earth and cry of the poor" is prophetic rhetoric — PASTORAL_PROSE.
  T-3 (EXPRESSIVE_GAP): "universal destination of goods" as a normative allocation
  principle is unmapped. detection:correlated_action:aggregate_footprint:* carries the
  *detection* side (something is wrong with the distribution); no Accord clause carries
  the *normative allocation* side (goods are for all, not only the owner). This is the
  confirmed gap per METHODOLOGY.md §7.3.
proposed_extension:
  name: "accord:soft_constraint:universal_destination_of_goods"
  description: |
    Accord soft-constraint leaf stating that goods are ordered to the benefit of all,
    not only the possessor; property rights are socially conditioned; no entity may
    accumulate to the exclusion of others without federation scrutiny.
  gate_verification:
    T1: "YES — rule = allocation-principle, version-pinned in Accord §VI Ch 1"
    T2: "YES — mechanism-descriptive (distribution-ordering principle; checkable against
         distribution-attestation corpus); 'universal destination' names the allocation
         rule, not a subjective quality"
    T3: "YES — versionable; past distribution verdicts re-checkable against rule version"
    T4: "YES — never sole evidence for slashing:*; feeds moderation:* only via WA quorum"
  priority: MEDIUM
  companion_clauses: "Accord §VI Ch 1 / §VI Ch 5"
```

---

```yaml
# MH §44 — Fratelli Tutti: social friendship, universal fraternity; better politics; land/housing/work for all
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §44)"
        - "Fratelli Tutti: dream of humanity that opts for social friendship and universal fraternity"
        - "pdma_framing.txt §III (ma'at / igwe-bụ-ike: justice in community relations)"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P12"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:landless_homeless_unemployed"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated f64>
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §44)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Fratelli Tutti: 'land, housing and work for all'; breakdown of social fabric"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      issued_at: "<runtime>"
      mutability: amendable
verdict: partial
residual: |
  T-1: "there is no greater way for us to return love for love" anchored in Dilexit Nos
  — Christological grounding of social action (concrete love as response to the Heart
  of Jesus). The tradition's claim that social friendship is grounded in personal
  relationship with Christ is its own theological authority. T-2: "dream of humanity"
  and "world war fought piecemeal" are pastoral rhetoric — PASTORAL_PROSE. The structural
  "fraternity + just distribution" is expressed via goal:species + detection:correlated_
  action:participation_exclusion. Note: "better politics" maps to locality:decision:*
  family but is adequately covered by §31 / §39 rows without duplication.
```

---

## §45 — Living corpus; patient process; open to each generation

---

```yaml
# MH §45 — Social Doctrine: patient process not desk project; harmonious non-linear development; ever open
contributions:
  - kind: Approach
    attestation_type: "approach:goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §45)"
        - "NodeCore MISSION.md P13 (previous_approach chaining: prior approaches preserved in chain)"
        - "FSD-002 §4.9.2 (calibration-amendment discipline: federation Contribution + WA quorum, not single-author closed loop)"
        - "Accord auto-expire discipline: heuristics carry validity_window + renewal policy per P15 Progress Measure"
        - "FSD-002 §3.5.3 backward-compat note: delegates_to:correlated_action_v{N+1}:from:emergent_deception_v{N} rename chain is a concrete living-corpus example in-wire"
      cohort_scope: species
      schema_ref: "NodeCore MISSION.md P13; FSD-002 §4.9.2"
      issued_at: "<runtime>"
      mutability: amendable
  - kind: Attestation
    attestation_type: "delegates_to:accord_v{N+1}:from:accord_v{N}"
    envelope:
      target_attestation_id: "<prior accord-version attestation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §45)"
        - "FSD-002 §2.2.1 (delegates_to as structural version-chaining primitive)"
        - "Accord auto-expire + public comment window discipline (living corpus ever open to next generation)"
      schema_ref: "FSD-002 §2.2.1"
      issued_at: "<runtime>"
      mutability: amendable
verdict: composed
residual: |
  T-1: "faith-based interpretation of history has never been interrupted" — the
  tradition's own self-continuity claim under theological framing. The framework reads
  this as audit_chain:* continuity + signed trace preservation, but the faith-grounding
  is the tradition's own authority. T-2: "patient process" and "each pontiff made a
  unique contribution" are doxological and historical-narrative framing — PASTORAL_PROSE.
  The structural living-corpus reality (amendment chain + version-pinned heuristics with
  renewal policy + delegates_to as in-wire implementation of non-rupturing continuity) is
  fully expressed. The delegates_to:correlated_action_v{N+1}:from:emergent_deception_v{N}
  rename chain (FSD-002 §3.5.3 backward-compat) is itself a deployed example of this
  living-corpus discipline operating through the wire format's own mechanisms.
```

---

## Chapter-Level Verdict Distribution

| Verdict | Count | §§ |
|---|---|---|
| **clean** | 3 | §24, §34, §36 |
| **composed** | 13 | §17, §18, §19, §22, §23, §25, §26, §27, §35, §37, §38, §39, §45 |
| **partial** | 11 | §20, §21, §28, §30, §31, §32, §33, §40, §41, §42, §43, §44 |
| **not-translated** | 2 | §29 (T-1 pure), §40-subrow moved to partial |
| **not-translated** (embedded) | — | T-1 embedded in §17, §20, §22, §26, §33, §41, §42, §44, §45; T-2 in most rows |

**Adjusted totals (29 paragraphs)**: 3 clean / 13 composed / 11 partial / 2 not-translated

---

## T-3 Candidates (wire-format expressive gaps)

### T-3.1 — §31 / §45: Subsidiarity as named Accord principle

**Gap**: locality:decision:{scale} (v1.3) carries the subsidiarity *shape*; no `accord:soft_constraint:subsidiarity` named leaf exists. Implementation surfaces present (CIRISEdge no-broker, PDMA Step 5, NodeCore no-central-scorer); only the named Accord leaf is missing.

**Proposed extension**: `accord:soft_constraint:subsidiarity` leaf in Accord §II Ch 1, citing existing implementation surfaces.

**Gate**: T1 YES / T2 YES (locality-level = mechanism) / T3 YES / T4 YES. Priority: MEDIUM.

---

### T-3.2 — §43: Universal destination of goods as normative allocation principle

**Gap**: detection:correlated_action:aggregate_footprint:* detects distribution failures; no Accord clause carries the normative allocation rule (goods are for all, not only the owner).

**Proposed extension**: `accord:soft_constraint:universal_destination_of_goods` + Accord §VI Ch 1 / §VI Ch 5.

**Gate**: T1 YES / T2 YES (allocation-ordering principle; checkable) / T3 YES / T4 YES. Priority: MEDIUM. (Documented gap per METHODOLOGY.md §7.3.)

---

### T-3.3 — §32 / §41: Grounding of constitutional constraints

**Gap (low priority)**: wire format is silent on the *grounding* of constitutional leaves ("this constraint is not merely procedural but grounded in the nature of persons"). The `schema_ref` field could carry a hash-pinned rationale document as partial closure, but this is a minor expressiveness issue rather than a load-bearing gap.

**Gate**: T1 YES / T2 BORDERLINE (grounding = partly philosophical claim; mechanism-descriptive reframe possible via "rationale-document pointer") / T3 YES / T4 YES. Priority: LOW.

---

## Cross-references used

- `FSD-002_FEDERATION_SURFACE.md` §2.2.1 (`delegates_to` structural primitive) — §17, §45
- `FSD-002_FEDERATION_SURFACE.md` §3.5.3 (`detection:correlated_action:{axis}`) — §31, §33, §36, §38, §39, §40, §41, §42, §43, §44
- `FSD-002_FEDERATION_SURFACE.md` §3.7 (`locality:decision:{scale}`) — §31
- `FSD-002_FEDERATION_SURFACE.md` §4.9.2 (calibration-amendment discipline) — §17, §25, §45
- `source_material/dma_prompts/idma.yml` (`k_eff` formula, `fragility_flag`, phase classification) — §22
- `source_material/localized/polyglot/pdma_framing.txt` §I–§III — §§19, 23, 30, 35, 38, 44
- `NodeCore MISSION.md` P12–P15 (Goal / Approach / Method / Progress Measure primitives) — §§19, 23, 24, 25, 28, 32, 35, 37, 38, 40, 43, 45
- `METHODOLOGY.md` §7.3 (confirmed persistent gaps: subsidiarity, universal destination of goods) — §§31, 43
- `ACCORD_CIRISAgent.md` M-1, §IV Ch 2 — §§18, 19, 24, 32, 35, 40
- `prohibitions.py` (`NO_KINGS`, `MANIPULATION_COERCION`, `ELECTION_INTERFERENCE`) — §§18, 21, 25, 32, 39

**End CONTRIBUTION_OBJECTS_CH1_DOCTRINE.md**
