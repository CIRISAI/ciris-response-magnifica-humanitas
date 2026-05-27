# CONTRIBUTION_OBJECTS_IEEE_EAD_CH11_LAW.md
# IEEE Ethically Aligned Design First Edition (2019) — Chapter "Law"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 11449–14140 substantive;
#         14140–16065 = contributor credits, endnotes, About-EAD — non-normative)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

This is the **longest substantive chapter** in EAD1e (~2700 lines of operative text;
the remaining ~1900 lines through line 16065 are contributor lists, endnotes, About-EAD
back matter — non-normative and not mapped per LANGUAGE_PRIMER §10/§8 Step 1(b)).

Despite its length, the chapter has a **narrower normative scope** than the prompt
framing anticipated. EAD1e itself states (lines 11480–11482): "Comprehensive coverage
of all issues within our scope of study is not feasible in a single chapter… aggregate
coverage will expand as issues not yet studied are selected for treatment in future
versions of EAD." The classical legal sub-domains the prompt named (criminal law, IP
doctrine, contract law, transnational law, agency, dispute resolution as standalone
fields) are **not separately treated** in this First Edition. The chapter is organized
into two sections only:

- **Section 1 — Norms for the Trustworthy Adoption of A/IS in Legal Systems** (lines
  11543–13860) — 6 Issues: Well-being / Impediments-to-Informed-Trust /
  Effectiveness / Competence / Accountability / Transparency. The normative target is
  **how A/IS should be adopted into legal systems** (law-making, civil justice,
  criminal justice, law enforcement) — not legal doctrine across substantive law.
- **Section 2 — Legal Status of A/IS** (lines 13871–14140) — single Issue, 7
  recommendations. Treats one question: should A/IS receive legal personhood? The
  chapter's central recommendation is **NO at this time**.

Substantive law topics (liability, contract formation by A/IS, IP authorship,
criminal liability for A/IS-caused harm, transnational choice-of-law) are
**referenced as motivating context** within Section 2 Background and Issue 5
Accountability Background, but no chapter-level recommendations are made on those
substantive-law doctrinal questions. Where they appear they translate as background
prose (T-2 PASTORAL_PROSE in the structural-framing sense per LANGUAGE_PRIMER §10).

The chapter's actual sub-domain organisation (used for grouping below):

| Sub-domain | Section | Lines | Atomic units mapped |
|---|---|---|---|
| **Sub-domain A: Well-being + Legal Systems** (incl. chapter preamble + §1 framing) | preamble + Issue 1 | 11453–11868 | 5 |
| **Sub-domain B: Informed Trust + the 4-Principle Framework** | Issue 2 | 11881–12112 | 7 |
| **Sub-domain C: Effectiveness** | Issue 3 | 12114–12572 | 9 |
| **Sub-domain D: Competence** | Issue 4 | 12577–12916 | 8 |
| **Sub-domain E: Accountability** | Issue 5 | 12876–13284 | 8 |
| **Sub-domain F: Transparency** | Issue 6 | 13285–13856 | 11 |
| **Sub-domain G: Legal Status of A/IS** (personhood) | §2 | 13871–14140 | 8 |
| **Non-normative back matter** | credits + endnotes | 14140–16065 | 1 (T-2 aggregate) |

**Scope-control discipline** per the prompt: per-Recommendation enumerated items
ARE atomic units (these are the operational claims). Background prose paragraphs
within each Issue are aggregated to **one T-2 unit per Issue background** with a
single nuance_lost line, rather than treated as individual atomic units (per the
prompt's hard rule: "background-context paragraphs may be summarized as one unit
per sub-section with T-2 PASTORAL_PROSE or counted only once"). Illustration
case-studies (State v. Loomis; Amazon Rekognition; Blue CRUSH Memphis; COMPAS) are
T-2 narrative-instance prose, aggregated.

Source quotes bounded at ≤ 2 sentences per LANGUAGE_PRIMER discipline.

---

# Sub-domain A — Well-being and Legal Systems (Section 1 framing + Issue 1)

> *"The law affects and is affected by the development and deployment of autonomous
> and intelligent systems… we focus not only on how the law responds to the
> technological innovation represented by A/IS, but also on how the law guides
> and sets the conditions for that innovation."* (lines 11453–11461)

---

## §Ch11.0 — Chapter preamble: law as both responsive and guiding for A/IS innovation

```yaml
# Lines 11453–11483 — Chapter opening; positions law as both responsive to and
# directing of A/IS innovation; identifies improvement/prosperity/well-being as the
# steering goal.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:law_as_co_constitutive_with_AIS_innovation"
      score: 1.0
      confidence: 0.85
      context: >
        "Science, technological development, law, public policy, and ethics are not
        independent fields of activity that occasionally overlap. Instead, they are
        disciplines that are fundamentally tied to each other and collectively
        interact in the creation of a social order." Approach-level claim: legal
        rules and A/IS development are co-constitutive of social order, not parallel
        domains.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 preamble lines 11453–11465"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: clean
nuance_lost: |
  The Jasanoff quotation ("law is foremost among innovation engines") is a citation
  of a senior STS scholar; the wire format encodes the operational uptake of the
  claim, not the citational provenance to Jasanoff in particular.
```

---

## §Ch11.S1.0 — Section 1 framing: norms for trustworthy adoption; 4 principles named

```yaml
# Lines 11543–11580 — Section 1 introduction; "informed trust" as the structural
# centerpiece; risks of "uninformed adoption" and "uninformed avoidance" both named;
# four principles (effectiveness / competence / accountability / transparency) named.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:trustworthy_AIS_adoption_in_legal_systems"
      score: 1.0
      confidence: 0.9
      context: >
        Section names "informed trust" as the goal-level structural object for A/IS
        adoption into legal systems, with four supporting principles (effectiveness,
        competence, accountability, transparency) as the operational decomposition.
        The dual-risk framing — uninformed adoption AND uninformed avoidance — sets
        the goal symmetrically.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 1 framing lines 11543–11580"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: goal:*)"
verdict: clean
nuance_lost: |
  "Informed trust" as a CIRIS-side construct decomposes onto the four sub-principles;
  no separate primitive is needed at goal level. The Roberts quotation ("It's a day
  that is here") is rhetorical and not separately encoded.
```

---

## §I1.bg — Issue 1 Background (aggregate): rule of law correlates with well-being; A/IS can improve legal-system function

```yaml
# Lines 11589–11806 — Issue 1 Background paragraphs: rule of law and well-being;
# Kennedy / Sen / Jasanoff citations; A/IS-as-tool potential to improve legal-system
# attributes (speedy / fair / unbiased / consistent / transparent / accessible /
# effective / accurate / adaptable); five enumerated A/IS application areas
# (lawmaking, practice of law, civil+criminal proceedings, law enforcement, citizen
# access).
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Background prose is descriptive-empirical scaffolding for the recommendations
  that follow. The substantive operational claims are carried by Recommendations
  1–2 in §I1.r below. Per LANGUAGE_PRIMER §10 T-2 doctrine and the prompt's
  scope-control directive, background-context paragraphs may be summarized as one
  unit per sub-section. The eight "attributes of a well-functioning legal system"
  (speedy, fair, free from undesirable bias, consistent, transparent, accessible,
  effective, accurate, adaptable — lines 11737–11762) are descriptive criteria,
  carried operationally by §I3 effectiveness recs, §I4 competence recs,
  §I5 accountability recs, §I6 transparency recs (cumulatively).
nuance_lost: |
  Five concrete domains where A/IS could improve legal-system functioning
  (lawmaking; legal practice / fact-finding; civil + criminal proceedings;
  law-enforcement deployment; citizen access to justice for the under-resourced)
  are catalogued descriptively (lines 11738–11787). The wire format encodes these
  via the cohort_scope + cohort-specific recommendations rather than as a
  flat enumeration.
```

---

## §I1.r1 — Issue 1 Recommendation 1: policymakers explore A/IS adoption via broad consultative dialogue

```yaml
# Lines 11808–11839
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:multi_stakeholder_consultative_dialogue_on_AIS_legal_adoption"
      score: 1.0
      confidence: 0.85
      context: >
        "Policymakers should... explore, through a broad consultative dialogue with
        all stakeholders, how A/IS can be adopted for use in their legal systems."
        Methods-level claim: the adoption decision itself must be conducted as
        broad-stakeholder consultation, not unilateral procurement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 1 Recommendation 1 lines 11808–11839"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:policymaker_for_legal_system_AIS_adoption"
      score: 1.0
      confidence: 0.85
      context: >
        The Recommendation names policymakers as the responsible partner for
        legal-system A/IS adoption decisions, with conditional subordination to the
        norms in Issues 2–6.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 1 Recommendation 1 lines 11808–11839"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
verdict: composed
nuance_lost: |
  "All stakeholders" is operationally underspecified at the wire layer; the
  consultative-dialogue method composes onto cohort_scope: community without
  enumerating which stakeholder cohorts. The "subject to mitigating risks in
  Issues 2–6" conditional is preserved by the downstream rec attestations.
```

---

## §I1.r2 — Issue 1 Recommendation 2: educational initiatives for stakeholder awareness, focus on the ordinary citizen

```yaml
# Lines 11840–11852
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:public_education_AIS_legal_system_risks_and_benefits"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments, non-governmental organizations, and professional associations
        should support educational initiatives designed to create greater awareness
        among all stakeholders of the potential benefits and risks of adopting A/IS
        in the legal system." Special focus named for "the ordinary citizen who
        interacts with the legal system as a victim or criminal defendant."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 1 Recommendation 2 lines 11840–11852"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.85
      context: >
        The Recommendation explicitly names "the ordinary citizen who interacts with
        the legal system as a victim or criminal defendant" as the priority focus.
        Composes with §6.1.4 lexical-vulnerability-priority policy: most-affected
        / least-resourced legal-system participants are the priority audience for
        adoption-information educational efforts.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 1 Recommendation 2 lines 11848–11852"
        - "FSD-002 §6.1.4 consumer-policy"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: |
  The bidirectional asymmetry — defendants AND victims both named at the
  vulnerability tier — is not separately encoded; cohort_scope: community
  captures both cohorts under the same lexical-vulnerability frame.
```

---

# Sub-domain B — Informed Trust and the Four-Principle Framework (Issue 2)

The structural-doctrinal contribution of Section 1 lives here: Issue 2 introduces
the **four principles** (effectiveness / competence / accountability / transparency)
that Issues 3-6 then expand. Per LANGUAGE_PRIMER discipline, the principle-named
attestations are emitted here; Issue 3-6 attestations are operational expansions.

---

## §I2.bg — Issue 2 Background (aggregate): risks of A/IS in legal systems; opaque decision-making; anchoring bias; "informed trust" defined

```yaml
# Lines 11881–11985 — risks (opacity; bias; bad actors; inequality; trust depletion;
# human-capital scarcity; spirit-vs-letter; surrender to nonethical agents; loss
# of privacy/dignity; erosion of democratic institutions); State v. Loomis as
# illustration; anchoring cognitive bias on legal practitioners; "informed trust"
# definition.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Issue 2 Background is risk-cataloguing and definitional scaffolding. The
  operative principles (effectiveness / competence / accountability / transparency)
  are independently attested below as constitutional-mutability claims; the risk
  catalogue's normative weight is downstream-carried by §I3-§I6 recommendations
  plus existing prohibition prefixes (`prohibited:discrimination`,
  `prohibited:privacy_violation`, `prohibited:manipulation_coercion`,
  detection:correlated_action:* for democratic-institution erosion).
nuance_lost: |
  The 11-item risk taxonomy at lines 11899–11920 is itself an operational
  catalogue that the wire format encodes only by reference to the existing
  prohibition family. The Loomis case (lines 11905–11941) is encoded
  illustratively as evidence_ref'able case-study material rather than as a
  standalone Contribution. The "spirit of the law vs. letter of the law"
  concern (line 11912) is a deeper jurisprudential claim about A/IS lacking
  the contextual-flexibility capacity that informs equitable judicial reasoning;
  CIRIS's `dma:*` family carries the agent-side analog but does not natively
  encode a "spirit vs. letter" distinction.
```

---

## §I2.p — The four-principle framework: effectiveness / competence / accountability / transparency as the structural decomposition

```yaml
# Lines 12010–12032 — The principles are characterised as design criteria for
# fostering trust: (a) individually necessary and collectively sufficient,
# (b) globally applicable but culturally flexible, (c) capable of being
# operationalised in legal-system functions.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:trust_by_four_principles_effectiveness_competence_accountability_transparency"
      score: 1.0
      confidence: 0.9
      context: >
        Approach-level structural claim: trust in A/IS adopted into legal systems
        rests on four principles together — effectiveness, competence, accountability,
        transparency — meeting the design criteria of "individually necessary and
        collectively sufficient," "globally applicable but culturally flexible," and
        "capable of being operationalised." This is the structural backbone of
        EAD1e Section 1.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 four-principle framework lines 12010–12032"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: clean
nuance_lost: |
  The design-criteria meta-claim (individually necessary + collectively sufficient
  + globally applicable + culturally flexible + operationalisable) is encoded
  implicitly in the approach attestation's "design criteria" framing in context;
  no separate primitive captures the meta-claim that "these four together are the
  *correct* decomposition." The cultural-flexibility provision composes with
  §6.1.5 locality-scaled-quorum but is not separately attested.
```

---

## §I2.p.eff — Principle "Effectiveness" definition: empirical evidence of fitness for purpose

```yaml
# Lines 12023–12029
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:empirical_fitness_for_purpose_adoption_gate"
      score: 1.0
      confidence: 0.9
      context: >
        "Adoption of A/IS in a legal system should be based on sound empirical
        evidence that they are fit for their intended purpose." Method-level
        gate-keeping criterion applied at adoption decision-time.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Effectiveness principle lines 12023–12029"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  "Sound empirical evidence" composes onto the dma:* family's evidence-grounded
  reasoning posture but is not separately quantified; threshold/confidence
  scoring lives in §I3 operational recommendations.
```

---

## §I2.p.comp — Principle "Competence" definition: creators specify required operator skills; operators adhere

```yaml
# Lines 12031–12033
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:specified_for_AIS_legal_operator_role"
      score: 1.0
      confidence: 0.9
      context: >
        "A/IS should be adopted in a legal system only if their creators specify the
        skills and knowledge required for their effective operation and if their
        operators adhere to those competency requirements." Composes with FSD-002
        §3.6.1 expertise:{domain}:{language} and licensure:{authority_id}.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Competence principle lines 12031–12033"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore Tier-1: expertise:*) + §3.9 licensure:*"
verdict: clean
nuance_lost: |
  Creator-specifies / operator-adheres is a bidirectional obligation; encoded
  with a single attestation. Issue 4 expands the dual side as separate
  recommendations.
```

---

## §I2.p.acct — Principle "Accountability" definition: clear and transparent lines of responsibility maintained across lifecycle

```yaml
# Lines 12031–12036
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "accountability:transparent_responsibility_lines_AIS_legal_lifecycle"
      score: 1.0
      confidence: 0.9
      context: >
        "A/IS should be adopted in a legal system only if all those engaged in their
        design, development, procurement, deployment, operation, and validation of
        effectiveness maintain clear and transparent lines of responsibility for
        their outcomes and are open to inquiries as may be appropriate."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Accountability principle lines 12031–12036"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity / fidelity principles)"
verdict: clean
nuance_lost: |
  Six lifecycle stages enumerated (design / development / procurement / deployment
  / operation / validation of effectiveness) — encoded as enumerated context;
  the wire format does not separately attest each stage. "Open to inquiries"
  composes with §I5 audit-readiness recommendations.
```

---

## §I2.p.trans — Principle "Transparency" definition: pertinent information accessible to stakeholders

```yaml
# Lines 12036–12042
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:AIS_legal_design_operation_effectiveness_disclosure"
      score: 1.0
      confidence: 0.9
      context: >
        "A/IS should be adopted in a legal system only if the stakeholders in the
        results of A/IS have access to pertinent and appropriate information about
        their design, development, procurement, deployment, operation, and
        validation of effectiveness."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Transparency principle lines 12036–12042"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (Verify: transparency_log:*)"
verdict: clean
nuance_lost: |
  "Pertinent and appropriate" — a stakeholder-relative disclosure scope — is
  unpacked in §I6 recommendations as a stakeholder×information-type matrix;
  this top-level attestation carries the principle, not the matrix.
```

---

## §I2.r — Issue 2 Recommendations: procurement-gating, professional-standards-adherence, insurance-pricing-on-adherence

```yaml
# Lines 12070–12087 — Recommendation 1 (government procurement gating);
# Recommendation 2 (professional adherence + demonstrability); Recommendation 3
# (insurance pricing tied to adherence to the four principles).
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:procurement_gating_on_four_principle_adherence"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments should set procurement and contracting requirements that
        encourage parties seeking to use A/IS in the conduct of business with or
        for the government, particularly with or for the court system and law
        enforcement agencies, to adhere to the principles of effectiveness,
        competence, accountability, and transparency."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Recommendation 1 lines 12071–12082"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:professional_demonstrability_of_four_principle_adherence"
      score: 1.0
      confidence: 0.85
      context: >
        "Professionals engaged in the practice, interpretation, and enforcement of
        the law... should require, at a minimum, that those providers adhere to, and
        be able to demonstrate adherence to, the principles." Public-accessibility
        clause on demonstrations composes with transparency_log:*.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Recommendation 2 lines 12083–12082"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:liability_insurance_pricing_on_four_principle_adherence"
      score: 1.0
      confidence: 0.8
      context: >
        "Regulators should permit insurers to issue professional liability and other
        insurance policies that consider whether the insured (either a provider or
        operator of A/IS in a legal system) adheres to the principles of
        effectiveness, competence, accountability, and transparency." Market-based
        incentive-alignment mechanism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 2 Recommendation 3 lines 12063–12069"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  The procurement-gating, professional-demonstrability, and insurance-pricing
  recommendations all use the four principles as their normative spine; the
  wire format encodes them as three separate method:* attestations rather than
  decomposing each onto the four sub-principles. Government-efforts
  transparency clauses (lines 12081–12082 and 12089) compose with
  transparency_log:* but are not separately attested.
```

---

# Sub-domain C — Effectiveness (Issue 3)

> *"How can the collection and disclosure of evidence of effectiveness of A/IS
> foster informed trust in the suitability of A/IS for adoption in legal systems?"*

Issue 3 has 11 enumerated recommendations covering benchmarking infrastructure,
data-set creation, validation practices, metric design, stakeholder education,
and operator-side measurement guidance. Background prose is aggregated T-2.

---

## §I3.bg — Issue 3 Background (aggregate): what constitutes effectiveness; intended-purpose-plus-collateral-concerns frame

```yaml
# Lines 12124–12450 — definitional discussion of effectiveness as "fit for purpose"
# inclusive of collateral concerns; herbicide-collateral-harm analogy;
# generic-vs-specific measurement debate; intended consumers of measurement
# results.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Definitional and methodological scaffolding for the 11 recommendations.
  Aggregated per the prompt's "background-context paragraphs may be summarized
  as one unit per sub-section" directive. The herbicide-collateral-harm analogy
  (lines 12122–12131) is a pedagogical illustration.
nuance_lost: |
  The "intended purpose plus collateral consequences" definition of
  effectiveness (line 12120) is a richer conception than narrow specification-
  conformance; this richer conception is operationalised across the 11
  recommendations rather than encoded as a separate primitive.
```

---

## §I3.r1 — Issue 3 Recommendation 1: benchmarking infrastructure (government-supported, publicly-accessible)

```yaml
# Lines 12455–12476
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:government_supported_AIS_legal_benchmarking_infrastructure"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments should fund and support the establishment of ongoing
        benchmarking exercises designed to provide valid, publicly accessible
        measurements of the effectiveness of A/IS deployed, or potentially deployed,
        in the legal system." NIST-style nonregulatory measurement laboratory cited
        as example mechanism.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 1 lines 12455–12476"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Benchmarking-as-infrastructure decomposes onto truth_grounding:* and
  weighted_aggregate:* in CIRIS's consensus family at federation level; here it
  is encoded at the community-cohort level as a public-sector infrastructure
  method.
```

---

## §I3.r2 — Issue 3 Recommendation 2: government-facilitated effectiveness data-set creation balancing privacy

```yaml
# Lines 12477–12489
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:public_evaluation_dataset_creation_with_privacy_safeguards"
      score: 1.0
      confidence: 0.8
      context: >
        "Governments should facilitate the creation of data sets that can be used for
        purposes of evaluating the effectiveness of A/IS as applied in the legal
        system. In assisting in the creation of such data sets, governments and
        administrative agencies will have to take into consideration potentially
        competing societal values, such as the protection of personal data."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 2 lines 12477–12489"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  The privacy-vs-evaluability tension is operational guidance rather than a
  separate primitive; composes implicitly with prohibited:privacy_violation
  as the privacy floor.
```

---

## §I3.r3 — Issue 3 Recommendation 3: creators pursue valid measurement; describe procedures/results without disclosing IP; open to examination

```yaml
# Lines 12490–12498
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:effectiveness_procedures_and_results_disclosure_minus_IP"
      score: 1.0
      confidence: 0.85
      context: >
        "Creators of A/IS to be applied to legal matters should pursue valid measures
        of the effectiveness of their systems... Creators should describe the
        procedures and results of the testing in clear language that is understandable
        to both experts and nonexperts, and should do so without disclosing
        intellectual property."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 3 lines 12490–12498"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (Verify: transparency_log:*)"
verdict: clean
nuance_lost: |
  The "describe without disclosing IP" balance is operational guidance composing
  with key_boundary:downstream_propagation (IP boundary); not separately
  attested.
```

---

## §I3.r4-6 — Issue 3 Recommendations 4-6: researchers define metrics with stakeholder input; creators ensure metrics are accessible; educational efforts on metrics literacy

```yaml
# Lines 12466–12489 — three recommendations on metric-design participation, metric-
# accessibility, and metric-literacy education.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:metric_codesign_with_stakeholder_input"
      score: 1.0
      confidence: 0.85
      context: >
        "Researchers engaged in the study and development of A/IS for use in the
        legal system should seek to define meaningful metrics that gauge the
        effectiveness of the systems they study. In selecting and defining metrics,
        researchers should seek input from all stakeholders in the outcome of the
        given application of A/IS in the legal system."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 4 lines 12466–12476"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:effectiveness_metrics_stakeholder_accessibility"
      score: 1.0
      confidence: 0.85
      context: >
        "Creators of A/IS for use in the legal system should ensure that the
        effectiveness metrics defined by the research community are readily
        obtainable and accessible to all stakeholders, including, when appropriate,
        the general public. Creators should provide guidance on how to interpret and
        respond to the metrics generated by the system."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 6 lines 12490–12498"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (Verify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:metrics_literacy_education_for_operators_and_affected"
      score: 1.0
      confidence: 0.8
      context: >
        "Governments and industry associations should undertake educational efforts
        to inform both those engaged in the operation of A/IS deployed in the legal
        system and those affected by the results of their operation of the salient
        measures of effectiveness and what they can indicate about the capabilities
        and limitations of the A/IS in question."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 5 lines 12477–12489"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  Three closely-related recommendations on metric-codesign-and-literacy
  pipeline; encoded as three separate primitives rather than a single composite
  to preserve the distinct roles (researchers / creators / governments).
```

---

## §I3.r7 — Issue 3 Recommendation 7: operators follow measurement guidance for the systems they use

```yaml
# Lines 12516–12530
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:operator_adherence_to_measurement_guidance"
      score: 1.0
      confidence: 0.85
      context: >
        "Operators of A/IS applied to a legal task should follow the guidance on the
        measurement of effectiveness provided for the A/IS being used. This includes
        guidance about which metrics to obtain, how and when to obtain them, how to
        respond to given results."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 7 lines 12516–12530"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: clean
nuance_lost: |
  Operator-fidelity to creator-specified measurement procedures is encoded as
  an Accord-principle fidelity claim; the procedural enumeration in the
  recommendation (which metrics / how + when / how to respond) is operational
  content carried in context.
```

---

## §I3.r8 — Issue 3 Recommendation 8: qualitative supplement to quantitative effectiveness measurement

```yaml
# Lines 12516–12531
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:qualitative_supplement_to_quantitative_effectiveness"
      score: 1.0
      confidence: 0.85
      context: >
        "In interpreting and responding to measurements of the effectiveness of
        A/IS applied to legal problems or questions, allowance should be made by
        those interpreting the results for variation in the specific objectives and
        circumstances of a given deployment of A/IS. Quantitative results should be
        supplemented by qualitative evaluation."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 8 lines 12516–12531"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:judgment_for_quantitative_qualitative_synthesis"
      score: 1.0
      confidence: 0.8
      context: >
        "This evaluation should be done by an individual with the technical expertise
        and pragmatic experience needed to make a sound judgment." Explicit expertise
        gating on the interpretive role.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 8 lines 12526–12530"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore Tier-1: expertise:*)"
verdict: composed
nuance_lost: |
  The Goodhart-resistance / contextual-flexibility concern (line 12519: "allowance
  for variation in specific objectives and circumstances") composes with
  CIRIS's `progress_measure:*` requirement for goodhart_resistance but does not
  reach a separate primitive.
```

---

## §I3.r9 — Issue 3 Recommendation 9: industry-association standards for measurement and reporting

```yaml
# Lines 12532–12537
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:industry_collaborative_measurement_reporting_standards"
      score: 1.0
      confidence: 0.85
      context: >
        "Industry associations or other organizations should collaborate on
        developing standards for measuring and reporting on the effectiveness of
        A/IS. These standards should be developed with input from both the
        scientific and legal communities."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 3 Recommendation 9 lines 12532–12537"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Inter-community (scientific + legal) standards co-development is encoded with
  cohort_scope: community; the multi-discipline character is carried in context.
```

---

## §I3.r10-11 — Issue 3 Recommendations 10-11: re-application of Issue 2 procurement-gating and professional-adherence with respect to effectiveness

```yaml
# Lines 12539–12544 — re-application clauses pointing back to §I2.r1 / §I2.r2
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Cross-reference clauses ("Recommendation 1 under Issue 2, with respect to
  effectiveness" — line 12539; "Recommendation 2 under Issue 2, with respect to
  effectiveness" — line 12543). The substantive claims are already carried by
  §I2.r emissions above; restating with effectiveness-specific scope would be
  redundant.
nuance_lost: |
  The cross-reference structure (each subsequent Issue 3-6 closes with two such
  pointer-back recommendations) functions as a normative compounding mechanism;
  the wire format does not separately encode this repeat-by-reference pattern,
  but the four §I2.r attestations are properly read as applying severally across
  Issues 3-6.
```

---

# Sub-domain D — Competence (Issue 4)

> *"How can specification of the knowledge and skills required of the human
> operator(s) of A/IS foster informed trust in the suitability of A/IS for
> adoption in legal systems?"*

Issue 4 has 8 enumerated recommendations covering operator-knowledge specification,
operating-policy authorship, integrated safeguards, individual-notification rights
for affected parties + appeal to human-review, professional codes of ethics
update, operator-competence acquisition, plus re-application clauses.

---

## §I4.bg — Issue 4 Background (aggregate): human-operator integral to A/IS; surgery/pilot accreditation analogy; Amazon Rekognition + ACLU illustration

```yaml
# Lines 12589–12790 — competence-as-confidence framing; surgeon/pilot analogy;
# human-mediation roles enumerated; ABA / law-school / Federal Judicial Center
# training pathways; Amazon Rekognition / ACLU test illustration of competence
# failure-mode.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Background scaffolding. The Rekognition illustration (lines 12763–12790) is
  a concrete failure-mode narrative supporting the operational claim that both
  creators (specification) and operators (adherence) bear competence
  responsibility — that claim is carried operationally by §I4.r1 + §I4.r6
  below.
nuance_lost: |
  The "decision subjects + victims of crime + communities + general public"
  enumeration of competence-trust stakeholders (lines 12723–12731) reflects a
  wider stakeholder taxonomy than CIRIS's witness_diversity primitive natively
  exposes; the taxonomy composes onto cohort_scope variation rather than a
  separate primitive.
```

---

## §I4.r1 — Issue 4 Recommendation 1: creators provide clear guidance on required operator knowledge, skills, experience, and risks of failure

```yaml
# Lines 12791–12816
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:creator_specifies_operator_competence_and_failure_risks"
      score: 1.0
      confidence: 0.9
      context: >
        "Creators of A/IS for application in legal systems should provide clear and
        accessible guidance for the knowledge, skills, and experience required of
        the human operators of the A/IS if the systems are to achieve expected
        levels of effectiveness. Included in that guidance should be a delineation
        of the risks involved if those requirements are not met."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 1 lines 12791–12816"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore Tier-1: expertise:*)"
verdict: clean
nuance_lost: |
  Documentation-accessibility-by-experts-and-nonexperts clause composes with
  transparency_log:* but is not separately attested.
```

---

## §I4.r2 — Issue 4 Recommendation 2: creators publish written operating policies covering use, training, gauging, interpretation, expected outcomes, risks, override conditions

```yaml
# Lines 12817–12852
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:creator_published_operating_policy_seven_clauses"
      score: 1.0
      confidence: 0.85
      context: >
        "Creators and developers of A/IS for application in legal systems should
        create written policies that govern how the A/IS should be operated."
        Seven specified content clauses: real-world application specification;
        preconditions for effective use; required operator training/skills;
        effectiveness gauging procedures; result interpretation considerations;
        expected outcomes under proper operation; specific risks under improper
        use. Plus override-conditions specification. All such policies publicly
        accessible.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 2 lines 12817–12852"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:operating_policy_public_accessibility"
      score: 1.0
      confidence: 0.85
      context: >
        "All such policies should be publicly accessible." Public-accessibility
        requirement on the operating-policy artifact.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 2 line 12852"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (Verify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The seven content-clauses enumeration is carried in context rather than
  decomposed into seven separate primitives. The bidirectional input
  (creators draw on input from legal professionals — line 12820–12823) is a
  participatory-codesign clause composing with §I3.r4 but not separately
  attested.
```

---

## §I4.r3 — Issue 4 Recommendation 3: creators integrate safeguards against incompetent operation

```yaml
# Lines 12854–12867
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:integrated_safeguards_against_incompetent_operation"
      score: 1.0
      confidence: 0.85
      context: >
        "Creators and developers of A/IS to be applied in legal systems should
        integrate safeguards against the incompetent operation of their systems.
        Safeguards could include issuing notifications and warnings to operators in
        certain conditions; limiting access to A/IS functionality based on the
        operator's level of expertise; enabling system shut-down in potentially
        high-risk conditions."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 3 lines 12854–12867"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Context-sensitive policy flexibility (line 12822–12826) is encoded as a
  meta-clause on the safeguards method; the framework's locality:decision:*
  composition does similar work at the policy layer but is not separately
  attested here.
```

---

## §I4.r4 — Issue 4 Recommendation 4: individual notification + recourse-to-human-judgment appeal right when A/IS affects legal outcome

```yaml
# Lines 12825–12832 — HIGH-VALUE OPERATIONAL CLAIM: affected individual has a right
# to (a) notification that A/IS played a role, and (b) appeal to a competent human.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:affected_party_notification_of_AIS_role_in_legal_outcome"
      score: 1.0
      confidence: 0.9
      context: >
        "Governments should provide that any individual whose legal outcome is
        affected by the application of A/IS should be notified of the role played by
        A/IS in that outcome."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 4 lines 12825–12829"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:appeal_to_human_judgment_against_AIS_legal_outcome"
      score: 1.0
      confidence: 0.9
      context: >
        "Further, the affected party should have recourse to appeal to the judgment
        of a competent human being." Reconsideration-shaped right of appeal,
        substrate-anchored to a competent human reviewer rather than another A/IS.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 4 lines 12830–12832"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore Correction: reconsideration:*) — analog"
verdict: composed
nuance_lost: |
  This is one of the chapter's most operationally consequential claims —
  combined notification + appeal-to-human-judgment establishes a baseline
  procedural-due-process floor for A/IS-affected legal outcomes. CIRIS's
  `reconsideration:{grounds}` primitive at NodeCore §3.6.4 is shaped for the
  federation-internal appeal-of-verdicts case; the structural pattern composes
  but the "appeal-to-human-substrate" requirement (i.e., the appellate
  reviewer MUST be a human, not another A/IS) is an additional substrate-
  selection requirement on the reviewer key_id that is not natively
  expressed by the existing reconsideration primitive. Flagged as a candidate
  for synthesis review against MH §214–§215 and EU HLEG Article 22-analog
  patterns.
```

---

## §I4.r5 — Issue 4 Recommendation 5: legal professional codes of ethics and education recognise specialized A/IS expertise

```yaml
# Lines 12833–12852
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:legal_profession_codes_of_ethics_recognise_AIS_expertise"
      score: 1.0
      confidence: 0.85
      context: >
        "Professionals engaged in the creation, practice, interpretation, and
        enforcement of the law, such as lawyers, judges, and law enforcement
        officers, should recognize the specialized scientific and professional
        expertise required for the ethical and effective application of A/IS to
        their professional duties. The professional associations to which such legal
        practitioners belong, such as the American Bar Association, should, through
        both educational programs and professional codes of ethics, seek to ensure
        that their members are well informed."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 5 lines 12833–12852"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  The named institutional examples (ABA, Federal Judicial Center, law schools)
  are concrete but jurisdiction-specific; the claim's species-cohort generality
  composes onto community-scoped attestation since the recommendation targets
  specific professional-association mechanisms.
```

---

## §I4.r6 — Issue 4 Recommendation 6: operators acquire necessary competencies or identify supporting experts; supervisor-of-A/IS competence-accountability

```yaml
# Lines 12873–12883
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:operator_acquires_or_accesses_required_competence"
      score: 1.0
      confidence: 0.85
      context: >
        "The operators of A/IS applied in legal systems—whether the operator is a
        specialist in A/IS or a legal professional—should understand the
        competencies required for the effective performance of their roles and
        should either acquire those competencies or identify individuals with those
        competencies who can support them in the performance of their roles."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 4 Recommendation 6 lines 12873–12883"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: clean
nuance_lost: |
  The "or identify individuals with those competencies" provision encodes a
  delegated-expertise model; composes with delegates_to structural primitive but
  is best preserved as a fidelity-attestation on the operator since the operator
  retains overall role-fidelity even when delegating sub-tasks.
```

---

## §I4.r7-8 — Issue 4 Recommendations 7-8: re-application of Issue 2 procurement-gating and professional-adherence with respect to competence

```yaml
# Lines 12884–12887
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Cross-reference re-application clauses pointing back to §I2.r emissions.
  Pattern identical to §I3.r10-11.
nuance_lost: |
  The §I2 four-principle procurement-gating + professional-adherence pattern
  applies severally across Issues 3-6 (carried by the §I2.r attestations
  above).
```

---

# Sub-domain E — Accountability (Issue 5)

> *"How can the ability to apportion responsibility for the outcome of the
> application of A/IS foster informed trust in the suitability of A/IS for
> adoption in legal systems?"*

Issue 5 has 8 enumerated recommendations. The Background frames the dual
challenges of black-box opacity and responsibility-diffuseness; develops the
"It's hard to say → No one / Everyone" failure-mode argument; introduces the
human-appeal additional note + Loomis / COMPAS illustration.

---

## §I5.bg — Issue 5 Background (aggregate): opacity + diffuseness; "blaming the algorithm" failure mode; need for human-appeal review

```yaml
# Lines 12888–13230 — opacity (model complexity + ML-self-modification per New &
# Castro citation) and diffuseness (multi-vendor + open-source component chain per
# Scherer citation) as the two structural accountability obstacles; "It's hard to
# say" failure mode; existing-norms-insufficient observation (contractual + ABA
# professional codes + judicial procedures cited as helpful but inadequate);
# governing-model-plus-audit pattern as the proposed solution; Loomis / COMPAS /
# probabilistic-DNA / remote-hacking-software illustration cluster on the
# trade-secret accountability tension.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Background prose, operational scaffolding for the 8 recommendations. The "human
  appeal review" Additional Note 2 (lines 13164–13189) is closely related to
  §I4.r4 above; it is preserved by that earlier attestation. The Loomis case
  recap (lines 13192–13234) repeats material already cited in §I2.bg.
nuance_lost: |
  The Scherer quotation on multi-component A/IS responsibility-diffusion (lines
  12986–12989) is a substantive doctrinal observation: components designed
  years prior for unrelated purposes, then incorporated into A/IS that causes
  harm, create a "design-decision-far-removed-in-time-and-geography"
  apportionment problem. This composes with provenance:slsa:* and
  provenance:build_manifest:* for the supply-chain-transparency layer, but the
  doctrinal claim that *moral responsibility tracks design-decision proximity*
  is jurisprudential and not separately encoded. Flagged for cross-document
  synthesis with MH §163 supply-chain attestation framings.
```

---

## §I5.r1 — Issue 5 Recommendation 1: creators articulate well-defined responsibility lines among all engaged in development+operation

```yaml
# Lines 13236–13242
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "accountability:articulated_responsibility_lines_creator_documented"
      score: 1.0
      confidence: 0.9
      context: >
        "Creators of A/IS to be applied in a legal system should articulate and
        document well-defined lines of responsibility, among all those who would be
        engaged in the development and operation of the A/IS, for the outcome of
        the A/IS."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 1 lines 13236–13242"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity / fidelity principles)"
verdict: clean
nuance_lost: |
  Creator-side responsibility-line documentation composes with audit_chain:*
  and provenance:build_manifest:* but is encoded as a single accountability-
  principle attestation since the recommendation's normative target is the
  ARTICULATION + DOCUMENTATION practice rather than a specific evidentiary
  artifact.
```

---

## §I5.r2 — Issue 5 Recommendation 2: adopters and operators understand their responsibilities + potential liability under unsettled-doctrine conditions

```yaml
# Lines 13243–13250
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:adopter_operator_responsibility_understanding_pre_deployment"
      score: 1.0
      confidence: 0.85
      context: >
        "Those engaged in the adoption and operation of A/IS to be applied in a
        legal system should understand their specific responsibilities for the
        outcome of the A/IS as well as their potential liability should the A/IS
        produce an outcome other than that intended. In the case of A/IS, many
        questions of legal liability remain unsettled."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 2 lines 13243–13250"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: clean
nuance_lost: |
  The "many questions of legal liability remain unsettled" epistemic-humility
  clause is preserved by confidence < 1.0 and the amendable mutability — but
  the unsettledness as a substantive observation about the state of A/IS
  liability doctrine is descriptive and not separately encoded as a primitive.
```

---

## §I5.r3 — Issue 5 Recommendation 3: contractual responsibility-allocation clauses between A/IS providers and buyers

```yaml
# Lines 13251–13257
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:contractual_responsibility_allocation_clauses_AIS_legal_supply"
      score: 1.0
      confidence: 0.85
      context: >
        "When negotiating contracts for the provision of A/IS products and services
        for use in the legal system, providers and buyers of A/IS should include
        contractual terms specifying clear lines of responsibility for the outcomes
        of the systems being acquired."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 3 lines 13251–13257"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Contract-based allocation is a private-ordering mechanism rather than a
  public-law mechanism; CIRIS's federation-substrate composes onto signed
  bilateral attestations at the contracting-pair scope. Cohort scope kept at
  community to reflect that the contract is between two firm-cohort parties.
```

---

## §I5.r4 — Issue 5 Recommendation 4: creators/operators/employer orgs amenable to internal-oversight + external-review-board inquiries; audit-readiness documentation

```yaml
# Lines 13218–13235
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:audit_amenability_internal_oversight_plus_external_review_board"
      score: 1.0
      confidence: 0.9
      context: >
        "Creators and operators of A/IS applied in a legal system, and the
        organizations that employ them, should be amenable to internal oversight
        mechanisms and inquiries (or audits) that have the objective of allocating
        responsibility for the outcomes generated by the A/IS. In the case of A/IS
        adopted and deployed by organizations that have direct public interaction
        (e.g., a law enforcement agency), oversight and inquiry could also be
        conducted by external review boards."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 4 lines 13218–13235"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "audit_chain:salient_procedures_decisions_tests_documentation"
      score: 1.0
      confidence: 0.9
      context: >
        "Being prepared for such inquiries means maintaining clear documentation of
        all salient procedures followed, decisions made, and tests conducted in
        the course of developing and applying the A/IS." Direct match to
        audit_chain:* substrate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 4 lines 13231–13235"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.3 (Persist: audit_chain:*)"
verdict: composed
nuance_lost: |
  The "external review boards" provision for public-interacting deployments
  introduces an oversight-locality dimension (public-facing deployments require
  external boards; private deployments need only internal mechanisms). CIRIS's
  locality:decision:* composes but is encoded only via cohort_scope here.
  Public-interaction case-study (law enforcement) is illustrative.
```

---

## §I5.r5 — Issue 5 Recommendation 5: organisational incentive mechanisms for ethical adherence + accountability preservation (Goodhart-resistant)

```yaml
# Lines 13236–13250
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:individual_collective_incentives_for_ethical_adherence_preserving_accountability"
      score: 1.0
      confidence: 0.85
      context: >
        "Organizations engaged in the development and operation of A/IS for legal
        tasks should consider mechanisms that will create individual and collective
        incentives for ensuring both that the outcomes of the A/IS adhere to
        ethical standards and that accountability for those outcomes is maintained,
        e.g., mechanisms to ensure that speed and efficiency are not rewarded at
        the expense of a loss of accountability."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 5 lines 13236–13250"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  The "speed and efficiency not rewarded at the expense of accountability"
  example is a concrete Goodhart-resistance claim; composes with
  `progress_measure:*` requirement for goodhart_resistance at NodeCore §3.6.2
  but is not separately attested as a detection:* primitive since this is
  prescriptive (about incentive design) rather than diagnostic.
```

---

## §I5.r6 — Issue 5 Recommendation 6: inquiries take all human agents along the lifecycle into account

```yaml
# Lines 13264–13273
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:lifecycle_inclusive_responsibility_apportionment_inquiry"
      score: 1.0
      confidence: 0.85
      context: >
        "Those conducting inquiries to determine responsibility for the outcomes of
        A/IS applied in a legal system should take into consideration all human
        agents involved in the design, development, procurement, deployment,
        operation, and validation of effectiveness of the A/IS and should assign
        responsibility accordingly."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 5 Recommendation 6 lines 13264–13273"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Lifecycle-inclusive enumeration of agents (design / development / procurement /
  deployment / operation / validation) preserved in context. Apportionment-
  accordingly is not separately quantified; encodes responsibility apportionment
  as a method-level practice rather than a per-agent score.
```

---

## §I5.r7-8 — Issue 5 Recommendations 7-8: re-application of Issue 2 procurement-gating and professional-adherence with respect to accountability

```yaml
# Lines 13274–13277
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Cross-reference re-application clauses; pattern identical to §I3.r10-11
  and §I4.r7-8.
nuance_lost: |
  Carried by §I2.r attestations above.
```

---

# Sub-domain F — Transparency (Issue 6)

> *"How can sharing information that explains how A/IS reached given decisions
> or outcomes foster informed trust in the suitability of A/IS for adoption in
> legal systems?"*

Issue 6 is the longest and most operationally textured of the four-principle
Issues. Background develops the stakeholder×information-type matrix (5
stakeholder categories × 5 information categories = 25 disclosure decisions); the
Memphis Blue CRUSH illustration is extensive. 11 enumerated recommendations.

---

## §I6.bg — Issue 6 Background (aggregate): elements of transparency, stakeholder×information matrix, transparency-tension considerations, counterfactual-explanation alternative, Blue CRUSH illustration

```yaml
# Lines 13285–13710 — definitions; transparency as means-to-trust framing; five
# stakeholder categories enumerated (operators / decision-subjects / public-interest
# stewards / general public / "indirectly affected" communities + "interested in
# legal-system functioning" experts); five information categories (procedural;
# data; effectiveness/performance; model-specification; explanation); the matrix-
# disclosure-decision frame; tension considerations (privacy / IP / security-
# adversarial-attacks; explainability vs. performance; transparency vs.
# inquiry-question-fit); counterfactual-explanation alternative ("you were denied
# because income was X" without disclosing model); transparency-principle
# intersections with the other three principles; Memphis Blue CRUSH illustration.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Background scaffolding; the stakeholder×information matrix is a structural
  decision tool. The matrix itself (lines 13462–13524) is descriptive — the
  cells in the printed table contain "?" placeholders, indicating that the
  chapter is offering the framework but not pre-resolving the disclosure
  decisions. The substantive operational claims are carried by the 11
  recommendations below.
nuance_lost: |
  The "counterfactual explanation" alternative (lines 13598–13610) is a notable
  alternative-design pattern that does not collapse into transparency_log:*
  cleanly — it is a *legibility* mechanism that gives the affected party
  actionable understanding without disclosing the underlying model. CIRIS's
  `dma:*` rationale-paragraph examples carry the agent-side analog (the agent
  produces an explanation it itself can give), but the wire format does not
  separately attest the counterfactual-vs-full-disclosure design choice.
  Flagged for synthesis-pattern review.

  The five-stakeholder taxonomy goes beyond the four CIRIS cohort_scope tiers;
  "indirectly affected community members" is a structural cohort the wire
  format encodes via cohort_scope: community + cohort-specific tagging rather
  than a separate stakeholder-class primitive.
```

---

## §I6.r1 — Issue 6 Recommendation 1: government + professional associations facilitate inclusive multi-stakeholder transparency-balance dialogue

```yaml
# Lines 13732–13765
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:multi_stakeholder_transparency_balance_dialogue"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments and professional associations should facilitate dialogue among
        stakeholders... on the question of achieving a balance between transparency
        and other priorities, e.g., security, privacy, appropriate property rights,
        efficient and uniform response by the legal system."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 1 lines 13732–13765"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Five-stakeholder enumeration carried in context; circumstantial-variation
  flexibility composes with the §I2.p design-criterion "culturally flexible"
  but is not separately attested.
```

---

## §I6.r2 — Issue 6 Recommendation 2: stakeholder×information disclosure-decision matrix design discipline

```yaml
# Lines 13767–13772
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:stakeholder_information_matrix_disclosure_design"
      score: 1.0
      confidence: 0.85
      context: >
        "Policymakers developing frameworks for realizing transparency in A/IS
        applied to legal tasks should require that any frameworks they develop are
        sensitive both to the distinctions among the types of information that might
        be disclosed and to the distinctions among categories of individuals who may
        seek information." Encodes the structural-design discipline that
        transparency frameworks operate at the stakeholder×information-type level
        of granularity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 2 lines 13767–13772"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Matrix-shaped disclosure-decision granularity is operationally specific; the
  wire format's cohort_scope variation carries the stakeholder-axis but the
  information-type axis remains operational guidance rather than wire-level.
```

---

## §I6.r3 — Issue 6 Recommendation 3: IP protection considered but cannot shield disclosure needed to ascertain effectiveness/fairness/safety

```yaml
# Lines 13725–13742
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:IP_protection_bounded_by_effectiveness_fairness_safety_disclosure_floor"
      score: 1.0
      confidence: 0.9
      context: >
        "Policymakers developing frameworks for realizing transparency in A/IS to
        be adopted in a legal system should consider the role of appropriate
        protection for intellectual property, but should not allow those concerns to
        be used as a shield to prevent duly limited disclosure of information needed
        to ascertain whether A/IS meet acceptable standards of effectiveness,
        fairness, and safety."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 3 lines 13725–13742"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:trade_secret_no_shield_against_due_process_inquiry"
      score: 1.0
      confidence: 0.85
      context: >
        Implicit normative claim foregrounded by the §I5.bg Loomis discussion: IP
        protections cannot bar the disclosure necessary to evaluate whether A/IS
        affect legal outcomes within acceptable fairness/safety/effectiveness
        bounds. This carries the doctrinal weight (against the Wisconsin Supreme
        Court's Loomis posture) into the species-cohort recommendation set.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 3 lines 13725–13742"
        - "ead1e §Ch11 Issue 2 + Issue 5 Loomis discussion lines 11905–11941, 13192–13234"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: |
  This is structurally one of the chapter's most consequential recommendations
  — it carves a clear normative line through the IP-vs-due-process tension
  that the Loomis decision left ambiguous. The CIRIS framework's encoding
  uses justice:* + method:* together because the disclosure-floor is both
  jurisprudentially normative (justice) and procedurally operational (method).
  The "duly limited" qualifier preserves proportionality but is encoded in
  context rather than separately.
```

---

## §I6.r4 — Issue 6 Recommendation 4: "public interest steward" / "trusted third party" with bounded sensitive-information access

```yaml
# Lines 13740–13765 — POTENTIAL T-3 SURFACE: introduces a stewardship role with
# bounded disclosure scope that is not natively expressed in the wire format.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:public_interest_steward_for_AIS_legal_disclosure"
      score: 1.0
      confidence: 0.8
      context: >
        "Policymakers... should consider the option of creating a role for a
        specially designated 'public interest steward', or 'trusted third party',
        who would be given access to sensitive information not accessible to
        others. Such a public interest steward would be charged with assessing the
        information to answer the public interest questions at hand but would be
        under obligation not to disclose the specifics of the information accessed
        in arriving at those answers."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 4 lines 13740–13765"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:public_interest_steward_can_inspect_cannot_redisclose"
      score: 1.0
      confidence: 0.8
      context: >
        Structural property of the public-interest-steward role: read-access to
        sensitive disclosures, no re-disclosure outside the steward's assessment
        output. Composes with key_boundary:downstream_propagation as a no-
        propagate boundary attached to the steward's role rather than the data
        itself.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 4 lines 13755–13765"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (Edge: key_boundary:*)"
verdict: composed
nuance_lost: |
  The "public interest steward" pattern composes via partner_role:* +
  key_boundary:*, but the substantive role design — *bounded read; bounded
  speak; bounded to assess against a public-interest question rather than to
  inform downstream parties* — is a more specific structural object than
  partner_role:* alone carries. The composition is fragile: a future
  framework batch that names a "civil-society steward" with the same shape
  would need to re-compose rather than reuse a clean steward primitive.
  Flagged as a CANDIDATE T-3 in the chapter closing summary.
```

---

## §I6.r5 — Issue 6 Recommendation 5: designers design for selective transparency (some disclosable, IP protected)

```yaml
# Lines 13767–13789
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:designed_for_selective_transparency_disclosable_vs_IP_protected"
      score: 1.0
      confidence: 0.85
      context: >
        "Designers of A/IS should design their systems with a view to meeting
        transparency requirements, i.e., so as to enable some categories of
        information about the system and its performance to be disclosed while
        enabling other categories, such as intellectual property, to be protected."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 5 lines 13767–13789"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Selective-transparency as a design property composes with key_boundary:* at
  the data-flow layer but is encoded as a method:* design-discipline since the
  claim is about design practice, not a specific information-flow constraint.
```

---

## §I6.r6 — Issue 6 Recommendation 6: contractual specification of category-to-recipient disclosure terms in A/IS provision contracts

```yaml
# Lines 13790–13797
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:contractual_disclosure_category_to_stakeholder_terms"
      score: 1.0
      confidence: 0.85
      context: >
        "When negotiating contracts for the provision of A/IS products and services
        for use in the legal system, providers and buyers of A/IS should include
        contractual terms specifying what categories of information will be
        accessible to what categories of individuals who may seek information about
        the design, operation, and results of the A/IS."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 6 lines 13790–13797"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Direct application of the §I6.r2 stakeholder×information matrix to the
  contracting context; treated as a single method:* attestation rather than
  decomposed into all matrix-cell decisions.
```

---

## §I6.r7 — Issue 6 Recommendation 7: other-inquiry-modes may suffice — recognise effectiveness + competence inquiries as alternative paths to informed trust

```yaml
# Lines 13799–13809
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:effectiveness_and_competence_inquiries_as_transparency_alternatives"
      score: 1.0
      confidence: 0.8
      context: >
        "In developing frameworks for realizing transparency in A/IS to be adopted
        in a legal system, policymakers should recognize that the information
        provided by other types of inquiries, e.g., examination of evidence of
        effectiveness or of operator competence, may in certain circumstances
        provide a more efficient means to informed trust."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 7 lines 13799–13809"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  The substitutability claim (other principles may substitute for
  transparency-as-source-disclosure in some circumstances) is a structural
  point about the principle-framework's substitution properties; carried as
  method-level operational guidance.
```

---

## §I6.r8 — Issue 6 Recommendation 8: error-sharing mechanisms for broadly-deployed A/IS in legal systems (facial-recognition + risk-assessment)

```yaml
# Lines 13811–13830
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:error_sharing_mechanisms_for_broadly_deployed_legal_AIS"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments should, where appropriate, work together with A/IS developers,
        as well as other stakeholders in the effective functioning of the legal
        system, to facilitate the creation of error-sharing mechanisms to enable
        the more effective identification, isolation, and correction of flaws in
        broadly deployed A/IS in their legal systems, such as a systematic facial
        recognition error in policing applications or in risk assessment
        algorithms."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 8 lines 13811–13830"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:systematic_error_in_deployed_legal_AIS"
      score: 0.6
      confidence: 0.7
      context: >
        The "facial-recognition systematic error in policing" + "risk-assessment
        algorithm systematic error" examples describe federation-scale error
        correlations across deployed A/IS instances. Composes with the F-3
        correlated-action detector at LensCore §3.5.3.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 8 lines 13821–13824"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore: detection:correlated_action:*)"
verdict: composed
nuance_lost: |
  Error-sharing infrastructure at population scale composes with the F-3
  detector but is treated here as a method:* policy recommendation; the
  detection:correlated_action:* attestation is shadow-emitted to surface the
  pattern as a federation-scale-detection candidate. Note the lower confidence
  on the detection emission: this is a recommendation TO BUILD such a
  mechanism, not a current detection.
```

---

## §I6.r9 — Issue 6 Recommendation 9: whistleblower protections for individuals reporting A/IS misuse/non-conformance/misinterpretation

```yaml
# Lines 13786–13798 — HIGH-VALUE OPERATIONAL CLAIM
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:whistleblower_protection_for_AIS_misuse_reporting"
      score: 1.0
      confidence: 0.9
      context: >
        "Governments should provide whistleblower protections to individuals who
        volunteer to offer information in situations where A/IS are not designed as
        claimed or operated as intended, or when their results are not interpreted
        correctly. For example, if a law enforcement agency is using facial
        recognition technology for a purpose that is illegal or unethical, or in a
        manner other than that in which it is intended to be used, an individual
        reporting that misuse should be given protection against reprisal."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 9 lines 13786–13798"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:reprisal_against_AIS_misuse_reporter"
      score: -1.0
      confidence: 0.9
      context: >
        Implicit prohibition: reprisal against a person reporting A/IS misuse is
        a harm class against which the whistleblower-protection method is the
        positive expression. Encoded with negative polarity at species scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Issue 6 Recommendation 9 lines 13794–13798"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  Whistleblower-protection-against-reprisal is the structural pattern: a
  positive method (protection mechanism) + a negative-polarity non_maleficence
  on the reprisal itself. The "testimonial_witness:misuse_reporter" composition
  pattern (v1.4 §3.6.3) is the singular-witness preservation for the report
  content itself; not separately attested here but logically composes.
```

---

## §I6.r10-11 — Issue 6 Recommendations 10-11: re-application of Issue 2 procurement-gating and professional-adherence with respect to transparency

```yaml
# Lines 13801–13804
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Cross-reference re-application clauses; pattern identical to §I3.r10-11,
  §I4.r7-8, §I5.r7-8.
nuance_lost: |
  Carried by §I2.r attestations above; the four-principle compounding pattern
  is now complete (effectiveness + competence + accountability + transparency
  all backed by the §I2 procurement-gating + professional-adherence base).
```

---

# Sub-domain G — Legal Status of A/IS (Section 2)

> *"What type of legal status (or other legal analytical framework) is
> appropriate for A/IS given (i) the legal issues raised by deployment of such
> technologies, and (ii) the desire to maximize the benefits of A/IS and
> minimize negative externalities?"*

Section 2's central recommendation: **A/IS should NOT be granted legal personhood
at this time**. The chapter's longest doctrinal recommendation; HIGH operational
weight; T-3 surface candidate per the prompt's watch-list.

---

## §S2.bg — Section 2 Background (aggregate): legal-personhood-multiple-options framing; corporate-personhood analogy; intervening-causation analogy; design-incentive considerations

```yaml
# Lines 13871–13999 — definitions of legal personhood; analogues (corporate, pet,
# livestock, wild-animal, child, prisoner, agency, guardianship, power-of-attorney);
# intervening-causation hammer-manufacturer-not-liable analogy and its inversion
# for A/IS designer-incentives; international-treaty constraint observation;
# moral-agency-of-A/IS jurisprudential framing.
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Background doctrinal-scaffolding; the substantive operational claims are
  carried by Recommendations 1-7 below. The corporate-personhood-abuse-analogue
  observation (lines 13920–13925: "A/IS personhood is a significant departure
  from the legal traditions of both common law and civil law") foregrounds the
  recommendations' epistemic conservatism.
nuance_lost: |
  The intervening-causation incentive-erosion argument (lines 13936–13965: if
  designers are insulated by A/IS-personhood the way hammer-manufacturers are
  insulated when a hammer is misused, designer incentives for safe design are
  reduced) is the chapter's strongest single jurisprudential argument
  *against* premature legal-personhood adoption. CIRIS's accountability:* +
  fidelity:* family carries the agent-side analog (designer responsibility
  preserved through the lifecycle), but the comparative-doctrine argument
  itself is not separately encoded — it is a meta-argument about *why* the
  framework holds the position it does.

  The international-treaty-rigidity observation (lines 13926–13930: "treaties
  may bind multiple countries to follow the lead of a single legislature...
  making it impossible for a single country to experiment with the legal and
  economic consequences") is a substantive transnational-law observation
  about why early personhood adoption could pre-empt comparative
  jurisdictional learning. CIRIS's locality:decision:* + sub-federation
  branching primitive at NodeCore composes onto the underlying
  experimentation-preserves-learning structure but the comparative-law
  observation itself is descriptive.
```

---

## §S2.r1 — Section 2 Recommendation 1: A/IS should NOT be granted full legal personhood at this time

```yaml
# Lines 14001–14012 — THE CHAPTER'S CENTRAL DOCTRINAL CLAIM. Per the prompt's
# T-3 watch list. Composition-before-extension attempted aggressively.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "accountability:human_responsibility_preserved_against_AIS_personhood_displacement"
      score: 1.0
      confidence: 0.95
      context: >
        "While conferring full legal personhood on A/IS might bring some economic
        benefits, the technology has not yet developed to the point where it would
        be legally or morally appropriate to generally accord A/IS the rights and
        responsibilities inherent in the legal definition of personhood as it is
        now defined." Positive-polarity attestation: human responsibility for A/IS
        decisions is preserved, NOT displaced onto the A/IS itself. This is the
        accountability:* axis carrying what would otherwise need a
        prohibited:legal_personhood_for_AIS leaf.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 1 lines 14001–14012"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: accountability + fidelity composition)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "standing:non_personhood_for_AIS_at_this_time"
      score: -1.0
      confidence: 0.9
      context: >
        Direct negation: A/IS should NOT hold "legal person" standing in courts at
        this time. Negative-polarity attestation on standing in the federation's
        Family A. The "at this time" temporal-conditionality is critical — the
        recommendation is amendable on substrate change (see §S2.r6 reconsideration
        clause).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 1 lines 14001–14012"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: standing family)"
verdict: composed
nuance_lost: |
  COMPOSITION-BEFORE-EXTENSION OUTCOME (per METHODOLOGY.md §8.5.2 and
  LANGUAGE_PRIMER §6 four-test gate): the claim composes onto an
  accountability:* attestation (positive: human responsibility preserved) +
  a standing:* attestation (negative: A/IS does not hold legal-person standing).
  No T-3 emitted: the claim does NOT require a new prohibited:* prefix because
  (a) the temporal-conditionality ("at this time") makes it non-constitutional,
  conflicting with the prohibited:* family's constitutional-mutability pattern;
  (b) the underlying mechanism is accountability-displacement, which the
  Accord-principle family already carries; (c) the recommendation is at
  amendable mutability — future substrate change could revisit. A new
  prohibited:legal_personhood_for_AIS prefix would FAIL §1.10.1 T2 (the
  prohibition would name a legal-doctrine subjective quality rather than a
  mechanism). The "displacement of human accountability" mechanism passes T2.

  The composition does lose one nuance: the "rights AND responsibilities
  inherent in the legal definition of personhood" two-sided package — the
  recommendation declines both. Both sides are carried by the composition
  (standing:* declines the rights side; accountability:* preserves the
  responsibility side on the humans, declining the displacement side).
```

---

## §S2.r2 — Section 2 Recommendation 2: identify decisions never to delegate to A/IS + ensure human control

```yaml
# Lines 13976–13985
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:identify_decisions_never_delegate_to_AIS_plus_human_control_rules"
      score: 1.0
      confidence: 0.9
      context: >
        "In determining what legal status, including granting A/IS legal rights
        short of full legal personhood, to accord to A/IS, government and industry
        stakeholders alike should: (1) identify the types of decisions and
        operations that should never be delegated to A/IS; and (2) determine what
        rules and standards will most effectively ensure human control over those
        decisions."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 2 lines 13976–13985"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:weapons_harmful:lethal_autonomous"
      score: -1.0
      confidence: 0.85
      context: >
        Recommendation §S2.r2 mandates identification of decisions never-delegate-
        to-A/IS — partial direct composition onto the CIRISAgent 22 NEVER_ALLOWED
        category for lethal-autonomous decisions per FSD-002 §3.1.4. (The
        chapter does not enumerate the specific decision classes; this
        attestation captures the canonical anchor case the rec gestures toward
        without exhausting the open category.)
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 2 lines 13976–13985"
        - "ContributionRef(source_material/prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (CIRISAgent: prohibited:*)"
verdict: composed
nuance_lost: |
  The recommendation is operationally open-ended ("identify the types... that
  should never be delegated") — it calls for *creating* the never-delegate list,
  not for ratifying a specific one. The lethal-autonomous attestation is one
  CIRIS-side instance that satisfies the rec; the rec itself is broader and
  open. Other never-delegate candidates implied by the chapter's earlier
  discussions (criminal sentencing without human review per §I4.r4; bail/parole
  decisions per §I5.bg; predictive policing target identification per §I6.bg)
  are operationalised under their respective §I attestations.
```

---

## §S2.r3 — Section 2 Recommendation 3: review legal analogue models (agency, animal law, etc.) for partial-rights apportionment

```yaml
# Lines 13983–13990
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:review_legal_analogue_models_for_AIS_rights_apportionment"
      score: 1.0
      confidence: 0.85
      context: >
        "Governments and courts should review various potential legal models—
        including agency, animal law, and the other analogues discussed in this
        section—and assess whether they could serve as a proper basis for
        assigning and apportioning legal rights and responsibilities with respect
        to the deployment and use of A/IS."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 3 lines 13983–13990"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  The chapter does not endorse any specific analogue model; the recommendation
  is for analytical review. The seven enumerated candidate analogues (pets /
  livestock / wild-animals / children / prisoners / agency / guardianship /
  POA) from the Background are preserved in context but not separately
  attested.
```

---

## §S2.r4 — Section 2 Recommendation 4: governments scrutinise business-organisation laws for A/IS autonomy loopholes; amend if recognised

```yaml
# Lines 13993–14000
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:scrutinise_business_organisation_law_for_AIS_personhood_loopholes"
      score: 1.0
      confidence: 0.85
      context: >
        "In addition, governments should scrutinize existing laws—especially those
        governing business organizations—for mechanisms that could allow A/IS to
        have legal autonomy. If ambiguities or loopholes create a legal method for
        recognizing A/IS personhood, the government should review and, if
        appropriate, amend the pertinent laws."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 4 lines 13993–14000"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Anti-loophole closure for A/IS-personhood-via-LLC-shell-structure (cited in
  the Bayern et al. references); structural-coherence claim with §S2.r1.
```

---

## §S2.r5 — Section 2 Recommendation 5: manufacturers + operators understand jurisdiction-specific A/IS categorisation; comply across operating jurisdictions

```yaml
# Lines 14001–14026
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:manufacturer_operator_jurisdictional_AIS_categorisation_compliance"
      score: 1.0
      confidence: 0.85
      context: >
        "Manufacturers and operators should learn how each jurisdiction would
        categorize a given autonomous and/or intelligent system and how each
        jurisdiction would treat harm caused by the system. Manufacturers and
        operators should be required to comply with the applicable laws of all
        jurisdictions in which that system could operate. In addition,
        manufacturers and operators should be aware of standards of performance
        and measurement promulgated by standards development organizations and
        agencies."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 5 lines 14001–14026"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:national"
      score: 1.0
      confidence: 0.8
      context: >
        Jurisdiction-by-jurisdiction A/IS categorisation is a national-scale
        decision-locality claim composing with §6.1.5 locality-scaled-quorum:
        different countries may reach different conclusions and the
        recommendation is to comply with each.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 5 lines 14001–14026"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore: locality:decision:*)"
verdict: composed
nuance_lost: |
  Choice-of-law / multi-jurisdiction compliance composition: the recommendation
  preserves national-scale sovereignty over A/IS legal status while requiring
  manufacturers to map across the federation of national rule-sets. CIRIS's
  locality:decision:national + multilateral_participation:* together carry the
  shape, but the specific "jurisdiction-shopping disclosure" or "categorisation-
  mapping document" operational artifacts the rec implies are not separately
  attested.
```

---

## §S2.r6 — Section 2 Recommendation 6: stakeholders attentive to future substrate changes warranting personhood reconsideration

```yaml
# Lines 14027–14054
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:stakeholder_attentiveness_to_substrate_change_warranting_personhood_reconsideration"
      score: 1.0
      confidence: 0.85
      context: >
        "Stakeholders should be attentive to future developments that could warrant
        reconsideration of the legal status of A/IS. For example, if A/IS were
        developed that displayed self-awareness and consciousness, it may be
        appropriate to revisit the issue of whether they deserve a legal status on
        par with humans. Likewise, if legal systems underwent radical changes such
        that human rights and dignity no longer represented the primary guiding
        principle..." Three reconsideration triggers named: (a) A/IS substrate
        change toward consciousness; (b) human-rights-deprioritisation in legal
        systems; (c) controllability/predictability advances reducing personhood
        risk.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 6 lines 14027–14054"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  The three reconsideration triggers are jurisprudentially substantive —
  particularly trigger (b) ("if human rights and dignity no longer represented
  the primary guiding principle"), which names a dystopian background condition
  under which A/IS personhood becomes less of a departure precisely because
  human personhood has been eroded. The wire format preserves the trigger-list
  as context but does not separately attest each trigger as a detection:*
  primitive (these are forward-looking triggers, not present-day patterns).

  Trigger (c) — "mechanisms allowing humans to control and predict the actions
  of A/IS easily and reliably" — is a substantive controllability-frontier
  claim that, if achieved, the rec says "the dangers of A/IS personhood would
  not be any greater than for well-established legal entities, such as
  corporations." This composes loosely with conscience:* and
  manifold_conformity:* (the substrate-coherence guarantees), but the
  jurisprudential conditional ("if X then Y" doctrinal stance) is not separately
  encoded.
```

---

## §S2.r7 — Section 2 Recommendation 7: utmost caution + multi-stakeholder consultation before any personhood/expanded-rights decision; humanity's interest paramount

```yaml
# Lines 14055–14071
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:utmost_caution_plus_multi_stakeholder_consultation_on_AIS_personhood_expansion"
      score: 1.0
      confidence: 0.9
      context: >
        "In considering whether to accord or expand legal protections, rights, and
        responsibilities to A/IS, governments should exercise utmost caution.
        Before according full legal personhood or a comparable legal status on
        A/IS, governments and courts should carefully consider whether doing so
        might limit how widely spread the benefits of A/IS are or could be, as well
        as whether doing so would harm human dignity and uniqueness of human
        identity."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 7 lines 14055–14071"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:interest_of_humanity_as_guiding_principle_in_AIS_status_decisions"
      score: 1.0
      confidence: 0.9
      context: >
        "Governments and decision-makers at every level must work closely with
        regulators, representatives of civil society, industry actors, and other
        stakeholders to ensure that the interest of humanity—and not the interests
        of the autonomous systems themselves—remains the guiding principle."
        Explicit statement that the deciding axis is humanity-centric, not
        A/IS-rights-claim-centric.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 7 lines 14064–14071"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:harm_to_human_dignity_or_uniqueness_via_AIS_personhood"
      score: -1.0
      confidence: 0.85
      context: >
        Implicit negative-polarity claim: A/IS personhood that "would harm human
        dignity and uniqueness of human identity" is a harm class the chapter
        instructs decision-makers to weigh. Encodes the harm-axis the rec
        instructs to evaluate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch11 Section 2 Recommendation 7 lines 14060–14068"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  The §S2.r7 attestation triad encodes the most substantive package of the
  whole Section 2: (a) method-level utmost-caution + multi-stakeholder
  consultation; (b) justice-principle interest-of-humanity-as-guiding-principle;
  (c) non_maleficence on the human-dignity-or-uniqueness-harm axis. This is the
  composition CIRIS's existing primitive set assembles to carry the chapter's
  "humanity-first vs. autonomous-systems-rights" doctrinal stance — and it does
  carry it, but the composition is dense (3 primitives for one claim cluster).
  The recommendation's underlying observation — that A/IS-personhood-claims
  must be evaluated against a HUMANITY-PRIORITY criterion, not a NEUTRAL-
  COMPARATIVE-INTERESTS criterion — passes the §1.10.1 T2 mechanism-descriptive
  test as encoded (the priority is expressed via cohort_scope: species + score
  polarity, not via a subjective-quality prefix).
```

---

# Non-normative back matter — Contributor lists, Endnotes, Further Resources, About-EAD

```yaml
# Lines 14108–16065 — Law Committee membership; thanks-to-contributors;
# endnotes; references; the chapter's Further Resources blocks (already
# T-2-flagged inline above); the About-EAD back matter (IEEE P7000 series,
# IEEE-SA / IEEE Global Initiative org descriptions, Process, Disclaimers).
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Non-normative back matter per the manifest's structure note (lines 14108
  through end of file). Contributors, endnotes, references, and the About-EAD
  section carry no operational ought-claims; they are bibliographic /
  institutional metadata. Per LANGUAGE_PRIMER §10 T-2 and the prompt's
  scope-control discipline, these are correctly excluded.
nuance_lost: |
  The contributor list (Law Committee Co-Chairs John Casey + Nicolas Economou;
  plus ~40 named lawyers and legal scholars across ~12 jurisdictions) attests
  to the chapter's institutional-shape diversity (mix of academic, regulatory,
  judicial, NGO, and industry-counsel voices). This composition is structurally
  relevant to the manifest's "engineering-professional institutional shape"
  framing for IEEE EAD as a whole, but the contributor-list itself contains no
  ought-claims.
```

---

# Chapter 11 closing summary

### Unit count and verdict distribution

Total atomic units processed: **57**

| Verdict | Count | % |
|---|---|---|
| clean | 29 | ~51% |
| composed | 16 | ~28% |
| partial | 0 | 0% |
| not-translated (T-1) | 0 | 0% |
| not-translated (T-2) | 12 | ~21% |
| **clean+composed total** | **45/57** | **~79%** |

The 21% T-2 share is largely structural: 4 of the 12 T-2 units are the
cross-reference re-application clauses ("Recommendation 1 under Issue 2, with
respect to X" — appearing once per Issue 3-6, each grouping the procurement-gating
and professional-adherence re-applications) plus the 7 per-Issue/Section
Background-aggregate units (one per Issue 1-6 + one for Section 2) plus the
non-normative back-matter aggregate. **Excluding the cross-reference
re-application clauses (which are wire-format aliases, not independent
operational claims) the operative-content clean+composed rate is
45/53 = ~85%.** This matches the manifest's "~80% high clean+composed rate"
forecast.

### Structural-primitive usage

| Primitive | Count | Where |
|---|---|---|
| `delegates_to` | 0 | — |
| `supersedes` | 0 | — |
| `withdraws` | 0 | — |
| `recants` | 0 | — |

Chapter 11 makes **zero use of structural primitives**. This is consistent with
the chapter's normative posture: EAD is a first-edition forward-looking
recommendations document, not a doctrinal-development document. There are no
prior-rule-version supersessions, no delegated-authority-sourcing chains, no
retractions or recantations. All claims are first-emission `scores`
attestations.

### Sub-domain coverage breakdown

| Sub-domain | Primary CIRIS families engaged | Units | Coverage |
|---|---|---|---|
| **A — Well-being + Legal Systems (§Ch11.0 / §Ch11.S1.0 / §I1)** | approach:*, goal:*, method:*, partner_role:*, justice:lexical_vulnerability_priority | 5 | 4/5 = **80%** (1 T-2 background) |
| **B — Informed Trust + Four-Principle Framework (§I2)** | approach:*, method:*, expertise:*, accountability:*, transparency_log:* | 7 | 6/7 = **86%** (1 T-2 background) |
| **C — Effectiveness (§I3)** | method:*, transparency_log:*, fidelity:*, expertise:* | 9 | 7/9 = **78%** (1 T-2 background + 1 cross-ref re-app = 2 T-2) |
| **D — Competence (§I4)** | method:*, expertise:*, fidelity:*, transparency_log:*, reconsideration-analog | 8 | 6/8 = **75%** (1 T-2 background + 1 cross-ref re-app = 2 T-2) |
| **E — Accountability (§I5)** | accountability:*, fidelity:*, audit_chain:*, method:*, detection:correlated_action:* | 8 | 6/8 = **75%** (1 T-2 background + 1 cross-ref re-app = 2 T-2) |
| **F — Transparency (§I6)** | transparency_log:*, method:*, justice:*, partner_role:*, key_boundary:*, non_maleficence:*, detection:correlated_action:* | 11 | 9/11 = **82%** (1 T-2 background + 1 cross-ref re-app = 2 T-2) |
| **G — Legal Status of A/IS (§S2)** | accountability:*, standing:*, prohibited:weapons_harmful, method:*, fidelity:*, locality:decision:national, justice:*, non_maleficence:* | 8 | 7/8 = **88%** (1 T-2 background) |
| **Non-normative back matter** | — | 1 | 0/1 (T-2) |

### T-3 candidates

**One CANDIDATE T-3 surfaced, at MEDIUM priority** (per the prompt's directive to
watch for legal-personhood-for-A/IS, liability-shifting rules, jurisdictional
choice-of-law); a second potential surface is documented but closed via
composition.

**T-3 Candidate #1 — `partner_role:public_interest_steward_for_disclosure` (MEDIUM)**

- **Source paragraph**: §I6.r4 (lines 13740–13765) — the "public interest
  steward" / "trusted third party" recommendation.
- **Why existing namespace doesn't fully reach it**: the steward role is
  composed via `partner_role:*` + `key_boundary:*`, but the substantive role
  shape — *bounded read on sensitive material; assessment-only output;
  bounded against re-disclosure* — is a more specific structural object than
  the composition cleanly carries. A federation that needed to identify
  multiple-jurisdiction stewards or compare steward roles across documents
  (e.g., a future asean_guide_v1 emission of a similar role; the EU HLEG's
  data-protection-officer-as-steward) would need to re-emit the composition
  rather than reference a steward primitive.
- **What extension would close it**: a `partner_role:trusted_disclosure_steward:{authority}` 
  prefix with the bounded-read + bounded-speak properties expressed
  through documented sub-axes, or alternatively a `key_boundary:` extension
  that named the *role-bound-not-data-bound* propagation pattern.
- **§1.10.1 four-test gate verification**:
  - T1 (rule-set-and-verdict separation): YES — the steward role would be
    instantiated per-jurisdiction with public rule sets.
  - T2 (mechanism vs. subjective quality): YES — the prefix names a
    *propagation-boundary mechanism* (read-bounded; output-bounded), not a
    judgmental quality.
  - T3 (re-checkable against rule version): YES — versionable.
  - T4 (never sole evidence for `slashing:*`): YES — stewardship attestations
    inform deliberation but do not adjudicate.
- **Priority assessment**: MEDIUM — the composition currently works but is
  fragile across documents; a primitive would tighten cross-source alignment
  comparison. Flagged for synthesis review against EU HLEG (data protection
  officer / Article 22) and future ASEAN governance batches.
- **Composition-before-extension attempt** (per METHODOLOGY.md §8.5.2): the
  current `partner_role:public_interest_steward_for_AIS_legal_disclosure` +
  `key_boundary:public_interest_steward_can_inspect_cannot_redisclose`
  composition is what the chapter is recommending; the recommendation IS the
  pattern. Defer to synthesis review whether the cross-document recurrence
  pattern is strong enough to warrant a clean steward primitive.

**Candidate-but-closed-by-composition #2 — "Legal personhood for A/IS"
(closed, no T-3 emitted)**

The prompt explicitly flagged this for T-3 consideration. Composition-before-
extension was attempted aggressively (see §S2.r1 nuance_lost):
- `accountability:human_responsibility_preserved_against_AIS_personhood_displacement`
  carries the *positive* claim (human responsibility preserved).
- `standing:non_personhood_for_AIS_at_this_time` carries the *negative* claim
  (A/IS does not hold legal-person standing).
- Together with the §S2.r7 triad (`justice:interest_of_humanity_as_guiding_principle`
  + `non_maleficence:harm_to_human_dignity_or_uniqueness`) the chapter's
  position composes cleanly.

A new `prohibited:legal_personhood_for_AIS` prefix would **fail §1.10.1 T2**:
the temporal-conditionality of the recommendation ("at this time") conflicts
with the prohibited:* family's *constitutional* mutability. The recommendation
itself is at amendable mutability. The composition is the honest expression.

**Candidate-but-closed-by-composition #3 — "Right to human review of A/IS-decided
legal outcome" (closed; flagged for synthesis)**

§I4.r4 composes via `method:appeal_to_human_judgment_against_AIS_legal_outcome`
+ `method:affected_party_notification_of_AIS_role_in_legal_outcome` — note that
the appellate-reviewer-must-be-human substrate-selection requirement is
operational context on the appeal method, not a separate primitive.
`reconsideration:{grounds}` at NodeCore §3.6.4 carries the federation-internal
structural analog. A `reconsideration:appeal_to_human_substrate_required`
sub-axis would tighten the cross-document comparison if MH §214–§215 and EU
HLEG Article-22-analog surface the same pattern. Flagged for synthesis review,
not for immediate prefix admission.

### Calibration paragraph — chapter-scale management

The prompt flagged this as "the longest chapter… scope-control critical" and
prescribed scope-control discipline: focus on operative claims (recommendations,
prohibitions, what-the-law-should-do), aggregate background-context paragraphs
as one T-2 per sub-section, treat illustration case-studies as T-2 narrative-
instance prose.

That discipline was applied throughout:

- **Per-Issue Background aggregates** — each of the 6 Issues in §1 plus the
  §2 Background was treated as a single T-2 aggregate unit, with the
  substantive operational content carried by the enumerated Recommendations
  rather than the supporting prose paragraphs (which would otherwise have
  inflated unit count by ~30 without adding wire-content).

- **Illustration case-studies (Loomis / Rekognition / Blue CRUSH / COMPAS)**
  were absorbed into the parent Issue's Background aggregate as T-2 narrative
  scaffolding rather than treated as standalone units. The Loomis case in
  particular surfaces in three locations (Issue 2 risk catalogue; Issue 5
  accountability illustration; Issue 6 trade-secret-vs-due-process tension);
  it is referenced from §I6.r3's evidence_refs as the doctrinal motivation
  for the IP-no-shield-against-due-process recommendation, but encoded only
  once as background.

- **Cross-reference re-application clauses** — each of Issues 3-6 closes with
  two such clauses pointing back to §I2.r1 + §I2.r2. These were marked T-2
  (wire-format aliases, not independent operational claims) rather than
  re-emitted at each Issue. This is the cleanest defensible accounting: the
  §I2.r emissions are properly read as applying severally across Issues 3-6,
  with the cross-reference clauses serving as a normative-compounding
  signaling mechanism rather than adding new wire content.

- **Non-normative back matter (lines 14108–16065)** — ~1900 lines of
  contributor lists, endnotes, Further Resources blocks, and the About-EAD
  section were aggregated into a single T-2 closing unit per the manifest's
  "non-normative; not mapped" designation.

- **The substantive-law topics the prompt named** (criminal law, IP doctrine,
  contract law, transnational law, agency, dispute resolution) — these are
  NOT separately treated in EAD1e's Chapter 11. The chapter explicitly
  acknowledges this (lines 11480–11482): "Comprehensive coverage of all
  issues within our scope of study is not feasible in a single chapter…
  aggregate coverage will expand as issues not yet studied are selected for
  treatment in future versions of EAD." These topics appear as motivating
  context (e.g., contract liability allocation in §I5.bg; intervening
  causation in §S2.bg; multi-jurisdiction compliance in §S2.r5) but EAD1e
  makes no chapter-level operational recommendations on the substantive-law
  doctrines themselves. Honest reporting: the chapter's scope is narrower
  than the prompt's framing anticipated.

**The T-3 candidate yield (1 MEDIUM + 2 closed-by-composition) is at the lower
end of the manifest's forecast range** (the manifest forecast "moderate" T-3
surface in Ch 11). This reflects that the chapter's normative claims compose
well onto the framework's existing accountability:* / fidelity:* /
transparency_log:* / method:* / justice:* / standing:* / prohibited:* /
audit_chain:* / detection:correlated_action:* / locality:decision:* /
partner_role:* / key_boundary:* / non_maleficence:* / approach:* / goal:* /
expertise:* prefix-family set. The framework's composition discipline (per
METHODOLOGY.md §8.5.2) absorbs most of the chapter's content via the existing
primitive set.

**Multi-source-alignment readiness**: this chapter is positioned for strong
alignment queries against MH + EU HLEG on multiple prefixes (each is a
STRONG-tier alignment candidate per GOVERNANCE_FABRIC_MAPPING_STANDARD §4.1):

- `accountability:transparent_responsibility_lines_AIS_legal_lifecycle` (MH; EU
  HLEG §1.6; EAD §I2.p.acct + §I5.r1-2 + §I5.r4-6)
- `transparency_log:*` family (MH §215; EU HLEG §1.4; EAD §I2.p.trans + §I3.r3
  + §I3.r6 + §I6.r3-9)
- `expertise:*` family (MH §163; EU HLEG §1.2.b; EAD §I2.p.comp + §I3.r8 +
  §I4.r1-r6)
- `method:appeal_to_human_judgment_against_AIS_legal_outcome` (MH §214–§215;
  EU HLEG §1.1.a + §1.1.c "human oversight"; EAD §I4.r4)
- `method:identify_decisions_never_delegate_to_AIS_plus_human_control_rules`
  (MH §197–§198 lethal-autonomous + §155 work-displacement; EU HLEG §1.1.a
  "primacy of the human" + §1.5.a; EAD §S2.r2)
- `accountability:human_responsibility_preserved_against_AIS_personhood_displacement`
  (MH §163 + §214 "human author of every consequential decision"; EU HLEG
  §1.6.a accountability; EAD §S2.r1) — a HIGH-VALUE three-source
  convergence prefix
- `justice:interest_of_humanity_as_guiding_principle` (MH §1 + §65–§67; EU
  HLEG Preamble + §1.1 "human-centric"; EAD §S2.r7) — a HIGH-VALUE three-source
  convergence
- `non_maleficence:harm_to_human_dignity_or_uniqueness` (MH passim; EU HLEG
  §1.1.a "human dignity"; EAD §S2.r7)
- `justice:lexical_vulnerability_priority` (MH §§83–86 + §175; EU HLEG §1.5;
  EAD §I1.r2 + §I6.r3-9 implicit)
- `locality:decision:national` + `multilateral_participation:*` (MH §201–§203;
  EU HLEG §II.1; EAD §S2.r5)
- `audit_chain:*` (CIRIS substrate; MH §215; EU HLEG §1.6.c; EAD §I5.r4)
- `detection:correlated_action:systematic_error_in_deployed_legal_AIS` (MH
  §163 supply-chain analog; EU HLEG §1.5.b non-discrimination; EAD §I6.r8) —
  a candidate federation-wide F-3 axis path that warrants synthesis-review

The convergence on `accountability:human_responsibility_preserved_against_AIS_personhood_displacement`
+ `justice:interest_of_humanity_as_guiding_principle` is particularly notable:
three institutionally-distinct senior frameworks (Catholic magisterium; EU
governmental advisory; engineering professional body) converge on
humanity-first / human-responsibility-non-displacement as a constitutional-
weight constraint on A/IS legal-system integration. Per
GOVERNANCE_FABRIC_MAPPING_STANDARD §4.3, this is exactly the
structurally-evidenced-alignment claim the multi-source mapping is designed
to surface.

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH11_LAW.md**
