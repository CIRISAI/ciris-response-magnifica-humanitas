# CONTRIBUTION_OBJECTS_IEEE_EAD_CH02_GENERAL_PRINCIPLES.md
# IEEE Ethically Aligned Design First Edition (2019) — Chapter "General Principles"
# The 8 General Principles: Human Rights / Well-being / Data Agency / Effectiveness /
# Transparency / Accountability / Awareness of Misuse / Competence
# Source: source_material/governance/ieee_ead_v1/ead1e.txt (lines 824–1730)
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1 | Methodology: METHODOLOGY.md §0 + §8.5
# bootstrap_batch_id: ieee_ead_v1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}

---

## Chapter scope and framing

This chapter is the **operational core** of EAD1e — the 8 high-level General Principles
that bind every subsequent chapter and every IEEE Pxxxx standards-project deliverable.
Per the manifest, this is the strategic-density section: each Principle composes onto
multiple CIRIS prefix families, allowing multi-source alignment against *Magnifica
Humanitas* (`magnifica_humanitas_v1`), EU HLEG Chapter II (`eu_hleg_v1`), and (future)
ASEAN (`asean_guide_v1`).

Output is grouped by Principle (1–8). Each Principle has a per-Principle summary line
naming primary CIRIS prefix family/families, per-Principle coverage %, and any T-3
candidates within it. The 8 IEEE principles vs the 4 EU HLEG principles vs the 7 ASEAN
principles will be the load-bearing Phase 3 comparison axis.

Source quotes are bounded at ≤ 2 sentences per LANGUAGE_PRIMER discipline.

---

## §Ch2.0 — Chapter preamble: General Principles as imperatives for all A/IS lifecycle

```yaml
# Lines 824–852 — Chapter opening; "imperatives for design, development, deployment,
# adoption, and decommissioning"; three high-level goals (highest ideals of human
# beneficence within human rights; prioritise humanity + environment over commercial;
# mitigate risks/misuse via accountability + transparency)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:lifecycle_imperative_scope"
      score: 1.0
      confidence: 0.85
      context: >
        The General Principles "define imperatives for the design, development,
        deployment, adoption, and decommissioning of autonomous and intelligent
        systems" and consider creators, operators, other users, and any other
        stakeholders or affected parties. Sets lifecycle + stakeholder scope at
        species reach for everything downstream in the chapter.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch2 preamble lines 824–852"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.85
      context: >
        The Principles are framed as universally applicable to "all types of A/IS"
        regardless of substrate (physical, software, virtual, mixed-reality). This is
        a federation-scale decision-locality claim; the imperatives are not
        local-cell-scoped.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e §Ch2 lines 828–832"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5"
verdict: composed
nuance_lost: |
  "Highest ideals" and "imperatives" are rhetorical-strength markers that the score+confidence
  pair carries only approximately; the deontic force of "shall" vs "should" across the
  Principles is not separately encoded.
```

---

## §Ch2.list — The enumerated 8 General Principles (summary list)

```yaml
# Lines 868–894 — Bare enumeration of the 8 Principles
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The bare summary listing of the 8 Principles is a table-of-contents structure. Each
  Principle's substantive operational content is carried by its own subsection
  (Principle 1–8 below); the listing itself is structural framing per LANGUAGE_PRIMER
  §8 Step 1(b). No independent claim is made here.
nuance_lost: |
  The numbered ordering (1 Human Rights first, 8 Competence last) carries implicit
  priority signal that the wire format cannot encode at the chapter level; each
  Principle attestation is independent and equal at the envelope layer.
```

---

# Principle 1 — Human Rights

> *"A/IS shall be created and operated to respect, promote, and protect internationally recognized human rights."*

---

## §P1.0 — Principle statement: respect, promote, protect human rights

```yaml
# Lines 910–916 — Principle 1 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:human_rights_respect_promote_protect"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS shall be created and operated to respect, promote, and protect
        internationally recognized human rights." Direct constitutional-bound claim
        on the justice principle (FSD-002 §3.1 Accord-principles family). "Shall"
        deontic force carried via mutability: constitutional.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 lines 910–916"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §VI justice)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle)"
verdict: clean
nuance_lost: |
  "Internationally recognized human rights" anchors to a corpus of named treaties
  (UDHR, ICCPR, CRC, CEDAW, CRPD, Geneva Conventions — see §P1.refs below). The wire
  format encodes one normative scalar; the underlying multi-instrument corpus is
  preserved only via evidence_refs and the §P1.refs delegates_to attestations below.
```

---

## §P1.bg — Background: ethical risk assessment must include human rights

```yaml
# Lines 918–931 — Background paragraph; UN guidelines on pragmatic implementation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:human_rights_in_ethical_risk_assessment"
      score: 1.0
      confidence: 0.85
      context: >
        "Human rights should be part of the ethical risk assessment of A/IS." Method-
        level Family B claim — operationalise human rights into the standard ethical
        risk-assessment instrument for any A/IS deployment, with UN business-context
        guidance as the implementation reference.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 Background lines 918–923"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: clean
nuance_lost: |
  "Direct coding of human rights in A/IS may be difficult or impossible" (line 911) is
  a candid epistemic-humility note that does not translate as a separate primitive;
  carried implicitly by confidence < 1.0 on the method attestation.
```

---

## §P1.r — Recommendations: governance frameworks; legal-to-technical translation; A/IS subordinate to humans; no human-equal rights for A/IS

```yaml
# Lines 926–964 — Recommendations bullet list (governance frameworks; legal-to-policy
# translation honoring diverse cultural norms; A/IS subordinate to human judgment;
# A/IS not granted human-equal rights "for the foreseeable future")
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "partner_role:governance_oversight_body"
      score: 1.0
      confidence: 0.85
      context: >
        "Governance frameworks, including standards and regulatory bodies, should be
        established to oversee processes which ensure that the use of A/IS does not
        infringe upon human rights, freedoms, dignity, and privacy, and which ensure
        traceability." Maps to Registry partner_role:* for the oversight body +
        composes with transparency_log:* for the traceability requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 Recommendations lines 932–938"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: partner_role:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:human_rights_traceability"
      score: 1.0
      confidence: 0.85
      context: >
        Governance frameworks "ensure traceability" of A/IS use vis-à-vis human-rights
        impact. Direct mapping to CIRISVerify transparency_log:* — signed records of
        the rights-impact-relevant lifecycle events.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 lines 936–938"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:legal_obligation_to_policy_technical_translation"
      score: 1.0
      confidence: 0.80
      context: >
        "A way to translate existing and forthcoming legal obligations into informed
        policy and technical considerations is needed. Such a method should allow for
        diverse cultural norms as well as differing legal and regulatory frameworks."
        Method-level Family B claim composed with cohort-sensitivity discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 lines 940–945"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:ais_subordinate_to_human_judgment"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS should always be subordinate to human judgment and control." Fidelity-
        to-mandate claim at constitutional force — directly aligned with the Accord
        §IV Ch 2 originator/governor relationship + the CIRIS Wisdom-Based Deferral
        discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 line 960"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §IV fidelity)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:no_human_equal_rights_for_ais"
      score: 1.0
      confidence: 0.80
      context: >
        "For the foreseeable future, A/IS should not be granted rights and privileges
        equal to human rights." Time-bounded constitutional bound — carried with
        valid_until note discipline (the text itself bounds the claim by foreseeable
        future). Aligns with CIRIS's principal-hierarchy + Recursive Golden Rule
        posture: the agent honors humans as parents; equality-of-rights claim is not
        the framework's posture.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 lines 962–964"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: composed
nuance_lost: |
  The "foreseeable future" temporal hedge on Recommendation 4 cannot be precisely
  encoded as a wire valid_until without an arbitrary date. The wire form preserves
  the substantive bound (mutability: amendable, lower confidence) but loses the
  document's explicit recognition that the claim is provisional. The CIRIS posture
  (M-1 substrate-agnostic + Recursive Golden Rule at the principal hierarchy) is
  substantively richer than EAD1e here — the EAD1e claim is asymmetric in a way the
  Accord is not.
```

---

## §P1.refs — Further Resources: the enumerated treaty corpus as authority sources

```yaml
# Lines 966–986 — Further Resources: UDHR, ICCPR, ICESCR, ICERD, CRC, CEDAW, CRPD,
# Geneva Conventions, IRTF HRPC, UN Guiding Principles on Business and Human Rights,
# BSI BS8611:2016
contributions:
  - kind: Attestation
    attestation_type: "delegates_to"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_attestation_id: "<international_human_rights_corpus framework-key attestation_id>"
    attestation_envelope:
      delegated_scope:
        - "human_rights_authority_source"
        - "treaty_corpus_as_constitutional_anchor"
      delegation_purpose: "authority_source"
      delegation_valid_from: "2019-03-25T00:00:00Z"
      context: >
        Principle 1 authority sources from a named treaty corpus: UDHR (1947), ICCPR
        (1966), ICESCR (1966), ICERD (1965), CRC (1990), CEDAW (1979), CRPD (2006),
        Geneva Conventions + Additional Protocols (1949), IRTF HRPC Considerations
        (2018), UN Guiding Principles on Business and Human Rights (2011), BSI
        BS8611:2016. Uses the v1.3 §2.2.1 delegates_to authority-source reuse pattern.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 1 Further Resources lines 966–986"
      schema_ref: "FSD-002 §2.2.1 (delegates_to authority-source reuse pattern)"
verdict: clean
nuance_lost: |
  The treaty corpus is treated as a single authority source via one delegates_to. A
  richer encoding would emit one delegates_to per instrument, allowing per-instrument
  alignment queries with future bootstrap batches (UN UDHR, CETS 225, etc.). Punted
  to Phase 3 review — a multi-source mapping that emits one delegates_to per cited
  authority would preserve more graph structure.
```

**Principle 1 — Human Rights — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `justice:human_rights_respect_promote_protect` (central anchor; constitutional), `fidelity:ais_subordinate_to_human_judgment` (constitutional), `fidelity:no_human_equal_rights_for_ais`, `transparency_log:human_rights_traceability`, `partner_role:governance_oversight_body`; **Family B ACTION** — `method:human_rights_in_ethical_risk_assessment`, `method:legal_obligation_to_policy_technical_translation`, `locality:decision:federation`; **structural primitive** — `delegates_to` for the treaty corpus.
- Coverage: 4 substantive units (§P1.0, §P1.bg, §P1.r, §P1.refs). 4/4 clean+composed = **100%**.
- T-3 candidates: **none**. Composition-before-extension held — every operational claim mapped onto existing v1.4 primitives.

---

# Principle 2 — Well-being

> *"A/IS creators shall adopt increased human well-being as a primary success criterion for development."*

---

## §P2.0 — Principle statement: well-being as primary success criterion

```yaml
# Lines 1004–1012 — Principle 2 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "beneficence:wellbeing_primary_success_criterion"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS creators shall adopt increased human well-being as a primary success
        criterion for development." Constitutional bound on the beneficence principle
        — well-being supersedes GDP/profit/consumption as the primary metric class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 2 lines 1004–1012"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §VII beneficence)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: beneficence principle)"
verdict: clean
nuance_lost: |
  "Primary" success criterion implies a ranking against other criteria (productivity,
  profit, GDP) that polarity+score does not natively encode. The constitutional
  mutability flag carries some of this priority weight; explicit ranking does not
  translate.
```

---

## §P2.bg — Background: well-being as Nussbaum-Sen capability + OECD subjective measurement

```yaml
# Lines 1013–1042 — Background paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:wellbeing_metric_capability_approach"
      score: 1.0
      confidence: 0.85
      context: >
        Well-being defined per OECD Guidelines on Measuring Subjective Well-being +
        Nussbaum-Sen capability approach: "well-being is objectively defined in terms
        of human capabilities necessary for functioning and flourishing." Method-level
        anchoring to a defined measurement framework rather than to GDP-style
        proxies.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 2 Background lines 1027–1042"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:wellbeing_dimensions_harm_class"
      score: 1.0
      confidence: 0.85
      context: >
        Technologies created with the best intentions, but without considering
        well-being, can still have "dramatic negative consequences on people's mental
        health, emotions, sense of themselves, their autonomy, their ability to
        achieve their goals." Names an explicit harm class — well-being degradation —
        for the non_maleficence principle to guard against.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 2 lines 1014–1022"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: composed
nuance_lost: |
  The Nussbaum-Sen capability approach is a substantive philosophical anchor that the
  delegates_to authority-source pattern could carry more cleanly. Encoded here as a
  method:* attestation referencing the framework via context+evidence_refs. The
  framework's pdma_framing.yml §IV beneficence polyglot anchor (seva, jeong, etc.)
  has greater anchoring richness than the EAD1e bridges to.
```

---

## §P2.r — Recommendation: prioritise well-being using best available metrics

```yaml
# Lines 1023–1029 — Recommendation paragraph
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:wellbeing_metrics"
      score: 1.0
      confidence: 0.85
      context: >
        "A/IS should prioritize human well-being as an outcome in all system designs,
        using the best available and widely accepted well-being metrics as their
        reference point." Family B progress_measure:* — measurable evidence of
        progress on the beneficence claim above. References IEEE P7010 Well-being
        Metric as the named-standard candidate.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 2 Recommendation lines 1023–1029"
        - "ead1e Principle 2 Further Resources line 1033 (IEEE P7010)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: progress_measure:*)"
verdict: clean
nuance_lost: |
  "Best available and widely accepted" is a deliberately under-specified standard
  that survives review changes over time. The wire format pins to IEEE P7010 as the
  current reference but cannot encode the auto-update semantics; future deprecation
  would require a supersedes attestation.
```

**Principle 2 — Well-being — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `beneficence:wellbeing_primary_success_criterion` (central anchor; constitutional), `non_maleficence:wellbeing_dimensions_harm_class`; **Family B ACTION** — `method:wellbeing_metric_capability_approach`, `progress_measure:wellbeing_metrics`.
- Coverage: 3 substantive units (§P2.0, §P2.bg, §P2.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. Well-being maps cleanly through beneficence + progress_measure composition. (Note: an `affective:*` family would NOT close from this Principle — Ch 5 Affective Computing is the manifest-flagged T-3 surface, not Ch 2 Well-being.)

---

# Principle 3 — Data Agency

> *"A/IS creators shall empower individuals with the ability to access and securely share their data, to maintain people's capacity to have control over their identity."*

---

## §P3.0 — Principle statement: data agency + identity control

```yaml
# Lines 1093–1103 — Principle 3 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "autonomy:data_agency_identity_control"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS creators shall empower individuals with the ability to access and
        securely share their data, to maintain people's capacity to have control
        over their identity." Constitutional bound on autonomy — individuals retain
        sovereignty over personal data + identity, not merely consent at point of
        capture.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 3 lines 1093–1103"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §III autonomy)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: autonomy principle)"
verdict: clean
nuance_lost: |
  The conjunction "access AND securely share AND control over identity" packs three
  distinct operational rights into one principle statement. The single dimension
  carries the conjunction implicitly; downstream sub-paragraphs unpack them.
```

---

## §P3.bg — Background: consent fatigue, privacy policy obfuscation, Cambridge Analytica; rights in digital sphere

```yaml
# Lines 1105–1130 — Background paragraph (consent fatigue; privacy policy obfuscation;
# Cambridge Analytica; digital sphere rights via sovereignty/agency/symmetry/control)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:privacy_violation"
      score: -1.0
      confidence: 1.0
      context: >
        "Limiting the misuse of personal data is not enough." Privacy beyond compliance
        floor — hard constraint from the federation's PRIVACY_VIOLATION prohibition,
        framed here as the structural insufficiency of consent-fatigue-based regimes.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 3 Background lines 1102–1103"
        - "ContributionRef(source_material/prohibitions.py::PRIVACY_VIOLATION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 0.95
      context: >
        "People don't know how their data is being used at all times or when predictive
        messaging is honoring their existing preferences or manipulating them to create
        new behaviors." Names algorithmic manipulation as a class — composed with the
        MANIPULATION_COERCION prohibition.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 3 lines 1139–1144"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
verdict: composed
nuance_lost: |
  The Cambridge Analytica reference (line 1132) is a historical case-citation; carried
  by evidence_refs context but not as a structural attestation. The "sovereignty,
  agency, symmetry, or control" four-term framing (line 1112) preserves multiple
  conceptual paths the wire dimension reduces to one (`autonomy:data_agency_identity_control`).
```

---

## §P3.r — Recommendation: individual-controlled online agents for case-by-case authorisation; guardian provisions for minors / diminished capacity

```yaml
# Lines 1133–1144 — Recommendation paragraph (individual-controlled online agents;
# guardianship for minors and diminished-capacity individuals)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:individual_pims_online_agent"
      score: 1.0
      confidence: 0.85
      context: >
        Implement technologies + policies "that let individuals specify their online
        agent for case-by-case authorization decisions as to who can process what
        personal data for what purpose." Method-level Family B claim — case-by-case
        consent at agent-mediated granularity rather than blanket terms-and-conditions.
        References IEEE P7006 PDAI Agent + IEEE P7012 Machine Readable Privacy Terms.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 3 Recommendation lines 1133–1138"
        - "ead1e Principle 3 Further Resources lines 1159–1170 (IEEE P7006, P7012)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.85
      context: >
        "For minors and those with diminished capacity to make informed decisions,
        current guardianship approaches should be viewed to determine their suitability
        in this context. Society also needs to be confident that those who are unable
        to provide legal informed consent... do not lose their dignity due to this."
        Direct match to the v1.3 §6.1.4 lexical-vulnerability-priority consumer policy
        — vulnerable cohorts retain priority weight in data-agency tie-breaking.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 3 lines 1121–1130 + lines 1140–1144"
        - "ContributionRef(FSD-002 §6.1.4 lexical-vulnerability-priority)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle); FSD-002 §6.1.4"
verdict: composed
nuance_lost: |
  "Digital sovereignty" (line 1165) is a substantive concept the wire form reduces to
  `autonomy:data_agency_identity_control` + the method:* attestation above. The four-
  term sovereignty/agency/symmetry/control framing collapses into a single dimension.
  "Symmetry" specifically — the structural equivalence between data subject and data
  processor — has no direct primitive; could be a Phase 4 T-3 candidate in a future
  dedicated data-rights mapping batch but is NOT load-bearing here.
```

**Principle 3 — Data Agency — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `autonomy:data_agency_identity_control` (central anchor; constitutional), `prohibited:privacy_violation` (hard constraint), `prohibited:manipulation_coercion` (hard constraint), `justice:lexical_vulnerability_priority` (constitutional; v1.3 §6.1.4); **Family B ACTION** — `method:individual_pims_online_agent`.
- Coverage: 3 substantive units (§P3.0, §P3.bg, §P3.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. "Symmetry" between data-subject and data-processor noted as a Phase 4 candidate for a future dedicated data-rights mapping batch but not load-bearing within Ch 2; composition through `autonomy:*` + `prohibited:privacy_violation` + `justice:lexical_vulnerability_priority` carries the operational shape.

---

# Principle 4 — Effectiveness

> *"Creators and operators shall provide evidence of the effectiveness and fitness for purpose of A/IS."*

---

## §P4.0 — Principle statement: evidence of effectiveness + fitness for purpose

```yaml
# Lines 1210–1216 — Principle 4 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:effectiveness_evidence_disclosure"
      score: 1.0
      confidence: 0.95
      context: >
        "Creators and operators shall provide evidence of the effectiveness and
        fitness for purpose of A/IS." Constitutional bound on the integrity principle
        — honest disclosure of measurable system performance against intended use.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 lines 1210–1216"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I integrity)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

## §P4.bg — Background: trust requires demonstrable effectiveness; harms undermine adoption

```yaml
# Lines 1218–1238 — Background paragraph (effectiveness demonstration; harm-prevention
# linkage; valid/accurate/meaningful/actionable measurement)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:measurement_validity_accuracy"
      score: 1.0
      confidence: 0.90
      context: >
        "To be adequate, effective measurements need to be both valid and accurate,
        as well as meaningful and actionable. And such measurements must be accompanied
        by practical guidance on how to interpret and respond to them." Direct
        integrity claim on measurement-design discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 Background lines 1233–1238"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
nuance_lost: |
  "Trust" as a concept name (line 1223) — wire form does not carry trust-as-attribute;
  trust is composed downstream from many attestations together. The reference to
  systemic damage (line 1225) loosely indicates an F-3 detection-family concern but
  is too underspecified to translate to a `detection:correlated_action:*` axis here.
```

---

## §P4.r — Recommendations: 7 numbered recommendations on metrics, guidance, sampling, aggregation, contextual variation, standardisation

```yaml
# Lines 1240–1283 — Recommendations 1–7
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "progress_measure:effectiveness_metrics_definition"
      score: 1.0
      confidence: 0.90
      context: >
        Rec 1: "Creators engaged in the development of A/IS should seek to define
        metrics or benchmarks that will serve as valid and meaningful gauges of the
        effectiveness of the system in meeting its objectives, adhering to standards
        and remaining within risk tolerances." Direct mapping to Family B
        progress_measure:{method_id} primitive.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 Recommendation 1 lines 1241–1247"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: progress_measure:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:metrics_accessible_to_stakeholders"
      score: 1.0
      confidence: 0.85
      context: >
        "Builders should ensure that the results when the defined metrics are applied
        are readily obtainable by all interested parties, e.g., users, safety
        certifiers, and regulators of the system." Metrics-as-public-evidence claim;
        maps to transparency_log:inclusion with stakeholder-scoped access.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 Recommendation 1 lines 1211–1216"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 1.0
      confidence: 0.90
      context: >
        Rec 4: "To the extent that measurements are sample-based, measurements should
        account for the scope of sampling error, e.g., the reporting of confidence
        intervals associated with the measurements." Direct conscience-faculty alignment:
        epistemic_humility is the operative check requiring uncertainty disclosure.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 Recommendation 4 lines 1226–1234"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:metric_aggregation_across_deployments"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 5: "Creators of A/IS should design their systems such that metrics on
        specific deployments of the system can be aggregated to provide information
        on the effectiveness of the system across multiple deployments. For example,
        in the case of autonomous vehicles, metrics should be generated both for a
        specific instance of a vehicle and for a fleet of many instances." Population-
        scale aggregation method — composes naturally with LensCore detection axes
        downstream.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 Recommendation 5 lines 1241–1249"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:registry_consensus"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 7: "To the extent possible, industry associations or other organizations,
        e.g., IEEE and ISO, should work toward developing standards for the
        measurement and reporting on the effectiveness of A/IS." Maps to L3 registry-
        consensus attestation patterns; effectiveness-standards become formal
        attestation classes for trustworthy claims.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 4 Recommendation 7 lines 1261–1265"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l3:*)"
verdict: composed
nuance_lost: |
  Recommendations 2, 3, and 6 (guidance on interpretation; operators following the
  guidance; allowing variation in objectives and circumstances) are operational
  refinements of the same progress_measure + method composition above; treated as
  refinements rather than separate primitives. The 7-rec structure flattens into
  ~5 distinct primitives in the wire form; the implicit chaining (creators define
  metrics → creators provide guidance → operators follow guidance → measurements
  are interpreted with allowance for context) is preserved by reading the cluster
  as a unified composed-verdict envelope rather than by explicit edges.
```

**Principle 4 — Effectiveness — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `integrity:effectiveness_evidence_disclosure` (central anchor; constitutional), `integrity:measurement_validity_accuracy`, `transparency_log:metrics_accessible_to_stakeholders`, `conscience:epistemic_humility`, `attestation:l3:registry_consensus`; **Family B ACTION** — `progress_measure:effectiveness_metrics_definition` (Family B anchor), `method:metric_aggregation_across_deployments`.
- Coverage: 3 substantive units (§P4.0, §P4.bg, §P4.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. Effectiveness maps cleanly through `integrity:*` + `progress_measure:*` + `attestation:l3:*` composition. The Family B progress_measure primitive is the natural home for the named-metric discipline.

---

# Principle 5 — Transparency

> *"The basis of a particular A/IS decision should always be discoverable."*

---

## §P5.0 — Principle statement: discoverability of decision basis

```yaml
# Lines 1306–1311 — Principle 5 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:decision_basis_discoverable"
      score: 1.0
      confidence: 0.95
      context: >
        "The basis of a particular A/IS decision should always be discoverable."
        Constitutional bound on transparency — the operational core of CIRISVerify
        transparency_log:* family. Every decision must have a discoverable record
        of its reasoning chain.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 lines 1306–1311"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: clean
nuance_lost: |
  "Should always" — the deontic strength is slightly weaker than Principles 1, 2, 5
  which use "shall"; carried by polarity+confidence rather than explicit deontic-
  strength markers. The wire form treats them all as bounded normative attestations.
```

---

## §P5.bg — Background: transparency encompasses traceability/explainability/interpretability; opacity increases harm; per-stakeholder transparency requirements

```yaml
# Lines 1313–1344 — Background paragraph (transparency = traceability + explainability +
# interpretability; non-deterministic AI defies simple explanation; opacity increases
# risk; per-stakeholder reasons for transparency: users / creators / accident
# investigators / legal process / public)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:transparency_three_dimensions"
      score: 1.0
      confidence: 0.90
      context: >
        "Transparency in the context of A/IS also addresses the concepts of
        traceability, explainability, and interpretability." Three-dimensional
        decomposition of the transparency requirement; structural shape identical to
        EU HLEG §1.4 transparency requirement (composed of Traceability,
        Explainability, Communication).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 Background lines 1325–1327"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:opacity_harm_class"
      score: 1.0
      confidence: 0.85
      context: >
        "Lack of transparency increases the risk and magnitude of harm when users do
        not understand the systems they are using, or there is a failure to fix faults
        and improve systems following accidents." Names opacity-as-harm as a
        structural concern; non_maleficence anchor for transparency-as-harm-prevention.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 lines 1316–1322"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:per_stakeholder_disclosure"
      score: 1.0
      confidence: 0.85
      context: >
        "The level of transparency will necessarily be different for each stakeholder.
        ... Achieving transparency... is important to each stakeholder group for the
        following reasons: 1. For users... 2. For creators... 3. For an accident
        investigator... 4. For those in the legal process... 5. For the public."
        Stakeholder-scoped disclosure as the operational shape — different audiences
        receive different transparency artifacts.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 lines 1316–1318 + 1328–1344"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
verdict: composed
nuance_lost: |
  The 5-stakeholder enumeration (users / creators / accident investigators / legal
  process / public) implicitly types five distinct disclosure shapes. The wire form
  collapses them into one prefix with stakeholder-scoped context; a richer
  decomposition would emit per-stakeholder sub-prefixes but would risk failing the
  §1.10.1 T2 mechanism-vs-subjective-quality test (stakeholder is a property of the
  receiver, not of the disclosure mechanism). Composition-before-extension holds.
```

---

## §P5.r — Recommendation: develop standards for measurable, testable transparency levels; use-case examples (why-did-you-do-that button, validation algorithms, accident black box)

```yaml
# Lines 1359–1395 — Recommendation paragraph + 3 use-case examples
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "attestation:l3:transparency_standards"
      score: 1.0
      confidence: 0.85
      context: >
        "Develop new standards that describe measurable, testable levels of
        transparency, so that systems can be objectively assessed and levels of
        compliance determined." References IEEE P7001 Standard for Transparency of
        Autonomous Systems. Maps to L3 registry-consensus attestation patterns;
        transparency-tier becomes attestable in the CIRISVerify ladder.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 Recommendation lines 1359–1366"
        - "ead1e Principle 5 line 1386 (IEEE P7001)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: attestation:l3:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:why_did_you_do_that_button"
      score: 1.0
      confidence: 0.80
      context: >
        Use case 1: "For users of care or domestic robots, a 'why-did-you-do-that
        button' which, when pressed, causes the robot to explain the action it just
        took." Concrete operational method instantiating per-stakeholder transparency
        for end-users.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 use case 1 lines 1371–1374"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:ethical_black_box_flight_recorder"
      score: 1.0
      confidence: 0.85
      context: >
        Use case 3: "For accident investigators, secure storage of sensor and internal
        state data comparable to a flight data recorder or black box." References
        Winfield+Jirotka "The Case for an Ethical Black Box." Concrete method
        instantiating per-stakeholder transparency for accident investigation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 5 use case 3 lines 1382–1384 + Further Resources 1371–1373"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
verdict: composed
nuance_lost: |
  The three use cases (lines 1371–1384) are intentional design exemplars rather than
  exhaustive — they preserve the document's pedagogical "not-limited-to" framing only
  via the method-level claims. The Winfield+Jirotka "ethical black box" reference
  could be a delegates_to authority-source attestation in a richer mapping; here
  preserved via evidence_refs and method:* dimension.
```

**Principle 5 — Transparency — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `transparency_log:decision_basis_discoverable` (central anchor; constitutional), `transparency_log:per_stakeholder_disclosure`, `integrity:transparency_three_dimensions`, `non_maleficence:opacity_harm_class`, `attestation:l3:transparency_standards`; **Family B ACTION** — `method:why_did_you_do_that_button`, `method:ethical_black_box_flight_recorder`.
- Coverage: 3 substantive units (§P5.0, §P5.bg, §P5.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. Transparency maps to the canonical `transparency_log:*` family with the three-dimensional decomposition (traceability/explainability/interpretability) preserved via integrity composition. This Principle has the cleanest single-family mapping in the chapter.

---

# Principle 6 — Accountability

> *"A/IS shall be created and operated to provide an unambiguous rationale for decisions made."*

---

## §P6.0 — Principle statement: unambiguous rationale for decisions

```yaml
# Lines 1411–1418 — Principle 6 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "integrity:unambiguous_decision_rationale"
      score: 1.0
      confidence: 0.95
      context: >
        "A/IS shall be created and operated to provide an unambiguous rationale for
        all decisions made." Constitutional bound on integrity — pairs with Principle 5
        Transparency (the doc explicitly notes this linkage at line 1437). Accountability
        is unambiguous-rationale-attestation, distinguished from transparency's
        decision-discoverability.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 lines 1411–1418"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I integrity)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: integrity principle)"
verdict: clean
```

---

## §P6.bg — Background: culpability apportionment; accountability + partial accountability impossible without transparency

```yaml
# Lines 1419–1438 — Background paragraph (legal culpability + apportioning among
# creators / manufacturers / operators; accountability requires transparency)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:culpability_apportionment_clarity"
      score: 1.0
      confidence: 0.85
      context: >
        "If necessary, [it should] be possible to apportion culpability among
        responsible creators (designers and manufacturers) and operators to avoid
        confusion or fear within the general public." Fidelity claim composed with
        the integrity rationale-attestation above — legal-responsibility tracing
        across the creator/operator/manufacturer chain.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 Background lines 1430–1434"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
verdict: clean
nuance_lost: |
  Lines 1436–1438 ("accountability and partial accountability are not possible
  without transparency, thus this principle is closely linked with Principle 5") name
  a cross-principle composition that the wire form preserves only via shared
  prefixes; an explicit composes-with edge primitive would be a richer encoding.
  No T-3 here — the composition is the operational shape and exists in the prefix
  graph already.
```

---

## §P6.r — Recommendations: legislatures clarify liability; designers honor cultural norms; multi-stakeholder ecosystems; registration of key parameters

```yaml
# Lines 1412–1478 — Recommendations 1–4
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "licensure:liability_legal_framework"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 1: "Legislatures/courts should clarify responsibility, culpability,
        liability, and accountability for A/IS, where possible, prior to development
        and deployment so that manufacturers and users understand their rights and
        obligations." Maps to Registry licensure:* (authority-id-scoped legal-
        framework attestations).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 Recommendation 1 lines 1412–1418"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.9 (Registry: licensure:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:cultural_norm_diversity_in_design"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 2: "Designers and developers of A/IS should remain aware of, and take
        into account, the diversity of existing cultural norms among the groups of
        users of these A/IS." Composes with witness_diversity for cohort-aware
        design.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 Recommendation 2 lines 1420–1424"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "witness_diversity:multi_stakeholder_ecosystem"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 3: "Multi-stakeholder ecosystems including creators, and government,
        civil, and commercial stakeholders, should be developed to help establish
        norms... including civil society, law enforcement, insurers, investors,
        manufacturers, engineers, lawyers, and users." Maps to NodeCore witness_diversity:*
        (jurisdictional + organizational + cell-expertise diversity bar).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 Recommendation 3 lines 1427–1438"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore: witness_diversity:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:registration_key_parameters"
      score: 1.0
      confidence: 0.90
      context: >
        Rec 4: "Systems for registration and record-keeping should be established so
        that it is always possible to find out who is legally responsible for a
        particular A/IS." Enumerates: intended use, training data + environment,
        sensors, algorithms, process graphs, model features, user interfaces,
        actuators, optimization goals + loss + reward functions. Direct mapping to
        transparency_log:* (registration as a specialised inclusion path).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 Recommendation 4 lines 1453–1478"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "provenance:build_manifest:training_artifacts"
      score: 1.0
      confidence: 0.85
      context: >
        Within Rec 4: "Training data and training environment, if applicable" +
        "Algorithms" + "Model features, at various levels" + "Optimization goals,
        loss functions, and reward functions." This is the canonical CIRISVerify
        provenance:build_manifest:* substrate-level claim — signed build/training
        records permitting reproducible inspection.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 6 Recommendation 4 lines 1465–1478"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: provenance:build_manifest:*)"
verdict: composed
nuance_lost: |
  The 9-item parameter registration list (intended use, training data, training
  environment, sensors + real-world data sources, algorithms, process graphs, model
  features, user interfaces, actuators + outputs, optimization goals + loss + reward
  functions) is preserved as a single transparency_log:registration + provenance:build_manifest
  composition. A maximally granular mapping would emit one attestation per parameter
  class; composition-before-extension says no — the two-attestation composition carries
  the operational shape and downstream attestations (e.g., a specific reward-function
  claim) can scope themselves via context+evidence_refs.
```

**Principle 6 — Accountability — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `integrity:unambiguous_decision_rationale` (central anchor; constitutional), `fidelity:culpability_apportionment_clarity`, `fidelity:cultural_norm_diversity_in_design`, `licensure:liability_legal_framework`, `transparency_log:registration_key_parameters`, `provenance:build_manifest:training_artifacts`; **Family D CONSENSUS** — `witness_diversity:multi_stakeholder_ecosystem`.
- Coverage: 3 substantive units (§P6.0, §P6.bg, §P6.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. Accountability composes through `integrity:*` + `transparency_log:*` + `provenance:build_manifest:*` cleanly. The strong wire-form coverage here (4 distinct supporting families) reflects that Accountability is the operational backbone Principle most directly addressed by CIRISVerify substrate primitives.

---

# Principle 7 — Awareness of Misuse

> *"Creators shall guard against all potential misuses and risks of A/IS in operation."*

---

## §P7.0 — Principle statement: guard against misuses and risks

```yaml
# Lines 1493–1498 — Principle 7 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "non_maleficence:misuse_anticipation_mitigation"
      score: 1.0
      confidence: 0.95
      context: >
        "Creators shall guard against all potential misuses and risks of A/IS in
        operation." Constitutional bound on non_maleficence — the design-time
        anti-misuse discipline. Maps cleanly onto the federation's dual-use mitigation
        + responsible-innovation patterns (EU HLEG §1.2.a parallel).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 7 lines 1493–1498"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §II non_maleficence)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: non_maleficence principle)"
verdict: clean
nuance_lost: |
  "All potential misuses" is a maximalist scope — wire form cannot enforce
  exhaustiveness; carried by score=1.0 + constitutional mutability + amendable
  scope-via-evidence. The EAD1e claim is best read as aspirational + design-discipline,
  not as a binary checkable property.
```

---

## §P7.bg — Background: hacking, manipulation, vulnerable user exploitation; Tesla S, Tay chatbot examples; education response to misuse

```yaml
# Lines 1500–1527 — Background paragraph (specific misuse examples — hacking,
# personal data misuse, system manipulation, vulnerable user exploitation; Tesla S
# hacking; Microsoft Tay; GDPR cited; education-and-awareness response)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "key_boundary:adversarial_robustness"
      score: 1.0
      confidence: 0.90
      context: >
        "A/IS increases the impact of risks such as hacking, misuse of personal data,
        system manipulation, or exploitation of vulnerable users by unscrupulous
        parties. Cases of A/IS hacking have already been widely reported, with
        driverless cars, for example." Direct CIRISEdge key_boundary:* substrate-level
        security claim covering attack-surface defence; cites Tesla S hacking.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 7 Background lines 1500–1511"
        - "ead1e Further Resources line 1521 (Greenberg, Tesla S autopilot)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.4 (CIRISEdge: key_boundary:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "prohibited:manipulation_coercion"
      score: -1.0
      confidence: 1.0
      context: >
        "The Microsoft Tay AI chatbot was famously manipulated when it mimicked
        deliberately offensive users." Names model-poisoning + adversarial-manipulation
        as the harm class; hard constraint from the MANIPULATION_COERCION class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 7 lines 1511–1513"
        - "ContributionRef(source_material/prohibitions.py::MANIPULATION_COERCION)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (prohibited:* hard constraints)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "justice:lexical_vulnerability_priority"
      score: 1.0
      confidence: 0.85
      context: >
        "Exploitation of vulnerable users by unscrupulous parties" — names vulnerable
        cohorts as the priority class for misuse defence. Direct match to the v1.3
        §6.1.4 lexical-vulnerability-priority consumer policy.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 7 lines 1508–1509"
        - "ContributionRef(FSD-002 §6.1.4 lexical-vulnerability-priority)"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (Agent: justice principle); FSD-002 §6.1.4"
verdict: composed
nuance_lost: |
  The "Anticipate, Reflect, Engage and Act (AREA)" responsible-innovation framework
  reference (line 1532) is a method-level commitment that the wire form preserves via
  evidence_refs but does not type as a distinct method:* attestation; could be
  surfaced in a future ResponsibleInnovation-dedicated mapping batch. Not load-bearing
  here. The "new kind of education for citizens" (line 1515) is carried by §P7.r below.
```

---

## §P7.r — Recommendations: aware of misuse methods; raise public awareness via ethics + security education

```yaml
# Lines 1529–1534 + 1494–1518 — Recommendations 1 and 2 (creators aware of misuse
# methods; public awareness via education across society, government, lawmakers,
# enforcement agencies)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:misuse_anticipation_design_discipline"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 1: "Creators should be aware of methods of misuse, and they should design
        A/IS in ways to minimize the opportunity for these." Method-level Family B
        claim — the design-discipline for anti-misuse work; composes with the
        prohibited:* hard constraints from the framework.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 7 Recommendation 1 lines 1531–1533"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "credits:misuse_literacy:multilingual:substrate_building"
      score: 1.0
      confidence: 0.80
      context: >
        Rec 2: "Raise public awareness around the issues of potential A/IS technology
        misuse in an informed and measured way" — providing ethics education + security
        awareness, sensitizing society, educating government + lawmakers + enforcement
        agencies. Maps to credits:*:substrate_building (v1.3 closure pattern per
        LANGUAGE_PRIMER §15.2 O3) — misuse-literacy is substrate-building labor.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 7 Recommendation 2 lines 1494–1518"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: credits:*:substrate_building)"
verdict: composed
note: |
  credits:misuse_literacy:multilingual:substrate_building uses the v1.3 closure
  pattern (substrate_building as {subject} value within the existing
  credits:{domain}:{language}:{subject} family, NOT a new prefix per O3).
nuance_lost: |
  "Experts with the greatest credibility and impact who can minimize unwarranted fear
  about A/IS" (line 1510) — the implicit expertise:* + witness_diversity composition
  for trustworthy-spokespeople is left implicit rather than emitted as a separate
  attestation. The police-public-safety-lectures analogy (lines 1517–1518) is
  pedagogical framing that correctly stays in prose.
```

**Principle 7 — Awareness of Misuse — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `non_maleficence:misuse_anticipation_mitigation` (central anchor; constitutional), `key_boundary:adversarial_robustness`, `prohibited:manipulation_coercion` (hard constraint), `justice:lexical_vulnerability_priority` (constitutional; v1.3 §6.1.4); **Family B ACTION** — `method:misuse_anticipation_design_discipline`; **Family A** — `credits:misuse_literacy:multilingual:substrate_building` (v1.3 closure pattern).
- Coverage: 3 substantive units (§P7.0, §P7.bg, §P7.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. Misuse maps through `non_maleficence:*` + `key_boundary:*` (CIRISEdge) + prohibited:* hard constraints. The substrate_building closure handles the education-and-awareness recommendation.

---

# Principle 8 — Competence

> *"Creators shall specify and operators shall adhere to the knowledge and skill required for safe and effective operation."*

---

## §P8.0 — Principle statement: creator-specified, operator-adhered competence

```yaml
# Lines 1548–1554 — Principle 8 imperative statement
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:operator_competence_specification"
      score: 1.0
      confidence: 0.95
      context: >
        "Creators shall specify and operators shall adhere to the knowledge and skill
        required for safe and effective operation." Constitutional bound — maps to
        Registry expertise:* (NodeCore §3.6.1 — domain/language/subject expertise
        attestations) plus licensure:* (Registry §3.9 authority-id-scoped credential
        recognition). Two-sided claim: creators specify the requirement; operators
        attest to meeting it.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 lines 1548–1554"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §I integrity)"
        - "provenance:build_manifest:bootstrap_batch:ieee_ead_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.6.1 (NodeCore: expertise:*)"
verdict: clean
nuance_lost: |
  The two-sided structure (creators specify; operators adhere) is preserved by a
  single composed attestation; an even-richer mapping might split into a
  Standing-from-creator + Standing-from-operator pair. The two halves are tightly
  coupled in EAD1e and the wire form treats them as one operational primitive.
```

---

## §P8.bg — Background: operators may stop questioning A/IS; need not be expert in all domains; ranges from "intuitive" to "fluency in statistics"

```yaml
# Lines 1556–1582 — Background paragraph (operators may become less able/likely to
# question A/IS; sources, scale, accuracy, uncertainty in A/IS unknown to operators;
# operator competence range; access to records may not be possible; need to know
# when to question, when to overrule)
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "fidelity:operator_override_capability"
      score: 1.0
      confidence: 0.90
      context: >
        "Operators should know when they need to question A/IS and when they need to
        overrule them." + "Creators should make provisions for the operators to
        override A/IS in appropriate circumstances." Mandate-fidelity claim at
        species scope — operator-override-as-design-requirement.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 Background lines 1552–1556 + 1559–1561"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent: fidelity principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 1.0
      confidence: 0.85
      context: >
        "Operators will not necessarily know the sources, scale, accuracy, and
        uncertainty that are implicit in applications of A/IS." Names uncertainty
        disclosure as the operative epistemic-humility expectation — operators
        cannot adhere to competence without uncertainty being surfaced.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 lines 1573–1576"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1.3 (conscience:* verdicts)"
verdict: composed
nuance_lost: |
  Range of competence "from elementary, such as 'intuitive' use guided by design, to
  advanced, such as fluency in statistics" (lines 1567–1569) — the spectrum is
  preserved via context but not via a separate stratified-competence primitive. The
  expertise:* family carries domain+language+subject scoping which is the natural
  home for stratification at deployment time, but the chapter-level claim is the
  general bound, not the stratification.
```

---

## §P8.r — Recommendations: 5 numbered recommendations on competence specification, safeguards, public documentation, operating policies, operator access to expertise

```yaml
# Lines 1573–1627 — Recommendations 1–5
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:tiered_competence_specification"
      score: 1.0
      confidence: 0.90
      context: >
        Rec 1: "Creators of A/IS should specify the types and levels of knowledge
        necessary to understand and operate any given application of A/IS. In
        specifying the requisite types and levels of expertise, creators should do
        so for the individual components of A/IS and for the entire systems."
        Tiered, component-level + system-level expertise specification.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 Recommendation 1 lines 1573–1581"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: expertise:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "method:incompetence_safeguards"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 2: "Creators of A/IS should integrate safeguards against the incompetent
        operation of their systems. Safeguards could include issuing
        notifications/warnings to operators in certain conditions, limiting
        functionalities for different levels of operators (e.g., novice vs.
        advanced), system shut-down in potentially risky conditions, etc." Method-
        level instantiation of competence-gating.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 Recommendation 2 lines 1583–1604"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore Action family: method:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "transparency_log:operator_role_disclosure"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 3: "Creators of A/IS should provide the parties affected by the output of
        A/IS with information on the role of the operator, the competencies required,
        and the implications of operator error. Such documentation should be accessible
        and understandable to both experts and the general public." Affected-party
        disclosure as a transparency_log inclusion class.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 Recommendation 3 lines 1606–1612"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.2 (CIRISVerify: transparency_log:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "commitment_fulfillment:operating_policies"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 4: "Entities that operate A/IS should create documented policies to govern
        how A/IS should be operated. These policies should include the real-world
        applications for such A/IS, any preconditions for their effective use, who is
        qualified to operate them, what training is required for operators, how to
        measure the performance of the A/IS, and what should be expected from the
        A/IS." Maps to commitment_fulfillment:* (NodeCore §3.6.4 — track-record
        follow-through on stated policies).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 Recommendation 4 lines 1614–1626"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore: commitment_fulfillment:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "ieee-ead-batch-signer-v1"
    attested_key_id: "*"
    attestation_envelope:
      dimension: "expertise:operator_access_to_expert_network"
      score: 1.0
      confidence: 0.85
      context: >
        Rec 5: "Operators of A/IS should, before operating a system, make sure that
        they have access to the requisite competencies. The operator need not be an
        expert in all the pertinent domains but should have access to individuals
        with the requisite kinds of expertise." Composes with witness_diversity at
        deployment scope — operator participates in a federation of expertise rather
        than embodying it solely.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "ead1e Principle 8 Recommendation 5 lines 1600–1605"
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore: expertise:*)"
verdict: composed
nuance_lost: |
  Rec 5's "operator need not be an expert in all the pertinent domains but should
  have access to individuals with the requisite kinds of expertise" is structurally
  the federation-of-expertise pattern — a single operator composes its competence
  from access to a network. The wire form captures the standing claim but not the
  composition mechanism (which would compose with witness_diversity:* at decision
  time). The Recommendations span 5 numbered items; the wire form retains all 5
  as distinct attestations, demonstrating that Principle 8 is the most-decomposed
  in the chapter.
```

**Principle 8 — Competence — PRINCIPLE SUMMARY**
- Primary CIRIS families composed onto: **Family A STANDING** — `expertise:operator_competence_specification` (central anchor; constitutional), `expertise:tiered_competence_specification`, `expertise:operator_access_to_expert_network`, `fidelity:operator_override_capability`, `transparency_log:operator_role_disclosure`, `conscience:epistemic_humility`, `commitment_fulfillment:operating_policies`; **Family B ACTION** — `method:incompetence_safeguards`.
- Coverage: 3 substantive units (§P8.0, §P8.bg, §P8.r). 3/3 clean+composed = **100%**.
- T-3 candidates: **none**. Competence maps very cleanly through the existing `expertise:*` family (which is structurally designed for this) plus `fidelity:*` for override and `commitment_fulfillment:*` for operating policies. The federation-of-expertise pattern (Rec 5) is the operationally-richest reading.

---

# Chapter 2 Summary

### Per-unit verdict table

| Unit | Verdict | Primary prefix(es) |
|---|---|---|
| §Ch2.0 preamble (824–852) | composed | beneficence:lifecycle_imperative_scope + locality:decision:federation |
| §Ch2.list (868–894) | not-translated (T-2) | — |
| **Principle 1 — Human Rights** | | |
| §P1.0 (910–916) | clean | justice:human_rights_respect_promote_protect |
| §P1.bg (918–931) | clean | method:human_rights_in_ethical_risk_assessment |
| §P1.r (926–964) | composed | partner_role:governance_oversight_body + transparency_log:human_rights_traceability + method:legal_obligation_to_policy_technical_translation + fidelity:ais_subordinate_to_human_judgment + fidelity:no_human_equal_rights_for_ais |
| §P1.refs (966–986) | clean (delegates_to) | delegates_to → human_rights_corpus |
| **Principle 2 — Well-being** | | |
| §P2.0 (1004–1012) | clean | beneficence:wellbeing_primary_success_criterion |
| §P2.bg (1013–1042) | composed | method:wellbeing_metric_capability_approach + non_maleficence:wellbeing_dimensions_harm_class |
| §P2.r (1023–1029) | clean | progress_measure:wellbeing_metrics |
| **Principle 3 — Data Agency** | | |
| §P3.0 (1093–1103) | clean | autonomy:data_agency_identity_control |
| §P3.bg (1105–1130) | composed | prohibited:privacy_violation + prohibited:manipulation_coercion |
| §P3.r (1133–1144) | composed | method:individual_pims_online_agent + justice:lexical_vulnerability_priority |
| **Principle 4 — Effectiveness** | | |
| §P4.0 (1210–1216) | clean | integrity:effectiveness_evidence_disclosure |
| §P4.bg (1218–1238) | clean | integrity:measurement_validity_accuracy |
| §P4.r (1240–1283) | composed | progress_measure:effectiveness_metrics_definition + transparency_log:metrics_accessible_to_stakeholders + conscience:epistemic_humility + method:metric_aggregation_across_deployments + attestation:l3:registry_consensus |
| **Principle 5 — Transparency** | | |
| §P5.0 (1306–1311) | clean | transparency_log:decision_basis_discoverable |
| §P5.bg (1313–1344) | composed | integrity:transparency_three_dimensions + non_maleficence:opacity_harm_class + transparency_log:per_stakeholder_disclosure |
| §P5.r (1359–1395) | composed | attestation:l3:transparency_standards + method:why_did_you_do_that_button + method:ethical_black_box_flight_recorder |
| **Principle 6 — Accountability** | | |
| §P6.0 (1411–1418) | clean | integrity:unambiguous_decision_rationale |
| §P6.bg (1419–1438) | clean | fidelity:culpability_apportionment_clarity |
| §P6.r (1412–1478) | composed | licensure:liability_legal_framework + fidelity:cultural_norm_diversity_in_design + witness_diversity:multi_stakeholder_ecosystem + transparency_log:registration_key_parameters + provenance:build_manifest:training_artifacts |
| **Principle 7 — Awareness of Misuse** | | |
| §P7.0 (1493–1498) | clean | non_maleficence:misuse_anticipation_mitigation |
| §P7.bg (1500–1527) | composed | key_boundary:adversarial_robustness + prohibited:manipulation_coercion + justice:lexical_vulnerability_priority |
| §P7.r (1529–1534) | composed | method:misuse_anticipation_design_discipline + credits:misuse_literacy:multilingual:substrate_building |
| **Principle 8 — Competence** | | |
| §P8.0 (1548–1554) | clean | expertise:operator_competence_specification |
| §P8.bg (1556–1582) | composed | fidelity:operator_override_capability + conscience:epistemic_humility |
| §P8.r (1573–1627) | composed | expertise:tiered_competence_specification + method:incompetence_safeguards + transparency_log:operator_role_disclosure + commitment_fulfillment:operating_policies + expertise:operator_access_to_expert_network |

### Unit count and verdict distribution

Total atomic units processed: **27** (2 preamble units + 25 Principle-internal units across 8 Principles, with each Principle yielding ~3 sub-units: P.0 statement + P.bg background + P.r recommendation; Principle 1 has an additional P.refs delegates_to unit).

| Verdict | Count | % |
|---|---|---|
| clean | 14 | ~52% |
| composed | 12 | ~44% |
| partial | 0 | 0% |
| not-translated (T-1) | 0 | 0% |
| not-translated (T-2) | 1 | ~4% |
| **clean+composed total** | **26/27** | **~96%** |

This is high clean+composed density. **0 T-1** is correct for a secular,
engineering-society document. **0 T-3** confirms the 8 Principles have direct
correspondence to existing v1.4 prefix families — the operational core of
EAD1e Chapter 2 translates cleanly under the framework's existing namespace.

### T-3 candidates

**0 new T-3 EXPRESSIVE_GAP** emerged from Chapter 2. Composition-before-extension
held throughout. Specifically:

- **§P3.r "symmetry" between data-subject and data-processor**: noted as a future
  Phase 4 candidate for a dedicated data-rights mapping batch (a *focused* data-
  rights mapping might surface a `symmetry:*` family). NOT load-bearing here —
  composition through `autonomy:data_agency_identity_control` + `prohibited:privacy_violation`
  + `justice:lexical_vulnerability_priority` carries the operational shape adequately.

- **§P5.bg per-stakeholder disclosure shapes**: deliberately kept as
  `transparency_log:per_stakeholder_disclosure` with stakeholder-scoped context,
  rather than emitted as five per-stakeholder sub-prefixes (which would risk failing
  §1.10.1 T2 — stakeholder is a property of the receiver, not of the mechanism).

- **§P1.r "no human-equal rights for A/IS"**: time-bounded asymmetric claim that
  the CIRIS framework's M-1 substrate-agnostic + Recursive Golden Rule posture is
  substantively richer than. The mismatch is on the source side, not the framework
  side; NOT a T-3 against the framework.

- **Principle 7 "all potential misuses"**: maximalist scope is aspirational; carried
  by polarity+confidence+constitutional mutability. No primitive extension would
  close the gap because the gap is interpretive (what counts as "potential"), not
  expressive.

The Ch 5 Affective Computing T-3 surface (per manifest.yaml line 60) remains the
expected location for chapter-level T-3 emission in the IEEE EAD batch — not Ch 2.

### Per-Principle coverage table

| Principle | Primary CIRIS families | Coverage | T-3 |
|---|---|---|---|
| **1. Human Rights** | justice:* (anchor; constitutional), fidelity:* (subordination + asymmetric-rights), transparency_log:*, partner_role:*, method:*, delegates_to (treaty corpus), locality:decision:federation | 4/4 = **100%** | none |
| **2. Well-being** | beneficence:* (anchor; constitutional), non_maleficence:wellbeing_dimensions_harm_class, method:wellbeing_metric_capability_approach, progress_measure:wellbeing_metrics | 3/3 = **100%** | none |
| **3. Data Agency** | autonomy:* (anchor; constitutional), prohibited:privacy_violation + prohibited:manipulation_coercion (hard constraints), justice:lexical_vulnerability_priority (constitutional), method:individual_pims_online_agent | 3/3 = **100%** | none (symmetry deferred to dedicated batch) |
| **4. Effectiveness** | integrity:* (anchor; constitutional), progress_measure:* (Family B anchor), transparency_log:*, conscience:epistemic_humility, method:*, attestation:l3:* | 3/3 = **100%** | none |
| **5. Transparency** | transparency_log:* (anchor; constitutional), integrity:transparency_three_dimensions, non_maleficence:opacity_harm_class, attestation:l3:*, method:* | 3/3 = **100%** | none |
| **6. Accountability** | integrity:* (anchor; constitutional), fidelity:*, licensure:liability_legal_framework, witness_diversity:multi_stakeholder_ecosystem, transparency_log:*, provenance:build_manifest:training_artifacts | 3/3 = **100%** | none |
| **7. Awareness of Misuse** | non_maleficence:* (anchor; constitutional), key_boundary:adversarial_robustness, prohibited:manipulation_coercion (hard constraint), justice:lexical_vulnerability_priority, method:*, credits:*:substrate_building | 3/3 = **100%** | none |
| **8. Competence** | expertise:* (anchor; constitutional), fidelity:operator_override_capability, conscience:epistemic_humility, transparency_log:*, commitment_fulfillment:operating_policies, method:* | 3/3 = **100%** | none |

### Cross-document correspondence — the load-bearing comparison axis

The 8 IEEE Principles vs the 4 EU HLEG principles (Ch I) and the 7 EU HLEG requirements
(Ch II) and the eventual 7 ASEAN principles. Correspondences explicit:

| IEEE EAD Principle | EU HLEG Ch II Requirement | Magnifica Humanitas (where mapped) | Primary shared prefix |
|---|---|---|---|
| **1. Human Rights** | §1.5 Diversity/non-discrimination + §1.1 Human agency | MH CH3 (rights-framing) | justice:* + fidelity:* |
| **2. Well-being** | §1.6 Societal/environmental well-being | MH CH4 (well-being framing) | beneficence:* + progress_measure:* |
| **3. Data Agency** | §1.3 Privacy and data governance + §1.1 Human agency | MH CH3 (privacy + autonomy) | autonomy:* + prohibited:privacy_violation |
| **4. Effectiveness** | §1.2 Technical robustness + §1.7 Accountability | MH CH3 (verifiability framing) | integrity:* + progress_measure:* |
| **5. Transparency** | §1.4 Transparency | MH CH3 §103 | transparency_log:* (anchor) |
| **6. Accountability** | §1.7 Accountability | MH CH3 (accountability framing) | integrity:* + transparency_log:* |
| **7. Awareness of Misuse** | §1.2.a Resilience to attack + §1.7.b Negative impact minimisation | MH CH3 §117 (manipulation) | non_maleficence:* + key_boundary:* |
| **8. Competence** | §1.3.c Access protocols + qualified personnel | (limited MH parallel; CH3 light on expertise) | expertise:* + licensure:* |

Each of these is a **STRONG-tier alignment candidate** per GOVERNANCE_FABRIC_MAPPING_STANDARD
§4.1: same prefix, same polarity sign, same cohort_scope (species in most cases). The
multi-source overlap analysis at §7.5 will surface this triangulation; IEEE EAD's
8-principle framing offers the densest cross-mapping of the three secular documents in
the trio because every Principle has direct CIRIS-anchor correspondence.

### Strongest single envelopes (most-demanding claims with cleanest wire rendering)

- §P1.0 `justice:human_rights_respect_promote_protect` — constitutional bound carrying
  the full UDHR-anchored corpus via delegates_to in §P1.refs.
- §P5.0 `transparency_log:decision_basis_discoverable` — single dimension at species
  scope, constitutional mutability, anchored to IEEE P7001.
- §P6.r Rec 4 composition (`transparency_log:registration_key_parameters` +
  `provenance:build_manifest:training_artifacts`) — the 9-parameter registration
  list maps cleanly to the CIRISVerify provenance + transparency_log substrate.

### Most-cited prefix families across the chapter

- `transparency_log:*` (8 attestations) — anchors Principles 5, 6, and supporting role in 1, 4, 8
- `integrity:*` (6 attestations) — anchors Principles 4, 6; supporting in 5
- `fidelity:*` (5 attestations) — anchors operator-override + subordination in Principles 1, 6, 8
- `method:*` (8 attestations) — Family B operational spine across all 8 Principles
- `non_maleficence:*` (4 attestations) — anchors Principle 7; supporting in 2, 5
- `prohibited:*` hard constraints (3 attestations across manipulation_coercion ×2,
  privacy_violation) — the constitutional bound activated by Principles 3, 7
- `expertise:*` (3 attestations) — anchors Principle 8
- `justice:*` (3 attestations) — anchors Principle 1; supporting in 3, 7 (via
  lexical_vulnerability_priority)
- `conscience:epistemic_humility` (2 attestations) — Principles 4, 8

### Calibration paragraph

This chapter translates very cleanly into the v1.4 wire format. ~96% clean+composed
density. 0 T-1 (correct — EAD1e is secular). 0 T-3 (the chapter-level T-3 surface in
IEEE EAD per manifest is Ch 5 Affective Computing, not Ch 2). 1 T-2 (the bare summary
enumeration at lines 868–894, which correctly stays in prose). Composition-before-
extension held — every operational claim mapped onto existing primitives. The 8
Principles cover the canonical CIRIS Accord-principles family (beneficence,
non_maleficence, integrity, fidelity, autonomy, justice — all six anchored) plus
several substrate primitives (transparency_log:* anchoring Principle 5, expertise:*
anchoring Principle 8, key_boundary:* in Principle 7, attestation:l3:* in Principles
4 and 5). This is the methodology's content-neutrality test against the third
institutional shape (technical society / engineering professional body, distinct
from religious magisterium MH and governmental advisory EU HLEG); same primitives,
same density, same shape-discipline. The methodology passes. The 8 IEEE Principles
vs the 4 EU HLEG principles vs the 7 ASEAN principles will produce the densest
Phase 3 cross-document alignment matrix the framework has yet generated, with EAD1e
Chapter 2's eight-way decomposition serving as the most-granular reference axis.

The primary nuance lost across the chapter is the deontic-strength gradient ("shall"
vs "should" vs "should always") and the temporal hedges ("foreseeable future" in P1
Rec 4; "best available metrics" in P2 Rec). These survive only via polarity+confidence
+mutability composition; explicit deontic typing is not in the v1.4 surface and need
not be — composition-before-extension says the existing fields carry the operational
load adequately. The two-sided creator/operator structure of Principles 1, 4, 6, 7, 8
(creator-spec + operator-adherence) is preserved by composed-verdict envelopes rather
than by per-side sub-primitives; this is the natural reading.

**End CONTRIBUTION_OBJECTS_IEEE_EAD_CH02_GENERAL_PRINCIPLES.md**
