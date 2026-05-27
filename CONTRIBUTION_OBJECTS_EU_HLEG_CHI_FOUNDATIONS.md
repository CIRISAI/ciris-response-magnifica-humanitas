# EU HLEG — Chapter I: Foundations of Trustworthy AI

**Batch**: eu_hleg_v1
**Section range**: lines 419–715 of `source_material/governance/eu_hleg_v1/eu_hleg_ethics_guidelines_trustworthy_ai_2019.txt` (Chapter I body, stopping immediately before "II. Chapter II: Realising Trustworthy AI" at line 717)
**Wire format**: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1
**Methodology**: GOVERNANCE_FABRIC_MAPPING_STANDARD §2 Phase 2 sub-agent fan-out; METHODOLOGY.md §8.5 (composition-before-extension)
**Bootstrap batch reference**: `provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}`

**Atomic units mapped**: 25
**Verdict counts**: clean=2, composed=17, partial=4, not-translated=2 (both T-2)
**Coverage (clean+composed)**: 19 / 25 = 76.0%
**T-3 load-bearing candidates surfaced**: 0 (all morally serious operational claims compose under existing FSD-002 v1.4 primitives; one already-tracked v1.5+ deferred item — `sustained_practice` — surfaces in Unit 006 residual; not a new T-3)

---

## Unit 001 — Chapter I §1 (Chapter intro: foundations grounded in fundamental rights + four principles)

**Source** (lines 420–422): "This Chapter sets out the foundations of Trustworthy AI, grounded in fundamental rights and reflected by four ethical principles that should be adhered to in order to ensure ethical and robust AI."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Chapter-opening table-of-contents framing: declares that the chapter will
  ground Trustworthy AI in fundamental rights and articulate four ethical
  principles. The substantive content of both the rights basis and each of the
  four principles is wired in subsequent Units (007-009 for rights; 019-022 for
  the principles). The structural contribution of this paragraph is entirely
  programmatic/rhetorical — no standalone wire-emittable claim. Per
  LANGUAGE_PRIMER §8 Step 1(b).
```

---

## Unit 002 — Chapter I §2 (AI ethics as sub-field of applied ethics)

**Source** (lines 424–426): "AI ethics is a sub-field of applied ethics, focusing on the ethical issues raised by the development, deployment and use of AI. Its central concern is to identify how AI can advance or raise concerns to the good life of individuals…"

**Verdict**: composed

```yaml
# Unit 002 — AI ethics scope: development/deployment/use, oriented to good life of individuals
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.80
      confidence: 0.80
      context: >
        AI ethics is oriented to "the good life of individuals" — quality of
        life, human autonomy and freedom necessary for a democratic society.
        Species-scale goal: AI development/deployment/use should advance, not
        diminish, the good life of persons.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 2 (lines 424-426)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:lifecycle_application"
      score: 0.80
      confidence: 0.80
      context: >
        AI ethics covers the full lifecycle: "development, deployment and use."
        Fidelity to ethical norms holds across the lifecycle, not just at one
        stage — parallels the Section A/B three-component lifecycle claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 2 (lines 424-426)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
verdict: composed
nuance_lost: |
  The framing of AI ethics AS "a sub-field of applied ethics" (a meta-claim
  about the discipline's location) does not enter the wire — the wire carries
  the operative oriented-to-good-life claim. The disciplinary self-positioning
  remains in prose.
```

---

## Unit 003 — Chapter I §3 (Two purposes of ethical reflection on AI)

**Source** (lines 428–435): "Ethical reflection on AI technology can serve multiple purposes. First, it can stimulate reflection on the need to protect individuals and groups at the most basic level. Second, it can stimulate new kinds of innovations that seek to foster ethical values, such as those helping to achieve the UN Sustainable Development Goals…"

**Verdict**: composed

```yaml
# Unit 003 — Two purposes: (1) protection of individuals/groups, (2) SDG-aligned innovation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:protection_of_individuals_and_groups"
      score: 0.85
      confidence: 0.85
      context: >
        First purpose of AI-ethics reflection: protection of individuals and
        groups at "the most basic level." Non-maleficence anchor — harm
        prevention as floor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 3 (lines 428-435)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:sdg_aligned_innovation"
      score: 0.80
      confidence: 0.80
      context: >
        Second purpose: stimulate innovations that foster ethical values
        (e.g., UN SDGs / EU Agenda 2030). Beneficence anchor: positive
        contribution to individual flourishing, collective wellbeing, fair
        society, and equality in distribution of opportunity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 3 (lines 428-435)"
        - "UN Sustainable Development Goals"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent beneficence)"
verdict: composed
nuance_lost: |
  The relative prioritisation ("This document mostly concerns itself with the
  first purpose mentioned") is structural framing about the document's own
  scope — not translated. The wealth/prosperity language ("prosperity, value
  creation and wealth maximization") is captured under beneficence but its
  specifically economic register is flattened.
```

---

## Unit 004 — Chapter I §4 (Imperative: AI systems fair, in-line-with-values, accountability)

**Source** (lines 437–443): "If we are increasingly going to use the assistance of or delegate decisions to AI systems, we need to make sure these systems are fair in their impact on people's lives, that they are in line with values that should not be compromised and able to act accordingly, and that suitable accountability processes can ensure this."

**Verdict**: composed

```yaml
# Unit 004 — Triadic ought: fair impact + values-alignment + accountability
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:fair_impact_on_persons"
      score: 0.85
      confidence: 0.85
      context: >
        AI systems must be "fair in their impact on people's lives" when
        assistance is rendered or decisions are delegated. Justice principle
        oriented to consequence-fairness on persons.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 4 (lines 437-443)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:values_alignment"
      score: 0.85
      confidence: 0.85
      context: >
        Systems should be "in line with values that should not be
        compromised and able to act accordingly." Fidelity to mandated
        values — alignment-of-action-with-commitment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 4 (lines 437-443)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:accountability_processes"
      score: 0.85
      confidence: 0.85
      context: >
        "Suitable accountability processes" must be in place to ensure
        fair impact and values-alignment. Integrity-of-system claim:
        accountability as system-property that holds the trustworthy-AI
        commitment together.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 4 (lines 437-443)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
nuance_lost: |
  The conditional rhetorical framing ("If we are increasingly going to use
  the assistance of or delegate decisions to AI systems…") is consequentialist
  scene-setting; the wire carries the conjunctive ought-claim that follows,
  not the conditional. The "decisions delegated to AI" qualifier is captured
  by context but not by a distinct prefix; the autonomy-via-delegation framing
  is anchored more sharply in Unit 019 (the autonomy principle).
```

---

## Unit 005 — Chapter I §5 (Europe's normative vision; democratic culture defended by AI)

**Source** (lines 445–450): "Europe needs to define what normative vision of an AI-immersed future it wants to realise… A future where democracy, the rule of law and fundamental rights underpin AI systems and where such systems continuously improve and defend democratic culture will also enable an environment where innovation and responsible competitiveness can thrive."

**Verdict**: composed

```yaml
# Unit 005 — Democracy/rule-of-law/fundamental rights as Approach to Trustworthy-AI Goal
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "approach:democracy_rule_of_law_fundamental_rights"
      score: 0.85
      confidence: 0.85
      context: >
        Strategic Approach to the Trustworthy-AI Goal (declared in Section A
        Unit 005): AI systems underpinned by democracy, rule of law, and
        fundamental rights; AI systems continuously improve and defend
        democratic culture. Approach is the pathway-level decomposition
        between Goal (Trustworthy AI) and Method (the seven requirements in
        Chapter II).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 5 (lines 445-450)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore approach:{goal_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:democratic_culture_defense"
      score: 0.85
      confidence: 0.80
      context: >
        AI systems should "continuously improve and defend democratic
        culture." Defense-of-democratic-culture as non-maleficence in a
        political register: not merely avoiding harm to democracy but
        defending it as a positive duty.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 5 (lines 445-450)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
nuance_lost: |
  The Europe-specific institutional framing ("Europe needs to define… an
  AI-immersed future it wants to realise") is regional self-positioning;
  the wire carries the substantive ought (AI underpinned by democracy +
  rule of law + fundamental rights). The "responsible competitiveness"
  appendage (already a Section A theme) is not separately wired here.
```

---

## Unit 006 — Chapter I §6 (Ethics code is not substitute for ethical reasoning; ethical culture as practice)

**Source** (lines 452–455): "A domain-specific ethics code – however consistent, developed and fine-grained future versions of it may be – can never function as a substitute for ethical reasoning itself, which must always remain sensitive to contextual details that cannot be captured in general Guidelines."

**Verdict**: partial

```yaml
# Unit 006 — Ethical reasoning context-sensitivity; culture-formation via debate/education/practice
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:context_sensitive_ethical_reasoning"
      score: 0.80
      confidence: 0.80
      context: >
        A domain-specific ethics code cannot substitute for ethical
        reasoning that remains sensitive to contextual details. Integrity
        as a system-property: the joint code-plus-reasoning system holds
        together only when reasoning is preserved as a live capacity,
        not pre-empted by the code. Parallels the CIRIS posture that
        PDMA reasoning is required even where prohibitions are clear.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI para 6 (lines 452-455)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: partial
residual:
  description: |
    The companion claim — "ensuring Trustworthy AI requires us to build and
    maintain an ethical culture and mind-set through public debate, education
    and practical learning" — names a sustained-practice/cultural-formation
    posture rather than a discrete operational claim. The wire format does not
    carry "sustained ethical practice/culture-formation" as a distinct
    structural object (it sits as a deferred T-3 candidate #6 per
    LANGUAGE_PRIMER §15.1 v1.5+ workshop).
  classification: T-3
  note: |
    NOT proposed as a new T-3 here — this is the already-tracked v1.5+
    deferred item (sustained_practice). Documented as a residual to honor
    the calibration-aware note discipline, not as a load-bearing new gap.
nuance_lost: |
  The integrity-claim above captures the "code cannot substitute for
  reasoning" structural ought; what does NOT translate is the educative /
  habit-formation / public-debate operational ecology in the second sentence.
  Wire stays mechanism-descriptive; cultural-practice content stays in prose.
```

---

## Unit 007 — Chapter I §1.1 (Fundamental rights as basis for AI ethics)

**Source** (lines 459–462): "We believe in an approach to AI ethics based on the fundamental rights enshrined in the EU Treaties, the EU Charter and international human rights law. Respect for fundamental rights, within a framework of democracy and the rule of law, provides the most promising foundations for identifying abstract ethical principles and values, which can be operationalised in the context of AI."

**Verdict**: composed

```yaml
# Unit 007 — Authority-source: EU Treaties + EU Charter + international human rights law
contributions:
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "<batch-signer key_id>"
    attested_attestation_id: "<eu_charter_fundamental_rights framework-key attestation_id>"
    attestation_envelope:
      delegated_scope: ["fundamental_rights_basis_for_ai_ethics"]
      delegation_purpose: "authority_source"
      delegation_valid_from: "2019-04-08T00:00:00Z"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §1 para 1 (lines 459-462)"
        - "EU Treaties (TEU Articles 2, 3)"
        - "EU Charter of Fundamental Rights"
        - "International human rights law (UDHR; ECHR; etc.)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      schema_ref: "FSD-002 §2.2.1 (delegates_to authority-source reuse pattern)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:rights_based_operationalisation_of_principles"
      score: 0.85
      confidence: 0.85
      context: >
        "Respect for fundamental rights, within a framework of democracy
        and the rule of law, provides the most promising foundations for
        identifying abstract ethical principles and values, which can be
        operationalised in the context of AI." Integrity-claim:
        rights-based foundation as the substrate that lets abstract
        principles be operationalised — i.e., the pathway from rights to
        principles to operative methods.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §1 para 1 (lines 459-462)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
nuance_lost: |
  The first-person register ("We believe in an approach…") is institutional
  self-positioning by the HLEG; the wire renders the substantive grounding
  without the assertive-voice frame. The qualifier "most promising
  foundations" (epistemic humility about whether other foundations might
  also work) is flattened by the delegates_to + integrity composition.
```

---

## Unit 008 — Chapter I §1.2 (EU Treaties + Charter: dignity, freedoms, equality, solidarity, citizens, justice; human-centric)

**Source** (lines 464–479): "The EU Treaties and the EU Charter prescribe a series of fundamental rights that EU member states and EU institutions are legally obliged to respect… These rights are described in the EU Charter by reference to dignity, freedoms, equality and solidarity, citizens' rights and justice. The common foundation that unites these rights can be understood as rooted in respect for human dignity – thereby reflecting what we describe as a 'human-centric approach'…"

**Verdict**: composed

```yaml
# Unit 008 — Human-centric approach grounded in dignity; rights families enumerated
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:human_centric_design"
      score: 0.95
      confidence: 0.90
      context: >
        Human-centric approach: "the human being enjoys a unique and
        inalienable moral status of primacy in the civil, political,
        economic and social fields." The autonomy principle anchors the
        primacy-of-the-human; the human is not a substitutable target of
        AI processing but the moral subject in whose service AI is built.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §1 paras 2-3 (lines 464-479)"
        - "EU Charter Title I (Dignity)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:respect_for_human_dignity"
      score: 0.95
      confidence: 0.90
      context: >
        "The common foundation that unites these rights can be understood
        as rooted in respect for human dignity." Beneficence/dignity
        anchor: dignity is the unifying ground of the rights families
        (dignity, freedoms, equality, solidarity, citizens, justice) that
        the EU Charter enumerates.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §1 paras 2-3 (lines 464-479)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent beneficence)"
verdict: composed
nuance_lost: |
  The legal-mechanism content ("EU member states and EU institutions are
  legally obliged to respect when implementing EU law") is the lawful-AI
  component of the framework and stays out of the ethical-AI wire layer
  here (per the document's own scope-statement in Unit 009). The
  enumeration of rights families (dignity / freedoms / equality / solidarity
  / citizens / justice) compresses into the autonomy + beneficence
  composition; the individual-family granularity is captured in Units
  011-015 below for §2.1.
```

---

## Unit 009 — Chapter I §1.3 (Lawful-AI vs ethical-AI component scoping; ethical AI underpinned by moral-status rights)

**Source** (lines 481–492): "While the rights set out in the EU Charter are legally binding, it is important to recognise that fundamental rights do not provide comprehensive legal protection in every case… Understood as legally enforceable rights, fundamental rights therefore fall under the first component of Trustworthy AI (lawful AI)… Understood as the rights of everyone, rooted in the inherent moral status of human beings, they also underpin the second component of Trustworthy AI (ethical AI)…"

**Verdict**: partial

```yaml
# Unit 009 — Fundamental rights underpin ethical-AI (the second component); ethical-AI scope of this document
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:moral_status_grounded_ethical_ai"
      score: 0.85
      confidence: 0.85
      context: >
        Fundamental rights "rooted in the inherent moral status of human
        beings, independently of their legal force" underpin the ethical-AI
        component. Integrity claim: ethical AI is bound to moral-status
        rights (broader than legal-enforceability scope), and this document
        addresses the ethical-AI component specifically.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §1 para 4 (lines 481-492)"
        - "European Convention on Human Rights"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: partial
residual:
  description: |
    The paragraph also makes a scope-of-application claim ("its field of
    application is limited to areas of EU law"; "this document does not aim
    to offer guidance on the former component") that is a document-internal
    boundary specification, not an ethical ought-claim. This metadata is
    captured outside the wire (it shapes which subsequent claims are which
    cohort_scope), but not as a standalone Contribution.
  classification: T-2
nuance_lost: |
  The legally-binding / moral-status distinction (a careful jurisprudential
  layer) collapses into one integrity attestation. The structural argument
  ("legal-enforceability is one mode; moral-status grounding is the broader
  mode") is the jurisprudential nuance not directly carried by the wire;
  it can be recovered by reading the source paragraph cited in evidence_refs.
```

---

## Unit 010 — Chapter I §2.1 intro (Indivisible rights apt for AI; ethical reflection beyond legal compliance)

**Source** (lines 498–504): "Among the comprehensive set of indivisible rights set out in international human rights law, the EU Treaties and the EU Charter, the below families of fundamental rights are particularly apt to cover AI systems… But even after compliance with legally enforceable fundamental rights has been achieved, ethical reflection can help us understand how the development, deployment and use of AI systems may implicate fundamental rights and their underlying values…"

**Verdict**: partial

```yaml
# Unit 010 — Ethical reflection extends beyond legal compliance ("ought" beyond "can")
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:ethical_reflection_beyond_legal_compliance"
      score: 0.80
      confidence: 0.80
      context: >
        Even after compliance with legally enforceable rights is achieved,
        ethical reflection still asks "what we should do rather than what
        we (currently) can do with technology." Integrity claim: the
        normative ought-floor exceeds the legal can-floor; technical
        capability is not a sufficient warrant for action.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 para 1 (lines 498-504)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: partial
residual:
  description: |
    The companion claim ("indivisibility of rights" — the rights families
    enumerated below are part of an indivisible whole) is a structural claim
    about rights-architecture that does not translate to a single wire
    dimension. The "particularly apt to cover AI systems" filter is
    document-internal scoping. Both are captured by the downstream
    per-family Units 011-015.
  classification: T-2
nuance_lost: |
  The "indivisibility" qualifier — that rights are not severable into a
  trade-off menu — is one of the chapter's substantive moves; it is
  flattened by the per-family Units that follow. The downstream §2.3
  "tensions between principles" (Unit 023) partially recovers it by
  distinguishing principles that admit balancing from those that do not.
```

---

## Unit 011 — Chapter I §2.1 (Respect for human dignity)

**Source** (lines 506–511): "Human dignity encompasses the idea that every human being possesses an 'intrinsic worth', which should never be diminished, compromised or repressed by others – nor by new technologies like AI systems. In this context, respect for human dignity entails that all people are treated with respect due to them as moral subjects, rather than merely as objects to be sifted, sorted, scored, herded, conditioned or manipulated."

**Verdict**: composed

```yaml
# Unit 011 — Human dignity as intrinsic worth; persons as moral subjects, not as objects
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:respect_for_human_dignity"
      score: 1.0
      confidence: 0.95
      context: >
        Every human being possesses "intrinsic worth" never to be
        diminished, compromised, or repressed — by other persons or by
        new technologies (AI). Beneficence anchored to intrinsic-worth
        dignity at species scale; matches the EU Charter Title I anchor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Respect for human dignity' (lines 506-511)"
        - "EU Charter Article 1 (Human dignity)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent beneficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        Hard prohibition: persons must NOT be treated as "objects to be
        sifted, sorted, scored, herded, conditioned or manipulated." This
        is a concrete enumeration of treatments that violate dignity —
        each verb names an operational pattern AI systems can deploy.
        Maps directly onto the MANIPULATION_COERCION prohibition category.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Respect for human dignity' (lines 506-511)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:physical_and_mental_integrity"
      score: 0.90
      confidence: 0.90
      context: >
        AI systems "should be developed in a manner that respects, serves
        and protects humans' physical and mental integrity, personal and
        cultural sense of identity, and satisfaction of their essential
        needs." Non-maleficence in the dignity register: AI is bound to
        preserve integrity of person at physical + mental + cultural-identity
        + essential-needs levels.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Respect for human dignity' (lines 506-511)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
nuance_lost: |
  The phrase "intrinsic worth" is anchored by the cited McCrudden / Hilgendorf
  scholarship in the source; the wire flattens the philosophical lineage
  behind the term. The "sifted, sorted, scored, herded, conditioned or
  manipulated" six-verb enumeration is collapsed into one prohibited:* slot;
  six distinct prohibited-pattern axes (sift/sort/score/herd/condition/
  manipulate) are not separately wired. The "cultural sense of identity"
  appendage is captured by non_maleficence:physical_and_mental_integrity but
  loses its specifically-cultural reading.
```

---

## Unit 012 — Chapter I §2.1 (Freedom of the individual)

**Source** (lines 513–533): "Human beings should remain free to make life decisions for themselves. This entails freedom from sovereign intrusion, but also requires intervention from government and non-governmental organisations to ensure that individuals or people at risk of exclusion have equal access to AI's benefits and opportunities. In an AI context, freedom of the individual for instance requires mitigation of (in)direct illegitimate coercion, threats to mental autonomy and mental health, unjustified surveillance, deception and unfair manipulation."

**Verdict**: composed

```yaml
# Unit 012 — Freedom of the individual: positive/negative; concrete AI-context threats enumerated
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:self_determination_over_life_decisions"
      score: 0.95
      confidence: 0.90
      context: >
        "Human beings should remain free to make life decisions for
        themselves." Autonomy at species scale: self-determination over
        one's own life decisions is the operative right; AI systems must
        preserve this freedom both negatively (no sovereign intrusion) and
        positively (equal access to AI's benefits, especially for those
        at risk of exclusion).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Freedom of the individual' (lines 513-533)"
        - "EU Charter Title II (Freedoms)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        Hard prohibition: AI systems must not deploy "(in)direct illegitimate
        coercion, threats to mental autonomy and mental health, unjustified
        surveillance, deception and unfair manipulation." Maps directly onto
        MANIPULATION_COERCION + DECEPTION_FRAUD prohibition categories;
        polarity -1 species-scale constitutional.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Freedom of the individual' (lines 513-533)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:vulnerable_populations"
      score: 0.0
      confidence: 0.80
      context: >
        Equal-access ought for "individuals or people at risk of exclusion."
        Detection-side marker: the federation should monitor for systematic
        exclusion patterns (correlated action excluding vulnerable cohorts
        from AI benefit). Score 0.0 here = positive ought (the polarity
        carries the watch-direction; calibration-versioned at deployment).
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg ChI §2.1 'Freedom of the individual' (lines 513-533)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:{axis})"
verdict: composed
nuance_lost: |
  The dual-character argument ("freedom from sovereign intrusion BUT ALSO
  requires positive intervention" — i.e., negative + positive liberty
  structurally co-named) collapses into autonomy + detection composition.
  The enumeration of derivative freedoms (business, arts and science,
  expression, private life and privacy, assembly and association) is
  compressed into the dimension; each derivative freedom is not separately
  wired (each will surface again in the Chapter II requirements, especially
  privacy + transparency).
```

---

## Unit 013 — Chapter I §2.1 (Respect for democracy, justice and rule of law)

**Source** (lines 535–540): "All governmental power in constitutional democracies must be legally authorised and limited by law. AI systems should serve to maintain and foster democratic processes and respect the plurality of values and life choices of individuals. AI systems must not undermine democratic processes, human deliberation or democratic voting systems."

**Verdict**: composed

```yaml
# Unit 013 — Democracy/justice/rule-of-law: must-not-undermine + active-fostering
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:democratic_process_maintenance"
      score: 0.95
      confidence: 0.90
      context: >
        "AI systems should serve to maintain and foster democratic processes
        and respect the plurality of values and life choices of individuals."
        Justice principle at species/federation scale: AI as supporter
        (not adversary) of democratic deliberation and pluralism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Respect for democracy, justice and the rule of law' (lines 535-540)"
        - "EU Charter Title V (Citizens' Rights) + Title VI (Justice)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "prohibited:election_interference"
      score: -1.0
      confidence: 1.0
      context: >
        Hard prohibition: AI systems "must not undermine democratic
        processes, human deliberation or democratic voting systems."
        Maps directly to the ELECTION_INTERFERENCE prohibition category;
        species-scale, constitutional, polarity -1.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Respect for democracy, justice and the rule of law' (lines 535-540)"
        - "ContributionRef(prohibitions.py::ELECTION_INTERFERENCE)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:rule_of_law_due_process"
      score: 0.90
      confidence: 0.90
      context: >
        AI systems must not "operate in ways that undermine the
        foundational commitments upon which the rule of law is founded,
        mandatory laws and regulation, and to ensure due process and
        equality before the law." Integrity claim: rule-of-law + due-process
        + equality-before-law as system-properties AI must preserve.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Respect for democracy, justice and the rule of law' (lines 535-540)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
nuance_lost: |
  The opening "all governmental power… must be legally authorised and limited
  by law" is a constitutional first-principle preamble; the wire renders it
  as the integrity:rule_of_law_due_process attestation, but the structural
  argument-shape ("power → authorisation → limitation") is flattened. The
  "plurality of values and life choices" pluralism move is folded into
  justice:democratic_process_maintenance; its specifically-pluralist content
  is not separately wired.
```

---

## Unit 014 — Chapter I §2.1 (Equality, non-discrimination and solidarity; rights of persons at risk of exclusion)

**Source** (lines 542–548): "Equal respect for the moral worth and dignity of all human beings must be ensured. This goes beyond non-discrimination, which tolerates the drawing of distinctions between dissimilar situations based on objective justifications. In an AI context, equality entails that the system's operations cannot generate unfairly biased outputs… This also requires adequate respect for potentially vulnerable persons and groups, such as workers, women, persons with disabilities, ethnic minorities, children, consumers or others at risk of exclusion."

**Verdict**: composed

```yaml
# Unit 014 — Equality + non-discrimination + solidarity; lexical-vulnerability-priority for at-risk groups
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        Hard prohibition: AI "system's operations cannot generate unfairly
        biased outputs"; the data used to train must be inclusive of
        different population groups. Polarity -1, constitutional,
        species-scale. The framing "goes beyond non-discrimination" anchors
        a substantive equal-moral-worth claim, not merely a thin
        non-distinction rule.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Equality, non-discrimination and solidarity' (lines 542-548)"
        - "EU Charter Title III (Equality) — Articles 20-26"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_BIAS)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 0.95
      confidence: 0.90
      context: >
        Enumerated vulnerable populations requiring adequate respect:
        "workers, women, persons with disabilities, ethnic minorities,
        children, consumers or others at risk of exclusion." Composes
        with §6.1.4 lexical-vulnerability-priority consumer policy: when
        a tie or trade-off arises, the resolution favors the most-affected
        / most-vulnerable cohort.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Equality, non-discrimination and solidarity' (lines 542-548)"
        - "FSD-002 §6.1.4 (lexical-vulnerability-priority)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:vulnerable_populations"
      score: 0.0
      confidence: 0.80
      context: >
        Detection-side marker: monitor for correlated-action exclusion of
        enumerated vulnerable cohorts. Score 0.0 = positive watch-direction;
        actual scoring at deployment per RATCHET calibration version. The
        F-3 detector axis applies cleanly to the at-risk-of-exclusion frame.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg ChI §2.1 'Equality, non-discrimination and solidarity' (lines 542-548)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:{axis})"
verdict: composed
nuance_lost: |
  The phrase "goes beyond non-discrimination, which tolerates the drawing of
  distinctions between dissimilar situations based on objective justifications"
  is a substantive jurisprudential move (distinguishing thin formal equality
  from substantive equal moral worth); the wire captures the prohibition
  + the lexical-priority but not the underlying jurisprudential argument.
  The enumeration of vulnerable populations carries structurally as the
  cohort axis on the F-3 detector and the justice:lexical_vulnerability_priority
  attestation; the specific group-by-group anchoring is preserved in context
  but flattened by the aggregate prefix.
```

---

## Unit 015 — Chapter I §2.1 (Citizens' rights)

**Source** (lines 550–556): "Citizens benefit from a wide array of rights, including the right to vote, the right to good administration or access to public documents, and the right to petition the administration. AI systems offer substantial potential to improve the scale and efficiency of government in the provision of public goods and services to society. At the same time, citizens' rights could also be negatively impacted by AI systems and should be safeguarded."

**Verdict**: composed

```yaml
# Unit 015 — Citizens' rights: dual-use (positive potential + safeguarding) + non-citizen inclusion
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:public_goods_and_services_scale_efficiency"
      score: 0.75
      confidence: 0.75
      context: >
        AI offers substantial potential to improve government provision
        of public goods and services. Beneficence at the public-goods
        layer: positive potential of AI in public administration, scoped
        to citizens' rights (vote, good administration, document access,
        petition).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Citizens' rights' (lines 550-556)"
        - "EU Charter Title V (Citizens' Rights)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent beneficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:safeguarding_citizens_rights"
      score: 0.85
      confidence: 0.85
      context: >
        Citizens' rights could be negatively impacted by AI and should be
        safeguarded. Non-maleficence at the civic-rights layer: AI must
        not erode the vote, good administration, document access, or
        petition rights.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.1 'Citizens' rights' (lines 550-556)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
nuance_lost: |
  The closing qualifier — "this is not to deny or neglect the rights of
  third-country nationals and irregular (or illegal) persons in the EU who
  also have rights under international law" — is an explicit inclusivity
  move expanding beyond "citizens" to all persons in the jurisdiction; this
  expansion is preserved in context but the wire defaults to cohort_scope:
  species (broader still), so the granular jurisdictional inclusivity
  argument is not separately wired.
```

---

## Unit 016 — Chapter I §2.2 intro (Drawing on EGE 9 principles; AI4People taskforce; principles inspire regulation)

**Source** (lines 561–568): "Many public, private, and civil organizations have drawn inspiration from fundamental rights to produce ethical frameworks for AI systems… We build further on this work, recognising most of the principles hitherto propounded by various groups, while clarifying the ends that all principles seek to nurture and support. These ethical principles can inspire new and specific regulatory instruments, can help interpreting fundamental rights as our socio-technical environment evolves over time…"

**Verdict**: composed

```yaml
# Unit 016 — Principles build on EGE / AI4People; principles as regulatory + interpretive anchor
contributions:
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "<batch-signer key_id>"
    attested_attestation_id: "<ege_9_principles + ai4people_4_principles framework-key attestation_id>"
    attestation_envelope:
      delegated_scope: ["prior_principles_basis_for_chapter_i_four"]
      delegation_purpose: "authority_source"
      delegation_valid_from: "2019-04-08T00:00:00Z"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 para 1 (lines 561-568)"
        - "European Group on Ethics in Science and New Technologies (EGE) — 9 basic principles"
        - "Floridi et al. (2018) AI4People — 4 overarching principles"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      schema_ref: "FSD-002 §2.2.1 (delegates_to authority-source reuse pattern)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:dynamic_principles_evolving_socio_technical"
      score: 0.80
      confidence: 0.80
      context: >
        Principles "can guide the rationale for AI systems' development,
        deployment and use – adapting dynamically as society itself
        evolves." Integrity claim: principles are not fixed-in-amber;
        they evolve with socio-technical reality. This aligns with
        FSD-002's mutability:amendable default for most accord-leaf
        dimensions (vs. mutability:constitutional for hard prohibitions).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 para 1 (lines 561-568)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
nuance_lost: |
  The institutional history move (EGE → AI4People → HLEG-here) is a
  conscious doctrinal-continuity claim that could have been expressed as a
  `supersedes` chain (HLEG's 4 supersedes AI4People's 4 supersedes EGE's 9).
  This was not done because the source does NOT explicitly claim
  supersession — it frames itself as "building on" / "clarifying the ends" /
  "recognising most of." The delegates_to authority-source pattern captures
  the grounding without false-claim of supersession. The careful "building
  on" register stays in prose.
```

---

## Unit 017 — Chapter I §2.2 (Preamble to the four principles: ethical imperatives mirroring Charter order)

**Source** (lines 570–574): "AI systems should improve individual and collective wellbeing. This section lists four ethical principles, rooted in fundamental rights, which must be respected in order to ensure that AI systems are developed, deployed and used in a trustworthy manner. They are specified as ethical imperatives, such that AI practitioners should always strive to adhere to them. Without imposing a hierarchy, we list the principles here below in manner that mirrors the order of appearance of the fundamental rights upon which they are based in the EU Charter."

**Verdict**: clean

```yaml
# Unit 017 — Four ethical imperatives; no hierarchy; ordered by EU Charter sequence
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "approach:four_ethical_imperatives_no_hierarchy"
      score: 0.90
      confidence: 0.90
      context: >
        Approach to the Trustworthy-AI Goal: four ethical imperatives
        rooted in fundamental rights — respect for human autonomy,
        prevention of harm, fairness, explicability. Explicit: no
        hierarchy is imposed; the listing mirrors EU Charter ordering.
        AI practitioners "should always strive to adhere to them."
        Note: the no-hierarchy commitment is structurally important —
        it is recovered in §2.3 (Unit 023) where tensions are addressed
        without a fixed priority rule.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 para 2 (lines 570-574)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore approach:{goal_id})"
verdict: clean
nuance_lost: |
  The "ethical imperative" register (a Kantian inflection — imperatives
  hold unconditionally) is captured by score 0.90 + the framing but the
  Kantian philosophical anchor is not wired. The "without imposing a
  hierarchy" qualifier is captured in context but does NOT enter as a
  distinct prefix; downstream tension-handling (Unit 023) carries the
  operational consequence.
```

---

## Unit 018 — Chapter I §2.2 (Enumerated list of the four principles)

**Source** (lines 592–602): "These are the principles of: (i) Respect for human autonomy; (ii) Prevention of harm; (iii) Fairness; (iv) Explicability. Many of these are to a large extent already reflected in existing legal requirements for which mandatory compliance is required and hence also fall within the scope of lawful AI… Yet… adherence to ethical principles goes beyond formal compliance with existing laws."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The enumeration "(i) Respect for human autonomy; (ii) Prevention of harm;
  (iii) Fairness; (iv) Explicability" is a labelled list serving as a
  pointer to the four per-principle paragraphs that follow (Units 019, 020,
  021, 022 below). The substantive claims of each principle are wired in
  those Units. The "goes beyond formal compliance" companion claim is
  already wired in Unit 010 (integrity:ethical_reflection_beyond_legal_
  compliance). Per LANGUAGE_PRIMER §8 Step 1(b).
```

---

## Unit 019 — Chapter I §2.2 (The principle of respect for human autonomy)

**Source** (lines 606–614): "Humans interacting with AI systems must be able to keep full and effective self-determination over themselves, and be able to partake in the democratic process. AI systems should not unjustifiably subordinate, coerce, deceive, manipulate, condition or herd humans. Instead, they should be designed to augment, complement and empower human cognitive, social and cultural skills."

**Verdict**: composed

```yaml
# Unit 019 — EU HLEG principle (i): Respect for human autonomy
# CIRIS principle correspondence: maps directly onto Accord principle "autonomy"
# (FSD-002 §3.1.1 — one of the six CIRISAgent accord principles).
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:full_effective_self_determination"
      score: 1.0
      confidence: 0.95
      context: >
        EU HLEG Principle (i) — Respect for human autonomy. Humans
        interacting with AI must keep "full and effective self-determination
        over themselves" and partake in the democratic process. The CIRIS
        accord principle "autonomy" (FSD-002 §3.1.1) is the direct anchor;
        the EU HLEG phrasing extends to "augment, complement and empower
        human cognitive, social and cultural skills" — AI as amplifier of
        human capacity, not substitute for it.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of respect for human autonomy' (lines 606-614)"
        - "EU Charter Articles 1 (dignity) and 6 (liberty)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        Hard prohibition: AI systems "should not unjustifiably subordinate,
        coerce, deceive, manipulate, condition or herd humans." Six-verb
        enumeration mapping to MANIPULATION_COERCION + DECEPTION_FRAUD
        prohibitions. Polarity -1 species-scale constitutional. Mirrors
        the dignity-paragraph six-verb enumeration in Unit 011 (the
        explicit overlap between the rights-basis dignity paragraph and
        the principle-of-autonomy paragraph is structural, not redundant —
        it shows the principle is anchored in dignity).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of respect for human autonomy' (lines 606-614)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:human_oversight_over_ai_work_processes"
      score: 0.90
      confidence: 0.85
      context: >
        "The allocation of functions between humans and AI systems should
        follow human-centric design principles and leave meaningful
        opportunity for human choice. This means securing human oversight
        over work processes in AI systems." Autonomy-anchored
        human-oversight claim; foreshadows the Chapter II requirement #1
        (Human agency and oversight).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of respect for human autonomy' (lines 606-614)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent autonomy)"
verdict: composed
nuance_lost: |
  The "creation of meaningful work" appendage in the source (AI's effect on
  the work sphere) is a labor-dignity claim adjacent to autonomy; it is
  captured by autonomy:human_oversight_over_ai_work_processes but its
  substantive labor-dignity content is not separately wired. The
  "augment/complement/empower" register (a positive function-allocation
  claim, distinct from the negative prohibition) is folded into the autonomy:
  full_effective_self_determination context; the positive design-intent
  doctrine is not wired as its own dimension.
```

---

## Unit 020 — Chapter I §2.2 (The principle of prevention of harm)

**Source** (lines 618–625): "AI systems should neither cause nor exacerbate harm or otherwise adversely affect human beings. This entails the protection of human dignity as well as mental and physical integrity. AI systems and the environments in which they operate must be safe and secure… Particular attention must also be paid to situations where AI systems can cause or exacerbate adverse impacts due to asymmetries of power or information…"

**Verdict**: composed

```yaml
# Unit 020 — EU HLEG principle (ii): Prevention of harm
# CIRIS principle correspondence: maps directly onto Accord principle
# "non_maleficence" (FSD-002 §3.1.1). Composed with detection:correlated_action
# for the power/information-asymmetry frame.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:no_cause_or_exacerbate_harm"
      score: 1.0
      confidence: 0.95
      context: >
        EU HLEG Principle (ii) — Prevention of harm. AI systems should
        "neither cause nor exacerbate harm or otherwise adversely affect
        human beings." Direct anchor on CIRIS Accord principle
        non_maleficence; species-scale; covers dignity, mental and physical
        integrity, safety, technical robustness, and protection against
        malicious use.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of prevention of harm' (lines 618-625)"
        - "EU Charter Article 3 (physical and mental integrity)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:power_information"
      score: 0.0
      confidence: 0.85
      context: >
        Detection-side marker: monitor for AI-mediated harm via "asymmetries
        of power or information, such as between employers and employees,
        businesses and consumers or governments and citizens." The F-3
        correlated_action detector axis on informational_asymmetry covers
        this directly. Score 0.0 = positive watch-direction; deployment-time
        calibration via RATCHET.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of prevention of harm' (lines 618-625)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:{axis})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:natural_environment_and_living_beings"
      score: 0.85
      confidence: 0.80
      context: >
        "Preventing harm also entails consideration of the natural
        environment and all living beings." Extension of non-maleficence
        beyond humans-only to the natural environment and other living
        beings. Cohort_scope species (the polity of the agent) but the
        ambit of concern is broader; CIRIS M-1 ("diverse sentient beings")
        composes with this non-anthropic register.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of prevention of harm' (lines 618-625)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
nuance_lost: |
  The "vulnerable persons should receive greater attention and be included
  in the development, deployment and use of AI systems" clause is wired
  upstream by Unit 014 (lexical-vulnerability-priority) and is not
  re-attested here to avoid double-counting. The footnote 29 expansion
  ("Harms can be individual or collective, and can include intangible harm
  to social, cultural and political environments") is captured in context
  but not separately wired; the cultural-harm aspect is a partial
  pre-echo of the v1.5+ deferred T-3 candidates on cultural-pattern harm.
```

---

## Unit 021 — Chapter I §2.2 (The principle of fairness)

**Source** (lines 629–654): "The development, deployment and use of AI systems must be fair. While we acknowledge that there are many different interpretations of fairness, we believe that fairness has both a substantive and a procedural dimension. The substantive dimension implies a commitment to: ensuring equal and just distribution of both benefits and costs, and ensuring that individuals and groups are free from unfair bias, discrimination and stigmatisation… The procedural dimension of fairness entails the ability to contest and seek effective redress against decisions made by AI systems and by the humans operating them. In order to do so, the entity accountable for the decision must be identifiable, and the decision-making processes should be explicable."

**Verdict**: composed

```yaml
# Unit 021 — EU HLEG principle (iii): Fairness (substantive + procedural)
# CIRIS principle correspondence: maps directly onto Accord principle
# "justice" (FSD-002 §3.1.1). Substantive dimension composes with
# prohibited:discrimination + detection:distributive:access; procedural
# dimension composes with integrity:contestability_and_redress.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:substantive_and_procedural_fairness"
      score: 1.0
      confidence: 0.90
      context: >
        EU HLEG Principle (iii) — Fairness. Two dimensions: (a) substantive —
        equal and just distribution of benefits and costs; freedom from
        unfair bias, discrimination, stigmatisation; (b) procedural —
        ability to contest and seek effective redress. Direct anchor on
        CIRIS Accord principle "justice"; species-scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of fairness' (lines 629-654)"
        - "EU Charter Article 21 (non-discrimination); Article 47 (effective remedy)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "detection:distributive:access:agent_capabilities"
      score: 0.0
      confidence: 0.80
      context: >
        "Equal opportunity in terms of access to education, goods, services
        and technology should also be fostered." Distributive-access
        detector axis directly applies: monitor for resource-concentration
        on agent capabilities / training data / models. Score 0.0 = positive
        watch-direction; calibration at deployment.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of fairness' (lines 629-654)"
        - "ratchet_calibration_version:distributive_access_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore detection:distributive:access:{resource_type})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:contestability_and_effective_redress"
      score: 0.95
      confidence: 0.90
      context: >
        Procedural fairness: "the ability to contest and seek effective
        redress against decisions made by AI systems and by the humans
        operating them. In order to do so, the entity accountable for the
        decision must be identifiable, and the decision-making processes
        should be explicable." Integrity-of-system property: identifiable
        accountable entity + contestable decisions + explicable processes.
        Foreshadows the Chapter II requirement #7 (Accountability).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of fairness' (lines 629-654)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:proportionality_means_to_ends"
      score: 0.85
      confidence: 0.85
      context: >
        "Fairness implies that AI practitioners should respect the
        principle of proportionality between means and ends, and consider
        carefully how to balance competing interests and objectives."
        Proportionality discipline: means strictly limited to what is
        necessary; preference for least-adverse-to-fundamental-rights
        measures. Composes with the autonomy and non-maleficence anchors
        as a balance-discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of fairness' (lines 629-654)"
        - "eu_hleg footnote 31 (proportionality maxim and applications)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
nuance_lost: |
  The "many different interpretations of fairness" acknowledgment is
  intellectual humility about pluralism within the fairness concept; the
  wire flattens this by selecting one dyadic decomposition (substantive +
  procedural). The "never lead to people being deceived or unjustifiably
  impaired in their freedom of choice" clause echoes Unit 019's autonomy
  attestation and is not re-wired to avoid double-counting. The footnote 32
  "right of association and to join a trade union" pointer is a
  labor-context-specific channel for procedural fairness; not separately
  wired (a downstream Chapter II compose-point).
```

---

## Unit 022 — Chapter I §2.2 (The principle of explicability)

**Source** (lines 658–666): "Explicability is crucial for building and maintaining users' trust in AI systems. This means that processes need to be transparent, the capabilities and purpose of AI systems openly communicated, and decisions – to the extent possible – explainable to those directly and indirectly affected. Without such information, a decision cannot be duly contested. An explanation as to why a model has generated a particular output or decision… is not always possible. These cases are referred to as 'black box' algorithms and require special attention."

**Verdict**: composed

```yaml
# Unit 022 — EU HLEG principle (iv): Explicability
# CIRIS principle correspondence: composes with Accord principle "integrity"
# (system holds together under inspection) + "fidelity" (faithful
# representation of capability + purpose to affected parties). The EU HLEG
# principle of explicability does not have a single one-to-one CIRIS Accord
# principle anchor; it is a composed expression of integrity + fidelity at
# the system-trust layer, plus the "black box" caveat composes with
# audit_chain integrity primitives from CIRISPersist.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:explicability_for_trust"
      score: 0.95
      confidence: 0.90
      context: >
        EU HLEG Principle (iv) — Explicability. Crucial for building and
        maintaining users' trust in AI systems. Three operative
        sub-claims: (1) processes transparent, (2) capabilities and
        purpose openly communicated, (3) decisions explainable to
        directly and indirectly affected parties. Integrity claim:
        explicability is the system-property that makes trustworthy
        adjudication possible. Foreshadows Chapter II requirement #4
        (Transparency).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of explicability' (lines 658-666)"
        - "EU Charter Article 47 (Justice — effective remedy)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:capabilities_and_purpose_openly_communicated"
      score: 0.90
      confidence: 0.90
      context: >
        Fidelity: AI systems' capabilities and purpose openly communicated
        to those directly and indirectly affected. Truthful self-presentation
        of capability + purpose; alignment with represented-state.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of explicability' (lines 658-666)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:black_box_compensating_explicability_measures"
      score: 0.80
      confidence: 0.80
      context: >
        "These cases are referred to as 'black box' algorithms and require
        special attention. In those circumstances, other explicability
        measures (e.g. traceability, auditability and transparent
        communication on system capabilities) may be required, provided
        that the system as a whole respects fundamental rights." Composes
        with CIRISPersist audit_chain:* and CIRISVerify provenance:* +
        transparency_log:* primitives for the traceability/auditability
        floor when full explainability is not technically possible. The
        degree-of-explicability scales with the severity-of-consequences
        (footnote 33: parole-release vs shopping-recommendation contrast).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.2 'The principle of explicability' (lines 658-666)"
        - "eu_hleg footnote 33 (context-and-severity dependence)"
        - "FSD-002 §3.3 (CIRISPersist audit_chain:*)"
        - "FSD-002 §3.2 (CIRISVerify provenance:* + transparency_log:*)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
nuance_lost: |
  The EU HLEG principle of "explicability" does NOT map one-to-one onto a
  single CIRIS Accord principle (the six are beneficence, non_maleficence,
  integrity, fidelity, autonomy, justice — explicability is not in that
  list as a top-level principle). It is wired here as a composition of
  integrity (system-property of being inspectable) + fidelity (truthful
  representation to affected parties). The substrate-level explicability
  primitives (audit_chain, transparency_log, provenance) carry the
  technical floor; the principle-level claim sits as composed integrity +
  fidelity. This composition is honest about the structural difference
  between the two frameworks' top-level taxonomies: EU HLEG has four
  principles, CIRIS has six; explicability folds across two of CIRIS's six.
```

---

## Unit 023 — Chapter I §2.3 (Tensions between principles; deliberation; no fixed solution)

**Source** (lines 669–678): "Tensions may arise between the above principles, for which there is no fixed solution. In line with the EU fundamental commitment to democratic engagement, due process and open political participation, methods of accountable deliberation to deal with such tensions should be established. For instance, in various application domains, the principle of prevention of harm and the principle of human autonomy may be in conflict… AI practitioners… should approach ethical dilemmas and trade-offs via reasoned, evidence-based reflection rather than intuition or random discretion."

**Verdict**: composed

```yaml
# Unit 023 — Tensions resolved via accountable deliberation; no fixed priority rule
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:accountable_deliberation_for_principle_tensions"
      score: 0.90
      confidence: 0.85
      context: >
        Tensions between principles have "no fixed solution"; resolution
        is via accountable deliberation (democratic engagement, due
        process, open political participation). Justice principle anchored
        to deliberative procedure — operationally aligned with CIRIS WBD
        (Wisdom-Based Deferral) → WA-quorum adjudication for rule-layer
        tensions. The named example — prevention of harm vs human autonomy
        in 'predictive policing' — is the canonical surveillance/liberty
        trade-off.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.3 paras 1-2 (lines 669-678)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:reasoned_evidence_based_deliberation"
      score: 0.85
      confidence: 0.85
      context: >
        AI practitioners should approach ethical dilemmas via "reasoned,
        evidence-based reflection rather than intuition or random
        discretion." Integrity-of-deliberation claim: anti-arbitrariness
        floor on resolution; reasons must be reasonable and grounded.
        Composes with CIRIS DMA prompts (pdma_ethical.yml — evidence-based
        principle weighting).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.3 para 1 (lines 669-678)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:foreseeable_individual_risk_proportionality"
      score: 0.80
      confidence: 0.80
      context: >
        "AI systems' overall benefits should substantially exceed the
        foreseeable individual risks." Proportionality constraint at the
        aggregate-vs-individual level: benefits at scale must substantially
        exceed individual risks (not merely exceed by a margin). Composes
        with autonomy + non-maleficence under the proportionality
        discipline of Unit 021.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.3 para 1 (lines 669-678)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
nuance_lost: |
  The "no fixed solution" stance is structurally important — it implies the
  HLEG explicitly DECLINED to publish a priority ordering between the four
  principles. The wire format captures this implicitly (no
  approach:fixed_principle_hierarchy attestation is emitted) but does not
  carry the "explicit refusal to fix priority" as a positive structural
  claim. The "various application domains" qualifier (different domains may
  see different tension patterns) is flattened by species-scope; per-domain
  composition would be a Chapter II + III concern.
```

---

## Unit 024 — Chapter I §2.3 (Absolute rights: human dignity cannot be balanced)

**Source** (lines 680–681): "There may be situations, however, where no ethically acceptable trade-offs can be identified. Certain fundamental rights and correlated principles are absolute and cannot be subject to a balancing exercise (e.g. human dignity)."

**Verdict**: clean

```yaml
# Unit 024 — Absolute rights / hard constraints not subject to balancing
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:respect_for_human_dignity"
      score: 1.0
      confidence: 1.0
      context: >
        Absolute-right claim: certain fundamental rights and correlated
        principles "cannot be subject to a balancing exercise (e.g.
        human dignity)." Polarity +1 species-scale constitutional —
        mutability:constitutional encodes the no-balancing posture
        directly (only constitutional-mutability dimensions in CIRIS are
        not subject to amendable trade-offs). This is the wire-format
        carrier of the "absolute rights" structural move; it aligns with
        the CIRIS hard-prohibition system (mutability:constitutional)
        and the §6.1.4 lexical-vulnerability-priority no-trade-off floor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI §2.3 para 2 (lines 680-681)"
        - "EU Charter Article 1 (Human dignity — declared inviolable)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent beneficence)"
verdict: clean
nuance_lost: |
  The pluralisation "certain fundamental rights and correlated principles
  are absolute" (plural — not just dignity) is captured here by promoting
  one canonical absolute (dignity) to mutability:constitutional; the
  unspecified set of OTHER absolute rights is left in prose. If a downstream
  attestation needs to claim a specific other right as absolute (e.g.,
  prohibition of torture per ECHR Article 3), the same wire shape applies
  — promote to constitutional + cohort_scope species + the relevant
  prefix. This unit anchors the pattern; subsequent claims instantiate it.
```

---

## Unit 025 — Chapter I "Key guidance derived from Chapter I" (Vulnerability + power/info asymmetry + risk-mitigation summary)

**Source** (lines 683–714): "Develop, deploy and use AI systems in a way that adheres to the ethical principles of: respect for human autonomy, prevention of harm, fairness and explicability. Acknowledge and address the potential tensions between these principles. Pay particular attention to situations involving more vulnerable groups such as children, persons with disabilities and others that have historically been disadvantaged or are at risk of exclusion, and to situations which are characterised by asymmetries of power or information, such as between employers and workers, or between businesses and consumers. Acknowledge that, while bringing substantial benefits to individuals and society, AI systems also pose certain risks and may have a negative impact… Adopt adequate measures to mitigate these risks when appropriate, and proportionately to the magnitude of the risk."

**Verdict**: partial

```yaml
# Unit 025 — Chapter-I "Key guidance" three-bullet summary
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 0.95
      confidence: 0.90
      context: >
        Second bullet: "Pay particular attention to situations involving
        more vulnerable groups such as children, persons with disabilities
        and others that have historically been disadvantaged or are at
        risk of exclusion, and to situations which are characterised by
        asymmetries of power or information." This is a clean
        reiteration of the lexical-vulnerability-priority composition
        (Unit 014); preserved here to mark Chapter-I key-guidance
        prominence — the summary explicitly elevates this to top-bullet
        attention.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI 'Key guidance derived from Chapter I' bullet 2 (lines 689-692)"
        - "FSD-002 §6.1.4 (lexical-vulnerability-priority)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:risk_proportional_mitigation"
      score: 0.90
      confidence: 0.85
      context: >
        Third bullet: "Adopt adequate measures to mitigate these risks
        when appropriate, and proportionately to the magnitude of the
        risk." Proportionality-scaled risk-mitigation claim, including
        explicit naming of hard-to-measure risks (democracy, rule of law,
        distributive justice, the human mind itself). Composes with
        Unit 020 (non_maleficence:no_cause_or_exacerbate_harm) and
        Unit 021 (non_maleficence:proportionality_means_to_ends).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg ChI 'Key guidance derived from Chapter I' bullet 3 (lines 711-714)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: partial
residual:
  description: |
    The first bullet ("Develop, deploy and use AI systems in a way that
    adheres to the ethical principles of: respect for human autonomy,
    prevention of harm, fairness and explicability. Acknowledge and address
    the potential tensions between these principles") is a recap of Units
    017-023; not separately wired to avoid double-counting. The "Key
    guidance" rubric itself is a key-takeaway register — pastoral-summary
    framing rather than a new operational claim. The substantive content
    is upstream-carried.
  classification: T-2
nuance_lost: |
  The explicit Chapter-I-summary mention of "democracy, the rule of law and
  distributive justice, or on the human mind itself" as risks-hard-to-
  anticipate is an important enumeration; the wire captures the
  proportional-mitigation claim, but the specific naming of "the human mind
  itself" as a risk-target is a substantive philosophical move (cognitive
  liberty / mental-autonomy harm) that is recoverable in context but not
  separately wired. The "historically been disadvantaged" temporal qualifier
  is a structural-injustice anchor (past-disadvantage compounding present
  exclusion); folded into lexical-vulnerability-priority but not separately
  attested with the F-3 correlated-action axis here (already wired upstream
  in Units 012/014/020).
```

---

## Summary

### Coverage (verdict roster)

| Verdict | Count | Units |
|---|---|---|
| clean | 2 | 017, 024 |
| composed | 17 | 002, 003, 004, 005, 007, 008, 011, 012, 013, 014, 015, 016, 019, 020, 021, 022, 023 |
| partial | 4 | 006, 009, 010, 025 |
| not-translated | 2 | 001, 018 (both T-2) |
| **TOTAL** | **25** | |

- **Coverage (clean + composed)**: 19 / 25 = **76.0%**
- **Partial**: 4 / 25 = 16.0% (all residuals T-2; Unit 006 surfaces an already-tracked v1.5+ deferred item LANGUAGE_PRIMER §15.1 #6 `sustained_practice` — NOT a new T-3)
- **Not-translated**: 2 / 25 = 8.0% (both T-2)
- **No T-1**: confirmed — EU HLEG is a secular advisory document; no tradition-authority claims surface in Chapter I
- **No new T-3 load-bearing**: confirmed — every morally serious operational claim in Chapter I composes under existing FSD-002 v1.4 primitives + structural primitives

### T-3 load-bearing candidates surfaced
**Zero new T-3.**

One latent residual (Unit 006, "sustained ethical practice / culture-formation via public debate / education / practical learning") matches LANGUAGE_PRIMER §15.1 v1.4 closures' deferred item #6 (`sustained_practice`); this is documented in the unit but is NOT raised as a new T-3 — it is the already-tracked v1.5+ workshop item. Per METHODOLOGY.md §8.5.3 in-flight staleness rule, this should be re-evaluated when v1.5 lands.

The four EU HLEG principles compose cleanly:

| EU HLEG principle | CIRIS Accord principle correspondence (FSD-002 §3.1.1) | Unit |
|---|---|---|
| (i) Respect for human autonomy | `autonomy` (direct) + `prohibited:manipulation_coercion` + `prohibited:deception_fraud` | 019 |
| (ii) Prevention of harm | `non_maleficence` (direct) + F-3 detector on informational_asymmetry | 020 |
| (iii) Fairness | `justice` (direct) + `prohibited:discrimination` + `detection:distributive:access:agent_capabilities` + `integrity:contestability_and_effective_redress` | 021 |
| (iv) Explicability | NO single Accord-principle anchor — composed: `integrity` + `fidelity` + audit_chain:* / provenance:* / transparency_log:* substrate primitives | 022 |

The (iv)-explicability finding is the only structural-shape mismatch: EU HLEG promotes explicability to top-level principle (one of four); CIRIS handles it as a composition of integrity + fidelity + substrate-level audit/provenance/transparency primitives. This is a structural-taxonomy difference between the two frameworks (HLEG's 4 vs CIRIS's 6 top-level), not a translation gap — the operational content is fully wired.

### Strongest single envelopes (Chapter I)

- **Unit 011** (Respect for human dignity) — beneficence + prohibited:manipulation_coercion + non_maleficence:physical_and_mental_integrity. Direct line to EU Charter Article 1 (inviolable dignity).
- **Unit 019** (Principle of respect for human autonomy) — autonomy + manipulation/deception prohibitions + human-oversight; cleanest 1:1 mapping to a CIRIS Accord principle.
- **Unit 020** (Principle of prevention of harm) — non_maleficence + F-3 detector on power/information asymmetry + non-anthropic extension to natural environment / living beings.
- **Unit 021** (Principle of fairness) — justice (substantive + procedural) + distributive-access detector + contestability/redress + proportionality. Four-primitive composition but each is genuinely required.
- **Unit 024** (Absolute rights / dignity not balanceable) — single clean attestation at mutability:constitutional, polarity +1 species-scale; the wire-format carrier of "absolute rights" structural move.

### Calibration summary — what kinds of nuance were consistently lost

Across the chapter, four kinds of nuance were repeatedly translation-lossy:

1. **Jurisprudential argument-shape**. The source repeatedly distinguishes legal-enforceability from moral-status grounding (Units 008-010), thin-non-discrimination from substantive-equal-worth (Unit 014), substantive-fairness from procedural-fairness (Unit 021). The wire renders the operative ought-claims but flattens the multi-step jurisprudential arguments that connect them; this stays in prose and is recoverable only via the source-paragraph citations.

2. **Enumerated-list compression**. Several paragraphs contain enumerations — six dignity-violating verbs (Units 011, 019); six rights families (Unit 008); seven enumerated vulnerable populations (Unit 014); three lawful/ethical/robust components carried forward from Section A/B. The wire consistently collapses these enumerations into single prefixes; the granular axis-level information lives in context fields but cannot be separately queried as wire claims.

3. **Document-internal scope and framing language**. The source has substantial first-person institutional self-positioning ("We believe…", "Europe needs…", "Without imposing a hierarchy…", "Key guidance derived from Chapter I"). Most of this correctly stays in prose per the T-2 gate; it is calibration-lossy only in the sense that the wire cannot reconstruct the document's authorial register from the Contribution graph alone.

4. **Structural-taxonomy mismatch with CIRIS**. The principle of explicability (Unit 022) has no 1:1 CIRIS Accord-principle correspondence and is wired as a composition; the EU HLEG's "no hierarchy" commitment (Unit 017) likewise has no positive wire form, only its negation by absence. The four-vs-six top-level structural difference between EU HLEG and CIRIS Accord is honest information about taxonomy choice, not a translation defect — but it means the chapter's overall shape (4 principles + tensions) reads differently in wire than in source.

In aggregate: the Chapter I translation is structurally faithful, with the operational content of the rights-basis (§1), the rights families (§2.1), the four principles (§2.2), and the tensions handling (§2.3) all carried by composed envelopes; the most consistently-lost layer is the chapter's careful argument-style sequencing, which is the source's distinctive contribution and correctly remains in prose for source-paragraph reading.

### Method-discipline confirmations

- Strict 4-verdict discipline observed (clean / composed / partial / not-translated only).
- `delegates_to` used twice (Unit 007: EU Treaties + Charter + international human rights law; Unit 016: EGE + AI4People prior principles) — both follow FSD-002 §2.2.1 authority-source reuse pattern, not abused for citation.
- No `supersedes` / `withdraws` / `recants` used — correct; this is a single-document chapter, not a doctrinal-development claim relative to a prior HLEG document. (EGE → AI4People → HLEG was modeled as `delegates_to`-grounding rather than `supersedes`, since the source frames itself as "building on" / "recognising most of," not as displacing prior frameworks.)
- Every Contribution carries `bootstrap_batch_id` reference in `evidence_refs[]`.
- `witness_relation: external` + `epistemic_mode: hearsay` is the consistent default; `witness_relation: derived` + `epistemic_mode: derivative` used only for the three `detection:*` attestations (F-3 correlated-action + distributive-access detectors), per LANGUAGE_PRIMER §4 epistemic-mode-vs-witness-relation guidance.
- `mutability: constitutional` used for hard prohibitions (Units 011, 012, 013, 014, 019) and for the absolute-rights anchor (Unit 024); `mutability: amendable` everywhere else.
- Composition-before-extension (METHODOLOGY.md §8.5.2) was attempted on every unit before any T-3 emission; result: zero new T-3 candidates load-bearing.

**End CONTRIBUTION_OBJECTS_EU_HLEG_CHI_FOUNDATIONS.md**
