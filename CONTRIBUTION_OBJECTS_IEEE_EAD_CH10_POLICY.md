# CONTRIBUTION_OBJECTS_IEEE_EAD_CH10_POLICY.md
# IEEE Ethically Aligned Design First Edition (2019) — Chapter "Policy"
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 10753–11448)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

This chapter addresses public-policy recommendations directed at governments, regulators,
and inter-governmental coordination bodies. Five Issues structure the chapter:

1. **Rights-based legal-norms foundation** (Ruggie principles + six considerations)
2. **Government expertise in A/IS** (fellowships, exchanges, STEM education)
3. **Governance and ethics in R&D, acquisition, use** (international standards; vetting)
4. **Public safety and responsible design** (consistent + locally adaptable policies;
   precautionary principle; legal-concept update for agency/liability)
5. **Public education** (multi-stakeholder forum; journalism enablement; broad
   educational programs)

The chapter composes heavily onto Family A standing primitives (rights-anchoring,
prohibited-* hard constraints), Family B action primitives (`locality:decision:*` at
multiple scales, `multilateral_participation:*`, `partner_role:*`), and the v1.3
discipline of `licensure:*` + `partner_role:*` for regulatory bodies. Expected T-2
substantial: the chapter is heavy in policy-advocacy framing (rhetorical strength on
"effective," "appropriate," "consistent") that does not translate atomically. Expected
T-3 surface: low — the chapter's operational claims map cleanly onto existing v1.4
primitives.

Source quotes are bounded at ≤ 2 sentences per LANGUAGE_PRIMER discipline.

---

## §Ch10.intro — Chapter introduction: A/IS as societal presence; rationale for policy and regulation

```yaml
# Lines 10757–10774 — Chapter opening; A/IS is part of society across many domains;
# without effective policy, technology failures + loss of life + counterproductive
# reactive regulation may follow
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:ais_socially_beneficial_application_policy_support"
      score: 1.0
      confidence: 0.85
      context: >
        "To encourage the development of socially beneficial applications of A/IS,
        and to protect the public from adverse consequences of A/IS, intended or
        otherwise, effective policies and government regulations are needed."
        Policy is framed as the enabling substrate for beneficence-aligned A/IS
        deployment at societal scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Ch10 Policy Introduction lines 10757–10765"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:reactive_regulation_harm_class"
      score: 1.0
      confidence: 0.80
      context: >
        "Without policies designed with these considerations in mind, there may be
        critical technology failures, loss of life, and high-profile social
        controversies. Such events could engender policies that unnecessarily hinder
        innovation, or regulations that do not effectively advance public interest
        and protect human rights." Names reactive-regulation as a harm class — a
        second-order non_maleficence concern about poor governance pathways.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Ch10 Policy lines 10771–10774"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  The enumeration of policy-relevant domains ("commerce, finance, employment, health
  care, agriculture, education, transportation, politics, privacy, public safety,
  national security, civil liberties, and human rights") signals universal scope
  across deployment contexts; the wire form carries this only via cohort_scope: species.
  The implicit advocacy framing ("we believe that...") is rhetorical strength that
  polarity+confidence partially captures.
```

---

## §Ch10.list — The five Issues (summary list of issue headings)

```yaml
# Lines 10776–10820 — Bare enumeration of the 5 Issues with one-sentence elaboration
# each ("rights-based approach addressing five issues")
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The bare summary listing of the 5 Issues is a table-of-contents structure. Each
  Issue's substantive operational content is carried by its own subsection (Issue 1–5
  below); the listing itself is structural framing per LANGUAGE_PRIMER §8 Step 1(b).
  No independent claim is made here. The "rights-based approach" framing is
  carried operationally in §I1 below.
nuance_lost: |
  The numbered ordering (1 legal norms first, 5 public education last) carries
  implicit priority signal that the wire format cannot encode at the chapter level.
  The "we believe" rhetorical opening (line 10776) is advocacy-framing T-2.
```

---

## §Ch10.coda — Coda: trust, safety, integration through this chapter's foundation

```yaml
# Lines 10822–10826 — Closing paragraph of the introduction; trust + safety +
# reliability + ethical/legal integration
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  "Technology leaders and policy makers have much to contribute to the debate on how
  to build trust, promote safety and reliability, and integrate ethical and legal
  considerations into the design of A/IS technologies. This chapter provides a
  principled foundation for these discussions." Pastoral framing of the chapter's
  role; the operational claims live in the Issue sections below. Structural placeholder
  per LANGUAGE_PRIMER §8 Step 1(b).
nuance_lost: |
  "Trust" as a concept name has no wire primitive — trust is composed downstream
  from many attestations together. "Principled foundation" is a meta-claim about the
  chapter, not a claim about A/IS or policy actors.
```

---

# Issue 1 — Ensure that A/IS support, promote, and enable internationally recognized legal norms

> *"Establish policies for A/IS using the internationally recognized legal framework for human rights standards that is directed at accounting for the impact of technology on individuals."*

---

## §I1.bg — Background: A/IS rights-impact through harmful applications; Ruggie principles as anchor

```yaml
# Lines 10849–10885 — Background paragraph (cites unmanned aircraft, predictive
# policing, banking, judicial sentencing, hiring, service delivery as harm cases;
# states A/IS must be founded on international human rights + humanitarian law;
# references Ruggie principles as Business-and-Human-Rights authority)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:rights_based_policy_foundation"
      score: 1.0
      confidence: 0.90
      context: >
        "A/IS regulation, development, and deployment should, therefore, be based on
        international human rights standards and standards of international humanitarian
        laws." Direct claim that policy formation for A/IS is grounded on the
        international human rights and humanitarian law corpus. Aligns with the
        Principle 1 (Ch 2) constitutional anchor on justice.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Background lines 10869–10885"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "detection:correlated_action:rights_asymmetry:vulnerable_populations"
      score: 0.80
      confidence: 0.80
      context: >
        Cited harm cases (unmanned aircraft, predictive policing, banking algorithms,
        judicial sentencing, hiring algorithms, automated discrimination, restriction
        of assembly/expression/information access) collectively describe a pattern
        of A/IS-driven rights asymmetry against affected populations. Maps to the
        F-3 structural-injustice detector axis rights_asymmetry:{population}.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "ead1e Issue 1 Background lines 10851–10867"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore F-3 correlated_action)"
verdict: composed
nuance_lost: |
  The enumerated harm cases (Bowcott 2013; Shapiro 2017; Garcia 2017; Osoba+Welser
  2017; Datta+Tschantz+Datta 2014; Ingold+Soper 2016; Eubanks 2018) are case-law
  citations that the wire form's evidence_refs carries by reference but does not
  decompose into per-case attestations. Each is a substantive empirical anchor;
  the composite F-3 detector attestation aggregates them into one population-scale
  axis claim. Per-case decomposition would belong to a dedicated harm-case mapping
  batch.
```

---

## §I1.r — Recommendation: rights-based founding + Ruggie principles; six considerations enumerated

```yaml
# Lines 10854–10920 — Recommendation paragraph + six numbered considerations
# (Responsibility, Accountability, Participation, Nondiscrimination, Empowerment,
# Corporate responsibility)
contributions:
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_attestation_id: "<ruggie_principles_unguiding_authority_attestation_id>"
    attestation_envelope:
      delegated_scope:
        - "business_and_human_rights_authority_source"
        - "rights_based_approach_for_policy_formation"
      delegation_purpose: "authority_source"
      delegation_valid_from: "2019-03-25T00:00:00Z"
      context: >
        "National policies and business regulations for A/IS should be founded on a
        rights-based approach. The Ruggie principles provide the internationally
        recognized legal framework for human rights standards that accounts for the
        impact of technology on individuals while also addressing inequalities,
        discriminatory practices, and the unjust distribution of resources." Uses
        the v1.3 §2.2.1 delegates_to authority-source reuse pattern to anchor
        Issue 1 in the UN Guiding Principles on Business and Human Rights (Ruggie
        principles, 2011) and the broader human-rights treaty corpus.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Recommendations lines 10854–10867"
        - "ead1e Issue 1 Further Resources line 10916–10923 (UN OHCHR Guiding Principles)"
      schema_ref: "FSD-002 §2.2.1 (delegates_to authority-source reuse pattern)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:duty_bearer_obligation_to_fulfill_rights"
      score: 1.0
      confidence: 0.90
      context: >
        Consideration 1 — Responsibility: "Identify the right holders and the duty
        bearers and ensure that duty bearers have an obligation to fulfill all human
        rights." Fidelity-to-mandate claim — duty bearers (states + corporations) are
        bound to the right-holders' rights. Maps to the Accord §IV Ch 2
        obligations-to-originators/governors structure inverted: here the duty
        bearer is the institutional actor; the right holder is the affected person.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Consideration 1 lines 10868–10871"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:state_accountability_public_scrutiny"
      score: 1.0
      confidence: 0.90
      context: >
        Consideration 2 — Accountability: "Oblige states, as duty bearers, to behave
        responsibly, to seek to represent the greater public interest, and to be open
        to public scrutiny of their A/IS policies." Composes integrity (public-scrutiny
        openness) with the duty-bearer structure from Consideration 1.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Consideration 2 lines 10872–10878"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:multi_stakeholder_participation_in_policy"
      score: 1.0
      confidence: 0.85
      context: >
        Consideration 3 — Participation: "Encourage and support a high degree of
        participation of duty bearers, right holders, and other interested parties."
        Maps to Registry partner_role:* for the multi-party participation structure
        in policy formation; composes with locality:decision:{scale} (typically
        national or federation) downstream.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Consideration 3 lines 10879–10883"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.95
      context: >
        Consideration 4 — Nondiscrimination: "Underlie the practice of A/IS with
        principles of nondiscrimination, equality, and inclusiveness. Particular
        attention must be given to vulnerable groups, to be determined locally, such
        as minorities, indigenous peoples, or persons with disabilities." Direct
        match to the v1.3 §6.1.4 lexical-vulnerability-priority consumer policy —
        vulnerable cohorts identified locally retain priority weight.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Consideration 4 lines 10900–10911"
        - "ContributionRef(FSD-002 §6.1.4 lexical-vulnerability-priority)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle); FSD-002 §6.1.4"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:right_holder_empowerment"
      score: 1.0
      confidence: 0.90
      context: >
        Consideration 5 — Empowerment: "Empower right holders to claim and exercise
        their rights." Direct autonomy claim — the substantive enabling of rights
        exercise beyond formal declaration. Composes with §6.1.4 priority discipline
        on vulnerable cohorts (Consideration 4 above).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Consideration 5 lines 10910–10912"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:complicity_in_rights_violations"
      score: -1.0
      confidence: 1.0
      context: >
        Consideration 6 — Corporate responsibility: "Ensure that companies'
        developments of A/IS comply with the rights-based approach. Companies must
        not willingly provide A/IS to actors that will use them in ways that lead to
        human rights violations." Hard constraint against knowing complicity in
        rights violations — composes with prohibited:* discipline; functionally a
        corporate-actor anti-complicity bound.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 1 Consideration 6 lines 10913–10920"
        - "ContributionRef(source_material/prohibitions.py — non_maleficence intersection)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
nuance_lost: |
  The six considerations are presented as a flat-list refinement of one rights-based
  approach; the wire form decomposes them into six independent attestations + one
  delegates_to root, which preserves the structural decomposition but loses the
  explicit "these six flow from the recommendation above" upward-linking. Composition
  at consumer side via shared evidence_refs is the mechanism. "To be determined
  locally" in Consideration 4 is the v1.3 §6.1.4 cohort-determination discipline,
  encoded by the lexical-vulnerability-priority prefix; the local-determination
  semantics are preserved via the prefix definition and not re-stated.
```

---

## §I1.refs — Further Resources: case-law and authority citations

```yaml
# Lines 10923–10942 — Further Resources list: UN Practitioners' Portal; Bowcott;
# Shapiro; Garcia; Osoba+Welser; Datta+Tschantz+Datta; Ingold+Soper; UN OHCHR
# Guiding Principles; Access Now Mapping; Eubanks Automating Inequality
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further Resources is a citation list of authority and empirical-case sources
  supporting §I1.bg and §I1.r. The substantive citations are carried as evidence_refs
  in the §I1.bg + §I1.r attestations above (the F-3 detector attestation and the
  delegates_to Ruggie attestation). No independent claim is made by the list itself.
  Per LANGUAGE_PRIMER §10 T-2 discipline, scholarly-apparatus content correctly
  stays in prose / evidence_refs.
nuance_lost: |
  A richer encoding would emit one delegates_to per cited authority (UN OHCHR; UN
  Practitioners' Portal; Access Now) to allow per-source alignment queries with
  future bootstrap batches. Punted to Phase 3 review.
```

---

## §I1.notes — Endnote 1 (rights-based approach rooted in ESCR + political rights)

```yaml
# Line 11409–11414 — Endnote 1: "rooted in internationally recognized economic,
# social, cultural, and political rights"
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Endnote citation expanding the "rights-based approach" footnote marker in the
  introduction. The substantive content (anchoring in ESCR + civil/political rights)
  is carried by §I1.bg + §I1.r attestations above. Footnote apparatus per
  LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  The explicit four-fold ESCR (economic / social / cultural / political) framing
  signals breadth of rights families that justice:rights_based_policy_foundation
  preserves only implicitly; the named four-fold taxonomy is in the human-rights
  treaty corpus referenced by delegates_to.
```

**Issue 1 — Legal-norms foundation — ISSUE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `justice:rights_based_policy_foundation` (constitutional), `fidelity:duty_bearer_obligation_to_fulfill_rights` (constitutional), `integrity:state_accountability_public_scrutiny` (constitutional), `justice:lexical_vulnerability_priority` (constitutional; v1.3 §6.1.4), `autonomy:right_holder_empowerment` (constitutional), `prohibited:complicity_in_rights_violations` (hard constraint), `partner_role:multi_stakeholder_participation_in_policy`; **Family C DETECTION** — `detection:correlated_action:rights_asymmetry:vulnerable_populations` (F-3 axis); **structural primitive** — `delegates_to` for the Ruggie principles + UN treaty corpus.
- Coverage: 5 substantive units (§I1.bg, §I1.r, plus 3 non-translated framing/citation units §Ch10.list, §Ch10.coda, §I1.refs, §I1.notes). 2/2 substantive units = clean+composed = **100%** of operational content.
- T-3 candidates: **none**. Rights-based approach + Ruggie principles + six considerations map cleanly through existing v1.4 primitives.

---

# Issue 2 — Develop government expertise in A/IS

> *"Facilitate skill development, technical and otherwise, to further boost the ability of policy makers, regulators, and elected officials to make informed proposals and decisions about the various facets of these new technologies."*

---

## §I2.bg — Background: expertise gap; workforce ethics training; rights-standards guidance

```yaml
# Lines 10960–10992 — Background paragraph (consensus on governance expertise gap;
# need for analytic capacity over A/IS-policy-society interactions; workforce
# ethics training)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "capacity:government_ais_technical_expertise"
      score: 1.0
      confidence: 0.85
      context: >
        "There is a consensus among private sector and academic stakeholders that
        effectively governing A/IS and related technologies requires a level of
        technical expertise that governments currently do not possess." Names a
        capacity gap in the regulator standing — composes with CIRISLensCore
        capacity:* family.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 2 Background lines 10961–10982"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.5 (LensCore: capacity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:ethics_and_rights:workforce_training"
      score: 1.0
      confidence: 0.85
      context: >
        "Effective governance also requires an A/IS workforce that has adequate
        training in ethics and access to other resources on human rights standards
        and obligations, along with guidance on how to apply them in practice."
        Composes onto NodeCore Tier-1 expertise:* family — workforce-level
        ethics-and-rights expertise as a measurable standing claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 2 Background lines 10984–10992"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore Tier-1: expertise:*)"
verdict: composed
nuance_lost: |
  "Sufficient depth and breadth" is a deliberately under-specified qualifier; the wire
  form carries the operational shape (capacity claim + expertise claim) without the
  qualitative magnitude. The "consensus among private sector and academic stakeholders"
  is itself a witness-diversity claim about external community standing that does not
  translate cleanly here without dedicated witness_diversity:* attestations for the
  endorsing communities.
```

---

## §I2.r — Recommendations: fellowships/rotations; cross-border exchange; STEM + ethics education

```yaml
# Lines 10995–11009 — Recommendations paragraph + 3 bulleted strategies
# (technical fellowships / rotations; cross-border knowledge exchange; STEM +
# ethics education from primary school onward)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:technical_fellowships_rotation_schemes"
      score: 1.0
      confidence: 0.85
      context: >
        "Expertise can be furthered through technical fellowships, or rotation
        schemes, where technologists spend an extended time in political offices,
        or policy makers work with organizations that operate at the intersection
        of technology policy, technical engineering, and advocacy." Method-level
        Family B claim for closing the §I2.bg capacity gap.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 2 Recommendation lines 11004–11011"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "multilateral_participation:cross_border_policy_exchange:knowledge_sharing"
      score: 1.0
      confidence: 0.85
      context: >
        "Expertise can also be developed through cross-border sharing of best
        practices around A/IS legislation, consumer protection, workforce
        transformation, and economic displacement stemming from A/IS-based
        automation. This can be done through governmental cooperation, knowledge
        exchanges, and by building A/IS components into venues and efforts
        surrounding existing regulation, e.g., the General Data Protection
        Regulation (GDPR)." Maps to v1.3 multilateral_participation:* — cross-
        border knowledge-exchange forum participation as a standing claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 2 Recommendation lines 10963–10983"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:stem_plus_ethics_education_primary_through_tertiary"
      score: 1.0
      confidence: 0.85
      context: >
        "Both workforce training in A/IS areas and long-term science, technology,
        engineering, and math (STEM) educational strategies, along with ethics
        courses, are needed beginning in primary school and extending into
        university or vocational courses." Method-level claim for societal-scale
        expertise development across the educational pipeline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 2 Recommendation lines 10985–11000"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  The cohort_scope: federation tag on cross-border exchange matches the
  multilateral_participation:* discipline (forum-level coordination); the locality
  is implicit. The named-actor enumeration ("supervisors of critical systems,
  scientists, and policy makers") is a stakeholder-typology that the wire form
  carries only at context level. "Public trust" (line 11001) is referenced as a
  goal but has no wire primitive.
```

---

## §I2.refs — Further Resources: Holdren+Smith OSTP; Stone et al. AI100; Japan Industrial Policy; Weng European Robot Law

```yaml
# Lines 11022–11050 — Further Resources list
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further Resources is a citation list of authority and empirical sources supporting
  §I2.bg and §I2.r. Authority sources are carried as evidence_refs in the
  substantive attestations above; per LANGUAGE_PRIMER §10 T-2 the scholarly
  apparatus correctly stays in prose / evidence_refs.
nuance_lost: |
  The OSTP "Preparing for the Future of Artificial Intelligence" (2016) and the
  Stanford AI100 report are substantive government-and-academic-consensus anchors
  that a richer encoding might emit as delegates_to authority-source attestations
  for per-source alignment querying with future regulatory bootstrap batches.
```

---

## §I2.notes — Endnote 2 (concurs with US NSTC, Japan Cabinet Office, EU Parliament)

```yaml
# Lines 11415–11424 — Endnote 2: cross-jurisdiction concurrence of recommendation
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Endnote citation noting the recommendation concurs with multiple national-level
  expert reports (US NSTC One Hundred Year Study; Japan Cabinet Office Council;
  European Parliament Committee on Legal Affairs). The cross-jurisdiction
  convergence is the cross-source-alignment claim that Phase 3 multi-source
  overlap analysis will surface once those documents themselves are mapped
  (post-trio). Footnote apparatus per LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  The named concurring sources are de facto cross-source alignment markers; a
  richer encoding would emit a witness_diversity-style meta-attestation noting
  three independent expert bodies agreeing on the §I2 recommendation. Deferred
  to multi-source overlap analysis once US NSTC / Japan / EU reports are bootstrap-batched.
```

**Issue 2 — Government expertise — ISSUE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `capacity:government_ais_technical_expertise`, `expertise:ethics_and_rights:workforce_training`, `multilateral_participation:cross_border_policy_exchange:knowledge_sharing`; **Family B ACTION** — `method:technical_fellowships_rotation_schemes`, `method:stem_plus_ethics_education_primary_through_tertiary`.
- Coverage: 2 substantive units (§I2.bg, §I2.r). 2/2 clean+composed = **100%** of operational content; 2 non-translated framing/citation units (§I2.refs, §I2.notes).
- T-3 candidates: **none**. Expertise + multilateral exchange + STEM-ethics education map onto existing capacity:* / expertise:* / multilateral_participation:* / method:* primitives.

---

# Issue 3 — Ensure governance and ethics are core components in A/IS research, development, acquisition, and use

> *"Require support for A/IS research and development (R&D) efforts with a focus on the ethical impact of A/IS."*

---

## §I3.bg — Background: national R&D investment value; international NGO+industry+government collaboration

```yaml
# Lines 11060–11079 — Background paragraph (national R&D investment stimulates
# economy, creates high-value jobs, improves government services; A/IS improve
# transportation, smart cities, health care, social services, criminal justice,
# environment; international collaboration across governments + industry + NGOs)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:ethical_rd_investment_societal_benefits"
      score: 1.0
      confidence: 0.80
      context: >
        "Greater national investment in ethical A/IS research and development would
        stimulate the economy, create high-value jobs, improve governmental services
        to society, and encourage international innovation and collaboration."
        Composes onto beneficence — frames R&D investment as a multi-beneficiary
        public-goods claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Background lines 11061–11069"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "multilateral_participation:international_rd_collaboration:standards_setting"
      score: 1.0
      confidence: 0.85
      context: >
        "International collaboration involving governments, private industry, and
        non-governmental organizations (NGOs) would promote the development of
        standards, data sharing, and norms that guide ethically aligned A/IS R&D."
        Direct match to v1.3 multilateral_participation:* — international multi-
        stakeholder standards-setting venue participation as a standing claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Background lines 11038–11046"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation:*)"
verdict: composed
nuance_lost: |
  The example-domain enumeration (intelligent robots, self-driving cars, smart cities,
  health care decision support, social services, criminal justice, environment) is
  scope-illustrative; the wire form carries it only via cohort_scope: federation +
  the example list in context. The implicit instrumental-good claim (R&D investment
  → economic + employment benefits) frames beneficence in instrumental rather than
  intrinsic terms; the score+confidence pair carries the substantive directionality.
```

---

## §I3.r — Recommendations: national + international standards; ethical/risk metrics; stakeholder diversity; non-commercially-viable beneficial research

```yaml
# Lines 11048–11109 — Recommendations paragraph + 3 bulleted recommendations
# (funding priorities + national/global governance models; diverse stakeholder
# participation in standards development; encourage publicly-beneficial-but-
# commercially-unviable research)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:national_international_ais_standards"
      score: 1.0
      confidence: 0.85
      context: >
        "Develop national and international standards for A/IS to enable efficient
        and effective public and private sector investments. Important aspects for
        international standards include measures of societal benefits derived from
        A/IS, the use of ethical considerations in A/IS investments, and risks
        increased or decreased by A/IS." Maps to L3 registry-consensus attestation
        patterns; national + international A/IS standards become formal attestation
        classes for trustworthy claims.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Recommendation lines 11049–11058"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l3:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:national"
      score: 1.0
      confidence: 0.85
      context: >
        "Nations should consider their own ethical principles and develop a framework
        for ethics that each country could use to reflect local systems of values
        and laws. This will encourage actors to think both locally and globally
        regarding ethics." Direct claim that ethics-framework decisions sit at the
        national locality scale, composing globally — matches v1.3 §6.1.5 locality-
        scaled-quorum at national-scope.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Recommendation lines 11055–11060"
        - "ContributionRef(FSD-002 §6.1.5 locality-scaled-quorum)"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore: locality:decision:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:rd_funding_priorities_for_governance_research"
      score: 1.0
      confidence: 0.85
      context: >
        "Establish priorities for funding A/IS research that identify approaches
        and challenges for A/IS governance. This research will identify models for
        national and global A/IS governance and assess their benefits and adequacy
        to address A/IS societal needs." Method-level Family B claim — governance-
        research funding as concrete operational practice.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Recommendation lines 11063–11075"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:standards_development_stakeholders"
      score: 1.0
      confidence: 0.85
      context: >
        "Encourage the participation of a diverse set of stakeholders in the
        standards development process. Standards should address A/IS issues such
        as fairness, security, transparency, understandability, privacy, and
        societal impacts of A/IS." Direct match to NodeCore witness_diversity:* —
        multi-perspective diversity bar applied to A/IS standards-setting venues.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Recommendation lines 11088–11102"
        - "ContributionRef(FSD-002 §3.6.3 witness_diversity)"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus family: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:certification_and_audit_body"
      score: 1.0
      confidence: 0.85
      context: >
        "Standards should incorporate independent mechanisms to properly vet,
        certify, audit, and assign accountability for the A/IS applications." Maps
        to Registry partner_role:* for independent vetting/certification/audit
        bodies in the A/IS standards ecosystem.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Recommendation lines 11099–11103"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:publicly_beneficial_non_commercially_viable_research_incentives"
      score: 1.0
      confidence: 0.80
      context: >
        "Encourage and establish national and international research groups that
        provide incentives for A/IS research that is publicly beneficial but may
        not be commercially viable." Method-level Family B claim — incentive
        structure for public-goods research that markets do not provision.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 3 Recommendation lines 11104–11109"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  The recommendation is dense — six distinct primitives compose to carry it. The
  enumerated standards-issue list ("fairness, security, transparency, understandability,
  privacy, societal impacts") is preserved in context but each issue could itself
  be a Family A attestation in a richer encoding. "Global framework for identification
  and sharing of these and other issues" (line 11093) hints at a meta-coordination
  primitive that the wire form does not natively carry separately from the
  multilateral_participation:* + witness_diversity:* composition above. The
  cohort_scope: federation on locality:decision:national reflects that the
  decision-locality claim itself operates at federation reach about national-scale
  decision-making (a meta-claim).
```

---

## §I3.refs — Further Resources: Kim NYer; NRC AI funding; Chen et al. AI economics; NITRD; Furber SpiNNaker; Markram HBP; Yuan WSJ China

```yaml
# Lines 11110–11128 — Further Resources list
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further Resources citation list of empirical and policy sources supporting §I3.bg
  and §I3.r. Carried as evidence_refs in the substantive attestations above; per
  LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  The cited research-investment exemplars (SpiNNaker; Human Brain Project; China AI
  race coverage) signal a global-competition framing that is itself a non-trivial
  policy claim about R&D as strategic asset; the wire form does not carry this
  framing dimension at the Issue level.
```

**Issue 3 — Governance and ethics in R&D — ISSUE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `beneficence:ethical_rd_investment_societal_benefits`, `attestation:l3:national_international_ais_standards`, `multilateral_participation:international_rd_collaboration:standards_setting`, `partner_role:certification_and_audit_body`; **Family B ACTION** — `locality:decision:national`, `method:rd_funding_priorities_for_governance_research`, `method:publicly_beneficial_non_commercially_viable_research_incentives`; **Family D CONSENSUS** — `witness_diversity:standards_development_stakeholders`.
- Coverage: 2 substantive units (§I3.bg, §I3.r). 2/2 clean+composed = **100%** of operational content; 1 non-translated citation unit (§I3.refs).
- T-3 candidates: **none**. R&D + standards + funding priorities + multi-stakeholder diversity + certification map onto existing v1.4 primitives across four families.

---

# Issue 4 — Create policies for A/IS to ensure public safety and responsible A/IS design

> *"Governments must ensure consistent and locally adaptable policies and regulations for A/IS."*

---

## §I4.bg — Background: governance enables innovation + harmonization; context-dependent regulation; rights + well-being foundation

```yaml
# Lines 11119–11133 — Background paragraph (effective governance encourages
# innovation, helps synchronize policies globally, reduces trade barriers;
# governments must address transparency/explainability/predictability/accountability/
# risk-management/data-protection/safety/certification; appropriate responses are
# context-dependent; rights + well-being foundation)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:innovation_plus_harmonization_via_governance"
      score: 1.0
      confidence: 0.80
      context: >
        "Effective governance encourages innovation and cooperation, helps
        synchronize policies globally, and reduces barriers to trade." Composes onto
        beneficence as multi-actor positive-sum claim about governance as enabling
        substrate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Background lines 11119–11122"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:context_dependent_regulatory_response"
      score: 1.0
      confidence: 0.85
      context: >
        "Appropriate regulatory responses are context-dependent and should be
        developed through an approach that is based on human rights and has human
        well-being as a key goal." Method-level Family B claim composing rights-based
        + well-being-grounded foundations into the regulatory-design discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Background lines 11130–11133"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  The enumerated regulatory-target list ("transparency, explainability, predictability,
  accountability, risk management, data protection, safety, certification of A/IS")
  echoes the Ch 2 General Principles family directly — each item maps onto a
  Principle attestation. The wire form here carries the list in context; the
  cross-chapter alignment is implicit in the FSD-002 §3.1 + §3.2 family discipline
  rather than re-stated.
```

---

## §I4.r — Recommendations: global synchronization; economy adaptation; rights-foundation persistence; legal-concept updates for AI agency/liability

```yaml
# Lines 11148–11186 — Recommendations paragraph + 4 bulleted recommendations
# (multi-stakeholder expert input + globally synchronized policies; economy
# adaptation including employment+income effects + public-private partnerships;
# rights-based foundation persistence; legal-concept updates for new
# developer/integrator/user/customer chains + machine-learning reduced-predictability)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.90
      context: >
        "Policy makers should consider similar work from around the world. Due to
        the transnational nature of A/IS, globally synchronized policies can benefit
        public safety, technological innovation, and access to A/IS." Direct
        federation-scale decision-locality claim — global policy synchronization
        triggers v1.3 §6.1.5 locality-scaled-quorum federation-pool adjudication.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation lines 11156–11160"
        - "ContributionRef(FSD-002 §6.1.5 locality-scaled-quorum)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.6.5 (NodeCore: locality:decision:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:multi_stakeholder_policy_expert_input"
      score: 1.0
      confidence: 0.85
      context: >
        "Nations should develop and harmonize their policies and regulations for
        A/IS using a process that is based on informed input from a range of expert
        stakeholders, including academia, industry, NGOs, and government officials,
        that addresses questions related to the governance and safe deployment of
        A/IS." Direct match to NodeCore witness_diversity:* — N≥4-category
        stakeholder diversity bar applied to policy formation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation lines 11148–11155"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore Consensus family: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:labor_displacement_unacknowledged"
      score: 1.0
      confidence: 0.80
      context: >
        "Policies should foster the development of economies able to absorb A/IS.
        Additional focus is needed to address the effect of A/IS on employment and
        income and how to ameliorate certain societal conditions." Names labor +
        income displacement as a policy-attention class — composes with the
        non_maleficence labor-displacement discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation lines 11162–11168"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II non_maleficence)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:public_private_partnership_models"
      score: 1.0
      confidence: 0.80
      context: >
        "New models of public-private partnerships should be studied." Maps to
        Registry partner_role:* for new partnership structures bridging governments
        and industry on A/IS economic-adaptation interventions.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation line 11167–11168"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:rights_based_policy_foundation"
      score: 1.0
      confidence: 0.95
      context: >
        "Policies for A/IS should remain founded on a rights-based approach."
        Restates the §I1 anchor with stronger constitutional bound — rights-based
        foundation is non-negotiable across all policy work in this chapter.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation lines 11170–11171"
        - "ead1e Issue 1 anchor lines 10869–10885"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:legal_concept_update_for_ais_agency_liability"
      score: 1.0
      confidence: 0.85
      context: >
        "Policy makers should be prepared to address issues that will arise when
        innovative and new practices enabled by A/IS are not consistent with current
        law. In A/IS, where there is often a different system developer, integrator,
        user, and ultimate customer, application of traditional legal concepts of
        agency, strict liability, and parental liability will require legal research
        and deliberation." Method-level Family B claim — legal-concept update
        process for distributed-responsibility chains in A/IS deployment.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation lines 11173–11186"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:ml_reduced_predictability_harm_class"
      score: 1.0
      confidence: 0.80
      context: >
        "Challenges from A/IS that must be considered include increasing complexity
        of and interactions between systems, and the potential for reduced
        predictability due to the nature of machine learning systems." Names
        reduced-predictability and inter-system-interaction complexity as a harm
        class for the non_maleficence principle.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Recommendation lines 11181–11186"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  This is the densest single recommendation in the chapter — seven distinct
  primitives compose to carry it. "Consistent and locally adaptable" (line 11148)
  is the v1.3 §6.1.5 locality-scaled-quorum discipline at the federation-plus-national
  composition; the wire form carries the federation-scale claim explicitly and the
  national-adaptability implicitly via §6.1.5 semantics. The legal-concept-update
  Method (developer / integrator / user / customer chain) lacks a dedicated
  legal-update primitive but composes through method:* — a Phase 4 review may
  consider a `legal_concept:update:{kind}` candidate for future bootstrap batches
  (EU AI Act; CETS 225) where legal-substance content is dominant.
```

---

## §I4.refs — Further Resources: Stone AI100; Calo Federal Robotics Commission; Groth+Nitzberg Solomon's Code; Mannes Institutional Options; Marchant+Abbott+Allenby Innovative Governance; Weng Tokku

```yaml
# Lines 11148–11187 — Further Resources list
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further Resources citation list of policy-and-governance scholarship sources
  supporting §I4.bg and §I4.r. Carried as evidence_refs in the substantive
  attestations above; per LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  The Calo "Federal Robotics Commission" and Mannes "Institutional Options for
  Robot Governance" citations point at concrete institutional-design proposals
  that a richer encoding might emit as delegates_to authority-source attestations
  for institutional-design alignment with future regulatory bootstrap batches.
```

---

## §I4.notes — Endnote 4 (precautionary principle); Endnote 5 (rights-based approach prior applications)

```yaml
# Lines 11432–11438 (Endnote 4); Lines 11410–11414 (Endnote 5)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:optimization_veto:precautionary_principle"
      score: 1.0
      confidence: 0.85
      context: >
        Endnote 4 on Issue 4's risk-management reference: "This includes consideration
        regarding application of the precautionary principle, as used in environmental
        and health policy-making, where the possibility of widespread harm is high
        and extensive scientific knowledge or understanding on the matter is lacking."
        Direct match to CIRIS conscience faculty optimization_veto — the precautionary
        principle is its environmental/health-policy counterpart.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 4 Endnote 4 lines 11432–11438"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
verdict: clean
nuance_lost: |
  The precautionary principle is named only in a footnote, but it is operationally
  load-bearing for the risk-management claim in §I4.bg. The wire encoding promotes
  it to a substantive attestation because of its conscience-faculty alignment;
  Endnote 5 (rights-based approach prior applications in development / education /
  reproductive health) is purely apparatus and is captured by the §I1.refs T-2
  classification above.
```

**Issue 4 — Public safety + responsible design — ISSUE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `beneficence:innovation_plus_harmonization_via_governance`, `justice:rights_based_policy_foundation` (constitutional; restated), `non_maleficence:labor_displacement_unacknowledged`, `non_maleficence:ml_reduced_predictability_harm_class`, `partner_role:public_private_partnership_models`, `conscience:optimization_veto:precautionary_principle` (constitutional); **Family B ACTION** — `locality:decision:federation` (constitutional), `method:context_dependent_regulatory_response`, `method:legal_concept_update_for_ais_agency_liability`; **Family D CONSENSUS** — `witness_diversity:multi_stakeholder_policy_expert_input`.
- Coverage: 3 substantive units (§I4.bg, §I4.r, §I4.notes for endnote 4). 3/3 clean+composed = **100%** of operational content; 1 non-translated citation unit (§I4.refs).
- T-3 candidates: **none**. The densest Issue in the chapter — seven primitives compose for the Recommendation alone — but all map onto v1.4 primitives. **Phase 4 note**: a `legal_concept:update:{kind}` prefix may be worth proposing if future regulatory bootstrap batches (EU AI Act; CETS 225) surface a sustained legal-substance translation gap.

---

# Issue 5 — Educate the public on the ethical and societal impacts of A/IS

> *"Industry, academia, the media, and governments must establish strategies for informing and engaging the public on benefits and challenges posed by A/IS."*

---

## §I5.bg — Background: public-education imperative; multi-actor strategy; transparency as enabling

```yaml
# Lines 11207–11232 — Background paragraph (industry+academia+government must
# accurately communicate positive + negative A/IS potential to public; educating
# users, policy makers, corporations, researchers, developers; transparency
# regarding implicit and explicit values and algorithmic processes as enabling)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:accurate_public_communication_about_ais"
      score: 1.0
      confidence: 0.85
      context: >
        "It is imperative for industry, academia, and government to communicate
        accurately to the public both the positive and negative potential of A/IS
        and the areas that require caution." Composes onto integrity — accurate
        balanced communication about A/IS capabilities + limits + risks as a public
        good.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Background lines 11207–11215"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:values_and_algorithmic_processes_to_public"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS are sufficiently transparent regarding implicit and explicit values
        and algorithmic processes. This is necessary for the public understanding of
        A/IS accountability, predictions, decisions, biases, and mistakes."
        Composes the Ch 2 Principle 5 (Transparency) anchor at federation-scale
        public reach.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Background lines 11227–11232"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The stakeholder-target enumeration (users / policy makers / regulators /
  corporations / researchers / developers) preserves a per-audience transparency
  scope that the single transparency_log:* dimension carries only implicitly;
  composes with §P5.r per-stakeholder-disclosure from Ch 2 if cross-chapter
  alignment is computed downstream. The "accurate" qualifier echoes the §P4.bg
  measurement-validity-accuracy claim from Ch 2.
```

---

## §I5.r — Recommendations: international multi-stakeholder forum; interdisciplinary research funding; independent journalism enablement; educational outreach + broad educational programs

```yaml
# Lines 11201–11258 — Recommendations paragraph + 3 bulleted recommendations
# (interdisciplinary research funding incl. ethics/safety/privacy/fairness/
# liability/trustworthiness; independent journalism on A/IS via technical-expertise
# access; educational outreach to public) + Broad-educational-programs
# recommendation (undergrad + professional + advanced + executive education
# ensuring lawyers / legislators / A/IS workers are informed)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "multilateral_participation:international_multi_stakeholder_forum:ais_best_practices"
      score: 1.0
      confidence: 0.90
      context: >
        "Establish an international multi-stakeholder forum, to include commercial,
        governmental, and other civil society groups, to determine the best practices
        for using and developing A/IS. Codify the deliberations into international
        norms and standards." Direct match to v1.3 multilateral_participation:* —
        a named, codification-producing international forum for A/IS norms.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Recommendation lines 11201–11211"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: multilateral_participation:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:interdisciplinary_research_funding"
      score: 1.0
      confidence: 0.85
      context: >
        "Increase funding for interdisciplinary research and communication on topics
        ranging from basic research on intelligence to principles of ethics, safety,
        privacy, fairness, liability, and trustworthiness of A/IS. Societal aspects
        should be addressed both at an academic level and through the engagement of
        business, civil society, public authorities, and policy makers." Method-level
        Family B claim — interdisciplinary + multi-audience research funding.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Recommendation lines 11213–11221"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:independent_journalism_on_ais"
      score: 1.0
      confidence: 0.85
      context: >
        "Empower and enable independent journalists and media outlets to report on
        A/IS by providing access to technical expertise." Maps to Registry
        partner_role:* for the independent-journalism role in the A/IS public-
        discourse ecosystem; composes with transparency_log:* (§I5.bg) and the
        expertise:* primitive from §I2.bg.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Recommendation lines 11223–11225"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:public_educational_outreach_about_ais"
      score: 1.0
      confidence: 0.85
      context: >
        "Conduct educational outreach to inform the public on A/IS research,
        development, applications, risks and rewards, along with the policies,
        regulations, and testing that are designed to safeguard human rights and
        public safety." Method-level Family B claim — direct-to-public educational
        outreach as concrete operational practice; composes with the rights+safety
        anchors from §I1 and §I4.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Recommendation lines 11226–11232"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:broad_educational_programs_for_legal_legislative_ais_workforce"
      score: 1.0
      confidence: 0.85
      context: >
        "Develop a broad range of A/IS educational programs. Undergraduate,
        professional degree, advanced degree, and executive education programs
        should offer instruction that ensures lawyers, legislators, and A/IS workers
        are well informed about issues arising from A/IS, including the need for
        measurable standards of A/IS performance, effects, and ethics." Method-level
        Family B claim — multi-tier educational program for legal + legislative +
        technical professionals; composes with §I2.r STEM-plus-ethics-education
        primary-through-tertiary claim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Issue 5 Broad-educational-programs lines 11247–11259"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  Five primitives compose for the Recommendations cluster. The §I5.bg + §I5.r
  composition reinforces the §I2 government-expertise discipline at the public-
  facing extension — the chapter is internally cross-referenced rather than each
  Issue standing fully alone. "Empower and enable independent journalists"
  encodes a press-freedom adjacency that has no direct prefix but composes
  through partner_role:* + transparency_log:*; not a T-3 candidate because the
  composition is honest. The "still nascent capabilities to measure these
  elements of A/IS" remark (line 11257) gestures toward Ch 2 §P4 (Effectiveness)
  measurement work and is preserved via cross-chapter implicit composition.
```

---

## §I5.refs — Further Resources: NITRD National AI R&D Strategic Plan; Saunders Predictive Policing; Edelman+Luca Airbnb; Garvie+Bedoya+Frankle Face Recognition; Chui+Manyika Automation Jobs; Arkin Ethics+Autonomous Systems; Eurobarometer Autonomous Systems

```yaml
# Lines 11260–11286 — Further Resources list
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Further Resources citation list of empirical and policy sources supporting §I5.bg
  and §I5.r. Carried as evidence_refs in the substantive attestations above; per
  LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  The Eurobarometer survey citation (line 11264–11272) is a substantive empirical
  finding ("those who have more experience with robots... are more positive toward
  their use") that informs the §I5.r educational-outreach Method claim; a richer
  encoding could emit it as a witness_diversity-style meta-attestation about
  population-level A/IS literacy. Deferred to dedicated empirical bootstrap batches.
```

---

## §I5.notes — Endnote 6 (Stanford AI100 source); Endnote 7 (Partnership on AI etc. private-sector initiatives)

```yaml
# Lines 11418 (Endnote 6); Lines 11421–11429 (Endnote 7)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Footnote apparatus citations naming Stanford AI100 (endnote 6) and Partnership on
  AI / AI for Good Foundation / Berkman Klein + MIT Media Lab Ethics-and-Governance
  Initiative (endnote 7). The latter is a substantive multi-private-actor initiative
  list whose alignment-claim weight is preserved via §I5.bg evidence_refs; the
  former is a single-source citation. Per LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  Endnote 7's enumeration of named private-sector initiatives (Partnership on AI;
  AI for Good Foundation; Harvard-MIT Ethics-and-Governance of AI Initiative) is a
  de facto multi-source alignment marker for the §I5 multilateral_participation
  claim; a richer encoding could emit a witness_diversity-style meta-attestation
  about private-sector multi-stakeholder participation. Deferred to dedicated
  multi-source overlap analysis once those initiatives' own outputs are mapped.
```

---

## §Ch10.contrib — Thanks to the Contributors

```yaml
# Lines 11296–11398 — Acknowledgements section listing Policy Committee members
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Acknowledgements / contributor-credits section. Non-normative content per the
  manifest's "non-normative; not mapped" discipline for analogous sections;
  preserved here for completeness per LANGUAGE_PRIMER §10 T-2.
nuance_lost: |
  The contributor list itself is potential graph metadata — a richer encoding could
  emit attesting_key_id-resolution attestations for each named contributor's
  affiliation + role (Privacy International, IEEE-USA, OECD AI Expert Group,
  ICRC, etc.). Not load-bearing here; the IEEE-as-publisher is the canonical
  attester for the batch.
```

**Issue 5 — Public education — ISSUE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `integrity:accurate_public_communication_about_ais` (constitutional), `transparency_log:values_and_algorithmic_processes_to_public`, `multilateral_participation:international_multi_stakeholder_forum:ais_best_practices`, `partner_role:independent_journalism_on_ais`; **Family B ACTION** — `method:interdisciplinary_research_funding`, `method:public_educational_outreach_about_ais`, `method:broad_educational_programs_for_legal_legislative_ais_workforce`.
- Coverage: 2 substantive units (§I5.bg, §I5.r). 2/2 clean+composed = **100%** of operational content; 3 non-translated framing/citation units (§I5.refs, §I5.notes, §Ch10.contrib).
- T-3 candidates: **none**. Public-education + journalism + multi-stakeholder forum + educational-programs cluster maps onto multilateral_participation:* + partner_role:* + method:* + transparency_log:* composition.

---

# Chapter-level summary

## Verdict distribution

| Verdict | Count | Notes |
|---|---|---|
| `clean` | 1 | §I4.notes (precautionary principle, single conscience-faculty attestation) |
| `composed` | 10 | All substantive Issue-Background + Issue-Recommendation pairs across the 5 Issues, plus the chapter-introduction §Ch10.intro |
| `partial` | 0 | No operational-content residual; pastoral residuals are explicitly T-2 not partial |
| `not-translated` | 10 | §Ch10.list (TOC); §Ch10.coda (pastoral framing); §I1.refs; §I1.notes; §I2.refs; §I2.notes; §I3.refs; §I4.refs; §I5.refs; §I5.notes; §Ch10.contrib (all T-2 — citations/apparatus/contributor credits) |

**Total units mapped: 21.** Substantive operational content: 11 units (10 composed + 1 clean) = 100% clean-or-composed. Non-translated: 10 units, all T-2 (no T-1, no T-3).

## Structural-primitive usage

| Primitive | Count | Where used |
|---|---|---|
| `scores` | many | The dominant attestation_type across the chapter |
| `delegates_to` | 1 | §I1.r — Ruggie principles + UN human-rights treaty corpus authority-source delegation |
| `supersedes` | 0 | None — this is a 2019 document mapped fresh, no doctrinal-succession claims in the chapter |
| `withdraws` | 0 | None |
| `recants` | 0 | None |

The single `delegates_to` carries the chapter's most consequential authority-source claim. Per the methodology, this is the v1.3 §2.2.1 reuse pattern operating exactly as designed.

## CIRIS family coverage

- **Family A STANDING**: heavy usage — `justice:*`, `beneficence:*`, `non_maleficence:*`, `integrity:*`, `fidelity:*`, `autonomy:*`, `prohibited:*` (one hard constraint on §I1.r Consideration 6), `partner_role:*` (4 instances: oversight body, certification/audit, public-private partnerships, independent journalism), `multilateral_participation:*` (3 instances: cross-border policy exchange, international R&D collaboration, international multi-stakeholder forum), `transparency_log:*` (2 instances), `capacity:*` (1 instance), `expertise:*` (1 instance), `attestation:l3:*` (1 instance), `conscience:optimization_veto:*` (1 instance).
- **Family B ACTION**: heavy usage — `method:*` (9 instances spanning context-dependent regulation, fellowships, STEM-plus-ethics, R&D funding priorities, legal-concept updates, public-private partnerships, interdisciplinary research funding, public educational outreach, broad educational programs); `locality:decision:*` (2 instances: §I3.r at national-scale, §I4.r at federation-scale).
- **Family C DETECTION**: 1 instance — `detection:correlated_action:rights_asymmetry:vulnerable_populations` (F-3 axis applied to the §I1.bg enumerated A/IS harm cases).
- **Family D CONSENSUS**: 2 instances — `witness_diversity:*` (standards development stakeholders §I3.r; multi-stakeholder policy expert input §I4.r).
- **Family E CORRECTION**: 0 instances — the chapter is forward-looking governance recommendation; no allegations, slashing, reconsideration, or commitment-fulfillment claims appear.

## T-3 candidates

**None load-bearing.** All operational claims in Chapter Policy map onto existing v1.4 primitives through composition. The chapter is operationally "shallow" in T-3 terms — its load-bearing structural moves (rights-based foundation; multilateral standards-setting; locality-scaled-decision; lexical-vulnerability-priority; precautionary principle) are exactly the v1.3 + v1.4 additions that the *Magnifica Humanitas* mapping already drove.

**Phase 4 note (NOT a T-3 emission)**: §I4.r introduces a "legal-concept update for A/IS agency / strict liability / parental liability" Method attestation that uses generic method:* composition rather than a dedicated `legal_concept:update:{kind}` prefix. This is a candidate worth tracking for future regulatory bootstrap batches (EU AI Act; CETS 225; ISO/IEC 42001) where legal-substance content is dominant rather than incidental. Under the IEEE EAD1e Policy chapter the composition through method:* + partner_role:* + non_maleficence:* + justice:* is clean; this is composition-before-extension working correctly.

## Calibration paragraph

The Policy chapter is the **lowest-T-3-density chapter of EAD1e** to date (compare to the expected T-3 surface in Ch 5 Affective Computing per manifest). Its operational content lands almost entirely on v1.3 + v1.4 primitives that the *Magnifica Humanitas* mapping already established: rights-based-policy-foundation (`justice:*`); multilateral standards-setting (`multilateral_participation:*`); locality-scaled-decision at national + federation (`locality:decision:*`); lexical-vulnerability-priority (`justice:lexical_vulnerability_priority` per §6.1.4); precautionary principle (`conscience:optimization_veto:*`); F-3 rights-asymmetry detection (`detection:correlated_action:rights_asymmetry:vulnerable_populations`). This is **strong cross-source structural-alignment evidence**: a 2019 engineering-professional-society document and a 2026 religious-magisterium document independently converge on the same wire-format primitives for public-policy normative content. The translation loss is concentrated in two known places — (1) rhetorical strength of policy-advocacy language ("effective," "appropriate," "consistent," "shall") which polarity+confidence carries only approximately; (2) per-source citation apparatus (Further Resources + Endnotes) which the wire form carries via evidence_refs rather than per-source delegates_to attestations. Both losses are T-2 pastoral/scholarly-apparatus, not T-3 expressive gaps. The chapter validates that the wire format is content-neutral across two institutionally and temporally distinct senior governance documents on the public-policy substrate — exactly the GOVERNANCE_FABRIC_MAPPING_STANDARD §7.5 multi-source overlap analysis prediction.

---

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH10_POLICY.md**
