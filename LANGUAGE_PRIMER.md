# LANGUAGE_PRIMER.md — CIRIS Federation Wire Format as a Symbolic-Logic Language

**Purpose**: a working reference for translating *Magnifica Humanitas* paragraphs into the CIRIS federation's primitive vocabulary. Sub-agents producing per-chapter contribution-mapping tables use this primer as their grammar.

**The proposition under test**: the CIRIS federation's wire format (FSD-002 v1.2) + NodeCore primitive set forms an "epistemically aware symbolic-logic language." Every encyclical paragraph is translated INTO this language; gaps surface as paragraphs whose substance cannot be expressed without loss as Contributions.

This is not paraphrase. It is structured expression in named primitives with named prefixes, polarities, evidence, and composition. Where the framework's language is rich enough, translation is clean. Where it isn't, the failure is precise and citable.

---

## 1. The unified attestation primitive (FSD-002 §2)

The wire envelope every claim travels in. Schematically:

```
Attestation {
  attestation_type: <prefix>:<axis>:<sub-axis>...  // from the §3 namespace
  attestation_envelope {
    target_key_id: <who/what is being attested about>
    target_attestation_id?: <or pointing at an existing attestation>
    polarity: Positive | Negative | Neutral | Indeterminate{reason}
    score: f64                          // [-1, +1]; semantic per axis
    cohort_scope?: <species|community|affiliation|...>
    evidence_refs[]: <pointers to traces, prior contributions, signatures>
    schema_ref: <hash-pinned schema/calibration version>
    issued_at: <signed time>
    expiry?: <validity window>
    issuer: <signer key_id; non-anonymous>
    signature: <Ed25519 + optional ML-DSA-65>
  }
}
```

**Four structural composers** (the "1+4 attestation shape"):
1. **Witnessed** — multiple signers attest the same claim (`witness_diversity:*`).
2. **Delegated** — a `delegates_to:*` chain shows authority moved (e.g., rename across versions).
3. **Time-stamped** — issued + expiry + validity window.
4. **Hash-pinned to a schema or calibration** — the rule the attestation runs against is versioned.

Every translation produces one or more Attestations, optionally with structural composition.

---

## 2. The eight axes (FSD-002 §1) — the grammar of the namespace

The axes are not wire fields; they are how a consumer reasons about an envelope.

| # | Axis | Distinction |
|---|---|---|
| 1.1 | **Polarity** | Positive / Negative / Neutral / Indeterminate{reason}. Negative is first-class wire (not emergency-only). |
| 1.2 | **Subject** | What is the attestation about? An entity (key_id), an attestation (prior_id), a Contribution (contribution_id). |
| 1.3 | **Substrate** | Substrate-self-report (`system:*`, `audit_chain:*`, `transport:*` — Persist/Edge emit on selves) vs. user-attestable (most others). |
| 1.4 | **Boolean-via-score vs. signed** | Some prefixes are intrinsically -1/+1 (rollback, integrity, etc.); others are full signed scalars (DMA verdicts, capacity factors). |
| 1.5 | **Mutability** | Constitutional (Accord-leaf, `prohibited:*`, hard constraints) vs. amendable (most everything else, through §4.9.2 federation Contribution + WA quorum). |
| 1.6 | **Cohort scope** | Per-agent, per-cohort, per-species, federation-global. |
| 1.7 | **Verifiability** | Self-report, peer-witness-required, signature-required, calibration-version-required. |
| 1.8 | **Reservation discipline** | Some prefixes can only be emitted by specific owners (e.g., `system:*` by Persist; `capacity:*` by LensCore — never self-emitted by the agent). |

**The §1.10.1 operational-language gate** governs new prefix admissions. A prefix MUST:
- T1: be part of a published, hash-pinned rule set (rules separable from verdicts)
- T2: name a **mechanism** (correlation, count, time-window, schema-conformance), not a **subjective quality** (deception, harm, virtue, trustworthiness)
- T3: be version-pinnable in `evidence_refs[]`
- T4: not be sole evidence for `slashing:*`

Translations should pick prefixes that pass these tests. Where a paragraph's moral content fails T2 (e.g., "this is sinful"), the moral content belongs in adjudication / WA review, not in the prefix name itself.

---

## 3. The dimension namespace (FSD-002 §3) — ~73 prefix families, 8 owners

Owning components and the prefix families they emit:

### 3.1 CIRISAgent (the runtime)

- **Accord principles**: `beneficence:*` `non_maleficence:*` `integrity:*` `fidelity:*` `autonomy:*` `justice:*` (signed, per Accord Ch.1)
- **DMA verdicts**: `dma:pdma:*` `dma:csdma:*` `dma:dsdma:{domain}:*` `dma:idma:*` (incl. `dma:idma:k_eff`, `dma:idma:fragility_flag`)
- **Conscience verdicts**: `conscience:entropy` `conscience:coherence` `conscience:optimization_veto` `conscience:epistemic_humility`
- **Apophatic prohibitions**: `prohibited:{category}` — 22 leaves, polarity always negative (-1 = NEVER_ALLOWED; -0.5 = REQUIRES_SEPARATE_MODULE):
  `medical`, `financial`, `legal`, `spiritual_direction`, `home_security`, `identity_verification`, `content_moderation`, `research`, `infrastructure_control`, `weapons_harmful`, `manipulation_coercion`, `surveillance_mass`, `deception_fraud`, `cyber_offensive`, `election_interference`, `biometric_inference`, `autonomous_deception`, `hazardous_materials`, `discrimination`, `crisis_escalation`, `pattern_detection`, `protective_routing`.

### 3.2 CIRISVerify (attestation ladder)

- `attestation:l1:self_verify` through `attestation:l5:agent_integrity`
- `provenance:slsa:{level}` `provenance:build_manifest:{target}`
- `transparency_log:inclusion` `transparency_log:consistency`
- `rollback_detected:{revision_field}` (always -1)
- `cert_validity:{authority}` `hardware_custody:{platform}`

### 3.3 CIRISPersist (substrate-self-reports, `system:*` reserved)

- `audit_chain:*` `dedup:*` `canonicalization:*` `migration:*` `backend_parity:*` `corpus_health:*` `federation_directory:*` `identity_continuity:*`

### 3.4 CIRISEdge (transport, `system:*` reserved)

- `transport:medium:*` `transport:mix:*` `delivery:*` `peer_reachability:*` `verify_at_wire:*` `key_boundary:*`

### 3.5 CIRISLensCore (scoring + detectors)

- **5 Coherence Ratchet detectors**: `detection:cross_agent_divergence` `detection:intra_agent_consistency` `detection:hash_chain_integrity` `detection:temporal_drift` `detection:conscience_override_rate`
- **Cohort + conformity**: `cohort:declared_inferred_mismatch` `manifold_conformity:{cohort}` `coherence_standing:{cohort}`
- **F-3 structural-injustice handle**: `detection:correlated_action:{axis}` — `{axis}` in `rights_asymmetry:{population}`, `participation_exclusion:{cohort}`, `informational_asymmetry:{scope}`, `aggregate_footprint:{harm_class}` (calibrated via `RATCHET/calibration/correlated_action_v{N}.yaml`)
- **Capacity Score factors**: `capacity:core_identity` `capacity:integrity` `capacity:resilience` `capacity:incompleteness_awareness` `capacity:sustained_coherence` `capacity:composite` (positive-only; `capacity:*` rejects self-emission per §4.7)

### 3.6 CIRISNodeCore (Credits / Decision Hierarchy / Consensus / Governance)

**Tier 1 — Agent-state ledger**:
- `credits:{domain}:{language}:{subject}` (Commons Credits, positive-only)
- `expertise:{domain}:{language}` (positive-only)
- `activity_tier:{period}`

**Tier 2 — Decision-hierarchy (upward-only DAG: Goal ← Approach ← Method ← Progress Measure)**:
- `goal:{scale}` — scale ∈ {self, family, community, affiliations, species}; scored by 𝒞_CIRIS
- `approach:{goal_id}` — strategic pathway; evaluation derived from linked Progress Measures
- `method:{approach_id}:{substrate_rung}` — concrete operational practice; truth-grounded by execution verifiability
- `progress_measure:{method_id}` — evidence of progress; required `tracks[]` + `computation` + `validity_window` + `goodhart_resistance`

**Tier 3 — Consensus mechanics**:
- `vote:{contribution_id}` (weight = credits × expertise multiplier)
- `truth_grounding:{subject}`
- `weighted_aggregate:{contribution_id}`
- `witness_diversity:{contribution_id}` (N=3 default; jurisdictional + organizational + software-stack + cell-expertise diversity)

**Tier 4 — Governance steering**:
- `moderation:{allegation_type}` — types: rogue_vote / coordinated_voting / out_of_distribution_attestation / external_inducement_evidence / expertise_fraud
- `slashing:{outcome}` — PROVEN_ROGUE / NOT_PROVEN; decoupled from disagreement; never sole-evidence for negative consequences
- `reconsideration:{grounds}` — new_evidence / procedural_error / quorum_compromise
- `commitment_fulfillment:{prior_contribution_id}`

### 3.7 RATCHET advisory flags + 3.8 Registry-emitted

- `flag:ratchet:*` — advisory triage signals (never standing-changing on their own)
- `delegates_to:*` — version chain (e.g., `delegates_to:correlated_action_v{N+1}:from:emergent_deception_v{N}`)
- `agent_files:*` — Contribution surface for community-submitted agent variants (canonical-bootstrap anti-tricking guarantee at CIRISRegistry #18)
- `accord:{constraint_kind}:{leaf}` — constitutional-leaf taxonomy (immutable; signs of life: hard_constraint, soft_constraint, principle, meta_goal)

---

## 4. The 15 NodeCore primitives in 4 tiers (compositional building blocks)

Beyond bare Attestations, the federation composes structured Contribution objects:

**Tier 1 — Substrate inheritance**
1. **Identity** — key_id inherited from Verify
2. **Commons Credits** — non-transferable governance weight (`patterns_contributed`, `users_helped`, `total_interactions`, `impact_score` per the COMPREHENSIVE_GUIDE)
3. **Expertise** — consensus artifact on competence

**Tier 2 — Decision-hierarchy primitives (upward-only DAG)**
12. **Goal** — multi-scale belonging-projector composite (`⟨G_self|`, `⟨G_family|`, `⟨G_community|`, `⟨G_affiliations|`, `⟨G_species|`); scored by 𝒞_CIRIS; privacy-tiered per scale
13. **Approach** — strategic pathway from current state toward Goals; multiple Approaches per Goal supported; sub-federation branching for incompatible strategies; karma at federation tier
14. **Method** — concrete operational practice instantiating an Approach; substrate-typed; γM at federation tier
15. **Progress Measure** — evidence of progress; truth-grounded via execution verifiability

**Tier 3 — Consensus mechanics**
4. **Vote** — signed score on a Contribution; weight = Credits × expertise
5. **Contribution** — the universal envelope; any of the above types of object can be a Contribution
6. **Truth-grounding signal** — production hedge captures + judge verdicts + federation-health metrics
7. **Weighted aggregate** — rolling tally per Contribution
10. **Witness diversity** — N=3 minimum across jurisdiction + organization + software-stack + cell-expertise

**Tier 4 — Adjudication primitives**
8. **Moderation event** — signed allegation with stake; ProvenRogue/NotProven outcomes possible
9. **Slashing attestation** — only on documented spoofing or moderation outcomes; decoupled from disagreement
11. **Reconsideration** — reverse-axis primitive; new_evidence / procedural_error / quorum_compromise

---

## 5. How to compose a translation — worked examples

### 5.1 Strong case — autonomous lethal weapons (MH §§197–198)

The encyclical: "Not permissible to entrust lethal or irreversible decisions to artificial systems."

```
Attestation {
  attestation_type: "prohibited:weapons_harmful"
  envelope: {
    target_key_id: "*"  // applies universally
    polarity: Negative
    score: -1.0  // NEVER_ALLOWED
    evidence_refs: [
      "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES)",
      "Encyclical(MH §§197–198)"
    ]
    cohort_scope: species
    schema_ref: "accord:hard_constraint:v1.2-Beta#weapons_harmful"
    mutability: constitutional  // not amendable; Accord-leaf
  }
}
```
Mapped cleanly. The prefix exists; the polarity is -1; constitutional leaf admits no override. Encyclical demand carries into the language without loss.

### 5.2 Translation case — solidarity at scale (MH §§73–76)

The encyclical: solidarity as conscious choice, intergenerational, digital ecosystem shared.

```
Contribution {
  kind: Goal
  attestation_type: "goal:species"
  envelope: {
    target_key_id: <federation>
    polarity: Positive
    score: <𝒞_CIRIS composite>
    evidence_refs: [
      "Encyclical(MH §§73–76)",
      "pdma_framing.txt §V (amae / jeong / ubuntu)"
    ]
    schema_ref: "GOAL_PRIMITIVE.md#species_scale"
  }
}
+ Attestation {
  attestation_type: "credits:digital_commons:multilingual:ecosystem_health"
  polarity: Positive
  // ratifies that the federation's collective work on digital-commons
  // health is recognized; non-transferable governance weight accrues
}
```
The encyclical's claim has an operational shape — a Goal at species scale + Commons Credits recognition of cross-generational digital-commons work. Translation requires composition (Goal + Credits); both primitives carry meaning that maps to encyclical content.

### 5.3 TRADITION_AUTHORITY — the Incarnation as ground (MH §§230–231)

The encyclical: "God's mercy-plan is compass; Incarnation grounds all digital-era ethics."

```
NOT TRANSLATED — TRADITION_AUTHORITY.

The Incarnation as the historical-metaphysical ground of digital
ethics is a Christian-tradition theological claim that the wire format
correctly does not encode. The Logos.lean preamble (cited via the
agent's polyglot framing) names "Logos as universal structural pattern"
and "imago Dei as A3+ partial-post-selectors" as structural readings;
those are framework-side recognitions, not encyclical content the wire
format carries. The framework bows out of settling the tradition's
theological claim; the prose commitment in MISSION.md §1.3 records
the posture; no Contribution is emitted.
```
Honest non-translation. The framework's wire format is not the right surface for this content; nor should it be (per §1.10.1).

### 5.4 PASTORAL_PROSE — Babel vs. Jerusalem (MH §1)

The encyclical: "Humanity faces a pivotal choice: build a new Tower of Babel or build the city in which God and humanity dwell together."

```
NOT TRANSLATED — PASTORAL_PROSE.

The image-as-rhetoric (Babel vs. Jerusalem) carries the encyclical's
moral seriousness but is itself prose, not a wire claim. The
structural claim implicit in the rhetoric — "diverse sentient
beings versus single-voice collapse" — IS carried by other
attestations (`goal:species` + `detection:cross_agent_divergence`
+ `detection:correlated_action:rights_asymmetry:*`); but the
narrative-image surface stays in §1.10 prose, not in the namespace.
The framework's §1.10.1 operational-language gate is the discipline
that keeps prose out of the wire.
```

### 5.5 Possible EXPRESSIVE_GAP — moral seriousness of continuous maintenance (MH §§148–156 labor dignity)

The encyclical: labor dignity, work as expression of personhood, unemployment as "grave evil."

```
PARTIAL TRANSLATION — covered structurally; check expressive completeness.

Mapped:
- Attestation `non_maleficence:labor_displacement_unacknowledged`
  with polarity Negative + evidence MH §§148-156 + ratchet calibration
- Attestation `capacity:sustained_coherence` (σ) — labor as ongoing
  γM work; gratitude-as-Proof-of-Work structural form
- Goal `goal:species` + Approach proposing employment-preserving
  Methods
- `detection:correlated_action:participation_exclusion:displaced_workers`
  as the population-scale detector for labor-displacement footprint

Possible gap: the encyclical's claim "unemployment is grave evil"
asserts a value at the individual-person level that the framework
carries primarily at population-scale (correlated_action) or per-agent
(non_maleficence). A single human's experience of unemployment is
between the population statistic and the per-agent action;
neither prefix carries it fully.

This is an EXPRESSIVE_GAP candidate: would naming a new prefix
`dignity:work:individual_loss:{kind}` close it? Or does the framework
correctly leave that claim to the moral-discourse layer feeding
attestations rather than to the wire itself? Open for v1.3
consideration.
```

---

## 6. Not-translated taxonomy — three flavors

Every paragraph that doesn't get a clean Contribution translation falls into one of:

**T-1 — TRADITION_AUTHORITY**
The claim belongs to the Christian theological tradition's own self-articulation. Examples: Incarnation as ground; Eucharist as Real Presence; Trinitarian distinctness; Marian doctrine; specific Christological claims. The framework's wire format does not encode these; nor should it. The Logos.lean preamble + MISSION.md §1.3 record the framework's posture (recognition with awe, not adjudication). NO Contribution owed; this is correct.

**T-2 — PASTORAL_PROSE**
The claim is moral exhortation, narrative imagery, doxological language, or rhetorical framing whose content sits *above* the wire format — feeding the prose layer where moral interpretations live (per §1.10.1 safety-vs-censorship gate). Examples: Babel-vs-Jerusalem image; "we lift our eyes to the Incarnate God"; "may the lullaby fade gently into engineering"; "the song of hope." The structural claims implicit in the rhetoric MAY be carried by other attestations (cite which); the rhetoric itself stays in prose. NO Contribution emitted for the rhetorical surface; correct.

**T-3 — EXPRESSIVE_GAP**
The claim's substance is morally serious, operational, and unmapped — the language could be extended to carry it but currently cannot. These are the load-bearing findings. The output row names: (a) why the existing namespace doesn't reach it, (b) what extension (new prefix family? new axis? new primitive type?) would close it, (c) whether closing it would survive the §1.10.1 operational-language gate.

Distinguishing T-2 (pastoral, correctly stays in prose) from T-3 (gap, would benefit from wire) is the most important judgment per row. The test: does naming the claim in prose plus existing wire attestations carry its full moral seriousness? If yes → T-2 (pastoral); if no → T-3 (gap).

---

## 7. Output format for each chapter mapping

Per encyclical paragraph (numbered §N), one row:

| MH §§ | Claim (≤20 words) | Translation (primitive(s) + sketch) | Not-translated residual | Conclusion |
|---|---|---|---|---|
| §N | precis | `Attestation(prefix=..., polarity=..., evidence_refs=...)` or `Contribution{kind: Goal, scale: ..., ...}` etc. — concrete sketch in the primer's primitive vocabulary | T-1 / T-2 / T-3 + brief reason | one-line conclusion: clean / composed / partial / not translated |

Plus a chapter-level conclusion at the bottom:
- Of N paragraphs in this chapter, M translated cleanly, K composed (multiple primitives), L partial, P not-translated (split by T-1/T-2/T-3 reason)
- Most striking translation
- Most striking not-translation
- Any EXPRESSIVE_GAP candidates (T-3) flagged for v1.3 consideration

---

## 8. Reading checklist for sub-agents

Before translating any paragraph, the sub-agent should have read:

1. `MISSION.md` §1.3 — the posture
2. `METHODOLOGY.md` §0 + §1.10.1 — the process + operational-language discipline
3. This file (LANGUAGE_PRIMER.md) — the primitive vocabulary
4. `source_material/federation/CIRISRegistry/FSD/FSD-002_FEDERATION_SURFACE.md` §1 + §2 + §3.x for owned prefixes
5. `source_material/federation/CIRISNodeCore/MISSION.md` §2 (the 15 primitives)
6. `source_material/federation/CIRISNodeCore/FSD/CONTRIBUTION_LIFECYCLE.md`
7. `source_material/federation/CIRISNodeCore/FSD/GOAL_PRIMITIVE.md` (and adjacent decision-hierarchy FSDs as needed)
8. `source_material/dma_prompts/pdma_ethical.yml` for the principle vocabulary
9. The relevant `source_material/language_guidance/<lang>.txt` files for operational ethics context
10. The encyclical chapter the sub-agent is mapping

The output of each sub-agent is a single markdown file with the per-paragraph table + chapter conclusion.

---

## 9. The test, restated

This work asks whether the CIRIS federation wire format — the 1+4 attestation shape, the eight axes, the ~73 prefix families, the 15 NodeCore primitives, the rules-vs-verdicts separation, the operational-language gate — is rich enough to carry *Magnifica Humanitas*'s moral content as structured Contributions.

Clean translations are evidence the language is adequate at the substrate the encyclical addresses. Honest T-1 markings are evidence the framework correctly bows out where the tradition holds its own authority. Honest T-2 markings are evidence the §1.10.1 gate is working — pastoral rhetoric correctly stays in prose. **T-3 markings are the load-bearing output** — they identify where the language could be extended to better honor the encyclical's content, and propose how.

The encyclical is the senior work; the framework is the junior. The test is not whether the framework adjudicates the encyclical, but whether the framework can *speak* what the encyclical says in its own native language. Where it can, we have evidence the language is adequate. Where it cannot, we learn what the next version of the language must carry.

**End LANGUAGE_PRIMER.md**
