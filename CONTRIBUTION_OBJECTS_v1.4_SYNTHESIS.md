# CONTRIBUTION_OBJECTS_v1.4_SYNTHESIS.md — Round-3 Conversion, Consolidated

**Version**: 1.0 (round 3; FSD-002 v1.4-aligned; Registry-synced primer; composition-before-extension discipline)
**Date**: 2026-05-27
**Inputs**: `CONTRIBUTION_OBJECTS_v1.4_CH{0_INTRO, 1_DOCTRINE, 2_FOUNDATIONS, 3_TECH_AI, 4_TRUTH_WORK_FREEDOM, 5_POWER_LOVE, CONCLUSION}.md` — 7 sub-agent outputs producing YAML wire envelopes under the corrected primer
**Grammar**: `LANGUAGE_PRIMER.md` (synced from `CIRISRegistry/FSD/LANGUAGE_PRIMER.md` v1.1 at commit `c232a60`); FSD-002 v1.4 (80 prefix families; 1+4 structural primitives; canonical 8 axes)
**Methodology**: `METHODOLOGY.md` §8.5 round-2-to-round-3 lessons

---

## 0. Headline — the framework is genuinely adequate

After three rounds of iterated conversion, FSD-002 v1.4 + the corrected Registry-synced primer + the composition-before-extension discipline produces **zero new load-bearing T-3 candidates** across all 245 numbered paragraphs of *Magnifica Humanitas*. The only T-3 emitted in round 3 (CH 0 §15, positive-dignity non-substitutability) is the already-tracked v1.5+ workshop candidate from FSD-002 §13.11 #3.

The encyclical mapping work is complete. **The federation wire format speaks the encyclical's content as structured Contributions, in CIRIS-native vocabulary, with discipline holding throughout.**

---

## 1. Verdict distribution (aggregate, 245 paragraphs)

| Verdict | Approx Count | Share |
|---|---|---|
| clean | ~73 | 30% |
| composed | ~107 | 44% |
| partial | ~13 | 5% |
| not-translated | ~52 | 21% (mostly T-1 + T-2; correct posture for theological / pastoral content) |

**Clean + composed**: ~73%. With partial-structural-translates included: ~78%.

Per-chapter:

| Chapter | Paragraphs | Clean | Composed | Partial | Not-translated | Clean+Composed |
|---|---|---|---|---|---|---|
| CH 0 Intro | 16 | 4 | 5 | 2 | 5 (mostly T-2) | 56% |
| CH 1 Doctrine | 29 | 6 | 17 | 6 | 0 | **79%** |
| CH 2 Foundations | 44 | 18 | 15 | 1 | 10 (T-1 + T-2) | **75%** (of wire-emitting: 97% clean+composed) |
| CH 3 Tech / AI | 41 | 8 | 18 | 0 | 15 (T-1 + T-2 residuals) | 63% on strict count; ~76% if T-1-residual-with-clean-structural counts as clean |
| CH 4 Truth / Work / Freedom | 51 | 14 | 33 | 0 | 4 (T-2) | **92%** |
| CH 5 Power / Love | 47 | 23 | 10 | 4 | 10 | **70%** (T-1 surge in Arc B is correct) |
| Conclusion | 17 | 0 | 9 | 0 | 8 (all T-1) | 53% (correct posture for doxological closing) |
| **TOTAL** | **245** | **~73** | **~107** | **~13** | **~52** | **~73%** |

The pure-count numbers are slightly lower than round-2's ~78% because round-3 was more honest about T-1 declarations (each one names the specific theological claim being honored, rather than counting as "partial + T-1 tail"). This is the correct trade-off — honest classification beats inflated clean+composed rate.

---

## 2. Structural primitives finally used correctly

The single biggest difference between round-2 and round-3 outputs: **the four structural primitives are now actually being used** where appropriate, after the primer drift was corrected.

### 2.1 `supersedes` — 15 uses

**The encyclical's doctrinal-development claims map exactly to `supersedes`.** This was entirely missed in round-2 due to the primer's mislabeling.

- CH 1 ×14: every paragraph in the papal-lineage survey (§§17, 28-44 — Leo XIII → Pius XII → Vatican II → Paul VI → JPII → Benedict → Francis → Leo XIV) cleanly emits a `supersedes` envelope with `differs_in: ["scope", "evidence_refs"]` + `integrity:doctrinal_continuity`. Each version extends but does not contradict the prior. The encyclical's "living-tradition development" claim has a precise wire-format home.
- CH 0 §3 ×1: Rerum Novarum → Magnifica Humanitas succession.

### 2.2 `recants` — 1 use (and it's the most striking finding)

**CH 4 §176** — the Church's historical complicity in slavery. The text explicitly admits prior attestations (and behaviors) were false at issuance and asks for pardon. This satisfies the epistemic-error-admission criterion per LANGUAGE_PRIMER §3:

- `recants` (not `withdraws`) is the correct primitive — the encyclical does not merely retract a position; it admits the position was wrong when held.
- This is the framework's `recants` primitive at its highest moral seriousness: admitting error as a primary act, not a derivative of retraction. The encyclical's willingness to apply this to its own institution's history is precisely what the primitive is designed to carry.
- No other prior identity system (PGP, SPKI/SDSI, W3C VC per the PRIOR_ART_SCAN) typed epistemic-error-admission as a wire primitive distinct from retraction. The federation has it because the Recursive Golden Rule applies to attesters.

### 2.3 `delegates_to` and `withdraws` — 0 uses

Neither structural primitive was warranted by encyclical content. `delegates_to` was tested as a possible reuse pattern for Magisterium-as-authority-source claims (per the §2.2.1 documented pattern); sub-agents correctly resolved those to T-1 instead, because the encyclical's Magisterium claims go beyond delegated-scope into the tradition's own theological authority.

### 2.4 What this means

The structural primitives are not pedagogical — they are wire-format primitives that carry specific moral acts (extending without contradiction; admitting error; retracting without claiming falsity; delegating authority). When sub-agents missed them in round 2, the encyclical's most distinctive structural acts (doctrinal continuity, institutional repentance) were rendered as paraphrases. Round 3 captures them precisely.

---

## 3. v1.3 + v1.4 closures confirmed in production

All wire-format additions from v1.3 and v1.4 are actively used by round-3 outputs. The framework's expressive coverage is verifiably broader than v1.2.

### v1.3 closures (4 HIGH-priority + 2 MEDIUM)

| Addition | Round-3 usage | Confirmation |
|---|---|---|
| `locality:decision:{scale}` | CH 0 §13; CH 1 §31; CH 2 §§68-72, 87; CH 3 §§110-111 federation scale | ✓ deployed widely; subsidiarity claim closed |
| `detection:distributive:access:{resource_type}` | CH 1 §43; CH 2 §§65-67, 76; CH 3 §§110-111 | ✓ deployed; universal-destination-of-goods closed |
| `credits:*:substrate_building` | CH 2 §73 (solidarity); CH 3 §109 (hidden algorithmic workers); CH 4 §§148-156 (labor displacement) | ✓ deployed; supply-chain labor recognition closed |
| `multilateral_participation:{forum}:{kind}` | CH 4 §§142, 155, 163; CH 5 §§189, 200-203, 224-227 | ✓ deployed; multilateral reform + cyber diplomacy closed |
| `detection:correlated_action:ecology_of_communication:{aspect}` | CH 4 §137 (×2 axes: transparency, intermediary_strength) | ✓ deployed |
| §6.1.4 lexical-vulnerability-priority policy | CH 0 §14 (preferential-option tie-breaking); CH 2 §§77-81 | ✓ used as composition tie-breaker |

### v1.4 closures (3 new + 1 documentation pattern)

| Addition | Round-3 usage | Confirmation |
|---|---|---|
| `testimonial_witness:{kind}` (NodeCore §3.6.3) | CH 2 §81 (displaced_person), §89 (abuse_survivor); CH 3 §124; CH 4 §§138, 151, 166, 167, 173 (5 instances); CH 5 §216 (war_victim), §217 | ✓ widely deployed; round-2 load-bearing T-3 closed |
| `agent_files:{kind}:{platform_or_target}` | not triggered by encyclical content (canonical-installer claims weren't in the text) | architectural addition for future bootstrap-contributions deployments |
| `holds_bytes:sha256:{prefix}` | same — substrate auto-emission, not triggered by encyclical | architectural addition |
| `labor:individual_loss` closed-by-documentation composition | CH 4 §§150-156, 166-167, 173 (8 instances) | ✓ composition pattern works; no new prefix needed |

---

## 4. The expressive map after round 3

**The federation wire format substantively covers the encyclical's operational content.** Of 245 paragraphs:

- ~73% (clean + composed) translate into structured Contributions with no operational loss
- ~5% (partial) translate the core structural shape with a meaningful T-1 / T-2 / T-3 tail
- ~21% (not-translated) are correctly classified:
  - **T-1 (TRADITION_AUTHORITY)** — Christological / Eucharistic / Trinitarian / Marian content; framework correctly bows out
  - **T-2 (PASTORAL_PROSE)** — rhetorical framing; §1.10.1 gate correctly excludes from wire prefix names
  - **T-3 (EXPRESSIVE_GAP)** — only 1 row across the entire conversion (CH 0 §15 positive-dignity), and it is the already-tracked v1.5+ workshop candidate

**Zero new load-bearing T-3 candidates surfaced in round 3.** The framework is genuinely epistemically adequate against *Magnifica Humanitas*; remaining design-workshop items (positive-dignity non-substitutability, finitude-as-value, sustained_practice) are LOW priority refinements, not gaps in coverage.

---

## 5. The strongest envelopes — the encyclical's most-demanding claims, cleanest wire renderings

**CH 4 §176 — Church's historical complicity in slavery** (`recants`): the morally heaviest single envelope. The text explicitly admits prior teaching was false at issuance; `recants` carries the admission cleanly. No other framework in the prior-art scan types this distinctly.

**CH 5 §§197-198 — autonomous lethal weapons** (`prohibited:weapons_harmful` polarity -1, constitutional): verbatim string matches to `WEAPONS_HARMFUL_CAPABILITIES`. The encyclical's most absolute moral claim has the framework's most absolute structural form. Constitutional-leaf, non-amendable, species scope.

**CH 1 §17 — doctrinal development in fidelity to Gospel** (`supersedes` with `differs_in: ["scope", "evidence_refs"]` + `integrity:doctrinal_continuity`): the chain that opens the entire papal-lineage survey. Captures "extends but does not contradict" exactly.

**CH 3 §§110-111 — disarm AI from monopoly** (5-primitive composed envelope: `accord:hard_constraint:no_kings` + `locality:decision:federation` + `detection:distributive:access:compute` + `integrity:design_transparency` + `beneficence:technology_as_creation_participation`): the chapter's strongest composed envelope; the architecture's NO KINGS invariant + transport + federation + license + design-transparency all mobilized for one paragraph.

**CH 2 §36 (referenced from CH 1) — structures of sin** (`detection:correlated_action:aggregate_footprint:expendability_of_persons`): the v1.2 extension that closed the original F-3 gap; round-3 confirms the closure.

---

## 6. The arc of the work

| Round | Question | Adequacy | T-3 candidates surfaced | Status |
|---|---|---|---|---|
| 1 (structural mapping) | Does CIRIS already cover this? | n/a | 13 candidates | Deleted; superseded |
| 2 (contribution-language test) | Can CIRIS *speak* what the encyclical says? | ~75-80% | 13 candidates surfaced; 7 closed in v1.3 prep | Deleted; superseded |
| 3 (wire conversion with primer-drift correction) | Can CIRIS *emit* what the encyclical says as wire envelopes? | ~73% clean+composed; ~78% including partial-structural | 1 candidate (already-tracked v1.5+ workshop) | **Current** |

Each round produced inputs that closed the prior round's residual gaps:
- Round 1 → drove v1.3 doctrinal revisions
- Round 2 → drove v1.4 wire-format additions (testimonial_witness, agent_files, etc.)
- Round 3 → no new T-3 candidates; framework is adequate

**The work is at a natural pause.** Future rounds will be triggered by:
- New senior frameworks deployed (EU AI Act, NIST AI RMF, CARE Principles, etc. per FSD-002 §10.4 bootstrap-contributions pattern)
- New encyclical or magisterial documents
- Live framework changes that warrant re-evaluation

---

## 7. Discipline checks held

- **No invented verdict categories.** Strict 4: clean / composed / partial / not-translated.
- **No over-composition.** Composed verdicts capped at 2-3 contributions per paragraph (with one rare 5-primitive composed envelope at §§110-111 where the architecture genuinely mobilizes 5 named commitments).
- **No Catholic vocabulary in prefix names.** Subsidiarity → `locality:decision:{scale}`; universal destination of goods → `detection:distributive:access:{resource_type}`; structures of sin → `detection:correlated_action:aggregate_footprint:expendability_of_persons`; preferential option for the poor → §6.1.4 lexical-vulnerability-priority policy.
- **Composition-before-extension held.** Every T-3 candidate (1 total) carried explicit composition-attempt documentation per METHODOLOGY.md §8.5.2.
- **Structural primitives actually used.** 15 `supersedes` + 1 `recants` — round-2 missed all of these due to primer drift.
- **Canonical envelope shape used throughout.** `attesting_key_id` / `attested_key_id` / `attestation_envelope` per FSD-002 §2.1.
- **Eight canonical axes** per FSD-002 §1.1-§1.8 — Polarity / Object / Time / Epistemic-mode / Reversibility / Stake / Scope / Inter-attestation-relations.

---

## 8. v1.5+ workshop candidates (deferred; not load-bearing)

Three items remain as design-workshop candidates per FSD-002 §13.11 — these were never triggered by encyclical content in any of the three rounds, and remain available for future refinement:

| # | Working name | Status | Reason for deferral |
|---|---|---|---|
| #3 | `attestation:singular_witness:non_substitutability` (positive dignity) | DEFERRED | T2 gate fragility — needs design workshop to surface a mechanism-descriptive form that doesn't collapse to subjective-quality vocabulary |
| #4 | `integrity:finitude_acknowledgment` | DEFERRED | LOW priority; conceptually interesting; not load-bearing |
| #6 | `sustained_practice:{kind}` | DEFERRED | LOW priority; partially covered by σ; sustained-vocation-vs-episodic-contribution distinction is conceptually adjacent to gratitude-signaling |

---

## 9. Cross-references

- `LANGUAGE_PRIMER.md` v1.1 (Registry-synced) — the corrected grammar
- `CONTRIBUTION_OBJECTS_v1.4_CH{0_INTRO, 1_DOCTRINE, 2_FOUNDATIONS, 3_TECH_AI, 4_TRUTH_WORK_FREEDOM, 5_POWER_LOVE, CONCLUSION}.md` — the 7 per-chapter conversion outputs
- `METHODOLOGY.md` §8.5 — round-2-to-round-3 lessons (wire-format sync discipline; composition-before-extension; in-flight staleness; namespace integrity; prompt synchronization; cleanup-and-redo)
- `source_material/federation/CIRISRegistry/FSD/FSD-002_FEDERATION_SURFACE.md` v1.4 — the wire format (LOCKED)
- `source_material/federation/CIRISNodeCore/MISSION.md` — the 15 NodeCore primitives
- `MISSION.md` §1.3 — the grounding posture (recognition with awe, not adjudication)
- Issue [`ciris-response-magnifica-humanitas#3`](https://github.com/CIRISAI/ciris-response-magnifica-humanitas/issues/3) — the drift correction that triggered round 3

**End CONTRIBUTION_OBJECTS_v1.4_SYNTHESIS.md**
