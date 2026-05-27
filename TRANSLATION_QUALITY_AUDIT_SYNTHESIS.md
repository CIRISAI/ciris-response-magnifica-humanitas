# Translation-quality audit — synthesis across four batches

**Date**: 2026-05-27
**Scope**: Phase 4 of `GOVERNANCE_FABRIC_MAPPING_STANDARD` — diagnostic calibration of wire-envelope translation fidelity across `magnifica_humanitas_v1` + `eu_hleg_v1` + `ieee_ead_v1` + `asean_guide_v1`
**Per-batch audits**: [`TRANSLATION_AUDIT_MH.md`](TRANSLATION_AUDIT_MH.md), [`TRANSLATION_AUDIT_EU_HLEG.md`](TRANSLATION_AUDIT_EU_HLEG.md), [`TRANSLATION_AUDIT_IEEE_EAD.md`](TRANSLATION_AUDIT_IEEE_EAD.md), [`TRANSLATION_AUDIT_ASEAN.md`](TRANSLATION_AUDIT_ASEAN.md)
**Cross-comparison**: [`FOUR_BATCH_OVERLAP_ANALYSIS.md`](FOUR_BATCH_OVERLAP_ANALYSIS.md)

---

## 0. Framing — what this audit IS and what it is NOT

**This is diagnostic for calibration, not break/fix.** Translation from natural-language governance prose to wire envelopes captures STRUCTURE, not fine grain. We will always lose some detail. The audit's job is to characterize and quantify the systematic loss patterns so the framework's structural-evidence claims are honestly bounded — not to fix individual envelopes or claim faithfulness we don't have.

Sampling methodology (per batch): ~15-20 atomic units, spanning all sections and all four verdict categories (clean / composed / partial / not-translated). Auditors read source paragraphs in natural context FIRST, formed independent readings, then compared to wire envelopes. Classification scheme: `faithful` / `partial-distortion` / `drift` / `over-reach` / `under-reach`.

## 1. Aggregate faithfulness across 67 sampled units

| Batch | Sampled | Faithful | Partial-distortion | Drift | Over-reach | Under-reach |
|---|---|---|---|---|---|---|
| MH | 15 | 1 (~8%) | 5 | 2 | 0 (+ 2 leaning) | 4 |
| EU HLEG | 19 | 14 (74%) | 2 | 0 | 1 | 2 |
| IEEE EAD | 16 | 13 (81%) | 1 | 0 | 0 | 2 |
| ASEAN | 17 | 10 (59% strict) | 2 | 0 | 3 | 2 |
| **Total** | **67** | **38 (57%)** | **10 (15%)** | **2 (3%)** | **4 (6%)** | **10 (15%)** |

Plus correctly-bowed not-translated units across all four batches: ~10 of ~10 sampled (T-1 and T-2 verdicts justified in every case audited).

### Per-batch fidelity profile (one paragraph each)

- **MH** — Structural-shape fidelity, NOT propositional fidelity. The wire reliably captures *family + scope per paragraph* and uses structural primitives (`supersedes` for doctrinal development) correctly. It cannot support: reconstruction of multi-item enumerations; preservation of conditional/enabling-clause structure; polarity-faithful translation of diagnostic paragraphs; tradition-specific reasoning sequences. Headline: the MH wire is good evidence for *what kind of claim* MH makes; weak evidence for *exactly* what MH asserts. **Lowest faithfulness of the four batches** — reflects the encyclical genre (dense, multi-mechanism, theologically conditioned), not a translator error.
- **EU HLEG** — Highest faithfulness (74% strictly faithful, no drift). Best property: honest `nuance_lost` self-annotation by the translator. Weakest properties: namespace-granularity at concrete-action-enumeration sites (six-verb manipulation lists collapse to one prefix); occasional prefix-discovery slips. The Explicability principle's taxonomic mismatch with CIRIS's 6 Accord principles is handled correctly via composition rather than prefix invention.
- **IEEE EAD** — Very high faithfulness (81%); zero drift; zero over-reach. Composition-before-extension consistently applied. The Ch5 Affective Computing cross-source conflict (licensure-gated beneficiary-deception in search/rescue vs CIRIS categorical DECEPTION_FRAUD) is REAL, not over-stated — confirmed by independent reading of the source. Ch11 Law (longest chapter) scope-management is good — no over-compression detected. The 4 affective-computing T-3 candidates genuinely require new prefixes; composition cannot reach them.
- **ASEAN** — Moderate faithfulness (59% strict, 82% with residual-rescue). Distinct failure mode: **softness-erosion**. ASEAN's voluntary "should/consider/can" modals systematically compress to score 1.0 / mutability:constitutional whenever the topic touches a CIRIS constitutional anchor. The framework's stricter posture wins by default — three specific cases confirmed (§A.2.1 sandbox staging; §A.4.18 explainability fallback; §A.5.3 opt-out). HITL/HOTL/HOOTL → `accountability:human_in_control` mapping is correct (not `fidelity:*`).

## 2. The five recurring loss patterns (calibration profile)

Across all 67 sampled units the auditors consistently identified five systematic loss patterns:

### 2.1 Enumeration compression
**Pattern**: multi-item enumerations in the source (e.g., MH's six dignity-violating verbs; EU HLEG's six rights families; IEEE EAD's four mitigation strategies) collapse to ≤2 envelopes per paragraph because of the two-primitive-cap discipline. Granular axes survive only in context fields.
**Effect**: a consumer querying for "the third item in MH's manipulation list" cannot reconstruct it from wire envelopes alone.
**Quantification**: affects ~5/67 sampled units (~7%); structural across all four batches.
**Implication for structural-evidence claims**: the framework can faithfully assert "MH attests `prohibited:manipulation_coercion`" but cannot assert "MH's enumeration of manipulation kinds is X". Bound claims accordingly.

### 2.2 Conditional/enabling-clause flattening
**Pattern**: scope-qualifying clauses ("permitted when X, prohibited when Y"; "shall do A unless B"; "only in context Z") flatten into unconditional polarity scores plus context-block prose. To recover the conditional, a consumer must read multi-attestation pairs jointly.
**Effect**: under-reading single envelopes leads to mis-stating the source's actual disposition. EU HLEG §C critical-concerns (identification-yes / mass-surveillance-no carve-outs) and IEEE EAD Ch5 (beneficiary-deception carve-outs) are the densest sites.
**Quantification**: affects ~10/67 sampled units (~15%); MH and IEEE EAD show this most.
**Implication**: the wire format requires multi-attestation reading discipline for any document that uses carve-outs — which is essentially all senior governance documents.

### 2.3 Modal-strength / deontic-gradient compression
**Pattern**: "shall" vs "should" vs "may" vs "consider" all compress to polarity ±1.0 plus mutability tag. Hortative-vs-obligatory force is lost.
**Effect**: ASEAN's voluntary modals get silently elevated to constitutional strength. EU HLEG's "should always" vs "should" disappears. MH's papal-register "we exhort" vs "the Church teaches" flattens.
**Quantification**: most acute in ASEAN (3 confirmed softness-erosion cases — §A.2.1 sandbox; §A.4.18 explainability fallback; §A.5.3 opt-out); recurring across all four batches.
**Implication**: when comparing convergent attestations across batches, the wire format will systematically *exaggerate agreement* between hard-rule and soft-rule documents on the same prefix family.

### 2.4 Taxonomic mismatch handling
**Pattern**: where the source's principle taxonomy doesn't 1:1 map CIRIS's (e.g., EU HLEG Explicability has no 1:1 CIRIS principle; CIRIS's 6 vs ASEAN's 7 vs IEEE's 8), composition is used in lieu of prefix invention. This is the correct discipline but it scatters the source's unified principle across multiple wire prefixes.
**Effect**: a reader looking for "the EU HLEG Explicability attestation" finds a composed envelope across `integrity:*` + `fidelity:*` + `transparency_log:*` — faithful in operative content, but the unified principle as a concept is gone.
**Quantification**: load-bearing at every cross-document principle-correspondence point (see Phase 3 §3).
**Implication**: cross-document principle-correspondence tables (Phase 3 §3) are essential reading; raw prefix-family overlap counts (Phase 3 §2) understate the methodology's discipline.

### 2.5 Polarity inversions on diagnostic paragraphs
**Pattern**: source paragraphs that *describe a problem* (crisis-description, lament, warning) sometimes get rendered as wire envelopes that *advocate the solution* — polarity flips from "this is bad" to "the opposite is good".
**Effect**: most acute single failure mode found. MH §201 ("crisis-description rendered as positive reform-advocacy") and one MH §125 "domain-mismatch forced fit" both fall here.
**Quantification**: 2/67 sampled units (~3%); concentrated in MH (encyclical lament passages).
**Implication**: future translation passes should add a "diagnostic vs prescriptive" pre-classification step.

## 3. The structural-evidence claim, honestly bounded

Phase 3 surfaced 16 STRONG-4 tier prefix families (attested by all four batches) and 6 STRONG-3 tier. Given the Phase 4 calibration findings, what can the framework honestly claim?

### Strong claim (defensible)
> The CIRIS wire format v1.4 applied to four institutionally-distinct senior governance frameworks (religious magisterium + governmental advisory + technical society + multilateral political body) exhibits convergent attestations on 22 structural dimensions. The convergence is non-redundant: each batch contributes a distinct shape of normative load onto the same prefix families. This is structural evidence that the framework's principle scaffolding is not an artifact of any one tradition.

### Weaker claim (not defensible without bounding)
> "The four documents agree on X."
For most X, the wire-format envelopes systematically exaggerate agreement because of softness-erosion (§2.3), conditional flattening (§2.2), and taxonomic-mismatch handling (§2.4). Convergent prefix attestations indicate *the same structural concern was raised by all four sources*, not that the sources prescribe the same response or hold the same strength of obligation.

### Limit-of-evidence claim (also defensible)
> Where the four documents *differ*, the wire format honestly surfaces those differences as cross-source conflicts (1 direct conflict + 4 tensions surfaced; ~0.5% rate). The translation does not silently average disagreements into false consensus. The IEEE Ch5 vs CIRIS DECEPTION_FRAUD conflict is real and load-bearing.

## 4. What the audit DID NOT do (scope honesty)

- We did NOT verify that every wire envelope's content is in the source.
- We sampled ~67 units out of ~921 total (~7% coverage). Findings extrapolate; they do not enumerate.
- We did NOT systematically check whether sub-agents missed paragraphs entirely (only sampled units that DID get envelopes; entirely-omitted source content is invisible to this method).
- Audit sub-agents are themselves LLMs subject to the same translation-loss patterns they audit. Methodological humility applies: this is calibration evidence, not ground-truth verification.

## 5. Implications for next-step work

### 5.1 For the federation runtime
Consumers of attestation queries should be aware that:
- STRONG-tier prefix-family overlap means structural-shape agreement, not propositional agreement.
- Convergent attestations from differently-soft sources will appear identical in score; the `mutability` tag and any `nuance_lost` context-block content carries the disagreement.
- Composed envelopes (multi-prefix translations of a single source paragraph) should be read jointly; single-prefix querying under-represents.

### 5.2 For v1.5+ wire format
Five candidates surfaced for explicit consideration:
1. **Two-primitive-cap relaxation** for enumeration-dense paragraphs (e.g., MH multi-mechanism enumerations).
2. **Conditional/enabling-clause structural primitive** (e.g., `conditional_on:{predicate}` linker between attestations).
3. **Soft-modal preservation field** (explicit deontic-strength axis distinct from polarity).
4. **Diagnostic-vs-prescriptive paragraph type tag** (pre-classification to prevent polarity inversion).
5. **Reinforced T-3 candidates from Phase 3**: `goal:planet` (MH + IEEE×2) and partner-role specialization patterns (IEEE + ASEAN).

These are NOT urgent — composition-before-extension still holds. They are documented for v1.5+ workshop consideration.

### 5.3 For Phase 5 publication
Each batch should be published as a `bootstrap_batch` with:
- Its manifest, contribution-objects files, and per-batch audit file
- The four-batch overlap analysis as a separate cross-batch artifact
- This synthesis as the documented calibration profile

Downstream consumers reading bootstrap_batch attestations get the structural-evidence claim AND the bounding it requires in one referenced set.

## 6. Posture note

We are not claiming our primitives ARE these documents' meaning. We are claiming that the wire format captures faithful structural correspondence sufficient to support cross-document overlap analysis, with the loss patterns above explicitly characterized. Senior governance documents — Pope Leo XIV's encyclical, the HLEG's deliberatively-produced guidelines, the IEEE Global Initiative's 700+ contributor consensus, the ASEAN Digital Ministers' endorsement — say things the wire format will not fully carry. That is the cost of structural composability; this audit names the price.
