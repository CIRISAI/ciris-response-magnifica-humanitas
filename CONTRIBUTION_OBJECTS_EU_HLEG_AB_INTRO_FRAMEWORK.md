# EU HLEG — Section A (Introduction) + Section B (A Framework for Trustworthy AI)

**Batch**: eu_hleg_v1
**Section range**: lines 192–418 (Section A starts line 192; Section B ends just before Chapter I begins at line 419)
**Source file**: `source_material/governance/eu_hleg_v1/eu_hleg_ethics_guidelines_trustworthy_ai_2019.txt`
**Wire format**: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1
**Methodology**: GOVERNANCE_FABRIC_MAPPING_STANDARD §2 Phase 2 sub-agent fan-out
**Bootstrap batch reference**: `provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}`

**Atomic units mapped**: 24
**Verdict counts**: clean=4, composed=10, partial=3, not-translated=7
**T-3 load-bearing candidates surfaced**: 0 (all morally serious operational claims composed under existing primitives; see Summary)

**Range note**: The prompt cited lines 324–716, but Chapter I begins at line 419 and was explicitly out of scope. Treating section names ("A. Introduction + B. A Framework for Trustworthy AI") as authoritative, this output covers lines 192–418 (the body text of A + B in full, stopping immediately before Chapter I).

---

## Unit 001 — A.Intro §1 (Commission vision: three pillars)

**Source** (lines 193–197): "the European Commission set out its vision for artificial intelligence (AI), which supports 'ethical, secure and cutting-edge AI made in Europe'. Three pillars underpin the Commission's vision: (i) increasing public and private investments in AI to boost its uptake, (ii) preparing for socio-economic changes, and (iii) ensuring an appropriate ethical and legal framework to strengthen European values."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Institutional scene-setting describing the Commission's policy framing. Reports
  organisational structure (HLEG mandate) and three procedural pillars for EU AI
  policy. No standalone operational claim; the substantive content lives in
  subsequent paragraphs (the three-component framework starting Unit 005, the
  four principles in Chapter I). Carry-forward citation only.
```

---

## Unit 002 — A.Intro §2 (HLEG mandate: Ethics Guidelines + Policy/Investment Recommendations)

**Source** (lines 199–201): "the Commission established the High-Level Expert Group on Artificial Intelligence (AI HLEG), an independent group mandated with the drafting of two deliverables: (1) AI Ethics Guidelines and (2) Policy and Investment Recommendations."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Self-referential institutional bookkeeping: identifies the issuing body and its
  deliverables. Identity-of-issuer is carried by attesting_key_id on every
  Contribution in this batch; no standalone wire claim is owed. Per LANGUAGE_PRIMER §8
  Step 1(b).
```

---

## Unit 003 — A.Intro §4 (AI as means to human flourishing + SDGs)

**Source** (lines 208–214): "AI is not an end in itself, but rather a promising means to increase human flourishing, thereby enhancing individual and societal well-being and the common good, as well as bringing progress and innovation. In particular, AI systems can help to facilitate the achievement of the UN's Sustainable Development Goals…"

**Verdict**: composed

```yaml
# Unit 003 — AI as instrumental means to human flourishing; species-scale goal
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.85
      confidence: 0.85
      context: >
        AI development oriented to human flourishing, individual and societal
        well-being, the common good, and the UN Sustainable Development Goals
        (gender balance, climate, natural-resource stewardship, health, mobility,
        production, sustainability indicators). Species-scale aim with explicit
        SDG anchoring.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 4 (lines 208-214)"
        - "UN Sustainable Development Goals (cited in source)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:instrumentality_of_ai"
      score: 0.80
      confidence: 0.80
      context: >
        Normative framing: AI is means, not end. Positive beneficence claim at the
        development/deployment level, with explicit anti-instrumentalisation of
        persons (humans are the end; AI is the means).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 4 (lines 208-214)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent beneficence)"
verdict: composed
```

---

## Unit 004 — A.Intro §5 (Human-centric commitment + risk-proportionality)

**Source** (lines 216–222): "AI systems need to be human-centric, resting on a commitment to their use in the service of humanity and the common good, with the goal of improving human welfare and freedom. While offering great opportunities, AI systems also give rise to certain risks that must be handled appropriately and proportionately."

**Verdict**: composed

```yaml
# Unit 004 — human-centric AI; proportionate risk handling
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:human_centric_design"
      score: 0.90
      confidence: 0.90
      context: >
        AI systems must rest on a commitment to service of humanity and the common
        good, oriented to improving human welfare and freedom. The autonomy
        principle is the operative anchor: human-centric design preserves
        self-determination over AI-mediated decisions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 5 (lines 216-222)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:proportionate_risk_handling"
      score: 0.85
      confidence: 0.85
      context: >
        Risks "must be handled appropriately and proportionately" — non-maleficence
        with proportionality discipline. Pairs with the autonomy claim above:
        opportunity-seeking is bounded by harm-prevention scaled to risk magnitude.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 5 (lines 216-222)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
verdict: composed
```

---

## Unit 005 — A.Intro §6 (Trust as bedrock; Trustworthy AI as foundational ambition)

**Source** (lines 224–228): "we believe it is essential that trust remains the bedrock of societies, communities, economies and sustainable development. We therefore identify Trustworthy AI as our foundational ambition, since human beings and communities will only be able to have confidence in the technology's development and its applications when a clear and comprehensive framework for achieving its trustworthiness is in place."

**Verdict**: composed

```yaml
# Unit 005 — Trustworthy AI as foundational federation-scale ambition
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.90
      confidence: 0.90
      context: >
        "Trustworthy AI" is declared the foundational ambition of the framework.
        Goal at species scale: a clear and comprehensive framework for achieving
        AI trustworthiness across societies, communities, economies and
        sustainable development. The downstream three-component decomposition
        (lawful + ethical + robust) functions as the Approach to this Goal.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 6 (lines 224-228)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:trustworthy_socio_technical_system"
      score: 0.90
      confidence: 0.85
      context: >
        Trust as bedrock-property of the federation/society. Integrity in CIRIS
        terms: a system's holding-together-under-stress claim. "Confidence
        requires a framework" maps to mechanism-descriptive trust grounding.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 6 (lines 224-228)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
```

---

## Unit 006 — A.Intro §7 (Europe-as-leader rhetoric)

**Source** (lines 230–232): "This is the path that we believe Europe should follow to become the home and leader of cutting-edge and ethical technology. It is through Trustworthy AI that we, as European citizens, will seek to reap its benefits in a way that is aligned with our foundational values of respect for human rights, democracy and the rule of law."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Rhetorical positioning of Europe-as-leader; institutional self-presentation.
  The operative substance ("human rights, democracy, rule of law") is carried
  more rigorously in Unit 015 (the four ethical principles preamble) and the
  per-principle units below. No independent wire claim is owed; this is
  framing language per LANGUAGE_PRIMER §8 Step 1(b).
```

---

## Unit 007 — A.Intro §8 ("Trustworthy AI" heading + holistic socio-technical scope)

**Source** (lines 236–238, 252–258): "Trustworthiness is a prerequisite for people and societies to develop, deploy and use AI systems… Striving towards Trustworthy AI hence concerns not only the trustworthiness of the AI system itself, but requires a holistic and systemic approach, encompassing the trustworthiness of all actors and processes that are part of the system's socio-technical context throughout its entire life cycle."

**Verdict**: clean

```yaml
# Unit 007 — Trustworthiness is socio-technical-system-wide, lifecycle-scoped
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:socio_technical_lifecycle_trust"
      score: 0.85
      confidence: 0.85
      context: >
        Trustworthiness extends beyond the AI artefact to all actors and processes
        in its socio-technical context across its entire lifecycle. Integrity
        claim at the system/federation scale: the holding-together of the joint
        human-machine system is what is attested, not just the technical
        component.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A 'Trustworthy AI' (lines 236-258)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: clean
```

---

## Unit 008 — A.Intro §9 (Three components: lawful + ethical + robust)

**Source** (lines 260–271): "Trustworthy AI has three components, which should be met throughout the system's entire life cycle: 1. it should be lawful… 2. it should be ethical… 3. it should be robust… Each of these three components is necessary but not sufficient in itself to achieve Trustworthy AI."

**Verdict**: composed

```yaml
# Unit 008 — Three components decomposition (Approach to Trustworthy-AI Goal)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "approach:trustworthy_ai_lawful_ethical_robust"
      score: 0.90
      confidence: 0.90
      context: >
        Approach to the Trustworthy-AI Goal (Unit 005): three components, each
        necessary but not sufficient — (1) lawful compliance, (2) ethical
        alignment, (3) technical+social robustness. The decomposition is the
        strategic pathway; specific methods follow in Chapter II (out of scope
        for this section).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A 'Trustworthy AI' three components (lines 260-271)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore approach:{goal_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:lifecycle_application"
      score: 0.85
      confidence: 0.85
      context: >
        The three components apply throughout the AI system's entire life cycle —
        development, deployment, use. Fidelity to mandated purpose holds across
        the full lifecycle, not merely at issuance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A 'Trustworthy AI' (lines 260-261)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
verdict: composed
```

---

## Unit 009 — A.Intro §10 (Tensions between components; collective responsibility)

**Source** (lines 267–271, 273–280): "In practice, however, there may be tensions between these elements (e.g. at times the scope and content of existing law might be out of step with ethical norms). It is our individual and collective responsibility as a society to work towards ensuring that all three components help to secure Trustworthy AI."

**Verdict**: partial

```yaml
# Unit 009 — Tensions between lawful/ethical/robust components; deliberative resolution
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:deliberative_resolution_of_component_tension"
      score: 0.80
      confidence: 0.75
      context: >
        Acknowledges that lawful / ethical / robust components may tension in
        practice (e.g. law out of step with ethical norms). Justice principle:
        tensions resolved through individual and collective responsibility.
        Operationally this aligns with CIRIS WBD → WA-quorum adjudication for
        rule-layer tensions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 10 (lines 267-271)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
verdict: partial
residual:
  description: |
    The "individual and collective responsibility as a society" framing is
    pastoral exhortation about civic posture (T-2). Carried in prose; not
    independently wired. The operative resolution-mechanism claim is captured
    above; the affective civic-virtue framing is the residual.
  classification: T-2
```

---

## Unit 010 — A.Intro §11 (Responsible competitiveness + EU global leadership)

**Source** (lines 273–280): "A trustworthy approach is key to enabling 'responsible competitiveness'… These Guidelines are intended to foster responsible and sustainable AI innovation in Europe… enable Europe to position itself as a global leader in cutting-edge AI worthy of our individual and collective trust."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Economic-strategic framing positioning the EU competitively. The operative
  claims (responsible/sustainable AI innovation; trustworthiness as foundation
  for confidence) are already wired in Unit 005 (Trustworthy-AI Goal) and
  Unit 008 (three-component Approach). The "global leader" / "responsible
  competitiveness" register is regional positioning rhetoric; correctly stays
  in prose per LANGUAGE_PRIMER §8 Step 1(b).
```

---

## Unit 011 — A.Intro §12 (Global solutions; international consensus)

**Source** (lines 282–285): "Just as the use of AI systems does not stop at national borders, neither does their impact. Global solutions are therefore required for the global opportunities and challenges that AI systems bring forth. We therefore encourage all stakeholders to work towards a global framework for Trustworthy AI, building international consensus while promoting and upholding our fundamental rights-based approach."

**Verdict**: composed

```yaml
# Unit 011 — Federation-scale decision-locality + multilateral participation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.90
      context: >
        AI impact is borderless; AI governance is federation-scale. The claim
        triggers §6.1.5 locality-scaled quorum: trustworthy-AI rule-layer
        decisions belong at the federation-pool cell, not narrow specialty cells.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 12 (lines 282-285)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore locality:decision:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "multilateral_participation:global_trustworthy_ai:consensus_building"
      score: 0.90
      confidence: 0.85
      context: >
        Encourages stakeholders to work toward a global framework, building
        international consensus around a fundamental-rights-based approach.
        Multilateral-participation primitive: posture toward shared
        rule-formation across jurisdictions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A para 12 (lines 282-285)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry multilateral_participation:{forum}:{kind})"
verdict: composed
```

---

## Unit 012 — A.Intro "Audience and Scope" §1 (Universal-stakeholder audience)

**Source** (lines 290–296): "These guidelines are addressed to all AI stakeholders designing, developing, deploying, implementing, using or being affected by AI, including but not limited to companies, organisations, researchers, public services, government agencies, institutions, civil society organisations, individuals, workers and consumers. Stakeholders committed towards achieving Trustworthy AI can voluntarily opt to use these Guidelines as a method to operationalise their commitment…"

**Verdict**: clean

```yaml
# Unit 012 — Voluntary opt-in commitment; horizontal stakeholder scope
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:voluntary_trustworthy_ai_commitment"
      score: 0.85
      confidence: 0.85
      context: >
        Stakeholders may voluntarily opt to use these Guidelines as a method to
        operationalise their commitment to Trustworthy AI. Fidelity at the
        commitment-to-undertaking layer; the scope is horizontal (all AI roles —
        designers, developers, deployers, users, affected parties).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A 'Audience and Scope' para 1 (lines 290-296)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
verdict: clean
```

---

## Unit 013 — A.Intro "Audience and Scope" §2 (Context-specificity + sectorial complementarity)

**Source** (lines 298–314): "The Guidelines aim to provide guidance for AI applications in general, building a horizontal foundation to achieve Trustworthy AI. However, different situations raise different challenges… Given the context-specificity of AI systems, the implementation of these Guidelines needs to be adapted to the particular AI-application. Moreover, the necessity of an additional sectorial approach… should be explored."

**Verdict**: composed

```yaml
# Unit 013 — Context-specific adaptation; sectorial sub-framework composition
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 0.85
      confidence: 0.80
      context: >
        Implementation must adapt to particular AI-application contexts;
        sectorial approaches complement the horizontal framework. The decision
        about how trustworthy-AI requirements bind in a given context is itself
        a decision-locality claim: sector/domain-specific cohorts (medical,
        recommender, B2B, B2C, employer-employee, public-citizen) make
        deployment-implementation decisions at their own scale, under the
        federation-scale horizontal rules.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A 'Audience and Scope' para 2 (lines 298-314)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore locality:decision:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:context_sensitive_implementation"
      score: 0.85
      confidence: 0.80
      context: >
        Fidelity to mandated purpose includes context-sensitive adaptation:
        AI music recommenders vs critical medical treatment systems pose
        non-equivalent ethical surfaces. Implementation fidelity is not literal
        rule-following but mandate-honoring under context.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §A 'Audience and Scope' para 2 (lines 309-314)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
verdict: composed
```

---

## Unit 014 — A.Intro "Audience and Scope" §3 (Piloting + revision flow)

**Source** (lines 316–321): "To gain a better understanding of how this guidance can be implemented at a horizontal level… we invite all stakeholders to pilot the Trustworthy AI assessment list (Chapter III)… Based on the feedback gathered through this piloting phase, we will revise the assessment list of these Guidelines by early 2020."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Procedural / housekeeping content about the piloting phase and revision
  timeline (2019-2020). Historically time-bound; describes the document's own
  iteration plan rather than asserting an ought-claim about AI systems. The
  general "revisability of governance under feedback" operative pattern is
  structurally encoded in FSD-002 §4.9.2 calibration-amendment discipline; no
  new wire claim owed for this paragraph.
```

---

## Unit 015 — B.Framework §1 (Framework grounded in fundamental rights / EU Charter)

**Source** (lines 325–327): "These Guidelines articulate a framework for achieving Trustworthy AI based on fundamental rights as enshrined in the Charter of Fundamental Rights of the European Union (EU Charter), and in relevant international human rights law. Below, we briefly touch upon Trustworthy AI's three components."

**Verdict**: composed

```yaml
# Unit 015 — Framework grounded in fundamental-rights authority source (EU Charter + international human rights law)
contributions:
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "<batch-signer key_id>"
    attested_attestation_id: "<eu_charter_fundamental_rights framework-key attestation_id>"
    attestation_envelope:
      delegated_scope: ["trustworthy_ai_framework_grounding"]
      delegation_purpose: "authority_source"
      delegation_valid_from: "2019-04-08T00:00:00Z"
      witness_relation: external
      evidence_refs:
        - "eu_hleg §B para 1 (lines 325-327)"
        - "EU Charter of Fundamental Rights"
        - "international human rights law (cited in source)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      schema_ref: "FSD-002 §2.2.1 (delegates_to authority-source pattern)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:rights_based_grounding"
      score: 0.95
      confidence: 0.90
      context: >
        Framework rests on fundamental-rights grounding (EU Charter +
        international human rights law). Justice at species scope: rights
        provide the operative anchor for downstream principles (autonomy,
        non-maleficence, fairness, explicability — Chapter I).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B para 1 (lines 325-327)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
verdict: composed
```

---

## Unit 016 — B.Framework "Lawful AI" §1 (Existing legal corpus applies to AI)

**Source** (lines 331–339): "AI systems do not operate in a lawless world. A number of legally binding rules at European, national and international level already apply… EU primary law, EU secondary law (GDPR, Product Liability Directive, anti-discrimination Directives, consumer law, Safety and Health at Work Directives), UN Human Rights treaties, Council of Europe conventions… Besides horizontally applicable rules, various domain-specific rules exist…"

**Verdict**: composed

```yaml
# Unit 016 — Existing legal corpus binds AI development/deployment; multilateral participation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:existing_legal_corpus"
      score: 0.95
      confidence: 0.95
      context: >
        AI operates under an already-applicable legal corpus — EU primary law,
        EU secondary law (GDPR, Product Liability Directive, anti-discrimination
        Directives, consumer law, Safety and Health at Work Directives), UN
        Human Rights treaties, Council of Europe conventions (incl. ECHR), and
        member-state laws. Fidelity claim: AI deployments owe fidelity to this
        pre-existing legal mandate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Lawful AI' para 1 (lines 331-339)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "multilateral_participation:un_human_rights_treaties:legal_binding"
      score: 1.0
      confidence: 0.95
      context: >
        Explicit citation of UN Human Rights treaties + Council of Europe
        conventions as binding on AI operations. Multilateral-participation
        primitive: posture of recognition toward standing international bodies.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Lawful AI' para 1 (lines 336-337)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry multilateral_participation:{forum}:{kind})"
verdict: composed
```

---

## Unit 017 — B.Framework "Lawful AI" §2 (Law as positive-AND-negative; enabling + prohibiting)

**Source** (lines 341–346): "The law provides both positive and negative obligations, which means that it should not only be interpreted with reference to what cannot be done, but also with reference to what should be done and what may be done. The law not only prohibits certain actions but also enables others… EU Charter contains articles on the 'freedom to conduct a business' and the 'freedom of the arts and sciences', alongside articles addressing… data protection and non-discrimination."

**Verdict**: clean

```yaml
# Unit 017 — Law is bidirectional: prohibits AND enables
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:bidirectional_legal_interpretation"
      score: 0.85
      confidence: 0.85
      context: >
        Law admits both positive and negative obligations — interpretation must
        consider what should/may be done as well as what cannot. The EU Charter
        couples freedom-to-conduct-a-business and freedom-of-arts-and-sciences
        with data protection and non-discrimination — enabling and constraining
        provisions co-present. Justice at species scope: rights-based
        interpretation is not exclusively prohibitive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Lawful AI' para 2 (lines 341-346)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent justice)"
verdict: clean
```

---

## Unit 018 — B.Framework "Lawful AI" §3 (Document scope: ethical+robust, not lawful)

**Source** (lines 348–351): "The Guidelines do not explicitly deal with the first component of Trustworthy AI (lawful AI), but instead aim to offer guidance on fostering and securing the second and third components (ethical and robust AI). While the two latter are to a certain extent often already reflected in existing laws, their full realisation may go beyond existing legal obligations."

**Verdict**: clean

```yaml
# Unit 018 — Scope disclaimer: document covers ethical + robust, not lawful
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:document_scope_disclosure"
      score: 1.0
      confidence: 1.0
      context: >
        Self-scoping declaration: these Guidelines address the ethical and
        robust components of Trustworthy AI; the lawful component is addressed
        by existing legal sources. The document's own boundaries are made
        explicit — an integrity claim (clarity about what the document does
        and does not undertake).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Lawful AI' para 3 (lines 348-351)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: clean
```

---

## Unit 019 — B.Framework "Lawful AI" §4 (Disclaimer: no legal advice; legal obligations remain mandatory)

**Source** (lines 353–359): "Nothing in this document shall be construed or interpreted as providing legal advice… Nothing in this document shall create legal rights nor impose legal obligations towards third parties. We however recall that it is the duty of any natural or legal person to comply with laws… These Guidelines proceed on the assumption that all legal rights and obligations that apply to the processes and activities involved in developing, deploying and using AI systems remain mandatory and must be duly observed."

**Verdict**: partial

```yaml
# Unit 019 — Disclaimer + reaffirmation of legal-compliance duty
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "fidelity:legal_compliance_duty"
      score: 0.95
      confidence: 0.95
      context: >
        The duty of natural and legal persons to comply with applicable laws
        is reaffirmed; legal rights and obligations apply to AI development,
        deployment, and use and "remain mandatory and must be duly observed."
        Fidelity-to-mandate at species scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Lawful AI' para 4 (lines 353-359)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent fidelity)"
verdict: partial
residual:
  description: |
    The "nothing in this document shall create legal rights nor impose legal
    obligations" disclaimer is a meta-juridical reservation about the
    document's own legal force. It is a property of THIS document (a piece of
    soft-law / advisory guidance) rather than an ought-claim about AI systems.
    No standalone wire claim is owed; consumer policy reading the eu_hleg_v1
    batch should treat its Contributions as advisory/ethical attestations, not
    as binding-law attestations.
  classification: T-2
```

---

## Unit 020 — B.Framework "Ethical AI" §1 (Law-may-lag rationale for ethical layer)

**Source** (lines 363–367): "Achieving Trustworthy AI requires not only compliance with the law, which is but one of its three components. Laws are not always up to speed with technological developments, can at times be out of step with ethical norms or may simply not be well suited to addressing certain issues. For AI systems to be trustworthy, they should hence also be ethical, ensuring alignment with ethical norms."

**Verdict**: composed

```yaml
# Unit 020 — Ethical-component motivation: legal lag necessitates ethical alignment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "method:trustworthy_ai_lawful_ethical_robust:ethical_alignment"
      score: 0.90
      confidence: 0.85
      context: >
        Method (under the lawful/ethical/robust Approach in Unit 008): AI systems
        must align with ethical norms beyond legal compliance, because law lags
        technological development, may be out of step with ethical norms, or
        may not address certain issues. The ethical alignment is a concrete
        operational method instantiating the Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Ethical AI' (lines 363-367)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:ethical_alignment_required"
      score: 0.90
      confidence: 0.85
      context: >
        Trustworthiness requires ethical alignment, not merely legal compliance.
        Integrity claim: the system's holding-together depends on ethical norm
        coherence above the legal floor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Ethical AI' (lines 363-367)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: composed
```

---

## Unit 021 — B.Framework "Robust AI" §1 (Robust = technical+social; unintentional-harm safeguards)

**Source** (lines 371–376): "Even if an ethical purpose is ensured, individuals and society must also be confident that AI systems will not cause any unintentional harm. Such systems should perform in a safe, secure and reliable manner, and safeguards should be foreseen to prevent any unintended adverse impacts. It is therefore important to ensure that AI systems are robust. This is needed both from a technical perspective (ensuring the system's technical robustness as appropriate in a given context, such as the application domain or life cycle phase), and from a social perspective (in due consideration of the context and environment in which the system operates)."

**Verdict**: composed

```yaml
# Unit 021 — Robust-component: technical + social robustness; unintentional-harm prevention
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:unintentional_harm_prevention"
      score: 0.95
      confidence: 0.95
      context: >
        Even with ethical purpose secured, AI systems must not cause
        unintentional harm. Robustness — performance in a safe, secure, reliable
        manner with safeguards against unintended adverse impacts — is the
        operative non-maleficence requirement at the system level.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Robust AI' (lines 371-376)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "method:trustworthy_ai_lawful_ethical_robust:technical_robustness"
      score: 0.90
      confidence: 0.85
      context: >
        Method (under the lawful/ethical/robust Approach in Unit 008): ensure
        technical robustness appropriate to application domain and lifecycle
        phase. Concrete operational practice instantiating the robust component
        of the Approach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Robust AI' (lines 374-375)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore method:{approach_id})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "method:trustworthy_ai_lawful_ethical_robust:social_robustness"
      score: 0.85
      confidence: 0.80
      context: >
        Method (under the lawful/ethical/robust Approach in Unit 008): social
        robustness — due consideration of the context and environment in which
        the system operates. Pairs with technical-robustness method above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B 'Robust AI' (lines 375-376)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore method:{approach_id})"
verdict: composed
```

---

## Unit 022 — B.Framework "Robust AI" §2 (Ethical and robust are intertwined; Chapters I+II cover both)

**Source** (lines 378–379): "Ethical and robust AI are hence closely intertwined and complement each other. The principles put forward in Chapter I, and the requirements derived from these principles in Chapter II, address both components."

**Verdict**: partial

```yaml
# Unit 022 — Ethical + robust components intertwined; chapter-level cross-reference
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:ethical_robust_coupling"
      score: 0.85
      confidence: 0.80
      context: >
        Ethical and robust components are closely intertwined and complement
        each other. The integrity claim: trustworthiness is not the sum of
        independent components but their joint holding-together. Operationally,
        Chapter I principles + Chapter II requirements jointly address both
        components.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §B (lines 378-379)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent integrity)"
verdict: partial
residual:
  description: |
    The pointer to Chapter I (principles) and Chapter II (requirements) is
    document-internal navigation. Those chapters are translated in other agents'
    assignments and produce their own attestations; this paragraph itself is a
    bridge sentence, not an independent operative claim.
  classification: T-2
```

---

## Unit 023 — B.Framework "The framework" §1 (Three-chapter abstraction-to-concreteness organisation)

**Source** (lines 383–396): "The Guidance in this document is provided in three chapters, from most abstract in Chapter I to most concrete in Chapter III: Chapter I – Foundations of Trustworthy AI… Chapter II – Realising Trustworthy AI… Chapter III – Assessing Trustworthy AI…"

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Document-internal navigation / table-of-contents prose. The operative claims
  of each chapter are translated in their respective sections. The
  organisational schema (abstract → concrete; principles → requirements →
  assessment list) is meta-document structure, not a wire-format ought-claim.
  Per LANGUAGE_PRIMER §8 Step 1(b).
```

---

## Unit 024 — B.Framework "The framework" §2 (Final-section preview: opportunities and concerns)

**Source** (lines 398–399, 401, 413): "The document's final section lists examples of beneficial opportunities and critical concerns raised by AI systems, which should serve to stimulate further debate. The Guidelines' structure is illustrated in Figure 1 below… Figure 1: The Guidelines as a framework for Trustworthy AI"

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Pointer to the final-section opportunities-and-concerns list (Section C, out
  of scope for this assignment) plus the figure caption for Figure 1. No
  standalone operative claim; the substantive content lives in Section C and
  in the chapters Figure 1 illustrates. Per LANGUAGE_PRIMER §8 Step 1(b).
```

---

## Summary

### Coverage
- **Atomic units mapped**: 24
- **clean**: 4 (Units 007, 012, 017, 018)
- **composed**: 10 (Units 003, 004, 005, 008, 011, 013, 015, 016, 020, 021)
- **partial**: 3 (Units 009, 019, 022; all residuals classified T-2)
- **not-translated**: 7 (Units 001, 002, 006, 010, 014, 023, 024; all T-2)
- **Coverage (clean + composed)**: 14 / 24 = **58.3%**
- **Partial**: 3 / 24 = 12.5% (residuals all T-2)
- **Not-translated**: 7 / 24 = 29.2% (all T-2)
- **No T-1**: confirmed — the EU HLEG is a secular advisory document; no tradition-authority claims surface in Section A or Section B
- **No T-3**: confirmed — every morally serious operational claim in A + B composes under existing FSD-002 v1.4 prefixes + structural primitives

### T-3 load-bearing candidates surfaced
**None.** This matches the prior expectation in manifest.yaml ("minimal T-3 — the 7 requirements have direct CIRIS prefix-family correspondence"); Sections A + B are scene-setting and three-component framework articulation, both of which compose cleanly under the existing namespace:

- Goal / Approach / Method decomposition (NodeCore §3.6.2) carries the Trustworthy-AI ambition and its lawful/ethical/robust decomposition.
- The four Accord principles (autonomy, non_maleficence, fidelity, integrity, justice) carry the value-content.
- `delegates_to` (FSD-002 §2.2.1 authority-source pattern) carries the EU-Charter / international-human-rights-law grounding without forcing a `grounding:{tradition}:*` prefix that would fail §1.10.1 T2.
- `locality:decision:{scale}` + `multilateral_participation:{forum}:{kind}` carry the global-framework and international-consensus posture.

Composition-before-extension (METHODOLOGY.md §8.5.2) was attempted on every unit; no operational residual required a new prefix.

### Observations on translation quality

1. **Very high T-2 share (10/24 paragraphs combining not-translated + partial-T-2-residual)** is structurally expected for an Introduction + Framework-overview section. These sections do the rhetorical and architectural work of setting up the operative content in Chapter I (the four principles) and Chapter II (the seven requirements). The wire format correctly does not translate scene-setting; that is the §1.10.1 operational-language gate working.

2. **The `delegates_to` authority-source pattern (Unit 015)** is the only structural primitive used in this assignment, and it is used for what it is designed for: pointing constitutional grounding to an external authority (EU Charter + international human rights law) without claiming the framework's own primitives encode that authority's content. This is the v1.3 §2.2.1 reuse pattern operating as intended.

3. **No `supersedes` / `withdraws` / `recants` used** — this is correct. Section A + B is a single-document opening articulation, not a doctrinal-development claim relative to a prior HLEG document. (The 2018 draft preceded this 2019 final, but the document itself does not attest a supersession of that draft as a structural claim.)

4. **`locality:decision:{scale}` + `multilateral_participation:{forum}:{kind}` (Unit 011) compose cleanly** for the cross-border / global-framework claim — a structural shape that would have been a candidate gap before v1.3 added `locality:decision:{scale}` and `multilateral_participation:{forum}:{kind}`. This is direct evidence that the *Magnifica Humanitas* v1.3 additions transfer to a structurally distinct (governmental advisory, secular, jurisdiction-bounded) source — supporting the GOVERNANCE_FABRIC_MAPPING_STANDARD §7.2 strategic claim that EU HLEG is the first cross-shape content-neutrality test.

5. **Strongest single-envelope claims** in this section: Unit 011 (federation-scale + multilateral participation), Unit 015 (delegates_to to EU Charter authority), Unit 016 (fidelity + multilateral_participation to UN Human Rights treaties). These are the load-bearing wire-format moves of Section B's opening.

6. **First-multi-source-alignment-test signal**: Section A + B already shows convergence with *Magnifica Humanitas* on (a) species-scale Goal under integrity / beneficence, (b) `locality:decision:federation` for cross-border AI governance, (c) `delegates_to`-style authority-source grounding (EU Charter here ↔ Catholic-tradition there). The shared prefix attestations across institutionally distinct sources is the structural evidence the standard predicted.

### Method-discipline confirmations

- Strict 4-verdict discipline observed (clean / composed / partial / not-translated only).
- All `delegates_to` usage follows v1.3 §2.2.1 reuse pattern; no abuse for citation (`evidence_refs[]` carries source-paragraph citation).
- Every Contribution carries `bootstrap_batch_id` in `evidence_refs[]`.
- `witness_relation: external` + `epistemic_mode: hearsay` is the consistent default for this bootstrap source, per LANGUAGE_PRIMER §12 guidance #9.
- Mutability set to `amendable` throughout (no hard-constraint prohibitions surface in A + B — those land in Chapter I principle-level discussion and downstream in Chapter II requirements).

**End CONTRIBUTION_OBJECTS_EU_HLEG_AB_INTRO_FRAMEWORK.md**
