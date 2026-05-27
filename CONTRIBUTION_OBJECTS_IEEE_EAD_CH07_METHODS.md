# CONTRIBUTION_OBJECTS_IEEE_EAD_CH07_METHODS.md
# IEEE Ethically Aligned Design First Edition (2019) — Chapter "Methods to Guide Ethical Research and Design"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 6605–7471)
# Chapter pages: 124–139 (3 sections: Interdisciplinary Education/Research; Corporate Practices; Responsibility/Assessment)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

This chapter is the **methodology core** of EAD1e — the operative recommendations for *how*
A/IS research and design should be conducted ethically (as distinct from *what* the General
Principles are in Ch 2). The chapter is composed of recommendations clustered under three
sections: (1) Interdisciplinary Education and Research; (2) Corporate Practices on A/IS;
(3) Responsibility and Assessment.

The natural mapping target is the Family B Action hierarchy: `method:*` proposals
(operational practices instantiating ethics-into-design goals), `goal:species` /
`goal:community` framings, and `partner_role:*` proposals (review boards, certification
bodies, CVO roles). Composition with `expertise:*` and `witness_diversity:*` is heavy.

A T-3 surface to watch is whether **specific named methodologies** (Value-Sensitive Design,
intercultural information ethics, participatory design with stakeholders, ethics-filter
gating, red-flag protocols, algorithmic impact assessment) compose adequately onto
`method:*` + `witness_diversity:*` + `testimonial_witness:*` + `expertise:*`, or whether a
methodology-naming primitive is owed. Pre-translation expectation: composition holds for
most; a small number of named methodologies push toward T-3.

Source quotes are bounded at ≤ 2 sentences per LANGUAGE_PRIMER discipline.

---

## §Ch7.0 — Chapter preamble: A/IS research and design must be underpinned by ethical norms via values-based methods

```yaml
# Lines 6609–6638 — Chapter opening; "technology is not neutral"; A/IS embody values and biases
# influencing voting, policing, banking; research & design must be underpinned by ethical and
# legal norms instantiated through values-based methods putting human well-being at the core
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:species"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS research and design must be underpinned by ethical and legal norms. These
        should be instantiated through values-based research and design methods. Such
        methods put human well-being at the core of A/IS development." Goal-level claim
        at species scope; values-based methods are the means.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Ch7 preamble lines 6609–6614"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:values_based_research_and_design"
      score: 1.0
      confidence: 0.85
      context: >
        "Researchers, product developers, and technologists across all sectors need to
        embrace research and development methods that evaluate their processes, products,
        values, and design practices." Approach-level pathway toward the species goal.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Ch7 preamble lines 6616–6619"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: composed
nuance_lost: |
  "Technology is not neutral" is a strong philosophical premise that the wire format carries
  only as evidence-context; no positive primitive encodes the substantive claim that
  artifacts have politics. The "voting, policing, banking" enumeration of socially-load-
  bearing domains drops out as illustrative rather than scope-defining.
```

---

## §Ch7.0a — Chapter structural note: three sections + structural/individual approaches

```yaml
# Lines 6619–6637 — Chapter is split into three sections (Education/Research; Corporate
# Practices; Responsibility/Assessment) addressing both structural and individual approaches
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Pure table-of-contents structural framing. The substantive claims of each section are
  carried by their respective Issue subsections below; the framing itself is rhetorical
  per LANGUAGE_PRIMER §8 Step 1(b).
nuance_lost: |
  The "structural AND individual" duality is a methodological commitment that maps onto
  CIRIS's own dual-layer architecture (Accord-layer principles + per-agent conscience),
  but is not separately encoded — the per-Issue attestations below each carry one side
  or the other.
```

---

# Section 1 — Interdisciplinary Education and Research

> *"Integrating applied ethics into education and research to address the issues of A/IS requires an interdisciplinary approach, bringing together humanities, social sciences, physical sciences, engineering, and other disciplines."*

---

## §S1.0 — Section preamble: ethics-integration into A/IS education requires interdisciplinarity

```yaml
# Lines 6653–6659 — Section 1 opening; interdisciplinary approach across humanities/social
# sciences/physical sciences/engineering required for ethics-integration into A/IS education
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:interdisciplinary_ethics_integration"
      score: 1.0
      confidence: 0.85
      context: >
        "Integrating applied ethics into education and research to address the issues of
        A/IS requires an interdisciplinary approach, bringing together humanities, social
        sciences, physical sciences, engineering, and other disciplines." Strategic
        pathway claim — interdisciplinarity is the route to ethics-integration.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 lines 6653–6659"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: clean
nuance_lost: |
  "Other disciplines" is an open class that the strict prefix scoping cannot enumerate;
  the disciplinary list (humanities/social sciences/physical sciences/engineering) is
  preserved as evidence-context but not as a structured field.
```

---

## §S1.I1.bg — Issue 1 Background: STEM ethics under-integration; ethics rendered invisible by technical practice

```yaml
# Lines 6662–6692 — A/IS engineers don't always explore ethical considerations; STEM
# struggles with ethics that can't be translated to formal mathematics/programming;
# ethical issues rendered invisible or inappropriately reduced
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:ethical_perspectives_in_stem"
      score: 0.6
      confidence: 0.6
      context: >
        "Ethical issues can easily be rendered invisible or inappropriately reduced and
        simplified in the context of technical practice." Pattern-claim: STEM-curricular
        and STEM-practice norms produce systematic exclusion of ethical-reasoning
        perspectives from A/IS design — a participation-exclusion axis variant.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 1 Background lines 6681–6685"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:*)"
verdict: partial
residual:
  description: |
    The background claim composes operational pattern (curricular under-integration of
    ethics) with an epistemic-shape claim ("ethical considerations cannot be readily
    articulated and translated into the formal languages of mathematics and computer
    programming"). The second half is a methodological-impossibility claim — that
    certain ethical content is not expressible in formal languages — which is exactly
    the T-2 / T-3 distinction LANGUAGE_PRIMER §10 names but at a meta-level. No wire
    primitive captures "this kind of content resists formalization"; the wire format
    itself is the formalization, so the residual is structural-self-aware.
  classification: T-2
nuance_lost: |
  The Lipton & Steinhardt citation (line 6684–6686) carries scholarly authority via
  hearsay-citation pattern but the wire format does not separately encode authority-
  weighting of cited literature versus the IEEE committee's own assertion.
```

---

## §S1.I1.aim — Issue 1 Aim: prepare students so ethics becomes a natural part of design

```yaml
# Lines 6662–6668 — "Aim of these recommendations is to prepare students for the technical
# training and engineering development methods that incorporate ethics as essential so that
# ethics, and relevant principles, like human rights, become naturally a part of the design
# process"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "goal:community"
      score: 1.0
      confidence: 0.85
      context: >
        "Prepare students for the technical training and engineering development methods
        that incorporate ethics as essential so that ethics, and relevant principles,
        like human rights, become naturally a part of the design process." Goal at
        community scope — the engineering community as the affected scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 1 lines 6662–6668"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: goal:{scale})"
verdict: clean
nuance_lost: |
  "Naturally a part of the design process" carries a dispositional claim — ethics
  internalized as habit rather than externally enforced — that the score-magnitude
  pair only approximately encodes. The Aristotelian / virtue-ethics resonance of
  "naturally" is not preserved in the prefix.
```

---

## §S1.I1.r — Issue 1 Recommendations: STEM ethics as core subject from earliest level, with non-STEM informants, spanning all schools

```yaml
# Lines 6671–6712 — Four bullets: (1) Ethics training core for STEM at earliest appropriate
# level + all advanced degrees; (2) STEM ethics curricula informed by non-STEM experts from
# diverse cultural/educational backgrounds; (3) Curricula teach engineers/CS/statisticians
# about impact of decisions; ethics education spans primary/secondary/postsecondary, both
# universities and vocational; (4) Accreditation bodies should reinforce
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:stem_ethics_curriculum_core_subject"
      score: 1.0
      confidence: 0.85
      context: >
        "Ethics training needs to be a core subject for all those in the STEM field,
        beginning at the earliest appropriate level and for all advanced degrees."
        Concrete operational method — curricular embedding at all levels.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 1 Recommendation 1 lines 6671–6674"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:stem_ethics_curriculum_informants"
      score: 1.0
      confidence: 0.85
      context: >
        "Effective STEM ethics curricula should be informed by experts outside the STEM
        community from a variety of cultural and educational backgrounds to ensure that
        students acquire sensitivity to a diversity of robust perspectives on ethics and
        design." Direct witness-diversity claim — N=multiple-jurisdictional-and-
        organizational diversity bar over curricular-input attesters.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 1 Recommendation 2 lines 6676–6683"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:accreditation_body"
      score: 1.0
      confidence: 0.85
      context: >
        "Relevant accreditation bodies should reinforce this integrated approach as
        outlined above." Partner-role claim — accreditation bodies as the enforcement
        partner for STEM-ethics curricular integration.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 1 Recommendation 4 lines 6711–6712"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
verdict: composed
nuance_lost: |
  "Earliest appropriate level" defers the threshold to deployment context — primary
  school for some content; postgraduate for others — but the wire prefix is scale-flat
  at affiliations. The vocational-vs-university span gets compressed into one prefix
  without preserving the equality-of-status claim between the two paths.
```

---

## §S1.I1.fr — Issue 1 Further Resources: IEEE P7000; Lipton/Steinhardt; Holdren/Smith; Cath et al.

```yaml
# Lines 6716–6748 — Resource citations: IEEE P7000 Standards Project; Lipton & Steinhardt
# 2018 (ICML); Holdren & Smith 2016 (NSTC); Cath et al. 2017 (Science and Engineering Ethics)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further-resources sections are bibliographic anchors carrying scholarly authority via
  citation, not independent operational claims. Per LANGUAGE_PRIMER §8 Step 1(b) these
  are framing/reference content; the operational claims they support are carried by the
  Recommendation attestations above, where they sit in evidence_refs.
nuance_lost: |
  IEEE P7000 ("Model Process for Addressing Ethical Concerns During System Design") is
  itself a methodology-naming reference that could anchor a method:p7000_model_process
  attestation in a more granular pass. Kept at evidence-anchor level here.
```

---

## §S1.I2.bg — Issue 2 Background: institutional resources needed to bring engineers into contact with ethicists/legal/social scientists

```yaml
# Lines 6711–6748 — More institutional resources needed; lack of diversity limits cross-
# pollination; translation work + resource sharing needed; cross-disciplinary research
# (FAT* conference; CIFAR cited as examples)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:sustained_interdisciplinary_collaboration"
      score: 1.0
      confidence: 0.8
      context: >
        "More institutional resources and incentive structures are necessary to bring
        A/IS engineers and designers into sustained and constructive contact with
        ethicists, legal scholars, and social scientists, both in academia and industry."
        Approach-level pathway claim with named non-engineering disciplines.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 2 Background lines 6713–6722"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:diverse_backgrounds_in_ais_institutions"
      score: 0.6
      confidence: 0.6
      context: >
        "Lack of diversity of backgrounds and perspectives in A/IS-related institutions
        and companies, which limit cross-pollination between disciplines." Pattern-claim
        about systematic exclusion at the institutional-composition level.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 2 Background lines 6724–6727"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:*)"
verdict: composed
nuance_lost: |
  "Cross-pollination between disciplines" is a metaphorical-ecological framing that the
  detection prefix flattens to mechanism. The specific examples (FAT* conference, CIFAR
  Canadian AI strategy) are preserved as evidence-context but not as institutional-
  recognition attestations on those specific entities.
```

---

## §S1.I2.r — Issue 2 Recommendation: funding/incentive structures revised to prioritize interdisciplinary ethics projects

```yaml
# Lines 6763–6769 — "Funding models and institutional incentive structures should be
# reviewed and revised to prioritize projects with interdisciplinary ethics components"
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:funding_incentive_revision_for_interdisciplinary_ethics"
      score: 1.0
      confidence: 0.8
      context: >
        "Funding models and institutional incentive structures should be reviewed and
        revised to prioritize projects with interdisciplinary ethics components to
        encourage integration of ethics into projects at all levels." Concrete method —
        funding-incentive realignment as the operational lever.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 2 Recommendation lines 6763–6769"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  Funding-incentive language carries a political-economy claim — that current funding
  structures actively disincentivize ethics-integration — which the positive-polarity
  prefix mutes. The implicit negative attestation on prior-funding-norms is not
  separately emitted.
```

---

## §S1.I3.bg — Issue 3 Background: A/IS culture and context — cross-cultural variation in ethics

```yaml
# Lines 6766–6779 — "A responsible approach to embedding values into A/IS requires that
# algorithms and systems are created in a way that is sensitive to the variation of
# ethical practices and beliefs across cultures. The designers of A/IS need to be mindful
# of cross-cultural ethical variations while also respecting widely held international
# legal norms."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:cross_cultural_ethical_variation"
      score: 1.0
      confidence: 0.85
      context: >
        "A responsible approach to embedding values into A/IS requires that algorithms
        and systems are created in a way that is sensitive to the variation of ethical
        practices and beliefs across cultures." Fidelity to plural ethical traditions —
        a constraint on the embedding process itself.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 3 Background lines 6766–6772"
        - "ContributionRef(source_material/dma_prompts/pdma_framing.txt §III polyglot anchoring)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: clean
nuance_lost: |
  "Mindful of cross-cultural ethical variations WHILE ALSO respecting widely held
  international legal norms" carries an implicit tension-management claim — that cross-
  cultural sensitivity has a floor in international legal norms. The wire prefix encodes
  the fidelity direction but not the floor-condition; that would need a composed
  attestation on justice:internationally_recognized_human_rights as the floor.
```

---

## §S1.I3.r — Issue 3 Recommendation: leading role for intercultural information ethics (IIE) practitioners

```yaml
# Lines 6781–6790 — "Establish a leading role for intercultural information ethics (IIE)
# practitioners in ethics committees informing technologists, policy makers, and engineers.
# Clearly demonstrate through examples how cultural variation informs not only information
# flows and information systems, but also algorithmic decision-making and value by design."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:intercultural_information_ethics:multi_lingual"
      score: 1.0
      confidence: 0.8
      context: >
        "Establish a leading role for intercultural information ethics (IIE)
        practitioners in ethics committees informing technologists, policy makers, and
        engineers." Expertise-domain claim — IIE as a recognized expertise category
        with weighted standing in ethics-committee composition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 3 Recommendation lines 6781–6785"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore Standing: expertise:{domain}:{language})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:ethics_committee"
      score: 1.0
      confidence: 0.8
      context: >
        Ethics committees as the institutional partner-role that integrates IIE
        expertise into A/IS guidance for technologists, policy makers, and engineers.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 3 Recommendation lines 6781–6785"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
verdict: composed
nuance_lost: |
  "Intercultural information ethics" (IIE) is a named methodology / scholarly tradition
  (Capurro / Bielby lineage cited in Further Resources). Treating it as an
  expertise:{domain} flattens the methodology to a credential, losing the substantive
  philosophical content (information ethics as a distinct subdiscipline grounded in
  hermeneutic engagement across traditions). Documentation-explicitness gap, not T-3 —
  the structural shape is captured.
```

---

## §S1.I3.fr — Issue 3 Further Resources: Pauleen et al.; Bielby (intercultural information ethics)

```yaml
# Lines 6794–6804 — Resource citations: Pauleen et al. 2006 on cultural bias in IS;
# Bielby 2016 on comparative philosophies in intercultural information ethics
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Bibliographic citations supporting the IIE recommendation above; not independent claims.
nuance_lost: |
  The intercultural-information-ethics lineage is genuinely a substantive philosophical
  tradition (engaging Capurro, Floridi, Hongladarom) that would warrant its own bootstrap-
  source mapping in the future deployment list of the standard. Acknowledged here without
  attestation.
```

---

## §S1.I4.bg — Issue 4 Background: research ethics boards inadequately equipped for A/IS

```yaml
# Lines 6821–6864 — IRBs/HCI research governance underdeveloped for A/IS; national /
# international regulations may exclude A/IS from purview on technicalities; PRIM&R /
# SoCRA / IACUC under-resourced for A/IS expertise; insufficient attention to A/IS ethics
# by board members; specific gaps in animal/A/IS interface, biosafety/A/IS interface
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:ais_research_ethics_oversight"
      score: 0.7
      confidence: 0.7
      context: >
        Multiple under-coverage patterns: A/IS research may be excluded from research-
        ethics-board purview on legal technicalities; IRB-trainer bodies (PRIM&R, SoCRA)
        under-resourced for A/IS expertise; animal-A/IS interface research
        underdeveloped for IACUC oversight; radiological/biological/toxicological/A/IS
        intersection rarely found in research-ethics literature.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 4 Background lines 6821–6864"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:*)"
verdict: clean
nuance_lost: |
  The specific institutional anchors (FDA, EMA, PRIM&R, SoCRA, IACUC) are preserved as
  evidence-context but the wire format does not separately tag jurisdictional applicability
  of those institutions (US-specific vs EU-specific vs international). Multi-jurisdiction
  oversight gap remains under-specified at the wire layer.
```

---

## §S1.I4.r — Issue 4 Recommendation: IEEE + standards-setting bodies should develop A/IS research governance standards in partnership with national/international agencies

```yaml
# Lines 6879–6889 — "The IEEE and other standards-setting bodies should draw upon existing
# standards, empirical research, and expertise to identify priorities and develop standards
# for the governance of A/IS research and partner with relevant national agencies, and
# international organizations, when possible."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ais_research_governance_standards_development"
      score: 1.0
      confidence: 0.85
      context: >
        "The IEEE and other standards-setting bodies should draw upon existing standards,
        empirical research, and expertise to identify priorities and develop standards
        for the governance of A/IS research and partner with relevant national agencies,
        and international organizations, when possible." Concrete operational method.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 4 Recommendation lines 6879–6889"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "multilateral_participation:standards_bodies:partnership"
      score: 1.0
      confidence: 0.8
      context: >
        Standards-setting bodies should "partner with relevant national agencies, and
        international organizations" — explicit multilateral-participation framing for
        A/IS research governance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S1 Issue 4 Recommendation lines 6886–6889"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation:*)"
verdict: composed
nuance_lost: |
  "When possible" is a softener that the score-magnitude pair imperfectly carries; the
  recommendation is aspirational rather than mandatory. The IEEE self-positioning as
  a standards-developing party is preserved as the attesting context but does not appear
  as a self-attestation on IEEE's identity.
```

---

# Section 2 — Corporate Practices on A/IS

> *"Corporations are eager to develop, deploy, and monetize A/IS, but there are insufficient structures in place for creating and supporting ethical systems and practices around A/IS funding, development, and use."*

---

## §S2.0 — Section preamble: corporate eagerness outstrips ethical structure

```yaml
# Lines 6915–6921 — Section opening; corporate eagerness for A/IS deployment outstrips
# ethical structures around funding/development/use; ethics review board well-timed in
# A/IS creation can mitigate problematic designs
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:corporate_ais_ethics_under_structuring"
      score: 0.65
      confidence: 0.7
      context: >
        "Corporations are eager to develop, deploy, and monetize A/IS, but there are
        insufficient structures in place for creating and supporting ethical systems and
        practices around A/IS funding, development, and use." Pattern-claim: the
        aggregate of corporate A/IS development outstrips the aggregate of ethical
        structure surrounding it.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 preamble lines 6915–6921"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:*)"
verdict: clean
nuance_lost: |
  "Eager to develop, deploy, and monetize" carries an implicit criticism of profit-driven
  velocity that the neutral-polarity detection prefix mutes; the polarity-positive on the
  detector reads as "yes the pattern is present," not "yes this is bad," per the §1.10.1
  T2 mechanism-not-judgment discipline.
```

---

## §S2.I1.bg — Issue 1 Background: values-based ethical culture and practices for industry

```yaml
# Lines 6924–6944 — Corporations built for profit/market-share; need values-based ethical
# culture beyond laws/regulations; identify and refine corporate processes facilitating
# values-based design
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:values_based_corporate_culture"
      score: 1.0
      confidence: 0.8
      context: >
        "Given the deep ethical implications of widespread deployment of A/IS, in
        addition to laws and regulations, there is a need to create values-based
        ethical culture and practices for the development and deployment of those
        systems." Approach-level claim: values-based culture beyond legal compliance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 1 Background lines 6932–6940"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: clean
nuance_lost: |
  "Values-based" is not a single methodology but a family — VSD (Value-Sensitive Design,
  Friedman et al.), Spiekermann's ethical IT innovation, virtue-ethics approaches.
  Flattening to one approach prefix loses the methodology-pluralism implicit in the
  text. See §S2.I6 below for the direct Values-Based Design Issue treatment.
```

---

## §S2.I1.r — Issue 1 Recommendations: top-down + bottom-up; ethics filters; ethics review boards in A/IS creation

```yaml
# Lines 6945–6957 — "The building blocks of such practices include top-down leadership,
# bottom-up empowerment, ownership, and responsibility, along with the need to consider
# system deployment contexts and/or ecosystems. Corporations should identify stages in
# their processes in which ethical considerations, 'ethics filters', are in place before
# products are further developed and deployed."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ethics_filters_at_stage_gates"
      score: 1.0
      confidence: 0.8
      context: >
        "Corporations should identify stages in their processes in which ethical
        considerations, 'ethics filters', are in place before products are further
        developed and deployed." Concrete method — gate-style ethics review at named
        development stages.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 1 Recommendations lines 6950–6954"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:corporate_ethics_review_board"
      score: 1.0
      confidence: 0.8
      context: >
        "If an ethics review board comes in at the right time during the A/IS creation
        process, it would help mitigate the likelihood of creating ethically problematic
        designs." Partner-role attestation on internal corporate ethics review boards.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 1 lines 6915–6919"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
verdict: composed
nuance_lost: |
  "Top-down leadership AND bottom-up empowerment" is a dual-vector claim that no single
  method:* attestation captures; the per-Issue sequence in §S2.I2 (leadership) and §S2.I3
  (empowerment) below carries the two vectors separately, so the composition is
  distributed across the section rather than encoded in one envelope here.
```

---

## §S2.I2.bg — Issue 2 Background: values-based leadership; ethical corporate culture from leadership

```yaml
# Lines 6970–6982 — "Technology leadership should give innovation teams and engineers
# direction regarding which human values and legal norms should be promoted in the design
# of A/IS. Cultivating an ethical corporate culture is an essential component of successful
# leadership in the A/IS domain."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:values_based_leadership_direction"
      score: 1.0
      confidence: 0.8
      context: >
        "Technology leadership should give innovation teams and engineers direction
        regarding which human values and legal norms should be promoted in the design
        of A/IS." Approach claim — leadership as the named source of values-direction
        for engineering teams.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 2 Background lines 6970–6982"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: clean
nuance_lost: |
  Top-down vector — paired with bottom-up vector in §S2.I3. The substantive claim that
  leadership SHOULD direct rather than abdicate is preserved; the implicit critique of
  leadership abdication (treating ethics as Legal's problem, mentioned in §S2.I4) is not
  separately attested here.
```

---

## §S2.I2.r — Issue 2 Recommendations: senior-level roles; in-house ethicists; Chief Values Officer (CVO); de jure + de facto international human rights standards

```yaml
# Lines 6984–7011 — "Companies should create roles for senior-level marketers, engineers,
# and lawyers who can collectively and pragmatically implement ethically aligned design.
# There is also a need for more in-house ethicists, or positions that fulfill similar
# roles. One potential way to ensure values are on the agenda in A/IS development is to
# have a Chief Values Officer (CVO)... However, ethical responsibility should not be
# delegated solely to CVOs."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:chief_values_officer"
      score: 0.85
      confidence: 0.7
      context: >
        "One potential way to ensure values are on the agenda in A/IS development is to
        have a Chief Values Officer (CVO), a role first suggested by Kay Firth-
        Butterfield... However, ethical responsibility should not be delegated solely
        to CVOs." Partner-role attestation with deliberately-soft polarity reflecting
        the "potential way" + "not solely" qualifications.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 2 Recommendations lines 6993–7001"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:applied_ethics:multi_lingual"
      score: 1.0
      confidence: 0.8
      context: >
        "There is also a need for more in-house ethicists, or positions that fulfill
        similar roles." Expertise-domain claim — applied-ethics expertise as recognized
        organizational capacity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 2 Recommendations lines 6989–6991"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore Standing: expertise:{domain}:{language})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:human_rights_de_jure_and_de_facto"
      score: 1.0
      confidence: 0.85
      context: >
        "Companies need to ensure that their understanding of values-based system
        innovation is based on de jure and de facto international human rights
        standards." Justice-principle anchoring with the de-jure-AND-de-facto coupling
        as a constraint on values-claims.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 2 Recommendations lines 7006–7011"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: |
  "Ethical responsibility should not be delegated solely to CVOs" is a structurally
  important anti-scapegoating constraint — that distributed responsibility cannot be
  collapsed to one named office. The wire format encodes the positive partner_role on
  CVO but does not separately encode the "non-delegation" constraint; partial composition
  hint via the moderate-score (0.85 rather than 1.0) on the CVO attestation.
```

---

## §S2.I3.bg — Issue 3 Background: empowerment to raise ethical concerns; obstacles within organizations

```yaml
# Lines 7006–7037 — Engineers/design teams encounter obstacles to raising ethical concerns;
# corporate culture should incentivize technical staff to voice ethical questions throughout
# the full product lifecycle; raising concerns can be perceived as slowing projects;
# values-based design should be recognized + incentivized
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:engineer_ethical_voice"
      score: 0.6
      confidence: 0.65
      context: >
        "Engineers and design teams may encounter obstacles to raising ethical concerns
        regarding their designs or design specifications within their organizations."
        Pattern of voice-suppression at organizational scale — participation-exclusion
        axis specifically over technical-staff ethical voice.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 3 Background lines 7006–7012"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:*)"
verdict: clean
nuance_lost: |
  "Raising ethical concerns can be perceived as slowing or halting a design project"
  carries a specific implicit-incentive-shape claim — that velocity-incentives suppress
  ethical voice — which the detection prefix flattens to the bare exclusion pattern.
  The incentive-mechanism behind the exclusion is preserved only in evidence_refs prose.
```

---

## §S2.I3.r — Issue 3 Recommendations: empower employees; create trust atmosphere; reward town halls bringing up ethics

```yaml
# Lines 7039–7062 — "Employees should be empowered and encouraged to raise ethical concerns
# in day-to-day professional practice." Company culture/norms encouraging incorporation of
# ethical considerations; new categories of considerations + updated Codes of Conduct;
# bottom-up "town hall meetings" should be explored that reward (not punish) ethical
# concern-raising
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:employee_ethical_voice_empowerment"
      score: 1.0
      confidence: 0.85
      context: >
        "Employees should be empowered and encouraged to raise ethical concerns in
        day-to-day professional practice." Concrete method — voice-empowerment as
        operational practice; paired with reward-rather-than-punish norm for those who
        bring up ethical concerns.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 3 Recommendations lines 7041–7061"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:codes_of_conduct_updated_for_ais_ethics"
      score: 1.0
      confidence: 0.8
      context: >
        "New categories of considerations around these issues need to be accommodated,
        along with updated Codes of Conduct, company value-statements, and other
        management principles." Method-level update of governance instruments to
        cover A/IS-specific ethics.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 3 Recommendations lines 7052–7057"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  "Atmosphere of trust" is a relational-emotional claim that the wire format cannot
  encode at the affective layer — the closest available framing would be a future
  v1.5+ affective:* prefix family per the Ch 5 T-3 surface. Whistleblower-protection
  is implicit but not explicitly attested as a prohibited:retaliation_against_ethical_voice
  type prohibition; the recommendation is positive-incentive-shaped, not constraint-shaped.
```

---

## §S2.I4.bg — Issue 4 Background: ownership and responsibility; "Legal will handle that" delegation; professional-ethics vs A/IS-ethics distinction

```yaml
# Lines 7035–7063 — Variance within tech community on its responsibility regarding A/IS;
# clear delineations among engineering/legal/marketing functions; technologists
# incentivized on functional/deadline/financial; "Legal will handle that" for larger
# social issues; ethics often = code of conduct vs values-driven design process
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:engineering_ethical_ownership"
      score: 0.6
      confidence: 0.65
      context: >
        "Technologists will often be incentivized in terms of meeting functional
        requirements, deadline, and financial constraints, but for larger social issues
        may say, 'Legal will handle that.'" Pattern-claim of systematic responsibility-
        externalisation from engineering to legal/marketing functions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 4 Background lines 7045–7052"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:*)"
verdict: clean
nuance_lost: |
  The "professional ethics vs A/IS ethics" distinction (line 7053–7063) is a meta-
  taxonomic claim about how the word "ethics" gets used in industry — that the wire
  format does not have a primitive for "definitional clarification of an ethical term."
  Closest fit would be a composed claim on integrity:terminology_clarification but that
  would be over-fitting; the substantive operational content is captured by the
  Recommendation below.
```

---

## §S2.I4.r — Issue 4 Recommendations: clarify professional vs applied-ethics; corporate ethical review boards with diverse composition examining justifications

```yaml
# Lines 7066–7103 — "Organizations should clarify the relationship between professional
# ethics and applied A/IS ethics by helping or enabling designers, engineers, and other
# company representatives to discern the differences." "Corporate ethical review boards,
# or comparable mechanisms, should be formed to address ethical and behavioral concerns...
# Such boards should seek an appropriately diverse composition and use relevant criteria,
# including both research ethics and product ethics... These boards should examine
# justifications of research or industrial projects."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:corporate_ethical_review_board"
      score: 1.0
      confidence: 0.85
      context: >
        "Corporate ethical review boards, or comparable mechanisms, should be formed to
        address ethical and behavioral concerns in relation to A/IS design, development
        and deployment." Partner-role for corporate-level ethical review with explicit
        diverse-composition + dual research/product ethics scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 4 Recommendations lines 7086–7097"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:corporate_ethical_review_board_composition"
      score: 1.0
      confidence: 0.85
      context: >
        "Such boards should seek an appropriately diverse composition and use relevant
        criteria, including both research ethics and product ethics, at the appropriate
        levels of advancement of research and development." Witness-diversity claim
        bound to the corporate-ethical-review partner_role.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 4 Recommendations lines 7090–7094"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:project_justification_examination"
      score: 1.0
      confidence: 0.8
      context: >
        "These boards should examine justifications of research or industrial projects."
        Concrete method on the corporate ethical review board's operational task.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 4 Recommendations lines 7095–7097"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  "Appropriately diverse" defers to the deployment context; the wire format encodes
  witness_diversity at the meta-attestation level (N=3 default per LANGUAGE_PRIMER) but
  not the substantive criteria for "appropriate" diversity at corporate ethical review
  scale. The "examine justifications" task is closer to the §Ch2 P2/P3 Accountability
  primitives (per the chapter's own self-reference at S3) than to a standalone method;
  carried here for completeness.
```

---

## §S2.I5.bg — Issue 5 Background: stakeholder inclusion; UX practitioners' on-the-ground expertise; accessibility

```yaml
# Lines 7107–7127 — Interface between A/IS and practitioners/stakeholders gaining attention
# (healthcare diagnostics example); on-the-ground expertise of occupational therapists,
# patient end-users; stakeholder feedback crucial; UX design concepts including
# accessibility (for human physical disabilities); continuously consider impact through
# unanticipated use + unforeseen interests
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:participatory_stakeholder_inclusion"
      score: 1.0
      confidence: 0.85
      context: >
        "Stakeholders' feedback is crucial to design a system that takes ethical and
        social issues into account." Approach claim — participatory stakeholder
        inclusion as a route to ethically-aligned A/IS design.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 5 Background lines 7122–7125"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "testimonial_witness:on_the_ground_practitioner"
      score: 1.0
      confidence: 0.85
      context: >
        "Occupational therapists and their assistants may have on-the-ground expertise
        in working with a patient, who might be the 'end user' of a robot or social
        A/IS technology." Singular-narrative claim — preserving practitioner's
        irreducible testimony as a structural shape distinct from witness_diversity
        aggregation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 5 Background lines 7118–7122"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus: testimonial_witness:{kind})"
verdict: composed
nuance_lost: |
  "Accessibility... that consider human physical disabilities" is a specific protected-
  characteristic anchor that compositionally hits prohibited:discrimination but is
  framed positive-side here (design-incorporation, not anti-discrimination). The
  positive-framing of disability-inclusion vs the negative-framing-only of the
  prohibitions catalog is a known asymmetry (per LANGUAGE_PRIMER §11.8 worked example
  on positive-dignity affirmation).
```

---

## §S2.I5.r — Issue 5 Recommendation: planned/controlled activities accounting for stakeholders, building on practitioner wisdom

```yaml
# Lines 7141–7148 — "To ensure representation of stakeholders, organizations should enact
# a planned and controlled set of activities to account for the interests of the full
# range of stakeholders or practitioners who will be working alongside A/IS and
# incorporating their insights to build upon, rather than circumvent or ignore, the
# social and practical wisdom of involved practitioners and other stakeholders."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:planned_stakeholder_inclusion_activities"
      score: 1.0
      confidence: 0.85
      context: >
        "Organizations should enact a planned and controlled set of activities to
        account for the interests of the full range of stakeholders or practitioners
        who will be working alongside A/IS." Concrete operational method specifying
        the planned + controlled discipline of stakeholder activities.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 5 Recommendations lines 7141–7148"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: clean
nuance_lost: |
  "Build upon, rather than circumvent or ignore, the social and practical wisdom of
  involved practitioners" carries the substantive normative content that practitioner
  wisdom is a positive input class with a non-negative-floor obligation. The method-
  prefix encodes the operational shape; the underlying wisdom-as-positive-input claim
  composes onto the testimonial_witness attestation in §S2.I5.bg above. No new prefix
  owed.
```

---

## §S2.I6.bg — Issue 6 Background: values-based design as innovation, not impediment

```yaml
# Lines 7142–7187 — Ethics often treated as impediment; advocates for ethical design should
# be seen as innovators; design processes have ethics-highlighting moments; no universally
# prescribed models because organizations vary; transition points between discovery/
# prototyping/release/revisions are natural review contexts; iterative review processes
# advisable
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "approach:values_based_design_as_innovation"
      score: 1.0
      confidence: 0.8
      context: >
        "Those who advocate for ethical design within a company should be seen as
        innovators seeking the best outcomes for the company, end users, and society."
        Approach-level reframing of ethics-advocacy as innovation rather than
        impediment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 6 Background lines 7156–7162"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: approach:*)"
verdict: clean
nuance_lost: |
  Values-Sensitive Design (Friedman, Hendry, Borning) as a specific named methodology in
  the academic literature is not separately attested — "values-based design" is used as
  generic. The wire format does not encode "this approach has a specific named
  methodology with a published literature" distinct from the operational shape. Watching
  this as a T-3 candidate (see §Methodology-T3-candidates note at end) but ultimately
  composition holds: VSD's operational shape = stakeholder identification + value
  identification + technical investigation = method:* + witness_diversity:* +
  testimonial_witness:* + expertise:*.
```

---

## §S2.I6.r — Issue 6 Recommendations: encourage notice/response; formal-review points; red-flag indicators; minors/protected-class triggers

```yaml
# Lines 7141–7187 — Companies should study design processes to identify when engineers/
# researchers can raise ethics; achieving distributed responsibility for ethics requires
# all people involved to notice/respond; organizations consider how to facilitate
# deliberations among peers; identify points for formal review; reviews focus on "red
# flags" identified in advance as risk indicators (e.g., datasets involving minors or
# protected-class users requiring additional justification)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:red_flag_indicators_in_formal_review"
      score: 1.0
      confidence: 0.85
      context: >
        "Organizations should identify points for formal review during product
        development. These reviews can focus on 'red flags' that have been identified
        in advance as indicators of risk. For example, if the datasets involve minors
        or focus on users from protected classes, then it may require additional
        justification or alterations to the research or development protocols."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 6 Recommendations lines 7161–7170"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:distributed_ethical_responsibility_in_design"
      score: 1.0
      confidence: 0.8
      context: >
        "Achieving a distributed responsibility for ethics requires that all people
        involved in product design are encouraged to notice and respond to ethical
        concerns." Method specifying the distribution-of-responsibility shape.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S2 Issue 6 Recommendations lines 7149–7159"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  The minors / protected-classes red-flag triggers are specific protected-characteristic
  anchors that hit prohibited:discrimination-adjacent territory but are framed
  procedurally (trigger-for-additional-review) rather than substantively (prohibition).
  The dataset-trigger pattern is closer to a detection:* axis on dataset-composition
  than to a method:*; chose method here for operational-fidelity to the recommendation's
  text but flagged as a potential refinement.
```

---

# Section 3 — Responsibility and Assessment

> *"Lack of accountability of the A/IS design and development process presents a challenge to ethical implementation and oversight."*

---

## §S3.0 — Section preamble: lack of accountability; four issues moving from macro to micro

```yaml
# Lines 7203–7208 — "Lack of accountability of the A/IS design and development process
# presents a challenge to ethical implementation and oversight. This section presents four
# issues, moving from macro oversight to micro documentation practices."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Structural-framing introduction; the substantive accountability claim is carried by
  the per-Issue attestations below. Per LANGUAGE_PRIMER §8 Step 1(b).
nuance_lost: |
  "Moving from macro oversight to micro documentation practices" is an organizational
  scale-cascade that the per-Issue attestations re-encode via cohort_scope ranging
  from species (oversight bodies) to affiliations (corporate documentation). Not
  separately encoded as a scale-cascade primitive.
```

---

## §S3.I1.bg — Issue 1 Background: oversight for algorithms; no end-user account of how a system reached its conclusions

```yaml
# Lines 7212–7225 — "The algorithms behind A/IS are not subject to consistent oversight.
# This lack of assessment causes concern because end users have no account of how a certain
# algorithm or system came to its conclusions."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:algorithmic_oversight_gap"
      score: 0.7
      confidence: 0.75
      context: >
        "The algorithms behind A/IS are not subject to consistent oversight. This lack
        of assessment causes concern because end users have no account of how a certain
        algorithm or system came to its conclusions." Population-scale informational-
        asymmetry pattern between deployers and end users.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 1 Background lines 7212–7218"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:informational_asymmetry)"
verdict: clean
nuance_lost: |
  "End users have no account" carries a specific epistemic-asymmetry claim — that users
  are structurally denied the inference chain leading to outputs that affect them. The
  detection-axis on informational_asymmetry captures the population-pattern; the
  individual-recipient claim (denial-of-account-to-this-user) is not separately
  attested but composes through §S3.I3 and §S3.I4 below (black-box mitigations +
  documentation requirements).
```

---

## §S3.I1.r — Issue 1 Recommendations: standards for A/IS oversight balancing IP with public protection; human rights + algorithmic impact assessments paired with public consultation

```yaml
# Lines 7228–7246 — Accountability: algorithmic transparency; IP cannot/will not be
# released; standards providing oversight need to be created to avoid harm; look to
# biomedical/civil/aerospace engineering for IP-vs-oversight balance. Human rights and
# algorithmic impact assessments should be explored; paired with public consultations;
# final impact assessments must be made public.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:human_rights_impact_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        "Human rights and algorithmic impact assessments should be explored as a
        meaningful way to improve the accountability of A/IS." Method-level claim
        on the HRIA/AIA instrument pairing.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 1 Recommendations lines 7209–7214"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:algorithmic_impact_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        Companion to HRIA — algorithmic impact assessment as paired method per the
        same Recommendation paragraph, with public-consultation discipline and public-
        release-of-final-assessments requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 1 Recommendations lines 7209–7214"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:public_consultation_on_ais_impact_assessments"
      score: 1.0
      confidence: 0.85
      context: >
        "These need to be paired with public consultations, and the final impact
        assessments must be made public." Method specifying the public-consultation
        and public-release discipline binding the impact-assessment methods.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 1 Recommendations lines 7210–7214"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  "Look to other technical domains, such as biomedical, civil, and aerospace engineering"
  is a methodology-import claim that the wire format treats as evidence-context rather
  than as a separate cross-domain-borrowing primitive. The IP-vs-oversight balance
  (lines 7235–7246) is preserved as background but not separately attested; the
  Recommendation primitives carry the resolved direction.
```

---

## §S3.I2.bg — Issue 2 Background: independent review organization needed; gap between A/IS marketing and performance

```yaml
# Lines 7268–7299 — "We need independent, expert opinions that provide guidance to the
# general public regarding A/IS. Currently, there is a gap between how A/IS are marketed
# and their actual performance or application." A/IS technology accompanied by best-use
# recommendations + warnings; certification scheme for A/IS; concrete examples (downloaded
# self-parking; companion robot watching children) with no independent reviewer; ratings
# and approval system needed; further government funding for review-research
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:ais_marketing_vs_performance_gap"
      score: 0.7
      confidence: 0.7
      context: >
        "Currently, there is a gap between how A/IS are marketed and their actual
        performance or application." Pattern claim — informational asymmetry between
        vendor representations and verified system behavior, at population scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 2 Background lines 7270–7275"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:informational_asymmetry)"
verdict: clean
nuance_lost: |
  The specific examples (self-parking download; companion robot for children) are
  preserved as evidence-context but the wire format does not separately tag deployment-
  category-specific risks. Children-as-protected-class for companion robotics composes
  onto prohibited:* or non_maleficence:* but the chapter does not assert at that level;
  it is in the Background as illustration. The §S3.I1.r impact-assessment methods carry
  the operational resolution.
```

---

## §S3.I2.r — Issue 2 Recommendation: independent, internationally coordinated body akin to ISO with certification process

```yaml
# Lines 7261–7269 — "An independent, internationally coordinated body—akin to ISO—should
# be formed to oversee whether A/IS products actually meet ethical criteria, both when
# designed, developed, deployed, and when considering their evolution after deployment and
# during interaction with other products. It should also include a certification process."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:independent_international_ais_review_body"
      score: 1.0
      confidence: 0.85
      context: >
        "An independent, internationally coordinated body—akin to ISO—should be formed
        to oversee whether A/IS products actually meet ethical criteria, both when
        designed, developed, deployed, and when considering their evolution after
        deployment and during interaction with other products." Partner-role attestation
        for a proposed international oversight body covering full lifecycle.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 2 Recommendations lines 7261–7269"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ais_certification_process"
      score: 1.0
      confidence: 0.85
      context: >
        "It should also include a certification process." Method-level claim — A/IS
        certification as the operational instrument of the proposed body.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 2 Recommendations lines 7267–7269"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.85
      context: >
        "Independent, internationally coordinated body" is explicit federation-scale
        locality framing for A/IS oversight decisions; triggers §6.1.5 locality-scaled-
        quorum on adjudication of this Contribution.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 2 Recommendations lines 7261–7263"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore Action: locality:decision:{scale})"
verdict: composed
nuance_lost: |
  "Akin to ISO" is a methodology-analogy that flags ISO as the operational template for
  the proposed body. The wire format does not separately encode "model your governance
  on this existing organization" as a primitive; it's preserved as evidence-context.
  Once formed, the body would itself become a key_id attestable in the federation, but
  the chapter is proposing it doesn't-yet-exist.
```

---

## §S3.I3.bg — Issue 3 Background: black-box components; deep learning as growing source; A/IS not guaranteed to operate as intended

```yaml
# Lines 7288–7304 — "Software developers regularly use 'black box' components in their
# software, the functioning of which they often do not fully understand. 'Deep' machine
# learning processes... A/IS developers will likely be unable to build systems that are
# guaranteed to operate as intended."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:black_box_components"
      score: 0.7
      confidence: 0.8
      context: >
        "Software developers regularly use 'black box' components in their software,
        the functioning of which they often do not fully understand... A/IS developers
        will likely be unable to build systems that are guaranteed to operate as
        intended." Pattern at developer-population scale; the asymmetry is also
        internal-to-the-builders (not just deployer-to-end-user).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 3 Background lines 7293–7304"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore detection:correlated_action:informational_asymmetry)"
verdict: clean
nuance_lost: |
  "Guaranteed to operate as intended" is a candid no-guarantee admission about the
  current technical state — an epistemic-humility claim from the IEEE committee itself.
  The wire format flags the pattern but does not separately encode "the experts admit
  current systems aren't guarantee-able"; that institutional-epistemic-humility content
  lives in evidence_refs prose.
```

---

## §S3.I3.r — Issue 3 Recommendations: acknowledge/assess ethical risks; documentation/audits/traceable standards; ethical due diligence; flight-data-recorder analogy

```yaml
# Lines 7319–7355 — Engineers must acknowledge and assess ethical risks involved with
# black-box software and implement mitigation strategies. Technologists should characterize
# what algorithms/systems will do via documentation, audits, transparent and traceable
# standards; characterizations should be predictive but may need to be retrospective and
# mitigation-oriented. Important to ensure access to remedy adverse impacts.
# Technologists/corporations must do ethical due diligence; standards from IEEE or ISO,
# barring that each corporation generates own ethical standards. Flight-data-recorder
# analogy — algorithmic traceability for questionable/dangerous behaviors. Even where
# processes opaque, seek indirect means of validating results + detecting harms.
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:black_box_ethical_risk_acknowledgment_and_mitigation"
      score: 1.0
      confidence: 0.85
      context: >
        "Engineers must acknowledge and assess the ethical risks involved with black
        box software and implement mitigation strategies." Concrete method — risk
        acknowledgment + mitigation strategies as paired operational practice for
        black-box components.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 3 Recommendations lines 7320–7325"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:algorithmic_traceability"
      score: 1.0
      confidence: 0.85
      context: >
        "Similar to a flight data recorder in the field of aviation, algorithmic
        traceability can provide insights on what computations led to questionable or
        dangerous behaviors." Concrete method on traceability instrumentation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 3 Recommendations lines 7348–7355"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:access_to_remedy_for_adverse_impacts"
      score: 1.0
      confidence: 0.85
      context: >
        "It is also important to ensure access to remedy adverse impacts." Method
        attestation on remedy-access as operational requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 3 Recommendations lines 7335–7337"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ais_ethical_due_diligence"
      score: 1.0
      confidence: 0.85
      context: >
        "Technologists and corporations must do their ethical due diligence before
        deploying A/IS technology. Standards for what constitutes ethical due diligence
        would ideally be generated by an international body such as IEEE or ISO, and
        barring that, each corporation should work to generate a set of ethical
        standards by which their processes are evaluated and modified."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 3 Recommendations lines 7339–7347"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
verdict: composed
nuance_lost: |
  Four methods stacked on one recommendation block — at the upper bound of composition-
  per-paragraph discipline (LANGUAGE_PRIMER §8 Step 5). Each is a distinct operational
  practice (risk acknowledgment, traceability, remedy access, due diligence) that the
  paragraph genuinely names; the alternative would be a residual on three of them which
  would be less honest. The flight-data-recorder analogy is preserved as evidence-context
  on the traceability method but not as a separate cross-domain-borrowing primitive.
```

---

## §S3.I4.bg — Issue 4 Background: better technical documentation needed; opacity often result of human decision

```yaml
# Lines 7344–7360 — "A/IS are often construed as fundamentally opaque and inscrutable.
# However, lack of transparency is often the result of human decision. The problem can be
# traced to a variety of sources, including poor documentation that excludes vital
# information about the limitations and assumptions of a system. Better documentation
# combined with internal and external auditing are crucial to understanding a system's
# ethical impact."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:opacity_as_human_decision_not_intrinsic"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS are often construed as fundamentally opaque and inscrutable. However,
        lack of transparency is often the result of human decision." Integrity-anchored
        claim — opacity is at least partly attributable to human choices around
        documentation, not solely intrinsic to the systems.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 4 Background lines 7344–7349"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  This is an analytically-load-bearing claim — that "the system is a black box" is at
  least partially a deferral of responsibility — that bears directly on whether
  accountability claims attach to humans or are diffused into "the technology." The
  integrity-prefix carries the direction but the specific responsibility-routing
  argument is preserved as evidence-context, not separately encoded.
```

---

## §S3.I4.r — Issue 4 Recommendation: thorough documentation of end product, data flows, performance, limitations, risks; auditability/accessibility/meaningfulness/readability

```yaml
# Lines 7376–7398 — "Engineers should be required to thoroughly document the end product
# and related data flows, performance, limitations, and risks of A/IS. Behaviors and
# practices that have been prominent in the engineering processes should also be explicitly
# presented, as well as empirical evidence of compliance and methodology used, such as
# training data used in predictive systems, algorithms and components used, and results of
# behavior monitoring. Criteria for such documentation could be: auditability,
# accessibility, meaningfulness, and readability. Companies should make their systems
# auditable and should explore novel methods for external and internal auditing."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:thorough_ais_documentation_requirement"
      score: 1.0
      confidence: 0.9
      context: >
        "Engineers should be required to thoroughly document the end product and
        related data flows, performance, limitations, and risks of A/IS." Concrete
        method on the documentation requirement scope (product, data flows,
        performance, limitations, risks) with documentation criteria (auditability,
        accessibility, meaningfulness, readability).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 4 Recommendations lines 7376–7390"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ais_internal_and_external_auditing"
      score: 1.0
      confidence: 0.85
      context: >
        "Companies should make their systems auditable and should explore novel methods
        for external and internal auditing." Method on dual-axis auditing (internal +
        external) with novel-methods exploration mandate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 4 Recommendations lines 7392–7395"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:documentation_criteria_audit_access_meaning_read"
      score: 1.0
      confidence: 0.85
      context: >
        "Criteria for such documentation could be: auditability, accessibility,
        meaningfulness, and readability." Progress-measure on the thorough-documentation
        method — four named criteria for documentation quality.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch7 S3 Issue 4 Recommendations lines 7388–7390"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action: progress_measure:{method_id})"
verdict: composed
nuance_lost: |
  The full goal/approach/method/progress_measure DAG composes here: the chapter goal
  (ethical A/IS R&D) → S3 approach (responsibility + assessment) → documentation method
  → audit/access/meaning/read progress measures. Encoded as three contributions at the
  method + progress_measure layer; the upward DAG to chapter-level goal is implicit via
  evidence_refs to §Ch7.0. The Family B upward-only DAG discipline (LANGUAGE_PRIMER §2
  Family B note) is respected — no downward references.
```

---

# Acknowledgements section

## §Ch7.ack — Contributors acknowledgement; Committee membership

```yaml
# Lines 7414–7466 — Thanks-to-contributors section listing Committee members with
# affiliations; non-normative process content
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Per the manifest, the Acknowledgements / About-Process / References sections are
  declared non-normative; not mapped. Each contributor's individual standing could
  theoretically be attested (credits:*:* or expertise:* on each name) but this would
  be over-fitting at the bootstrap layer — those attestations should originate from
  the individuals themselves via standard federation onboarding, not be assigned
  by the bootstrap-batch signer.
nuance_lost: |
  The committee-composition itself is a witness_diversity-relevant artifact (geographic
  spread, institutional spread, disciplinary spread). Documenting that the Methods
  chapter was produced by a diverse committee strengthens its standing as a Contribution
  source; that meta-claim is recorded in this paragraph in prose but not separately
  attested. The bootstrap_batch_id evidence ref carries the chain via the manifest.
```

---

# Chapter synthesis notes (for §Ch7 reviewer + Phase 3 synthesis)

## Verdict distribution (this chapter)

| Verdict | Count | Notes |
|---|---|---|
| clean | 14 | Single-primitive units across all three sections |
| composed | 10 | 2–4 primitive composition; heaviest in Recommendation blocks |
| partial | 1 | §S1.I1.bg — methodological-impossibility residual (T-2 classification) |
| not-translated | 5 | §Ch7.0a, §S1.I1.fr, §S1.I3.fr, §S3.0, §Ch7.ack — all T-2 (structural/bibliographic) |

Total atomic units: **30**.

## Structural-primitive usage (this chapter)

| Primitive | Count | Notes |
|---|---|---|
| scores | ~50 individual Attestations | dominant |
| delegates_to | 0 | no authority-source claims in this chapter (the cited literature is hearsay-citation via evidence_refs, not delegated-authority) |
| supersedes | 0 | this is original IEEE EAD1e content, not a versioned doctrinal development |
| withdraws | 0 | not applicable |
| recants | 0 | not applicable |

## Prefix family distribution

| Family | Approximate count | Most-used prefix |
|---|---|---|
| A — STANDING | ~8 | `partner_role:*` (review boards, CVO, accreditation, certification body); `expertise:*` (IIE, applied ethics); `multilateral_participation:*` |
| B — ACTION | ~25 | `method:*` (dominant — fitting for a methodology chapter); `approach:*`; `goal:*`; `locality:decision:*`; `progress_measure:*` |
| C — DETECTION | ~7 | `detection:correlated_action:participation_exclusion:*` and `:informational_asymmetry:*` (the background-paragraph workhorses) |
| D — CONSENSUS | ~3 | `witness_diversity:*` (curricular informants; board composition); `testimonial_witness:*` (on-the-ground practitioners) |
| E — CORRECTION | 0 | not applicable in this chapter — no moderation/slashing/reconsideration content |

`method:*` dominates as expected for a methodology chapter. The composition pattern that
held: `method:* + witness_diversity:* + testimonial_witness:* + expertise:*` carried
every specific named methodology in the chapter (Value-Sensitive Design / participatory
design / intercultural information ethics / values-based design / ethics filters /
red-flag protocols / algorithmic impact assessment / human rights impact assessment /
documentation auditing).

## T-3 candidates surfaced

**None load-bearing.** The pre-translation flag for value-sensitive-design / participatory-
method specific recommendations was **investigated and rejected as T-3** at three points:

1. **§S1.I3.r — intercultural information ethics (IIE)**: surfaced as a named methodology
   with its own scholarly lineage (Capurro, Bielby). Considered T-3 (`methodology:iie:*`)
   but rejected: composition `expertise:intercultural_information_ethics:multi_lingual +
   partner_role:ethics_committee` carries the operational shape. The substantive
   philosophical content of IIE is T-1-adjacent (the tradition holds its own authority);
   the operational shape (committee composition + expertise role) translates clean. No
   methodology-naming primitive owed.

2. **§S2.I6.bg — Values-Sensitive Design (VSD)**: VSD is a named methodology in the HCI
   literature (Friedman, Hendry, Borning) with three named stages (conceptual /
   empirical / technical investigations). Considered T-3 (`methodology:vsd:*`) but
   rejected: VSD's operational shape = stakeholder identification + value identification
   + technical investigation = `method:* + witness_diversity:* + testimonial_witness:* +
   expertise:*`. Composition holds; no methodology-naming primitive owed. The
   methodology's *internal structure* (the three-investigation discipline) is a
   sub-methodology detail that future bootstrap-batches of the VSD literature could carry
   via composed `method:*` chains, not requiring a new prefix family.

3. **§S2.I5 + §S2.I6 — participatory stakeholder inclusion + red-flag protocols**:
   considered T-3 (`methodology:participatory_design:*` and `methodology:red_flag:*`)
   but rejected: both compose cleanly onto `method:* + witness_diversity:* +
   testimonial_witness:*`. The "red flag" pattern is operationally a method that
   triggers other methods (additional justification / protocol alteration); composes
   onto the existing Family B Action hierarchy without naming-pressure.

**Composition-before-extension discipline (per METHODOLOGY.md §8.5.2) held in all three
candidate moments.** No load-bearing T-3 surface emerges from this chapter.

## Calibration paragraph

The chapter's methodological character means heavy `method:*` usage — at the upper end
of what FSD-002 §3.6.2 anticipates for a single chapter. This is appropriate to the
chapter's role (the operative *how* of ethics-into-design) but is a tighter test of the
Family B Action hierarchy than the General-Principles chapter (Ch 2) was. The DAG
discipline (goal:species → approach:* → method:* → progress_measure:*) was respected
upward at the §S3.I4.r block (documentation criteria as progress_measure on documentation
method).

The chapter's recommended **institutional infrastructure** (CVO role; corporate ethics
review boards; intercultural information ethics committees; independent international
review body akin to ISO; accreditation bodies; algorithmic impact assessment + human
rights impact assessment) maps onto `partner_role:*` (Registry §3.9) and
`multilateral_participation:*` cleanly. No infrastructure-naming primitive is owed.

The chapter's recommended **detective patterns** (engineering ethical voice exclusion;
black-box informational asymmetry; algorithmic oversight gap; marketing-vs-performance
asymmetry) map onto `detection:correlated_action:*` with axis values
`participation_exclusion:*` and `informational_asymmetry:*`. Pattern-language is
mechanism-descriptive throughout per §1.10.1 T2.

The chapter's heaviest composition pressure was at §S3.I3.r (four-method stack on one
recommendation block) and §S3.I4.r (three-attestation method/progress-measure DAG). Both
remained honest compositions — each primitive named a structurally distinct operational
object — rather than over-composition for ceremonial completeness. The chapter respects
LANGUAGE_PRIMER §8 Step 5 (compose only when needed).

The Acknowledgements / Resources / Further-Resources sections (T-2 classification) are
correctly held in prose per LANGUAGE_PRIMER §10 — bibliographic and process content does
not translate to wire format. The pastoral-prose discipline holds.

Verdict: chapter translates **cleanly** as structure-capture. The recommendation density
is high but composes onto existing primitives without forcing extensions. Confidence in
the v1.4 wire format's expressive adequacy for ethics-methodology content is reinforced
by this chapter, complementing the General-Principles chapter (Ch 2) coverage of the
operative-content side.

---

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH07_METHODS.md**
