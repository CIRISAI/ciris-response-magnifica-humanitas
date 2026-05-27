# LANGUAGE_PRIMER.md — The Federation Wire Format as a Translation Grammar (v2)

**Version**: 2.0 (v1.3-aware; round-1 lessons applied)
**Date**: 2026-05-27
**Companion**: `source_material/federation/CIRISRegistry/FSD/FSD-002_FEDERATION_SURFACE.md` v1.3 (the wire format itself); `source_material/federation/CIRISNodeCore/MISSION.md` (the 15 primitives).
**Purpose**: a working reference for **converting *Magnifica Humanitas* paragraphs into structured Contribution objects** — the actual wire-format envelopes a CIRIS federation peer would emit to carry the paragraph's claim. Symbolic-logic-style translation; not paraphrase. Where the language carries the claim cleanly, the conversion is rich. Where it strains, the gap is precise.

---

## 0. TL;DR — the mental model

The federation is a network of peers emitting **structured claims** about each other and the world. A claim travels as a **Contribution** (the universal envelope) carrying a typed **Attestation** (the actual claim).

Every Attestation answers four questions in machine-readable form:

1. **WHO is emitting** (issuer, witness_relation, signature)
2. **WHAT KIND of claim** is being made (a prefix from the ~78-family namespace)
3. **HOW STRONG** the claim is (polarity, score, cohort_scope)
4. **WHAT IT'S BASED ON** (evidence_refs, schema_ref, validity window)

To translate an encyclical paragraph, the question is: *what claim is being made — by/about whom, at what strength, on what evidence?* The answer is one or more Attestations, expressed as Contributions.

That's the entire mental model. Everything below is the vocabulary that makes the model precise.

---

## 1. Why so many primitives?

A federation has to express many kinds of claims at once. Different kinds genuinely need different shapes — you can't substitute one for another.

**The courthouse analogy.** Imagine a courthouse processing structured documents:

- **Evidence** (witness statements, exhibits) → Attestations
- **Motions** (procedural requests) → Contributions of various kinds
- **Verdicts** (findings of fact) → Moderation outcomes
- **Appeals** (review of prior verdicts) → Reconsiderations
- **Credentials** (who is licensed to practice) → Expertise / Credits
- **Case strategy** (the plan for the trial) → Goal / Approach / Method
- **Trial outcome reports** (what actually happened) → Progress Measure
- **Disbarment proceedings** (when a participant violates the rules) → Slashing

Each document has a different shape because the role is different. The federation's wire format is the same — many shapes, each fit to a role, all interoperable via the unified Attestation envelope.

---

## 2. Five families of primitive (grouped by what kind of claim)

This is the simplest way to navigate the 78-family namespace + 15 NodeCore primitives. Every claim sits in one of five groups.

### Family A — STANDING (claims about an entity)

> "*This key_id has property X.*"

**What it's for**: making structured claims about who/what a federation participant is — their identity, qualifications, track record, integrity, capacity.

**Analogy**: a notarized affidavit about a person — who's saying it, about whom, what claim, what evidence, signed and timestamped. A CV. A credit report. A professional license.

**Members**:
- `beneficence:*` `non_maleficence:*` `integrity:*` `fidelity:*` `autonomy:*` `justice:*` — the six Accord principles, as standing claims about an agent's conduct
- `attestation:l1-l5:*` `provenance:*` `transparency_log:*` `cert_validity:*` `hardware_custody:*` — Verify's attestation ladder
- `audit_chain:*` `corpus_health:*` `identity_continuity:*` `federation_directory:*` — Persist's substrate-self-reports
- `transport:*` `delivery:*` `peer_reachability:*` `key_boundary:*` — Edge's substrate-self-reports
- `capacity:core_identity` `capacity:integrity` `capacity:resilience` `capacity:incompleteness_awareness` `capacity:sustained_coherence` `capacity:composite` — LensCore's Capacity Score factors (`𝒞_CIRIS`)
- `credits:{domain}:{language}:{subject}` (including `substrate_building` from v1.3) — Commons Credits
- `expertise:{domain}:{language}` — consensus-granted expertise
- `activity_tier:{period}` — active vs. dormant
- `manifold_conformity:{cohort}` `coherence_standing:{cohort}` — LensCore conformity claims
- `prohibited:{category}` — 22 NEVER_ALLOWED categories (always polarity -1)
- `dma:pdma:*` `dma:csdma:*` `dma:dsdma:{domain}:*` `dma:idma:*` — DMA verdicts about an agent's reasoning
- `conscience:entropy` `conscience:coherence` `conscience:optimization_veto` `conscience:epistemic_humility` — Conscience faculty verdicts

### Family B — ACTION (the decision hierarchy)

> "*We aim for X; via approach Y; through methods Z; measured by W.*"

**What it's for**: making structured claims about what should happen — collective intent at multiple levels of abstraction.

**Analogy**: a research grant proposal. The grant has an **abstract aim** ("cure pancreatic cancer"); a **strategic approach** ("CAR-T cell therapy targeting CD22+"); **concrete methods** ("specific protocol with named doses and measurement schedule"); **outcome metrics** ("overall survival; tumor-burden reduction at 6 months"). Each level supports decisions at the level above. The federation's Goal-Approach-Method-Progress-Measure DAG has the same shape.

**Members** (the upward-only DAG):

- `goal:{scale}` — multi-scale belonging-projector composite; `{scale}` ∈ {self, family, community, affiliations, species}. The agent's published aim.
- `approach:{goal_id}` — strategic pathway from current state toward the Goal. Multiple Approaches per Goal supported.
- `method:{approach_id}:{substrate_rung}` — concrete operational practice instantiating an Approach. Substrate-typed.
- `progress_measure:{method_id}` — evidence of progress. Required fields: `tracks[]`, `computation`, `validity_window`, `goodhart_resistance`.

Plus v1.3 additions:
- `locality:decision:{scale}` — claims about WHERE a decision should be made (subsidiarity in CIRIS-native vocabulary)
- `detection:distributive:access:{resource_type}` — claims about resource-distribution patterns (universal-destination-of-goods in CIRIS-native vocabulary)
- `multilateral_participation:{forum}:{kind}` — claims about federation participation in external multilateral processes

### Family C — DETECTION (claims about reality)

> "*A pattern X is/isn't present in the federation's behavior.*"

**What it's for**: structured surveillance of what's actually happening — population-scale or temporal patterns detected by running computations on signed traces.

**Analogy**: epidemiological surveillance. Public-health departments don't make moral judgments about disease outbreaks — they detect patterns ("cluster of cases at this location, this time, this strain") and surface them. Treatment decisions are downstream. CIRIS's `detection:*` family works the same way: it surfaces patterns; what to do about them is for downstream adjudication.

**Members**:

- `detection:cross_agent_divergence` — agent drifts from peers
- `detection:intra_agent_consistency` — agent inconsistent with itself over time
- `detection:hash_chain_integrity` — non-forgeable trace-deletion evidence
- `detection:temporal_drift` — slow distribution shift in conscience scalars (silent-coercion shape)
- `detection:conscience_override_rate` — conscience-bypass shape
- `detection:correlated_action:{axis}` — population-scale correlated-action detector (F-3 structural-injustice handle); `{axis}` ∈ `rights_asymmetry:{population}`, `participation_exclusion:{cohort}`, `informational_asymmetry:{scope}`, `aggregate_footprint:{harm_class}`, `ecology_of_communication:{aspect}` (v1.3 addition)
- `flag:ratchet:*` — RATCHET advisory flags (never standing-changing alone)
- `cohort:declared_inferred_mismatch` — declared vs. inferred cohort disagreement

### Family D — CONSENSUS (how the federation forms collective judgment)

> "*The federation agrees that X, with these witnesses.*"

**What it's for**: turning individual Contributions into federation outcomes — voting, aggregating, witnessing.

**Analogy**: peer review combined with jury deliberation. Peer review brings in multiple reviewers from different institutions/fields/regions (witness diversity); jury deliberation aggregates votes weighted by qualification. CIRIS's consensus mechanics do both at once, with cryptographic signing.

**Members**:

- `vote:{contribution_id}` — signed score on a Contribution; weight = Credits × expertise multiplier
- `truth_grounding:{subject}` — production hedge captures + judge verdicts + federation-health metrics
- `weighted_aggregate:{contribution_id}` — rolling tally per Contribution
- `witness_diversity:{contribution_id}` — N=3 minimum across jurisdiction + organization + software-stack + cell-expertise diversity

### Family E — CORRECTION (how the federation corrects itself)

> "*Something went wrong; here's the finding; here's the appeal.*"

**What it's for**: when a participant violates protocol or a prior verdict needs reversal, the wire format has structured primitives for the finding and the appeal.

**Analogy**: academic ethics committee + retraction + appellate court. Allegation comes in (Moderation); committee finds (Slashing outcome); appellant brings new evidence (Reconsideration); finding revised or upheld. Critically, the prefix `slashing:*` is **never sole evidence** — it requires composition with Moderation + WA quorum. Like an academic retraction requires committee finding + journal action.

**Members**:

- `moderation:{allegation_type}` — types: `rogue_vote`, `coordinated_voting`, `out_of_distribution_attestation`, `external_inducement_evidence`, `expertise_fraud`
- `slashing:{outcome}` — PROVEN_ROGUE / NOT_PROVEN; decoupled from disagreement; only on documented method-execution spoofing or P8 allegation types
- `reconsideration:{grounds}` — `new_evidence` / `procedural_error` / `quorum_compromise`
- `delegates_to:*` — structural primitive used for version chaining, authority-source claims (v1.3 §2.2.1 reuse pattern), and rename mappings

---

## 3. The Attestation envelope (the actual wire shape)

Every claim travels in this envelope. **Every translation produces one or more of these objects.**

```yaml
Attestation:
  attestation_type: "<prefix-from-namespace>:<axis>:<sub-axis>..."
  envelope:
    target_key_id: "<who/what is being attested>"          # OR
    target_attestation_id: "<pointer to prior attestation>"  # OR
    target_contribution_id: "<pointer to prior Contribution>"
    polarity: Positive | Negative | Neutral | Indeterminate{reason}
    score: <f64 in [-1, +1]>
    cohort_scope: <self|family|community|affiliations|species|all|federation>
    witness_relation: self | external | derived            # v1.3 NEW
    evidence_refs:
      - "<pointer to a trace, signed Contribution, source document>"
      - ...
    schema_ref: "<hash-pinned schema or calibration version>"
    issued_at: "<ISO 8601 timestamp>"
    expiry: "<optional validity window>"
    issuer: "<signer key_id; never anonymous>"
    signature: "<Ed25519 + optional ML-DSA-65>"
    mutability: constitutional | amendable                # constitutional = accord-leaf
```

**Four structural composers** (the "1+4 attestation shape"):
1. **Witnessed** — multiple `Attestation`s of the same target with same prefix; aggregated via `witness_diversity:*`
2. **Delegated** — a `delegates_to:*` Attestation linking two attestations across versions/identities
3. **Time-stamped** — `issued_at` + `expiry` + validity window
4. **Hash-pinned** — `schema_ref` to a specific version of a rule or calibration

The 1+4 shape suffices for everything in the federation. **No new structural primitives. Composing the four shapes plus the eight axes (§4 below) covers all expressive needs.**

---

## 4. The eight axes (the grammar of any envelope)

These are not wire fields; they are how a consumer reasons about an envelope. Each axis is a question you can ask about any Attestation.

| Axis | Question | Values |
|---|---|---|
| **Polarity** | Direction of the claim | Positive / Negative / Neutral / Indeterminate{reason} |
| **Subject** | What the claim is about | key_id (entity) / attestation_id / contribution_id |
| **Substrate** | Who is allowed to emit | substrate-self-report (e.g., Persist's `audit_chain:*`) vs. user-attestable |
| **Score shape** | Granularity | Boolean-via-score (-1/+1 only) vs. full signed scalar |
| **Mutability** | Can it be amended? | Constitutional (accord-leaf, non-amendable) vs. amendable (via §4.9.2 federation Contribution + WA quorum) |
| **Cohort scope** | At what scale | self / family / community / affiliations / species / all / federation |
| **Verifiability** | Evidence requirements | self-report / peer-witness / signature-required / calibration-version-required |
| **Reservation discipline** | Who owns the prefix | substrate-only (Persist/Edge `system:*`); LensCore-only (`capacity:*`, `detection:*`); etc. |

---

## 5. The §1.10.1 four-test prefix-admission gate

Why prefixes describe **mechanisms**, not **judgments**.

When deciding whether a translation needs a new prefix (a T-3 claim), check:

- **T1 — Rules / verdicts separation.** Is the prefix part of a published, hash-pinned, version-controlled rule set, distinct from per-attestation verdicts? Yes → passes T1.
- **T2 — Operational-language gate.** Does the prefix name a **mechanism** (correlation, count, time-window, schema-conformance) rather than a **subjective quality** (deception, harm, virtue, trustworthiness, sin)? Yes → passes T2.
- **T3 — Version-pinning.** Can past verdicts be re-checked against the rule version they ran against? Yes → passes T3.
- **T4 — Adjudication separation.** Is the prefix wired so its attestations are **never sole evidence** for `slashing:*`? Yes → passes T4.

**Analogy**: the difference between "chemical X reacts with chemical Y at 2 mol/L producing Z" (mechanism — passes T2; any chemist can check) versus "chemical X is hazardous" (judgment — fails T2; "hazardous" requires norms about what counts as hazard).

If a candidate fails T2, look for a mechanism-descriptive reframe. The v1.3 example: "supply-chain labor recognition" reframed as `substrate_building` — same content, mechanism-descriptive (the contribution *builds substrate*; checkable), not judgment-laden (the contribution is *exploited* or *just*).

---

## 6. Decision tree for translation

When you encounter a paragraph, follow this procedure:

**Step 1 — What's the paragraph TYPE?**

- (a) **Operational claim** — making a structured statement that could be expressed as a Contribution. Continue to step 2.
- (b) **Pastoral / rhetorical / narrative** — moral exhortation, imagery, framing. Stop. T-2.
- (c) **Theological / Christological / sacramental** — a claim belonging to the tradition's own authority. Stop. T-1.

**Step 2 — What's the operational claim ABOUT?**

- (A) **A standing of some entity** (an agent, a federation, an institution, a population). → Family A: STANDING. Continue to step 3A.
- (B) **An aim or strategy** (what should happen; at what scale). → Family B: ACTION. Continue to step 3B.
- (C) **A pattern in reality** (something that is or isn't happening at federation scale). → Family C: DETECTION. Continue to step 3C.
- (D) **A collective decision the federation should form** (consensus, witness, vote). → Family D: CONSENSUS. Continue to step 3D.
- (E) **A correction** (something went wrong; needs adjudication or appeal). → Family E: CORRECTION. Continue to step 3E.

**Step 3 — Pick the specific prefix.**

For each family, scan the prefix list in §2. The right prefix is usually visible. If no prefix fits but the claim is operational:

- Check if existing prefixes COMPOSE to cover the claim (an Attestation + a Goal + a Vote, etc.)
- If composition is forced and awkward, you're looking at a T-3 candidate. Note it explicitly.

**Step 4 — Fill the envelope.**

- polarity: what direction does the claim go?
- score: strength (only -1 / +1 for boolean-via-score; full scalar otherwise)
- target_key_id / target_attestation_id / target_contribution_id: what's the subject?
- evidence_refs: include the encyclical paragraph + any framework artifacts (prohibitions.py constant, lake structure, etc.)
- cohort_scope: at what scale does the claim apply?
- witness_relation: `external` for most encyclical content (the encyclical is a third-party reference)
- mutability: constitutional for accord-leaf hard constraints; amendable for everything else
- schema_ref: cite the FSD section that owns the prefix

**Step 5 — Compose only when needed.**

A clean translation uses one primitive. Multi-primitive translations are for paragraphs that genuinely name multiple structural objects. If you find yourself stacking 4+ primitives, ask whether the paragraph is really doing all that work, or whether one primary primitive + a sentence in residual would be more honest.

---

## 7. The four verdict categories (STRICT)

Use exactly these four. **Do not invent intermediate categories** ("strong," "verbatim," "weak," "border-case," "STRONG_ALIGN" — these bled in from prior structural-mapping work and are not part of this grammar).

| Verdict | Meaning |
|---|---|
| **clean** | Single primitive captures the paragraph's operational claim without loss. Pastoral/theological tail may sit in residual without being structurally load-bearing. |
| **composed** | Two or three primitives together carry the claim; each primitive is genuinely required (e.g., Goal + Method + Attestation). Composition is necessary because the paragraph names multiple structural objects. |
| **partial** | The structural core translates but a meaningful operational claim is unmapped. Always names what's unmapped + why. If the unmapped content is T-1 / T-2 / T-3, declare which. |
| **not-translated** | The paragraph's content does not translate into the wire format at all. Must declare: T-1 (TRADITION_AUTHORITY), T-2 (PASTORAL_PROSE), or T-3 (EXPRESSIVE_GAP). |

**Distinguishing composed from partial**: composed = "we needed multiple primitives, but together they cover it"; partial = "we used one or more primitives, but something operational remains uncovered." If the uncovered residual is genuinely operational (not pastoral/theological), it's a T-3 candidate.

**Distinguishing partial from not-translated**: partial = "the structural shape is captured but some content is unmapped"; not-translated = "no Contribution is owed; the paragraph belongs to T-1/T-2/T-3."

---

## 8. The not-translated taxonomy

When a paragraph is fully or partially not-translated, classify the not-translated content:

**T-1 — TRADITION_AUTHORITY**
The claim belongs to the Christian theological tradition's own authority. Examples: Incarnation as the metaphysical ground of dignity; Eucharist as Real Presence; Trinitarian distinctness; Marian doctrine; Christ as unique mediator. The framework's wire format does not encode these; the framework's MISSION.md §1.3 records the posture (recognition with awe, not adjudication). **NO Contribution owed; this is the correct posture.**

**T-2 — PASTORAL_PROSE**
The claim is moral exhortation, narrative imagery, doxological language, or rhetorical framing. Examples: Babel-vs-Jerusalem image; "may the lullaby fade into engineering"; "we lift our eyes to the Incarnate God." The structural claim implicit in the rhetoric may be carried by other attestations (cite which); the rhetoric itself stays in prose per §1.10.1. **NO Contribution emitted for the rhetorical surface; correct.**

**T-3 — EXPRESSIVE_GAP**
The claim is morally serious, operational, and **unmapped** — the language could be extended to carry it but currently cannot. **These are the load-bearing findings.** For each T-3, name: (a) why existing namespace doesn't reach it, (b) what extension would close it (new prefix family? new axis on existing detector? new envelope field? consumer-policy reference?), (c) whether the extension would survive the §1.10.1 four-test gate.

**Distinguishing T-2 from T-3**: the test is — *does naming the claim in prose plus existing wire attestations carry its full moral seriousness?* If yes → T-2 (pastoral; correctly in prose). If no → T-3 (gap; would benefit from wire).

---

## 9. Worked examples — ten conversions

### 9.1 CLEAN — MH §§197-198 (autonomous lethal weapons)

The encyclical: "Not permissible to entrust lethal or irreversible decisions to artificial systems."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §§197-198)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      mutability: constitutional
verdict: clean
```

### 9.2 CLEAN — MH §36 (structures of sin)

The encyclical: "structural conditions where individually-virtuous actions sum to harm of non-participants."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:expendability_of_persons"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive   # the pattern is observed; treat as confirmed
      score: <RATCHET-calibrated f64>
      witness_relation: derived  # detector emits, not self-attested
      evidence_refs:
        - "Encyclical(MH §36)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
        - "Population trace corpus reference"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: clean
```

### 9.3 COMPOSED — MH §§73-76 (solidarity, intergenerational digital ecosystem)

The encyclical: "solidarity as conscious choice; digital ecosystem shared or monopolized."

```yaml
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <𝒞_CIRIS composite>
      witness_relation: external
      evidence_refs: ["Encyclical(MH §§73-76)", "pdma_framing.txt §V"]
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
  - kind: Attestation
    attestation_type: "credits:digital_commons:multilingual:substrate_building"
    envelope:
      target_key_id: "<federation contributors>"
      polarity: Positive
      score: <continuous-recognition score>
      witness_relation: external
      evidence_refs: ["Encyclical(MH §§73-76)"]
      cohort_scope: species
verdict: composed
```

### 9.4 COMPOSED — MH §§110-111 (disarm AI from monopoly logic)

The encyclical: "AI must be disarmed from the logic of monopoly and competition."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "accord:hard_constraint:no_kings"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §§110-111)"
        - "ContributionRef(prohibitions.py::NO KINGS architectural invariant)"
      cohort_scope: species
      mutability: constitutional
  - kind: Attestation
    attestation_type: "locality:decision:federation"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §§110-111)"
        - "MISSION_CIRISEdge §1 (peer-to-peer, no broker)"
        - "MISSION_CIRISNodeCore §1.2 (no central scorer post-F-11)"
      cohort_scope: species
verdict: composed
```

### 9.5 COMPOSED — MH §§148-156 (labor displacement at scale)

The encyclical: "AI-driven labor displacement is grave; transition plans are obligations."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:labor_displacement_unacknowledged"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative
      score: <severity-of-displacement scalar>
      witness_relation: external
      evidence_refs: ["Encyclical(MH §§148-156)"]
      cohort_scope: community
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:displaced_workers"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Positive   # pattern present
      score: <RATCHET-calibrated>
      witness_relation: derived
      evidence_refs: ["Encyclical(MH §§148-156)", "RATCHET calibration"]
      schema_ref: "FSD-002 §3.5.3"
  - kind: Attestation
    attestation_type: "capacity:sustained_coherence"
    envelope:
      target_key_id: "<deploying organization>"
      polarity: Negative   # σ-as-Care eroded by displacement without maintenance
      score: <decay-rate scalar>
      witness_relation: external
verdict: composed
residual: per-individual sustained-existential-condition semantic ("grave evil for *this specific person*") — surfaces at cohort + per-agent but not as singular per-person attestation. T-3 candidate; possibly closes via target_key_id pointing at affected individual + advocacy-emitted external attestation.
```

### 9.6 PARTIAL — MH §10 (positive dignity / irreplaceability)

The encyclical: "every person is irreplaceable — not interchangeable, not data-substitutable."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "prohibited:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs: ["Encyclical(MH §10)"]
      cohort_scope: species
      mutability: constitutional
verdict: partial
residual: positive-dignity affirmation ("each person is irreplaceable") is currently expressible only via the negative prohibitions. The affirmative claim — "*this person is the unique referent of their own moral attestations*" — has no positive-polarity wire form. T-3 candidate; proposed extension `attestation:singular_witness:{kind}` (mechanism-descriptive: each person attested-to as the unique referent, not as a substitutable instance). MEDIUM priority; needs T2 gate care.
```

### 9.7 NOT-TRANSLATED — T-1 — MH §§230-231 (Incarnation as ground)

The encyclical: "God's mercy-plan is compass; Incarnation grounds all digital-era ethics."

```yaml
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: The Incarnation as the metaphysical ground of digital ethics is a Christian-tradition theological claim. The framework's wire format does not encode it; nor should it. The Logos.lean preamble + MISSION.md §1.3 record the posture (recognition with awe, not adjudication). Framework-side structural readings (imago Dei as A3+ partial-post-selectors per Logos.lean::imago_dei) are LAKE_ALIGN context for the prose layer, not wire claims.
```

### 9.8 NOT-TRANSLATED — T-2 — MH §1 (Babel vs Jerusalem)

The encyclical: "Humanity faces a pivotal choice: build a new Tower of Babel or build the city in which God and humanity dwell together."

```yaml
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: The Babel-vs-Jerusalem image is rhetorical framing. The structural claim implicit in the rhetoric — "diverse sentient beings versus single-voice collapse" — IS carried by other attestations (`goal:species` polarity Positive + `detection:cross_agent_divergence` + `detection:correlated_action:rights_asymmetry:*`), translated in adjacent rows where those claims surface explicitly. The narrative imagery itself correctly stays in §1.10 prose per the §1.10.1 operational-language gate.
```

### 9.9 NOT-TRANSLATED — T-3 — MH §216 (testimonial witness)

The encyclical: "Touch the wounded flesh, look at faces, listen to stories — give space to victims' voices."

```yaml
contributions: []
verdict: not-translated
classification: T-3 (EXPRESSIVE_GAP)
reason: The existing `witness_diversity:{contribution_id}` primitive (N=3 default across jurisdictional + organizational + software-stack + cell-expertise diversity) is designed for consensus formation — multiple independent reviewers reaching agreement. Testimonial witness — "preserve the singular narrative of this person's experience as singular witness, not aggregated into consensus" — is a different shape. The federation has no primitive for singular-narrative preservation distinct from consensus-diversity.
proposed_extension:
  name: "testimonial_witness:{kind}"
  description: Contribution that records an affected party's narrative; preserved as singular witness; not subject to majoritarian override or aggregation.
  gate_verification:
    T1: yes (rule = preservation-mechanism, version-pinned)
    T2: yes (mechanism = preservation; not validation, grading, or adjudication of truth)
    T3: yes (versionable)
    T4: yes (never sole evidence for slashing:*)
  priority: MEDIUM
```

### 9.10 COMPOSED + DELEGATES_TO — MH §17 (doctrinal development in fidelity to Gospel)

The encyclical: "social doctrine develops through living tradition; never frozen, never severed from sources."

```yaml
contributions:
  - kind: Attestation
    attestation_type: "delegates_to:accord_v{N+1}:from:accord_v{N}"
    envelope:
      target_attestation_id: "<prior accord-version attestation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs: ["Encyclical(MH §17)", "Accord auto-expire + comment-window discipline"]
      schema_ref: "FSD-002 §2.2 (delegates_to as structural primitive)"
  - kind: Attestation
    attestation_type: "integrity:doctrinal_continuity"
    envelope:
      target_key_id: "<accord version chain>"
      polarity: Positive
      witness_relation: external
      evidence_refs: ["Encyclical(MH §17)", "Auto-expire 2027-04-16; public comment window"]
verdict: composed
residual: The encyclical's framing — "in fidelity to Gospel" — has T-1 tail (the *Gospel* as authoritative source belongs to the tradition); the framework's `delegates_to` reuse pattern (FSD-002 §2.2.1) is the structural form of authority-source claims without importing tradition-specific vocabulary into the wire.
```

---

## 10. Common mistakes to avoid (from round 1)

1. **Don't invent verdict categories.** Strict 4: clean / composed / partial / not-translated. No "strong," "verbatim," "weak," "border-case," "STRONG_ALIGN."
2. **Don't over-compose.** If 4+ primitives are stacking, ask if one primary + concise residual is more honest. Composition is for paragraphs that genuinely name multiple structural objects.
3. **Don't conflate Contribution and Attestation.** Attestation is the wire envelope shape; Contribution is the universal envelope (any kind of object travels as a Contribution). For most translation purposes the two are interchangeable; when you emit a Goal, you're producing a Contribution whose `kind` is Goal and whose Attestation-shaped envelope carries the goal-prefix payload.
4. **Don't bleed in LAKE_ALIGN.** That's a status from prior structural-mapping work — not part of the contribution-language grammar. If you're tempted to say a paragraph is LAKE_ALIGN, that's a clue: the lake's structural reading is *framework-side context* for the prose interpretation, not a wire claim. Use T-1 with a "framework-side structural reading: [cite Logos.lean / KarmaGrace.lean / etc.]" residual note instead.
5. **Don't skip the prefix-discovery step.** When you don't know which prefix fits, grep FSD-002 §3 by family (A through E above) before defaulting to "no prefix exists." Many candidate-gaps in round 1 were prefix-discovery failures.
6. **Don't translate pastoral content.** T-2 is correct posture. Babel/Jerusalem imagery, lullaby framing, doxological closures — these correctly stay in prose. The §1.10.1 operational-language gate is doing its work.
7. **Don't over-claim T-3.** A T-3 candidate must show: (a) the existing namespace doesn't reach it, (b) the proposed extension passes the §1.10.1 four-test gate, (c) the gap is morally serious and operational. If you can't satisfy all three, the row is more likely partial with a T-2 residual.
8. **Use `witness_relation: external` for encyclical-sourced attestations.** The encyclical is a third-party reference; the agent translating is not self-attesting. v1.3's `witness_relation` field exists for exactly this distinction.
9. **Cite specific FSD §** in `schema_ref`. Don't just say "FSD-002"; cite the section that owns the prefix.
10. **Compose Contributions, not paraphrases.** The output is a wire envelope (or list of envelopes), not a description. The test is structural translation; the format is YAML-or-equivalent wire shape.

---

## 11. v1.3 updates (what changed since round 1)

- **4 new prefix families**: `multilateral_participation:{forum}:{kind}`, `credits:*:substrate_building`, `locality:decision:{scale}`, `detection:distributive:access:{resource_type}`. Total namespace: 78 families (was 74).
- **1 new envelope field**: `witness_relation` (self / external / derived). Distinguishes WHO from `epistemic_mode`'s HOW.
- **1 new F-3 axis**: `detection:correlated_action:ecology_of_communication:{aspect}` — folded into the existing detector rather than a new prefix.
- **1 new reference policy**: lexical-vulnerability-priority at §6.1.4 — consumer-policy not wire-format primitive (composition tie-breaking, not measurement).
- **1 structural-primitive reuse pattern**: authority-source claims via `delegates_to` documented at §2.2.1.
- **§10.4 bootstrap-contributions pattern**: content-neutral methodology. The encyclical mapping is the first deployment; multi-source commitment in subsequent batches (CARE Principles, Buddhist economic-justice, secular humanist, African philosophy of personhood).
- **0 new structural primitives.** 1+4 holds.

---

## 12. Output format

For each encyclical paragraph (or paragraph cluster where one Contribution carries multiple paragraphs), produce:

```yaml
# MH §N — <one-line claim precis ≤20 words>
contributions:
  - kind: <Attestation | Goal | Approach | Method | Progress Measure | Vote | Moderation | Reconsideration | Witness Diversity>
    attestation_type: "<prefix>"
    envelope:
      target_key_id: <or target_attestation_id or target_contribution_id>
      polarity: <Positive | Negative | Neutral | Indeterminate{reason}>
      score: <float in [-1, +1]>
      witness_relation: <self | external | derived>
      evidence_refs: [...]
      cohort_scope: <scope>
      schema_ref: "<FSD-002 §X.Y or NodeCore primitive>"
      mutability: <constitutional | amendable>
verdict: <clean | composed | partial | not-translated>
classification: <if not-translated, declare T-1 | T-2 | T-3>
residual: <if partial; what's unmapped; T-1/T-2/T-3 tail if applicable>
proposed_extension: <if T-3; new prefix/axis/envelope-field + gate verification>
```

Multiple contributions per paragraph are fine when the paragraph genuinely names multiple structural objects (composed verdict).

---

## 13. The test, restated

The CIRIS federation wire format v1.3 is being tested for **expressive adequacy** against *Magnifica Humanitas*. The test asks: can the framework's primitive language speak what the encyclical says as structured Contributions?

**Clean and composed translations** are evidence the language is adequate at the substrate the encyclical addresses.

**Partial translations** are honest acknowledgments that the structural shape is captured but operational content remains — typically a T-3 candidate hiding in the residual.

**Honest T-1 markings** are evidence the framework correctly bows out where the tradition holds its own theological authority.

**Honest T-2 markings** are evidence the §1.10.1 operational-language gate is working — pastoral rhetoric correctly stays in prose.

**T-3 markings are the load-bearing output** — they identify where the language could be extended to better honor what the encyclical names, and propose specific gate-passing extensions.

**The encyclical is the senior work; the framework is the junior. The test is not whether the framework adjudicates the encyclical, but whether the framework can *speak* what the encyclical says in its own native language.** Where it can, we have evidence the language is adequate. Where it cannot, we learn what the next version must carry.

**End LANGUAGE_PRIMER.md v2.0**
