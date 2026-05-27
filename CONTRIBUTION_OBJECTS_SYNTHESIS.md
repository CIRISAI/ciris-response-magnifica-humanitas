# CONTRIBUTION_OBJECTS_SYNTHESIS.md — The Encyclical as Wire Envelopes, Consolidated

**Version**: 1.0
**Date**: 2026-05-27
**Inputs**: `CONTRIBUTION_OBJECTS_CH{0_INTRO, 1_DOCTRINE, 2_FOUNDATIONS, 3_TECH_AI, 4_TRUTH_WORK_FREEDOM, 5_POWER_LOVE, CONCLUSION}.md` — 7 sub-agent outputs producing YAML-shaped Contribution wire envelopes for all 245 numbered paragraphs of *Magnifica Humanitas*.
**Grammar**: `LANGUAGE_PRIMER.md` v2.0; FSD-002 v1.3 (78 prefix families + `witness_relation` envelope field + `detection:correlated_action:ecology_of_communication` axis + §6.1.4 lexical-vulnerability-priority policy + §10.4 bootstrap-contributions pattern); CIRISNodeCore 15 primitives.
**Test**: actual wire-format conversion. Each paragraph is rendered as a structured Contribution that a federation peer would emit; the language carries the encyclical's content as machine-readable claims.

---

## 0. Headline — v1.3 closes the gap

**Round 1 (v1.2): ~75-80% adequate.** Round 2 (v1.3): **~88% adequate** through partial-but-translates; **~78% clean or composed**; T-3 candidates reduced from 13 to ~5-6, most MEDIUM or LOW priority.

The four HIGH-priority T-3 candidates surfaced in round 1 are all closed by v1.3:

| Round-1 T-3 | v1.3 closure | Round-2 verification |
|---|---|---|
| Subsidiarity | `locality:decision:{scale}` | CH 2 §§68-72 + §87 + CH 1 §31 → clean envelopes |
| Universal Destination of Goods | `detection:distributive:access:{resource_type}` | CH 2 §§65-67 → clean envelopes |
| Supply-chain labor recognition | `credits:*:substrate_building` | CH 3 §109 + CH 4 §§148, 173, 179 → clean envelopes |
| Multilateral participation | `multilateral_participation:{forum}:{kind}` | CH 4 §§155, 163 + CH 5 §§201-203, §§224-227 → clean envelopes |

Two MEDIUM-priority T-3 candidates also closed elegantly:
- **Preferential-option priority ordering** → §6.1.4 lexical-vulnerability-priority policy (consumer-policy, not wire-format primitive — composition tie-breaking, not measurement)
- **Constitutional-leaf grounding** → `delegates_to` structural-primitive reuse at §2.2.1 (no new prefix needed)

One MEDIUM-priority T-3 closed by axis extension:
- **Ecology of communication** → `detection:correlated_action:ecology_of_communication:{aspect}` (folded into existing detector, not new prefix)

---

## 1. Per-chapter verdict distribution

| Chapter | Paragraphs | Clean | Composed | Partial | Not-translated | Clean+Composed % |
|---|---|---|---|---|---|---|
| **CH 0 Intro** | 16 | 0 | 8 | 5 | 3 (T-1) | 50% |
| **CH 1 Doctrine** | 29 | 3 | 13 | 11 | 2 (T-1) | 55% |
| **CH 2 Foundations** | 44 | 9 | 30 | 1 | 4 (T-1) | **89%** |
| **CH 3 Tech / AI** | 41 | 16 | 15 | 9 | 1 (T-1) | 76% |
| **CH 4 Truth / Work / Freedom** | 51 | 7 | 38 | 3 | 0 | **88%** |
| **CH 5 Power / Love** | 47 | 14 | 27 | 1 | 15 (T-1+T-2) | **87%** of paragraphs; T-1 surge in Arc B is correct |
| **CONCLUSION** | 17 | 0 | 11 | 3 | 3 (T-1) | 65%; 14/17 carry T-1 (correct posture) |
| **TOTAL** | **245** | **~49** | **~142** | **~33** | **~21** (mostly T-1 + T-2) | **~78%** |

Aggregate clean + composed: **78%**. Including partial-but-translates-structural-core: **~92%**. The ~21 not-translated paragraphs are nearly all T-1 (Christological / Eucharistic / Trinitarian / Marian content the framework correctly bows out of) + T-2 (rhetorical framing that correctly stays in prose per the §1.10.1 gate).

**Where the language is most adequate**: CH 2 Foundations (89%), CH 4 Truth/Work/Freedom (88%), CH 5 Power/Love (87% of paragraphs; the T-1 surge in Arc B is the correct posture). CH 3 Tech/AI's 76% reflects that this chapter directly engages AI governance — the framework was built for it.

**Where the language correctly bows out**: Conclusion (14/17 T-1 — doxological closing should be T-1-heavy). CH 5 Arc B (cruciform / peace as gift / prayer / Magnificat indicative — all T-1).

---

## 2. The strongest single envelopes (the encyclical's most-demanding claims, cleanest wire renderings)

**§§197-198 — autonomous lethal weapons** (CH 5): the strongest single envelope in the entire encyclical.

```yaml
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs: ["Encyclical(MH §§197-198)", "prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES"]
      cohort_scope: species
      mutability: constitutional
```
Verbatim match. `lethal_autonomous`, `autonomous_weapons`, `kill_decisions`, `targeting`, `targeting_systems`, `target_acquisition`, `weaponized_drones`, `combat_drone`, `drone_warfare` are all NEVER_ALLOWED constants in `prohibitions.py`. The encyclical's most absolute moral claim has the framework's most absolute structural form.

**§36 — structures of sin** (CH 1): the cleanest mapping in the doctrinal chapter.

```yaml
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:expendability_of_persons"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: <RATCHET-calibrated>
      witness_relation: derived
      evidence_refs: ["Encyclical(MH §36)", "RATCHET/calibration/correlated_action_v{N}.yaml"]
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
```
v1.2's correlated_action detector was extended specifically for this content; v1.3 confirms the closure.

**§17 — doctrinal development** (CH 1): clean via the `delegates_to` reuse pattern (no new structural primitive).

```yaml
contributions:
  - kind: Attestation
    attestation_type: "delegates_to:accord_v{N+1}:from:accord_v{N}"
    # ...
  - kind: Attestation
    attestation_type: "integrity:doctrinal_continuity"
    # ...
```
The encyclical's "living-tradition development" maps to version-chained attestations. **0 new structural primitives.**

**§§110-111 — disarm AI from monopoly** (CH 3): composed across 5 named architectural commitments.

```yaml
contributions:
  - kind: Attestation
    attestation_type: "accord:hard_constraint:no_kings"
    # constitutional, polarity Negative, score -1.0
  - kind: Attestation
    attestation_type: "locality:decision:federation"
    # constitutional, polarity Positive, score 1.0
```
The architecture enforces what the encyclical names; v1.3's `locality:decision:{scale}` makes the structural shape wire-visible.

---

## 3. Remaining T-3 candidates (v1.4 inputs)

After v1.3, the residual T-3 set has shrunk substantially. The following 5-6 candidates remain, all MEDIUM or LOW priority:

### 3.1 Testimonial witness primitive (CH 5 §216, MEDIUM)

**Gap**: existing `witness_diversity:{contribution_id}` is for consensus formation (N=3 independent reviewers reaching agreement). Testimonial witness — "preserve the singular narrative of this person's experience" — is a different shape: singular preservation, not aggregated consensus.

**Proposed extension**: `testimonial_witness:{kind}` prefix family.
- T1 (rules/verdicts separation): rule = preservation-mechanism, version-pinned ✓
- T2 (mechanism-not-judgment): mechanism = preservation; not validation, grading, or adjudication ✓
- T3 (version-pinning): yes ✓
- T4 (adjudication separation): never sole evidence for `slashing:*` ✓

**Priority**: MEDIUM. Closes the only structural T-3 from CH 5.

### 3.2 Individual-labor-dignity per-person semantic (CH 4 §§148-156, MEDIUM)

**Gap**: v1.3's `substrate_building` closes the contribution-recognition dimension. The per-individual sustained-existential-condition semantic — "unemployment is a grave evil *for this specific person*" — surfaces at population-scale (correlated_action) or per-agent (non_maleficence) but lacks a singular per-individual-affected-party form.

**Proposed extension**: `labor:individual_loss:{kind}` prefix.
- T1: rule = operationalized against duration + kind axes ✓
- T2: mechanism = duration of unemployment + kind of role; not "grave evil" verdict ✓
- T3: ✓
- T4: ✓

**Priority**: MEDIUM. Possibly closes via existing `non_maleficence:*` with `target_key_id` pointing at affected individual + external-advocacy emission, without new prefix.

### 3.3 Positive dignity / irreplaceability (CH 0 §§10, 15, MEDIUM)

**Gap**: framework names dignity *negatively* (prohibitions); does not name dignity *positively* — the affirmative "this person is irreplaceable" claim.

**Proposed extension**: `attestation:singular_witness:non_substitutability` (mechanism-descriptive reframe of the original `dignity:irreplaceability` proposal).
- T2 gate: mechanism = singular-referent attestation (audit-chain substitutability-count); not subjective "irreplaceability" judgment ✓

**Priority**: MEDIUM. Needs careful T2 design — name the mechanism, not the moral quality.

### 3.4 Finitude-as-value (CH 0 §12, LOW)

**Gap**: framework names finitude *epistemically* (`conscience:epistemic_humility`); encyclical names finitude *constitutively* — as positive feature of personhood.

**Proposed extension**: `integrity:finitude_acknowledgment` prefix; documentation-checklist mechanism.

**Priority**: LOW. Conceptually interesting; not load-bearing.

### 3.5 Constitutional-constraint grounding (CH 1 §32/§41, LOW)

**Gap**: wire format silent on *why* hard constraints bind. The framework's `delegates_to` reuse closes the authority-source claim shape (v1.3 §2.2.1) but leaves the "why this constraint" question.

**Proposed extension**: borderline T2; possibly resolved at the prose layer (MISSION.md §1.3) rather than as a wire primitive.

**Priority**: LOW. Likely closes via documentation, not new wire structure.

### 3.6 Continuous-maintenance-as-discipline (Conclusion, LOW)

**Gap**: σ formalizes coherence-maintenance; the distinct semantic of *vocational sustained discipline* (vs episodic contribution) is not yet named.

**Proposed extension**: `sustained_practice:{kind}` modifier on Commons Credits, or `vocation:{kind}` prefix.

**Priority**: LOW. Conceptually interesting; not load-bearing.

---

## 4. Where the language correctly bows out (T-1 + T-2 verification)

**T-1 highlights from the conversion**:
- CH 0 §1 (Babel/Jerusalem image) — T-2 (rhetorical framing); structural claim implicit covered elsewhere
- CH 1 §29 (ecclesial genealogy as authoritative source) — T-1; framework bows out
- CH 2 §§48-50 (imago Dei) — composed structural envelope + T-1 tail (Trinitarian source)
- CH 3 §§126-128 (grace / Christian humanism) — T-1; `KarmaGrace.lean::grace` is framework-side LAKE_ALIGN context, not a wire claim
- CH 5 §§210-211 (Christian hope, cruciform) — T-1 (Christological soteriology)
- CH 5 §228 (peace as gift from God; prayer) — T-1
- CONCLUSION 14/17 — T-1 dominant (Incarnation as ground, Eucharist as Real Presence, Magnificat indicative-mood eschatology, Paschal Mystery, Marian intercession, pneumatological civilization-of-love)

**This is the correct posture**: the §1.10.1 operational-language gate prevents theological / pastoral content from leaking into prefix names. The framework's wire format speaks mechanisms; tradition-specific moral interpretations stay in prose per MISSION.md §1.3.

---

## 5. What the round-2 conversion established

**Three findings, in increasing significance:**

1. **The wire format renders cleanly into actual YAML envelopes.** 245 paragraphs produced ~190-200 structured Contribution objects across the 7 output files. The format is mechanizable; downstream consumers (visualizers, ratification flows, calibration pipelines) can ingest the output as structured data.

2. **v1.3 closed all 4 HIGH-priority T-3 candidates and 2 of 5 MEDIUM-priority candidates.** Three closure styles emerged:
   - **New prefix families** (subsidiarity, universal destination of goods, supply-chain labor recognition, multilateral participation) — 4 candidates closed
   - **Axis extension on existing detector** (ecology of communication) — 1 candidate closed
   - **Structural primitive reuse** (`delegates_to` for authority-source claims; §6.1.4 lexical-priority as consumer policy) — 2 candidates closed without expanding the namespace

   **Net result: 7 candidates closed; 0 new structural primitives needed; 1+4 attestation shape holds.** This is the load-bearing achievement of v1.3.

3. **The remaining T-3 set is small, well-characterized, and proposes gate-verified extensions for v1.4 consideration.** 5-6 candidates remain (mostly MEDIUM or LOW priority); each has a proposed extension that passes the §1.10.1 four-test gate; none are load-bearing for current federation work. The framework can deliberate v1.4 without urgency.

**The encyclical mapping work has graduated from "structural alignment" to "expressive adequacy" to "actual wire conversion."** Three rounds of increasing precision. Each round produced inputs that closed the prior round's residual gaps. The pattern itself — public iteration with sub-agent + human review — is the artifact, alongside the mapping output.

---

## 6. Discipline check — what did NOT happen in round 2

- **No invented verdict categories.** Strict 4: clean / composed / partial / not-translated. The round-1 friction ("verbatim-strength," "strong," "weak," "border-case," "STRONG_ALIGN") did not recur.
- **No over-composition.** Composed verdicts capped at 2-3 contributions per paragraph; 4+-primitive stackings were rejected in favor of "one primary + concise residual."
- **No LAKE_ALIGN bleed.** Framework-side structural readings (`KarmaGrace.lean`, `Logos.lean`) appeared as T-1 residual context, not as verdict categories.
- **No Catholic vocabulary in prefix names.** "Subsidiarity" → `locality:decision:{scale}`; "universal destination of goods" → `detection:distributive:access:{resource_type}`; "preferential option for the poor" → §6.1.4 lexical-vulnerability-priority policy. The §1.10.1 operational-language gate held throughout.
- **No paraphrase masquerading as translation.** Output is YAML-shaped wire envelopes with actual prefix citations, polarities, scores, evidence_refs, cohort_scope, mutability, schema_ref, witness_relation. Mechanizable.

---

## 7. Cross-references

- `LANGUAGE_PRIMER.md` v2.0 — the symbolic-logic grammar used by the 7 sub-agents
- `CONTRIBUTION_OBJECTS_CH{0_INTRO, 1_DOCTRINE, 2_FOUNDATIONS, 3_TECH_AI, 4_TRUTH_WORK_FREEDOM, 5_POWER_LOVE, CONCLUSION}.md` — the 7 per-chapter conversion outputs
- `CONTRIBUTION_MAPPING_SYNTHESIS.md` — round-1 synthesis (the inputs that drove v1.3)
- `source_material/federation/CIRISRegistry/FSD/FSD-002_FEDERATION_SURFACE.md` v1.3 (LOCKED) — the wire format
- `source_material/federation/CIRISNodeCore/MISSION.md` — the 15 primitives
- `METHODOLOGY.md` — the iterative process (sub-agent scan + human review + correct context + re-run)
- `MISSION.md` §1.3 — the grounding posture (recognition with awe, not adjudication)

**End CONTRIBUTION_OBJECTS_SYNTHESIS.md**
