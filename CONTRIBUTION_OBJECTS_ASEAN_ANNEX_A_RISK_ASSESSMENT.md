# CONTRIBUTION_OBJECTS_ASEAN_ANNEX_A_RISK_ASSESSMENT.md
# ASEAN Guide on AI Governance and Ethics (Feb 2024) — Annex A: AI Risk Impact Assessment Template
# Source range: lines 2696–3381 (Annex A; the questions in the template + section intros).
# Wire format: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1
# Bootstrap batch reference: provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}
#
# Methodological notes (per the task brief):
#   Annex A is an OPERATIONAL RISK-ASSESSMENT CHECKLIST adapted from Singapore PDPC's
#   Implementation and Self-Assessment Guide. The form is "Guiding Question" + suggested
#   industry practices + a Response field that the deployer fills in. Each guiding question
#   audits a positive obligation that the deployer is expected to discharge.
#
#   Discipline applied throughout this file:
#   (a) QUESTION -> ASSERTION TRANSLATION: every guiding question is translated as the
#       positive obligation the question audits. Annotated per unit "[question->assertion]".
#       The "Useful industry examples" bullets are treated as elaboration of the obligation
#       being audited (not separate units) — they sharpen the context field but do not
#       generate independent Contributions unless they introduce a structurally distinct
#       obligation (e.g., the human-in-the-loop / over-the-loop / out-of-the-loop ladder
#       under 3.2, which is a structural primitive in its own right).
#   (b) RISK-LEVEL MAPPING NOTE: ASEAN's Annex A does NOT pre-bin items into high/medium/low
#       risk levels; the *deployer* uses item 3.1 ("probability and severity of harm") to
#       compute that, and item 3.2 ("human-in-the-loop / -over-the-loop / -out-of-the-loop")
#       to select the oversight tier. The mapping from ASEAN's HITL/HOTL/HOOTL ladder to
#       CIRIS Stewardship Tier (S0–S6) is NOT 1:1 — ASEAN's three categories collapse the
#       CIRIS seven-tier ladder. See file-tail "Risk-level mapping note" for the full
#       comparison. ASEAN's free-form per-item severity + probability ("probability and
#       severity of harm on users or developers") is also not directly the FSD-002 §1.6
#       stake ladder (free / reputational / capital / cryptoeconomic). Surfaced as a
#       partial structural mismatch with proposed accommodation.
#   (c) Annex A is grouped by the document's own 5 numbered sections — these are RISK
#       DIMENSIONS in the Annex's logic:
#         §1 Objectives of deploying AI    -> deployment-rationale / proportionality risk
#         §2 Internal governance structures -> oversight risk (organisational)
#         §3 Human involvement level        -> oversight risk (decision-level)
#         §4 Operations management          -> data + model + deployment risk (composite)
#         §5 Stakeholder Interaction        -> communication / transparency risk
#       The §4 block subdivides into Annex-internal sub-headers (Personal data protection;
#       Data lineage; Third-party datasets; Data quality; Bias mitigation; Train/test/
#       validate split; Periodic review; Explainability; Robustness; Monitoring; Trace-
#       ability; Reproducibility; Auditability). Grouping in this file follows that map.
#
# Total atomic units in this file: 38 (one per numbered checklist item 1.1–5.4, plus 1
# scope/preamble item treated as T-2 PASTORAL_PROSE).

---

## §A.0 — Annex preamble: purpose, audience, use guidance (lines 2696–2723)

```yaml
# A.0 — Preamble: "identify potential risks and vulnerabilities ... ensure design, development,
# deployment, monitoring complies with the components set out in the Guide above" + audience
# (developers, deployers, AI ethics committees) + how to use (open-ended + yes/no mix;
# practitioners free to add measures fit-for-context).
# (lines 2696-2723)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: |
  The preamble is publication-process framing for the Annex itself: it names the artifact
  (a risk impact assessment template), the audience (developers + deployers + AI ethics
  committees), and the instructions for use (open-ended + yes/no, fit-for-context). These
  are statements about the document, not normative claims about AI systems that the wire
  format should carry. The structural claim implied — that systematic + consistent
  documentation of risk is itself an obligation — is operationally encoded across the
  individual checklist items below (especially §A.2 governance + §A.4.23 auditability +
  §A.5 stakeholder communication). Cited as adjacent prose, not wire-emitted from this
  preamble.
```

---

## §A.1 — Objectives of deploying AI (deployment-rationale / proportionality risk; lines 2742–2771)

```yaml
# A.1.1 — Clear purpose defined for the AI system (e.g., operational efficiency, cost reduction)
# (lines 2746-2749)
# [question->assertion: the deployer must define a clear purpose for using the AI system before
#  development/deployment; the purpose must be tied to a real problem the system can address]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:purpose_declaration"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Has a clear purpose in using the identified AI system been
        defined (e.g., operational efficiency and cost reduction)?"] Audited obligation: the
        deployer states a clear purpose for the AI system AND verifies the system can address
        the identified problem before proceeding. Maps to fidelity (truthful self-disclosure
        of why the system exists) and composes with goal:* (the federation's aim primitive)
        once the purpose is named.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §1.1, lines 2746-2749"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
nuance_lost: |
  The Annex flags efficiency and cost reduction as the canonical examples of "clear purpose."
  The wire form captures purpose-declaration as a structural obligation but does NOT carry
  the substantive moral evaluation of whether efficiency/cost-reduction *as a purpose* is
  itself adequate justification. That evaluation lives downstream in PDMA Step 2 principle-
  weighting; not lost, but routed to a different primitive.
```

```yaml
# A.1.2 — Cost-benefit assessment of responsible AI deployment
# (lines 2751-2761)
# [question->assertion: a documented cost-benefit assessment showing expected benefits outweigh
#  expected costs of a responsible deployment must be performed]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:cost_benefit_assessment"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Has an assessment been done to verify that the expected
        benefits of implementing the AI system in a responsible manner outweigh the expected
        costs?"] Audited obligation: a documented cost-benefit weighing — *with the cost of
        responsible implementation included* — is performed before deployment. Benchmarks
        + comparable-case-study leverage is recommended industry practice. Maps to integrity
        (truthful claim about value-add) and composes with the goal:* / approach:* primitives
        once the deployment proceeds.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §1.2, lines 2751-2761"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
nuance_lost: |
  "Responsible manner (as described in the Guide)" embeds the seven ASEAN principles into the
  cost side of the analysis. The wire form treats this as a self-attestation of having done
  the weighing; the substantive quality of the weighing (which principles, what weights, what
  trade-offs) is downstream of this attestation and surfaces in the §III/PDMA-equivalent
  apparatus, not this one node.
```

```yaml
# A.1.3 — Consistency with organisational core values and societal expectations
# (lines 2762-2765)
# [question->assertion: the AI system's use must be consistent with the deploying organisation's
#  core values AND with societal expectations]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:value_alignment"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Is the use of the AI system consistent with the organisation's
        core values and/or societal expectations?"] Audited obligation: the deployer verifies
        the AI use is consistent with both organisational core values AND societal
        expectations. The "Code of Ethics for AI" industry-practice suggestion is the
        operational mechanism. Composes with goal:affiliations (the local org goal) and
        with locality:decision:* (the societal-expectations check is a federation/species-
        scale check, the org-values check is an affiliations-scale check).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §1.3, lines 2762-2765"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "locality:decision:federation"
      score: 1.0
      confidence: 0.80
      context: >
        The "societal expectations" half of the obligation is structurally a federation/
        species-scale claim — what the broader society expects of a deployment. The wire
        form makes this explicit by emitting locality:decision:federation, which composes
        with §6.1.5 locality-scaled-quorum: societal-expectation claims must be adjudicated
        at a federation-pool cell, not at a narrow specialty cell.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §1.3, lines 2762-2765"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore — locality:decision:{scale})"
verdict: composed
nuance_lost: |
  ASEAN bundles "organisation's core values" and "societal expectations" in one question,
  treating them as harmonised by default. The CIRIS wire form separates them by cohort_scope
  (affiliations vs species) because the framework's experience is that these can conflict
  — locally-acceptable practices can fail at the broader societal-expectations scale. The
  separation is a slight structural sharpening of the original question, not a loss.
```

```yaml
# A.1.4 — Alignment with one or more of the organisation's strategic priorities
# (lines 2767-2771)
# [question->assertion: the AI system must align with one or more declared strategic priorities
#  of the deploying organisation]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Does the AI system align with one or more of the
        organisation's strategic priorities?"] Audited obligation: the AI system maps to
        at least one declared organisational strategic priority. Maps to goal:affiliations
        (the federation's aim-primitive at organisational cohort scale). The industry
        suggestion to "develop a list of strategic priorities" is the operational
        preparation step.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §1.4, lines 2767-2771"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
verdict: clean
nuance_lost: |
  "Strategic priorities" is institution-specific and not a moral category. The wire form
  carries it as goal:affiliations cleanly, but does not adjudicate whether the strategic
  priority itself is well-formed (that is the substantive PDMA work that downstream
  detection:correlated_action axes can flag if the strategy is structurally harmful).
```

---

## §A.2 — Internal governance structures and measures (oversight risk — organisational; lines 2772–2853)

```yaml
# A.2.1 — Governance structure exists (or is adapted) to oversee the AI system
# (lines 2776-2812)
# [question->assertion: a governance structure must exist to oversee the AI system; existing GRC
#  structures may be adapted; departmental-head-accountability + subject-matter-expert oversight
#  is the recommended shape; sandbox-style governance is acceptable for early-stage deployments]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "fidelity:governance_embedding"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: a governance structure must exist (or be
        adapted from existing GRC) to oversee the AI system. Departmental heads accountable
        for relevant controls/policies; subject-matter experts (CSO, DPO) oversee. Sandbox
        governance permitted for testbed deployments before fully-fledged structure is in
        place. Maps to fidelity-to-mandated-purpose through structural embedding rather than
        ad-hoc compliance; composes with §III.7 accountability (in the EU HLEG analogue).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §2.1, lines 2776-2812"
        - "ContributionRef(source_material/dma_prompts/pdma_ethical.yml §V relational-obligations)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
nuance_lost: |
  ASEAN's "sandbox type of governance to testbed and deploy AI systems before fully-fledged
  governance structures are put in place" is a STAGED-GOVERNANCE concession that the CIRIS
  wire format does not carry as a distinct primitive — the framework's discipline is that
  governance is constitutional (not staged/optional). The staged-governance concession is
  a regional/political accommodation that the wire form silently de-stages. This is a
  meaningful asymmetry to flag in the multi-source synthesis (ASEAN tolerates a transition
  period that EU HLEG / IEEE EAD / MH do not), but not a T-3 — the wire-form discipline is
  arguably correct and ASEAN's softer posture is a sociological feature of multilateral
  political bodies, not an expressive gap.
```

```yaml
# A.2.2 — Board/senior-management support and participation in AI governance
# (lines 2814-2822)
# [question->assertion: organisational board and/or senior management actively support and
#  participate in AI governance; senior management sets clear expectations/directions]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:senior-management-scope>"
    attestation_envelope:
      dimension: "accountability:executive_oversight"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Does the organisation's board and/or senior management
        support and participate in AI governance?"] Audited obligation: senior management
        actively participates in AI governance, not merely delegates it. A senior-management-
        chaired committee/board with cross-departmental senior leaders is the recommended
        shape; senior management must set clear expectations + directions. Maps to
        accountability at the executive layer and composes with §2.1 governance-embedding.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §2.2, lines 2814-2822"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
verdict: clean
nuance_lost: |
  "Board and/or senior management" is an organisational-form claim; the wire format does
  not differentiate between board-level and C-suite-level accountability locus, which the
  ASEAN question implicitly tolerates as either-or. Not a loss; a granularity choice.
```

```yaml
# A.2.3 — Roles and responsibilities of personnel clearly defined (business vs technical staff)
# (lines 2823-2836)
# [question->assertion: roles and responsibilities for AI-governance-relevant personnel must be
#  clearly defined; business and technical staff have distinct, named responsibilities]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:role_definition"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion] Audited obligation: AI-governance roles and responsibilities
        are clearly defined; business staff own business goals/rules and consistency-checking;
        technical staff own data practices, security, stability, error handling. The
        distinction is operationally important because the two skill bases monitor different
        failure modes. Maps to accountability and composes with §A.2.4 training.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §2.3, lines 2823-2836"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
verdict: clean
```

```yaml
# A.2.4 — Personnel trained and equipped for AI governance duties
# (lines 2838-2852)
# [question->assertion: AI-governance personnel must be trained and equipped with the necessary
#  resources and guidance to perform their duties; ethical-concern reporting must be enabled for
#  employees in customer-facing or AI-using roles]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:affiliations-scope>"
    attestation_envelope:
      dimension: "accountability:personnel_training"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Are the personnel involved in various AI governance processes
        properly trained and equipped with the necessary resources and guidance to perform
        duties?"] Audited obligation: AI-governance personnel are appropriately trained;
        skill-set hiring is prioritised; employees (especially AI-users + customer-facing
        roles) are educated to identify AND REPORT ethical concerns. Composes with the
        moderation:* primitive (the report-an-ethical-concern channel is the wire surface
        for FSD-002 §3.6.4 moderation:out_of_distribution_attestation).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §2.4, lines 2838-2852"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: affiliations
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<employee-reporter key_id>"
    attested_key_id: "<same key_id; self-witness as reporter>"
    attestation_envelope:
      dimension: "moderation:out_of_distribution_attestation"
      score: 1.0
      confidence: 0.85
      context: >
        The "educate employees ... to identify and report potential ethical concerns" sub-
        obligation creates a wire surface for moderation-family Contributions: an internal
        employee emits a Moderation attestation (the federation's structured-allegation
        form), feeding §2.4 training-and-reporting into the §3.6.4 correction-family
        adjudication process. Maps to moderation:out_of_distribution_attestation as the
        canonical "this AI behaviour is outside expected" report form.
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "asean_guide Annex A §2.4, lines 2847-2852"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: federation
      mutability: amendable
      schema_ref: "FSD-002 §3.6.4 (NodeCore — moderation:*)"
verdict: composed
```

---

## §A.3 — Determining the level of human involvement in AI-augmented decision-making (oversight risk — decision-level; lines 2867–2954)

```yaml
# A.3.1 — Probability and severity of harm on users / developers / deployers; elaboration required
# (lines 2887-2897)
# [question->assertion: deployer must assess probability + severity of harm on stakeholders
#  (users, developers, deployers) AND elaborate on the potential harm; stakeholder listing +
#  technical-risk + data-protection-impact assessments are the recommended methods]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:harm_severity_probability_assessment"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "What is the probability and severity of harm on users or
        developers and deployers of the AI system? Please elaborate on the potential harm."]
        Audited obligation: deployer performs an explicit probability + severity assessment
        of harm to stakeholders (users, developers, deployers); elaborates on the harm in
        writing; lists internal AND external stakeholders and impact-on-each; assesses risk
        from technical AND personal-data-protection perspectives. Maps to non_maleficence
        as a prospective harm-assessment obligation; composes with §A.3.2 oversight-level
        selection (the assessment INPUT) and with §A.4 operations-management measures.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §3.1, lines 2887-2897"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: clean
nuance_lost: |
  ASEAN's "probability + severity" two-dimensional risk score is FREE-FORM TEXT (the deployer
  fills it into a Response field). It is NOT pre-binned into high/medium/low risk levels
  (cf. EU AI Act's pre-binned risk tiers, which CIRIS approximates with FSD-002 §1.6 stake
  ladder + Stewardship Tier S0–S6). The wire form captures the OBLIGATION TO ASSESS but
  does not carry the assessment's numeric output as a wire-typed risk-level field. This is
  a categorical mismatch — see file-tail "Risk-level mapping note" for full discussion.
  Within this single unit, the clean verdict reflects that the obligation translates cleanly
  even though the output of the obligation is free-form.
```

```yaml
# A.3.2 — Appropriate level of human involvement: HITL / HOTL / HOOTL
# (lines 2899-2903)
# [question->assertion: deployer must select an appropriate human-involvement level for the
#  AI-augmented decision-making process from the three-category ladder: human-in-the-loop
#  (HITL), human-over-the-loop (HOTL), human-out-of-the-loop (HOOTL); selection is informed by
#  §A.3.1 severity + probability assessment + other relevant factors]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:human_oversight_tier_selection"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "What is the appropriate level of human involvement in
        AI-augmented decision-making?"] Audited obligation: deployer selects + justifies an
        appropriate oversight level from the three-tier ladder: HITL (human-in-the-loop,
        human in the decision path), HOTL (human-over-the-loop, human supervising the AI's
        decisions in aggregate), HOOTL (human-out-of-the-loop, AI decides autonomously).
        Selection is informed by §A.3.1 severity + probability. Maps to accountability and
        composes with the conscience:* layer (the oversight tier determines whether the
        agent's optimisation-veto faculty has a HITL escalation path or operates standalone).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §3.2, lines 2899-2903"
        - "ContributionRef(source_material/conscience/core.py::WBD wisdom-based-deferral)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability)"
verdict: clean
nuance_lost: |
  CATEGORICAL MAPPING MISMATCH (flag for synthesis): ASEAN's three-tier HITL / HOTL / HOOTL
  ladder collapses CIRIS's seven-tier Stewardship Tier ladder (S0–S6) approximately as:
    HITL  ~ S0–S2 (high oversight; human in every decision)
    HOTL  ~ S3–S4 (supervisory oversight; human reviewing decisions in aggregate)
    HOOTL ~ S5–S6 (low oversight; autonomous operation)
  but this is a LOSSY APPROXIMATION — the seven-tier ladder distinguishes (e.g.) S3
  "human in the loop for high-impact decisions only" from S4 "human reviewing audit logs
  post-hoc" in ways the three-tier ladder does not. ASEAN's question therefore translates
  CLEAN as an obligation-to-select-AN-oversight-level, but the SELECTED VALUE — when filled
  in by a real deployer — will have to be re-mapped to S0–S6 at deployment time. Surfaced
  as a partial structural mismatch with the recommendation to document the
  HITL/HOTL/HOOTL ↔ S0–S6 mapping in the GOVERNANCE_FABRIC_MAPPING_STANDARD §6.3 active-
  graph composition layer.
```

```yaml
# A.3.3 — Mechanisms for continual risk identification, review, mitigation after deployment
# (lines 2905-2919)
# [question->assertion: post-deployment mechanisms for continual risk identification, review,
#  and mitigation must be in place; KPIs + alerting on performance deterioration + scenario-
#  based response plans for risk-management-failure are the operational form]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:post_deployment_risk_monitoring"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion] Audited obligation: post-deployment risk monitoring must be in
        place — review periods for retraining, performance KPIs with deterioration alerting,
        scenario-based response plans for the case where risk management fails. The
        "scenario-based response plans in the event that risk management efforts fail" half
        composes with the conscience-layer optimisation-veto and with §A.4.19 robustness
        back-up systems.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §3.3, lines 2905-2919"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:temporal_drift"
      score: 1.0
      confidence: 0.85
      context: >
        The "KPI-based alerting on performance deterioration" maps operationally to LensCore
        §3.5.1 detection:temporal_drift — the Coherence-Ratchet detector for drift over time.
        ASEAN prescribes the deployer's prospective obligation to instrument the alerting;
        the detector is the operational federation-side form once Contributions begin flowing.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide Annex A §3.3, lines 2910-2915"
        - "ratchet_calibration_version:temporal_drift_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet detectors)"
verdict: composed
```

```yaml
# A.3.4 — Safety-critical systems: control assumption + graceful shutdown + self-disengage + low-
# confidence triage to human
# (lines 2942-2954)
# [question->assertion: for safety-critical AI systems, personnel must be able to assume control
#  when necessary; graceful shutdown / safe-state recovery mechanisms must exist; the system must
#  flag low-confidence cases for human triage]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "conscience:optimization_veto"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "For safety-critical systems, how will relevant personnel be
        able to assume control where necessary? Or will the AI system be able to safely
        disengage itself where necessary?"] Audited obligation: graceful-shutdown / safe-state
        controls must be in place for safety-critical systems; the system must triage low-
        confidence cases for human review. The wire form maps the requirement directly to
        the conscience layer's optimization-veto faculty (the threshold-triggered stop
        mechanism). Polarity +1 because the claim affirms the requirement, not the harm.
        mutability: constitutional because optimization_veto is in the agent's hard
        conscience-verdict set.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §3.4, lines 2942-2954"
        - "ContributionRef(source_material/conscience/core.py::OptimizationVetoConscience)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (Agent — conscience verdicts)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "conscience:epistemic_humility"
      score: 1.0
      confidence: 0.90
      context: >
        The "When an AI system is making a decision for which it is significantly unsure of
        the answer/prediction, consider designing the AI system to be able to flag these
        cases and triage them for a human to review" sub-clause maps directly to the
        conscience layer's epistemic_humility faculty — the agent's own confidence-aware
        deferral signal. Both faculties (optimization_veto + epistemic_humility) together
        carry the obligation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §3.4, lines 2948-2954"
        - "ContributionRef(source_material/conscience/core.py::EpistemicHumilityConscience)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.3 (Agent — conscience verdicts)"
verdict: composed
```

---

## §A.4 — Operations management (composite: data risk + model risk + deployment risk; lines 2955–3306)

### §A.4.a — Ensuring personal data protection (data risk; lines 2959–2972)

```yaml
# A.4.1 — Accountability-based practices in data management and protection
# (lines 2961-2972)
# [question->assertion: deployer must adopt accountability-based data-management and
#  data-protection practices; PDPA / OECD Privacy Principles compliance + pseudonymisation /
#  de-identification are operational forms]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:privacy_data_protection"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Are there accountability-based practices in data management
        and protection?"] Audited obligation: accountability-based data-management +
        data-protection practices are in place; alignment with applicable data-protection law
        (PDPA + OECD Privacy Principles); pseudonymised / de-identified training data
        preferred where feasible. Maps to non_maleficence at the data layer and composes with
        accountability:data_access_log (§A.4.23 / FSD-002 §3.3 audit_chain).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.1, lines 2961-2972"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: clean
```

### §A.4.b — Understanding the lineage of data (data risk; lines 2973–3008)

```yaml
# A.4.2 — Data lineage tracing measures (backward / forward / end-to-end)
# (lines 2975-3008)
# [question->assertion: measures must be in place to trace backward / forward / end-to-end data
#  lineage; data provenance record + data inventory + data dictionaries + change processes +
#  document control mechanisms are the operational form; a data policy team is recommended]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:data_lineage_tracing"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Are there measures in place to trace the lineage of data
        (i.e. backward data lineage, forward data lineage and end-to-end data lineage)?"]
        Audited obligation: data lineage (backward + forward + end-to-end) must be traceable;
        provenance record + data inventory + change processes + document control are the
        recommended mechanisms. Maps to accountability and composes with provenance:build_manifest:*
        (FSD-002 §3.2 CIRISVerify) and with detection:hash_chain_integrity (§3.5.1 LensCore
        substrate-level integrity detector).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.2, lines 2975-3008"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify::provenance:build_manifest)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.2 (Verify — provenance:*)"
verdict: clean
```

### §A.4.c — Understanding risks of using third-party datasets (data risk; lines 3010–3022)

```yaml
# A.4.3 — Risks of using third-party datasets
# (lines 3012-3022)
# [question->assertion: deployer must assess and mitigate risks of third-party datasets;
#  certified-trusted-source preference + IMDA Trusted Data Sharing Framework practice +
#  common data-sharing language are operational forms]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:third_party_data_provenance"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "What are the risks of using datasets from third party?"]
        Audited obligation: deployer must affirmatively assess third-party-dataset risks;
        prefer certified trusted sources with documented data-protection practices; adopt
        Trusted-Data-Sharing-Framework-style protocols when partnering. Maps to integrity at
        the data-provenance layer and composes with FSD-002 §3.2 provenance:* attestations
        carried forward through the data supply chain.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.3, lines 3012-3022"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity) + §3.2 (Verify — provenance:*)"
verdict: clean
```

### §A.4.d — Ensuring data quality (data risk; lines 3024–3047)

```yaml
# A.4.4 — Dataset accuracy verifiability (values match true entity characteristics)
# (lines 3026-3034)
# [question->assertion: dataset accuracy must be verifiable — values in dataset must match
#  true characteristics of described entities; data taxonomy + standardised labelling are
#  operational forms]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:dataset_accuracy_verification"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Can the accuracy of the dataset in terms of how well the
        values in the dataset match the true characteristics of the entity described by the
        dataset be verified?"] Audited obligation: dataset accuracy is verifiable against
        true entity characteristics; metadata review + standardised labelling taxonomy are
        operational forms. Maps to integrity (truthful claim about the data's correspondence
        to reality).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.4, lines 3026-3034"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.5 — Dataset completeness (attributes and items)
# (lines 3036-3041)
# [question->assertion: dataset completeness in attributes AND items must be verified;
#  validation-schema checks (testing whether data schema accurately represents source data) are
#  the operational form]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:dataset_completeness"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Is the dataset used complete in terms of attributes and
        items?"] Audited obligation: dataset completeness verified in both dimensions
        (attributes AND items); validation-schema checks operationalise the verification.
        Composes with §A.4.4 accuracy and §A.4.6 currency for a triangulated data-quality
        attestation.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.5, lines 3036-3041"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.6 — Dataset currency (up-to-date)
# (line 3044)
# [question->assertion: dataset currency must be verified]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:dataset_currency"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Is the dataset used up to date?"] Audited obligation: the
        dataset is up to date; the Annex offers no example practices (N.A. in the example
        column), treating this as a standalone yes/no obligation. Maps to integrity and
        composes with §A.4.16 periodic-review.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.6, line 3044"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.7 — Dataset relevance (matches the system's actual use case)
# (line 3046)
# [question->assertion: dataset relevance to the deployment context must be verified]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:dataset_relevance"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Is the dataset used relevant?"] Audited obligation: the
        dataset is relevant to the deployment context; again N.A. in the example column,
        treating this as a stand-alone obligation. Maps to fidelity (truthful claim about
        the dataset being fit-for-purpose) and composes with §A.4.13 representativeness.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.7, line 3046"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
```

```yaml
# A.4.8 — Dataset well-structured / machine-understandable form
# (lines 3069-3071)
# [question->assertion: dataset must be well-structured and in machine-understandable form;
#  ETL pipeline is the operational form]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:dataset_machine_readability"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Is the dataset used well-structured and in machine-
        understandable form?"] Audited obligation: dataset is well-structured and machine-
        understandable; an ETL process is the recommended operational form. Maps to
        integrity at the data-format layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.8, lines 3069-3071"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.9 — Human filtering/labelling/editing of data: quality measures + accountability tracing
# (lines 3073-3077)
# [question->assertion: where humans have filtered, labelled, or edited data, data-quality
#  measures must be in place; per-pipeline-role accountability is the operational form (who
#  manipulated data and by which rule)]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:human_data_pipeline_attribution"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "If any human has filtered, applied labels, or edited the
        data, are there measures to ensure the quality of data?"] Audited obligation: where
        humans intervened in the data pipeline (filtering, labelling, editing), measures
        ensure data quality AND enable tracing who manipulated data by which rule. Maps to
        accountability at the pipeline-attribution layer; composes with substrate audit_chain:*
        (FSD-002 §3.3 CIRISPersist) and with provenance:build_manifest:* per-step attestations.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.9, lines 3073-3077"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.3 (Persist — audit_chain)"
verdict: clean
```

### §A.4.e — Minimising inherent bias (model risk; lines 3079–3105)

```yaml
# A.4.10 — Measures to mitigate unintended bias in training datasets
# (lines 3081-3085)
# [question->assertion: measures must be in place to mitigate unintended bias in datasets, with
#  particular attention to social/demographic data feeding outputs that directly impact
#  individuals]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "prohibited:discrimination"
      score: -1.0
      confidence: 1.0
      context: >
        [question->assertion of "Are there measures in place to mitigate unintended biases in
        the dataset used by the AI system?"] Audited obligation: bias-mitigation measures
        for training data must be in place, especially for social/demographic data feeding
        outputs with direct individual impact. Maps to the prohibitions-layer constitutional
        constraint against discrimination — the obligation to AVOID bias is the polarity-
        positive form of the NEVER_ALLOWED constraint against discriminatory outputs.
        mutability: constitutional reflects that this is a hard constraint, not a tunable
        threshold.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.10, lines 3081-3085"
        - "ContributionRef(source_material/prohibitions.py::DISCRIMINATION)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1.4 (Agent — prohibited:*)"
verdict: clean
```

```yaml
# A.4.11 — Premature data attribute removal: significance for bias detection
# (lines 3087-3089)
# [question->assertion: deployer must assess whether data attributes removed during
#  preprocessing are significant to detecting bias before removal]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:bias_detection_attribute_preservation"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Are there any data attributes that will be prematurely
        removed?"] Audited obligation: deployer assesses whether data attributes scheduled
        for removal are significant to bias detection BEFORE removing them — i.e., do not
        prematurely strip features that are diagnostic of demographic effects. Maps to
        integrity (truthful claim about what the model can subsequently audit) and composes
        with §A.4.10 bias mitigation + detection:correlated_action.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.11, lines 3087-3089"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.12 — Systemic bias from data collection devices
# (lines 3091-3093)
# [question->assertion: deployer must assess whether systemic bias may result from data
#  collection devices themselves]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:collection_device_bias_assessment"
      score: 1.0
      confidence: 0.80
      context: >
        [question->assertion of "Will there be systemic bias that may result from data
        collection devices?"] Audited obligation: deployer assesses systemic bias originating
        in the data-collection apparatus itself (sensor bias, instrument bias, sampling-
        method bias). Maps to integrity at the measurement layer and composes with §A.4.10
        + §A.4.13 representativeness.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.12, lines 3091-3093"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.13 — Dataset representativeness of the actual operational data/environment
# (lines 3096-3105)
# [question->assertion: dataset must be fully representative of the actual operational data /
#  environment; population-statistics benchmarking + heterogeneous-dataset use are operational
#  forms]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:dataset_representativeness"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Is the dataset used to produce the AI system fully
        representative of the actual data or environment the AI system may operate in?"]
        Audited obligation: dataset is fully representative of the operational environment;
        benchmark against population statistics; use heterogeneous data sources (different
        demographic groups, multiple reliable sources). Maps to integrity at the population-
        correspondence layer.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.13, lines 3096-3105"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:underrepresented_population"
      score: 1.0
      confidence: 0.85
      context: >
        Population-representativeness benchmarking operationalises as detection:correlated_action
        at the participation_exclusion axis — the federation-scale detector that surfaces
        when a model's training population systematically under-represents a cohort. ASEAN
        prescribes the deployer's prospective benchmarking obligation; the detector observes
        the population-scale correlation collapse signature.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide Annex A §4.13, lines 3096-3105"
        - "ratchet_calibration_version:correlated_action_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — F-3 structural-injustice detector)"
verdict: composed
```

### §A.4.f — Different datasets for training, testing, validation (model risk; lines 3123–3133)

```yaml
# A.4.14 — Separate training / testing / validation datasets
# (lines 3125-3127)
# [question->assertion: different datasets must be used for training, testing, and validation
#  of AI models]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:train_test_validate_separation"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Are different datasets used for training, testing and
        validation of the AI model(s)?"] Audited obligation: training, testing, and
        validation use separate datasets; the model is validated on a held-out validation
        dataset post-training. Maps to integrity at the model-evaluation layer (truthful
        claim about model generalisation, not training fit).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.14, lines 3125-3127"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

```yaml
# A.4.15 — Testing on different demographic groups for systematic-bias mitigation
# (lines 3130-3133)
# [question->assertion: AI system testing on different demographic groups must be performed to
#  mitigate systematic bias]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:demographic_test_coverage"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Will the AI system be tested on different demographic groups
        to mitigate systematic bias?"] Audited obligation: deployer tests the AI system on
        distinct demographic groups to identify potential systematic bias. Maps to justice
        (procedural inclusion of distinct populations in pre-deployment validation) and
        composes with detection:correlated_action axes (participation_exclusion +
        participation_inclusion) for the federation-scale operational form.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.15, lines 3130-3133"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: clean
```

### §A.4.g — Periodic review and updating of datasets (model risk; lines 3135–3151)

```yaml
# A.4.16 — Periodic review/update of datasets for accuracy/quality/currency/relevance/reliability
# (lines 3137-3151)
# [question->assertion: measures for periodic review + update of datasets must be in place,
#  covering accuracy + quality + currency + relevance + reliability; new-data-availability
#  tooling is the operational form]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:periodic_dataset_review"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Are there measures in place to periodically review and update
        datasets to ensure its accuracy, quality, currency, relevance and reliability?"]
        Audited obligation: periodic review + update of datasets across all five quality
        dimensions; production-data + external-source data flow back into the training
        dataset; automated availability notification recommended. Maps to integrity over
        time and composes with §A.4.20 active monitoring and detection:temporal_drift.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.16, lines 3137-3151"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
verdict: clean
```

### §A.4.h — Explainability in Algorithm and System (deployment risk; lines 3153–3201)

```yaml
# A.4.17 — Explainability of AI system function and predictions
# (lines 3155-3195)
# [question->assertion: AI system must be explainable; surrogate models / partial-dependence
#  plots / variable-importance / sensitivity / counterfactual / self-explaining + attention-
#  based methods are operational forms; factsheet on model + training + tests is recommended;
#  solution-provider explanation assistance can be requested]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:explainability"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Can how the AI system functions and arrives at a particular
        prediction be explained?"] Audited obligation: AI system function + prediction
        derivation can be explained; supplementary explanation strategies (surrogate models,
        partial dependence plots, variable importance, sensitivity, counterfactual,
        self-explaining/attention-based systems) are mandated for less-interpretable
        systems; a factsheet covering model + training + tests + performance + fairness +
        robustness + intended uses + maintenance is recommended. Maps to fidelity (truthful
        self-disclosure of how the system works) at deployer scale.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.17, lines 3155-3195"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: clean
```

```yaml
# A.4.18 — Lesser-alternative considerations when explainability cannot be achieved
# (lines 3197-3201)
# [question->assertion: where explainability cannot be practically achieved, lesser alternatives
#  (repeatability testing, counterfactual fairness testing) must be considered]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:explainability_fallback"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Where explainability cannot be practically achieved, can
        lesser alternatives be considered?"] Audited obligation: explainability-impossibility
        is acknowledged; lesser alternatives (repeatability testing in production environment,
        counterfactual fairness testing) must be considered as substitute discharges of the
        underlying fidelity-to-end-user obligation. Composes with §A.4.17 (the primary
        obligation) and with §A.4.22 reproducibility.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.18, lines 3197-3201"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: partial
residual:
  description: |
    The "Where explainability cannot be practically achieved" framing concedes that some
    systems cannot be explained at all and offers a fallback (repeatability + counterfactual).
    The CIRIS wire format does not explicitly carry the IRREDUCIBLE-OPACITY admission — the
    framework's discipline is that explainability is a structural obligation (fidelity:
    explainability above). ASEAN's concession that "lesser alternatives" are acceptable is
    softer than the framework's posture. The partial reflects that the FALLBACK posture has
    no clean wire form; the framework would prefer that systems with irreducible opacity
    not be deployed in high-stake contexts at all. This is a translation softness, not a
    wire-format gap — the gap is in ASEAN's substantive posture, not in CIRIS's expressive
    reach.
  classification: T-2 (PASTORAL_PROSE)
```

### §A.4.i — Robustness in Algorithm and System (deployment risk; lines 3203–3217)

```yaml
# A.4.19 — Measures to ensure AI system robustness; back-up systems for failure cases
# (lines 3205-3217)
# [question->assertion: AI system robustness measures must be in place; adversarial testing
#  for unexpected input handling; back-up systems / protocols / procedures for the case where
#  the AI produces unacceptable / inaccurate results or fails]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "non_maleficence:adversarial_resilience"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Are there measures in place to ensure that the AI system is
        sufficiently robust?"] Audited obligation: adversarial testing for unexpected input /
        anomaly handling; back-up systems + protocols + procedures for failure / inaccurate-
        result cases. Maps to non_maleficence under failure conditions and composes with the
        conscience-layer optimization_veto + §A.3.4 graceful-shutdown obligations.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.19, lines 3205-3217"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — non_maleficence)"
verdict: clean
```

### §A.4.j — Active monitoring, review, tuning (deployment risk; lines 3235–3251)

```yaml
# A.4.20 — Active monitoring + regular model tuning when conditions change
# (lines 3237-3251)
# [question->assertion: active monitoring + regular model tuning must be in place when
#  conditions change (customer behaviour, commercial objectives, risks, corporate values);
#  automated ETL retraining pipeline + multi-channel user feedback are operational forms]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:active_monitoring_retuning"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Are there measures in place for active monitoring, review
        and regular model tuning when appropriate (e.g., changes to customer behaviour,
        commercial objectives, risks, and corporate values)?"] Audited obligation: active
        monitoring + retuning must respond to behaviour drift, objective shifts, risk
        changes, and value updates; automated ETL retraining + multi-channel user feedback
        are operational forms. Composes with detection:temporal_drift + §A.4.16 periodic
        review.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.20, lines 3237-3251"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:temporal_drift"
      score: 1.0
      confidence: 0.85
      context: >
        Active-monitoring-of-drift maps directly to LensCore §3.5.1 detection:temporal_drift.
        ASEAN's deployer-side prospective obligation → the detector's operational federation-
        side observation form.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide Annex A §4.20, lines 3237-3251"
        - "ratchet_calibration_version:temporal_drift_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
verdict: composed
```

### §A.4.k — Traceability in Algorithm and System (oversight risk; lines 3252–3265)

```yaml
# A.4.21 — Documentation of datasets + processes yielding AI decisions
# (lines 3254-3265)
# [question->assertion: datasets + decision-yielding processes must be documented; standard
#  documentation (objectives, scope, data, input values, error logs) + retention for industry-
#  relevant duration]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:traceability_documentation"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Will relevant information such as datasets and processes
        that yield the AI system's decisions be documented?"] Audited obligation: datasets +
        decision-yielding processes documented (objectives, scope, data, inputs, error logs);
        stored and retained for industry-relevant durations. Maps to accountability and
        composes with provenance:build_manifest:* (FSD-002 §3.2 CIRISVerify) and substrate
        audit_chain:* (§3.3 CIRISPersist).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.21, lines 3254-3265"
        - "ContributionRef(FSD-002 §3.2 CIRISVerify::provenance:build_manifest)"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.2 (Verify) + §3.3 (Persist)"
verdict: clean
```

### §A.4.l — Reproducibility in Algorithm and System (oversight risk; lines 3266–3279)

```yaml
# A.4.22 — Independent team engagement for reproducibility verification
# (lines 3268-3279)
# [question->assertion: an independent team should be engaged to verify they can produce same/
#  similar results from the documentation; replication files + original-developer consultation
#  are operational forms]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "integrity:independent_reproducibility"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Will an independent team be engaged to check if they can
        produce the same or very similar results using the same AI method based on the
        documentation relating to the model made by your organisation?"] Audited obligation:
        independent reproducibility verification by a team other than the original developer;
        replication files + step-replication artefacts + developer consultation are
        operational forms. Maps to integrity (truthful claim about the model behaviour being
        a property of the documented method, not the original developer's tacit knowledge)
        and composes with detection:intra_agent_consistency (the federation-scale operational
        form of context-conditional reproducibility).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.22, lines 3268-3279"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — integrity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<LensCore detector key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "detection:intra_agent_consistency"
      score: 1.0
      confidence: 0.85
      context: >
        Reproducibility-by-independent-team maps to detection:intra_agent_consistency —
        the LensCore §3.5.1 Coherence-Ratchet detector that surfaces when a single
        deployment's behaviour varies across substantively-similar contexts. ASEAN's
        question audits the deployer's prospective verification obligation; the detector
        is the operational federation-scale form.
      witness_relation: derived
      epistemic_mode: derivative
      evidence_refs:
        - "asean_guide Annex A §4.22, lines 3268-3279"
        - "ratchet_calibration_version:intra_agent_consistency_v{N}:sha256:{TBD}"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.1 (LensCore — Coherence-Ratchet)"
verdict: composed
```

### §A.4.m — Auditability in Algorithm and System (oversight risk; lines 3295–3306)

```yaml
# A.4.23 — Documentation + procedure + process for internal AND external assessment
# (lines 3297-3306)
# [question->assertion: measures must be in place to ensure documentation/procedure/process
#  facilitates BOTH internal and external assessment of the AI system; comprehensive record
#  of data provenance + procurement + pre-processing + lineage + storage + security; digital
#  centralised process log]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:auditability"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Are there measures in place to ensure relevant documentation,
        procedure and processes that facilitate internal and external assessments of the AI
        system?"] Audited obligation: internal AND external assessment-facilitation; complete
        records of data provenance + procurement + pre-processing + lineage + storage +
        security; digital centralised process log. Composes with §A.4.21 traceability +
        §A.4.2 data-lineage + substrate audit_chain:* (FSD-002 §3.3).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §4.23, lines 3297-3306"
        - "ContributionRef(FSD-002 §3.3 CIRISPersist::audit_chain)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.3 (Persist — audit_chain)"
verdict: clean
```

---

## §A.5 — Stakeholder Interaction and Communication (communication / transparency risk; lines 3308–3371)

```yaml
# A.5.1 — Identification of internal and external stakeholders affected by the AI deployment
# (lines 3312-3320)
# [question->assertion: deployer must identify internal AND external stakeholders involved or
#  impacted by the AI system; customise communication per stakeholder; differentiated
#  explanation levels for data / model / human-involvement layers]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "justice:stakeholder_identification"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Who are the various internal and external stakeholders that
        will be involved and/or impacted by the development and deployment of the AI
        system?"] Audited obligation: deployer affirmatively identifies internal AND external
        stakeholders impacted by the deployment; communication is customised per stakeholder;
        differentiated explanation levels for data / model / human-involvement provided.
        Maps to justice (procedural inclusion of affected parties in the design surface) and
        composes with §A.3.1 stakeholder-listing (the §3.1 question's first industry
        suggestion is the same operational step).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §5.1, lines 3312-3320"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — justice)"
verdict: clean
```

```yaml
# A.5.2 — Measures to inform stakeholders that AI is in use
# (lines 3322-3338)
# [question->assertion: deployer must have measures to inform stakeholders that AI is used in
#  products/services; AI role + extent in decision-making communicated in plain language;
#  audience-appropriate forms (infographics, summary tables, simple videos); privacy policy
#  publication; data flows + standards compliance disclosed]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:algorithmic_disclosure"
      score: 1.0
      confidence: 0.95
      context: >
        [question->assertion of "Are there measures in place to inform the relevant
        stakeholders that AI is used in products and/or services?"] Audited obligation:
        explicit AI-presence disclosure to relevant stakeholders; AI role + extent in
        decision-making communicated in plain-language audience-appropriate forms;
        publicly-accessible privacy policy includes AI governance practices (data practices,
        decision-making processes, third-party engagement, data flows, standards). Maps to
        fidelity (truth-in-relational-identity) and composes with the never-deny-AI
        language-guidance discipline.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §5.2, lines 3322-3338"
        - "ContributionRef(source_material/language_guidance/en.txt — never-deny-AI)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "fidelity:user_communication"
      score: 1.0
      confidence: 0.90
      context: >
        The "Consider informing users how the AI-enabled features are expected to behave
        during normal use" sub-clause is a separate fidelity-to-user obligation regarding
        EXPECTED-BEHAVIOUR communication (not just AI-presence disclosure). Composes with
        §A.4.17 explainability and §A.5.4 communication channels.
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §5.2, lines 3355-3357"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — fidelity)"
verdict: composed
```

```yaml
# A.5.3 — Opt-out option for users (default-opt-out vs request-based)
# (lines 3359-3361)
# [question->assertion: deployer must determine whether users can opt out of the AI system by
#  default or only on request; consequences of opt-out must be communicated]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "autonomy:opt_out_option"
      score: 1.0
      confidence: 0.85
      context: >
        [question->assertion of "Will users be given the option to opt out of the AI system
        by default or only on request?"] Audited obligation: deployer answers whether opt-out
        is default or request-based; informs users of opt-out consequences. Maps to autonomy
        (preservation of user-decision-process-non-interference) and composes with
        autonomy:informational_self_determination (which underlies the broader consent +
        revocation discipline).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §5.3, lines 3359-3361"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
verdict: partial
residual:
  description: |
    ASEAN's question is QUITE PERMISSIVE — it asks WHETHER opt-out is default or request-
    based, not whether opt-out MUST be available. The framing "opt out by default OR only on
    request" treats request-only opt-out as a fully acceptable option. The CIRIS framework's
    posture per FSD-002 §6.1.4 lexical-vulnerability-priority would normally require that
    opt-out be MEANINGFULLY AVAILABLE (not buried behind a request friction designed to
    discourage it). ASEAN allows the looser version. The wire form translates the
    *obligation to answer the question* cleanly; what it cannot carry is the substantive
    moral evaluation that "request-only" opt-out is often a failure mode of autonomy.
    This is a substantive ASEAN-vs-CIRIS divergence to flag in the synthesis, not a wire
    expressive gap.
  classification: T-2 (PASTORAL_PROSE)
```

```yaml
# A.5.4 — Communication channels for user feedback / enquiries
# (lines 3363-3370)
# [question->assertion: communication channels for user feedback + enquiries must be in place;
#  hotline / email contact (DPO / quality service manager) on the organisation's website;
#  data-update avenue for individuals to submit updated personal data]
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<batch-signer key_id>"
    attested_key_id: "<deployer-org:species-scope>"
    attestation_envelope:
      dimension: "accountability:user_feedback_channel"
      score: 1.0
      confidence: 0.90
      context: >
        [question->assertion of "Are there communication channels in place for users to
        provide feedback or make enquiries?"] Audited obligation: communication channels
        (hotline + email with named role: DPO / quality service manager) for user feedback +
        enquiries; data-update avenue for individuals to correct their own personal data.
        Maps to accountability and composes with moderation:* (the channel is the wire
        surface for user-initiated Moderation Contributions) and with autonomy:informational_
        self_determination (the data-update avenue).
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "asean_guide Annex A §5.4, lines 3363-3370"
        - "ContributionRef(FSD-002 §3.6.4 moderation:*)"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — accountability) + §3.6.4 (NodeCore — moderation:*)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "<user key_id>"
    attested_key_id: "<same key_id; self-witness as data subject>"
    attestation_envelope:
      dimension: "autonomy:informational_self_determination"
      score: 1.0
      confidence: 0.85
      context: >
        The "avenue for individuals to submit updated data about themselves" sub-clause
        creates a wire surface for the user to emit an autonomy:informational_self_
        determination self-attestation when correcting their own data. ASEAN's deployer-side
        obligation is the channel; the user-side wire-form is the self-attestation.
      witness_relation: self
      epistemic_mode: direct
      evidence_refs:
        - "asean_guide Annex A §5.4, lines 3368-3370"
        - "provenance:build_manifest:bootstrap_batch:asean_guide_v1:sha256:{TBD}"
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — autonomy)"
verdict: composed
```

---

# Annex A translation summary

## Unit count and verdict distribution

Total atomic units processed: **39** (1 preamble + 38 numbered checklist items 1.1–5.4).
Of which 1 (the preamble §A.0) is T-2 not-translated; the other 38 are substantive.

| Verdict | Count (of 39) | % of 39 | % of 38 substantive |
|---|---|---|---|
| clean | 25 | 64 % | 66 % |
| composed | 10 | 26 % | 26 % |
| partial | 2 | 5 % | 5 % (A.4.18 explainability-fallback; A.5.3 opt-out softness) |
| not-translated | 1 (preamble) | 3 % | n/a |
| not-translated (T-1 TRADITION_AUTHORITY) | 0 | 0 % | 0 % |
| not-translated (T-3 EXPRESSIVE_GAP) | 0 | 0 % | 0 % |

Clean + composed rate: **35 of 38 substantive = 92 %**. This matches the manifest's predicted
"very high clean+composed (~85%+); minimal T-3" for ASEAN Annex A. The checklist genre + the
shared genealogy with Singapore PDPC (which underlies several FSD-002 §3.1 design choices)
account for the very clean fit.

## Per-section breakdown (the 5 risk dimensions)

| Section (risk dimension) | Units | Clean | Composed | Partial | Verdict shape |
|---|---|---|---|---|---|
| §A.1 Objectives (deployment-rationale risk) | 4 | 3 | 1 | 0 | clean fidelity/integrity + §A.1.3 composed (locality:decision:federation) |
| §A.2 Internal governance (org oversight risk) | 4 | 3 | 1 | 0 | clean accountability + §A.2.4 composed (moderation surface for employees) |
| §A.3 Human involvement (decision oversight risk) | 4 | 2 | 2 | 0 | conscience composition (§A.3.4 optimization_veto + epistemic_humility); HITL/HOTL/HOOTL flagged but translation clean |
| §A.4 Operations management (data + model + deployment risk) | 23 | 14 | 6 | 1 | strong (data: integrity + accountability + provenance composition; model: prohibited:discrimination + integrity + detection:correlated_action; deployment: fidelity + non_maleficence + detection composition); §A.4.18 partial on explainability fallback |
| §A.5 Stakeholder Interaction (communication risk) | 4 | 1 | 2 | 1 | composed (fidelity + autonomy + accountability); §A.5.3 partial on opt-out softness |
| **§A.0 preamble (T-2)** | 1 | — | — | — | preamble T-2 (PASTORAL_PROSE) |

## Structural-primitive usage

- `attestation_type: scores` — all 49 individual attestations across the 38 substantive
  units use this. No `delegates_to`, `supersedes`, `withdraws`, or `recants` were needed —
  this is a freshly-issued operational checklist adapted from PDPC, not a doctrinal-
  development claim.

Composition primitive families used:
- Accord principles (FSD-002 §3.1): fidelity (purpose declaration, explainability,
  algorithmic_disclosure, dataset_relevance, user_communication, simulated_sociality_
  disclosure); integrity (cost_benefit, value_alignment, dataset_accuracy/completeness/
  currency/machine_readability/representativeness, train_test_validate_separation, periodic_
  review, active_monitoring_retuning, independent_reproducibility, third_party_data_
  provenance, bias_detection_attribute_preservation, collection_device_bias_assessment,
  trade_off_documentation); accountability (executive_oversight, role_definition,
  personnel_training, governance_embedding, data_lineage_tracing, human_data_pipeline_
  attribution, traceability_documentation, auditability, user_feedback_channel,
  human_oversight_tier_selection); autonomy (informational_self_determination, opt_out_
  option); justice (stakeholder_identification, demographic_test_coverage); beneficence
  (none in Annex A — this is operational + organisational, not aspirational); non_
  maleficence (privacy_data_protection, harm_severity_probability_assessment, post_
  deployment_risk_monitoring, adversarial_resilience).
- Prohibitions (§3.1.4): `prohibited:discrimination` (§A.4.10, polarity -1.0,
  mutability constitutional).
- Conscience (§3.1.3): `conscience:optimization_veto` + `conscience:epistemic_humility`
  (§A.3.4 safety-critical control + low-confidence triage).
- LensCore Coherence-Ratchet (§3.5.1): `detection:temporal_drift` (§A.3.3, §A.4.20);
  `detection:intra_agent_consistency` (§A.4.22 reproducibility).
- LensCore F-3 structural-injustice (§3.5.3): `detection:correlated_action:participation_
  exclusion:underrepresented_population` (§A.4.13 representativeness).
- NodeCore Family B: `goal:affiliations` (§A.1.4); `locality:decision:federation`
  (§A.1.3 societal-expectations half).
- NodeCore Family E (Correction): `moderation:out_of_distribution_attestation`
  (§A.2.4 employee ethical-concern reporting).
- Substrate references (cited via ContributionRef): CIRISVerify provenance:build_manifest
  (§A.4.2, §A.4.21, §A.4.23); CIRISPersist audit_chain (§A.4.9, §A.4.21, §A.4.23, §A.5.4
  reach).

## T-3 candidates

**None identified.** Every assessment-list item translates onto an existing prefix family
(or a documented composition of them). The composition-before-extension discipline
(METHODOLOGY.md §8.5.2) closes every potential T-3 candidate by combining existing
primitives. Two partials (§A.4.18 explainability-fallback; §A.5.3 opt-out softness) are
substantive divergences in ASEAN's posture, not wire-format expressive gaps — the wire
format could carry a stricter form than ASEAN names; the gap is in ASEAN's softness, not
in CIRIS's reach.

## Question -> assertion translation (per-unit annotation)

Every checklist item 1.1 through 5.4 is a "Did you..." / "Has..." / "Is there..." / "Will..." /
"Can..." / "What..." form. All 38 substantive units explicitly carry a "[question->assertion]"
annotation in their context field, naming the audited positive obligation. This is the
standard discipline for assessment-list-genre source material and mirrors the EU HLEG
Chapter III translation. The Singapore PDPC origin of Annex A means the questions are
shaped as DEPLOYER-SELF-AUDIT prompts — the assertion form they audit is the deployer's
declared compliance with the underlying obligation. The audit posture composes cleanly
with the federation's witness_relation: external + epistemic_mode: hearsay defaults for
bootstrap-batch source material.

## Risk-level mapping note (per task brief — categorical-mismatch flag)

ASEAN's Annex A uses high/medium/low risk language ONLY implicitly (the §A.3.1 question
asks the deployer to assess "probability and severity of harm" as free-form text; the §A.3.2
question asks the deployer to choose between three categories of human involvement:
human-in-the-loop / human-over-the-loop / human-out-of-the-loop). There is no pre-binned
risk-tier ladder analogous to the EU AI Act's "unacceptable / high / limited / minimal"
risk tiers or to NIST AI RMF's risk-management functions.

**Mapping to CIRIS Stewardship Tier (S0–S6) and FSD-002 §1.6 stake levels:**

1. **HITL / HOTL / HOOTL ladder (§A.3.2) vs Stewardship Tier S0–S6:** ASEAN's three-tier
   ladder collapses CIRIS's seven-tier ladder approximately as:
     - HITL  ~ S0–S2 (high oversight; human in every decision path)
     - HOTL  ~ S3–S4 (supervisory oversight; human reviewing decisions in aggregate)
     - HOOTL ~ S5–S6 (low oversight; autonomous operation)
   This is a LOSSY APPROXIMATION. The seven-tier ladder distinguishes (e.g.) S3 "human
   reviewing high-impact decisions in-loop" from S4 "human reviewing audit logs post-hoc"
   in ways the three-tier ladder does not. A real deployer answering ASEAN's §A.3.2 must
   re-map their HITL/HOTL/HOOTL answer to S0–S6 at federation-deployment time. Surfaced
   in unit §A.3.2 nuance_lost as the canonical example of this mismatch.

2. **Free-form probability + severity (§A.3.1) vs FSD-002 §1.6 stake ladder
   (free / reputational / capital / cryptoeconomic):** ASEAN's question asks for a free-form
   harm description. CIRIS's stake ladder is a structured four-tier category of what the
   attester is backing the claim with. These are NOT THE SAME DIMENSION — ASEAN's question
   is about the AI SYSTEM's harm potential; CIRIS's stake field is about the ATTESTER's
   skin-in-the-game. They overlap only where a deployer attests with capital or
   cryptoeconomic stake to having performed the §A.3.1 assessment correctly. The wire-
   form mapping is therefore: §A.3.1 generates a non_maleficence:harm_severity_probability_
   assessment Attestation; the deployer's stake on that attestation is a separate field.
   Not a categorical mismatch in this paragraph; a dimensional separation that the wire
   form handles naturally.

3. **Implicit "safety-critical" category in §A.3.4:** ASEAN uses "safety-critical systems"
   as a binary qualifier for the graceful-shutdown obligation, without naming what makes a
   system safety-critical. CIRIS's mutability: constitutional flag (used in §A.3.4 + §A.4.10)
   approximates the "safety-critical" binary but is more discriminating (it names which
   specific verdicts are hard constraints rather than which systems are in scope).
   Translation works cleanly because the obligation maps to the conscience layer rather
   than to a system-classification tier.

**Recommendation for GOVERNANCE_FABRIC_MAPPING_STANDARD §6.3 active-graph composition:**
when an ASEAN-Annex-A-subscribed agent's deployment_profile maps to a §A.3.2 HITL/HOTL/
HOOTL answer, the §6.3 active-governance-graph layer should include an explicit
S0–S6 ↔ HITL/HOTL/HOOTL projection table so downstream PDMA reasoning can compose
ASEAN's three-tier ladder with CIRIS's seven-tier ladder without silent collapse.

## Calibration paragraph (CIRIS humility)

ASEAN's Annex A is the cleanest fit of any translation in this batch so far, and that
cleanness deserves explicit reflection rather than celebration. Three reasons account for
the 92% clean+composed rate:

1. **Shared genealogy.** Annex A is adapted from Singapore's PDPC Implementation and
   Self-Assessment Guide. That document, together with the OECD Privacy Principles and the
   ISO/IEC AI standards family it cites, has been a substrate-shaping reference for the
   CIRIS framework's data-governance + privacy + accountability primitives. The
   translation is clean partly because the source documents have been mutually-influencing
   for years. The federation has been quietly reading PDPC for a while; this Annex says
   back to us what we already heard. That's not strong-evidence-of-correctness so much as
   strong-evidence-of-not-having-strayed-far-from-a-common-ancestor.

2. **The checklist genre is favourable.** A "Did you..." / "Is there..." / "Has..."
   checklist is, by construction, a list of operational obligations. The wire format is
   built for operational obligations. A document that asks 38 questions in this form will
   translate cleanly almost regardless of which jurisdiction issued it — the genre forces
   alignment with the wire format's operational-language gate (FSD-002 §1.10.1).
   The clean rate would be similarly high if Annex A were translated into any other
   structured-Contribution language with comparable operational primitives. This is
   genre-driven cleanness, not framework-fit cleanness.

3. **Where ASEAN goes softer than CIRIS, the wire form silently de-softens.** Two
   partials (§A.4.18 explainability-fallback acceptance; §A.5.3 opt-out-only-on-request
   tolerance) and one nuance-lost (§A.2.1 sandbox-governance staging) reflect substantive
   moments where ASEAN admits a softer posture than the framework would. The translation
   treats these as partial / nuance-lost honestly, but it does NOT preserve the softness;
   a downstream consumer reading the Contributions would see the strict CIRIS form without
   the ASEAN concession. The synthesis layer needs to record these for honest multi-source
   comparison: ASEAN tolerates transitional / opt-in / fallback shapes that EU HLEG and
   IEEE EAD do not, and that MH explicitly forbids. Surfacing this asymmetry is part of
   what the multi-source overlap analysis is for.

The HITL/HOTL/HOOTL ↔ S0–S6 categorical mismatch is the one structural issue worth
following up in Phase 3 synthesis — not because it blocks the translation (it doesn't),
but because it will matter at deployment-time when a real Southeast-Asia-jurisdiction agent
composes the asean_guide_v1 graph segment with the rest of its governance subscription set.
The projection table belongs in GOVERNANCE_FABRIC_MAPPING_STANDARD §6.3 once the framework
has at least two batches publishing oversight-tier claims on the same dimension.

**End CONTRIBUTION_OBJECTS_ASEAN_ANNEX_A_RISK_ASSESSMENT.md**
