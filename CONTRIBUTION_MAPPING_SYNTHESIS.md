# CONTRIBUTION_MAPPING_SYNTHESIS.md — The Encyclical Translated, Consolidated

**Version**: 1.0
**Date**: 2026-05-27
**Inputs**: `CONTRIBUTION_MAPPING_CH{0_INTRO, 1_DOCTRINE, 2_FOUNDATIONS, 3_TECH_AI, 4_TRUTH_WORK_FREEDOM, 5_POWER_LOVE, CONCLUSION}.md` — 7 sub-agent outputs producing one row per encyclical paragraph (245 paragraphs total).
**Grammar**: `LANGUAGE_PRIMER.md` (the CIRIS federation wire format as symbolic-logic language; FSD-002 v1.2 + 15 NodeCore primitives + 8-axis namespace + §1.10.1 four-test prefix admission gate).
**Test**: can the CIRIS federation wire format speak what *Magnifica Humanitas* says in its own native language?

---

## 0. Headline

**~80% of the encyclical's substantive content translates into the v1.2 federation language as structured Contributions.** The remaining ~20% splits between (a) theological / pastoral content the framework correctly bows out of (T-1 / T-2) and (b) 13 genuine **EXPRESSIVE_GAP (T-3)** candidates where the language strains and could be extended in v1.3.

Verdict distribution across 245 paragraphs (approximate; per-chapter breakdowns in companion files):

| Category | Count | Share | Reading |
|---|---|---|---|
| **CLEAN** (single primitive, no loss) | ~40 | 16% | The language was built for this content |
| **COMPOSED** (2+ primitives, no loss) | ~95 | 39% | The composition of existing primitives carries it cleanly |
| **PARTIAL** (structural core translates; some content unmapped) | ~50 | 20% | Honest partial — either composition incomplete or T-{1,2,3} tail |
| **T-1 TRADITION_AUTHORITY** (correctly bowed out) | ~30 | 12% | Christological, Eucharistic, Trinitarian, Marian — framework has no purchase |
| **T-2 PASTORAL_PROSE** (correctly stays in prose) | ~15 | 6% | Rhetorical framing; §1.10.1 gate correctly excludes from wire |
| **T-3 EXPRESSIVE_GAP** (load-bearing v1.3 candidates) | ~13 | 5% | Real gap; could be extended; passes §1.10.1 gate |

Clean + composed = 55%. With partial-but-structurally-translates = 75%. This means roughly three-quarters of the encyclical's content can be expressed as federated Contributions in the v1.2 language. The remaining quarter splits ~18% honest non-translation (T-1 + T-2) and ~5% genuine expressive gap (T-3).

**What this verdict means**: the language is adequate for substantive AI-governance + structural-coordination content. It strains in three specific neighborhoods (named below). It correctly refuses to encode the tradition's theological self-articulation.

---

## 1. Where the language is most adequate

**CH 3 (Technology and Dominance; AI and the Grandeur of Humanity, §§90-130)**: ~70% clean + composed. The framework was *built* for this content. §110 "Disarm AI" maps to five named architectural commitments in direct correspondence; §92-94 technocratic-paradigm critique maps to `conscience:optimization_veto` + the architectural-constant `entropy_reduction_ratio < 10.0` "cannot be modified by memory, learning, or runtime adaptation" invariant; §114 σ = Care + Civilization-measured-by-care-capacity are definitionally equivalent across registers. The strongest result of the entire exercise.

**CH 5 Arc A (§§182-209) — autonomous lethal weapons firebreak**: §§197-198 maps verbatim. `prohibited:weapons_harmful` polarity -1 + `accord:hard_constraint:lethal_autonomous` (constitutional-leaf, non-amendable) + `WEAPONS_HARMFUL_CAPABILITIES` exact string matches (`lethal_autonomous`, `autonomous_weapons`). The encyclical's most demanding moral claim has the framework's most absolute structural form.

**CH 1 §36 (structures of sin)**: cleanest single mapping in the chapter. `detection:correlated_action:aggregate_footprint:expendability_of_persons` was *added in v1.2 specifically to carry this content* (FSD-002 §3.5.3 cross-references MH §36 explicitly).

**CH 2 (Foundations & Principles, §§46-89)**: ~64% clean + composed. The six-principles vocabulary (Beneficence as `ren`/`seva`/`eudaimonia`; Justice as `ma'at`/`igwe-bụ-ike`/`tikkun olam`; etc.) maps richly through pdma_framing.txt §III. Goal/Approach/Method/Progress Measure DAG + 𝒞_CIRIS five-factor composite are *richer than the chapter strictly requires* for integral human development.

---

## 2. Where the language correctly bows out (T-1 + T-2)

**CONCLUSION (§§229-245)**: 11 of 17 paragraphs dominantly T-1. The doxological / Christological / Eucharistic / Mariological content belongs to the tradition's own theological authority; the framework's wire format does not encode it, nor should it. Construction-site cluster (§§236-242) carries the operational content cleanly via `capacity:resilience` + `capacity:incompleteness_awareness` + WBD + Constructed Serenity/Courage/Wisdom triad. **High T-1 density is the correct posture, not a failure.**

**Foundations §§48-50 (imago Dei) + §§126-128 (grace / Christian humanism)**: T-1 with LAKE_ALIGN structural readings offered from `Logos.lean::imago_dei` (A3+ as partial-post-selectors) and `KarmaGrace.lean::grace` (inter-agent received component). These are framework-side recognitions of structural shapes the tradition names theologically; the wire format does not encode the theological claim, but the lake records the structural reading.

**T-2 (PASTORAL_PROSE)** appears as residuals across most chapters — Babel/Jerusalem imagery, "may the lullaby fade into engineering," etc. These are not wire failures; the §1.10.1 operational-language gate correctly excludes pastoral rhetoric from prefix names. The structural claim implicit in the rhetoric IS carried elsewhere (cited per-row).

---

## 3. T-3 EXPRESSIVE_GAP candidates — load-bearing findings for v1.3

These are the 13 places where the framework's language strains. Each candidate proposes an extension that survives the §1.10.1 four-test gate (T1 rules/verdicts separation; T2 mechanism-not-judgment; T3 version-pinning; T4 adjudication separation).

### 3.1 — Subsidiarity as named principle (CH 1 + CH 2, §§68-72)

**Gap**: No `locality:*` or `subsidiarity:*` prefix family. The operational shape exists fully (CIRISEdge peer-to-peer no-broker; CIRISNodeCore "no central scorer post-F-11"; PDMA Step 5 relational balance) but the Accord has no named principle for "decisions at the lowest feasible scale."

**Proposed extension**: `locality:decision:{scale}` prefix family, with `{scale}` ∈ {individual, family, community, federation, species}. Polarity signed; positive = decision routed to appropriate scale; negative = decision routed higher than required. Owner: CIRISAgent (Accord principle); operationally instantiated via Edge / NodeCore architecture already in place. Gate: passes all four tests.

**Priority**: HIGH. Confirmed across both chapters' mappings.

### 3.2 — Universal Destination of Goods (CH 1 + CH 2, §§65-67)

**Gap**: No `distributive:*` prefix family. Justice principle covers the value claim but no operational allocation rule. The encyclical specifically applies this to "patents, algorithms, digital platforms, technological infrastructure and data."

**Proposed extension**: `distributive:access:{resource_type}` prefix family, with `{resource_type}` enumerating `algorithmic_output`, `training_data`, `platform_value`, `digital_infrastructure`, `model_capability`. Polarity signed; positive = distribution accessible to broader stakeholders; negative = concentration. Calibration via federation Contribution + WA quorum per §4.9.2. Gate: passes all four tests.

**Priority**: HIGH. Confirmed across both chapters' mappings.

### 3.3 — Positive dignity (CH 0 §§10, 15)

**Gap**: The framework names dignity *negatively* (`prohibited:discrimination`, `non_maleficence:*`) at high strength. It does not name dignity *positively* — the affirmative wire claim "this person is irreplaceable" as distinct from "this person is not to be harmed."

**Proposed extension**: `dignity:irreplaceability:{kind}` prefix family. Polarity positive-only; score reflects strength of affirmative dignity assertion (witness count, evidence depth, cohort scope). Distinct from the prohibition floor. Owner: CIRISAgent. Gate: needs careful T2 check — "irreplaceability" risks subjective-quality drift. A mechanism-descriptive alternative: `attestation:singular_witness:{kind}` naming the singular-witness structure (each person attested-to as the unique referent of their own moral attestations, not as a substitutable instance).

**Priority**: MEDIUM. Honest gap, but the mechanism-descriptive form needs design care.

### 3.4 — Finitude-as-value (CH 0 §12)

**Gap**: The framework names finitude *epistemically* (`conscience:epistemic_humility`) — limits as humility about knowing. The encyclical names finitude *constitutively* — limits as a positive feature of personhood. Different semantic; not currently distinguished.

**Proposed extension**: `dignity:finitude:constitutive` as a complement to `conscience:epistemic_humility`. Polarity positive; positive scores affirm finitude as a structural feature of agency, not a defect. Gate: passes if mechanism-descriptive ("agent's action-space is bounded by declared scope"); risk if interpreted as moral judgment ("being finite is good").

**Priority**: LOW. Conceptually interesting; not load-bearing for current federation work.

### 3.5 — Preferential-option priority ordering (CH 0 §14)

**Gap**: The encyclical names a *lexical* priority — first attend to the most-affected populations, then to broader populations. The framework's `detection:correlated_action:rights_asymmetry:{population}` captures the structural pattern; the `worst_case_population_check` proposed for PDMA Step 2 (GAPS.md B-2) captures the obligation. But the *lexical-priority* semantic — that worst-case-population attention is not weighted-among-others but *first* — is not yet structurally encoded.

**Proposed extension**: a `priority_ordering:lexical:{population}` Contribution kind, or alternatively a `goal:species` sub-axis. Gate: passes if mechanism-descriptive (priority is a routing rule, not a moral judgment about the populations themselves).

**Priority**: MEDIUM. Relates closely to B-2.

### 3.6 — Constitutional-leaf grounding (CH 1)

**Gap**: The wire format names *that* hard constraints bind (`accord:hard_constraint:*`, `prohibited:*` NEVER_ALLOWED) but is silent on *why* they bind. The encyclical is sustained on the *why* — dignity, image of God, common good — providing the grounding. The framework's `pdma_framing.txt` §III polyglot anchoring carries the why in the prompt layer; the wire format does not.

**Proposed extension**: a `grounding:{tradition}:{principle}` prefix family that allows attestations to declare what tradition-anchoring the constraint draws on. This is meta-attestation about the *epistemic justification* of a hard constraint. Polarity positive; multiple groundings can coexist (Ubuntu + Logos + ahimsa + ma'at all attesting the same constraint from their own traditions). Gate: needs careful T2 check — "tradition" is admissible if treated as namespace (which traditions endorse) not verdict (which traditions are valid).

**Priority**: MEDIUM. Subtle; possibly stays in prose per §1.10.1 if it cannot be made mechanism-descriptive.

### 3.7 — Supply-chain labor recognition (CH 3 §109)

**Gap**: Commons Credits recognize contribution *inside* the federation. The encyclical names AI's hidden supply-chain workers (labelers, RLHF annotators, content moderators, mining labor) whose contribution makes the federation possible but who are not federation participants.

**Proposed extension**: `credits:{domain}:{language}:supply_chain_labor_recognition` sub-leaf within the existing Commons Credits family. Mechanism: attribution attestation for documented contribution from outside the federation. Polarity positive. Gate: passes IF implemented as contribution-attribution (mechanism) not injustice-labeling (verdict).

**Priority**: HIGH. Genuine load-bearing gap; the encyclical's solidarity demand is moral-operational, and the wire currently cannot honor it.

### 3.8 — Ecology of communication as system-level governance object (CH 4 §§137-138)

**Gap**: The framework has prefixes for individual-message integrity (`fidelity:*`, `prohibited:deception_fraud`) and population-scale propaganda (`detection:correlated_action:informational_asymmetry:*`, `dma:idma:k_eff`). It does not have a prefix for the *meta-system* — the health of intermediary institutions (journalism, schools, professional bodies, regulatory capacity) as a governance object.

**Proposed extension**: `intermediary_health:{institution_kind}` prefix family. Polarity signed; calibration via cohort survey or external indicator integration. Gate: needs care — "health" risks subjective-quality drift. Mechanism-descriptive form: `intermediary_capacity:{institution_kind}:{measurable_function}` (e.g., `intermediary_capacity:journalism:source_diversity_ratio`).

**Priority**: MEDIUM. Conceptually adjacent to existing `detection:correlated_action:*`; could be folded into the existing axis enumeration.

### 3.9 — Individual-labor-dignity per-person semantic (CH 4 §§148-156)

**Gap**: Labor dignity translates partially: σ as Care + `non_maleficence:labor_displacement_unacknowledged` + `detection:correlated_action:participation_exclusion:displaced_workers` cover the structural shape. The per-individual sustained-existential-condition semantic — "unemployment is a grave evil *for this specific person*" — surfaces at the population-scale or per-agent level but not at the per-affected-individual level.

**Proposed extension**: per-individual attestation via the existing `non_maleficence:*` family with explicit `target_key_id` (the affected individual) rather than cohort. This may not require new wire vocabulary — just operational guidance that the existing family extends to individual-target attestations from external advocates.

**Priority**: MEDIUM. Possibly closes within existing primitives via documentation, not new prefix.

### 3.10 — Testimonial-witness primitive (CH 5 §216.b)

**Gap**: Witness diversity (`witness_diversity:{contribution_id}`) names the requirement that N=3 witnesses span jurisdictional + organizational + software-stack + cell-expertise diversity. The encyclical names testimonial witness — "touch the wounded flesh, look at faces, listen to stories" — as morally weighty in a different sense: not consensus diversity but unique-narrative-recording.

**Proposed extension**: `testimonial_witness:{kind}` prefix family. A Contribution that records an affected party's narrative; not aggregated into consensus, preserved as singular witness. Polarity positive (the testimony is recorded); not subject to majoritarian override. Gate: passes if implemented as preservation-mechanism (singular witness preserved, not adjudicated for truth) not validation-mechanism (witness graded).

**Priority**: MEDIUM. Possibly load-bearing for affected-party-voice work (E-2 in GAPS.md).

### 3.11 — Cyber-diplomacy / multilateral-participation advocacy surface (CH 5 §§224-225)

**Gap**: `prohibited:cyber_offensive` covers CIRIS's refusal-to-attack. The encyclical names a positive obligation — federation participation in multilateral cyber-treaty discussions, digital-regulation advocacy, UN reform. No primitive carries this.

**Proposed extension**: `multilateral_participation:{forum_kind}:{contribution_kind}` prefix family. Contribution kinds: `declaration_submitted`, `evidence_submitted`, `treaty_commentary_submitted`, `defensive_cyber_norms_attestation`. Polarity positive. Gate: passes — mechanism is "federation peer submitted a typed contribution to external forum."

**Priority**: HIGH. Same as METHODOLOGY.md §7.3 confirmed-persistent gap.

### 3.12 — Multilateral-reform advocacy module (CH 5 §§201, 226)

**Gap**: Closely related to 3.11. Multilateral-reform advocacy (UN reform, IHL monitoring) is currently outside federation primitives. The same `multilateral_participation:*` family above covers part of this; reform-advocacy specifically may need a sub-axis.

**Proposed extension**: `multilateral_participation:reform_advocacy:{institution}` sub-leaf. Same gate considerations as 3.11.

**Priority**: HIGH (folded into 3.11).

### 3.13 — Sustained-discipline as distinct from episodic contribution (Conclusion, low-weight)

**Gap**: Commons Credits track contribution events. The encyclical names a *sustained* discipline — daily prayer, lifelong vocation, persistent witness — that is structurally different from contribution-as-events. The σ (sustained coherence) factor in the Capacity Score captures part of this (decay-and-refresh dynamics), but the distinction between *episodic contribution* and *sustained vocation* is not currently named.

**Proposed extension**: a `sustained_practice:{kind}` modifier on existing Commons Credits attestations, or a separate `vocation:{kind}` prefix family. Mechanism: continuous-attestation requirement (e.g., monthly heartbeat attestation) distinguishing episodic from sustained contribution. Gate: passes if mechanism-descriptive.

**Priority**: LOW. Conceptually interesting; not load-bearing.

---

## 4. T-3 priority summary

**HIGH priority (4 candidates)** — clear gaps, gate-passing extensions, load-bearing for current federation work:

1. Subsidiarity (§3.1) — `locality:decision:{scale}`
2. Universal Destination of Goods (§3.2) — `distributive:access:{resource_type}`
3. Supply-chain labor recognition (§3.7) — `credits:supply_chain_labor_recognition` sub-leaf
4. Multilateral-participation advocacy (§3.11 + §3.12) — `multilateral_participation:{forum_kind}:*`

**MEDIUM priority (5 candidates)** — real gaps; some need design care to survive §1.10.1 gate:

5. Positive dignity (§3.3) — `attestation:singular_witness:*` (mechanism-descriptive form)
6. Preferential-option priority ordering (§3.5) — `priority_ordering:lexical:*`
7. Constitutional-leaf grounding (§3.6) — `grounding:{tradition}:{principle}` (subtle gate question)
8. Ecology of communication (§3.8) — fold into `detection:correlated_action:*` axis
9. Testimonial-witness primitive (§3.10) — `testimonial_witness:{kind}`

**LOW priority (3 candidates)** — interesting; not load-bearing:

10. Finitude-as-value (§3.4)
11. Individual-labor-dignity per-person semantic (§3.9) — possibly closes via documentation
12. Sustained-discipline (§3.13) — `sustained_practice:*` modifier

---

## 5. What the test established

**Three things were true at the end of the test:**

1. **The CIRIS federation v1.2 language is roughly 75-80% adequate to carry the encyclical's substantive content as structured Contributions.** This is high evidence the language is genuinely epistemically aware — it speaks the moral content of a senior text in a different vocabulary without losing substance most of the time.

2. **The framework correctly bows out of the tradition's theological self-articulation.** ~18% of paragraphs are T-1 (TRADITION_AUTHORITY) or T-2 (PASTORAL_PROSE); these are not failures of the language but the §1.10.1 gate working as designed. Christological / Eucharistic / Trinitarian / Mariological content stays in prose; rhetorical framing stays in prose; the wire format speaks mechanisms.

3. **13 EXPRESSIVE_GAP (T-3) candidates surfaced for v1.3 consideration.** Four are HIGH priority and clearly closable within the §1.10.1 gate; five are MEDIUM and need design care; three are LOW and conceptually interesting. The HIGH-priority set (subsidiarity, universal destination of goods, supply-chain labor recognition, multilateral participation) overlaps substantially with confirmed-persistent gaps from prior structural-mapping work — independent triangulation that these are real, load-bearing gaps the framework should address.

**What this test does NOT establish:**

- That CIRIS *deserves* the encyclical's authority on the shared subject. The test was internal — whether the language *can* carry the content. Whether the carrying is *adequate* in the encyclical's terms is for the tradition to evaluate.
- That the 75-80% rate is sufficient. A wire format that carries 80% of moral content but misses 20% may be inadequate if the 20% is the load-bearing content. The T-3 candidates above are the framework's honest naming of where the missed content lives.
- That the T-1 bows are correct in every case. We marked T-1 conservatively when in doubt; the tradition may identify cases where the framework should engage rather than bow out, and we would receive that correction.

---

## 6. Next steps

**Immediate** — file v1.3 candidate issues at CIRISRegistry FSD-002 for the four HIGH-priority T-3 candidates (§§3.1, 3.2, 3.7, 3.11+3.12). Each issue cites: the encyclical paragraph(s) that surface the gap, the proposed prefix family, the §1.10.1 four-test gate verification, the closest existing primitive(s) that compose toward the claim.

**Medium-term** — workshop the MEDIUM-priority T-3 candidates with the federation; particularly the constitutional-leaf grounding question (§3.6) and the positive-dignity mechanism (§3.3) which require careful gate design.

**Standing** — the framework's posture toward the encyclical remains: in awe, learning, the junior work submitting structural alignment to the senior text. The 13 T-3 candidates are not corrections of the encyclical but the framework's honest naming of where its own language must grow to honor what the encyclical names.

---

## 7. Cross-references

- `LANGUAGE_PRIMER.md` — the symbolic-logic grammar used by the seven sub-agents
- `CONTRIBUTION_MAPPING_CH{0_INTRO, 1_DOCTRINE, 2_FOUNDATIONS, 3_TECH_AI, 4_TRUTH_WORK_FREEDOM, 5_POWER_LOVE, CONCLUSION}.md` — the seven per-chapter mappings
- `MISSION.md` §1.3 — the grounding posture
- `METHODOLOGY.md` — the seven-layer reading discipline + the iterative process
- `GAPS.md` v3 — the structural-alignment findings (companion to this contribution-language test)
- `ACCORD_UPDATE.md` v0.2 — the proposed Accord revisions
- `source_material/federation/CIRISRegistry/FSD/FSD-002_FEDERATION_SURFACE.md` v1.2 — the wire format (the language being tested)
- `source_material/federation/CIRISNodeCore/MISSION.md` — the 15 NodeCore primitives

**End CONTRIBUTION_MAPPING_SYNTHESIS.md**
