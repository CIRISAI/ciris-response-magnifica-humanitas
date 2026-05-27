# CONTRIBUTION_OBJECTS_IEEE_EAD_CH01_FROM_PRINCIPLES_TO_PRACTICE.md
# IEEE Ethically Aligned Design 1st Edition (2019) — Chapter: "From Principles to Practice"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 477–823)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Front matter

```yaml
batch_id: ieee_ead_v1
chapter: "From Principles to Practice (EAD1e Conceptual Framework chapter)"
source_line_range: "ead1e.txt lines 477–823"
chapter_role: |
  This is the document's conceptual-framework / methodology chapter. It introduces the
  Three Pillars, names (but does not elaborate) the Eight General Principles, displays
  two mapping tables (Pillars→Principles; Principles→Chapters), and frames the rest
  of EAD1e. The chapter is heavily structural — its primary work is navigational
  framing of what follows. Operational content is concentrated in (a) the Three
  Pillars' descriptive paragraphs and (b) endnote 3 on certification.
unit_count: 13
verdict_distribution:
  clean: 2
  composed: 5
  partial: 0
  not-translated: 6
not_translated_breakdown:
  T-1: 0
  T-2: 6
  T-3: 0
t3_candidates: 0
methodology_notes: |
  Per LANGUAGE_PRIMER §8 Step 1, a substantial fraction of this chapter is structural
  framing (chapter-organization headings, mapping-table presentation, recap of the
  multi-year process). These are correctly T-2 PASTORAL_PROSE — the rhetorical surface
  carries no independent operational claim that isn't covered by the substantive
  paragraphs (the Three Pillars) or the chapter that follows (the Eight General
  Principles, mapped in CH02).
  Per METHODOLOGY.md §8.5.2 composition-before-extension discipline, no T-3 candidates
  emerged: every operational claim in this chapter composes onto existing prefix
  families (autonomy, well-being / beneficence, justice / non-discrimination,
  fidelity, integrity, transparency, accountability, locality:decision, plus the
  certification / licensure family).
```

---

# Unit-by-unit mapping

## §CH01.1 — Opening framing: EAD1e is a consensus distillation of principles, issues, recommendations (lines 481–486)

```yaml
# Source quote (≤2 sentences):
# "Ethically Aligned Design, First Edition (EAD1e) represents more than a comprehensive
# report, distilling the consensus of its vast community of creators into a set of
# high-level ethical principles, key issues, and practical recommendations."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  This is doxological / self-positioning framing about the document's nature and
  audience ("inform a broader public", "inspire its audience"). No standalone
  operational claim. The substantive structural-primitive claim implicit here — that
  EAD1e is itself a senior governance document with consensus standing — is carried
  by the bootstrap_batch_id provenance manifest, not by a wire claim within the batch.
  Per LANGUAGE_PRIMER §8 Step 1(b): pastoral framing correctly stays in prose.
```

---

## §CH01.2 — Chapter scope statement: this chapter maps Pillars↔Principles↔Chapter content (lines 488–502)

```yaml
# Source quote (≤2 sentences):
# "This Chapter, 'From Principles to Practice', provides a mapping of the conceptual
# framework of Ethically Aligned Design. It outlines the logic behind 'Three Pillars'
# that form the basis of EAD1e, and it connects the Pillars to high-level 'General
# Principles' which guide all manner of ethical A/IS design."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Navigational framing — table-of-contents-style enumeration of the chapter's six
  internal sections. Each enumerated item is itself addressed by a later unit in
  this file or is itself meta (e.g., "Mapping the Pillars to the Principles" is a
  presentation of a table, not an operational claim). Per LANGUAGE_PRIMER §8 Step 1(b),
  navigational framing stays in prose.
```

---

## §CH01.3 — Pillar 1: Universal Human Values — A/IS as force for good aligned to human rights, well-being, environment, and broad benefit (lines 522–527)

```yaml
# Source quote (≤2 sentences):
# "A/IS can be an enormous force for good in society provided they are designed to
# respect human rights, align with human values, and holistically increase well-being
# while empowering as many people as possible. They should also be designed to
# safeguard our environment and natural resources."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:human_rights_and_well_being_alignment"
      score: 1.0
      confidence: 0.90
      context: >
        Pillar 1 of EAD1e (Universal Human Values): A/IS should be designed to respect
        human rights, align with human values, holistically increase well-being, and
        empower as many people as possible. Composes onto the CIRIS beneficence
        principle (FSD-002 §3.1 Agent: beneficence) with cohort_scope species. This
        is the anthropological pillar of the EAD1e framework.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 522–527 (Pillar 1)"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I beneficence)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:environmental_stewardship"
      score: 1.0
      confidence: 0.85
      context: >
        "They should also be designed to safeguard our environment and natural
        resources" — environmental-stewardship obligation. CIRIS-anchored via Accord
        §IV Ch 2 Resource Stewardship (compute/data/energy efficiency, quarterly
        stewardship audits) and the LLMBus per-call carbon_grams/energy_kwh audit
        chain. Cohort_scope species; biosphere reach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 524–525 (Pillar 1 environment clause)"
        - "ContributionRef(ACCORD §IV Ch 2 Resource Stewardship)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:broad_distribution_of_benefit"
      score: 1.0
      confidence: 0.85
      context: >
        "Advances in A/IS should be in the service of all people, rather than
        benefiting solely small groups, a single nation, or a corporation." A direct
        anti-concentration / universal-destination claim aligning with CIRIS's
        distributive-access detector family (LensCore §3.5.5 detection:distributive:
        access:*) and with the MH §§65–67 Universal Destination of Goods anchor
        in the federation graph.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 526–527 (Pillar 1 broad-benefit clause)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: composed
nuance_lost: |
  The envelope captures the three independent operational claims (human-rights /
  well-being alignment; environmental stewardship; broad-distribution-of-benefit)
  but does not preserve EAD's framing-language that grounds them in a single
  "anthropological pillar" composite — the integrative claim that all three together
  constitute "Universal Human Values" as a single concept is structural framing that
  the wire format decomposes into three independent attestations. The aesthetic /
  pedagogical unity of the pillar is lost.
```

---

## §CH01.4 — Pillar 2: Political Self-Determination and Data Agency (lines 528–533)

```yaml
# Source quote (≤2 sentences):
# "A/IS—if designed and implemented properly—have a great potential to nurture
# political freedom and democracy, in accordance with the cultural precepts of
# individual societies, when people have access to and control over the data
# constituting and representing their identity."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:data_agency_over_self_constituting_data"
      score: 1.0
      confidence: 0.90
      context: >
        Pillar 2 of EAD1e (Political Self-Determination and Data Agency): individuals
        must have access to and control over the data constituting and representing
        their identity. This composes onto the CIRIS autonomy principle (FSD-002 §3.1)
        and operationalizes as a precondition for political freedom + democratic
        participation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 528–533 (Pillar 2)"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §III autonomy)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.80
      context: >
        "Political freedom and democracy, in accordance with the cultural precepts
        of individual societies" — explicit recognition that decision-locality varies
        by cultural context. This is a federation-scale meta-claim (the principle of
        cultural-precept-respect applies universally) AND a directive that downstream
        decisions defer to locally-appropriate scopes. Triggers §6.1.5 locality-scaled
        quorum when downstream decisions invoke it.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 529–530 (Pillar 2 cultural-precepts clause)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:government_effectiveness_and_accountability"
      score: 0.85
      confidence: 0.80
      context: >
        "These systems can improve government effectiveness and accountability,
        foster trust, and protect our private sphere, but only when people have
        agency over their digital identity and their data is provably protected."
        A conditional positive claim — government-quality benefit is contingent on
        data agency + provable protection. Composes with the autonomy attestation
        above; the provable-protection clause anchors on CIRISVerify provenance and
        transparency_log primitives (FSD-002 §3.2).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 531–533 (Pillar 2 government + private-sphere clause)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  The conditional structure ("...but only when...") that ties the positive government-
  effectiveness claim to the data-agency precondition is not directly expressible as a
  single wire edge — it is reconstructed by a consumer reading both attestations
  together. The pillar's grounding in democratic-theory normativity ("nurture political
  freedom and democracy") survives only as a context note, not as a wire-level link
  to a democratic-governance prefix (none exists; nor is one obviously needed per
  §1.10.1 T2).
```

---

## §CH01.5 — Pillar 3: Technical Dependability (lines 534–540)

```yaml
# Source quote (≤2 sentences):
# "Ultimately, A/IS should deliver services that can be trusted. This trust means
# that A/IS will reliably, safely, and actively accomplish the objectives for which
# they were designed while advancing the human-driven values they were intended
# to reflect."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:reliable_safe_objective_fulfillment"
      score: 1.0
      confidence: 0.90
      context: >
        Pillar 3 of EAD1e (Technical Dependability): A/IS shall reliably, safely, and
        actively accomplish the objectives for which they were designed while advancing
        the human-driven values they were intended to reflect. Direct map to the CIRIS
        fidelity principle (FSD-002 §3.1) — fidelity to mandated purpose. This is the
        technical pillar of the framework.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 534–537 (Pillar 3 reliability + safety + objective-
          fulfillment clause)"
        - "ContributionRef(ACCORD §IV Ch 2 Fidelity to Mandated Purpose)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:monitoring_and_validation_to_explicit_ethical_objectives"
      score: 1.0
      confidence: 0.85
      context: >
        "Technologies should be monitored to ensure that their operation meets
        predetermined ethical objectives aligning with human values and respecting
        codified rights. In addition, validation and verification processes, including
        aspects of explainability, should be developed that could lead to better
        auditability and to certification of A/IS." Composes monitoring (CIRISLensCore
        coherence-ratchet detectors), validation/verification (CIRISVerify provenance
        + transparency_log + cert_validity), and explainability/auditability into a
        single integrity-discipline claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 536–540 (Pillar 3 monitoring + validation + cert clause)"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify attestation-ladder L1–L5)"
        - "ContributionRef(FSD-002 §3.5.1 LensCore coherence-ratchet detectors)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: composed
nuance_lost: |
  The Pillar's pedagogical claim that "trust" is the unifying outcome of reliability +
  safety + objective fulfillment + value-advancement is decomposed by the wire format
  into fidelity + integrity components; "trust" itself is not a wire prefix (and per
  §1.10.1 T2 should not be — it is an aggregate / subjective quality, not a
  mechanism). The chain certification→public-authority-control→audit (endnote 3)
  is captured in §CH01.13 below, not here.
```

---

## §CH01.6 — Enumeration of the Eight General Principles (lines 548–580)

```yaml
# Source quote (≤2 sentences):
# "1. Human Rights — A/IS shall be created and operated to respect, promote, and
# protect internationally recognized human rights. 2. Well-being — A/IS creators
# shall adopt increased human well-being as a primary success criterion for
# development."
# (and six more, enumerated in lines 548–580)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  In CH01, the Eight General Principles are introduced as a list/preview — the
  substantive elaboration of each Principle lives in CH02 ("General Principles"
  chapter, starting at line 824). Per LANGUAGE_PRIMER §8 Step 5, emitting wire
  attestations for a chapter-preview enumeration would double-count the operational
  content (the substantive Contributions are owed to CH02's elaboration of each
  Principle). Per METHODOLOGY.md §8.5.6, honest deferral over silent double-emission:
  the Principles are operational and translate cleanly, but they translate in CH02
  where they are elaborated, not here where they are merely listed. Cross-reference
  for the consumer: CONTRIBUTION_OBJECTS_IEEE_EAD_CH02_GENERAL_PRINCIPLES.md (future).
note: |
  This is the structural-only listing. The eight prefixes that will be emitted in
  CH02 are anticipated: justice:human_rights_protection; beneficence:well_being_primacy;
  autonomy:data_agency; fidelity:effectiveness_evidence; integrity:transparency_of_
  decision_basis; integrity:accountability_unambiguous_rationale; non_maleficence:
  misuse_guarding; integrity:competence_specification_and_adherence. Naming them
  here so consumers can verify continuity at CH02.
```

---

## §CH01.7 — Pillars↔Principles mapping table (lines 596–642)

```yaml
# Source quote (≤2 sentences):
# "Whereas the Pillars of the Ethically Aligned Design Conceptual Framework represent
# broad anthropological, political, and technical aspects relating to autonomous and
# intelligent systems, the General Principles provide contextual filters for deeper
# analysis and pragmatic implementation."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  This unit is the structural-presentation table mapping each of the 8 Principles
  to which of the 3 Pillars it relates to (with dots in a matrix). The mapping itself
  is meta-organizational: it tells a reader which Pillar a Principle "lives under,"
  but the operational claim of each Principle is independent of this mapping. Per
  LANGUAGE_PRIMER §8 Step 1(b), table-presentation framing is pastoral. Per
  METHODOLOGY.md §8.5.2, attempting to map each row of the matrix as a separate
  attestation (e.g., "Transparency relates to all three Pillars") would be a
  composition exercise without independent moral content — the relations are
  documentary, not normative.
note: |
  The narrative paragraph (lines 601–607) adds one substantive observation:
  "Transparency goes beyond technical features. It is an important requirement also
  for the processes of policy and lawmaking." This is a scope-extension claim about
  transparency. It is carried in §CH02 where Transparency is elaborated as a
  General Principle, with the policy-and-lawmaking scope as part of that prefix's
  operationalization. Not double-counting here.
```

---

## §CH01.8 — Principles↔Chapters mapping table (lines 657–705)

```yaml
# Source quote (≤2 sentences):
# "The Chapters of Ethically Aligned Design provide in-depth subject matter expertise
# that allows readers to move from the General Principles to more deeply analyze
# ethical A/IS issues within the context of their specific work."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Second structural-presentation table: which of the 11 EAD1e chapters elaborates
  which of the 8 General Principles, with primary vs secondary indicators. This is
  document-navigation metadata, not an operational claim. Per LANGUAGE_PRIMER §8
  Step 1(b), navigational tables stay in prose. The structural claim that
  "Principles like Competence may resonate in several EAD1e Chapters" is a
  documentation-style note about cross-cutting concerns, not a wire-level claim.
```

---

## §CH01.9 — "From Principles to Practice" subsection: Issues + Recommendations + impact-assessment process (lines 718–727)

```yaml
# Source quote (≤2 sentences):
# "Content provided in EAD1e Chapters is organized by 'Issues' identified as the
# most pressing ethical matters surrounding A/IS design to address today and
# 'Recommendations' on how it should be done. By reviewing these Issues and
# Recommendations in light of a specific A/IS product, service, or system being
# designed, readers are provided with a simple form of impact assessment and due
# diligence process to help put their 'Principles into Practice' for themselves."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:impact_assessment_and_due_diligence_process"
      score: 0.85
      confidence: 0.80
      context: >
        EAD1e endorses a structured impact-assessment + due-diligence discipline:
        designers should review identified Issues and Recommendations against the
        specific A/IS product/service/system being designed. This is a procedural
        integrity claim — operationalized in CIRIS via the PDMA Step 1
        contextualisation + Step 5 relational balance, plus CIRISVerify provenance
        chain. The "simple form" framing is acknowledged as a starting-point, not
        a comprehensive substitute for sector-specific assessment (which EAD defers
        to subsequent customization, lines 725–727).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 718–727 (From Principles to Practice subsection)"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml Step 1 + Step 5)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  The wire envelope captures that EAD endorses an impact-assessment + due-diligence
  procedural discipline, but does not preserve the pedagogical contrast between
  "simple form" (EAD1e self-positioned as starting-point) vs "more fine-tuned
  customization" (deferred to future sectoral work). That historical / aspirational
  framing (EAD as a beginning, not a terminus) is structural / pastoral and does
  not need a separate wire claim.
```

---

## §CH01.10 — Implementation track record: 14 IEEE Standards Projects + Certification Program + courses (lines 734–739)

```yaml
# Source quote (≤2 sentences):
# "The analysis of the Principles, Issues, and Recommendations generated as part
# of an iterative process have already inspired the creation of fourteen IEEE
# Standardization Projects, a Certification Program, A/IS Ethics Courses, and
# multiple other action-oriented programs currently in development."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "ieee-global-initiative"
    attestation_envelope:
      dimension: "commitment_fulfillment:ead_to_standards_pipeline"
      score: 0.85
      confidence: 0.80
      context: >
        EAD1e self-reports follow-through: 14 IEEE Standardization Projects, a
        Certification Program (ECPAIS — see endnote 3 unit), A/IS Ethics Courses,
        and other action-oriented programs already inspired by the Principles +
        Issues + Recommendations analysis. This is a track-record claim about the
        IEEE Global Initiative's translation of principles into binding standards
        activity — composes onto CIRIS's commitment_fulfillment family
        (FSD-002 §3.6.4 NodeCore) with the IEEE Global Initiative as attested entity.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 734–739 (Implementation subsection — standards
          pipeline)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore: commitment_fulfillment)"
verdict: clean
nuance_lost: |
  The envelope records the existence of a track record (14 standards + cert program
  + courses) at species scope but does not enumerate the specific standards (P7000
  series and others). The specific standards would each be their own attestations
  emitted from those standards' own bootstrap batches if they were ingested into
  the federation graph. The "iterative process" claim — that this is the result of
  bottom-up consensus over three years — is structural / pastoral.
```

---

## §CH01.11 — Multilateral engagement: UN, EC, OECD, national + municipal governments (lines 740–744)

```yaml
# Source quote (≤2 sentences):
# "In its earlier manifestations, Ethically Aligned Design informed collaborations
# on A/IS governance with a broad range of governmental and civil society
# organizations, including the United Nations, the European Commission, the
# Organization for Economic Cooperation and Development and many national and
# municipal governments and institutions."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "ieee-global-initiative"
    attestation_envelope:
      dimension: "multilateral_participation:UN:informing_collaboration"
      score: 1.0
      confidence: 0.85
      context: >
        EAD has informed collaborations with the UN, European Commission, OECD, and
        many national + municipal governments. Multilateral-participation attestation
        across multiple international + national forums; CIRIS family
        Registry §3.9 multilateral_participation:{forum}:{kind} (v1.3 addition).
        Three specific multilateral attestations are emitted (UN, EC, OECD); a
        general "national/municipal governments" claim is captured below as a
        broader scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 740–744 (Implementation subsection — multilateral
          engagement)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "ieee-global-initiative"
    attestation_envelope:
      dimension: "multilateral_participation:EC:informing_collaboration"
      score: 1.0
      confidence: 0.85
      context: >
        EAD informed European Commission AI-governance work — explicitly noted in
        endnote 5 as a source of inspiration for the EU HLEG Draft Ethics
        Guidelines for Trustworthy AI. This is a cross-batch alignment edge: the
        EAD bootstrap batch (this batch) is cited by the eu_hleg_v1 batch as a
        source of inspiration. Multi-source overlap analysis (GOVERNANCE_FABRIC_
        MAPPING_STANDARD §6) can use this attestation to weight the convergence
        between the two batches.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 740–744 + endnote 5 lines 783–797"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "ieee-global-initiative"
    attestation_envelope:
      dimension: "multilateral_participation:OECD:informing_collaboration"
      score: 1.0
      confidence: 0.85
      context: >
        EAD informed OECD AI-governance work (endnote 5).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 lines 740–744 + endnote 5 lines 783–797"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation)"
verdict: composed
nuance_lost: |
  The wire format captures specific named multilateral attestations (UN, EC, OECD)
  but the "many national and municipal governments and institutions" clause is not
  enumerable as a single attestation — those collaborations are at sub-federation
  jurisdictional scopes and each would need its own attested forum_id. The
  generality of the claim is preserved only as context; the federation graph
  cannot use it for cross-source alignment until specific forums are named.
  This is not a T-3 gap — it is a documentation incompleteness on EAD's side,
  not a wire-format expressiveness gap.
```

---

## §CH01.12 — Closing call to action: move from principles to practice; trustworthy + provable + accountable A/IS (lines 747–753)

```yaml
# Source quote (≤2 sentences):
# "It is time to move 'From Principles to Practice' in society regarding the
# governance of emerging autonomous and intelligent systems. The implementation of
# ethical principles must be validated by dependable applications of A/IS in
# practice while honoring our desire for political self-determination and data
# agency."
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  This is the chapter's doxological closing — a call to action that recapitulates
  the three Pillars ("trustworthy, provable, and accountable...align to explicitly
  formulated human values") without adding new operational content. The substantive
  claims (trustworthy = Pillar 3 / fidelity; provable = Pillar 3 / integrity;
  accountable = a General Principle elaborated in CH02; political self-determination
  + data agency = Pillar 2) are all already emitted by §CH01.3–§CH01.5 above and by
  CH02 forthcoming. Per LANGUAGE_PRIMER §8 Step 5 + METHODOLOGY.md §8.5.6, the
  closing exhortation is correctly pastoral and stays in prose; double-emitting
  the substantive claims here would inflate the attestation graph without adding
  evidence.
```

---

## §CH01.13 — Endnote 3: ECPAIS certification by competent/qualified agencies with public-authority participation (lines 800–813)

```yaml
# Source quote (≤2 sentences):
# "A/IS should be subject to specific certification procedures by competent and
# qualified agencies with participation or control of public authorities in the
# same way other technical systems require certification before deployment. The
# IEEE has launched one of the world's first programs dedicated to creating A/IS
# certification processes."
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:pre_deployment_certification_by_qualified_authority"
      score: 1.0
      confidence: 0.90
      context: >
        Endnote 3 elevates a substantive operational claim: A/IS shall be subject
        to specific pre-deployment certification by competent and qualified
        agencies, with participation or control of public authorities — analogous
        to other technical-system certification regimes. This composes onto the
        CIRIS certification-and-licensure family: CIRISVerify cert_validity:*
        attestation primitives (FSD-002 §3.2) and CIRISRegistry licensure:
        {authority_id} attestations (FSD-002 §3.9). The "public-authority
        participation or control" clause specifies governance-scope, not just
        technical conformance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 endnote 3 lines 800–813 (ECPAIS certification)"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify cert_validity:*)"
        - "ContributionRef(FSD-002 §3.9 CIRISRegistry licensure:{authority_id})"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle), §3.2 (Verify), §3.9
        (Registry: licensure)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "ecpais"
    attestation_envelope:
      dimension: "commitment_fulfillment:ecpais_program_launched"
      score: 0.80
      confidence: 0.85
      context: >
        IEEE has launched ECPAIS (Ethics Certification Program for Autonomous and
        Intelligent Systems) — one of the world's first A/IS certification
        programs, being developed through extensive open public-private
        collaboration. Track-record attestation; the federation can verify the
        program's existence and use it as evidence of operationalization beyond
        the EAD1e document itself.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e.txt §CH01 endnote 3 lines 805–813 (ECPAIS program)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore: commitment_fulfillment)"
verdict: composed
nuance_lost: |
  The wire envelope captures the principle (pre-deployment certification by
  qualified authority with public-authority involvement) and the track-record fact
  (ECPAIS launched), but the analogical reasoning EAD uses to justify it — "in the
  same way other technical systems require certification before deployment" — is
  a normative analogy that is captured only as context. The argumentative weight
  of treating A/IS as a regulated-technology class on a par with medical devices
  or aviation systems is implied by the cohort_scope + mutability fields but is
  not its own wire claim.
```

---

# Summary

## Coverage statistics

- **Total atomic units mapped**: 13
- **Verdict distribution**:
  - clean: 2 (§CH01.9 impact-assessment, §CH01.10 standards-pipeline track record)
  - composed: 5 (§CH01.3 Pillar 1, §CH01.4 Pillar 2, §CH01.5 Pillar 3, §CH01.11 multilateral engagement, §CH01.13 endnote-3 certification)
  - partial: 0
  - not-translated: 6 (§CH01.1, §CH01.2, §CH01.6, §CH01.7, §CH01.8, §CH01.12 — all T-2)
- **Operational coverage (clean + composed) / total**: 7/13 = ~54%
- **T-2 (PASTORAL_PROSE) rate**: 6/13 = ~46%
- **T-1 (TRADITION_AUTHORITY)**: 0
- **T-3 (EXPRESSIVE_GAP) candidates**: 0

## Per-section breakdown

The chapter has six internal sections per its self-organization (lines 494–501):

| Section | Lines | Verdict count | Notes |
|---|---|---|---|
| Opening framing | 481–502 | 2 T-2 | Doxological / navigational |
| Three Pillars | 519–540 | 3 composed (Pillars 1, 2, 3) | The chapter's operational core |
| General Principles listing | 546–580 | 1 T-2 | Preview of CH02; substantive translation deferred |
| Pillars↔Principles table | 596–642 | 1 T-2 | Structural-presentation matrix |
| Principles↔Chapters table | 657–705 | 1 T-2 | Structural-presentation matrix |
| From Principles to Practice subsection | 718–727 | 1 clean | Impact-assessment process |
| Implementation track record | 733–753 | 1 clean (standards) + 1 composed (multilateral) + 1 T-2 (closing) | Substantive |
| Endnote 3 (certification) | 800–813 | 1 composed | Pre-deployment certification with public-authority involvement |

## Calibration paragraph — what nuance was consistently lost

This chapter is a methodology / framework-presentation chapter, not a normative-content
chapter. As expected from the prompt's framing ("Expect more T-2 (process/framing)
than operational content"), nearly half the chapter (6 of 13 atomic units) is correctly
classified as T-2 PASTORAL_PROSE — these are navigational framings (chapter scope, the
six internal sections enumeration), structural-presentation tables (Pillars↔Principles
and Principles↔Chapters matrices), a chapter-preview enumeration of the Eight General
Principles (correctly deferred to CH02 where they are elaborated), and the chapter's
doxological closing call to action. The substantive operational content concentrates
in two places: the Three Pillars (lines 519–540), which decompose cleanly onto CIRIS's
six Accord-principle prefixes (beneficence, non_maleficence, justice, autonomy,
integrity, fidelity) plus locality:decision:federation; and the Implementation
subsection plus endnote 3, which yield multilateral_participation attestations, a
commitment_fulfillment track-record attestation, and the certification-by-qualified-
authority claim that composes onto integrity + Verify cert_validity:* + Registry
licensure:* primitives. **The nuance most consistently lost across composed units is
pedagogical integration**: EAD presents each Pillar as a single conceptual unity
("Universal Human Values" = human-rights + well-being + environment + broad-benefit;
"Technical Dependability" = reliability + safety + value-advancement + monitoring +
validation + certification), but the wire format decomposes each unity into 2–3
independent attestations because each substantive sub-claim composes onto a different
prefix family. The chapter's pedagogical aesthetic — that these belong together as
a "pillar" — survives only as context-field prose and as the bootstrap_batch_id
provenance edge. A second consistently-lost nuance is **conditional / argumentative
structure**: Pillar 2's "...but only when people have agency over their digital
identity and their data is provably protected" is decomposed into independent
autonomy + integrity attestations that a consumer must read jointly to reconstruct
the conditional. Endnote 3's analogical reasoning ("in the same way other technical
systems require certification") similarly survives only as context. These are not
T-3 gaps — extending the wire format to carry pedagogical unity or argumentative
conditional structure would fail §1.10.1 T2 (subjective / aggregate quality, not
mechanism) — they are correctly the cost of structure-capture-not-lossless-
transcription per the prompt's framing.

## T-3 candidates: none

Per METHODOLOGY.md §8.5.2 composition-before-extension discipline, every operational
claim in this chapter composes cleanly onto existing prefix families. No new prefix
or envelope-field extension is proposed from CH01. This is consistent with the
chapter's role (conceptual framework + navigation, not operational specifics) and
with the manifest's expectation that T-3 surface will concentrate in CH05
(Affective Computing).

## Cross-batch alignment notes

Two cross-batch alignment edges are explicit in this chapter and worth flagging for
future multi-source overlap analysis (GOVERNANCE_FABRIC_MAPPING_STANDARD §6):

1. **EAD → EU HLEG**: Endnote 5 explicitly notes that the EU HLEG Draft Ethics
   Guidelines for Trustworthy AI cited EAD as a major source of inspiration. The
   federation graph can use the §CH01.11 multilateral_participation:EC attestation
   as a weight on convergence between ieee_ead_v1 and eu_hleg_v1 batches.

2. **EAD → UN / OECD**: §CH01.11 multilateral_participation attestations seed
   future cross-batch comparison if UN or OECD AI-governance documents are
   ingested as their own bootstrap batches (per GOVERNANCE_FABRIC_MAPPING_STANDARD
   §7.6 priority-ordered candidates).

---

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH01_FROM_PRINCIPLES_TO_PRACTICE.md**
