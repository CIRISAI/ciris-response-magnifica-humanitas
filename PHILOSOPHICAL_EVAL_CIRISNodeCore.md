# PHILOSOPHICAL_EVAL_CIRISNodeCore.md

**Subject**: Proposed enhancements A-1, A-3, E-2, E-3 from `GAPS.md` evaluated against `MISSION_CIRISNodeCore.md`.
**Evaluator**: Claude Sonnet 4.6
**Date**: 2026-05-25
**Verdict set**: NOTHING_NEEDED | REFINEMENT | SUBSTANTIAL_EDIT | PAPERING_OVER

---

## Gap A-1: Decision Locality — lateral scale-routing in deferral

**Verdict**: PAPERING_OVER

**Rationale**: MISSION_CIRISNodeCore §1.2 function 1 defines deferral routing as agent → human WA only. §2.17 explicitly rejects "Deferral as its own primitive" and collapses it into a Contribution subtype. The routing target is the Expertise ledger — human contributors with standing in (domain, language). There is no philosophical surface in the document for routing *to peer agents or smaller institutional units*; the entire deferral model presupposes a human expert pool as the receiving end. Adding lateral peer-agent routing does not extend the existing function; it adds a structural presupposition (peer agents as deferral destinations) that the MISSION has no vocabulary for. The M-1 mandate ("route deferrals to people with relevant expertise") is the operative phrase in §1.1 — "people" is load-bearing. Introducing machine-peer routing as a first-class step before human escalation contradicts the human-expert-as-destination model the philosophy is built around.

**MISSION_CIRISNodeCore section**: §1.1 (Meta-Goal), §1.2 (function 1, deferral routing), §2.17 (rejected primitives: "Deferral as its own primitive"), §3.3 (deferral routing flow — steps 1–4 all resolve to human contributor pool)

**Seventh-function signal**: YES. Lateral scale-routing to peer agents would constitute a seventh function — inter-agent deferral arbitration — that is not named, not bounded, and not philosophically grounded in the current MISSION. The document's six functions all operate over a human participant set. A peer-agent routing layer operates over a machine participant set. That is a different consensus philosophy.

---

## Gap A-3: Federation-Scale Accountability Registry + Cross-Jurisdictional WA Quorum

**Verdict**: SUBSTANTIAL_EDIT

**Rationale**: MISSION_CIRISNodeCore already names jurisdictional diversity as a Witness diversity dimension at P10 (§2, Tier 3) — "Jurisdictional: witnesses span ≥ 2 jurisdictions." This gives the philosophy a jurisdictional-diversity hook. However, P10 applies to *witness attestation* for high-stakes Contributions, not to *deferral resolution itself*. The cross-jurisdictional WA quorum requirement proposed in A-3 is a deferral-resolution discipline, not a witness-attestation discipline. No section of MISSION_CIRISNodeCore addresses the routing of deferral responses through a multi-jurisdictional adjudicator quorum. The high-impact-deployment registry concept has no philosophical home: the crate's Expertise ledger tracks (domain, language) competence, not deployment-scale or jurisdictional footprint of the *requesting agent*. M-1 ("sustainable adaptive coherence... diverse sentient beings") plausibly grounds the concern, but the document provides no mechanism for translating deployment-scale into quorum composition. This is a real philosophical absence in the deferral function's scope, not a contradiction.

**MISSION_CIRISNodeCore section**: §1.1 (M-1), §1.2 (function 1), §3.3 (routing — steps 1–4, no impact-scale signal), §2 Tier 3 P10 (jurisdictional diversity for witnesses, not for WA quorum)

**Seventh-function signal**: PARTIAL. A high-impact-deployment registry tracking (mau_estimate, jurisdictions_touched) is not a new consensus function but it would require CIRISNodeCore to consume deployment-context metadata it currently has no schema for. Whether this is an extension of function 1 or a new function depends on whether the registry lives inside deferral routing (extension) or becomes a separate intake gate (new). The distinction matters and MISSION_CIRISNodeCore should resolve it.

---

## Gap E-2: Affected-Party Inputs Ledger

**Verdict**: PAPERING_OVER

**Rationale**: MISSION_CIRISNodeCore's consensus philosophy is constituted by a *participant pool*: contributors with federation identity, Credits, and Expertise who sign Contributions and Votes. Affected parties (persons impacted by agent actions who did not participate in the review process) are structurally outside the participant pool. The philosophy has no concept of non-participant input to the consensus pipeline. P10 Witness diversity ensures jurisdictional and organizational breadth among *federation participants*; it does not extend to persons who have not joined the federation. Adding an affected-party input ledger requires either (a) granting non-participants a voice in federation consensus, which contradicts the participant-bounded model, or (b) creating a parallel input channel that feeds WA adjudication but bypasses consensus mechanics, which is a new structural presupposition nowhere grounded in the MISSION. ACCORD §M-1's "diverse sentient beings" language is cited as the motivation, but M-1 in MISSION_CIRISNodeCore §1.1 is operationalized as "route deferrals to people with relevant expertise" — the consensus instantiation of M-1 is expertise-and-participation-bounded. Affected-party voice is a different moral category. Filling that gap with a ledger while leaving the philosophy bounded to participants is papering over a real tension: the system claims to serve "diverse sentient beings" but its consensus is constituted only by enrolled ones.

**MISSION_CIRISNodeCore section**: §1.1 (M-1 operationalization), §1.5 (Golden Rule — "participants in the federation"), §1.5 ("humanity accord" — AccordCarrier authority held outside participant set, the one designed asymmetry), P10 (§2 Tier 3 — diversity among participants, not input from non-participants)

**Seventh-function signal**: YES. Affected-party voice is a distinct function — intake from non-participant principals — that the six existing functions do not cover. It would be philosophically novel relative to the MISSION: the document deliberately distinguishes the federation participant set from humanity-as-such (§1.5 humanity accord), and the only mechanism for non-participant authority is the AccordCarrier halt authority — not an input ledger. Implementing an affected-party-input ledger introduces a third category (non-participant affected party with input rights but no halt authority and no consensus standing) that the MISSION does not name.

---

## Gap E-3: Structured Negotiation Primitive — Implement the Stubbed `/api/v1/wa/deferral`

**Verdict**: SUBSTANTIAL_EDIT

**Rationale**: MISSION_CIRISNodeCore identifies the six functions explicitly. Function 1 (deferral routing) returns an aggregate plus individual responses — a one-round process. Function 4 (moderation) provides the adjudication pathway when consensus fails. There is no multi-round exchange mechanism between the deferring agent and the WA pool. P11 Reconsideration provides a reverse adjudication path but operates on a prior SlashingAttestation, not on an open deferral. The `/api/v1/wa/deferral` stub signals that the original CIRISNode designers anticipated a richer semantic — multi-round negotiation — that was never philosophically grounded. The proposed structured negotiation primitive (threaded positions, counter-proposals, negotiation_outcomes) is not a contradiction of MISSION_CIRISNodeCore, but it is absent from the philosophy. Moderation is named as the governance-steering tier (Tier 4) when consensus fails; there is no "negotiated convergence" tier between Tier 3 consensus mechanics and Tier 4 governance steering. This is a genuine structural gap — the philosophy jumps from "aggregate votes produce an outcome" to "persistent failure triggers moderation" without a negotiation layer. Given M-1's emphasis on consent and adaptive coherence, the absence is philosophically significant, not merely implementational.

**MISSION_CIRISNodeCore section**: §1.2 (six functions — none names negotiation), §2 Tier 3 (P4/P5/P6/P7/P10 — outcome is aggregate, not negotiated position), §2 Tier 4 (P8/P9/P11 — moderation and reconsideration, no negotiation tier between), §6.1 (review heuristic — binary M-1 alignment question, no negotiation framing)

**Seventh-function signal**: YES. Structured negotiation is a distinct mode of consensus that is neither vote-aggregation (Tier 3) nor moderation/adjudication (Tier 4). It would constitute a seventh function — or a new intermediate tier — that the six-function model does not accommodate without philosophical extension.

---

## Overall Pattern

**Verdict counts**:
- NOTHING_NEEDED: 0
- REFINEMENT: 0
- SUBSTANTIAL_EDIT: 2 (A-3, E-3)
- PAPERING_OVER: 2 (A-1, E-2)

**Most philosophically significant finding**:

All four gaps circle a single unnamed tension: **CIRISNodeCore's consensus model is participant-bounded but M-1's scope is not**. The MISSION operationalizes M-1 as "route deferrals to people with relevant expertise" and §1.5 explicitly names the participant/humanity distinction as the one designed asymmetry. Every gap that attempts to widen the system's responsiveness — lateral peer-agent routing (A-1), affected-party voice (E-2) — collides with this boundary. These are not implementation omissions; they reveal a philosophical choice the MISSION made (participants-as-the-consensus-set) that may be narrower than M-1 warrants. Implementing A-1 and E-2 without revisiting that choice is papering over it.

**Seventh-function audit**:

Three of the four gaps signal an unnamed seventh (or additional) function:

| Gap | Seventh-function candidate | Status |
|---|---|---|
| A-1 | Inter-agent deferral arbitration (machine-peer routing) | YES — no philosophical home in the six |
| A-3 | Deployment-impact-scaled quorum composition | PARTIAL — extension of function 1 if registry is in-scope; new function if separate gate |
| E-2 | Non-participant affected-party intake | YES — third principal category not named in MISSION |
| E-3 | Structured negotiation tier | YES — neither Tier 3 aggregation nor Tier 4 moderation |

**Recommended action**: Before implementing A-1 or E-2, MISSION_CIRISNodeCore needs an explicit §1.2 addition or §1.5 amendment that either (a) names the new function and grounds it in M-1, or (b) explicitly declines to include non-participant and machine-peer inputs and explains why the participant-bounded model is the right shape for M-1. The stub at `/api/v1/wa/deferral` (E-3) warrants a MISSION amendment naming a negotiation tier between Tier 3 and Tier 4 — this is the one gap where the original design left a marker that philosophy should follow.

---

*End PHILOSOPHICAL_EVAL_CIRISNodeCore.md*
