# MISSION_CIRISLensCore.md evaluation against GAPS.md

## Gap A-2: cohort detector for concentration patterns
**Verdict**: REFINEMENT
**Rationale**: Cohort routing exists philosophically; adding a concentration-pattern detector is a new detector type, not a new philosophy. MISSION covers the shape; the subject matter (market position) needs a clarifying sentence.
**MISSION section if applicable**: §2 `cohort/` — "cohort routing makes the federation pluralistic at the analytical surface"

---

## Gap B-1: benefit_distribution_index
**Verdict**: SUBSTANTIAL_EDIT
**Rationale**: MISSION_CIRISLensCore is entirely about scoring reasoning traces for alignment-conformity. Aggregating CIS declaration fields (operator/user value split) as a federation metric operates on declared intent data, not trace behavior — no philosophical grounding in the current charter.
**MISSION section if applicable**: §1 — "route, score, and sign every trace"; §8 closing — "make alignment measurable on the hot path"

---

## Gap B-3: intertemporal_beneficiary_ratio
**Verdict**: SUBSTANTIAL_EDIT
**Rationale**: Lens-core's manifold-conformity scoring is per-trace, per-agent, per-cohort. An intertemporal ratio aggregates action-stream impact across time horizons — impact measurement, not reasoning-trace measurement. Philosophically outside current charter scope.
**MISSION section if applicable**: §2 `scoring/` — "capacity scores, N_eff trajectories, detection events"

---

## Gap C-1: ecosystem metrics (source_diversity_index, attention_flow_concentration, discourse_correlation_rise)
**Verdict**: PAPERING_OVER
**Rationale**: MISSION explicitly defines lens-core as measuring signed reasoning traces. C-1 proposes measuring aggregate output content (source citations, attention flows) — this is "measure the impact," not "measure the reasoning." The charter has no hook for this and actively scopes against it.
**MISSION section if applicable**: §1 — "lens-core is what makes signed traces measurable"; §8 — "make alignment measurable on the hot path of every CIRIS peer"

---

## Gap D-1: labor_displacement_index
**Verdict**: SUBSTANTIAL_EDIT
**Rationale**: Aggregating CIS-declared labor-displacement fields across federation peers is a governance metric, not a trace-scoring primitive. Lens-core has no philosophical grounding for CIS-declaration aggregation; the charter is silent on this class of measurement.
**MISSION section if applicable**: §2 `scoring/` — all scored outputs are detection events on the trace corpus

---

## Gap D-2: agency_erosion_index federation aggregator
**Verdict**: PAPERING_OVER
**Rationale**: Longitudinal user-decision-acceptance patterns are not present in the signed trace corpus lens-core scores. Aggregating this cross-federation requires measuring behavioral content of agent-user interaction streams — impact measurement that directly contradicts the charter's trace-substrate philosophy.
**MISSION section if applicable**: §1 — "a function any peer can run on data the peer already has"; §3 anti-pattern #1 — "re-implementing what edge or persist owns"

---

## Gap F-1: structural pattern metrics (disparate_outcome_index, incumbent_reinforcement_signal, stakeholder_exclusion_signal)
**Verdict**: PAPERING_OVER
**Rationale**: These metrics require analyzing the semantic content of agent recommendations and their real-world routing of resources/attention — outcome impact analysis. Lens-core's mission is manifold-conformity on the reasoning trace. This is a different epistemological layer the charter explicitly does not address.
**MISSION section if applicable**: §8 — "operationalize F-AV catalog Class 2–5 detection" (all five are reasoning/behavioral detectors on traces, not outcome impact detectors)

---

## Gap G-1: compute_intensity_per_outcome
**Verdict**: REFINEMENT
**Rationale**: Energy telemetry is already in the trace corpus (LLMBus tags per thought_id). A compute/outcome ratio is a new aggregation on existing trace data — within lens-core's substrate philosophy. One clarifying sentence suffices.
**MISSION section if applicable**: §2 `scoring/` — "every score is a record in persist signed via the host's steward identity"

---

## Overall pattern

- Verdict distribution: NOTHING_NEEDED: 0 | REFINEMENT: 2 (A-2, G-1) | SUBSTANTIAL_EDIT: 3 (B-1, B-3, D-1) | PAPERING_OVER: 3 (C-1, D-2, F-1)

- Most philosophically-significant finding: Three gaps (C-1, D-2, F-1) introduce a scope-creep from "measure the reasoning" to "measure the impact." MISSION_CIRISLensCore defines lens-core's substrate as signed reasoning traces that any peer can re-score from data it already holds. C-1 ecosystem metrics, D-2 agency-erosion federation aggregation, and F-1 structural pattern analysis all require measuring the semantic content or real-world downstream effects of agent outputs — a categorically different epistemological layer. These are not extensions of the charter; they contradict its central architectural constraint (§1: "a function any peer can run on data the peer already has"; §3 anti-pattern #1). If implemented under the lens-core umbrella, they paper over the trace-substrate philosophy without naming the philosophical shift. The honest move is a new charter for an impact-measurement crate, not an extension of lens-core's MDD.
