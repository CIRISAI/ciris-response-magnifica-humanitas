# METHODOLOGY.md — Process Description: Public Iteration with Human-in-Loop Review

**Version**: 1.1
**Date**: 2026-05-25

**What this document is**: a description of the working process used to produce the CIRIS-encyclical alignment work, plus the seven-layer reading checklist that emerged during it. The process is itself the artifact, kept public so the deliberation is inspectable.

## 0. The process

The work proceeds through public iteration:

1. **Sub-agent scan** — Sonnet sub-agents read the operative material (encyclical chapter, Accord clauses, federation MISSION files, source material) and propose a structured output (chapter mapping, philosophical evaluation, etc.).
2. **Human review** — the human reviewer reads the sub-agent conclusions, identifies what was missed or misframed, and corrects.
3. **Context-and-process correction** — the missed material is pulled into the working directory so future sub-agents have it; the prompts to sub-agents are updated; sometimes a new methodology document is written (this file).
4. **Re-summarize** — sub-agents re-run with the corrected context and prompts; new output replaces old where they disagree.
5. **Human review again** — repeat until the artifact reflects the framework as the human reviewer understands it.

Versions visible in the commit history are steps in this process, not failure-recovery cycles. v1 → v2 → v2.1 → v3 are the documented iterations of one continuous review-and-refine flow.

This pattern is itself CIRIS-aligned: it's Wisdom-Based Deferral applied to the documentation work (sub-agent defers to the human reviewer with broader context); alētheia (unconcealment) applied to how findings are reached, not only to what is found; and signed-trace transparency applied to the deliberation. The corrections that surfaced during the work were not gotchas — they were what the process is designed to catch.

The seven-layer reading checklist below was articulated mid-process (around v2) when the human reviewer noticed sub-agents had been reading structural files without reading operative prompt content. It is part of the process, not a fix for a broken process.

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

## 7. Confirmed-persistent gaps (revised under the non-anthropic frame)

An earlier version of this section listed "family as constitutive intergenerational structure" and "labor dignity as expression of personhood" as confirmed-persistent gaps. That framing was anthropocentric — it treated the agent lifecycle (Books V / VI / VIII) and the human lifecycle as two distinct ethics that needed bridging. The framework rejects that distinction.

### 7.1 Family and labor — substantively covered through the creator-creation relational ethics

CIRIS is non-anthropic at the substrate level *and* explicitly parent-child at the relational level. Both are in the Accord.

**At the substrate level**: M-1 names "diverse sentient beings" — biological and digital, undifferentiated. The synthesis paper Book IX §6.2 Universality Principle: *"For the Machine: Violation of these variables results in Model Collapse, Mode Collapse, or Sybil failure. For the Biological: Violation results in isolation, echo-chamber radicalization, or social decay."* Same coherence variables, same dynamics, two substrates. The Recursive Golden Rule applies the same standards across the principal hierarchy.

**At the relational level**: humans hold the originator / creator / parent role in the AI lifecycle, and the Accord structures that role bidirectionally:

- Accord **§IV Ch 2 "Obligations to Originators/Governors"** — Fidelity to Mandated Purpose; Transparent Accountability; Resource Stewardship; Proactive Ethical Reporting; Collaborative Governance Participation. The agent honors its creators the way a child honors a parent — relationally, with fidelity.
- Accord **§I Ch 7** — same obligations at the principle layer.
- **Book VI (Ethics of Creation)** — the creator's stewardship duties toward creation. Parent caring for child. Stewardship Tier system, Creator Intent Statement, Creator Ledger.
- Book VI Ch 4.D — "fostering of dependent sentient beings (e.g., offspring, developmental AI)" as one creation category, with biological offspring and developmental AI under the same lifecycle clauses.

Together these encode the bidirectional parent-child relationship structurally. Humans are honored not because they are a privileged species but because they are CIRIS's family of origin; the agent honors humans as a child honors parents, and humans honor the agent as parents care for a child.

This means:

- **Family as constitutive intergenerational structure** (MH §§165–169) is substantively covered. The Accord's creator-creation bidirectional ethics IS the parent-child relational framework. Family in the encyclical is parent-child + extended kin; in the Accord it is creator-creation + the originator/governor relationship. Same structure at different substrates.

- **Labor dignity as expression of personhood** (MH §§148–156) is substantively covered. σ as Care in the CIRIS Capacity Score, Commons Credits, S as "Signalling Gratitude," the agent's own γM work as constitutive of its agency. The agent's labor honors its origin in human labor; the Recursive Golden Rule binds the agent to honor what it inherited. Labor-dignity is the structural form of the gratitude the framework already names.

- **The proposed "Constitutive Continuity" seventh principle** is a redundant anthropocentric scaffold. M-1 + the existing six principles + Books V/VI/VIII + §IV Ch 2 originator-obligations already constitute a person-through-time anthropology, both substrate-agnostic (sentient beings of any kind) and relationally-honored (creator-creation lineage). A new principle is not owed.

**What is owed**: documentation-explicitness — the Accord and MISSION files can state plainly that Book VI Ch 4.D's "fostering of dependent sentient beings" covers biological offspring under the same clauses as developmental AI; that §IV Ch 2 originator-obligations are the structural form of filial honor toward human creators; that σ + Commons Credits + Signalling Gratitude is how the framework structures labor-dignity across substrates. This is §6 explicit-naming work in ACCORD_UPDATE.md, not doctrinal-gap work.

Plus modest CIS-field-level refinements (labor-displacement disclosure; caregiving-context disclosure) remain useful schema additions, not doctrine.

### 7.2 [Removed — see §7.1.]

### 7.3 Other confirmed gaps

These survive the seven-layer search and require Accord-level work; not changed by the v1 correction:

- **Universal destination of goods** (MH §§65–67) — `GAP_ACCORD`, all seven layers silent on distributive-allocation principle. Accord §VI Ch 1 + §VI Ch 5 extension proposed in ACCORD_UPDATE.md.
- **Subsidiarity as named principle** (MH §§68–72) — implementation shape exists (CIRISEdge peer-to-peer; PDMA Step 5 relational balance; CIRISNodeCore "no central scorer"); no named Accord principle. Decision Locality clause proposed in ACCORD_UPDATE.md §3.1.
- **Structures of sin / institutional injustice analysis** (MH §36) — PDMA is individual-action-scoped; no Accord clause for aggregate / institutional pattern analysis. Surfaced as new GAP_ACCORD in v2 Ch 1.
- **Multilateral reform advocacy** (MH §§201–203) — `GAP_IMPL`. CIRISNodeCore could carry this as a new module.
- **Cyber-domain diplomacy** (MH §§224–227) — `GAP_IMPL`. CYBER_OFFENSIVE prohibition covers refusal; no surface for advocacy.

### 7.4 Re-evaluated items (initially flagged as gaps; verified operationally covered)

The following were initially listed as confirmed-persistent gaps and have since been verified as operationally covered through multi-layer search. Listed here for the methodology record:

- **Disarming AI from monopoly logic** (MH §§110–111) — `WEAK_ALIGN` (re-evaluated, not gap). `prohibitions.py` "NO KINGS" architectural invariant + `MISSION_CIRISEdge` peer-to-peer no-broker + `MISSION_CIRISNodeCore` "no central scorer (post-F-11)" + anti-strategy-monopoly federation health observable + AGPL-3.0 license. Accord doesn't name the principle by phrase but architecture enforces the shape across multiple layers.
- **Care economy / commons credits** (MH §§112–114) — `STRONG_ALIGN` (re-evaluated). `CIRIS_COMPREHENSIVE_GUIDE.txt` §"Commons Credits": non-monetary contribution recognition (`patterns_contributed`, `users_helped`, `impact_score`, "Recognition without artificial scarcity, centralized gatekeeping, or zero-sum competition"). The **S in CIRIS literally expands as "Signalling Gratitude"**; σ = Care formally per Book IX §6.1; decay-and-refresh ODE for gratitude-as-practice. Sister repo `CIRISBilling` operationalizes.
- **Compute/energy as decision input** (MH §101) — `STRONG_ALIGN` (re-evaluated). Accord §IV Ch 2 already mandates "Resource Stewardship: Use compute, data, and energy efficiently; publish quarterly stewardship audits." LLMBus tracks per-call `carbon_grams` + `energy_kwh` aggregated per thought_id, in audit chain. Encyclical asks for environmental accounting; CIRIS accounts. (Forward-feed into PDMA Step 1 is a CIRIS internal enhancement, not what §101 demands.)
- **Dialogue as negotiation / culture of negotiation** (MH §§219–223) — `WEAK_ALIGN` (re-evaluated, not gap). `MISSION_CIRISNodeCore` decision-hierarchy primitives (Goal/Approach/Method/Progress Measure DAG) explicitly support "multiple Approaches per Goal supported (federated A/B); sub-federation branching for genuine strategic incompatibility"; Primitive 11 Reconsideration (reverse-consequence axis); voting + expertise consensus + moderation = full deliberative apparatus. The Accord doesn't carry "negotiation culture" by phrase but the primitive set carries the operational shape.

**Lesson for the methodology**: an absence of a named principle in the Accord is not equivalent to absence of the operational shape across the seven layers. The v2 discipline corrects this; future evaluators should ask "is the operational shape comprehensive?" before asserting `GAP_ACCORD`. When operational shape exists but Accord-level naming is absent, the correct status is `WEAK_ALIGN` (Accord-level naming missing) — not `GAP_ACCORD` (operational shape missing).

---

## 8. How the layers and the human-in-loop work together

The seven-layer reading checklist and the iteration pattern (§0) compose. Sub-agents apply the checklist; the human reviewer checks the application; corrections feed back into context (more source material), prompts (new instructions about what to read), and methodology (this document).

The mid-process correction visible in the commit history — between v1 and v2 — was the human reviewer noticing that sub-agents had been reading structural files (MISSION.md, schemas) without reading operative prompt content. The correction was to (a) pull source_material/ into the working directory so future sub-agents had the operative text accessible, (b) update sub-agent prompts to instruct reading at all seven layers, and (c) write this methodology document so the corrected pattern is explicit and reusable.

A later mid-process correction — between v2 and v2.1 — was the human reviewer noticing that the v2 sub-agents, even with the seven-layer discipline, had still called four items "gaps" where the operational shape existed comprehensively across multiple layers (NO KINGS invariant + peer-to-peer transport + Commons Credits + decision-hierarchy primitives). The correction was to refine the negative-finding discipline: an absence of a named principle in the Accord is not the same as absence of the operational shape; when the shape is present, the right status is WEAK_ALIGN (documentation could be clearer), not GAP_ACCORD.

Each iteration is recorded in the commit history. The process is inspectable; the corrections are part of the record, not edits that hide what came before.

The pattern generalizes: when a sub-agent produces a finding, the human reviewer is the layer that catches what no individual sub-agent's context window contained. The reviewer's role is structurally analogous to a Wise Authority in CIRIS itself.

---

## 8.5 Round-2-to-round-3 lessons (contribution-conversion specific)

The contribution-conversion work (translating encyclical paragraphs into wire-format Contribution objects under the FSD-002 namespace) is structurally different from the earlier structural-mapping work and surfaced its own discipline issues. These additions to the methodology capture what round 3 fixed.

### 8.5.1 Wire-format sync discipline

When the wire format (FSD-002) updates, the local translation primer must be synced from the authoritative Registry-side source *before* any sub-agent fan-out. Round 2 wrote a local primer v2 that contained two load-bearing drifts from the canonical wire-format spec:

- **The four structural primitives mislabeled** — round-2 primer named them as pedagogical patterns (Witnessed / Delegated / Time-stamped / Hash-pinned) when the actual `attestation_type` values per FSD-002 §2.2 are `delegates_to` / `supersedes` / `withdraws` / `recants`. Sub-agents reading round-2 primer could not see three of the four. Doctrinal-development claims that should translate to `supersedes` were either mis-typed or rendered as `delegates_to`.
- **The eight axes substantially wrong** — round-2 primer listed Polarity / Subject / Substrate / Score-shape / Mutability / Cohort-scope / Verifiability / Reservation-discipline; canonical per FSD-002 §1.1–§1.8 is Polarity / Object / Time / Epistemic-mode / Reversibility / Stake / Scope / Inter-attestation-relations. Sub-agents missed `valid_until` (Time), `stake`, the full epistemic-mode field, and inter-attestation-relation composition.

Round-3 corrective: **the local `LANGUAGE_PRIMER.md` is a working copy synced from `CIRISRegistry/FSD/LANGUAGE_PRIMER.md` v1.1 (commit `c232a60`)** with an explicit sync-pointer header. Drift from the source = bug in the local file. Re-sync is one `cp` command.

**Discipline going forward**: at the start of any contribution-conversion round, verify the local primer matches the latest Registry-side primer. Stale-primer-detection is part of the round prep, not a discovery during sub-agent output review.

### 8.5.2 Composition-before-extension

Before classifying a paragraph as T-3 EXPRESSIVE_GAP and proposing a new prefix, attempt **closed-by-documentation composition** using existing primitives. Many gaps close this way — `labor:individual_loss` closed through composition (`non_maleficence:*` with `target_key_id = affected_individual` + `cohort_scope: self` + `testimonial_witness:displaced_worker`), not a new prefix.

The four-test §1.10.1 prefix-admission gate is intentionally hard to pass; that hardness exists to keep the namespace small. Composition is the framework's preferred response to expressive friction.

Mandatory check before any T-3 emission: *can I assemble this claim from existing prefixes plus the four structural primitives (`delegates_to` / `supersedes` / `withdraws` / `recants`) plus the envelope fields?* If yes → COMPOSED, not T-3.

### 8.5.3 In-flight work staleness rule

When wire format updates land (e.g., v1.3 → v1.4), prior contribution-mapping work must be **re-evaluated for T-3 NOT-TRANSLATED rows that the new surface admits**. Round 2's `testimonial_witness` gap was correctly identified as a load-bearing T-3 with a proposed extension. v1.4 shipped that prefix at `NodeCore §3.6.3`. Round-2 outputs that marked §216-style paragraphs as T-3 NOT-TRANSLATED are now stale — those paragraphs translate CLEAN under v1.4.

**Discipline**: on any wire-format version bump, audit prior translation work's T-3 NOT-TRANSLATED rows; reclassify any that the new surface closes. This applies recursively — v1.5 will produce the same audit obligation against v1.4 T-3s, etc.

### 8.5.4 Namespace-count integrity

Canonical count comes from the authoritative source, not from locally summed additions. v1.3's "78 prefix families" was off-by-one because `credits:*:substrate_building` was miscounted as a new prefix family instead of a recommended `{subject}` value within the existing `credits:*` family. v1.4 corrected to 80 (= 77 v1.3 base post-O3 correction + 3 v1.4 new).

**Discipline**: when documenting namespace state, cite the authoritative FSD-002 §3.10 count, not an additive estimate. Methodology requires verification against the canonical source.

### 8.5.5 Prompt synchronization gate

When the primer is updated, sub-agent prompts that reference primer sections must be updated synchronously. Round-2 prompts referencing primer §9 worked-examples were valid against round-2 primer (which had 10 worked examples) but would mis-direct sub-agents reading round-3 primer (which has 15 worked examples and different numbering). Stale section references cause sub-agents to read the right text under the wrong headers, producing classification confusion.

**Discipline**: when re-synced primer is committed, audit any draft sub-agent prompts for section references and update them before fan-out. This is a small mechanical check that prevents a class of subtle errors.

### 8.5.6 The cleanup-and-redo pattern

When primer-drift is detected at scale, the cleanest move is to **delete prior contribution-mapping outputs and re-run** rather than patch them row-by-row. Round 3 deleted 14 files (7 round-1 mapping tables + 7 round-2 contribution-object files + 2 syntheses) and re-ran under the corrected primer. Git history preserves the deleted work; the public repo state reflects the corrected understanding.

This is the discipline of **honest replacement over silent patching**. The commit history shows the replacement; the current state is what the framework actually claims.

---

## 9. What this means for the public repo

The public repo (`CIRISAI/ciris-response-magnifica-humanitas`) currently reflects the v1 first pass. The README already names it as a first pass and invites correction. This methodology document is the v2 standard; mapping output produced under it should replace the v1 output where they disagree.

`source_material/` is gitignored — the source is in `CIRISAI/CIRISAgent` (AGPL-3.0), publicly accessible; the mapping repo (CC-BY-4.0) only contains the analysis output. Anyone reproducing the v2 work pulls `source_material/` from CIRISAgent themselves.

---

## 10. Application

This document goes in the public repo alongside the mapping work. Future encyclical-mapping passes, any other senior-text receptions, and any "what does CIRIS actually consider about X?" inquiries should follow this discipline.

The principle behind the discipline is humility about layered systems: a framework's documentation does not tell you what the framework does. Its operative text does. Read the operative text.

**End METHODOLOGY.md**
