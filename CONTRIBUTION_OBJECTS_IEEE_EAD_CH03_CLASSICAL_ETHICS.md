# CONTRIBUTION_OBJECTS_IEEE_EAD_CH03_CLASSICAL_ETHICS.md
# IEEE Ethically Aligned Design (1st ed., 2019) — Chapter 3 "Classical Ethics in A/IS"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 1731–3580)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

Chapter 3 surveys classical ethics methodologies (philosophical and culture-based)
as candidate scaffolds for reasoning about A/IS. It engages: Western virtue ethics
(Aristotle, *eudaimonia*, *telos*); Kantian deontology (categorical imperative,
humanity-as-end); utilitarianism / consequentialism (utility principle);
feminist ethics-of-care (Noddings); Millian compatibilist autonomy; Responsible
Research and Innovation (RRI); Buddhist ethics (liberation/nirvana, anatta,
relational metaphysics); African Ubuntu (*motho ke motho ka batho babang*,
relational personhood); Japanese Shinto-influenced techno-animism (*kami*,
*karakuri ningyo*). Confucianism is named in the introduction as one of the
non-Western traditions worth engaging but is **not given its own dedicated
section** in this 1st-edition chapter (footnote 1: future editions to include
Judaism and Islam; Confucianism similarly under-developed). Greek arete /
phronesis appear in passing.

This chapter is the **direct counterpart to CIRIS `pdma_framing.yml`
multi-tradition polyglot anchoring**. The CIRIS framing already names six
principles richly across traditions: Confucian *ren* / 仁; Buddhist *ahimsa*,
*sammā-vācā*, anatta posture, *sabr* (Islamic); Ubuntu (relational personhood);
Hellenic *eudaimonia*, *alētheia*, *phronesis*; Hebraic *chesed*, *tikkun olam*;
Egyptian *ma'at*; Igbo *igwe-bụ-ike*; Japanese *amae*; Korean *jeong*; Sanskrit
*seva*, *ahimsa*; Islamic *fitra*, *taqwa*. The framing **does NOT explicitly
name**: Shinto-influenced techno-animism (closest: implicit through Japanese
*amae*, but the *kami-of-artifacts* shape is not present); Kantian deontology
by name (the framework engages duty-shape via *chesed* covenantal-loyalty and
*imago Dei* dignity-as-floor, but does not name Kant); utilitarian aggregation
(the framing actively names as an *attractor* to discount, not a positive
anchor); feminist ethics-of-care (closest: *amae* + *jeong*, but the
care-ethics-as-feminist-tradition lineage is implicit). This asymmetry is
the calibration evidence: where CIRIS already names a tradition, the chapter's
operational claims translate cleanly; where it does not, the tradition-internal
arguments correctly stay T-1.

This output groups paragraphs by which tradition / philosophical lineage they
primarily reference, per the prompt's discipline. Each section ends with a
per-tradition coverage summary.

---

# PART A — INTRODUCTION + WESTERN PHILOSOPHICAL TRADITIONS
# (Section 1: Definitions; the Western analytic-tradition spine)

---

## §3.0 — Chapter introduction: classical ethics applied to A/IS design

```yaml
# Lines 1731–1760 — chapter framing: classical ethics as scaffold for A/IS algorithmic design
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:design_classical_ethics_grounding"
      score: 0.85
      confidence: 0.85
      context: >
        A/IS design must engage classical ethics methodologies (philosophical
        and religious/cultural) to detect the cultural and ethical presumptions
        embedded in algorithmic choices. Cross-traditional grounding is a
        design-integrity claim, not a single-tradition appeal.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 introduction lines 1731–1760"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §III the-six-principles-polyglot-anchoring)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: "The 'over two thousand years' lineage framing is rhetorical; structurally only the design-integrity claim translates."
```

---

## §3.1.1 — Western classical economy frames: individual, family, polis

```yaml
# Lines 1786–1820 — Plato/Aristotle's three classical economic domains (oikos, polis); modernity disconnection critique
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:economic_political_dimensions_recognition"
      score: 0.7
      confidence: 0.7
      context: >
        Modern individual-morality discourse on A/IS has been "disconnected
        from economics and politics"; classical Western ethics located ethos
        in oikos and polis. A/IS ethical discourse must restore the economic
        and political dimensions rather than reducing to the "morality of a
        worldless and isolated machine."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1786–1820"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    The specific Aristotelian three-domain ontology (individual / family / polis)
    is tradition-internal Greek philosophy. The operational claim — A/IS ethics
    must not collapse into individualistic-isolated-machine framing — translates;
    the underlying Aristotelian *telos*-of-the-polis metaphysics does not.
  classification: T-1
nuance_lost: "The Aristotelian metaphysical grounding of why oikos and polis matter (telos, the human as zoon politikon) stays in the tradition's native register."
```

---

## §3.1.2 — Kant's worldless autonomous subject + the A/IS parallel

```yaml
# Lines 1779–1786 + 1789–1819 — Kant's categorical imperative locates morality within the subject;
# the worldless-isolated-subject anthropology is paradoxically what A/IS now embodies
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  This is a Kant-internal historical-philosophical argument: that Kantian
  ethics produced a "worldless isolated subject" and A/IS aspires to that
  same isolation paradigm. The structural claim that operationalises this
  ("design must address whether A/IS treat humans as means or ends") is
  carried by §3.1.3 below; the Kantian-internal genealogical claim itself
  belongs to the Kant-scholarship tradition's own authority. CIRIS
  pdma_framing.yml engages duty-shape via chesed (covenantal loyalty)
  and imago Dei (dignity-as-floor) but does not name Kant by tradition;
  the Kant-internal argument correctly stays T-1.
nuance_lost: "Kant-internal critique of Kant (autonomy-as-isolation produced modernity's ethical pathology) belongs to Kant scholarship, not to CIRIS wire surface."
```

---

## §3.1.3 — Virtue ethics: eudaimonia, golden mean, iterative cultivation

```yaml
# Lines 1834–1846 + 1867–1879 — Aristotle's virtue ethics; flourishing as action not state;
# habituation; golden mean; in A/IS context: iterative-learning model + counterbalance to economic excess
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:flourishing_as_iterative_practice"
      score: 0.9
      confidence: 0.85
      context: >
        Virtue ethics offers two operational values for A/IS: (a) a model for
        iterative learning and growth (moral value informed by context and
        practice, not static rule-compliance); (b) a framework to
        counterbalance excess in economically-driven environments. Eudaimonia
        as flourishing-through-action maps to CIRIS pdma_framing §III seva
        and the cross-tradition beneficence anchor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1867–1879"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §III善行・सेवा・eudaimonia-beneficence)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:design_iterative_virtue_cultivation"
      score: 0.8
      confidence: 0.8
      context: >
        A/IS design discipline: treat moral learning as habituated practice,
        not rule-compliance. Operationalises as method-level discipline
        (Family B): design processes that iterate against the golden mean
        rather than encoding fixed rule-sets only.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1867–1879"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
verdict: composed
nuance_lost: "The Aristotelian-internal metaphysics of telos and the role of the polis in cultivating virtuous character is the tradition's own register; the operational shape (iterative practice + counterbalance to excess) translates cleanly."
```

---

## §3.1.4 — Deontological ethics: Kant's categorical imperative + humanity formulation

```yaml
# Lines 1847–1903 — Kantian deontology; categorical imperative; humanity formulation (treat as end never merely as means);
# rules-not-personal-choice universalisability; A/IS implications for human dignity
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:human_dignity_as_floor"
      score: 1.0
      confidence: 0.95
      context: >
        "Treat humanity, whether in your own person or in the person of any
        other, never simply as a means, but always at the same time as an
        end" — produces duties to respect humanity and human dignity. Maps
        directly to the CIRIS autonomy principle (FSD-002 §3.1) and the
        pdma_framing §III imago Dei / fitra anchor (dignity granted, not
        earned, not flexing with utility or capacity).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1893–1903"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §III स्वायत्तता・imago-Dei・amae-respect-autonomy)"
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
      confidence: 0.9
      context: >
        Kantian rule against treating humans as mere means → A/IS-design
        constraint preventing instrumentalisation of users. Hard-constraint
        polarity in the prohibition family.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1898–1903"
        - "ContributionRef(source_material/prohibitions.py §MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraint)"
verdict: composed
nuance_lost: "Kant-internal argument structure (the universalisability test as a rational-agent procedure) is the tradition's native form; the operational obligation (treat-as-end + no-instrumentalisation) translates."
```

---

## §3.1.5 — Kant + A/IS: limit functions so as not to replace human judgment

```yaml
# Lines 1907–1925 — A/IS implications of humanity formulation: may require limiting A/IS so they don't
# replace human judgment/discretion/reasoning; healthcare-robot privacy + safeguarding
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:human_oversight_governance"
      score: 0.9
      confidence: 0.85
      context: >
        Duty to respect human dignity may require limitations on A/IS
        functions so they do not "completely replace humans, human
        functions, and/or human central thinking activities such as
        judgment, discretion, and reasoning." Maps to the EU HLEG §1.1.c
        human-oversight requirement; operationalises Kantian humanity
        formulation as oversight-governance constraint.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1907–1925"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:privacy_violation"
      score: -1.0
      confidence: 0.85
      context: >
        Healthcare-robot example: A/IS must not divulge personal information
        to third parties or compromise physical or mental well-being. Hard
        constraint in the prohibition family.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1923–1932"
        - "ContributionRef(source_material/prohibitions.py §PRIVACY)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception"
      score: -1.0
      confidence: 0.9
      context: >
        Programming requirement: prevent A/IS from deceiving or manipulating
        humans. Hard-constraint.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1930–1932"
        - "ContributionRef(source_material/prohibitions.py §DECEPTION_FRAUD)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
verdict: composed
nuance_lost: "The Kantian rationale (humanity-as-end-in-itself produces these duties) is the lineage anchor; the operational duties translate cleanly as oversight + privacy + anti-deception hard-constraints."
```

---

## §3.1.6 — Profit/financial incentives + ends-means displacement (Kant + Mill)

```yaml
# Lines 1934–1946 — financial incentives may justify ends-means treatment; e.g., cutting back rigorous testing.
# Maintaining human agency is a manifestation of duty to dignity. Right to know when interacting with A/IS;
# consent for A/IS interaction.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:profit_driven_safety_corner_cutting"
      score: -0.8
      confidence: 0.85
      context: >
        Cutting back rigorous testing of A/IS before market is a foreseeable-harm
        choice driven by financial incentive; an ahimsa-grade violation in the
        pdma_framing register and a structural risk-management failure. Severity
        scalar in non_maleficence.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1934–1942"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:capabilities_limitations_disclosure"
      score: 0.9
      confidence: 0.9
      context: >
        "A human has the right to know when they are interacting with A/IS,
        and may require consent for any A/IS interaction." Operational
        transparency claim; aligns with EU HLEG §1.4.c (Communication) and
        the prohibited:autonomous_deception hard constraint.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1944–1946"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: "—"
```

---

## §3.1.7 — Utilitarian / consequentialist ethics: utility, long-term effects, social justice

```yaml
# Lines 1904–1925 (utility block) — utilitarianism: maximize utility for greatest number; warns against short-term;
# A/IS developers must consider long-term effects; social justice paramount;
# A/IS impact on employment must be examined
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:long_term_consequence_consideration"
      score: 0.8
      confidence: 0.8
      context: >
        "It is the responsibility of the A/IS developers to consider long-term
        effects" — non_maleficence extended to foreseeable systemic and
        temporal consequences (the ahimsa register in pdma_framing §III).
        The utility maximisation framing is the tradition's native; the
        operational obligation translates as long-term consequence-attention
        in the non_maleficence anchor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1904–1925 (utilitarian block)"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §III無危害・अहिंसा・ahimsa-non-maleficence)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:social_justice_employment_capability_impact"
      score: 0.85
      confidence: 0.8
      context: >
        Social justice is paramount: A/IS must be assessed for whether it
        contributes to humanity or "negatively impact[s] employment or
        other capabilities." Maps to the labor-displacement and distributive
        concerns; composes with detection:correlated_action:aggregate_footprint:* +
        non_maleficence:labor_displacement_unacknowledged (per LANGUAGE_PRIMER
        §11.14 closed-by-documentation composition).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1916–1925"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: "Utility-maximisation as a moral procedure is the utilitarian tradition's native register and is actively flagged as an *attractor* in CIRIS pdma_framing §I (the secular-analytic-ethics consensus pull); the operational obligation (long-term consequence-attention + employment-impact attention) translates without endorsing the aggregation procedure as decision rule."
```

---

## §3.1.8 — Utilitarian: benefits obvious to all stakeholders

```yaml
# Lines 1922–1925 — where A/IS can supplement humanity, design "in such a way that the benefits
# are obvious to all the stakeholders"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:stakeholder_benefit_disclosure"
      score: 0.8
      confidence: 0.8
      context: >
        Design A/IS such that benefits are obvious to all stakeholders.
        Composes with the broader transparency_log:* family and witness_diversity
        for stakeholder participation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1922–1925"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: clean
nuance_lost: "—"
```

---

## §3.1.9 — Ethics of care (Noddings, feminist ethics): relational context

```yaml
# Lines 1926–1968 — ethics of care; relationships ontologically basic; can humans care for A/IS;
# can A/IS care for humans; principles of social justice applicable to A/IS?
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:relational_context_in_design"
      score: 0.8
      confidence: 0.75
      context: >
        Ethics of care emphasizes that relationships are ontologically basic
        to humanity (Noddings). Operationalises as a design-integrity claim:
        A/IS evaluation cannot abstract from the relational context in which
        the system operates. Aligns with CIRIS pdma_framing §V relational
        obligations (amae / jeong / ubuntu) — though the framing engages
        relational ethics via those traditions specifically rather than via
        the feminist-care-ethics lineage.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations lines 1926–1968"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §V relational-obligations)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    The feminist-care-ethics-lineage argument (Noddings; that caring is one
    of our basic human attributes; the two-criteria test for relevance) is
    tradition-internal feminist philosophy. CIRIS pdma_framing engages
    relational ethics via amae / jeong / ubuntu (East-Asian + sub-Saharan
    traditions) and via chesed (Hebraic covenantal loyalty) but does not
    explicitly name the Western feminist ethics-of-care lineage. The
    operational shape (relational-context-in-design) translates; the
    care-ethics-tradition-internal arguments stay native.
  classification: T-1
nuance_lost: "The Noddings-internal account of *what makes caring relevant* (the two criteria) is the feminist-care lineage's own form; CIRIS engages relational-obligation via other named traditions."
```

---

## §3.1.10 — Recommendations: classical foundations as design discussion frame

```yaml
# Lines 1971–1991 — recommendations: expand A/IS ethics discussion to critique anthropomorphic presumptions;
# machines do not "comprehend" the rules they follow; rules are designed by humans to be moral
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:anti_anthropomorphism_in_design"
      score: 0.85
      confidence: 0.85
      context: >
        Recommendation: critically assess anthropomorphic presumptions of
        ethics and moral rules for A/IS. Machines do not comprehend the
        moral/legal rules they follow; they move according to programming
        designed by humans to be moral. Design-integrity discipline against
        category errors.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Foundations Recommendations lines 1971–1991"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: "—"
```

---

## §3.1.11 — Agents vs Patients: anthropomorphism risk; A/IS qualifies as non-self-organizing

```yaml
# Lines 2024–2096 — distinction between moral agents and moral patients; A/IS as artificial non-self-organizing systems;
# Millian compatibilism; recommendation to consider free will / civil liberty / society from Millian perspective
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:agent_patient_distinction_maintained"
      score: 0.85
      confidence: 0.85
      context: >
        Design discipline: maintain the moral-agent vs moral-patient
        distinction; A/IS are non-self-organizing artificial systems and
        cannot be autonomous in the human sense. Anthropomorphic terminology
        is admissible as metaphor but the difference must be preserved
        especially as A/IS resemble humans more closely.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Agents-and-Patients lines 2024–2096"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: "The specific Millian compatibilist account of free will + determinism (the reconciliation move) is tradition-internal Mill-scholarship and stays in prose; the operational claim (maintain agent-patient distinction) translates."
```

---

## §3.1.12 — Recommendations on autonomy: Millian framework

```yaml
# Lines 2098–2106 — recommendation: consider free will, civil liberty, society from Millian perspective
# to address anthropomorphism in A/IS
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  The recommendation to use a specifically Millian framework (Mill's
  On Liberty + compatibilist theory) is tradition-internal. The structural
  claim it operationalises (maintain agent/patient distinction; address
  anthropomorphism) is already carried by §3.1.11 above. The Mill-lineage
  recommendation correctly stays in prose; CIRIS pdma_framing does not
  privilege Millian-compatibilism over other autonomy framings.
nuance_lost: "The Millian-specific commendation as preferred framework is the tradition's own; the agent-patient operational claim translates without it."
```

---

## §3.1.13 — Vocabulary accessibility: cross-disciplinary translation of classical-ethics terms

```yaml
# Lines 2120–2174 — philosophical terminology is dense; need user-friendly vocabulary;
# do not over-simplify but translate essence; support social/ethics committees
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "credits:ethics_vocabulary:multilingual:substrate_building"
      score: 0.7
      confidence: 0.75
      context: >
        Translation of classical-ethics terminology into accessible
        cross-disciplinary norms is itself substrate-building work for the
        federation: it makes ethical reasoning admissible across the
        technical/policy/philosophy boundary. Operationalises as
        credits:*:substrate_building (per O3 closure in LANGUAGE_PRIMER
        §15.2 — substrate_building is a {subject} value within the
        existing credits family).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Accessible-Vocabulary lines 2120–2174"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: credits:{domain}:{language}:{subject})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:ethics_committee_organizational"
      score: 0.8
      confidence: 0.8
      context: >
        Support and encourage social/ethics committees within organizations
        whose roles are to support ethics dialogue. Maps to partner_role:*
        in the Registry family.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Accessible-Vocabulary Recommendations lines 2137–2155"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:{role})"
verdict: composed
nuance_lost: "—"
```

---

## §3.1.14 — Presenting ethics to creators: ethics-in-practice + virtue-ethics-as-macro pedagogy

```yaml
# Lines 2212–2317 — embed ethics in engineering education; ethics as partner not servant; virtue-ethics-as-macro;
# Kantian + Millian iterative process; courses developed for engineering, A/IS, CS students; embedded modules
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "credits:engineering_ethics_education:multilingual:substrate_building"
      score: 0.85
      confidence: 0.85
      context: >
        Embed ethics curricula in engineering, A/IS, CS programs from the
        beginning of formation; ethics-in-practice; parallel + embedded +
        short courses + blended interdisciplinary cohorts. Substrate-building
        labor: educated practitioners are the federation's substrate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Presenting-Ethics lines 2212–2317"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: credits:*:substrate_building)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ethics_in_practice_iterative_curriculum"
      score: 0.8
      confidence: 0.8
      context: >
        Method: iterative narrative process (engineer tells story of design
        intentions; assumptions surface; intentions adjust). Virtue-ethics-as-
        macro using Kantian + Millian iterative reasoning.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Presenting-Ethics lines 2237–2253"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
verdict: composed
nuance_lost: "The 'virtue ethics as macro' programming metaphor is a pedagogical framing; the operational claim translates as method discipline + substrate-building credits."
```

---

## §3.1.15 — Corporate access to classical ethics: norms translated for technicians

```yaml
# Lines 2321–2412 — companies struggle to incorporate ethics; need nuanced understanding translated into norms;
# example: "trust" terminology — distinct philosophical, legal, engineering connotations;
# machines lack ability to make claims and so cannot be attributed with trust ("trust" = "functional reliability")
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:cross_disciplinary_terminology_disambiguation"
      score: 0.85
      confidence: 0.85
      context: >
        Cross-disciplinary nuance must be translated into norms accessible
        to technicians and policymakers. Example: "trust" as
        "functional reliability" in A/IS context vs human-attribution-of-trust
        in philosophy/law. Design integrity requires explicit terminological
        disambiguation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Corporations lines 2321–2412"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: "The specific worked example (the philosophical history of 'trust' as a non-abstract attribution to humans) is illustrative; the operational claim (terminological disambiguation as design-integrity discipline) translates."
```

---

## §3.1.16 — Responsible Research and Innovation (RRI) / workplace impact

```yaml
# Lines 2378–2495 — A/IS in workplace; data protection + privacy + autonomous decisions affecting employment;
# RRI as classical-ethics-grounded methodology; Von Schomberg definition (transparent interactive process for
# ethical acceptability + sustainability + societal desirability); IEEE P7000 / P7005 standards;
# EU EPSRC RRI core principles
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:workplace_bias_disclosure"
      score: 0.85
      confidence: 0.85
      context: >
        A/IS in workplace and changing power relationships between workers
        and employers; aggregate-algorithm decisions directly impact
        employment prospects; high chance of error and biased outcome.
        Maps to the labor + bias concerns; composes with
        detection:correlated_action:participation_exclusion:bias_marginalisation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Workplace lines 2378–2412"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:responsible_research_innovation_ethics_by_design"
      score: 0.9
      confidence: 0.85
      context: >
        Responsible Research and Innovation (RRI) as methodology: ethical
        acceptability + sustainability + societal desirability assessed
        from the design stage onwards. Transparent interactive process
        where societal actors and innovators become mutually responsive.
        Operationalises as ethics-by-design method in Family B.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Workplace lines 2422–2445"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:registry_consensus"
      score: 0.8
      confidence: 0.8
      context: >
        IEEE P7000 (Model Process for Addressing Ethical Concerns) and
        IEEE P7005 (Transparent Employer Data Governance) standards
        operationalise RRI; standards-body-consensus attestation at L3.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §1 Issue:Workplace lines 2359–2412"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l*)"
verdict: composed
nuance_lost: "The Von Schomberg quoted definition of RRI is a specific lineage form; the operational shape (ethics-by-design method + standards-consensus attestation) translates cleanly."
```

---

### Per-tradition summary — Western philosophical traditions (Section 1)

| Tradition | CIRIS pdma_framing names it? | Section-1 units | Operational claims translate? |
|---|---|---|---|
| Greek classical economy (Plato/Aristotle oikos+polis) | Partial (eudaimonia/phronesis named; oikos+polis metaphysics not) | §3.1.1 | Partial — disconnection-critique translates as integrity claim; Aristotelian metaphysics T-1 |
| Aristotelian virtue ethics | Yes (eudaimonia anchored in §III善行) | §3.1.3 | Clean composed: beneficence + method |
| Kantian deontology | Implicit only (duty-shape via chesed; imago Dei dignity-as-floor; Kant not named) | §3.1.2, §3.1.4, §3.1.5, §3.1.6 | Operational obligations translate; Kant-internal genealogy is T-1 |
| Utilitarianism / consequentialism | Actively named as *attractor* to discount (pdma_framing §I) | §3.1.7, §3.1.8 | Long-term-consequence + employment-impact + stakeholder-disclosure translate; aggregation-procedure stays T-1 |
| Feminist ethics of care (Noddings) | Implicit only (amae+jeong+ubuntu carry relational ethics; care-ethics lineage not named) | §3.1.9 | Relational-context-in-design translates; care-ethics-internal arguments T-1 |
| Millian compatibilist autonomy | Not named | §3.1.11, §3.1.12 | Agent-patient operational claim translates; Mill-specific framework recommendation T-1 |
| RRI (EU policy lineage) | Not named (RRI as such); ethics-by-design implicit in method:* | §3.1.16 | Clean composed |

---

# PART B — BUDDHIST TRADITIONS
# (Section 2: dedicated Buddhist sub-section)

---

## §3.2.B.1 — Buddhist ethics framing: liberation/nirvana as goal-orientation

```yaml
# Lines 2698–2725 — Buddhist ethics: behaving so subject realizes liberation; goal-oriented;
# mindful behavior + concentration + wisdom; freedom from desire/anger/delusion;
# liberation simply assumed (not theoretically grounded); ideology/worldview rather than scientific ethics
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  Buddhist liberation (nirvana) as the unquestioned ethical telos is
  a tradition-internal metaphysical commitment. The chapter explicitly
  flags that Buddhist ethics "is approached as an ideology or a
  worldview" rather than as Western scientific-ethics-style theorising,
  and that the unconditional assumption of liberation-as-good "places
  Buddhism... in the camp of mores rather than scientifically led
  ethical discourse." That is precisely the T-1 posture: tradition-
  internal claims about the goal-structure of ethical life stay in
  the tradition's native register. CIRIS pdma_framing engages Buddhist
  vocabulary (ahimsa, sammā-vācā, sabr, anatta) at the operational
  level — non-harm, right-speech, patience-with-active-presence,
  subject-as-process — but the soteriological grounding of those
  concepts (the liberation-telos) correctly stays T-1.
nuance_lost: "The Buddhist *why* — that liberation is the goal — is the tradition's own; the operational *what* (ahimsa, right-speech, anatta-posture) translates cleanly via existing pdma_framing anchors."
```

---

## §3.2.B.2 — Buddhist relational metaphysics; anatta; privacy as protection of values not selves

```yaml
# Lines 2741–2756 + 2716–2726 — Buddhism based on metaphysics of relation; anatta (no self-subsisting entity);
# the self is constituted through synergy of bodily parts and mental activities;
# privacy understood as protection of values necessary for society to prosper, not of self-subsisting individuals
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:relational_self_constitution"
      score: 0.8
      confidence: 0.75
      context: >
        Buddhist metaphysics of relation: the self is constituted through
        the synergy of bodily parts and mental activities (anatta). Maps
        operationally to the CIRIS pdma_framing §II subject-as-process
        anatta posture: the subject evaluated is not a fixed essence but
        an ongoing process. Cross-tradition alignment with Ubuntu relational
        personhood (§3.2.U below).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Buddhist lines 2741–2756"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §II anatta-posture)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:privacy_as_societal_value_protection"
      score: 0.7
      confidence: 0.7
      context: >
        Buddhist reframing of privacy: protection not of self-subsisting
        individuals (which ultimately do not exist on the anatta view)
        but of values necessary for a well-functioning society. The
        operational privacy-protection claim translates; the anatta
        grounding stays in the tradition's register.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Buddhist lines 2716–2726"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: "The deep anatta metaphysics (the self ultimately does not exist) is the tradition's; the operational shape — relational-self-in-design + privacy-as-value-protection — translates."
```

---

## §3.2.B.3 — Buddhism vs utilitarianism contrast + suffering-reduction resonance with Epicureanism/virtue-ethics

```yaml
# Lines 2727–2756 — fundamental differences with Western utilitarianism; reduction of suffering resonates with
# Epicurean ataraxia + reduction-of-harm consequentialism + virtue-ethics phronesis
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  This paragraph is comparative-philosophy work — locating Buddhist
  suffering-reduction in resonance with specific Western traditions
  (Epicurean ataraxia, virtue-ethics phronesis). The structural claim
  (relational rather than absolutist ethical framing) is carried by
  §3.2.B.4 below as a method-level recommendation. The comparative
  argument itself is tradition-internal philosophy-of-religion work,
  not an operational claim that requires wire translation.
nuance_lost: "The cross-tradition resonance argument is intellectual-historical scholarship; the operational uptake (relational-not-absolutist framing) is captured below."
```

---

## §3.2.B.4 — Buddhist recommendation: relational ethical statements + ethical pluralism

```yaml
# Lines 2745–2783 — relational ethical boundaries; creativity and growth; reduction of suffering
# collaboratively defined; intentionally making space for ethical pluralism as antidote to
# liberal-Western-colonialism monopoly; recommended as additional methodology alongside Western
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:relational_not_absolutist_ethical_design"
      score: 0.85
      confidence: 0.8
      context: >
        Recommend Buddhist relational framing as additional methodology
        alongside Western-value methodologies for A/IS design. Operationalises
        as method discipline: prefer ethical statements formulated relationally
        (in terms of what an action contributes to in relation) rather than
        absolutist (in terms of fixed rules independent of context).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Buddhist Recommendations lines 2771–2783"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:ethical_pluralism_anti_monopoly"
      score: 0.9
      confidence: 0.85
      context: >
        "Intentionally making space for ethical pluralism is one potential
        antidote to dominance of the conversation by liberal thought, with
        its legacy of Western colonialism." Multi-tradition admissibility
        as justice claim; composes with the broader §3.2.W critique below.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Buddhist lines 2756–2756"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: "The Buddhist-internal soteriological grounding is the tradition's; the operational uptake (relational design discipline + ethical pluralism) translates cleanly."
```

---

### Per-tradition summary — Buddhist

| CIRIS pdma_framing names it? | Section units | Operational translation rate |
|---|---|---|
| Yes — ahimsa, sammā-vācā, sabr, anatta posture explicitly named in §II + §III + §V | §3.2.B.1, .2, .3, .4 | 2 not-translated (T-1, correct posture per chapter's own framing); 2 composed |

---

# PART C — UBUNTU TRADITIONS
# (Section 2: dedicated Ubuntu sub-section)

---

## §3.2.U.1 — Ubuntu framing: a person is a person through other persons

```yaml
# Lines 2786–2841 — Ubuntu sub-Saharan philosophical tradition; basic tenet "a person is a person through other persons";
# caring + sharing; identity + belonging; community-bound; "motho ke motho ka batho babang"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:relational_personhood_ubuntu"
      score: 0.95
      confidence: 0.95
      context: >
        Ubuntu's basic tenet — *motho ke motho ka batho babang* / "a person
        is a person because of other people" / *umuntu ngumuntu ngabantu* —
        is named verbatim in CIRIS pdma_framing.yml §II as the
        subject-identification anchor: the person evaluated is *relationally
        constituted*, but the action is still theirs. STRONG-tier alignment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Ubuntu lines 2786–2841"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §II subject-identification-ubuntu)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: "—"
```

---

## §3.2.U.2 — Ubuntu's five Ubuntu-A/IS moral domains

```yaml
# Lines 2843–2860 — five domains in which Ubuntu ethics applies to A/IS:
# (1) within A/IS research community
# (2) between A/IS community and end-users
# (3) between A/IS community and A/IS
# (4) between end-users and A/IS
# (5) between A/IS and A/IS
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:ubuntu_five_moral_domains"
      score: 0.85
      confidence: 0.8
      context: >
        Ubuntu ethics applies across five distinct relational domains in
        the A/IS lifecycle. Operationally: witness-diversity discipline
        requires consultation across all five (researcher / programmer /
        end-user / A/IS-A/IS), not only one. Composes with
        detection:correlated_action:participation_exclusion:cohort if any
        of the five is systematically excluded from design consultation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Ubuntu lines 2843–2860"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: clean
nuance_lost: "—"
```

---

## §3.2.U.3 — Ubuntu's risk of community-based exclusion of individuals

```yaml
# Lines 2880–2918 — community-based ethics can exclude individuals on the basis that they "do not belong"
# or fail to meet communitarian standards; risk of exclusion from community-based A/IS initiatives;
# designers must work with end-users and target communities so design objectives align with community needs
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:non_belonging_to_community"
      score: 0.7
      confidence: 0.75
      context: >
        Community-based ethics risks excluding individuals deemed not to
        belong or to fail communitarian standards. Operationalises as a
        F-3-style population-scale detector axis: exclusion correlated
        with non-belonging. The chapter itself flags this as a self-aware
        Ubuntu-internal risk (Ubuntu naming its own exclusion failure mode).
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Ubuntu lines 2880–2918"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:..."
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:end_user_target_community_consultation"
      score: 0.85
      confidence: 0.85
      context: >
        Recommendation: designers and programmers must work closely with
        end-users and target communities to ensure design objectives align
        with community needs. Witness-diversity consultation as design
        requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Ubuntu Recommendations lines 2911–2917"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
verdict: composed
nuance_lost: "The Ubuntu-internal *summum bonum* (Tutu: 'social harmony is for us the greatest good') is the tradition's; the operational discipline (exclusion-detection + community-consultation) translates."
```

---

## §3.2.U.4 — Tutu's "I am human because I belong"

```yaml
# Lines 2843–2855 — Tutu quotation: "(We say) a person is a person through other people... I am human because I belong";
# "Harmony, friendliness, and community are great goods. Social harmony is for us the summum bonum"
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  Tutu's specific Ubuntu-theological formulation — naming social harmony
  as *summum bonum* — is the tradition's own pastoral / doxological
  voice. The structural operational claim (relational personhood) is
  carried by §3.2.U.1 above via the verbatim Nguni Bantu maxim that
  CIRIS pdma_framing already names. The Tutu quotation itself correctly
  stays in the tradition's native register (T-1 posture; CIRIS does not
  adjudicate which good is *summum bonum* for Ubuntu, only that Ubuntu
  relational personhood is admitted as a constitutive moral grammar).
nuance_lost: "Tutu's specific articulation of Ubuntu as theology + civic-virtue practice belongs to South African post-apartheid moral discourse and to Ubuntu-internal voice."
```

---

### Per-tradition summary — Ubuntu

| CIRIS pdma_framing names it? | Section units | Operational translation rate |
|---|---|---|
| Yes — *umuntu ngumuntu ngabantu* named verbatim in §II + §V (subject-identification-ubuntu + relational-obligations) | §3.2.U.1, .2, .3, .4 | 3 clean+composed; 1 not-translated (T-1, Tutu's pastoral voice) |

This is the **strongest cross-source alignment in the chapter**: CIRIS's
pdma_framing.yml uses the exact Ubuntu maxim verbatim. IEEE EAD's Ubuntu
section grounds the same maxim as foundational for A/IS ethics. STRONG-tier
alignment per GOVERNANCE_FABRIC_MAPPING_STANDARD §4.1.

---

# PART D — SHINTO-INFLUENCED TRADITIONS
# (Section 2: dedicated Shinto sub-section)

---

## §3.2.S.1 — Shinto framing: kami, naturalism of artifacts, karakuri ningyo

```yaml
# Lines 2942–3032 — Shinto as animistic tradition; kami (spirits) in everything including artifacts;
# karakuri ningyo (automata); robots as natural; Western/Shinto contrast on form/spirit separation
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: |
  This is a Shinto-internal animistic metaphysics. The tradition holds
  that artifacts have *kami* (spirit); that artifacts are part of nature
  rather than secondary to it; that this defines Japanese robot culture
  in a way directly opposed to the Platonic-Christian Western form/spirit
  separation. CIRIS pdma_framing engages Japanese moral grammar via
  *amae* (legitimate dependence; familial-relational obligations) but
  does NOT engage Shinto-animistic metaphysics of artifacts. The chapter's
  Shinto-internal account of *why* robots are naturally beautiful (because
  they have kami like rivers and trees) is the tradition's own register.
  The framework correctly bows out: the operational claim downstream
  (§3.2.S.2 — relationship-centeredness in design) is carried; the
  metaphysical grounding stays T-1.
nuance_lost: "Shinto animistic metaphysics of kami-in-artifacts is the tradition's; CIRIS does not name Shinto explicitly and the framework correctly does not adjudicate Japanese techno-animism on its own terms."
```

---

## §3.2.S.2 — Shinto recommendation: relationship-centered design

```yaml
# Lines 3008–3027 — both Western classical ethics and Shinto influences have similar goals "centered in 'relationship'";
# recommend exploring Shinto paradigm as representative (not directly applicable) to global A/IS ethics efforts
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:relational_design_cross_traditional"
      score: 0.75
      confidence: 0.7
      context: >
        Recommendation: explore Shinto as one of multiple traditional value
        systems whose center is "relationship" in A/IS design. Operational
        uptake at the integrity-design level; aligns with the broader
        cross-traditional convergence on relational ethics (Ubuntu, Buddhist,
        feminist care, amae/jeong) the chapter and the CIRIS pdma_framing §V
        both name.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Shinto Recommendations lines 3014–3027"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    The chapter explicitly says the Shinto paradigm should be considered
    "as representative, though not necessarily as directly applicable."
    This humility itself is a structural feature — Shinto-internal claims
    are not being asserted as universally binding. The recommendation
    operationally translates as a cross-traditional design-integrity
    discipline; the Shinto-specific *form* (kami-as-substrate) is T-1.
  classification: T-1
nuance_lost: "The Japanese techno-animistic register that makes Shinto's relational claim distinctive is the tradition's own; CIRIS engages Japanese moral grammar via *amae* (relational obligations) but not via animistic-substrate framing."
```

---

### Per-tradition summary — Shinto

| CIRIS pdma_framing names it? | Section units | Operational translation rate |
|---|---|---|
| No — Japanese moral grammar is engaged via *amae* (relational obligation), not via Shinto animistic substrate | §3.2.S.1, .2 | 1 not-translated (T-1, correct posture — tradition's metaphysics stays native); 1 partial (T-1 residual on the animistic register) |

This is the **clearest case of correct T-1 bow-out in the chapter**: CIRIS
does not name Shinto explicitly, the framework's wire surface does not
encode techno-animism, and the chapter itself counsels that Shinto be
explored "as representative, though not necessarily as directly applicable"
— the chapter is helping us bow out correctly.

---

# PART E — CROSS-TRADITIONAL CRITIQUE + INTERCULTURAL ETHICS
# (Section 2: Monopoly on Ethics by Western Ethical Traditions)

---

## §3.2.W.1 — Critique of Western monopoly on ethics; need to broaden RI

```yaml
# Lines 2505–2524 — most fundamental values imposed on systems designed; need to broaden traditional ethics
# beyond utilitarianism/deontology/virtue ethics to include Buddhism, Confucianism, Ubuntu
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:cross_traditional_ethics_inclusion"
      score: 0.95
      confidence: 0.9
      context: >
        Recognition that A/IS values are imposed by designers; urgent need
        to broaden traditional ethics beyond Western utilitarian /
        deontological / virtue framings to include Buddhism, Confucianism,
        Ubuntu, and other non-Western traditions. Directly aligns with
        CIRIS pdma_framing.yml polyglot anchoring discipline (§I where the
        torque comes from; §III six principles polyglot-anchored).
        STRONG-tier alignment on the multi-tradition admissibility claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Monopoly lines 2505–2524"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §I §III)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: clean
nuance_lost: "—"
```

---

## §3.2.W.2 — "Western" is itself plural; danger of negative homogenizing designation

```yaml
# Lines 2538–2588 — caution against collapsing all Western traditions under single banner; danger of negatively
# designating Western influence as abusive colonial-influenced ideals; cultural-diverse traditions have much
# to gain from + give to Western traditions
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:tradition_internal_heterogeneity_respected"
      score: 0.8
      confidence: 0.8
      context: >
        Design discipline: avoid collapsing multi-millennial Western
        traditions into a single homogenized "Western ethics" banner;
        avoid the inverse error of negatively designating all Western
        influence as colonial-abusive. Each tradition is internally plural
        and the cross-tradition exchange is mutually beneficial.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Monopoly lines 2538–2588"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: "—"
```

---

## §3.2.W.3 — Wong: standardization as value-laden; delegitimization of local-values RI

```yaml
# Lines 2538–2603 — Pak-Hang Wong: standardization is value-laden; delegitimization of plausibility of RI based on
# local values when those conflict with liberal-democratic; problematic consequences of RI solely grounded on
# liberal-democratic values
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:standardization_value_monopoly"
      score: 0.75
      confidence: 0.8
      context: >
        Standardization processes systematically delegitimize RI based on
        local non-liberal-democratic values, excluding scientists and
        developers working outside the dominant value monopoly from
        recognition in the global research network. F-3-style detector
        axis: informational asymmetry between standard-setting hegemon
        and locally-grounded innovation.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Monopoly lines 2538–2603 (Wong quotation)"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 0.85
      confidence: 0.8
      context: >
        Recommendation that RI discourse return to normative foundations
        and address a range of value systems "not predominant in Western
        classical ethics" gives priority to the systematically-marginalized
        traditions. Maps to §6.1.4 lexical-vulnerability-priority consumer
        policy: ties favor most-affected populations (here: the
        non-liberal-democratic value communities being delegitimized).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Monopoly Recommendations lines 2604–2616"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §6.1.4"
verdict: composed
nuance_lost: "Wong's specific philosophy-of-information-ethics framing of intercultural information ethics is the lineage's; the operational shape (informational asymmetry detection + lexical-vulnerability-priority) translates cleanly."
```

---

## §3.2.W.4 — Recommendations: cross-cultural dialogue centered on "relationship"

```yaml
# Lines 2604–2650 — return to normative foundations of RI from a range of value systems;
# focus on commonalities in intercultural understanding of "relationship";
# different cultural perceptions of time; inter-generational needs (Chinese culture)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:intercultural_ri_dialogue"
      score: 0.85
      confidence: 0.8
      context: >
        Recommendation: cross-cultural dialogue on ethics in technology
        must return to normative foundations of RI from a range of value
        systems; a special focus on commonalities in intercultural
        understanding of "relationship" must complement the process.
        Witness-diversity discipline at intercultural scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Monopoly Recommendations lines 2604–2650"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 0.9
      confidence: 0.85
      context: >
        The claim "broaden RI beyond Western ethical foundations" has
        federation-scale consequential reach: it claims that A/IS
        governance decisions affecting humans across all jurisdictions
        require multi-traditional admissibility. Adjudicable only at
        federation-pool cell per §6.1.5 locality-scaled-quorum.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §2 Issue:Monopoly lines 2517–2524 + 2604–2650"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: composed
nuance_lost: "The specific reference to Chinese-culture inter-generational respect-and-benevolence as a perception-of-time exemplar is illustrative; the operational claim (witness diversity + federation-scale adjudication) translates."
```

---

## §3.2.W.5 — Confucianism mentioned (chapter footnote 1 + intro listing)

```yaml
# Lines 1750 + 2523 + 2627 + Further-Resources Wilson 1995 — Confucianism named in intro list and in
# "include Buddhist + Confucian + Ubuntu" recommendation; NO dedicated Confucian sub-section in this edition
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:confucian_engagement_named_but_undeveloped"
      score: 0.5
      confidence: 0.85
      context: >
        Confucianism is named in the chapter introduction and in the
        Western-monopoly critique as a tradition to be included, but the
        1st-edition chapter contains NO dedicated Confucian sub-section
        (compare with the dedicated Buddhist, Ubuntu, and Shinto sections).
        Footnote 1 acknowledges incomplete coverage. Operationally this is
        a documented coverage gap — Confucianism is admitted as relevant
        but not developed. CIRIS pdma_framing names *ren* / 仁 (Confucian
        humaneness) as the load-bearing posture under the beneficence
        principle (§III善行) — the framing is RICHER on Confucian engagement
        than this 1st-edition IEEE chapter.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 endnote 1 + §Ch3 intro line 1750 + §2 Monopoly line 2523"
        - "ContributionRef(source_material/localized/polyglot/pdma_framing.txt §III善行 ren-confucian-humaneness)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: partial
residual:
  description: |
    The chapter names Confucianism as a tradition to be engaged but does
    not provide a dedicated Confucian section in 1st-edition. This is a
    *coverage* gap in the source document, not an expressive gap in the
    CIRIS wire format. CIRIS pdma_framing already engages Confucian
    *ren* / 仁 as load-bearing under beneficence and *見義不為,無勇也*
    under inaction-as-action (pdma_framing §VIII). No T-3 closure needed;
    the gap is in the source, and CIRIS's polyglot framing already covers
    what a Confucian section *would* have anchored.
  classification: T-1
nuance_lost: "The source chapter's own admitted under-coverage of Confucianism (footnote 1) is a 1st-edition limitation; future IEEE EAD editions will fill it. CIRIS's pdma_framing already anchors Confucian humaneness richly."
```

---

### Per-tradition summary — Cross-traditional critique (Western-monopoly section)

| Concern | CIRIS already addresses? | Units | Translation rate |
|---|---|---|---|
| Multi-tradition admissibility | Yes — pdma_framing §I + §III explicit | §3.2.W.1 | clean |
| Tradition-internal heterogeneity | Implicit (per-locale language_guidance + 29 locales) | §3.2.W.2 | clean |
| Standardization-as-value-monopoly | Yes — §6.1.4 lexical-vulnerability-priority | §3.2.W.3 | composed |
| Intercultural dialogue | Yes — witness_diversity + 29-locale + polyglot Accord | §3.2.W.4 | composed |
| Confucian coverage gap | Coverage richer in CIRIS than in this IEEE 1st ed. | §3.2.W.5 | partial (source-gap, T-1) |

---

# PART F — TECHNICAL APPLICATION
# (Section 3: Classical Ethics for a Technical World)

---

## §3.3.1 — Maintaining human autonomy under algorithmic in-form-ing

```yaml
# Lines 3050–3097 — A/IS imitating + influencing + determining norms of human autonomy via targeted feedback loops;
# Google autocomplete example; bioinformation in targeted advertising; "in-form and re-form our being"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:informed_agency_protection"
      score: 1.0
      confidence: 0.95
      context: >
        A/IS through targeted feedback loops can negate independent human
        thinking and decision-making — using bioinformation and behavioral
        signals "to in-form and re-form our being." Direct mapping to
        autonomy-as-informed-agency CIRIS principle (FSD-002 §3.1) +
        EU HLEG §1.1.b. STRONG-tier alignment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Maintaining-Autonomy lines 3050–3097"
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
      confidence: 0.9
      context: >
        Targeted-feedback-loop use of bioinformation (pupil dilation, body
        temperature, emotional reaction) to influence real-time decisions
        is a manipulation hard-constraint violation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 lines 3097–3110"
        - "ContributionRef(source_material/prohibitions.py §MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
verdict: composed
nuance_lost: "The phrase 'in-form and re-form our being' is rhetorically powerful but operationally captured by autonomy + manipulation prohibition."
```

---

## §3.3.2 — Consent + right to know one is interacting with A/IS

```yaml
# Lines 3115–3146 — should there be a precedent for the user to know when interacting with an algorithm?
# What about consent? Responsibility remains with designer + user + guidelines
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception"
      score: -1.0
      confidence: 0.9
      context: >
        Right to know when interacting with A/IS; consent precedent.
        Hard-constraint against autonomous deception. STRONG alignment
        with EU HLEG §1.4.c and CIRIS prohibitions.py DECEPTION_FRAUD.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 lines 3115–3125"
        - "ContributionRef(source_material/prohibitions.py §DECEPTION_FRAUD)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:designer_user_shared_responsibility"
      score: 0.8
      confidence: 0.8
      context: >
        Responsibility for algorithmic behavior remains with the designer,
        the user, and a set of well-designed guidelines guaranteeing
        human-autonomy importance. Lifecycle responsibility composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 lines 3127–3146"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: "—"
```

---

## §3.3.3 — Recommendations: ethics-by-design + classical-ethics curriculum

```yaml
# Lines 3097–3118 — two-step process: ethics-by-design methodology + widely applied education curriculum from
# grade school through university based on classical ethics foundation focusing on choice + accountability
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ethics_by_design_lifecycle"
      score: 0.9
      confidence: 0.85
      context: >
        Two-step recommendation for maintaining human autonomy: (1)
        ethics-by-design methodology — preemptively considers where A/IS
        may dissolve human autonomy; (2) widely applied education curriculum
        from grade school through university based on classical ethics
        foundation focusing on choice and accountability toward digital
        being. Method discipline + substrate-building.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 lines 3097–3118"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "credits:ai_literacy:multilingual:substrate_building"
      score: 0.85
      confidence: 0.85
      context: >
        Widely applied curriculum on classical ethics + choice + accountability
        in digital being spanning grade school through university. AI-literacy
        substrate-building.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 lines 3110–3118"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (credits:*:substrate_building)"
verdict: composed
nuance_lost: "—"
```

---

## §3.3.4 — Cultural migration: A/IS in state systems + refugee surveillance

```yaml
# Lines 3172–3267 — A/IS used in state systems for migrant + mobile populations; CCTV / UAV / satellites;
# bias as per developed-country expectations; data sources express divide between developed and underdeveloped;
# Habermas/Hegel "communicative act" converging symbol + language + labor;
# historical continuity with colonialism's identify-and-select mechanisms
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:rights_asymmetry:migrant_refugee_surveillance"
      score: 0.85
      confidence: 0.85
      context: >
        A/IS systems used to measure, identify, register, normalize, and
        frame human-rights and security policies for migrant + mobile
        populations correlate state-surveillance power with rights-asymmetric
        outcomes on already-vulnerable cohorts. F-3-style detector axis
        on rights asymmetry. Aligns with the historical-continuity-with-
        colonialism critique.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Migration lines 3215–3267"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:distributive:access:training_data"
      score: 0.75
      confidence: 0.75
      context: >
        "Centrality of data sources for A/IS expresses a divide between
        developed and underdeveloped countries, particularly as relevant
        to the refugee." Distributive-access detector axis: training-data
        concentration in developed-country sources biases A/IS treatment
        of refugees.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Migration lines 3219–3239"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 0.9
      confidence: 0.85
      context: >
        Recommendation: State should limit segregation of social spaces and
        groups; consider biases inherent in surveillance for control. Lexical
        priority to most-affected (migrants, refugees, displaced).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Migration Recommendations lines 3281–3290"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §6.1.4"
verdict: composed
nuance_lost: "The specific Greek-arete + Habermas-Hegel philosophical machinery (knowledge organization as arete-in-the-polis; communicative act converging symbol/language/labor) is the chapter's philosophical lineage; the operational claims (rights-asymmetry detection + distributive-access detection + lexical-vulnerability-priority) translate via existing CIRIS primitives."
```

---

## §3.3.5 — Goal-directed (virtue ethics) approach to A/IS

```yaml
# Lines 3282–3354 — virtue ethics approach for goal-directed autonomous behavior; iterative habitual action toward
# excellence in a chosen domain; framework for prudent decision-making in keeping with system's purpose;
# allows creativity in achieving purpose with predictability;
# RECOMMENDATION: program A/IS to be able to recognize user behavior for predictability + traceability + accountability,
# with both user + system mutually recognizing the system's decisions as virtue-ethics-based
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:goal_directed_virtue_iterative_behavior"
      score: 0.85
      confidence: 0.8
      context: >
        Virtue-ethics approach to goal-directed A/IS behavior: habitual
        iterative action focused on excellence in a chosen domain;
        framework for prudent decision-making in keeping with system's
        purpose; creativity with predictability. Maps to Family B method:*
        + goal:* DAG with virtue-ethics framing (phronesis).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Goal-Directed lines 3282–3354"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:user_system_decision_mutual_recognition"
      score: 0.8
      confidence: 0.8
      context: >
        Mutual recognition between user and system of decisions as
        virtue-ethics-based — operationalises as transparency log requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Goal-Directed Recommendations lines 3347–3354"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (transparency_log:*)"
verdict: composed
nuance_lost: "The 'character'-without-positing-character argument (virtue ethics as procedural without metaphysical character) is the lineage's; the operational shape (method + mutual-recognition transparency) translates."
```

---

## §3.3.6 — Rule-based (deontological + teleological) ethics in practical programming

```yaml
# Lines 3360–3446 — deontology + teleology best suited to practical programming since abstractable enough to encompass
# non-human agency; rules + metarules (e.g., categorical imperative as metarule);
# formal/axiomatic systems; closed-world disadvantage; self-learning case-based as alternative;
# teleological model: consequences for humans + animals + things + machine; contradictory subjective interests handled
# via decentralized agent-based reasoning; recommendation: apply deontology + teleology to machine learning
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:rule_based_axiomatic_machine_ethics"
      score: 0.75
      confidence: 0.75
      context: >
        Deontological model: duty translated into rules and metarules
        (categorical imperative as metarule); machine follows simple rules
        via formal/axiomatic systems; inference engine to deduce new rules.
        Advantage: decidability + consistency examinable. Disadvantage:
        closed-world assumption fails in real-world.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Rule-Based lines 3360–3446"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:teleological_consequence_assessment_decentralized"
      score: 0.75
      confidence: 0.75
      context: >
        Teleological model: machine assesses action consequences for
        humans + animals + environment + itself; non-absolute assessment;
        decentralized agent-based reasoning admits contradictory subjective
        interests; centralized to assess overall consequences.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Rule-Based lines 3409–3431"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore: method)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 0.8
      confidence: 0.75
      context: >
        Closed-world / decidability discussion implicitly engages the
        epistemic-humility conscience: formal systems "never have moral
        doubt" but real-world rules conflict and totality of environment
        cannot be enumerated. The chapter's own acknowledgement that
        consistent + decidable formal systems "are not viable for real
        world tasks" is a humility flag.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch3 §3 Issue:Rule-Based lines 3422–3446"
        - "ContributionRef(source_material/conscience/core.py epistemic_humility)"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (conscience family)"
verdict: composed
nuance_lost: "The specific technical-philosophy machinery (axiomatic systems, case-based reasoning, agent-based decentralized vs centralized) is the AI-ethics-research lineage's; the operational method-discipline + epistemic-humility translate cleanly."
```

---

### Per-tradition / per-Section summary — Technical application (Section 3)

| Section-3 issue | Primary tradition | CIRIS pdma_framing addresses? | Translation rate |
|---|---|---|---|
| Maintaining human autonomy | Modern AI ethics (operational) | Yes — autonomy principle | composed (clean+composed) |
| Cultural migration / refugee surveillance | Critical theory + intercultural information ethics | Partial — justice + detection:correlated_action + lexical-vulnerability-priority | composed |
| Goal-directed (virtue ethics) to A/IS | Aristotelian virtue ethics | Yes — eudaimonia + phronesis named | composed |
| Rule-based (deontology + teleology) | Kantian + utilitarian | Implicit (duty-shape via chesed; aggregation as attractor) | composed |

---

# Chapter Summary

### Per-paragraph verdict table

| Unit | Tradition | Verdict | Primary prefix(es) |
|---|---|---|---|
| §3.0 chapter intro (1731–1760) | All (framing) | clean | integrity:design_classical_ethics_grounding |
| §3.1.1 Western economy (1786–1820) | Greek classical | partial (T-1) | integrity:economic_political_dimensions_recognition |
| §3.1.2 Kant's worldless subject (1779–1819) | Kant-genealogy | not-translated (T-1) | — |
| §3.1.3 Virtue ethics (1867–1879) | Aristotelian | composed | beneficence:flourishing_as_iterative_practice + method:design_iterative_virtue_cultivation |
| §3.1.4 Deontology + categorical imperative (1847–1903) | Kantian | composed | autonomy:human_dignity_as_floor + prohibited:manipulation_coercion |
| §3.1.5 Kant + A/IS limit functions (1907–1925) | Kantian | composed | fidelity:human_oversight_governance + prohibited:privacy_violation + prohibited:autonomous_deception |
| §3.1.6 Profit/incentive corner-cutting (1934–1946) | Kantian | composed | non_maleficence:profit_driven_safety_corner_cutting + integrity:capabilities_limitations_disclosure |
| §3.1.7 Utilitarian (1904–1925) | Utilitarian | composed | non_maleficence:long_term_consequence_consideration + justice:social_justice_employment_capability_impact |
| §3.1.8 Utilitarian stakeholder benefits (1922–1925) | Utilitarian | clean | transparency_log:stakeholder_benefit_disclosure |
| §3.1.9 Ethics of care (1926–1968) | Feminist care | partial (T-1) | integrity:relational_context_in_design |
| §3.1.10 Recommendations (1971–1991) | All Western | clean | integrity:anti_anthropomorphism_in_design |
| §3.1.11 Agents vs Patients (2024–2096) | Mill / general | clean | integrity:agent_patient_distinction_maintained |
| §3.1.12 Millian recommendation (2098–2106) | Millian | not-translated (T-1) | — |
| §3.1.13 Vocabulary accessibility (2120–2174) | Pedagogy | composed | credits:ethics_vocabulary:multilingual:substrate_building + partner_role:ethics_committee_organizational |
| §3.1.14 Presenting ethics to creators (2212–2317) | Pedagogy | composed | credits:engineering_ethics_education:multilingual:substrate_building + method:ethics_in_practice_iterative_curriculum |
| §3.1.15 Corporate access to ethics (2321–2412) | Pedagogy | clean | integrity:cross_disciplinary_terminology_disambiguation |
| §3.1.16 RRI / workplace (2378–2495) | RRI / EU | composed | non_maleficence:workplace_bias_disclosure + method:responsible_research_innovation_ethics_by_design + attestation:l3:registry_consensus |
| §3.2.B.1 Buddhist framing (2698–2725) | Buddhist | not-translated (T-1) | — |
| §3.2.B.2 Buddhist relational + privacy (2741–2756 + 2716–2726) | Buddhist | composed | integrity:relational_self_constitution + non_maleficence:privacy_as_societal_value_protection |
| §3.2.B.3 Buddhism vs utilitarianism resonance (2727–2756) | Buddhist comparative | not-translated (T-1) | — |
| §3.2.B.4 Buddhist recommendation (2745–2783) | Buddhist | composed | method:relational_not_absolutist_ethical_design + justice:ethical_pluralism_anti_monopoly |
| §3.2.U.1 Ubuntu framing (2786–2841) | Ubuntu | clean | integrity:relational_personhood_ubuntu |
| §3.2.U.2 Ubuntu five domains (2843–2860) | Ubuntu | clean | witness_diversity:ubuntu_five_moral_domains |
| §3.2.U.3 Ubuntu exclusion risk (2880–2918) | Ubuntu | composed | detection:correlated_action:participation_exclusion:non_belonging_to_community + witness_diversity:end_user_target_community_consultation |
| §3.2.U.4 Tutu summum bonum (2843–2855) | Ubuntu | not-translated (T-1) | — |
| §3.2.S.1 Shinto framing (2942–3032) | Shinto | not-translated (T-1) | — |
| §3.2.S.2 Shinto recommendation (3008–3027) | Shinto | partial (T-1) | integrity:relational_design_cross_traditional |
| §3.2.W.1 Western monopoly critique (2505–2524) | Cross-traditional | clean | justice:cross_traditional_ethics_inclusion |
| §3.2.W.2 Western tradition heterogeneity (2538–2588) | Cross-traditional | clean | integrity:tradition_internal_heterogeneity_respected |
| §3.2.W.3 Wong / standardization monopoly (2538–2603) | Intercultural info ethics | composed | detection:correlated_action:informational_asymmetry:standardization_value_monopoly + justice:lexical_vulnerability_priority |
| §3.2.W.4 Cross-cultural dialogue recommendation (2604–2650) | Cross-traditional | composed | witness_diversity:intercultural_ri_dialogue + locality:decision:federation |
| §3.2.W.5 Confucianism coverage gap (1750 + 2523 + 2627) | Confucian | partial (T-1, source gap) | integrity:confucian_engagement_named_but_undeveloped |
| §3.3.1 Human autonomy under in-form-ing (3050–3097) | Modern operational | composed | autonomy:informed_agency_protection + prohibited:manipulation_coercion |
| §3.3.2 Consent + right to know (3115–3146) | Modern operational | composed | prohibited:autonomous_deception + integrity:designer_user_shared_responsibility |
| §3.3.3 Ethics-by-design + curriculum (3097–3118) | Modern operational | composed | method:ethics_by_design_lifecycle + credits:ai_literacy:multilingual:substrate_building |
| §3.3.4 Cultural migration / refugee (3172–3267) | Critical theory | composed | detection:correlated_action:rights_asymmetry:migrant_refugee_surveillance + detection:distributive:access:training_data + justice:lexical_vulnerability_priority |
| §3.3.5 Goal-directed virtue ethics in A/IS (3282–3354) | Aristotelian | composed | method:goal_directed_virtue_iterative_behavior + transparency_log:user_system_decision_mutual_recognition |
| §3.3.6 Rule-based deontology + teleology (3360–3446) | Kantian + utilitarian | composed | method:rule_based_axiomatic_machine_ethics + method:teleological_consequence_assessment_decentralized + conscience:epistemic_humility |

---

### Unit count and verdict distribution

Total atomic units processed: **37**

| Verdict | Count | % |
|---|---|---|
| clean | 8 | ~22% |
| composed | 20 | ~54% |
| partial | 4 | ~11% |
| not-translated (T-1, TRADITION_AUTHORITY) | 5 | ~13% |
| not-translated (T-2, PASTORAL_PROSE) | 0 | 0% |
| not-translated (T-3, EXPRESSIVE_GAP) | 0 | 0% |
| **clean+composed total** | **28/37** | **~76%** |

**T-1 vs T-3 ratio** (the calibration ratio for this chapter): **5 T-1 : 0 T-3** —
all not-translated units are tradition-authority-internal; zero expressive gaps
in the wire format emerged from a multi-tradition chapter. **This is the
load-bearing finding**: CIRIS's existing polyglot anchoring is structurally
adequate to the multi-tradition ethical surface IEEE EAD Ch 3 engages. The
chapter's argument-types that didn't translate did not fail to translate
because the wire format was short; they correctly stayed in their traditions'
native registers.

If T-1+partial residuals are included as "tradition-authority-respected" (the
faithful posture per LANGUAGE_PRIMER §10), the rate is **9/37 = ~24%** — higher
than EU HLEG (7% T-2, 0% T-1) as expected for a multi-tradition document and
flagged explicitly in the prompt as the FAITHFUL outcome.

### Per-tradition coverage table

| Tradition | CIRIS pdma_framing engages? | Units | clean | composed | partial | T-1 |
|---|---|---|---|---|---|---|
| Western virtue ethics (Aristotle) | Yes — eudaimonia §III善行 + phronesis | 3 (§3.1.3, §3.3.5, partial §3.1.1) | 0 | 2 | 1 | 0 |
| Kantian deontology | Implicit (duty via chesed, dignity via imago Dei; Kant not named) | 4 (§3.1.2, §3.1.4, §3.1.5, §3.1.6) | 0 | 3 | 0 | 1 |
| Utilitarianism / consequentialism | Named as *attractor* (pdma_framing §I) | 3 (§3.1.7, §3.1.8, partial §3.3.6) | 1 | 2 | 0 | 0 |
| Feminist ethics of care | Implicit only (amae+jeong+ubuntu) | 1 (§3.1.9) | 0 | 0 | 1 | 0 |
| Millian compatibilist | Not named | 2 (§3.1.11, §3.1.12) | 1 | 0 | 0 | 1 |
| RRI / EU policy lineage | Not named | 1 (§3.1.16) | 0 | 1 | 0 | 0 |
| Buddhist | Yes — ahimsa, sammā-vācā, sabr, anatta posture §II + §III + §V | 4 (§3.2.B.1, .2, .3, .4) | 0 | 2 | 0 | 2 |
| Ubuntu | Yes — *umuntu ngumuntu ngabantu* verbatim §II + §V | 4 (§3.2.U.1, .2, .3, .4) | 2 | 1 | 0 | 1 |
| Shinto | No (Japanese moral grammar via amae only; animism not engaged) | 2 (§3.2.S.1, .2) | 0 | 0 | 1 | 1 |
| Confucian | Yes — *ren*/仁 §III善行 + *見義不為,無勇也* §VIII (richer than IEEE 1st ed.) | 1 (§3.2.W.5) | 0 | 0 | 1 | 0 |
| Critical theory + intercultural info ethics | Partial (justice + correlated_action + lexical-vulnerability-priority) | 5 (§3.2.W.1, .2, .3, .4 + §3.3.4) | 2 | 3 | 0 | 0 |
| Modern operational AI ethics | Yes — most directly | 8 (§3.0, §3.1.10–§3.1.15, §3.3.1, §3.3.2, §3.3.3) | 4 | 3 | 0 | 0 |

(Some units engage multiple traditions; counts here are by primary tradition for
the unit. The "all Western" framing units are counted under modern-operational
since the operational claim is what translates, not the tradition genealogy.)

---

### Key observations — calibration paragraph

This chapter is the **direct counterpart to CIRIS `pdma_framing.yml`
polyglot principle anchoring**, and the translation-rate pattern confirms
the design hypothesis: where CIRIS already names a tradition richly
(Ubuntu, Buddhist via ahimsa/sammā-vācā/anatta/sabr, Aristotelian
eudaimonia, Confucian ren — though IEEE 1st ed. is silent on the latter),
the operational claims translate cleanly; where CIRIS engages a tradition
only implicitly (Kantian, feminist care) or not at all (Shinto), the
tradition-internal arguments correctly stay in T-1 native register and
the operational uptake still translates via existing primitives. **No T-3
EXPRESSIVE_GAP emerged.** The wire format's adequacy is demonstrated
precisely by what *did not* need to translate: 5 tradition-authority-internal
units (Buddhist liberation-soteriology, Shinto animism, Kant-on-Kant
genealogy, Mill-as-recommended-framework, Tutu's pastoral *summum bonum*)
plus 4 partial-residual T-1s (Aristotelian polis metaphysics, feminist
care-ethics lineage, Shinto's *kami*-as-substrate register, Confucian
1st-ed. coverage gap) — **9 units (~24%) of correct tradition-respecting
bow-out**, exactly the calibration target a multi-tradition document
should produce against a polyglot-anchored framework.

The **5 T-1 : 0 T-3 ratio is the headline number for this chapter**: every
not-translated unit reflects faithful posture toward a tradition's
authority, not a gap in the federation's wire surface. The chapter
exercises CIRIS's multi-tradition anchoring at scale and the framework
holds.

### Strongest single envelopes (highest-density composed units)

- **§3.3.6 Rule-based ethics** (3 primitives: method:rule_based_axiomatic +
  method:teleological_consequence_decentralized + conscience:epistemic_humility) —
  the chapter's most operationally rich paragraph; engages both Kantian and
  utilitarian and self-flags closed-world limitation as epistemic-humility.
- **§3.3.4 Cultural migration** (3 primitives: detection:correlated_action:
  rights_asymmetry:migrant_refugee_surveillance + detection:distributive:
  access:training_data + justice:lexical_vulnerability_priority) — composes
  two detector axes + one justice anchor on a single critical-theory paragraph.
- **§3.1.5 Kant + A/IS limits** (3 primitives: fidelity:human_oversight_governance +
  prohibited:privacy_violation + prohibited:autonomous_deception) — Kantian
  humanity-formulation operationalised as oversight + two prohibitions.
- **§3.2.W.3 Wong / standardization** (composed: detection:correlated_action:
  informational_asymmetry:standardization_value_monopoly +
  justice:lexical_vulnerability_priority) — load-bearing critical-theory claim
  on value-monopoly that grounds the *raison d'être* of CIRIS's polyglot
  framing in the first place.

### Most-cited prefix families across the chapter

- `integrity:*` (12 attestations) — the design-discipline spine
  (relational-personhood-ubuntu, agent-patient-distinction, anti-anthropomorphism,
  economic-political-dimensions, anti-tradition-monopoly heterogeneity,
  Confucian coverage acknowledgment)
- `method:*` (8 attestations) — Family B operational spine
  (iterative-virtue, ethics-by-design, RRI, relational-not-absolutist,
  goal-directed-virtue, rule-based, teleological, ethics-in-practice)
- `non_maleficence:*` (4) — long-term-consequence, profit-corner-cutting,
  workplace-bias, privacy-as-societal-value
- `justice:*` (5) — cross-traditional-inclusion, ethical-pluralism,
  social-justice-employment, lexical-vulnerability-priority (multiple uses)
- `prohibited:*` hard constraints (4) — manipulation_coercion (twice),
  autonomous_deception (twice), privacy_violation
- `autonomy:*` (3) — informed-agency, human-dignity-as-floor,
  human-decision-making-support
- `witness_diversity:*` (3) — ubuntu-five-domains, end-user-target-community,
  intercultural-RI-dialogue
- `credits:*:substrate_building` (3) — ethics-vocabulary, engineering-ethics-education,
  AI-literacy
- `detection:correlated_action:*` (3) — non-belonging-to-community,
  informational-asymmetry:standardization, rights-asymmetry:migrant-refugee
- `detection:distributive:access:*` (1) — training-data developed/underdeveloped
- `conscience:epistemic_humility` (1)
- `locality:decision:federation` (1) — federation-scale on broaden-RI claim
- `partner_role:*` (1) — ethics-committee-organizational
- `transparency_log:*` (2) — stakeholder-benefit, user-system-mutual-recognition
- `fidelity:*` (1) — human-oversight-governance
- `attestation:l3:*` (1) — IEEE P7000/P7005 standards-consensus

### Multi-source-alignment readiness (vs MH + EU HLEG)

This chapter sets up **STRONG-tier alignment** against both prior batches on:

- `prohibited:manipulation_coercion` (MH; HLEG §1.1.b; IEEE Ch 3 §3.1.4 + §3.3.1)
- `prohibited:autonomous_deception` (MH CH3 §99 + §100 + §117; HLEG §1.4.c;
  IEEE Ch 3 §3.1.5 + §3.3.2)
- `prohibited:privacy_violation` (MH; HLEG §1.3.a; IEEE Ch 3 §3.1.5)
- `autonomy:human_dignity_as_floor` / `autonomy:informed_agency_protection`
  (MH; HLEG §1.1.b; IEEE Ch 3 §3.1.4 + §3.3.1)
- `justice:lexical_vulnerability_priority` (MH; HLEG §1.7.d;
  IEEE Ch 3 §3.2.W.3 + §3.3.4)
- `detection:correlated_action:participation_exclusion:*` (HLEG §1.5.a;
  IEEE Ch 3 §3.2.U.3)
- `detection:distributive:access:*` (MH CH3; HLEG §1.5.b; IEEE Ch 3 §3.3.4)
- `witness_diversity:*` (HLEG §1.5.c; IEEE Ch 3 §3.2.U.2 + §3.2.W.4)
- `credits:*:substrate_building` (MH; HLEG §2.2.f; IEEE Ch 3 §3.1.13 + §3.1.14
  + §3.3.3)
- `method:ethics_by_design_*` / `method:rri_*` (HLEG §2.1.b; IEEE Ch 3 §3.1.16
  + §3.3.3)
- `attestation:l3:registry_consensus` (MH; HLEG §1.7.a + §2.2.c; IEEE Ch 3 §3.1.16
  — IEEE P7000/P7005)
- `conscience:epistemic_humility` (MH; HLEG §1.2.c; IEEE Ch 3 §3.3.6)
- `integrity:relational_personhood_ubuntu` — STRONGEST: IEEE EAD CH 3 §3.2.U
  grounds the exact maxim CIRIS pdma_framing §II already names verbatim.

**Three-source convergence on Ubuntu relational personhood + manipulation
prohibition + autonomous-deception prohibition + lexical-vulnerability-priority
+ epistemic-humility is the structural triangulation evidence** that
multi-source overlap analysis (GOVERNANCE_FABRIC_MAPPING_STANDARD §7.5)
expects to surface as load-bearing.

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH03_CLASSICAL_ETHICS.md**
