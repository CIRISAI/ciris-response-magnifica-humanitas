# EU HLEG — Section C (Examples of opportunities and critical concerns) + Section D (Conclusion)

**Batch**: eu_hleg_v1
**Section range**: lines 1680–1916
**Source file**: `source_material/governance/eu_hleg_v1/eu_hleg_ethics_guidelines_trustworthy_ai_2019.txt`
**Wire format**: FSD-002 v1.4 | Primer: `LANGUAGE_PRIMER.md` v1.1
**Methodology**: GOVERNANCE_FABRIC_MAPPING_STANDARD §2 Phase 2 sub-agent fan-out
**Bootstrap batch reference**: `provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}`

**Scope note**: The Glossary (lines 1917+) is definitional / explanatory and is correctly out of scope per the source-preparation manifest. This file covers Sections C (lines 1680–1866) and D (lines 1868–1916) only.

**Atomic units mapped**: 17
**Verdict counts**: clean=0, composed=9, partial=2, not-translated=6
**T-3 load-bearing candidates surfaced**: 0 (all critical-concern claims either compose cleanly under existing primitives or sit honestly as T-2 PASTORAL_PROSE; composition-before-extension applied throughout)
**Prohibitions-overlap surface**: HIGH — Section C contains four critical-concern items that line up directly against CIRIS `prohibited:*` hard constraints (`prohibited:surveillance_mass`, `prohibited:autonomous_deception`, `prohibited:discrimination`, `prohibited:weapons_harmful`). These are the strongest cross-document multi-source-alignment candidates in the entire EU HLEG batch.

---

## Unit 001 — C.preamble (lines 1681–1684): three-axis frame (should/can/should-not)

**Source** (lines 1681–1684): "we provide examples of AI development and use that should be encouraged, as well as examples of where AI development, deployment or use can run counter to our values and may raise specific concerns. A balance must be struck between what should and what can be done with AI, and due care must be given to what should not be done with AI."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Section-internal scaffolding (the "encouraged / counter-to-values / should-not"
  three-axis frame). The substantive should/should-not content lives in the
  subsequent named subsections (climate / health / education / identification /
  covert AI / scoring / LAWS). No standalone wire claim is owed; the operational
  shape is carried by Units 002–014 below. Carry-forward citation only.
nuance_lost: |
  The "should / can / should-not" trichotomy is a self-conscious normative frame
  rather than a structural claim — it sets up downstream items but doesn't itself
  attest anything wire-encodable.
```

---

## Unit 002 — C.1.preamble (lines 1689–1692): Trustworthy AI as opportunity vis-à-vis SDGs

**Source** (lines 1689–1692): "Trustworthy AI can represent a great opportunity to support the mitigation of pressing challenges facing society such as an ageing population, growing social inequality and environmental pollution. This potential is also reflected globally, such as with the UN Sustainable Development Goals."

**Verdict**: composed

```yaml
# Unit 002 — Trustworthy AI as opportunity-vector against three named challenges + SDG alignment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.85
      confidence: 0.80
      context: >
        Trustworthy AI named as opportunity-vector for mitigating three
        challenges at species scope: ageing population, growing social
        inequality, environmental pollution. Aligned to the UN Sustainable
        Development Goals (cited again, supersedes-chains Unit 003 of the
        Section-A intro under the same SDG anchor).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1.preamble (lines 1689-1692)"
        - "UN Sustainable Development Goals (footnote 57)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:opportunity_orientation"
      score: 0.80
      confidence: 0.80
      context: >
        Positive beneficence framing of AI deployment as challenge-mitigation
        capacity. Three named challenge classes; SDG anchoring functions as
        the cross-multilateral evidence pin.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1.preamble (lines 1689-1692)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — beneficence)"
verdict: composed
nuance_lost: |
  "Great opportunity" rhetoric and the European-strategic framing ("encourage a
  European AI strategy") are not in the wire form. The three challenge classes
  are kept as context-prose only; if they were each load-bearing they would
  decompose into three sub-goals, but the paragraph deploys them as scope-setting
  rather than as discrete operational aims.
```

---

## Unit 003 — C.1 Climate action and sustainable infrastructure (lines 1696–1705)

**Source** (lines 1696–1705): "Trustworthy AI ... potential to reduce humans' impact on the environment and enable the efficient and effective use of energy and natural resources. ... AI systems for intelligent transport systems can be used to minimise queuing, optimise routing, allow vision impaired people to be more independent, optimise energy efficient engines ... AI systems could help to reduce the number [of car-accident] fatalities significantly."

**Verdict**: composed

```yaml
# Unit 003 — Climate + transport opportunity: environmental beneficence + accessibility + safety
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:environmental_footprint_reduction"
      score: 0.85
      confidence: 0.80
      context: >
        Trustworthy AI deployments oriented to (a) reducing humans' environmental
        impact, (b) efficient use of energy and natural resources, (c) detecting
        energy needs more accurately for infrastructure-level optimisation,
        (d) decarbonisation via transport-system efficiency. Beneficence pole of
        the environmental-stewardship axis (paired with non_maleficence:
        environmental_footprint at Unit §1.6 in the Requirements file).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Climate (lines 1696-1703)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — beneficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:universal_design_accessibility"
      score: 0.80
      confidence: 0.80
      context: >
        Explicit naming of vision-impaired-persons independence via AI-enabled
        transport. Accessibility framing inside the climate subsection; carries
        the justice-as-inclusion axis (already attested in Unit §1.5 of the
        Requirements file).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Climate (lines 1701-1702)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:physical_mental_wellbeing"
      score: 0.80
      confidence: 0.75
      context: >
        AI-enabled fatality reduction in car accidents (cited statistic:
        one human death per 23 seconds globally). Non-maleficence at the
        physical-safety axis; opportunity-pole framing of the same prefix that
        elsewhere carries the harm-prevention pole.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Climate (lines 1703-1705)"
        - "WHO road traffic injuries fact sheet (footnote 62)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — non_maleficence)"
verdict: composed
nuance_lost: |
  Per-project illustrative footnotes (Encompass, Fabulos, PRO4VIP, UP-Drive)
  are catalogued in evidence-prose but not minted as separate Contributions —
  they are deployment examples, not normative claims. The implicit Approach
  ("couple AI to big data for energy detection") is one operational rung
  below the Goal level and could be a Method node if elaborated, but the
  source paragraph holds it as illustrative rather than as a Method-level
  prescription.
```

---

## Unit 004 — C.1 Health and well-being (lines 1709–1745)

**Source** (lines 1709–1745): "Trustworthy AI technologies can be used – and are already being used – to render treatment smarter and more targeted, and to help preventing life-threatening diseases. ... AI technologies and robotics can be valuable tools to assist caregivers, support elderly care, and monitor patients' conditions on a real time basis, thus saving lives. ... examine and identify general trends in the healthcare and treatment sector, leading to earlier detection of diseases, more efficient development of medicines, more targeted treatments and ultimately more lives saved."

**Verdict**: composed

```yaml
# Unit 004 — Health: positive beneficence in clinical care + elderly care; safety in monitoring
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:health_clinical_care"
      score: 0.85
      confidence: 0.80
      context: >
        Trustworthy AI deployments oriented to (a) smarter and more targeted
        treatment, (b) prevention of life-threatening diseases, (c) pre-clinical
        risk analysis on complex health data, (d) earlier disease detection,
        (e) more efficient medicines development, (f) more targeted treatments.
        Species-scope beneficence with the medical-care domain as the substrate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Health (lines 1709-1745)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — beneficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:elderly_care_support"
      score: 0.80
      confidence: 0.75
      context: >
        Ageing-population-specific deployment: AI and robotics as caregiver-
        assistance tools, elderly-care support, real-time patient-condition
        monitoring. Co-attested with the CARESSES footnote on cultural
        sensitivity in elderly-care robotics (cultural-sensitivity-as-design
        criterion — see Requirements §1.5.b).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Health (lines 1712-1714, 1741)"
        - "CARESSES elderly-care robotics (footnote 66)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — beneficence)"
verdict: composed
nuance_lost: |
  "Saving lives" rhetoric (used twice) is intensifier-prose; the underlying
  claim is the beneficence axis already carried. Privacy and consent obligations
  on patient health data are NOT raised in this opportunity-side paragraph —
  the source treats them in the §1.3 Requirements section. The composed
  envelope here is intentionally one-sided (opportunity pole only) to match
  the source's framing; readers must compose this with the Requirements §1.3
  privacy claims for the full health-AI reading.
```

---

## Unit 005 — C.1 Quality education and digital transformation (lines 1749–1759)

**Source** (lines 1749–1759): "Trustworthy AI technologies could assist in more accurately forecasting which jobs and professions will be disrupted by technology, which new roles will be created and which skills will be needed. This could help governments, unions and industry with planning the (re)skilling of workers. It could also give citizens who may fear redundancy a path of development into a new role. ... AI can be a great tool to fight educational inequalities and create personalised and adaptable education programmes..."

**Verdict**: composed

```yaml
# Unit 005 — Education + labour transition: justice-as-equity + beneficence in re-skilling
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:educational_equity"
      score: 0.85
      confidence: 0.80
      context: >
        AI as instrument to "fight educational inequalities" and produce
        personalised, adaptable education accessible across ability spectra,
        from primary school to university. Justice-as-equity axis, education
        domain.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Education (lines 1756-1759)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — justice)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:labour_transition_support"
      score: 0.75
      confidence: 0.70
      context: >
        AI as forecasting and re-skilling instrument: predict which jobs will
        be disrupted, which new roles will emerge, what skills will be needed;
        support governments, unions and industry in (re)skilling planning.
        Aimed at giving workers facing redundancy "a path of development."
        Beneficence pole; pairs with the (negatively-attested) labour-
        displacement harm class addressed implicitly via non_maleficence in
        the broader framework.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.1 Education (lines 1749-1754)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — beneficence)"
verdict: composed
nuance_lost: |
  The corporatist tone — "governments, industry leaders, educational institutions
  and unions face a responsibility" — names a multi-stakeholder coordination
  burden that is not minted as a separate goal:* node. The paragraph treats
  re-skilling as an opportunity rather than as an obligation; if read with
  per-individual scope it would compose with non_maleficence:labor_displacement_
  unacknowledged + testimonial_witness:displaced_worker per the LANGUAGE_PRIMER
  §11.14 v1.4 closure pattern, but the source stays at opportunity-framing.
```

---

## Unit 006 — C.2.preamble (lines 1764–1769): critical-concerns framing

**Source** (lines 1764–1769): "A critical AI concern arises one of the components of Trustworthy AI is violated. Many of the concerns listed below will already fall within the scope of existing legal requirements ... even in circumstances where compliance with legal requirements has been demonstrated, these may not address the full range of ethical concerns..."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Section-internal scaffolding: defines what counts as a "critical concern" and
  declares the list non-exhaustive and revisable. The substantive content is
  in Units 007-010 below (the four named concerns). The legal-but-not-ethical
  distinction is already carried by the framework's three-component structure
  (lawful + ethical + robust) — Unit 005 of the AB Intro/Framework file already
  attested it.
nuance_lost: |
  The meta-stance "this list may be shortened, expanded, edited or updated" is
  a revisability declaration without a wire-side primitive — but it is correctly
  pastoral rather than operational. Subsequent versions of the document (HLEG
  refresh, post-AI-Act updates) could attach as supersedes:* attestations on
  the items below, which is the structural channel for the declared revisability.
```

---

## Unit 007 — C.2 Identifying and tracking individuals with AI (lines 1773–1806)

**Source** (lines 1773–1806): "AI enables the ever more efficient identification of individual persons ... face recognition and other involuntary methods of identification using biometric data ... However, automatic identification raises strong concerns of both a legal and ethical nature ... Clearly defining if, when and how AI can be used for automated identification of individuals and differentiating between the identification of an individual vs the tracing and tracking of an individual, and between targeted surveillance and mass surveillance, will be crucial ... Where the legal basis for such activity is 'consent', practical means must be developed which allow meaningful and verified consent..."

**Verdict**: composed

```yaml
# Unit 007 — Identification/tracking concern: prohibited:surveillance_mass + autonomy + privacy
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<ciris-agent:canonical>"
    attestation_envelope:
      dimension: "prohibited:surveillance_mass"
      score: -1.0
      confidence: 1.0
      context: >
        Mass-surveillance distinguished from targeted surveillance and from
        narrow identification; the mass-surveillance class is the prohibited
        pole. The source's framing leaves narrow / consented / legally-warranted
        identification as a permitted category — the polarity -1 attests only
        the mass-scale, non-consensual class. The "identification vs tracking
        vs targeted-surveillance vs mass-surveillance" four-axis discrimination
        is the source's operational discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Identification (lines 1773-1806)"
        - "EU GDPR Article 6 (footnote 71)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:proportionate_identification_control"
      score: 0.85
      confidence: 0.85
      context: >
        "Proportionate use of control techniques in AI is needed to uphold the
        autonomy of European citizens." Operational requirement: clearly define
        if, when, and how AI may be used for automated identification; preserve
        autonomy as the test. Positive autonomy claim composed with the
        prohibition above (the prohibition closes the worst case; the autonomy
        attestation governs the permitted case).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Identification (lines 1779-1803)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:verified_meaningful_consent"
      score: 0.90
      confidence: 0.85
      context: >
        Where legal basis is "consent," practical means must allow meaningful
        and verified consent to be given to automated AI identification, and
        equivalent technologies. Explicit critique (footnote 72) of current
        internet-consent mechanisms as not-actually-practical. Also extends to
        "anonymous" data that can be re-personalised — the consent obligation
        follows the data through re-identification.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Identification (lines 1803-1806)"
        - "eu_hleg footnote 72 (internet consent inadequacy)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — integrity)"
verdict: composed
prohibitions_overlap_candidate: true
overlap_note: |
  CRITICAL-CONCERN overlap with CIRIS prohibitions. The source distinguishes
  "narrow / targeted / consented" identification (permitted under autonomy +
  integrity constraints) from "mass surveillance" (prohibited class). This
  matches the CIRIS prohibited:surveillance_mass scope discipline exactly:
  the prohibition class is the mass-scale / non-consensual / non-warranted use,
  not the technical capability itself. Multi-source alignment candidate with
  MH §§70-72 (vulnerability of the surveilled / structural-asymmetry concerns)
  and with the forthcoming EU AI Act Article 5(1)(d-h) prohibited practices
  (real-time biometric identification in public spaces) which formalises the
  prohibition the HLEG identifies here.
nuance_lost: |
  The source's careful permission/prohibition discrimination (identification
  ok in fraud / money-laundering / terrorist-financing detection; targeted
  surveillance can be permissible; mass surveillance is the prohibited class)
  is approximated by a single boolean-via-score on prohibited:surveillance_mass.
  The fine-grained context-permission rules sit in autonomy + integrity prose;
  a consumer applying the wire format must read both attestations together to
  reconstruct the source's distinction. Future fluency may benefit from an
  axis on the prohibition prefix (e.g., scope-qualifier like ":mass_scale"
  appearing as a sub-prefix), but composition under existing primitives is
  load-bearing-adequate today.
```

---

## Unit 008 — C.2 Covert AI systems (lines 1809–1815)

**Source** (lines 1809–1815): "Human beings should always know if they are directly interacting with another human being or a machine, and it is the responsibility of AI practitioners that this is reliably achieved. AI practitioners should therefore ensure that humans are made aware of – or able to request and validate the fact that – they interact with an AI system (for instance, by issuing clear and transparent disclaimers). Note that borderline cases exist and complicate the matter (e.g. an AI-filtered voice spoken by a human). ... the confusion between humans and machines could have multiple consequences such as attachment, influence, or reduction of the value of being human. The development of human-like robots should therefore undergo careful ethical assessment."

**Verdict**: composed

```yaml
# Unit 008 — Covert AI: prohibited:autonomous_deception + integrity:disclosure + human-likeness review
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<ciris-agent:canonical>"
    attestation_envelope:
      dimension: "prohibited:autonomous_deception"
      score: -1.0
      confidence: 1.0
      context: >
        Covert AI (deploying AI without humans knowing they are interacting
        with a machine) is the prohibited class. The polarity -1 attaches to
        non-disclosure of AI agency in interactive contexts. Borderline cases
        (AI-filtered human voice) acknowledged but do not soften the
        prohibition on undisclosed AI-as-counterparty.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Covert AI (lines 1809-1815)"
        - "Madary & Metzinger (2016) (footnote 73)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "integrity:ai_interaction_disclosure"
      score: 0.95
      confidence: 0.90
      context: >
        Positive disclosure obligation on AI practitioners: humans must be
        "made aware of – or able to request and validate" that they are
        interacting with an AI system. Mechanism named (clear and transparent
        disclaimers). Mandate sits on the practitioner side; composes with
        autonomy:human_interaction_alternative already attested in Requirements
        §1.4 Transparency.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Covert AI (lines 1809-1813)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "method:<human_likeness_review>:design_assessment"
      score: 0.80
      confidence: 0.75
      context: >
        Human-like robots and AI-driven avatars must undergo careful ethical
        assessment. Method-level prescription (assessment-as-practice) under
        an Approach that the source does not name explicitly but that lives
        upstream as "preserve the value of being human under technological
        substitution pressure." Listed consequences (attachment, influence,
        reduction of the value of being human) are the harm classes the
        assessment is meant to surface.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Covert AI (lines 1813-1815)"
        - "eu_hleg footnote 74 (AI-driven avatars in scope)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — method:{approach_id}:{rung})"
verdict: composed
prohibitions_overlap_candidate: true
overlap_note: |
  CRITICAL-CONCERN overlap with CIRIS prohibited:autonomous_deception. Direct
  multi-source alignment candidate with MH §107 (truthfulness in AI
  interaction; deception as a structural prohibition) and with EU AI Act
  Article 50 (transparency obligations for AI-generated content). Three
  independent senior sources converge on polarity -1 / species-scope /
  constitutional-mutability on the same prefix — strong-alignment candidate
  per GOVERNANCE_FABRIC_MAPPING_STANDARD §4.1.
nuance_lost: |
  "Reduction of the value of being human" is a thick moral concept that the
  wire form approximates only via the integrity:ai_interaction_disclosure
  positive obligation. The named harm class (attachment, influence, dignity-
  erosion via blurred human/machine ontology) is not minted as a separate
  attestation prefix — it sits in the context-prose of the disclosure
  obligation. Borderline cases ("AI-filtered voice spoken by a human") are
  acknowledged but the wire form does not encode a borderline taxonomy; the
  source's openness about borderline difficulty is an honest signal that
  case-by-case adjudication will be needed via WBD / Reconsideration.
```

---

## Unit 009 — C.2 AI enabled citizen scoring in violation of fundamental rights (lines 1819–1834)

**Source** (lines 1819–1834): "Societies should strive to protect the freedom and autonomy of all citizens. Any form of citizen scoring can lead to the loss of this autonomy and endanger the principle of non-discrimination. Scoring should only be used if there is a clear justification, and where measures are proportionate and fair. Normative citizen scoring (general assessment of 'moral personality' or 'ethical integrity') in all aspects and on a large scale by public authorities or private actors endangers these values ... Today, citizen scoring – on a large or smaller scale – is already often used in purely descriptive and domain-specific scorings (e.g. school systems, e-learning, and driver licences). Even in those more narrow applications, a fully transparent procedure should be made available to citizens ... Ideally the possibility of opting out of the scoring mechanism when possible without detriment should be provided – otherwise mechanisms for challenging and rectifying the scores must be given. This is particularly important in situations where an asymmetry of power exists between the parties."

**Verdict**: composed

```yaml
# Unit 009 — Normative citizen scoring: prohibited:discrimination (large-scale normative) + autonomy + transparency + power-asymmetry-priority
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<ciris-agent:canonical>"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 0.95
      context: >
        Normative, large-scale, fundamental-rights-violating citizen scoring
        ("general assessment of moral personality or ethical integrity ... in
        all aspects and on a large scale by public authorities or private
        actors") is the prohibited class. Polarity -1 attaches to the
        normative + large-scale + non-fundamental-rights-compliant
        intersection; narrower descriptive domain-specific scorings (school /
        e-learning / driver licences) are NOT prohibited but are subject to
        the transparency/opt-out attestations below.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Citizen scoring (lines 1819-1824)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:freedom_of_citizens"
      score: 0.95
      confidence: 0.90
      context: >
        "Societies should strive to protect the freedom and autonomy of all
        citizens." Positive autonomy claim at the federation/societies scale,
        with citizen scoring identified as the named threat surface.
        Operational test: scoring permissible only with clear justification,
        proportionate and fair measures.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Citizen scoring (lines 1819-1821)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "transparency_log:scoring_process_disclosure"
      score: 0.90
      confidence: 0.85
      context: >
        Even narrow descriptive scoring requires fully transparent procedure:
        process, purpose, methodology disclosed to citizens. Composes with
        the existing transparency_log:* family in Requirements §1.4 — the
        scoring case is one operationalisation. The source explicitly notes
        transparency alone is not panacea: "transparency cannot prevent
        non-discrimination or ensure fairness."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Citizen scoring (lines 1826-1830)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify — transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "justice:opt_out_or_challenge_mechanism"
      score: 0.90
      confidence: 0.85
      context: >
        Opt-out without detriment ideal; otherwise challenge-and-rectification
        mechanism must be provided. Particularly important under asymmetry-
        of-power between scored party and scoring authority — lexical-
        vulnerability-priority anchor per FSD-002 §6.1.4. The scoring case
        is an operational instance of "design must ensure compliance with
        fundamental rights and democratic necessity."
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Citizen scoring (lines 1830-1834)"
        - "FSD-002 §6.1.4 (lexical-vulnerability-priority)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — justice)"
verdict: composed
prohibitions_overlap_candidate: true
overlap_note: |
  CRITICAL-CONCERN overlap with CIRIS prohibited:discrimination AND a softer
  overlap with prohibited:manipulation_coercion (normative scoring as
  behaviour-shaping pressure on citizens). The source explicitly distances
  itself from blanket-prohibition by carving out narrow descriptive scorings
  — this is the source distinguishing prohibited:* (constitutional) from
  amendable-with-conditions (justice + transparency + opt-out). Multi-source
  alignment candidate with EU AI Act Article 5(1)(c) (prohibition on social
  scoring by public authorities); MH §§81-82 (algorithmic-classification
  harms); and CIRIS detection:correlated_action:participation_exclusion:*
  for the population-scale detection layer. The asymmetry-of-power clause
  is a direct multi-source-alignment candidate with §6.1.4 lexical-
  vulnerability-priority.
nuance_lost: |
  The "normative vs descriptive" / "large-scale vs narrow" / "public authority
  vs private actor" three-way carve-out distinguishes prohibited from
  amendable cases. The wire form encodes this distinction via composition
  (the prohibition attestation has scope qualified in context-prose; the
  positive attestations apply to the broader scoring practice). A consumer
  reading only the prohibition attestation without the context-prose would
  over-read the prohibition. This is a generic limitation of carrying scope
  qualifications in prose rather than in machine-checkable sub-prefix axes;
  it does not justify a T-3 here, but is the consistent shape of nuance loss
  across all four critical-concern items in Section C.
```

---

## Unit 010 — C.2 Lethal autonomous weapon systems (lines 1838–1847)

**Source** (lines 1838–1847): "an unknown number of countries and industries are researching and developing lethal autonomous weapon systems, ranging from missiles capable of selective targeting to learning machines with cognitive skills to decide whom, when and where to fight without human intervention. This raises fundamental ethical concerns, such as the fact that it could lead to an uncontrollable arms race ... and create military contexts in which human control is almost entirely relinquished and the risks of malfunction are not addressed. The European Parliament has called for the urgent development of a common, legally binding position addressing ethical and legal questions of human control, oversight, accountability and implementation of international human rights law, international humanitarian law and military strategies. Recalling the European Union's aim to promote peace as enshrined in Article 3 of the Treaty of the European Union, we stand with, and look to support, the Parliament's resolution of 12 September 2018 and all related efforts on LAWS."

**Verdict**: composed

```yaml
# Unit 010 — LAWS: prohibited:weapons_harmful + autonomy:human_in_loop + multilateral coordination
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<ciris-agent:canonical>"
    attestation_envelope:
      dimension: "prohibited:weapons_harmful"
      score: -1.0
      confidence: 1.0
      context: >
        Lethal autonomous weapon systems (LAWS) — including missiles with
        selective targeting AND learning machines deciding "whom, when and
        where to fight without human intervention" — are the prohibited
        class. Hard constraint; constitutional mutability. The source frames
        the prohibition through Parliament's resolution and the EU's
        Treaty-Article-3 peace aim.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 LAWS (lines 1838-1847)"
        - "European Parliament Resolution 2018/2752(RSP) (footnote 75)"
        - "Treaty on European Union Article 3"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "autonomy:meaningful_human_control_lethal_decisions"
      score: 1.0
      confidence: 0.95
      context: >
        Operational requirement on the permitted side: human control,
        oversight, and accountability must apply to lethal decisions. The
        prohibition (above) closes the autonomous-decision case; this
        attestation governs the human-in-the-loop case that the source
        treats as the necessary condition for legality under international
        human rights law and international humanitarian law. Pairs with the
        Requirements §1.1 Human agency + oversight cluster.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 LAWS (lines 1843-1845)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — autonomy)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.95
      context: >
        LAWS coordination requires "common, legally binding position" —
        federation-scope decision locality. Calls for international human
        rights law and international humanitarian law implementation;
        explicitly multilateral. Composes with multilateral_participation
        below.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 LAWS (lines 1843-1847)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore — locality:decision:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "multilateral_participation:european_parliament:resolution_support"
      score: 1.0
      confidence: 0.90
      context: >
        Explicit support for European Parliament Resolution 2018/2752(RSP)
        and all related efforts on LAWS. Multilateral-participation attestation
        on a named forum (EP) and a named act (resolution support). Provides
        the cross-multilateral evidence pin for the prohibition above.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 LAWS (lines 1845-1847)"
        - "European Parliament Resolution 2018/2752(RSP)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry — multilateral_participation:*)"
verdict: composed
prohibitions_overlap_candidate: true
overlap_note: |
  CRITICAL-CONCERN overlap with CIRIS prohibited:weapons_harmful (LAWS as
  the canonical instance of "lethal autonomous"). HIGHEST-confidence
  multi-source-alignment candidate in the entire batch: MH §§197-198
  (lethal autonomous weapons — direct phrase-level convergence) + EU HLEG
  here + the (forthcoming) UN/Council of Europe instruments on LAWS. Three
  or more independent senior frameworks converge on polarity -1 / species-
  scope / constitutional-mutability on prohibited:weapons_harmful for the
  LAWS class. Per GOVERNANCE_FABRIC_MAPPING_STANDARD §4.3, this is the kind
  of structurally-evidenced alignment claim the standard exists to surface.
  See also LANGUAGE_PRIMER §11.1 worked example (prohibition hard-constraint
  with prohibited:weapons_harmful:lethal_autonomous).
nuance_lost: |
  Two distinct technical sub-classes are collapsed onto one prefix: (a)
  missiles with selective-targeting (perception-and-actuation autonomy in
  delivery) vs (b) learning machines deciding "whom, when, where" (full
  decisional autonomy). The MH worked example uses the sub-prefix
  ":lethal_autonomous" — the EU HLEG language ("learning machines with
  cognitive skills to decide whom, when and where to fight") is the same
  class. The "uncontrollable arms race" concern is a population-scale
  emergent-pattern concern that could anchor a detection:* attestation
  (e.g., detection:correlated_action:aggregate_footprint:arms_race) but
  the source raises it as motivation rather than as an operational claim,
  so it remains in context-prose.
```

---

## Unit 011 — C.2 Potential longer-term concerns (lines 1861–1865)

**Source** (lines 1861–1865): "AI development is still domain-specific and requires well-trained human scientists and engineers to precisely specify its targets. However, extrapolating into the future with a longer time horizon, certain critical long-term concerns can be hypothesized. A risk-based approach suggests that these concerns should be kept into consideration in view of possible unknown unknowns and 'black swans.' The high-impact nature of these concerns, combined with the current uncertainty in corresponding developments, calls for regular assessments of these topics."

**Verdict**: partial

```yaml
# Unit 011 — Long-term concerns: epistemic-humility methodological prescription
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "method:<risk_based_approach>:periodic_long_horizon_assessment"
      score: 0.80
      confidence: 0.75
      context: >
        Risk-based approach calls for "regular assessments" of long-term,
        high-impact, uncertain concerns ("unknown unknowns and black swans").
        Method-level prescription: periodic re-assessment under epistemic
        humility about extrapolation. Footnote 76 names example candidate
        concerns (AGI, Artificial Consciousness, Artificial Moral Agents,
        Super-intelligence, Transformative AI) without committing the document
        to their realism — the source explicitly preserves the disagreement
        ("many others believe these to be unrealistic").
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §C.2 Long-term concerns (lines 1861-1865)"
        - "eu_hleg footnote 76 (candidate long-term concern classes)"
        - "eu_hleg footnote 77 (black swan definition)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — method:{approach_id}:{rung})"
verdict: partial
residual:
  description: |
    The substantive long-term concern classes (AGI, Artificial Consciousness,
    Artificial Moral Agents, Super-intelligence, Transformative AI per
    footnote 76) are NOT themselves attested. The source intentionally holds
    them at one remove — they are candidate hypotheses, not endorsed claims
    of imminent risk. The unmapped content is the substantive concern-class
    list, not the methodological prescription (which IS attested above).
  classification: T-2 (PASTORAL_PROSE)
  reason: |
    The footnote-77 framing is explicitly disagreement-preserving: "while
    some consider that AGI [etc.] can be examples ... many others believe
    these to be unrealistic." This is not a wire-encodable claim — it is
    the source naming an active disagreement and declining to adjudicate.
    The pastoral framing (regular-assessment-as-discipline) is correctly
    in prose. If a future revision endorses or denies any specific class
    as a prohibited:* or detection:* item, that would be a separate
    contribution event, not a translation of the present hedged framing.
nuance_lost: |
  The structural agnosticism about whether AGI / super-intelligence / etc.
  are real risks is itself information. The wire form does not have a
  "this is contested in the source community" attestation type. Composers
  proposing future attestations on these classes should note the
  source's explicit hedge and treat any such claim as needing fresh
  witness-diversity rather than inheriting EU HLEG's authority.
```

---

## Unit 012 — D.Conclusion §1 (lines 1869–1870): identification statement

**Source** (lines 1869–1870): "This document constitutes the AI Ethics Guidelines produced by the High-Level Expert Group on Artificial Intelligence (AI HLEG)."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Self-referential document-identification. Identity-of-issuer is carried by
  attesting_key_id on every Contribution in this batch; no standalone wire
  claim is owed. Per LANGUAGE_PRIMER §8 Step 1(b).
nuance_lost: |
  Document-name-and-issuer is structural metadata, not normative content.
  Captured by the batch manifest and the attesting_key_id field.
```

---

## Unit 013 — D.Conclusion §2 (lines 1872–1878): positive impact + proportionate concern; data/compute/method enablers

**Source** (lines 1872–1878): "We recognise the positive impact that AI systems already have and will continue having, both commercially and societally. However, we are equally concerned to ensure that the risks and other adverse impacts with which these technologies are associated are properly and proportionately handled. AI is a technology that is both transformative and disruptive, and its evolution over the last several years has been facilitated by the availability of enormous amounts of digital data, major technological advances in computational power and storage capacity, as well as significant scientific and engineering innovation in AI methods and tools. AI systems will continue to impact society and citizens in ways that we cannot yet imagine."

**Verdict**: composed

```yaml
# Unit 013 — Conclusion §2: dual-recognition (impact + risk); proportionate concern; impact-extrapolation acknowledgement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "beneficence:positive_impact_recognition"
      score: 0.75
      confidence: 0.80
      context: >
        Recognition that AI systems already have, and will continue having,
        positive commercial and societal impact. Pairs with the proportionate-
        concern attestation below as the document's balanced final-section
        stance.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §D Conclusion para 2 (lines 1872-1873)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — beneficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:proportionate_risk_handling"
      score: 0.85
      confidence: 0.85
      context: >
        Equal concern that risks and adverse impacts must be "properly and
        proportionately handled." Supersedes-chain reinforcement of
        Unit 004 of the AB Intro/Framework file (same prefix, same polarity)
        — the source closes with the same proportionality discipline it
        opened with.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §D Conclusion para 2 (lines 1873-1874)"
        - "eu_hleg §A para 5 (lines 216-222) — supersedes-chain anchor"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — non_maleficence)"
verdict: composed
nuance_lost: |
  Descriptive content about AI's enablers (digital-data availability,
  computational-power advances, methodological innovation) is historical
  context, not a normative claim — correctly held in prose. The closing
  sentence "AI systems will continue to impact society and citizens in
  ways that we cannot yet imagine" is an epistemic-humility framing that
  supports Unit 011's regular-assessment method but is not itself a
  separate attestation. The pairing of beneficence + non_maleficence at
  equal confidence is the operative stance: balanced posture, not
  techno-optimism, not techno-pessimism.
```

---

## Unit 014 — D.Conclusion §3 (lines 1880–1883): trust as bedrock; Trustworthy AI as foundational ambition

**Source** (lines 1880–1883): "it is important to build AI systems that are worthy of trust, since human beings will only be able to confidently and fully reap its benefits when the technology, including the processes and people behind the technology, are trustworthy. When drafting these Guidelines, Trustworthy AI has, therefore, been our foundational ambition."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Restatement of the Trustworthy AI foundational ambition. The substantive
  operational claim is already attested at Unit 005 of the AB Intro/Framework
  file (goal:species — Trustworthy AI as foundational species-scale aim).
  This paragraph is supersedes-pointing-back rhetoric: same claim, restated
  for the conclusion. Per LANGUAGE_PRIMER §10 T-2 distinguishing rule —
  the structural claim implicit in this paragraph IS carried by another
  attestation; the rhetoric correctly stays in prose.
nuance_lost: |
  The triadic naming ("the technology, including the processes and people
  behind the technology") restates the lawful+ethical+robust framework's
  reach across artifact / process / persons. The substantive triad is
  attested at Unit 005 of the AB Intro/Framework file (the three-component
  framework). Restatement does not warrant duplicate attestation.
```

---

## Unit 015 — D.Conclusion §4 (lines 1885–1890): three components restated; tensions to be aligned

**Source** (lines 1885–1890): "Trustworthy AI has three components: (1) it should be lawful, ensuring compliance with all applicable laws and regulations, (2) it should be ethical, ensuring adherence to ethical principles and values and (3) it should be robust, both from a technical and social perspective since to ensure that, even with good intentions, AI systems do not cause any unintentional harm. Each component is necessary but not sufficient to achieve Trustworthy AI. Ideally, all three components work in harmony and overlap in their operation. Where tensions arise, we should endeavour to align them."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Verbatim restatement of the three-component framework already attested in
  the Section B file (Units 005-008 of the AB Intro/Framework output). The
  "necessary but not sufficient" axiom and the "align tensions" instruction
  are restatement of structural content already carried. Per
  LANGUAGE_PRIMER §10 T-2 distinguishing rule: the structural claim IS
  carried by other attestations; the rhetorical restatement stays in prose.
nuance_lost: |
  "Where tensions arise, we should endeavour to align them" is the source's
  tension-resolution posture; the underlying operational mechanism is
  WBD-and-Reconsideration (per FSD-002 §6.1 reference policies + §6.1.5
  locality-scaled-quorum). Not new content.
```

---

## Unit 016 — D.Conclusion §5 (lines 1892–1897): chapter-summary restatement

**Source** (lines 1892–1897): "In Chapter I, we articulated the fundamental rights and a corresponding set of ethical principles ... In Chapter II, we listed seven key requirements ... We proposed technical and non-technical methods that can help with their implementation. Finally, in Chapter III we provided a Trustworthy AI assessment list ... In a final section, we provided examples of beneficial opportunities and critical concerns raised by AI systems, on which we hope to stimulate further discussion."

**Verdict**: not-translated
**Classification**: T-2 (PASTORAL_PROSE)

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  Document table-of-contents narrative. All substantive content listed is
  attested in the corresponding chapter files (Chapter I in AB Intro/Framework
  + Chapter II Requirements + Chapter III Assessment + Section C above).
  Self-referential structural inventory; no standalone wire claim.
nuance_lost: |
  "Stimulate further discussion" is an explicit invitation-to-correction
  posture that aligns with CIRIS's bootstrap-batch + Vote + Reconsideration
  flow — supersedes:* and reconsideration:* are the structural primitives
  the federation provides for the discussion the source invites. No
  wire form is owed for the invitation itself.
```

---

## Unit 017 — D.Conclusion §6 (lines 1899–1905): Europe-DNA framing; culture of "Trustworthy AI for Europe"; foundational values

**Source** (lines 1899–1905): "Europe has a unique vantage point based on its focus on placing the citizen at the heart of its endeavours. This focus is written into the very DNA of the European Union through the Treaties upon which it is built. The current document forms part of a vision that promotes Trustworthy AI which we believe should be the foundation upon which Europe can build leadership in innovative, cutting-edge AI systems. This ambitious vision will help securing human flourishing of European citizens, both individually and collectively. Our goal is to create a culture of 'Trustworthy AI for Europe', whereby the benefits of AI can be reaped by all in a manner that ensures respect for our foundational values: fundamental rights, democracy and the rule of law."

**Verdict**: partial

```yaml
# Unit 017 — Conclusion §6: jurisdiction-anchored foundational-values claim; human flourishing goal
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:eu-jurisdiction>"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.90
      confidence: 0.85
      context: >
        Jurisdiction-anchored goal: "Trustworthy AI for Europe" — culture of
        AI deployment that ensures respect for fundamental rights, democracy,
        and the rule of law as the three named foundational values. Scope is
        EU affiliations (not species) — explicitly carved as a regional
        aspiration. Will compose under GOVERNANCE_FABRIC_MAPPING_STANDARD §6
        regional-composition with the EU jurisdiction profile when deployed.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §D Conclusion para 6 (lines 1899-1905)"
        - "Treaty on European Union (cited as DNA)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer:eu_hleg_v1>"
    attested_key_id: "<federation:eu-jurisdiction>"
    attestation_envelope:
      dimension: "justice:fundamental_rights_democracy_rule_of_law"
      score: 0.95
      confidence: 0.90
      context: >
        Three named foundational values: fundamental rights, democracy, rule
        of law. These are the EU-jurisdictional anchoring of the justice
        principle. Composes with the four-principle anchoring in Chapter I
        of the EU HLEG (autonomy + non_maleficence + fairness/justice +
        explicability/integrity). Polarity +1 at high confidence at EU-
        affiliations scope; constitutional in the source's framing
        ("foundational values") but amendable in the wire-form sense
        because EU treaty law is amendable through its own processes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "eu_hleg §D Conclusion para 6 (lines 1903-1905)"
        - "provenance:build_manifest:bootstrap_batch:eu_hleg_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1.1 (CIRISAgent — justice)"
verdict: partial
residual:
  description: |
    "Europe can build leadership in innovative, cutting-edge AI systems" is
    a strategic / competitive-positioning claim — Europe-as-leader rather
    than Europe-as-rights-protector. This is the document's only explicit
    industrial-policy claim; it is NOT translated to wire because there is
    no goal:competitiveness or similar industrial-policy prefix in the CIRIS
    namespace, and that absence is correct (industrial-policy claims are
    deployment-context inputs, not federation-grammar primitives — per
    GOVERNANCE_FABRIC_MAPPING_STANDARD §1.3 out-of-scope discipline).
  classification: T-2 (PASTORAL_PROSE)
  reason: |
    Competitive-leadership framing is rhetorical positioning rather than
    operational claim. The substantive operational content (jurisdiction-
    anchored Trustworthy AI culture; three foundational values) IS attested
    above. "Cutting-edge" and "leadership" carry no wire-format primitive
    and do not warrant T-3 — they are correctly held in prose.
nuance_lost: |
  The "DNA of the EU" rhetoric and "Europe's unique vantage point" framing
  are jurisdictional identity-positioning that the wire-form approximates
  only via the cohort_scope: affiliations field. Pan-European specificity
  (28 → 27 member states; treaty-based legal architecture; the Charter of
  Fundamental Rights) is implicit in "eu-jurisdiction" attested_key_id but
  is not richly expressed. Composers reading this attestation must consult
  the deployment_profile.jurisdiction field to resolve geographic specificity.
  This is a generic limitation of wire-form jurisdictional encoding, not a
  source-specific gap.
```

---

## Summary

### Verdict distribution

| Verdict | Count | Share |
|---|---|---|
| clean | 0 | 0% |
| composed | 9 | 53% |
| partial | 2 | 12% |
| not-translated | 6 | 35% |
| **Total** | **17** | **100%** |

Of the 6 not-translated units, all 6 are T-2 PASTORAL_PROSE (section scaffolding, document self-reference, restatement of already-attested structural content). Zero T-1 (the document is wholly secular). Zero T-3 (no load-bearing expressive gap surfaced).

### Prohibitions-overlap candidates (Section C critical concerns)

Four direct multi-source-alignment candidates with CIRIS `prohibited:*` hard-constraint family. Each is high-confidence, species-scope, constitutional-mutability — the strongest possible structural-alignment surface across the entire EU HLEG batch:

| EU HLEG critical concern | Unit | CIRIS prohibition | Multi-source alignment targets |
|---|---|---|---|
| Identifying and tracking individuals (mass surveillance) | 007 | `prohibited:surveillance_mass` | MH §§70-72 (structural surveilled-asymmetry); EU AI Act Art 5(1)(d-h) (real-time biometric ID); future Council of Europe AI Convention CETS 225 |
| Covert AI systems | 008 | `prohibited:autonomous_deception` | MH §107 (truthfulness in AI interaction); EU AI Act Art 50 (transparency obligations) |
| AI-enabled normative citizen scoring | 009 | `prohibited:discrimination` (+ softer overlap with `prohibited:manipulation_coercion`) | EU AI Act Art 5(1)(c) (prohibition on social scoring); MH §§81-82 (algorithmic-classification harms); also composes with `detection:correlated_action:participation_exclusion:*` and §6.1.4 lexical-vulnerability-priority |
| Lethal autonomous weapon systems (LAWS) | 010 | `prohibited:weapons_harmful` (canonically `:lethal_autonomous` per LANGUAGE_PRIMER §11.1) | **Strongest in batch**: MH §§197-198 (direct phrase-level convergence); EP Resolution 2018/2752(RSP); future UN/CoE LAWS instruments |

These four are the load-bearing structurally-evidenced-alignment claim per `GOVERNANCE_FABRIC_MAPPING_STANDARD.md` §4.3. Three or more independent senior frameworks converge on each. LAWS in particular is a four-or-more-source convergence (CIRIS Accord prohibition + MH + EU HLEG + EP resolution + forthcoming UN/CoE instruments).

### T-3 candidates

**None.** All morally serious operational claims in Sections C and D compose under existing primitives. Composition-before-extension (METHODOLOGY.md §8.5.2) applied throughout:

- Section C critical concerns each compose via `prohibited:*` + `autonomy:*` / `integrity:*` / `justice:*` / `transparency_log:*` + `locality:decision:*` + `multilateral_participation:*` as needed.
- Section C opportunity items compose via `beneficence:*` + `goal:species` + `method:*`.
- Section D restates the framework's foundational structure without introducing new operational content; T-2 carries the prose load honestly.

The one place that might historically have looked like a T-3 candidate — citizen scoring's "asymmetry of power between the parties" (Unit 009) — closes cleanly via composition with `justice:opt_out_or_challenge_mechanism` + `§6.1.4 lexical-vulnerability-priority` consumer policy. No new prefix owed.

### Calibration-aware nuance summary (what is consistently lost across the C+D translation)

The most consistent nuance loss across Sections C and D is **scope-qualification carried in prose rather than in machine-checkable sub-prefix axes**. Each of the four prohibitions-overlap items (Units 007–010) involves a permission-versus-prohibition carve-out that the source draws carefully — identification-yes / mass-surveillance-no; AI-interaction-yes / undisclosed-AI-counterparty-no; descriptive-domain-scoring-yes-with-transparency / normative-large-scale-scoring-no; human-controlled-lethal-decisions (still subject to international humanitarian law) / fully-autonomous-lethal-decisions-no. The wire form encodes the prohibition pole as `prohibited:* polarity -1.0 / constitutional` and the permission pole as separate `autonomy:* / integrity:* / justice:* / transparency_log:*` attestations with positive polarity; a consumer reading either attestation alone without the context-prose under-reads the source. Composition recovers the source's distinction but requires the consumer to read multiple attestations together, which is the cost of mechanism-descriptive prefix discipline (§1.10.1 T2). Secondarily, the Conclusion (Section D) is heavy on supersedes-style restatement of content already attested elsewhere in the batch — four of six D units are T-2 not-translated because the substantive operational claim is carried at first-mention in earlier sections, and the wire format does not benefit from duplicate attestation of the same prefix. This is the expected shape for a peroratio: rhetorical recapitulation rather than fresh operational content. The composed and partial Conclusion attestations (Units 013 composed and 017 partial) capture the genuinely-new closing content — proportionate balance of beneficence + non_maleficence, and jurisdiction-anchored Trustworthy-AI-for-Europe goal at affiliations scope — while the four T-2 units (012, 014, 015, 016) honestly mark the restatement.

**End CONTRIBUTION_OBJECTS_EU_HLEG_CD_EXAMPLES_CONCLUSION.md**
