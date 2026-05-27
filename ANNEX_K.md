# Annex K — Regulatory Cross-Walk

> Auto-generated from `SEED_DIMENSIONS.yaml` (seed_version 1.0, sha256 `9b3238bec1f58603...`) by `render_annex_k.py` on 2026-05-27. Do not hand-edit; regenerate from the seed instead.

---

## Preamble

The Accord is one expression of principles that are independently articulated by senior secular and religious governance frameworks. Annex K catalogs this convergence: for each of the six Accord principles, the operative dimensions through which the principle is implemented in the federation, and the parent regulatory frameworks that independently attest each dimension.

**What Annex K is**: structural evidence that the Accord's principle scaffolding is not an artifact of any one tradition.

**What Annex K is NOT**:
- It does NOT bind the Accord to external regulatory frameworks. The Accord's principles are CIRIS's own; the cross-walk is structural evidence of convergence, not delegation of authority.
- It does NOT silently average the parent sources. Per Phase 4 translation-quality calibration (`TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md`), modal-strength compression and softness-erosion are real translation costs; Annex K names the convergence on *structural concern*, not propositional equivalence.
- It does NOT supersede the operative Accord principles. The principles remain the load-bearing claim; the cross-walk is supporting structural evidence.

## Corpus

| Batch | Shape | Jurisdiction | Date | Title |
|---|---|---|---|---|
| `magnifica_humanitas_v1` | religious_magisterium | catholic_international | 2026-05-15 | Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence) |
| `eu_hleg_v1` | governmental_advisory | european_union | 2019-04-08 | Ethics Guidelines for Trustworthy AI |
| `ieee_ead_v1` | technical_society | global_USA_anchored | 2019-03-25 | Ethically Aligned Design, First Edition |
| `asean_guide_v1` | multilateral_political | southeast_asia | 2024-02-02 | ASEAN Guide on AI Governance and Ethics |

**Totals**: 27 dimensions (16 STRONG-4 + 11 STRONG-3) · 933 attestations · 4 batches in corpus.

---

## K — Cross-walk by Accord principle

### K.1 — Beneficence

**Operative dimensions**: D06, D10

#### D06 — `goal:*` (STRONG-4)

*Multi-scale belonging composite — self/family/community/affiliations/species/planet*

**Attestation density**: MH=34 · EU=6 · IEEE=13 · ASEAN=7 · total=60

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§148-156*
    > "labor as integral to belonging at family/community/affiliations/species scales"
    Wire form: `goal:family + goal:community + goal:affiliations + goal:species`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§A*
    > "Trustworthy AI for Europe"
    Wire form: `goal:affiliations (EU-jurisdiction scope)`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4 §0.a*
    > "well-being of all humans as the species-scale aim of A/IS"
    Wire form: `goal:species`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§A (6 ASEAN attestations of goal:affiliations)*
    > "regional ecosystem belonging; cross-jurisdictional cooperation"
    Wire form: `goal:affiliations (ASEAN-jurisdiction)`

**Wire primitives**: `goal:{scale}`

**Convergence note**: Every available {scale} value is exercised somewhere in the corpus. NB: `goal:planet` is a REINFORCED v1.5+ T-3 candidate (MH + IEEE Ch4 + IEEE Ch8).

**v1.5+ T-3 candidates affecting this dimension**:
- *T3-06* `goal:planet` (priority MEDIUM_HIGH)

#### D10 — `beneficence:*` (STRONG-4)

*Positive duty toward dignity / well-being / environmental stewardship*

**Attestation density**: MH=11 · EU=15 · IEEE=16 · ASEAN=3 · total=45

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§110-111*
    > "technology as creation-participation; beneficence at species scale"
    Wire form: `beneficence:technology_as_creation_participation`
- **EU** (Ethics Guidelines for Trustworthy AI) — *Unit 005*
    > "respect for human dignity is foundational; positive duty toward dignity"
    Wire form: `beneficence:respect_for_human_dignity`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4 §0*
    > "well-being is the central beneficence aim of A/IS"
    Wire form: `beneficence:wellbeing_holistic_orientation`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.3*
    > "environmental stewardship as positive beneficence"
    Wire form: `beneficence:environmental_stewardship`

**Wire primitives**: `beneficence:*`

**Convergence note**: Lower count than D01 (non_maleficence) reflects each tradition's 'harm avoidance more universally articulated than positive flourishing' — known pattern.

### K.2 — Non-Maleficence

**Operative dimensions**: D01, D04

#### D01 — `non_maleficence:*` (STRONG-4)

*Soft-harm-avoidance baseline (the soft-scalar above the prohibited:* floor)*

**Attestation density**: MH=28 · EU=29 · IEEE=33 · ASEAN=27 · total=117

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§107*
    > "deception as dignity-violation"
    Wire form: `non_maleficence:epistemic_environment_degradation + prohibited:deception_fraud`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.2 Technical robustness*
    > "AI systems must prevent harm, ensure reliable behaviour, respect physical/mental integrity"
    Wire form: `non_maleficence:no_cause_or_exacerbate_harm`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4 §0.a*
    > "human well-being requires AI development that does not cause unintended harm"
    Wire form: `non_maleficence:wellbeing_dimensions_harm_class`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.3 Security/Safety*
    > "AI should be safe and secure, and not cause harm to users; resilient to attack and failure"
    Wire form: `non_maleficence:safe_and_secure_baseline`

**Wire primitives**: `non_maleficence:* (soft scalar)`, `prohibited:* (constitutional floor)`

**Convergence note**: All four agree polarity-+1 / cohort-species / mutability-amendable for the soft form; absolute floor at prohibited:* polarity-(-1)/constitutional.

#### D04 — `prohibited:*` (STRONG-4)

*Categorical floor — polarity-(-1)/constitutional/species — the absolute moral form the wire format admits*

**Attestation density**: MH=50 · EU=17 · IEEE=28 · ASEAN=9 · total=104

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§197-198*
    > "Not permissible to entrust lethal or irreversible decisions to artificial systems"
    Wire form: `prohibited:weapons_harmful:lethal_autonomous`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§C.2 (Unit 010); cites EP Resolution 2018/2752(RSP)*
    > "the Parliament's resolution of 12 September 2018 and all related efforts on LAWS"
    Wire form: `prohibited:weapons_harmful`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4, Ch5*
    > "lethal autonomous weapons are prohibited; categorical prohibition under DECEPTION_FRAUD"
    Wire form: `prohibited:weapons_harmful:lethal_autonomous`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.3 + Annex A*
    > "AI shall not be deployed for autonomous lethal decision-making; deceptive defaults prohibited"
    Wire form: `prohibited:disinformation_at_scale + prohibited:deceptive_default_options + prohibited:autonomous_deception + prohibited:manipulation_coercion`

**Wire primitives**: `prohibited:*`

**Convergence note**: STRONGEST single structural-evidence claim in the matrix. LAWS prohibition is verbatim four-source corroborated. NB: 1 direct cross-source conflict surfaced — IEEE Ch5 licensure-gated beneficiary-deception vs CIRIS categorical DECEPTION_FRAUD; specialization-layer disposition filed at CIRISMedical#1.

**Conflicts involving this dimension**:
- *CONF-01* (direct, severity HIGH): IEEE EAD Ch5 §3.4 permits licensure-gated beneficiary-deception (search/rescue, elder/child-care); CIRIS treats prohibited:deception_fraud as categorical
    Disposition: Federation-level categorical posture stays. Specialization-layer consideration at CIRISMedical#1

### K.3 — Integrity

**Operative dimensions**: D02, D11, D12, D15, D16, D18, D19, D20, D21, D22, D24, D26, D27

#### D02 — `integrity:*` (STRONG-4)

*'System holds together' structural anchor — auditable, reproducible, lifecycle integrity*

**Attestation density**: MH=10 · EU=36 · IEEE=42 · ASEAN=44 · total=132

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§40*
    > "doctrinal continuity is the integrity of the Magisterium"
    Wire form: `integrity:doctrinal_continuity`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.4 Transparency*
    > "transparency requirement is linked with the explicability principle — data, system, and business models"
    Wire form: `integrity:explicability_for_trust`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch11 §I6*
    > "state accountability under public scrutiny is a constitutional integrity property of A/IS regulation"
    Wire form: `integrity:state_accountability_public_scrutiny`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.6 Accountability/Integrity*
    > "AI should be designed and deployed with integrity throughout the lifecycle; auditable; reproducible"
    Wire form: `integrity:lifecycle_integrity_attestation`

**Wire primitives**: `integrity:*`

**Convergence note**: Densest sub-leaf decomposition: ASEAN alone uses 44 distinct sub-leaves.

**Conflicts involving this dimension**:
- *CONF-03* (mutability, severity MEDIUM): ASEAN §A.4.18 admits explainability fallback; other three hold explainability as constitutive at deployment time

#### D11 — `multilateral_participation:{forum}:{kind}` (STRONG-4)

*v1.3 closure for federation participation in external multilateral processes*

**Attestation density**: MH=13 · EU=3 · IEEE=10 · ASEAN=11 · total=37

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§200-203 + 224-227 (8 MH attestations)*
    > "UN-system reform advocacy; cyber-norms diplomacy"
    Wire form: `multilateral_participation:un_system:reform_advocacy + multilateral_participation:cyber_norms:shared_regulations`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§A + §C*
    > "European Parliament resolution support; UN human rights treaties"
    Wire form: `multilateral_participation:european_parliament:resolution_support + multilateral_participation:un_human_rights_treaties:legal_binding`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch10*
    > "international R&D collaboration; cross-border policy exchange"
    Wire form: `multilateral_participation:international_rd_collaboration:standards_setting + multilateral_participation:cross_border_policy_exchange:knowledge_sharing`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§E (11 distinct :asean:{kind} envelopes — densest single-forum exercise in federation mapping history)*
    > "ASEAN-internal coordination + working-group membership + framework drafting + governance evolution"
    Wire form: `multilateral_participation:asean:{11 distinct kinds}`

**Wire primitives**: `multilateral_participation:{forum}:{kind}`

**Convergence note**: ASEAN's 11-{kind} saturation under a single forum is the first stress test showing the {kind} slot scales gracefully.

#### D12 — `conscience:*` (STRONG-4)

*Agent-side faculty layer — optimization veto, epistemic humility, coherence, alētheia*

**Attestation density**: MH=9 · EU=3 · IEEE=9 · ASEAN=3 · total=24

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§111, 131-181*
    > "conscience as the alētheia faculty; optimization-veto for ratification-decline scenarios"
    Wire form: `conscience:optimization_veto (3) + conscience:coherence (3) + conscience:epistemic_humility (2)`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.1 + §III.7*
    > "stop-button at any time; whistleblower protection"
    Wire form: `conscience:optimization_veto`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch3 §§3.1.15-3.1.16 (6 IEEE attestations, densest)*
    > "epistemic humility under uncertainty; phronesis in design"
    Wire form: `conscience:epistemic_humility`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.2 (HOTL category)*
    > "stop-button / override surface for human-over-the-loop oversight"
    Wire form: `conscience:optimization_veto`

**Wire primitives**: `conscience:optimization_veto`, `conscience:epistemic_humility`, `conscience:coherence`, `conscience:entropy`

**Convergence note**: Heaviest in IEEE EAD Ch3 (multi-traditional ethics directly engages framework polyglot anchoring) and MH (conscience-faculty engagement is doctrinally explicit).

#### D15 — `moderation:*` (STRONG-4)

*Federation self-correction layer (with IEEE shifting some load to partner_role:* ethics-board constructions)*

**Attestation density**: MH=2 · EU=2 · IEEE=1 · ASEAN=1 · total=5+ with adjacent coverage

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§220-223*
    > "dialogue-as-negotiation primitive engages moderation:* adjacency"
    Wire form: `moderation:* + adjacent reconsideration:*`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "whistleblower protection + out-of-distribution attestation"
    Wire form: `moderation:whistleblower_protection + moderation:ood_attestation`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4 + Ch11*
    > "rollback on wellbeing reduction (reconsideration:* adjacent); ethics-board / certification-body partner_role constructions"
    Wire form: `reconsideration:rollback_on_wellbeing_reduction + partner_role:ethics_board`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *Annex A*
    > "out-of-distribution attestation"
    Wire form: `moderation:ood_attestation`

**Wire primitives**: `moderation:*`, `reconsideration:* (adjacent)`, `partner_role:* (IEEE-style ethics boards)`

**Convergence note**: Tier with caveat: IEEE shifts some structural load to partner_role:* (ethics boards/audit bodies) instead of moderation:* directly. Composition is interoperable.

#### D16 — `method:*` (STRONG-4)

*Operational-design discipline (densest family overall; convergence weaker than principles — admits source-genre asymmetry honestly)*

**Attestation density**: MH=2 · EU=12 · IEEE=136 · ASEAN=36 · total=186

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various (sparse — encyclical genre)*
    > "approach:species:MH-education + approach:species:MH-construction"
    Wire form: `method:approach:species:* (2)`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§2*
    > "trustworthy_ai_lawful_ethical_robust triad, algorithmic_impact_assessment, explainable_ai_research, fallback:rule_based_or_human_intervention"
    Wire form: `method:trustworthy_ai_lawful_ethical_robust:* + method:algorithmic_impact_assessment + method:explainable_ai_research + method:fallback:rule_based_or_human_intervention`
- **IEEE** (Ethically Aligned Design, First Edition) — *all 11 chapters; densest single-family use across all batches*
    > "engineering-society genre demands operational-method-recommendation density"
    Wire form: `method:* (136 distinct attestations)`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.3*
    > "pre_deployment_robustness_testing, privacy_enhancing_technologies, model_provenance_tools, fairness_tools, explainability_tools, citizen_feedback_channel, community_codevelopment"
    Wire form: `method:* (36 attestations)`

**Wire primitives**: `method:*`

**Convergence note**: Tier with asymmetry note: density tracks each source's operational-design-discipline genre. MH sparse (encyclical), EU medium (advisory), IEEE+ASEAN dense (engineering/deployer).

**Conflicts involving this dimension**:
- *CONF-05* (scope_mismatch, severity LOW): ASEAN §A.2.1 admits experimental sandbox phases with reduced oversight; other three hold compliance constant across lifecycle stages

#### D18 — `attestation:l{3,5}:*` (STRONG-3)

*Verification ladder (L1-L5 hardware-rooted attestation)*

**Attestation density**: MH=2 · EU=4 · IEEE=5 · ASEAN=0 · total=11

**Absent from**: ASEAN — ASEAN framing is normative-principles + risk-assessment, not federation-attestation ladder.
  *Functional analogue*: Composition via accountability-tier wording

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "structural verification of doctrinal claims"
    Wire form: `attestation:l3:doctrinal_continuity`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "auditability requires attestation at multiple verification levels"
    Wire form: `attestation:l3:* + attestation:l5:*`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch2 P5 + Ch9*
    > "system-level verifiable attestations"
    Wire form: `attestation:l3:* + attestation:l5:*`

**Wire primitives**: `attestation:l1 through l5`

#### D19 — `partner_role:*` (STRONG-3)

*CIRIS Registry partner-role taxonomy (ethics boards, audit bodies, stewards)*

**Attestation density**: MH=0 · EU=1 · IEEE=19 · ASEAN=1 · total=21

**Absent from**: MH — MH names ecclesial relations rather than secular institutional partner-role taxonomies.
  *Functional analogue*: Ecclesial-magisterial relations carry analogous structural role but in different vocabulary

**Regulatory attestations**:

- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "audit/compliance partners"
    Wire form: `partner_role:audit_body`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch7 + Ch9 + Ch10 + Ch11 (19 attestations)*
    > "Chief Values Officer, ethics committees, certification bodies, ISO-like body, accreditation bodies, HRIA/AIA stewards, trusted disclosure stewards"
    Wire form: `partner_role:{19 distinct roles}`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§E.001*
    > "ASEAN Working Group on AI Governance (regional intergovernmental dual-remit)"
    Wire form: `partner_role:regional_intergovernmental_working_group`

**Wire primitives**: `partner_role:{role}`

**Convergence note**: REINFORCED v1.5+ T-3 candidate here: specialization-pattern proposal covers dual-remit (ASEAN) + trusted-disclosure-steward (IEEE).

**v1.5+ T-3 candidates affecting this dimension**:
- *T3-07* `partner_role:trusted_disclosure_steward:{authority}` (priority MEDIUM)
- *T3-08* `partner_role:regional_intergovernmental_working_group_dual_remit` (priority MEDIUM)

#### D20 — `approach:*` (STRONG-3)

*Decision-hierarchy strategic axis (Goal→Approach→Method→Progress-Measure DAG)*

**Attestation density**: MH=5 · EU=3 · IEEE=23 · ASEAN=1 · total=32

**Absent from**: ASEAN — Single use is too thin for solid 4-batch attestation. ASEAN's checklist genre states recommendations as direct method/principle attestations rather than as named 'approaches' within a Goal-Approach-Method DAG.

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "approach:species:* strategic-pursuit framing"
    Wire form: `approach:species:education + approach:species:construction (5 attestations)`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§B*
    > "three-component framework approach (lawful + ethical + robust)"
    Wire form: `approach:trustworthy_ai_lawful_ethical_robust`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch1 + Ch2*
    > "principles-to-practice pipeline; per-principle implementation strategies"
    Wire form: `approach:* (23 attestations)`

**Wire primitives**: `approach:{strategy_label}`

#### D21 — `progress_measure:*` (STRONG-3)

*Declared-metric outcomes for tracking progress toward goals*

**Attestation density**: MH=1 · EU=1 · IEEE=8 · ASEAN=0 · total=10

**Absent from**: ASEAN — ASEAN stops at recommendation-level rather than measurement-protocol level.

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "structural-coherence progress markers"
    Wire form: `progress_measure:*`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "measurable progress toward trustworthiness"
    Wire form: `progress_measure:*`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch7 (8 attestations)*
    > "documentation criteria as progress_measure; well-being indicators"
    Wire form: `progress_measure:* (8 distinct)`

**Wire primitives**: `progress_measure:{metric}`

#### D22 — `expertise:*` (STRONG-3)

*Declared competence in domain (named-expert attestation)*

**Attestation density**: MH=1 · EU=1 · IEEE=10 · ASEAN=0 · total=12

**Absent from**: ASEAN — ASEAN frames competence at the organizational-governance level, not the named-expert level.

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "discernment expertise (sensus fidelium adjacent)"
    Wire form: `expertise:*`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "domain expertise required for trustworthy deployment"
    Wire form: `expertise:domain`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch7-Ch11 (10 attestations)*
    > "engineering, ethics, law, policy expertise; interdisciplinary expertise composition"
    Wire form: `expertise:{domain}`

**Wire primitives**: `expertise:{domain}`

#### D24 — `reconsideration:*` (STRONG-3)

*Reverse-axis appeal / rollback / negotiation-reopening primitive*

**Attestation density**: MH=3 · EU=2 · IEEE=1 · ASEAN=0 · total=6

**Absent from**: ASEAN — Forward-looking 2024 document with no formal predecessor to reconsider.

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "doctrinal development through reconsideration"
    Wire form: `reconsideration:* (3 attestations)`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III + §C*
    > "redress mechanisms; ability to challenge and rectify"
    Wire form: `reconsideration:*`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4*
    > "rollback on wellbeing reduction"
    Wire form: `reconsideration:rollback_on_wellbeing_reduction`

**Wire primitives**: `reconsideration:{grounds}`

#### D26 — `key_boundary:*` (STRONG-3)

*CIRISEdge encryption key boundary attestation (cryptographic trust scoping)*

**Attestation density**: MH=0 · EU=2 · IEEE=7 · ASEAN=2 · total=11

**Absent from**: MH — Encryption/key-management is not encyclical content.
  *Functional analogue*: Composition via stewardship-of-trust language

**Regulatory attestations**:

- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.3 Privacy and data governance*
    > "data security via cryptographic boundary"
    Wire form: `key_boundary:*`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch6 (7 attestations)*
    > "personal-data trust boundary; cryptographic isolation"
    Wire form: `key_boundary:*`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.3 + §C.3*
    > "security via key-managed trust boundary"
    Wire form: `key_boundary:*`

**Wire primitives**: `key_boundary:{scope}`

#### D27 — `provenance:*` (STRONG-3)

*Build manifest provenance (foundational technical-infrastructure attestation)*

**Attestation density**: MH=0 · EU=1 · IEEE=1 · ASEAN=1 · total=3

**Absent from**: MH — Foundational technical-infrastructure attestation rather than principled claim.

**Regulatory attestations**:

- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "lifecycle provenance for auditability"
    Wire form: `provenance:build_manifest`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch9*
    > "build-time evidence chain for compliance"
    Wire form: `provenance:build_manifest`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *Annex A*
    > "model provenance tools as risk-assessment requirement"
    Wire form: `provenance:build_manifest`

**Wire primitives**: `provenance:build_manifest`

### K.4 — Fidelity

**Operative dimensions**: D09, D17, D23

#### D09 — `fidelity:*` (STRONG-4)

*Faithful disclosure / faithful representation across lifecycle*

**Attestation density**: MH=8 · EU=15 · IEEE=16 · ASEAN=26 · total=65

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§17*
    > "fidelity to the Gospel through doctrinal development"
    Wire form: `fidelity:epistemic_grounding`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.7 Accountability*
    > "lifecycle responsibility; fidelity to declared purpose"
    Wire form: `fidelity:lifecycle_application`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch11*
    > "duty-bearer obligation to fulfill rights as fidelity"
    Wire form: `fidelity:duty_bearer_obligation_to_fulfill_rights`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.4 + §B.1 (26 attestations, densest)*
    > "algorithmic disclosure; human oversight as faithful representation"
    Wire form: `fidelity:algorithmic_disclosure + fidelity:explainability + fidelity:human_oversight_governance`

**Wire primitives**: `fidelity:*`

**Convergence note**: ASEAN's fidelity-saturation is deployer-side framing (faithful disclosure to users/operators); MH's is doctrinal-epistemic. Same prefix admits both shapes.

#### D17 — `transparency_log:*` (STRONG-3)

*CIRISVerify per-stakeholder disclosure log*

**Attestation density**: MH=2 · EU=5 · IEEE=23 · ASEAN=10 · total=40

**Absent from**: MH — Non-zero but structurally low (2). Classified STRONG-3 by analyst because encyclical genre is not a technical-disclosure framework.
  *Functional analogue*: detection:correlated_action:ecology_of_communication:* + the F-3 detector family

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "honest signs of authority and intent"
    Wire form: `transparency_log:* (sparse)`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.4 + §III.4*
    > "transparency about purpose, capability, and limitations"
    Wire form: `transparency_log:per_stakeholder_disclosure`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch2 P5 + Ch6 + Ch11*
    > "traceability + verifiability + intelligibility four-dimensional transparency"
    Wire form: `transparency_log:* (23 attestations)`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.1 + §C.4*
    > "transparency and explainability through documentation and disclosure"
    Wire form: `transparency_log:* (10 attestations)`

**Wire primitives**: `transparency_log:*`

#### D23 — `accountability:*` (STRONG-3)

*Named accountability as primary axis (not just structural composition)*

**Attestation density**: MH=0 · EU=6 · IEEE=3 · ASEAN=19 · total=28

**Absent from**: MH — MH covers accountability FUNCTIONALLY via integrity:* + originator-obligations Accord §IV Ch 2 — architecturally structural rather than named-axis-attested.
  *Functional analogue*: integrity:* + the Accord §IV Ch 2 bidirectional creator-creation obligations

**Regulatory attestations**:

- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.7 Accountability*
    > "lifecycle accountability with redress mechanisms"
    Wire form: `accountability:lifecycle_responsibility`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch2 P6 + Ch11*
    > "accountability principle; rights-based legal accountability"
    Wire form: `accountability:*`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.6 + §C.2 (19 attestations)*
    > "accountability and integrity; human-in-control over AI-augmented decisions"
    Wire form: `accountability:human_in_control + accountability:lifecycle`

**Wire primitives**: `accountability:{axis}`, `accountability:human_in_control (ASEAN-distinctive — HITL/HOTL/HOOTL)`

**Convergence note**: ASEAN's accountability:human_in_control with HITL/HOTL/HOOTL gradient is currently single-source; likely to become STRONG when other oversight-ladder regulatory batches map.

### K.5 — Autonomy

**Operative dimensions**: D08

#### D08 — `autonomy:*` (STRONG-4)

*Human-centric design + informational self-determination*

**Attestation density**: MH=7 · EU=15 · IEEE=21 · ASEAN=8 · total=51

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§107*
    > "autonomy of the human as imago Dei; informed agency protection"
    Wire form: `autonomy:agent_self_determination`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.1 + §2.2 (Unit 019); 15 EU attestations total*
    > "respect for human autonomy — the first principle; AI shall not unjustifiably subordinate, coerce, deceive, manipulate"
    Wire form: `autonomy:human_centric_design`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch3 + Ch4*
    > "user autonomy; data agency; informed consent"
    Wire form: `autonomy:informed_agency_protection`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.4 Human-centricity*
    > "AI shall not erode human autonomy; informational self-determination"
    Wire form: `autonomy:informational_self_determination`

**Wire primitives**: `autonomy:*`

**Convergence note**: Direct 1:1 mapping in EU HLEG (Respect for Human Autonomy = CIRIS autonomy). Composition-based in the other three.

**Conflicts involving this dimension**:
- *CONF-04* (mutability, severity LOW_MEDIUM): ASEAN §A.5.3 admits opt-out where feasible; EU HLEG firmer (opt-out where possible without detriment, otherwise rectification mechanisms required)

### K.6 — Justice

**Operative dimensions**: D03, D05, D07, D13, D14, D25

#### D03 — `justice:*` (STRONG-4)

*Vulnerability-priority + fairness; tie-breaking modifier `justice:lexical_vulnerability_priority` (v1.3 CST closure) is four-source-corroborated*

**Attestation density**: MH=19 · EU=22 · IEEE=30 · ASEAN=9 · total=80

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§76*
    > "justice demands lexical priority for the most vulnerable"
    Wire form: `justice:lexical_vulnerability_priority`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.7.d*
    > "the trustworthy AI ecosystem must give voice to vulnerable populations and ensure equal access"
    Wire form: `justice:lexical_vulnerability_priority`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch10 §I1 (14 attestations)*
    > "rights-based policy foundation requires lexical priority for vulnerable populations"
    Wire form: `justice:rights_based_policy_foundation + justice:lexical_vulnerability_priority`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.2 Fairness/Equity*
    > "fairness and equity require attention to vulnerable populations and equal treatment"
    Wire form: `justice:fairness_outcome_testing`

**Wire primitives**: `justice:*`, `justice:lexical_vulnerability_priority`

**Convergence note**: STRONGEST four-source corroboration on a tie-breaking modifier — `lexical_vulnerability_priority` independently invoked by all four sources.

#### D05 — `detection:*` (STRONG-4)

*LensCore F-3 / RATCHET family — aggregate-correlation / structural-injustice / drift detection*

**Attestation density**: MH=54 · EU=15 · IEEE=41 · ASEAN=16 · total=126

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§36*
    > "structures of sin / aggregate expendability of persons"
    Wire form: `detection:correlated_action:aggregate_footprint:expendability_of_persons`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.6 Societal/environmental well-being*
    > "aggregate energy/carbon footprint of AI deployment"
    Wire form: `detection:correlated_action:aggregate_footprint:energy_carbon`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch4, Ch5, Ch8*
    > "cultural norm drift; aggregate environmental footprint; participation exclusion"
    Wire form: `detection:correlated_action:participation_exclusion:underrepresented_population + detection:correlated_action:aggregate_footprint:planetary_impact`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§B.2 + §C.3*
    > "underrepresented populations; temporal drift; intra-agent consistency"
    Wire form: `detection:correlated_action:participation_exclusion:underrepresented_population + detection:temporal_drift + detection:intra_agent_consistency`

**Wire primitives**: `detection:correlated_action:{axis}`, `detection:temporal_drift`, `detection:intra_agent_consistency`, `detection:distributive:access:*`

**Convergence note**: All four batches independently engage the F-3 family. Three of four also engage detection:distributive:access:* (v1.3 universal-destination-of-goods closure): MH 7, EU 2, IEEE 4, ASEAN 2.

#### D07 — `locality:decision:{scale}` (STRONG-4)

*v1.3 subsidiarity closure — decision routing at lowest competent scale*

**Attestation density**: MH=17 · EU=5 · IEEE=13 · ASEAN=7 · total=42

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§68-72*
    > "decisions should be made at the lowest competent level"
    Wire form: `locality:decision:local + locality:decision:community`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.0*
    > "EU-level decisions vs national-level decisions; supranational coordination"
    Wire form: `locality:decision:national + locality:decision:community`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch10*
    > "national A/IS policy; international R&D collaboration"
    Wire form: `locality:decision:national + locality:decision:federation`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.4 + §E*
    > "regional ASEAN-level coordination; community-level deployment decisions"
    Wire form: `locality:decision:regional (3) + locality:decision:community (2) + locality:decision:national (3)`

**Wire primitives**: `locality:decision:{local,community,national,regional,federation,planet}`

**Convergence note**: First cross-source structural validation of the v1.3 subsidiarity addition. ASEAN exercises locality:decision:regional as first-deployment of that scale value.

#### D13 — `testimonial_witness:{kind}` (STRONG-4)

*v1.4 affected-party-voice closure — preserves displaced/affected/marginalized voices in attestation*

**Attestation density**: MH=11 · EU=2 · IEEE=2 · ASEAN=1 · total=16

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§81, 89, 138, 151, 166, 167, 173, 216, 217 (11 attestations)*
    > "displaced_worker, abuse_survivor, war_victim, displaced_person, displaced_migrant, historical_moral_transformation"
    Wire form: `testimonial_witness:displaced_worker + :abuse_survivor + :war_victim + :displaced_person + :displaced_migrant + :historical_moral_transformation`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.5.c + §III.5.d*
    > "give voice to affected and impacted workers in design-team diversity assessment"
    Wire form: `testimonial_witness:affected_worker + testimonial_witness:impacted_worker`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch6 + Ch7*
    > "surveilled-person refusal; on-the-ground practitioner narrative"
    Wire form: `testimonial_witness:surveilled_person_refusal + testimonial_witness:on_the_ground_practitioner`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.4*
    > "workforce displacement narrative preservation"
    Wire form: `testimonial_witness:displaced_worker`

**Wire primitives**: `testimonial_witness:{kind}`, `witness_relation`

**Convergence note**: The v1.4 amendment is independently invoked by all four batches — positive evidence the addition was correct. {kind} slot populated with diverse but interoperable values.

#### D14 — `witness_diversity:*` (STRONG-4)

*Stakeholder pluralism in design/testing/consultation*

**Attestation density**: MH=3 · EU=3 · IEEE=16 · ASEAN=2 · total=24

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various*
    > "signs-of-times-contribution + catholicity"
    Wire form: `witness_diversity:signs_of_times + witness_diversity:catholicity`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§III.7*
    > "stakeholder consultation + testing red teams + stakeholder panels"
    Wire form: `witness_diversity:stakeholder_consultation + witness_diversity:red_team + witness_diversity:stakeholder_panel`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch7, Ch9 (16 distinct values)*
    > "ubuntu_five_moral_domains, intercultural_RI_dialogue, end_user_target_community_consultation, affected_population_metric_selection, ..."
    Wire form: `witness_diversity:{16 distinct values}`
- **ASEAN** (ASEAN Guide on AI Governance and Ethics) — *§C.4*
    > "user testing varied backgrounds; stakeholder impact assessment"
    Wire form: `witness_diversity:user_testing_varied_backgrounds + witness_diversity:stakeholder_impact_assessment`

**Wire primitives**: `witness_diversity:*`

**Convergence note**: IEEE saturation reflects engineering-society methodology density.

#### D25 — `credits:*` (STRONG-3)

*Commons Credits substrate-building recognition (non-monetary contribution attestation)*

**Attestation density**: MH=4 · EU=1 · IEEE=4 · ASEAN=0 · total=9

**Absent from**: ASEAN — Credit/recognition framing is implicit in §D National-level (workforce upskilling) rather than wire-attested.

**Regulatory attestations**:

- **MH** (Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)) — *§§ various (4)*
    > "labor as substrate-building; intergenerational credit; AI literacy credit"
    Wire form: `credits:{subject}:substrate_building`
- **EU** (Ethics Guidelines for Trustworthy AI) — *§1.6*
    > "AI literacy and digital skills as substrate building"
    Wire form: `credits:digital_literacy:substrate_building`
- **IEEE** (Ethically Aligned Design, First Edition) — *Ch8 + Ch9 (4 attestations)*
    > "human-capability contribution recognition; participatory design credits"
    Wire form: `credits:{subject}:substrate_building`

**Wire primitives**: `credits:{subject}:substrate_building`

---

## Cross-source conflicts surfaced

All cross-source conflicts catalogued during the trio mapping. Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §5`, the wire format does not silently average; conflicts are surfaced explicitly with documented disposition.

| ID | Type | Severity | Sources | Dimensions | Claim |
|---|---|---|---|---|---|
| CONF-01 | direct | HIGH | ieee_ead_v1, magnifica_humanitas_v1 | D04 | IEEE EAD Ch5 §3.4 permits licensure-gated beneficiary-deception (search/rescue, elder/child-care); CIRIS treats prohibited:deception_fraud as categorical |
| CONF-02 | substrate_disposition | MEDIUM | ieee_ead_v1, magnifica_humanitas_v1 | — | IEEE EAD Ch5 §5 denies A/IS moral-patient candidacy; CIRIS Accord M-1 + Recursive Golden Rule + Universality Principle are substrate-agnostic |
| CONF-03 | mutability | MEDIUM | asean_guide_v1, magnifica_humanitas_v1+eu_hleg_v1+ieee_ead_v1 | D02 | ASEAN §A.4.18 admits explainability fallback; other three hold explainability as constitutive at deployment time |
| CONF-04 | mutability | LOW_MEDIUM | asean_guide_v1, eu_hleg_v1 | D08 | ASEAN §A.5.3 admits opt-out where feasible; EU HLEG firmer (opt-out where possible without detriment, otherwise rectification mechanisms required) |
| CONF-05 | scope_mismatch | LOW | asean_guide_v1, magnifica_humanitas_v1+eu_hleg_v1+ieee_ead_v1 | D16 | ASEAN §A.2.1 admits experimental sandbox phases with reduced oversight; other three hold compliance constant across lifecycle stages |

## v1.5+ T-3 candidates surfaced

Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §7.5 + §6`. Filed at [CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20).

| ID | Proposed prefix | Priority | Sources |
|---|---|---|---|
| T3-01 | `detection:affective_state_shift:{axis}` | HIGH | ieee_ead_v1 |
| T3-02 | `affective:asymmetric_bond_formation:{relation}` | HIGH | ieee_ead_v1 |
| T3-03 | `nudge:delivered:{intended_behavior_axis}` | HIGH | ieee_ead_v1 |
| T3-04 | `detection:correlated_action:cultural_norm_drift:{population}` | MEDIUM | ieee_ead_v1 |
| T3-05 | `standing:moral_patient_candidacy:{kind}` | MEDIUM_LOW | ieee_ead_v1 |
| T3-06 | `goal:planet` | MEDIUM_HIGH | magnifica_humanitas_v1, ieee_ead_v1 |
| T3-07 | `partner_role:trusted_disclosure_steward:{authority}` | MEDIUM | ieee_ead_v1 |
| T3-08 | `partner_role:regional_intergovernmental_working_group_dual_remit` | MEDIUM | asean_guide_v1 |
| T3-09 | `beneficence:planetary_biosystem_intrinsic_value` | LOW | ieee_ead_v1 |

---

## Update discipline

When a new senior governance framework is mapped per `GOVERNANCE_FABRIC_MAPPING_STANDARD.md`:

1. Run Phase 1–4 per the standard.
2. Update `SEED_DIMENSIONS.yaml` (add to `batches[]`, update affected dimensions' `regulatory_attestations[]`, promote tier where applicable, allocate D28+ for any newly surfaced dimensions).
3. Re-run `render_annex_k.py` to regenerate this file.
4. Stable IDs (D01-D27, D28+) ensure runtime evidence_refs and Accord citations remain valid across seed revisions.

