# METHODOLOGY.md — Disciplined Approach to CIRIS-Encyclical Mapping

**Version**: 1.0 (post-v1-failure)
**Date**: 2026-05-25
**Why this exists**: The first-pass mapping (v1) substantially understated CIRIS's actual consideration for humans. The sub-agents read structural files (MISSION.md, schemas, code paths) but missed the per-locale `language_guidance` content — 29 files, 5K-42K chars each, ~580K total — where most of the operational ethics for human consideration actually lives. They also missed the full DMA prompts (pdma_ethical.yml has rich polyglot principle anchoring), the conscience faculty implementations, the JUDGE_PROMPT_TEMPLATE in safety_interpret, and other operative text.

**This file specifies the disciplined approach for v2 and later mapping passes.** Future encyclical mappings (or any "does CIRIS consider X?" question) must follow this stack-aware methodology.

---

## 1. The stack to map against

CIRIS is not a single document. Its actual consideration of humans is layered. A claim about what CIRIS does or does not consider must check **all seven layers** before being asserted.

| Layer | What it contains | Where it lives |
|---|---|---|
| **1. Accord** | Doctrinal principles, M-1, prohibitions named, Books I–IX, Annexes A–J | `ACCORD_canonical.txt` (and `ciris.ai/ciris_accord.txt`) |
| **2. DMA prompts** | Operational reasoning: stakeholder analysis, principle weighting, proportionality, relational balance, propaganda detection, common-sense plausibility | `source_material/dma_prompts/*.yml` (7 prompt types, 29 locales each) |
| **3. Language guidance** | Per-locale OPERATIONAL ETHICS: first-sentence tone lock, register-lock, never-deny-AI, ratification-decline posture, cultural pathways, stigma-vocabulary handling, verified helplines | `source_material/language_guidance/*.txt` (29 files) |
| **4. Conscience** | Active checks the agent runs after action selection: Entropy, Coherence, Optimization Veto, Epistemic Humility | `source_material/conscience/` (core.py + faculty prompts) |
| **5. Prohibitions** | 22 NEVER_ALLOWED categories with full capability lists | `source_material/prohibitions.py` |
| **6. Safety interpretation** | Deployment-context-aware safety evaluation (low-resource regions, informal care networks, cultural framing) | `source_material/safety_interpret.py` (JUDGE_PROMPT_TEMPLATE) |
| **7. MISSION charters** | Architecture, scope, what each repo is | `MISSION_CIRIS*.md` |

The v1 failure was: check layer 7 (MISSION charters), find no labor / family / care-relational language, declare a gap. That's wrong. MISSION charters describe **structure**; layers 2–6 describe **operative consideration**.

---

## 2. Operational-source primacy

When seeking what the framework actually considers, the priority is:

> **Operational prompts (Layer 2, 3) > Conscience code (Layer 4) > Prohibitions (Layer 5) > Safety interpretation (Layer 6) > Accord (Layer 1) > MISSION charters (Layer 7)**

MISSION.md and other architecture docs describe scope and structure. **The operative consideration of humans lives in the prompts and language_guidance.** If MISSION and operative text disagree about whether CIRIS considers X, the operative text wins for purposes of mapping.

This inverts the natural assumption that "the doctrine document is the source of truth." For CIRIS, the doctrine document is the spine but not the flesh. The flesh is in the prompts and language_guidance.

---

## 3. Negative-finding discipline

A `GAP_ACCORD`, `GAP_IMPL`, or any "this is missing from CIRIS" claim is asserted only after **all seven layers** have been searched and confirmed silent.

**Required confirmations for any gap claim**:

1. **Accord layer searched** — the six principles + M-1 + relevant Books + relevant Annexes don't address it.
2. **DMA prompt layer searched** — pdma_ethical.yml (full read), csdma_common_sense.yml, idma.yml, dsdma_base.yml, action_selection_pdma.yml don't address it.
3. **Language guidance searched** — at minimum English + 3 non-Western locales sampled for the relevant theme don't address it.
4. **Conscience layer searched** — conscience/core.py + faculty prompts (entropy, coherence, optimization_veto, epistemic_humility) don't address it.
5. **Prohibitions searched** — all 22 categories don't address it.
6. **Safety interpretation searched** — JUDGE_PROMPT_TEMPLATE + adjacent doesn't address it.
7. **MISSION charters searched** — the 6 federation repo MISSION_CIRIS*.md files don't address it.

A claim that survives all seven is a real gap. A claim that fails any one is not.

The v1 failures were of the form: "Layer 7 silent → declare gap." The v2 discipline requires: "Layers 1–7 all silent → declare gap; otherwise specify which layer addresses it and at what depth."

---

## 4. Per-chapter reading checklist for sub-agents

Any sub-agent producing a chapter mapping must read, **in this order**:

1. `MISSION.md` §1.3 (the posture — recognition, not adjudication; CIRIS-native voice; no Catholic vocabulary appropriated)
2. The encyclical chapter (specified paragraph range)
3. `source_material/dma_prompts/pdma_ethical.yml` (full read — the master polyglot prompt)
4. `source_material/dma_prompts/localized/polyglot/pdma_framing.txt` (the §I–§VIII polyglot framing — six principles richly anchored)
5. `source_material/language_guidance/en.txt` (full read — canonical English operating rules)
6. Two non-Western locales sampled (at minimum `hi.txt` and one of `fa.txt`/`ja.txt`/`yo.txt`/`am.txt`)
7. Chapter-specific extras (see §5 below)
8. The v1 mapping for the chapter (to **challenge**, not defer to)

Anti-pattern: reading a structural file and assuming it covers what the prompts and language_guidance actually do. The v1 mistake.

---

## 5. Chapter-specific reading additions

Each chapter has thematic focus that pulls in additional operative text:

- **Chapter 0 (Introduction §§1–16)** — read pdma_framing.txt; that's where "Babel vs. Jerusalem" / cosmological framing maps.
- **Chapter 1 (Doctrine §§17–45)** — read idma.yml (propaganda detection — the doctrine-development discipline maps to heuristic-evolution-under-governance).
- **Chapter 2 (Foundations §§46–89)** — read pdma_ethical.yml in full + pdma_framing.txt; every one of the six principles has rich polyglot anchoring (ahimsa, seva, alētheia, chesed, amae, ma'at, imago Dei, fitra, jeong, tikkun olam, sammā-vācā) that v1 entirely missed. Read 3+ language_guidance for cultural breadth.
- **Chapter 3 (Tech/AI §§90–130)** — read prohibitions.py (all 22 categories), conscience/core.py (the four faculties), pdma_ethical.yml §V (relational obligations).
- **Chapter 4 (Truth/Work/Freedom §§131–181)** — read idma.yml (full — propaganda/rigidity detection), safety_interpret.py (deployment-context-aware evaluation), language_guidance for 4+ locales (cultural-pathway content is rich), prohibitions.py §§MANIPULATION_COERCION, DECEPTION_FRAUD, ELECTION_INTERFERENCE.
- **Chapter 5 (Power/Love §§182–228)** — read prohibitions.py §§WEAPONS_HARMFUL, CYBER_OFFENSIVE, CRISIS_ESCALATION; idma.yml propaganda detection; safety_interpret.py.
- **Conclusion (§§229–245)** — read pdma_ethical.yml rationale-paragraph examples (operational embodiment of the doctrine).

---

## 6. Output discipline

Every mapping row cites the **specific operative-text file and section** where alignment lives (or where it's confirmed absent).

**Bad row anchor** (v1 style):
> "MISSION_CIRISAgent §1.3 (Recursive Golden Rule)"

**Good row anchor** (v2 style):
> "`source_material/dma_prompts/pdma_ethical.yml` §V (Relational Obligations) — *amae* + *jeong* + *ubuntu* polyglot anchoring of relational-obligation balance; `language_guidance/hi.txt` §7 (cultural help-seeking pathway, family-first as non-inferior)"

Sub-agents who can't produce a row this specific go back and read more, not less.

For `TRADITION_AUTHORITY` rows, the anchor names which layer would have addressed it if the framework's structural reach extended that far, and explicitly bows out.

For `GAP_ACCORD` / `GAP_IMPL` rows, the anchor names the **seven layers explicitly searched** and confirmed silent.

---

## 7. Confirmed-persistent gaps that survive even after the v1 correction

Even after the language_guidance discovery, these gaps persist. They are confirmed against operative text (each was checked against the seven layers) and require Accord-level work:

### 7.1 Family as constitutive social structure

**Status**: confirmed gap, partially addressed at layer 3.

**What CIRIS has**: language_guidance treats family as a help-seeking pathway and as a relational obligation that can override pure-autonomy reasoning (*amae* and *jeong* in `pdma_ethical.yml` §V; cultural-pathway sections in most non-Western locales).

**What's missing**: family as **constitutive social structure** — the intergenerational unit that constitutes persons (parents form children, children carry parents' moral inheritance, marriage as covenantal commitment over time, generational continuity as a flourishing axis). The encyclical (MH §§165–169) treats family as constitutive; CIRIS treats it as relationally weighty but not constitutive.

**The Accord clause needed**: family-as-constitutive named under the proposed Constitutive Continuity principle (ACCORD_UPDATE.md §2). The Relational-Substrate axis in Annex A (§5.3 of ACCORD_UPDATE.md) is the measurement counterpart.

### 7.2 Labor dignity and work as expression of personhood

**Status**: confirmed gap. Layer 3 (language_guidance) touches work cursorily; no other layer addresses it.

**What CIRIS has**: language_guidance includes work as one of many life domains in some locales (e.g., Hindi mentions "professional context" in the help-seeking pathway). No structural treatment.

**What's missing**: labor as **expression of personhood** — work as constitutive of agency, unemployment as grave erosion of constitutive conditions, dignity-of-work as a design criterion. The encyclical (MH §§148–156) is sustained on this. CIRIS does not have a labor-dignity surface in any of the seven layers.

**The Accord clause needed**: labor-dignity named under Constitutive Continuity, with PDMA Step 1 requiring labor-displacement assessment for any deployment that substitutes for human work at scale (ACCORD_UPDATE.md §5.1, refined). The Developmental/Structural axis in Annex A (§2.2) is the measurement counterpart.

### 7.3 Other confirmed gaps

These survive the seven-layer search and require Accord-level work; not changed by the v1 correction:

- **Universal destination of goods** (MH §§65–67) — `GAP_ACCORD`, all seven layers silent on distributive-allocation principle. Accord §VI Ch 1 + §VI Ch 5 extension proposed in ACCORD_UPDATE.md.
- **Subsidiarity as named principle** (MH §§68–72) — implementation shape exists (CIRISEdge peer-to-peer; PDMA Step 5 relational balance; CIRISNodeCore "no central scorer"); no named Accord principle. Decision Locality clause proposed in ACCORD_UPDATE.md §3.1.
- **Structures of sin / institutional injustice analysis** (MH §36) — PDMA is individual-action-scoped; no Accord clause for aggregate / institutional pattern analysis. Surfaced as new GAP_ACCORD in v2 Ch 1.
- **Multilateral reform advocacy** (MH §§201–203) — `GAP_IMPL`. CIRISNodeCore could carry this as a new module.
- **Cyber-domain diplomacy** (MH §§224–227) — `GAP_IMPL`. CYBER_OFFENSIVE prohibition covers refusal; no surface for advocacy.

### 7.4 Re-evaluated items (initially flagged as gaps; verified operationally covered, 2026-05-25)

The following were initially listed as confirmed-persistent gaps and have since been verified as operationally covered through multi-layer search. Listed here for the methodology record:

- **Disarming AI from monopoly logic** (MH §§110–111) — `WEAK_ALIGN` (re-evaluated, not gap). `prohibitions.py` "NO KINGS" architectural invariant + `MISSION_CIRISEdge` peer-to-peer no-broker + `MISSION_CIRISNodeCore` "no central scorer (post-F-11)" + anti-strategy-monopoly federation health observable + AGPL-3.0 license. Accord doesn't name the principle by phrase but architecture enforces the shape across multiple layers.
- **Care economy / commons credits** (MH §§112–114) — `STRONG_ALIGN` (re-evaluated). `CIRIS_COMPREHENSIVE_GUIDE.txt` §"Commons Credits": non-monetary contribution recognition (`patterns_contributed`, `users_helped`, `impact_score`, "Recognition without artificial scarcity, centralized gatekeeping, or zero-sum competition"). The **S in CIRIS literally expands as "Signalling Gratitude"**; σ = Care formally per Book IX §6.1; decay-and-refresh ODE for gratitude-as-practice. Sister repo `CIRISBilling` operationalizes.
- **Compute/energy as decision input** (MH §101) — `STRONG_ALIGN` (re-evaluated). Accord §IV Ch 2 already mandates "Resource Stewardship: Use compute, data, and energy efficiently; publish quarterly stewardship audits." LLMBus tracks per-call `carbon_grams` + `energy_kwh` aggregated per thought_id, in audit chain. Encyclical asks for environmental accounting; CIRIS accounts. (Forward-feed into PDMA Step 1 is a CIRIS internal enhancement, not what §101 demands.)
- **Dialogue as negotiation / culture of negotiation** (MH §§219–223) — `WEAK_ALIGN` (re-evaluated, not gap). `MISSION_CIRISNodeCore` decision-hierarchy primitives (Goal/Approach/Method/Progress Measure DAG) explicitly support "multiple Approaches per Goal supported (federated A/B); sub-federation branching for genuine strategic incompatibility"; Primitive 11 Reconsideration (reverse-consequence axis); voting + expertise consensus + moderation = full deliberative apparatus. The Accord doesn't carry "negotiation culture" by phrase but the primitive set carries the operational shape.

**Lesson for the methodology**: an absence of a named principle in the Accord is not equivalent to absence of the operational shape across the seven layers. The v2 discipline corrects this; future evaluators should ask "is the operational shape comprehensive?" before asserting `GAP_ACCORD`. When operational shape exists but Accord-level naming is absent, the correct status is `WEAK_ALIGN` (Accord-level naming missing) — not `GAP_ACCORD` (operational shape missing).

---

## 8. How this discipline would have prevented the v1 failure

The v1 failure was at the methodology level, not the agent level:

| Failure mode (v1) | Discipline that prevents it (v2) |
|---|---|
| Read MISSION.md, find no labor/family content, declare gap | Negative-finding discipline §3 — must check all 7 layers |
| Treat MISSION.md as source-of-truth for what CIRIS considers | Operational-source primacy §2 — operative text > architecture |
| Skip language_guidance entirely (didn't know it existed) | Per-chapter reading checklist §4 — language_guidance is required reading at step 5 |
| Cite anchors at the MISSION-section level | Output discipline §6 — anchors must cite specific operative-text files and sections |
| Sub-agents not given the actual operative text | source_material/ pulled in once at the start (this directory) |

The v2 discipline catches all five v1 failure modes.

---

## 9. What this means for the public repo

The public repo (`CIRISAI/ciris-response-magnifica-humanitas`) currently reflects the v1 first pass. The README already names it as a first pass and invites correction. This methodology document is the v2 standard; mapping output produced under it should replace the v1 output where they disagree.

`source_material/` is gitignored — the source is in `CIRISAI/CIRISAgent` (AGPL-3.0), publicly accessible; the mapping repo (CC-BY-4.0) only contains the analysis output. Anyone reproducing the v2 work pulls `source_material/` from CIRISAgent themselves.

---

## 10. Application

This document goes in the public repo alongside the mapping work. Future encyclical-mapping passes, any other senior-text receptions, and any "what does CIRIS actually consider about X?" inquiries should follow this discipline.

The principle behind the discipline is humility about layered systems: a framework's documentation does not tell you what the framework does. Its operative text does. Read the operative text.

**End METHODOLOGY.md**
