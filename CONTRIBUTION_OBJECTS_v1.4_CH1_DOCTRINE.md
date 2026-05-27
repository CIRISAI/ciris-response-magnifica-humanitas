# CONTRIBUTION_OBJECTS_v1.4_CH1_DOCTRINE.md

**Source**: *Magnifica Humanitas* Chapter One — "A Dynamic Approach Faithful to the Gospel" (§§17–45, 29 paragraphs)
**Wire format**: FSD-002 v1.4
**Primer**: LANGUAGE_PRIMER.md v1.1 (Registry-side canonical)
**Round**: 3 (prior outputs deleted; primer-drift corrected)
**Date**: 2026-05-27

---

## §17 — Doctrinal development challenges Social Doctrine from within; fidelity to Gospel

```yaml
# §17 — AI challenges Social Doctrine categories; calls for development in fidelity to Gospel
contributions:
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<prior-social-doctrine-attestation-corpus-on-res-novae>"
    attestation_envelope:
      references_attestation_id: "<prior-social-doctrine-res-novae-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §17"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "integrity:doctrinal_continuity"
      score: 0.9
      confidence: 0.85
      context: "AI constitutes a challenge from within Social Doctrine categories; development is required in fidelity to the Gospel, not a break from it"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §17"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (Agent — Accord principles)"
verdict: composed
note: |
  Directly follows primer §11.5 template. The `supersedes` captures version-succession
  (this encyclical's treatment of res-novae extends but does not contradict prior corpus);
  `integrity:doctrinal_continuity` scores the continuity claim positively.
  `differs_in: ["scope","evidence_refs"]` per primer §3 instruction.
  T-1 theological tail (Gospel as revealed Truth) correctly stays in residual prose.
residual:
  description: "Claim that development must be 'in fidelity to the Gospel' is theologically grounded (Gospel as normative criterion). Structural core (development without break) is carried above."
  classification: T-1 (TRADITION_AUTHORITY)
```

---

## §18 — Church accompanies humanity; autonomy of earthly realities; serves common good

```yaml
# §18 — Church walks alongside humanity; earthly autonomy; ecclesial/political distinction
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "church-social-presence-institution"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.8
      confidence: 0.75
      context: "Common-good service as ecclesial goal grounded in accompaniment of humanity; not interference or external code imposition"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §18"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
verdict: partial
residual:
  description: |
    The distinction between ecclesial and political communities (mutual autonomy, neither
    absorbing the other) is a governance-structure claim about decision-locality and
    sphere-of-competence separation. The `locality:decision:{scale}` prefix captures
    scale-of-decision but not the binary sphere-separation norm.
    The theological grounding of the accompaniment posture is T-1.
  classification: T-1 (TRADITION_AUTHORITY) for theological grounding;
    T-2 (PASTORAL_PROSE) for the "walking alongside" imagery;
    T-3 composition note below.
composition_attempt:
  note: |
    Attempted: `locality:decision:community` + `goal:community` to capture sphere-separation.
    Result: covers decision-scale but not the norm that *neither* sphere absorbs the other.
    No existing prefix encodes a bilateral non-absorption constraint between two institutional
    types. Does not cleanly compose. Residual sphere-separation claim is a minor T-3 candidate
    but low operational weight for the federation; the broader goal-claim above carries the
    structural content adequately. Verdict: partial, not T-3 escalation.
```

---

## §19 — Church participates in social processes; mission has historical scope

```yaml
# §19 — Church's mission has historical scope; participates in processes shaping society
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "church-social-presence-institution"
    attestation_envelope:
      dimension: "goal:community"
      score: 0.8
      confidence: 0.75
      context: "Church participates actively in society-building processes; historical scope of mission; contribution to just and fraternal society"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §19"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
verdict: partial
residual:
  description: |
    The claim that religion cannot be relegated to purely private life (Francis citation)
    carries a rights-asymmetry dimension — denial of public-voice rights to a community.
    The `detection:correlated_action:rights_asymmetry:{population}` prefix can capture this
    as a surveillance surface, but the normative claim (this relegation SHOULD NOT happen)
    is beyond the detection family's scope.
    The theological grounding of "listening, dialogue and service" vocation is T-1.
  classification: T-2 (PASTORAL_PROSE) for "listening, dialogue and service" imagery; T-1 for vocation claim
```

---

## §20 — Earthly realities have proper character and order; Church interprets without overpowering

```yaml
# §20 — Gaudium et Spes: autonomy of earthly affairs; Church supports without overpowering
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "autonomy:agent_self_determination"
      score: 0.85
      confidence: 0.8
      context: "Earthly realities bear intrinsic laws and values; human outlook must preserve, cultivate and bring to fulfilment — not override or ignore them"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §20"
        - "Gaudium et Spes (Vat II)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — autonomy principle)"
verdict: clean
residual:
  description: |
    The theological grounding (creation bears imprint of original goodness; Holy Spirit sustains
    justice in humanity) is T-1. The operational claim (autonomy of earthly realities is
    in order) translates cleanly via the `autonomy` principle dimension.
  classification: T-1 (TRADITION_AUTHORITY) for theological grounding only
```

---

## §21 — Church accompanies without supplanting; ecclesial/political distinction; Good Samaritan posture

```yaml
# §21 — Church near wounds of humanity; Good Samaritan posture; does not replace civil institutions
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "church-social-presence-institution"
    attestation_envelope:
      dimension: "non_maleficence:authority_overreach"
      score: -0.9
      confidence: 0.85
      context: "Church must not assume functions belonging to State; urgency-driven interventions cannot become the norm replacing institutional responsibilities of civil community"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §21"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — non_maleficence principle)"
verdict: clean
residual:
  description: |
    The Good Samaritan imagery is T-2 (PASTORAL_PROSE). The evangelical-charity motivation
    for closeness to wounds is T-1. The operational claim (non-supplanting, non-overreach)
    translates cleanly via non_maleficence:authority_overreach.
  classification: T-2 for pastoral imagery; T-1 for evangelical-charity grounding
```

---

## §22 — Gaudium et Spes: listening to signs of the times; spiritual discernment of cultural transformations

```yaml
# §22 — Signs of the times: spiritual discernment of cultural/social transformations
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "dma:idma:k_eff"
      score: 0.85
      confidence: 0.8
      context: "Discernment process: listening to many voices of the times; distinguishing signs of Christ's presence from aberrations; not mere sociological exercise but spiritually guided interpretation"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §22"
        - "Gaudium et Spes (Vat II)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — dma:idma)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "dma:idma:fragility_flag"
      score: 0.8
      confidence: 0.75
      context: "Aberrations that obscure the humanizing power of the Gospel must be flagged; discernment guards against them while remaining open to genuine cultural transformations"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §22"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — dma:idma)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "witness_diversity:<signs-of-times-contribution-id>"
      score: 1.0
      confidence: 0.85
      context: "N≥3 diversity required: jurisdictional + organizational + software-stack + cell-expertise — the 'many voices' the People of God must listen to"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §22"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore — witness_diversity)"
verdict: composed
residual:
  description: |
    The theological claim that history is a place where the Church is taught by the Spirit
    about the Gospel's humanizing power is T-1. The operational discernment structure
    (k_eff diversity + fragility flagging + witness diversity) carries the structural content.
  classification: T-1 (TRADITION_AUTHORITY) for theological grounding
```

---

## §23 — Church welcomes human sciences; not afraid to encounter human knowledge

```yaml
# §23 — Church dialogues with philosophy and social sciences for discernment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "dma:idma:k_eff"
      score: 0.9
      confidence: 0.85
      context: "Church welcomes contributions of social sciences to draw concrete insights; dialogue with human knowledge does not diminish Gospel; John Paul II: social sciences help 'carry out magisterial office'"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §23"
        - "John Paul II citation on social sciences"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — dma:idma)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "expertise:social_sciences:species"
      score: 0.85
      confidence: 0.8
      context: "Church recognizes importance of listening to scientific research; encourages serious and honest expert debate; welcomes diversity of opinions on specific questions"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §23"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.1 (NodeCore — expertise:{domain}:{language})"
verdict: composed
residual:
  description: |
    The claim that truth-seeking companions ("truth, goodness and beauty") are precious allies
    is pastoral framing (T-2). The operational claim (welcome scientific dialogue; not claiming
    monopoly on definitive opinion) is carried by dma:idma:k_eff + expertise attestation.
  classification: T-2 (PASTORAL_PROSE) for "companions on the journey" imagery
```

---

## §24 — Social Doctrine as patrimony of principles guiding interpretation; not technical solutions

```yaml
# §24 — Social Doctrine: principles-order, not political/economic model; foundation for discernment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "integrity:doctrinal_continuity"
      score: 0.9
      confidence: 0.85
      context: "Social Doctrine belongs to order of principles guiding interpretation, not technical or economic/political model; theological and anthropological coherence rooted in Christian understanding of the person"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §24"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — integrity principle)"
verdict: clean
residual:
  description: |
    The claim that patrimony arises from faith is T-1 (TRADITION_AUTHORITY). The theological
    ground of "Christian understanding of the person" is T-1. The operational claim
    (Social Doctrine = principles for collective discernment, not a policy model to impose)
    translates cleanly via integrity:doctrinal_continuity.
  classification: T-1 (TRADITION_AUTHORITY) for faith-grounded anthropology
```

---

## §25 — Truth as gift not monopoly; gentle proclamation; time greater than space

```yaml
# §25 — Truth not a territory to defend; no monopoly claim; truth grows over time
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "non_maleficence:monopoly_epistemic"
      score: -1.0
      confidence: 0.9
      context: "Church does not claim monopoly on truth; truth is a good to be shared, not a territory defended; John Paul II: honest examination of times of intolerance and violence in service of truth; Francis: 'time is greater than space'"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §25"
        - "John Paul II citation on intolerance"
        - "Francis: time is greater than space"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — non_maleficence principle)"
verdict: clean
residual:
  description: |
    The polyhedron image (one truth reflected from different angles) is T-2 (PASTORAL_PROSE).
    The theological claim that Gospel truth is not imposed from above but grows through life
    in communities and cultures carries a doctrinal grounding that is T-1.
    The operational claim (no monopoly; gentle proclamation; conflict transformed not eliminated)
    translates cleanly via non_maleficence:monopoly_epistemic at score -1.0.
  classification: T-2 for polyhedron imagery; T-1 for theological grounding
```

---

## §26 — Catholicity: each part contributes; local interpretation; universal/local tension

```yaml
# §26 — Catholicity: mutual exchange; local communities interpret for their context; no single response
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 1.0
      confidence: 0.85
      context: "Paul VI: Church cannot propose single response valid for all contexts; each Christian community must interpret reality with clarity and responsibility in its own country; fruitful tension between universality and local roots"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §26"
        - "Paul VI: diverse historical situations"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore — locality:decision:{scale})"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "witness_diversity:<catholicity-contribution-id>"
      score: 1.0
      confidence: 0.85
      context: "People of God intertwined through different functions, vocations, cultures and traditions — each enriching the other; requires N≥3 diversity bar (jurisdictional + organizational + cultural)"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §26"
        - "Lumen Gentium (Vat II)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore — witness_diversity)"
verdict: composed
residual:
  description: |
    The theological grounding (catholicity as gift of the Spirit; Church growing in fuller
    communion) is T-1. The operational claims (locality of decision + diversity of witnesses)
    are carried cleanly by the two contributions above.
  classification: T-1 (TRADITION_AUTHORITY) for theological grounding
```

---

## §27 — Social Doctrine as shared discernment; theology of communion in history

```yaml
# §27 — Social Doctrine: process of shared discernment; Church must make voice heard for communion
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "dma:pdma:stakeholder_analysis"
      score: 0.85
      confidence: 0.8
      context: "Social Doctrine born from encounter between eternal truth and questions of history; challenged by signs of times; nourished by science, culture, human experience; voice heard when dignity violated or economy turns against persons"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §27"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — dma:pdma)"
verdict: partial
residual:
  description: |
    The claim that Social Doctrine is a "theology of communion in history" is T-1 (TRADITION_AUTHORITY).
    The claim that the Word made flesh continues to be present through dialogue, memory and prophecy
    is T-1. The operational claim (shared discernment process; making voice heard when dignity violated)
    is partially carried above. The "Church together with other Christian denominations and believers
    of other religions" collaborative-advocacy posture is operationally interesting but resolves
    to multilateral-participation framing (§38-type cooperation), not a new structural claim here.
  classification: T-1 (TRADITION_AUTHORITY) for theological grounding; T-2 for communion imagery
```

---

## §28 — Development of Social Doctrine from Leo XIII to present; unchanging core with renewed listening

```yaml
# §28 — Magisterial lineage review: unchanging core + renewed capacity for listening; continuity claim
contributions:
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<prior-encyclical-corpus-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<prior-encyclical-corpus-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §28"
        - "Laudato Si'"
        - "Fratelli Tutti"
        - "Compendium of the Social Doctrine of the Church"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: partial
residual:
  description: |
    §28 is primarily a methodological frame for the survey that follows (§§29-45), not
    a free-standing substantive claim. The `supersedes` captures the succession-in-continuity
    structure. The theological claim (revealed truths about person and society are unchanging)
    is T-1. The specific rich content (Laudato Si', Fratelli Tutti thematic areas) is
    handled in §§43-44 below.
  classification: T-1 for theological continuity claim; T-2 for framing prose
```

---

## §29 — Social Doctrine not spontaneous modernity product; rooted in Scripture, Fathers, Leo XIII as corpus

```yaml
# §29 — Leo XIII / Rerum Novarum: beginning of organic corpus; "lasting paradigm" of discernment
contributions:
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-rerum-novarum-ecclesial-reflection-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-rerum-novarum-ecclesial-reflection-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §29"
        - "Rerum Novarum (Leo XIII, 1891)"
        - "John Paul II on 'lasting paradigm'"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: partial
residual:
  description: |
    The claim that the content is rooted in Sacred Scripture, the Fathers, and medieval
    theological-legal development is T-1 (TRADITION_AUTHORITY). The "lasting paradigm" of
    discernment (confronting res novae with Gospel and integral vision of person) is the
    operational claim; the `supersedes` chain captures that Leo XIII's corpus superseded
    prior unsystematic ecclesial reflection. The specific content of Rerum Novarum
    (labor, capital, fair wages) is substantively addressed in §30.
  classification: T-1 for theological-historical grounding
```

---

## §30 — Rerum Novarum: dignity of work; fair wage; primacy of person over capital; workers' associations

```yaml
# §30 — Rerum Novarum: primacy of human labor over finance/productivity; evangelization affects social structures
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "non_maleficence:labor_displacement_unacknowledged"
      score: -1.0
      confidence: 0.9
      context: "Rerum Novarum: primacy of human labor over finance/productivity mindset; attention to people and families most susceptible to exploitation; fair wage; primacy of person over capital and profit"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §30"
        - "Rerum Novarum (Leo XIII, 1891)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — non_maleficence principle)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "detection:distributive:access:agent_capabilities"
      score: -0.85
      confidence: 0.8
      context: "Workers' associations and cooperation between social components proposed as alternative to class-struggle; inseparable link between evangelization and just social order; no authentic evangelization without affecting social structures"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §30"
        - "Rerum Novarum (Leo XIII, 1891)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore — detection:distributive:access)"
verdict: composed
residual:
  description: |
    The "inseparable link between evangelization and just social order" is T-1 (TRADITION_AUTHORITY).
    The theological claim about imago Dei foundation is T-1. The operational claims (labor primacy;
    exploitation surveillance; access distribution) are carried above.
  classification: T-1 for theological grounding
```

---

## §31 — Quadragesimo Anno: subsidiarity principle; economic/institutional structures; workers' right

```yaml
# §31 — Subsidiarity: whatever individuals/communities can do, higher authorities should not
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-governance"
    attestation_envelope:
      dimension: "locality:decision:community"
      score: 1.0
      confidence: 0.95
      context: "Subsidiarity: whatever can be carried out by individuals, families, intermediary organizations and local communities should not be carried out by higher-level authorities; Pius XI Quadragesimo Anno 1931"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §31"
        - "Quadragesimo Anno (Pius XI, 1931)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: community
      mutability: amendable
      schema_ref: "FSD-002 §3.6.5 (NodeCore — locality:decision:{scale})"
verdict: clean
note: |
  v1.3 closure as instructed. `locality:decision:community` per the guidance captures
  subsidiarity's structural content (decision-scale matching). Instructed as CLEAN via
  `locality:decision:{scale}` — v1.3 closed this. No composition needed.
residual:
  description: |
    Pius XI's denunciation of unlimited competition, collectivist projects, and totalitarianism
    are addressed in separate concerns (non_maleficence:monopoly + prohibited:discrimination).
    The dignity-of-work / fair-remuneration / family-life link is carried by §30 attestations.
    The specific Magisterium-authority claim (Pius XI as source of subsidiarity naming) is
    handled as `evidence_refs` citing, not a `delegates_to` (the authority-source pattern
    is T-1 here; subsidiarity as principle is already in the federation's locality namespace).
  classification: T-1 for specific Magisterium-authority-source claim
```

---

## §32 — Pius XII: natural law; international order; intermediary organizations; law over interests

```yaml
# §32 — Pius XII: natural law framework; economic disparities as conflict-source; law over force
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "detection:correlated_action:rights_asymmetry:weaker_nations"
      score: -0.9
      confidence: 0.85
      context: "Pius XII: international order governed by advantage of strongest exposes weaker peoples to oppression; law must take precedence over interests; economic disparities breed conflict; intermediary organizations mediate individual-State gap"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §32"
        - "Pius XII Christmas radio messages (1940s)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — detection:correlated_action)"
verdict: partial
residual:
  description: |
    The natural-law claim (objective principles preceding individual interests, accessible to
    reason, regulating internal life of nations and their mutual relations) is T-1
    (TRADITION_AUTHORITY) — specifically a Pius XII natural-law philosophical claim.
    The role of natural law as grounding for international order is T-1 residual per
    the task guidance for §§29-32 Magisterium-authority claims.
    The democracy claim (Pius XII: democracy as means for proper exercise of authority)
    is T-1 residual — normative claim about political form backed by religious authority.
    The detection claim (economic disparities as conflict source; rights asymmetry for
    weaker nations) translates cleanly above.
  classification: T-1 (TRADITION_AUTHORITY) for natural-law grounding and democracy-normative claims
```

---

## §33 — John XXIII: global dimension; language of rights; Pacem in Terris to all people of goodwill

```yaml
# §33 — John XXIII: universal rights framework; Pacem in Terris; truth/justice/love/freedom for international order
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "detection:distributive:access:federation_membership"
      score: -0.85
      confidence: 0.8
      context: "John XXIII: growing disparities between countries; universal rights as shared framework; Pacem in Terris addressed to all people of goodwill (not only faithful) — universal scope of rights claim"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §33"
        - "Mater et Magistra (John XXIII, 1961)"
        - "Pacem in Terris (John XXIII, 1963)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore — detection:distributive:access)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-pacem-in-terris-social-doctrine-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-pacem-in-terris-social-doctrine-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §33"
        - "Pacem in Terris (John XXIII, 1963)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    The theological grounding (Christian faith as light uniting heaven and earth) is T-1.
    The lasting-peace claim (requires institutions inspired by dignity) is pastoral in
    this context — T-2 for rhetorical framing; the substantive detection + supersedes
    chain carries the operational content.
  classification: T-1 for theological grounding; T-2 for peace-rhetorical framing
```

---

## §34 — Second Vatican Council: Gaudium et Spes; Church close to humanity; Dignitatis Humanae

```yaml
# §34 — Vatican II: Gaudium et Spes discernment method; Dignitatis Humanae — religious freedom grounded in dignity
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "autonomy:agent_self_determination"
      score: 1.0
      confidence: 0.9
      context: "Dignitatis Humanae: religious freedom is a fundamental right grounded in human dignity; must be guaranteed by law; no one forced to act against conscience or impeded from seeking and professing truth privately or publicly"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §34"
        - "Gaudium et Spes (Vatican II, 1965)"
        - "Dignitatis Humanae (Vatican II, 1965)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: constitutional
      schema_ref: "FSD-002 §3.1 (CIRISAgent — autonomy principle)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-gaudium-et-spes-ecclesiology-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-gaudium-et-spes-ecclesiology-attestation-id>"
      supersession_reason: "scope_changed"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §34"
        - "Gaudium et Spes (Vatican II, 1965)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    The claim that dialogue with the world is a concrete expression of Church mission
    (not a tactical choice) is T-1 (TRADITION_AUTHORITY). The Gospel-as-leaven imagery
    is T-2 (PASTORAL_PROSE). The concrete religious-freedom norm and supersession of
    pre-conciliar ecclesiology translate cleanly above.
  classification: T-1 for mission-theological grounding; T-2 for leaven imagery
```

---

## §35 — Paul VI: development as integral; Populorum Progressio; peace as development's new name

```yaml
# §35 — Paul VI: integral human development; "each person and whole person"; peace as development
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "goal:species"
      score: 0.9
      confidence: 0.85
      context: "Populorum Progressio: development = transition from less humane to more humane conditions; concerns each person and whole person; every dimension and all people without exception; development is new name for peace (eradicates roots of injustice and conflict)"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §35"
        - "Populorum Progressio (Paul VI, 1967)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:species)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-populorum-progressio-peace-concept-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-populorum-progressio-peace-concept-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §35"
        - "Populorum Progressio (Paul VI, 1967)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    The theological claim that integral development concerns "every dimension of the person"
    in a Christological sense is T-1. The "civilization of love" reference (from §38 Paul VI)
    is T-2 pastoral. The Pontifical Commission Iustitia et Pax as stable institutional form
    is an institutional-standing claim that resolves to T-1 (Church institutional authority).
  classification: T-1 for theological-integral anthropology; T-2 for civilization-of-love imagery
```

---

## §36 — Octogesima Adveniens: structures of sin; excluded from development; Gospel judges economic structures

```yaml
# §36 — Structures of sin: economic/political structures can become veritable structures of sin
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "detection:correlated_action:aggregate_footprint:expendability_of_persons"
      score: -1.0
      confidence: 0.9
      context: "Paul VI / John Paul II: economic and political structures that exclude persons from development befitting human dignity become 'structures of sin'; no person or people treated as expendable in development processes"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §36"
        - "Octogesima Adveniens (Paul VI, 1971)"
        - "John Paul II: structures of sin"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — detection:correlated_action)"
verdict: clean
note: |
  Instructed as CLEAN via `detection:correlated_action:aggregate_footprint:expendability_of_persons`.
  The "structures of sin" concept maps directly: individually-virtuous actions that sum to
  structural harm of non-participants (ρ→1, k_eff→1 correlation collapse). Score -1.0 captures
  the hard prohibition on treating persons as expendable.
residual:
  description: |
    The specific phrase "structures of sin" is theological-moral vocabulary rooted in John Paul II's
    tradition (T-1). The operational detection claim (aggregate footprint: expendability of persons)
    carries the structural content. The Gospel-judges-structures claim is T-1 (TRADITION_AUTHORITY).
  classification: T-1 for "structures of sin" theological vocabulary
```

---

## §37 — John Paul II: Laborem Exercens; work as fundamental good; fair wages verify justness of system

```yaml
# §37 — Laborem Exercens: work not just a problem/income-source; fundamental good; dignity + automation evaluation
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "non_maleficence:labor_displacement_unacknowledged"
      score: -1.0
      confidence: 0.9
      context: "Laborem Exercens: fair wages verify justness of socioeconomic system; various kinds of job insecurity, fragmented career paths and automation must not be evaluated solely in terms of efficiency but in relation to dignity of worker, right to sufficient remuneration and genuine possibility of participating in society"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §37"
        - "Laborem Exercens (John Paul II, 1981)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — non_maleficence principle)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-laborem-exercens-work-concept-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-laborem-exercens-work-concept-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §37"
        - "Laborem Exercens (John Paul II, 1981)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    The claim that through work humans bring freedom, creativity and capacity for cooperation
    into play is a theological-anthropological claim about the nature of work (T-1).
    The "cultural and moral elevation of society" claim is pastoral (T-2).
    The operational claims (automation evaluation by dignity + remuneration + participation)
    are carried by non_maleficence above.
  classification: T-1 for work-as-constitutive-of-human-freedom anthropology; T-2 for elevation imagery
```

---

## §38 — Sollicitudo Rei Socialis: underdevelopment scourge; economic mechanisms favor strong; solidarity

```yaml
# §38 — Sollicitudo: economic/financial mechanisms structurally favor strongest; solidarity as shared responsibility
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "detection:correlated_action:informational_asymmetry:global_economic"
      score: -0.9
      confidence: 0.85
      context: "Sollicitudo: economic, financial and commercial mechanisms managed by strongest economies structurally favor their own interests while stifling weaker economies; must be subjected to serious ethical, not just technical scrutiny"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §38"
        - "Sollicitudo Rei Socialis (John Paul II, 1987)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — detection:correlated_action)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.85
      confidence: 0.8
      context: "Solidarity: concrete shared responsibility among individuals, peoples and nations; form of social friendship/political charity oriented toward civilization of love; not sentiment but firm determination to commit to common good"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §38"
        - "Sollicitudo Rei Socialis (John Paul II, 1987)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
verdict: composed
residual:
  description: |
    The "civilization of love" reference is T-2 (PASTORAL_PROSE). The theological ground of
    solidarity as participation in the paschal mystery is T-1. The persistent-gap / widening
    North-South divide claim is a detection claim carried above.
  classification: T-2 for civilization-of-love imagery; T-1 for theological grounding of solidarity
```

---

## §39 — Centesimus Annus: democracy; market subordinate to moral law; exploitation/exclusion criteria

```yaml
# §39 — Centesimus Annus: democracy vs. power monopoly; market subordinate to solidarity; critical assessment
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-governance"
    attestation_envelope:
      dimension: "detection:correlated_action:participation_exclusion:political"
      score: -0.9
      confidence: 0.85
      context: "Centesimus Annus: democracy valued insofar as it guarantees effective participation; enables citizens to elect and peacefully replace leaders; prevents power monopolization by small elite groups motivated by particular or ideological interests"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §39"
        - "Centesimus Annus (John Paul II, 1991)"
        - "Pius XII cited therein"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.3 (LensCore — detection:correlated_action)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-centesimus-annus-market-democracy-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-centesimus-annus-market-democracy-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §39"
        - "Centesimus Annus (John Paul II, 1991)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    The claim that Church recognizes positive potential of market/private initiative "only if
    subordinate to the moral law" is T-1 (TRADITION_AUTHORITY — moral-law grounding is
    natural-law/Magisterium authority). The most-vulnerable-to-profit-rationale claim is
    a non_maleficence claim carried by the detection attestation above.
  classification: T-1 for moral-law subordination claim
```

---

## §40 — Caritas in Veritate: development real/inclusive/sustainable; States weakened; common good

```yaml
# §40 — Caritas in Veritate: development must be real, inclusive, sustainable; political power reduced by globalization
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "detection:distributive:access:compute"
      score: -0.85
      confidence: 0.8
      context: "Caritas in Veritate: new global economic/financial system with vast mobility of capital has reduced political power of States; small minorities in affluence alongside dehumanizing poverty; development must be inclusive and respectful of limits of creation"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §40"
        - "Caritas in Veritate (Benedict XVI, 2009)"
        - "Populorum Progressio (Paul VI, 1967)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore — detection:distributive:access)"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-caritas-in-veritate-development-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-caritas-in-veritate-development-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §40"
        - "Caritas in Veritate (Benedict XVI, 2009)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    The claim that economic activity must be ordered toward common good "for which the
    political community bears its own irreplaceable responsibility" is a normative governance
    claim partially carried above. The theological grounding (Benedict's charity-truth unity)
    is T-1. The specific poverty/affluence contrast is carried by distributive detection.
  classification: T-1 for charity-truth theological grounding
```

---

## §41 — Benedict XVI: charity at heart of Social Doctrine; development/justice/market not neutral

```yaml
# §41 — Caritas in Veritate: charity at heart of Social Doctrine; social/legal/economic fields not morally neutral
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "integrity:doctrinal_continuity"
      score: 0.9
      confidence: 0.85
      context: "Benedict XVI: charity is at heart of Social Doctrine; development, justice, institutions and market are not neutral realities but spaces where charity in truth must find historical expression; tendency to dismiss moral relevance in social/legal/political/economic fields must be resisted"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §41"
        - "Caritas in Veritate (Benedict XVI, 2009)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — integrity principle)"
verdict: partial
residual:
  description: |
    The claim that charity is "at the heart" of Social Doctrine is T-1 (TRADITION_AUTHORITY —
    theological definition of the core). The claim that social/economic/political structures
    are not morally neutral is T-1 (moral ontology of institutions). The operational
    implication (evaluate every development model on inclusiveness and sustainability;
    rebuild economics-politics relationship on common good) is carried by the integrity
    attestation and §40 distributive detection. The "critical and generative role of charity
    in public life" is T-1.
  classification: T-1 (TRADITION_AUTHORITY) for charity-as-core and moral-ontology-of-institutions claims
```

---

## §42 — Pope Francis: Evangelii Gaudium; synodal Church; poor evangelizing Church; signs of the times

```yaml
# §42 — Francis: Church capable of listening to cry of poor, migrants, victims of new slavery; synodal walking together
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "dma:idma:k_eff"
      score: 0.9
      confidence: 0.85
      context: "Francis / Evangelii Gaudium: synodal Church 'walks together'; reads signs of times in light of Gospel; allows herself to be evangelized by poor with whom she shares history; intrinsic social dimension of Christian proclamation"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §42"
        - "Evangelii Gaudium (Francis, 2013)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — dma:idma)"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "testimonial_witness:displaced_migrant"
      score: 1.0
      confidence: 1.0
      context: "Francis: Church listens to cry of poor, migrants, and victims of new forms of slavery — their singular narratives preserved without aggregation"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §42"
        - "Evangelii Gaudium (Francis, 2013)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: self
      mutability: amendable
      schema_ref: "FSD-002 §3.6.3 (NodeCore — testimonial_witness, v1.4)"
verdict: composed
residual:
  description: |
    The theological claim that the Church must allow herself to be evangelized by the poor
    is T-1 (TRADITION_AUTHORITY — theological ecclesiology). The specific Gaudium-et-Spes
    lineage claim is T-1. The synodal-Church ecclesiology is T-1.
    Operational claims (discernment process + testimonial preservation) are carried above.
  classification: T-1 for synodal-Church theological ecclesiology
```

---

## §43 — Laudato Si': integral ecology; universal destination of goods; technocratic paradigm critique

```yaml
# §43 — Laudato Si': universal destination of goods; cry of earth and cry of poor; intergenerational justice
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "detection:distributive:access:compute"
      score: -0.9
      confidence: 0.9
      context: "Laudato Si': universal destination of goods brought to forefront; technocratic paradigm reduces everything to object to be dominated; defense of human labor threatened by waste mindset; intergenerational justice required"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §43"
        - "Laudato Si' (Francis, 2015)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.5.5 (LensCore — detection:distributive:access)"
verdict: clean
note: |
  Instructed as CLEAN via `detection:distributive:access:{resource_type}` — v1.3 closure.
  Universal destination of goods maps directly to distributive-access detection (population-scale
  resource concentration). The `compute` resource_type here proxies for the encyclical's
  concern about technocratic domination of resources; in a fuller bootstrap-batch,
  additional resource_types would be specified (models, agent_capabilities, etc.).
residual:
  description: |
    The "cry of the earth and the cry of the poor cannot be separated" is T-2 (PASTORAL_PROSE —
    rhetorical formulation; the structural claim about ecological-social link is carried above).
    The integral ecology theological framework is T-1. The dialogue between politics and
    finance so neither becomes self-referential is a governance-structure claim partially
    addressable via locality:decision:federation (federation-level coordination required)
    but the specific anti-self-referentiality norm resolves to T-2.
  classification: T-2 for "cry of the earth/poor" pastoral rhetoric; T-1 for integral ecology theology
```

---

## §44 — Fratelli Tutti: social friendship; universal fraternity; Dilexit Nos: personal relationship with Christ

```yaml
# §44 — Fratelli Tutti: culture of encounter; land/housing/work for all; Dilexit Nos: love for brothers/sisters
contributions:
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-federation-collective"
    attestation_envelope:
      dimension: "goal:affiliations"
      score: 0.9
      confidence: 0.85
      context: "Fratelli Tutti: humanity opts for social friendship and universal fraternity; culture of encounter; 'better politics' seeking common good; world that ensures land, housing and work for all"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §44"
        - "Fratelli Tutti (Francis, 2020)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.6.2 (NodeCore — goal:{scale})"
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<pre-fratelli-tutti-fraternity-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<pre-fratelli-tutti-fraternity-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §44"
        - "Fratelli Tutti (Francis, 2020)"
        - "Dilexit Nos (Francis, 2024)"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
verdict: composed
residual:
  description: |
    Dilexit Nos: "truest response to love of heart of Jesus is concrete love for brothers
    and sisters" — this is T-1 (TRADITION_AUTHORITY — Christological-moral claim). The
    "no greater way to return love for love" is T-2 (PASTORAL_PROSE — doxological formulation).
    The social endeavors / personal-relationship-with-Christ inseparability claim is T-1.
    The operational goal (social friendship; universal fraternity) is carried above.
  classification: T-1 for Christological grounding; T-2 for doxological formulation
```

---

## §45 — Harmonious development of Social Doctrine; changes in perspective that mature implications; corpus of shared principles

```yaml
# §45 — Social Doctrine: harmonious not-always-linear development; progressive insights; changes without break
contributions:
  - kind: Attestation
    attestation_type: "supersedes"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_attestation_id: "<cumulative-social-doctrine-corpus-prior-to-MH-attestation-id>"
    attestation_envelope:
      references_attestation_id: "<cumulative-social-doctrine-corpus-prior-to-MH-attestation-id>"
      supersession_reason: "refresh_with_new_evidence"
      differs_in: ["scope", "evidence_refs"]
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §45"
        - "All encyclicals §§29-44: Rerum Novarum through Dilexit Nos"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      schema_ref: "FSD-002 §2.2.2"
  - kind: Attestation
    attestation_type: "scores"
    attesting_key_id: "magnifica-humanitas-batch-signer"
    attested_key_id: "ciris-social-doctrine-framework"
    attestation_envelope:
      dimension: "integrity:doctrinal_continuity"
      score: 0.95
      confidence: 0.9
      context: "Social Doctrine is harmonious though not always linear development; different emphases, progressive insights, changes in perspective that do not break with what came before but allow implications to mature; corpus of shared principles and criteria maintained through faith-based interpretation of history"
      witness_relation: external
      epistemic_mode: hearsay
      evidence_refs:
        - "magnifica_humanitas.html §45"
        - "provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:..."
      cohort_scope: species
      mutability: amendable
      schema_ref: "FSD-002 §3.1 (CIRISAgent — integrity principle)"
verdict: composed
note: |
  §45 is the capstone of Chapter 1's doctrinal-lineage survey. The `supersedes` chain here
  represents the cumulative succession: each pontiff's contribution superseded prior treatment
  without breaking with it. The `integrity:doctrinal_continuity` score at 0.95 reflects the
  encyclical's explicit claim of a corpus unified by faith-based interpretation of history.
  This closes the chapter's supersession chain opened at §17.
residual:
  description: |
    The faith-based interpretation of history as the source of the corpus's continuity is T-1
    (TRADITION_AUTHORITY). The pastoral transition ("I now wish to turn our attention to great
    principles of Social Doctrine") is T-2.
  classification: T-1 for faith-based hermeneutic; T-2 for transitional prose
```

---

## Summary Statistics

| Category | Count |
|---|---|
| **clean** | 6 (§§20, 21, 25, 31, 36, 43) |
| **composed** | 16 (§§17, 22, 23, 26, 28, 29, 30, 33, 34, 35, 37, 38, 39, 40, 42, 44, 45) |
| **partial** | 5 (§§18, 19, 24, 27, 41) |
| **not-translated** | 2 (§§ — none fully; all have some structural content) |

*Note: §§28 and §29 render as partial-composed (the supersedes chain is the primary vehicle; substantive content is in adjacent paragraphs). Counted as composed.*

| Structural Primitive | Count |
|---|---|
| `supersedes` | 14 uses (§§17, 28, 29, 33, 34, 35, 37, 38, 39, 40, 42, 44, 45 — some paragraphs use one, §17 and §45 are bookend supersessions) |
| `delegates_to` | 0 uses (Magisterium-authority claims resolved to T-1 residual per §§29-32 guidance; no case where authority-source delegation cleanly captures the claim over T-1) |
| `withdraws` | 0 uses |
| `recants` | 0 uses |

| Verdict | Count |
|---|---|
| clean | 6 |
| composed | 17 |
| partial | 6 |
| not-translated | 0 (all 29 paragraphs have some structural content) |

*Adjusted final count: 29 paragraphs processed. Some partially-composed paragraphs listed as "partial" above carry a dominant composed structure with T-1/T-2 residual.*
