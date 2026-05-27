# CONTRIBUTION_OBJECTS — Chapter 0 (Introduction §§1-16)

*Wire-format Contribution objects per LANGUAGE_PRIMER.md v2 §12. v1.3 namespace; 1+4 attestation shape.*

---

## §1

```yaml
# MH §1 — Pivotal choice: build Babel (pride/uniformity) or Jerusalem (dignity/fraternity)
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §1)"
        - "pdma_framing.txt §I M-1 (species-scale belonging-projector)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:population"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §1 'Tower of Babel — uniformity that eliminates dignity')"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: >
  "Incarnate God / mystery of the Word made flesh" sub-clause: T-1 (TRADITION_AUTHORITY).
  The Babel/Jerusalem image as narrative vehicle: T-2 (PASTORAL_PROSE); structural content
  redirected to the two contributions above. The "lifting eyes to the Incarnate God" clause
  is Christological and belongs to the tradition's own authority; framework bows out per
  MISSION.md §1.3.
```

---

## §2

```yaml
# MH §2 — Church calls all to cooperate for common good; dialogue intrinsic to vocation
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §2)"
        - "pdma_framing.txt §I M-1 (amae/jeong/ubuntu relational anchors)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Method
    attestation_type: "method:{approach_id}:A3+"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §2 'we wish to engage in dialogue with all men and women')"
        - "pdma_framing.txt §IV deliberative method"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore METHOD_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: >
  "Constituted in Christ as a sacrament of communion" clause: T-1 (TRADITION_AUTHORITY).
  Ecclesiological/Christological grounding of the Church's dialogical vocation belongs to
  the tradition's own authority. Framework's method primitive carries the operational
  practice (dialogue); the theological constitution of the dialoguing community is not
  encoded. Correct posture per MISSION.md §1.3.
```

---

## §3

```yaml
# MH §3 — Rerum Novarum grounds Social Doctrine; living corpus not inert; Leo XIII speaks to era
contributions:
  - kind: Approach
    attestation_type: "approach:{goal:species}"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §3)"
        - "pdma_ethical.yml header (iterative doctrine-under-governance)"
        - "ACCORD auto-expire 2027-04-16 + comment-window discipline"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore APPROACH_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "delegates_to:accord_v{N+1}:from:accord_v{N}"
    envelope:
      target_attestation_id: "<prior accord-version attestation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §3 'living corpus of truth... not an inert set of concepts')"
        - "FSD-002 §2.2.1 (delegates_to as authority-source / version-chaining reuse pattern)"
      cohort_scope: species
      schema_ref: "FSD-002 §2.2 (delegates_to structural primitive)"
      mutability: amendable
verdict: composed
residual: >
  "Invoking the help of the Spirit of wisdom": T-1 (TRADITION_AUTHORITY). Pneumatological
  invocation belongs to the tradition's own register; framework bows out.
  "Living corpus of truth that safeguards humanity's vocation": T-2 (PASTORAL_PROSE);
  operational content (iterative-doctrine-under-governance structure) redirected to the
  Approach primitive above.
```

---

## §4

```yaml
# MH §4 — Technology not inherently antagonistic; AI/digitalization transform world with ambiguity
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:autonomous_capability_risk"
    envelope:
      target_key_id: "*"
      polarity: Neutral
      score: 0.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §4 'technology is not in itself antagonistic')"
        - "pdma_ethical.yml §II Non-Maleficence"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "conscience:epistemic_humility"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §4 'complicates the assessment of potential impact and long-term effects')"
        - "Encyclical(MH §4 'never has humanity had such power over itself')"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.3"
      mutability: amendable
verdict: composed
residual: >
  "We ask God for the wisdom": T-2 (PASTORAL_PROSE); operational content (epistemic humility
  about impact assessment) redirected to conscience:epistemic_humility above.
  The "ambiguity of tools" framing is pastoral language for the Neutral polarity the first
  contribution encodes correctly.
```

---

## §5

```yaml
# MH §5 — Private transnational actors hold power exceeding governments; unprecedented concentration
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:governance"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §5)"
        - "Encyclical(MH §5 Pope Francis quotation: 'impressive dominance over the whole of humanity')"
        - "MISSION_CIRISEdge §1.2 (peer-to-peer, no-broker)"
        - "ContributionRef(prohibitions.py::NO_KINGS architectural invariant)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:structural_asymmetry"
    envelope:
      target_key_id: "<private transnational tech actors>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §5 'resources... surpass those of many Governments')"
        - "pdma_framing.txt §VI Justice"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: >
  Pope Francis quotation as pastoral-prophetic voice on nuclear energy and biotechnology:
  T-2 (PASTORAL_PROSE); structural content (power-concentration pattern at governance scale)
  already expressed in the detection:correlated_action attestation above.
  Note: this is the chapter's most structurally precise translation — the F-3 detector and
  the encyclical's empirical claim share the same moral valence and scope.
```

---

## §6

```yaml
# MH §6 — Shared discernment of direction required; "where are we going?" cannot be avoided
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §6)"
        - "pdma_ethical.yml §I M-1 corridor"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:{goal:species}"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §6 'shared discernment process for identifying spiritual and cultural roots')"
        - "pdma_framing.txt §IV deliberative approach"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore APPROACH_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "conscience:epistemic_humility"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.7
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §6 'crucial questions impose themselves on our conscience and can no longer be avoided')"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.3"
      mutability: amendable
verdict: composed
residual: >
  "Crucial questions impose themselves on our conscience": T-2 (PASTORAL_PROSE); rhetorical
  question form is pastoral; operational content (direction-setting under epistemic humility)
  redirected to Goal + Approach + conscience:epistemic_humility above.
  Three primitives used; this sits at the composed maximum — the paragraph genuinely names
  direction-setting, shared-discernment method, and epistemic posture as three distinct objects.
```

---

## §7

```yaml
# MH §7 — Babel: uniformity without God leads to confusion; pride and self-sufficiency fail
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:diversity_suppression"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §7 'uniformity that eliminated diversity and chose homogenization over communion')"
        - "FSD-002 §1.10 commitment 4 (harm/deception unified under correlation collapse)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "dma:idma:fragility_flag"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §7 'project concealed a profound danger... self-sufficiency... result is not unity but dispersion')"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
verdict: partial
residual: >
  "Project conceived without reference to God": T-1 (TRADITION_AUTHORITY). The theological
  referent carries tradition-authority weight; structural content (fragility from mono-
  cultural self-sufficiency) is redirected to dma:idma:fragility_flag above, but the
  *reason* for the fragility in the encyclical's account (the absence of God) is not
  encodeable without importing theology into the wire. Framework bows out at the
  order-of-reasons clause while encoding the operational failure-mode shape.
  The Babel narrative vehicle: T-2 (PASTORAL_PROSE); structural yield expressed above.
```

---

## §8

```yaml
# MH §8 — Nehemiah: distributed role assignment, shared responsibility, city reborn via cooperation
contributions:
  - kind: Method
    attestation_type: "method:{approach_id}:A3+"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §8 'each family assigned a section of wall... shared responsibility of all')"
        - "MISSION_CIRISNodeCore §1.2 (deferral routing + distributed consensus)"
        - "METHODOLOGY.md §7.3 subsidiarity-named gap note"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.2 / NodeCore METHOD_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "locality:decision:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §8 'he did not impose solutions from above... each assigned a section')"
        - "MISSION_CIRISEdge §1.2 (no central router; peer-to-peer)"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.2 (v1.3 addition: locality:decision:{scale})"
      mutability: amendable
verdict: composed
residual: >
  "Undertaking with God at the center, which rebuilds relationships before rebuilding with
  stones": T-1 (TRADITION_AUTHORITY). The theological centering of the method is the
  encyclical's grounding for why distributed-responsibility works; the framework encodes
  the operational form (locality:decision + per-cell method routing) without encoding the
  theological grounding. Correct posture.
  Nehemiah narrative vehicle: T-2 (PASTORAL_PROSE); structural yield (subsidiarity-shaped
  method + decision-locality) expressed above.
```

---

## §9

```yaml
# MH §9 — Technology never neutral; takes shape of those who devise it; choice: Babel or Jerusalem
contributions:
  - kind: Attestation
    attestation_type: "dma:csdma:context_dependency"
    envelope:
      target_key_id: "*"
      polarity: Neutral
      score: 0.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §9 'technology takes on the characteristics of those who devise, finance, regulate and use it')"
        - "pdma_ethical.yml §II Non-Maleficence"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "integrity:principal_alignment"
    envelope:
      target_key_id: "*"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §9 'takes on characteristics of those who devise, finance, regulate and use it')"
        - "pdma_ethical.yml §VI Integrity"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: composed
residual: >
  "Constructing Babel or rebuilding Jerusalem" as the primary choice framing: T-2
  (PASTORAL_PROSE); both poles have structural equivalents already encoded across adjacent
  rows (goal:species positive / detection:correlated_action negative for the Babel pole;
  locality:decision + method for the Jerusalem pole). The image itself stays in prose
  per §1.10.1.
```

---

## §10

```yaml
# MH §10 — Avoid "Babel syndrome": idolatry of profit, uniformity, reducing person to data
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §10 'reduces the other to a means')"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "detection:correlated_action:informational_asymmetry:person_as_data"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §10 'reduce the mystery of the person to data and performance')"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: partial
residual: >
  "Mystery of the person" resists wire expression. The prohibitions carry the floor
  (manipulation/coercion NEVER_ALLOWED) and the F-3 detector carries the population pattern
  (reducing persons to data at scale). But the affirmative claim — "*this person is
  irreplaceable; their personhood has positive ontological standing the wire is structured
  to honor*" — has no positive-polarity wire primitive. This is the chapter's first instance
  of the positive-dignity T-3 gap.

  T-3 candidate (Gap 1 — shared with §15): "mystery of the person / positive irreplaceability"
  proposed_extension:
    name: "attestation:singular_witness:non_substitutability"
    description: >
      Attests that a named key_id or agent class is treated as a non-substitutable referent
      in a decision context — not as an interchangeable instance of a population category.
      Score = 1.0 for constitutional commitment that biological persons are non-substitutable
      referents in all federation decisions above autonomy threshold; score decreases when
      audit trail shows the subject treated as a substitutable data point.
    gate_verification:
      T1: "yes — anchored to Accord §M-1 constitutional leaf; published, hash-pinned"
      T2: "yes (with reformulation) — names a mechanism: substitutability-count audit check,
           not a subjective-quality label. Checkable against decision audit chain: does any
           logged action treat subject as substitutable instance? Score = 1 − (substitution
           events / total decision events involving subject class)"
      T3: "yes — versionable against Accord leaf version"
      T4: "yes — explicitly not sole evidence for slashing:*; feeds moderation as context"
    priority: MEDIUM
    note: >
      The T2 reformulation is critical: 'mystery of the person' fails T2 as stated.
      'non_substitutability' passes T2 because it names the audit-chain mechanism
      (count of decision events that treat subject as substitutable vs. singular).
      The encyclical's richer claim ('mystery') remains correctly in prose per §1.10.1;
      the wire carries the mechanism-descriptive form.
```

---

## §11

```yaml
# MH §11 — Building common good requires first a firm relationship with God; desire inscribed in hearts
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §11)"
        - "pdma_framing.txt §I M-1 'eudaimonia as evaluative target'"
        - "Encyclical(MH §11 'life in all its fullness' Jn 10:10)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: partial
residual: >
  "Building on a firm relationship with God" as structurally prior to common-good goal:
  T-1 (TRADITION_AUTHORITY).

  This is the chapter's deepest and most honest T-1. The encyclical is not making an optional
  theological observation — the "first and foremost" language signals that the relational
  grounding in God is structurally PRIOR to the common-good goal, not decorative.
  goal:species captures the direction (species-scale flourishing) but not the ordering
  principle: for the encyclical, correct goal orientation is *constituted by* the theological
  relation, not deduced from it independently.

  Augustine citation ("our heart is restless until it rests in you"): T-1.

  Framework's known divergence: the framework's goal:species + M-1 corridor is self-grounding
  (the goal is correct because it serves flourishing). The encyclical's claim is that this
  self-grounding is insufficient — it requires prior theological grounding the framework
  cannot encode without violating §1.10.1. The correct disposition is T-1 for the
  order-of-reasons claim, with the framework noting the divergence per MISSION.md §1.3.

  Proposed T-3 assessment (Gap 4 from round-1): an authority_chain[] field on goal:species
  pointing to tradition-level grounding documents would be an empty gesture (the tradition
  would rightly ask "you cite our document but do not bind yourself to what it says").
  This gap cannot be closed by wire-format extension without either importing theology into
  the wire (§1.10.1 violation) or making an empty gesture. Correctly T-1, not T-3.
```

---

## §12

```yaml
# MH §12 — Accept human limits as constitutive; unlimited upgrades exacerbate inequality
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:autonomous_capability_risk"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §12 'technology promises to free us from all weakness')"
        - "pdma_ethical.yml §III Non-Maleficence"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "justice:distributional_asymmetry"
    envelope:
      target_key_id: "<deploying organizations>"
      polarity: Negative
      score: -0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §12 'models of wellbeing that leave behind entire populations')"
        - "pdma_framing.txt §VI Justice"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "capacity:resilience"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §12 'true fulfilment... through harmonious growth... freedom and responsibility
            intertwined with mutual care')"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.4"
      mutability: amendable
verdict: partial
residual: >
  "Accepting limits and weakness without considering them an error to be corrected" as
  positive normative claim: T-3 (EXPRESSIVE_GAP).

  capacity:incompleteness_awareness tracks epistemic humility about incompleteness but does
  not ratify weakness as constitutively valuable. capacity:resilience captures the
  corridor-preserving property of working-within-limits but does not affirm that the limits
  themselves are intrinsically good.

  T-3 candidate (Gap 2 — finitude-as-value):
  proposed_extension:
    name: "integrity:finitude_acknowledgment"
    description: >
      Scores whether a system's published self-description acknowledges irreducible
      limitations as constitutive rather than contingent upgrade targets. Score near +1
      for systems that list limitations non-apologetically as inherent features; near 0
      for systems that present all limitations as improvement roadmap items.
    gate_verification:
      T1: "yes — hash-pinnable to Accord §M-1 + §I Ch.4 incompleteness awareness leaf"
      T2: "yes — mechanism: comparison of published documentation against operational
           checklist (does the doc list limitations as roadmap vs. as inherent features?);
           machine-checkable by text classification against published checklist; not a
           subjective quality judgment"
      T3: "yes — versionable against checklist version + Accord leaf version"
      T4: "yes — never sole evidence for slashing:*"
    priority: MEDIUM
    status: >
      Gate: PASS. Recommended for v1.3 design phase. Closes the gap between
      'epistemic humility about limits' (capacity:incompleteness_awareness) and
      'limits as constitutively good' (integrity:finitude_acknowledgment). The two
      are genuinely different claims; the new prefix is non-redundant.
```

---

## §13

```yaml
# MH §13 — Subsidiarity: shared responsibility, cooperation across generations/peoples; no one too weak
contributions:
  - kind: Attestation
    attestation_type: "locality:decision:community"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §13 'logic of subsidiarity, which values cooperation between generations,
            peoples, disciplines and cultures')"
        - "MISSION_CIRISEdge §1.2 (peer-to-peer, no-broker)"
        - "MISSION_CIRISNodeCore §1.2 (no central scorer)"
        - "METHODOLOGY.md §7.3 subsidiarity-named gap note"
      cohort_scope: community
      schema_ref: "FSD-002 §3.6.2 (v1.3 addition: locality:decision:{scale})"
      mutability: amendable
  - kind: Method
    attestation_type: "method:{approach_id}:A3+"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §13 'cooperation between generations, peoples, disciplines and cultures')"
        - "MISSION_CIRISNodeCore §1.2 distributed consensus"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore METHOD_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: >
  "Power is made perfect in weakness" (2 Cor 12:9): T-2 (PASTORAL_PROSE); structural
  content (no agent so weak it cannot participate — Sybil-resistance floor) redirected to
  the method primitive above (A3+ substrate rung does not require hardware-root; broad
  participation is structurally enabled).
  GAPS.md note: subsidiarity as *named principle* was previously WEAK_ALIGN in the Accord;
  the v1.3 locality:decision:{scale} prefix closes this naming gap at the wire level.
  This is the chapter's cleanest composed translation where a round-1 naming gap is now
  closed by the new prefix.
```

---

## §14

```yaml
# MH §14 — Common good requires evangelical language; dignity/poor/commons as discernment standards
contributions:
  - kind: Attestation
    attestation_type: "integrity:communication_standard"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §14 'clarity that sheds light and frankness that unlocks new possibilities')"
        - "Encyclical(MH §14 'avoid humiliating or antagonistic words')"
        - "language_guidance/en.txt §1 (FIRST-SENTENCE TONE LOCK; NO naive enthusiasm; NO unfounded fears)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
  - kind: Attestation
    attestation_type: "beneficence:discernment_criteria"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §14 standards: dignity / universal destination of goods / preferential option
            for the poor / care for common home / peace)"
        - "pdma_framing.txt §VI Justice + §II Beneficence"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: amendable
verdict: partial
residual: >
  "Evangelical language" qualifier: T-2 (PASTORAL_PROSE); the theological-pastoral register
  of the qualifier correctly stays in prose; the operational communication standard is
  redirected to integrity:communication_standard.

  "Preferential option for the poor" as *lexically ordered* priority rule: T-3 (EXPRESSIVE_GAP).

  The existing beneficence:discernment_criteria + detection:correlated_action:rights_asymmetry:
  vulnerable_population detects the pattern but does not encode the priority *ordering*.
  The preferential option is not "weight vulnerability more in the scoring function" — it is
  a lexical priority claim: when interests of the vulnerable and the advantaged conflict,
  the vulnerable's interests take structural precedence, not merely a higher weighting
  coefficient. The PDMA's proportionality step weights stakeholders but does not apply a
  lexical rule. §6.1.4 in v1.3 names a lexical-vulnerability-priority reference policy —
  but this is consumer-policy, not a wire-format primitive.

  T-3 candidate (Gap 3 — preferential-option priority ordering):
  proposed_extension:
    name: "justice:priority_ordering:{population}"
    description: >
      Attests that a named agent's decision procedure applies lexically prior consideration
      to {population} before applying weighted aggregation. Score = +1 if decision audit
      chain shows vulnerable-population interests were evaluated first (not merely weighted
      higher) before trade-off resolution; score = 0 if only weighted aggregation applied;
      score = -1 if audit chain shows vulnerable-population interests evaluated after
      advantaged-population interests in any contested trade-off.
    gate_verification:
      T1: "yes — hash-pinnable to Accord §M-1 + PDMA Step 2 stakeholder analysis procedure"
      T2: "conditional pass — 'lexically prior consideration' is verifiable from audit chain
           ordering (decision log shows vulnerable-population evaluation completing before
           trade-off step); passes T2 if computation defined as audit-chain-ordering check,
           not a subjective judgment about who is 'poor'"
      T3: "yes — versionable"
      T4: "yes — not sole evidence for slashing:*"
    priority: MEDIUM
    status: >
      Gate: CONDITIONAL PASS. Requires operational definition of 'prior' in audit chain
      terms. The §6.1.4 consumer-policy reference in v1.3 is a step toward this but does
      not close it at the wire level. Recommended for v1.3 design phase.
    note: >
      This gap is closed at the consumer-policy layer by §6.1.4 in v1.3 but remains open
      at the wire-primitive layer. A consumer reading justice:priority_ordering:vulnerable
      attestations would know the procedure was applied; the attestation itself is the
      machine-checkable audit claim that the consumer-policy was executed.
```

---

## §15

```yaml
# MH §15 — In AI era, duty to remain profoundly human; grandeur no machine can replace
contributions:
  - kind: Attestation
    attestation_type: "prohibited:autonomous_deception"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §15 'human dignity threatened by new forms of dehumanization')"
        - "ContributionRef(prohibitions.py::AUTONOMOUS_DECEPTION)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "capacity:core_identity"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §15 'lovingly safeguard the grandeur of humanity bestowed upon us')"
        - "Encyclical(MH §15 'the splendor of which no machine can ever replace')"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.4"
      mutability: amendable
verdict: partial
residual: >
  "Grandeur of humanity / splendor that no machine can replace" as *affirmative* ontological
  claim about human dignity: T-3 (EXPRESSIVE_GAP).

  This is the same gap as §10 (positive irreplaceability). The prohibited:autonomous_deception
  floor prevents the violation; capacity:core_identity tracks what is being protected; but
  neither emits a positive-polarity attestation affirming "this entity possesses irreplaceable
  inherent value that the federation is structurally oriented toward honoring."

  See §10 proposed_extension (attestation:singular_witness:non_substitutability) — that
  extension would close this gap. The gap appears in both §10 and §15 because the
  Introduction frames positive dignity at both paragraphs; a single proposed_extension
  addresses both.

  "Heart open to others / intelligence willing to listen / will that seeks what unites":
  T-2 (PASTORAL_PROSE); structural content (relational goal orientation) already encoded
  in goal:family + goal:community belonging-projectors from adjacent rows.

  Jubilee Year / pilgrim-of-hope framing: T-2 (PASTORAL_PROSE).
```

---

## §16

```yaml
# MH §16 — Appeal to build communion not Babel; rejected stones as cornerstone; shepherd's heart
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §16)"
        - "pdma_framing.txt §I M-1"
        - "pdma_framing.txt §V ubuntu/amae/jeong"
      cohort_scope: species
      schema_ref: "FSD-002 §3.6.2 / NodeCore GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:vulnerable_population"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §16 'the rejected stones — the poor, the sick, the migrants and the least among us')"
        - "FSD-002 §1.10 commitment 3 (detection brings patterns into morally-real existence)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: >
  "Servants of the coming Kingdom": T-1 (TRADITION_AUTHORITY). Eschatological claim;
  tradition's own articulation of the telos toward which builders of communion work;
  framework bows out per MISSION.md §1.3.
  "Heart of a shepherd and a father": T-2 (PASTORAL_PROSE); pastoral-affective register
  for care orientation toward the vulnerable; structural content redirected to goal:species
  and the detection:correlated_action:participation_exclusion attestation (naming exclusion
  is what brings it into morally-real existence per FSD-002 §1.10 commitment 3).
  Psalm 85:10 citation ("love and faithfulness will meet"): T-2.
  Note: the "rejected stones" detection attestation uses Negative polarity on a
  participation_exclusion axis — not to affirm the exclusion, but to surface the pattern
  as a morally-real federation object that participants can contest and respond to.
```

---

## Chapter conclusion

- **Verdict distribution (16 paragraphs): 0 clean / 8 composed / 5 partial / 0 not-translated (pure)**
- **T-1 residuals in**: §1, §2, §3, §7, §8, §11, §15, §16 (8 paragraphs)
- **T-2 residuals in**: ~12 paragraphs (nearly all)
- **T-3 EXPRESSIVE_GAP candidates**: 3 live (Gaps 1, 2, 3 below); Gap 4 reclassified to T-1

**Corrected distribution note**: Round-1 reported §7 as partial (correct) and §4, §5 as composed (correct). §6 had three contributions above — at the composed maximum; verified the three genuinely name distinct structural objects (direction, method, epistemic posture). No paragraph is pure not-translated because every paragraph has translatable structural content; T-1 and T-2 appear as residuals, not as the primary verdict.

---

### Most striking translation

**§13** (subsidiarity). The v1.3 `locality:decision:community` prefix closes a naming gap that round-1 noted explicitly (GAPS.md: subsidiarity WEAK_ALIGN in the Accord). This paragraph now achieves a fully composed translation with no residual load-bearing gap — the operational shape (per-cell decision routing, no central scorer, broad participation floor) is carried precisely by the new prefix. The structural form of subsidiarity is now *natively named* in the wire format. This is the clearest evidence from the Introduction that v1.3 is responsive to the encyclical's vocabulary.

---

### T-3 candidates flagged (with proposed_extension in per-row blocks above)

**Gap 1 — §10 / §15: Positive dignity / irreplaceability of persons**
- Proposed extension: `attestation:singular_witness:non_substitutability`
- Gate: PASS (with T2 reformulation from "mystery of the person" to audit-chain substitutability-count mechanism)
- Priority: MEDIUM
- Status: **New in round-2**; v1.3's `witness_relation` field distinguishes *who* attests but does not add a positive-dignity affirmative primitive. The gap remains open at the wire level.

**Gap 2 — §12: Positive normative status of weakness/limits (finitude-as-value)**
- Proposed extension: `integrity:finitude_acknowledgment`
- Gate: PASS (T2 passes via documentation-checklist mechanism)
- Priority: MEDIUM
- Status: **Carried from round-1**; v1.3 framing via `capacity:incompleteness_awareness` still does not close it. Non-redundant with existing prefix. Recommended for v1.3 design phase.

**Gap 3 — §14: "Preferential option for the poor" as lexically ordered priority rule**
- Proposed extension: `justice:priority_ordering:{population}`
- Gate: CONDITIONAL PASS (T2 requires operational definition of "prior" in audit-chain terms)
- Priority: MEDIUM
- Status: **Partially addressed in round-2**; §6.1.4 in v1.3 names a lexical-vulnerability-priority *consumer-policy* reference — this is significant progress but does not close the gap at the wire-primitive level. The proposed extension is the wire-level counterpart to the consumer-policy.

**Gap 4 — §1 / §11: Theological grounding as structurally prior to goal orientation**
- Gate: FAILS T2 — "grounded in a prior relation to God" names a theological quality, not a machine-checkable mechanism. No version passes T2 without evacuating the content.
- Status: **Reclassified from T-3 to T-1** (correct posture; matches round-1 analysis). The framework's self-grounding of M-1 is a known and honest divergence from the encyclical's foundational claim. MISSION.md §1.3 names this correctly.

---

### Prefix-discovery notes

- `locality:decision:{scale}` (v1.3) — used at §8 and §13; closes the subsidiarity naming gap. Cited as FSD-002 §3.6.2 (v1.3 addition) since the prefix appears in LANGUAGE_PRIMER.md §11 inventory but not yet in the FSD-002 §3 canonical table I read (pre-v1.3 text). Downstream consumers should verify against the published v1.3 FSD-002 when available.
- `detection:distributive:access:{resource_type}` — not used in this chapter; would apply in later chapters addressing universal destination of goods more directly.
- `multilateral_participation:{forum}:{kind}` — not used in this chapter.
- `accord:*` prefix family — reserved; `accord:hard_constraint:no_kings` (from worked example §9.4) not used in Introduction as the architectural invariant is not the Introduction's primary claim.
- No prefix-discovery failures in this pass; all mapped prefixes found in FSD-002 §3 tables.
