# GOVERNANCE_FABRIC_MAPPING_STANDARD.md — Mapping Governance Documents to CIRIS Contributions

**Version**: 0.1 (proposal; not adopted)
**Status**: Draft — for review by CIRISRegistry. Candidate to land as `FSD-003` at CIRISRegistry once stable.
**Date**: 2026-05-27
**Companion documents**: `LANGUAGE_PRIMER.md` (Registry-synced v1.1); `METHODOLOGY.md` §0 + §8.5 (iteration process and primer-drift discipline); `FSD-002 §10.4` (bootstrap-contributions pattern, content-neutral).

This document proposes a **repeatable, content-neutral standard** for mapping any senior governance document (moral / legal / regulatory / philosophical) into CIRIS Contribution wire envelopes, producing a structured graph that supports:

1. **Alignment detection** between multiple governance documents — where they agree.
2. **Conflict detection** between governance documents — where they disagree at the wire level.
3. **Regional composition** for agent deployments — surfacing the relevant local + global governance graph + named conflicts.
4. **Audit-trail provenance** from any agent decision back to its governance sources.

The *Magnifica Humanitas* mapping (three iterations: round 1 structural, round 2 contribution-language, round 3 wire conversion under FSD-002 v1.4) is the **first deployment of this standard**. The standard generalizes the methodology into a reusable form.

---

## 1. Purpose and scope

### 1.1 Purpose

CIRIS's federation wire format admits structured Contributions from many sources. The wire format itself is content-neutral — `prohibited:weapons_harmful` polarity -1 means the same thing regardless of whether the attester is an encyclical, an EU regulation, an indigenous-rights framework, or a corporate-policy statement.

This standard ensures that:

- Senior governance documents (regardless of tradition or origin) are mapped to CIRIS Contributions through a **uniform process**
- The resulting Contribution graph is **queryable** — alignment and conflict between sources can be computed by following edges
- Agent deployments **compose multiple sources** appropriate to their jurisdiction and context, with conflicts surfaced explicitly rather than averaged silently
- The **provenance trail** from any decision to its source documents is intact and inspectable

### 1.2 In-scope governance documents

The standard applies to any senior governance text that asserts ought-claims (about persons, agents, institutions, or technologies) and that someone in the federation wants to make available as Contributions. Examples:

- **Religious / moral**: *Magnifica Humanitas* (deployed); *Caritas in Veritate*; *Laudato Si'*; Reformed / Lutheran / Orthodox social-doctrine documents; Buddhist economic-justice texts; Islamic jurisprudence on AI; Jewish bioethics.
- **Regulatory**: EU AI Act; NIST AI RMF; ISO/IEC 42001; ISO/IEC 23894; UK AI white paper; Singapore Model AI Governance; Canada AIDA; China algorithmic recommendation rules; Brazil PL 2338.
- **International**: Council of Europe AI Convention (CETS 225); Hiroshima AI Process; UNESCO Recommendation on AI Ethics; UN Guiding Principles on Business and Human Rights.
- **Indigenous / community**: CARE Principles for Indigenous Data Governance; First Nations Information Governance Centre OCAP principles.
- **Philosophical tradition (deeply read)**: Ubuntu philosophy of personhood; Confucian ethics; Stoic *physis*; secular humanist consensus documents.

### 1.3 Out-of-scope

- Technical standards without normative content (e.g., HTTP RFCs)
- Private corporate policies (these can flow as Contributions but use a different framing — they are deployment-context inputs, not governance documents)
- Single-author opinion pieces (these may inform the federation through Vote / Reconsideration, but are not bootstrap-source-of-record)

A bootstrap candidate must have **standing in some community** — a magisterium, a legislature, a treaty body, a recognized indigenous council, an established philosophical tradition. This is a soft check via §4.9.2 WA quorum during the publication phase, not a hard wire-format test.

---

## 2. The five-phase mapping process

Every deployment of this standard follows the same five phases. Each phase produces specific artifacts that the next phase consumes. The full process for *Magnifica Humanitas* took roughly three weeks across three iterations; subsequent governance documents should take less because the methodology and primer are mature.

### Phase 1 — Source preparation

**Inputs**: the authoritative governance document; the current Registry-side `LANGUAGE_PRIMER.md`; the current `METHODOLOGY.md`.

**Steps**:

1. **Copy the authoritative text into `source_material/governance/{document_id}/`** in the mapping repository. Include the original-language version + any official English translation. Hash the bytes; record in `source_material/governance/{document_id}/manifest.yaml`.
2. **Identify the unit of mapping**. For *Magnifica Humanitas* this was numbered paragraphs (245 of them). For the EU AI Act it would be articles (~120). For indigenous frameworks it may be principle clauses (5–12). The unit is the smallest atomic claim-bearer.
3. **Verify primer + methodology are current**. Per `METHODOLOGY.md` §8.5.1 wire-format sync discipline, the local primer must match the Registry-side primer. Stale-primer detection happens here, not after sub-agent output review.
4. **Pull supporting source material** as needed — the federation's prohibitions, prompts, conscience faculties, etc. The encyclical mapping required ~30 supporting files in `source_material/`.
5. **Declare the document's `bootstrap_batch_id`** following FSD-002 §10.4 convention: `{document_short_name}_v{version}` (e.g., `magnifica_humanitas_v1`, `eu_ai_act_v1`, `nist_airmf_v2`, `care_principles_v1`).

**Outputs**: `source_material/governance/{document_id}/` populated; primer + methodology verified current; `bootstrap_batch_id` declared.

### Phase 2 — Sub-agent fan-out

**Inputs**: prepared source material; current primer + methodology; `bootstrap_batch_id`.

**Steps**:

1. **One sub-agent per section** of the document. The encyclical's 7-chapter structure → 7 sub-agents in parallel. The EU AI Act's title-level structure → ~10 sub-agents.
2. **Each sub-agent reads**, in order: `MISSION.md` (or its equivalent — the framework's posture); `METHODOLOGY.md` §0 + §8.5; `LANGUAGE_PRIMER.md` FULL; the document section assigned; relevant supporting source material.
3. **Each sub-agent produces** a YAML-shaped output file `CONTRIBUTION_OBJECTS_{batch_id}_{section}.md` with one YAML block per atomic unit (paragraph / article / clause) per LANGUAGE_PRIMER §4 envelope shape.
4. **Strict 4-verdict discipline**: clean / composed / partial / not-translated. No invented intermediates.
5. **Composition-before-extension** per METHODOLOGY.md §8.5.2: every T-3 candidate must carry an explicit composition-attempt note showing what was tried.
6. **Cohort-scope and jurisdiction tagging**: each Contribution declares its cohort_scope (self / family / community / affiliations / species / federation / all) and any jurisdictional applicability. Religious documents typically default to `species`; regulatory frameworks typically declare their jurisdictional scope explicitly.
7. **`bootstrap_batch_id` carried** in every Contribution's `evidence_refs[]` for traceability.

**Outputs**: One `CONTRIBUTION_OBJECTS_{batch_id}_{section}.md` file per section.

### Phase 3 — Human review + synthesis

**Inputs**: All section outputs from Phase 2.

**Steps**:

1. **Read each section's verdict distribution + structural-primitive usage + T-3 candidates**. The reviewer is checking for: invented categories (forbidden); over-composition (cap 2-3 per unit); structural-primitive misuse (the round-2 mistake — `delegates_to` used where `supersedes` was right); LAKE_ALIGN bleed (residual vocabulary from prior mapping rounds).
2. **Synthesize**: produce `CONTRIBUTION_OBJECTS_{batch_id}_SYNTHESIS.md` with:
   - Aggregate verdict distribution (clean / composed / partial / not-translated)
   - Per-section breakdown
   - Structural-primitive usage table (`delegates_to` count, `supersedes` count, `withdraws` count, `recants` count)
   - T-3 candidates with §1.10.1 four-test gate verification
   - Strongest single envelopes (the most-demanding claims with cleanest wire renderings)
   - Confirmation that composition-before-extension was attempted before any T-3 emission
3. **If T-3 candidates emerged that are load-bearing**, route them to FSD-002 §4.9.2 wire-format amendment process. The wire format is content-neutral; T-3 closures benefit all future bootstrap batches.
4. **If primer drift is detected** (round-3 lesson per METHODOLOGY.md §8.5.6), apply the **cleanup-and-redo pattern**: delete prior outputs, re-sync primer, re-run sub-agents. Honest replacement over silent patching.

**Outputs**: Synthesis document; load-bearing T-3 inputs routed to FSD-002 amendment flow.

### Phase 4 — Wire-format input proposal (if applicable)

**Inputs**: T-3 candidates from Phase 3.

**Steps**:

If load-bearing T-3 candidates emerged, file an issue at CIRISRegistry referencing the proposed extension. The issue must include:

- The encyclical / regulation / framework paragraph(s) surfacing the gap
- The proposed prefix name (mechanism-descriptive per §1.10.1 T2)
- §1.10.1 four-test gate verification (T1 / T2 / T3 / T4)
- Closest existing primitive(s) that compose toward the claim (proving composition-before-extension was attempted)
- Priority assessment (HIGH / MEDIUM / LOW; load-bearing or refinement)

Per FSD-002 §4.9.2, the proposal flows: P5 Contribution → P10 witness diversity → P8 WA quorum → 1-of-6 sign-off. No silent additions.

**Outputs**: GitHub issue at `CIRISAI/CIRISRegistry` per the wire-format amendment flow.

### Phase 5 — Publication as bootstrap-batch

**Inputs**: Validated Contribution envelopes; synthesis document; any wire-format additions that landed in v1.X.

**Steps**:

1. **Sign the bootstrap-batch attestation** — a meta-attestation declaring the batch is complete, the methodology was followed, the verdict distribution is honest, and the T-3 candidates were routed.
2. **Tag every Contribution in the batch** with `evidence_refs[]` including `provenance:build_manifest:bootstrap_batch:{batch_id}:sha256:{batch_hash}` per FSD-002 §4.9.2 step 5.
3. **Publish to the federation directory** so other peers can ingest the bootstrap batch.
4. **Multi-source overlap analysis** triggers automatically once the batch is published: §6 below.

**Outputs**: Signed bootstrap-batch; published Contribution graph segment; multi-source overlap analysis report.

---

## 3. The contribution graph — structure

Once published, a bootstrap batch's Contributions are nodes in a graph. The federation maintains this graph at CIRISPersist (per the substrate contract); CIRISLensCore queries it; CIRISAgent consumes it for deployment-context decisions.

### 3.1 Node structure

Each Contribution is a node with these fields (from FSD-002 §2.1 + bootstrap-batch tagging):

```yaml
node_id: <attestation_id; content-hash of envelope>
attestation_type: <scores | delegates_to | supersedes | withdraws | recants>
attesting_key_id: <issuer; typically the bootstrap-batch publisher>
attested_key_id: <subject — entity or "*" for universal claims>
dimension: <prefix from FSD-002 §3>
score: <float [-1, +1]>
polarity: <derived from score sign>
confidence: <float [0, 1]>
cohort_scope: <self | family | community | affiliations | species | federation | all>
mutability: <constitutional | amendable>
bootstrap_batch_id: <which document this came from>
section_reference: <paragraph / article / clause id within the source>
witness_relation: <self | external | derived>
epistemic_mode: <direct | crypto | hearsay | derivative | appeal>
issued_at: <ISO 8601>
valid_until: <ISO 8601, optional>
issuer_signature: <Ed25519 + ML-DSA-65>
```

### 3.2 Edge types

Five edge types connect nodes:

1. **`evidence_refs` edges**: Contribution A's evidence_refs[] points at Contribution B. Most common edge type — "this claim is based on that prior claim or signed document."
2. **`supersedes` edges**: Contribution A `supersedes` Contribution B. The encyclical mapping produced 15 of these in CH 1 alone (Leo XIII → Pius XII → ... → Leo XIV doctrinal-continuity chain).
3. **`recants` edges**: Contribution A `recants` Contribution B (admits B was false at issuance). Rare and morally heavy. MH §176 (Church's slavery complicity admission) is the canonical example.
4. **`delegates_to` edges**: Contribution A delegates authority to B (bounded scope, validity window).
5. **`withdraws` edges**: Contribution A withdraws B (without claiming B was false).

Plus composition edges from the decision hierarchy (Goal ← Approach ← Method ← Progress Measure) for Family B Contributions.

### 3.3 Multi-source overlap

The same `dimension` (prefix) can be attested by Contributions from multiple `bootstrap_batch_id`s. This is the unit of cross-source comparison:

- **Magnifica Humanitas attestation**: `prohibited:weapons_harmful` polarity -1.0, cohort_scope species, mutability constitutional, bootstrap_batch `magnifica_humanitas_v1`, section_reference `MH §§197-198`
- **EU AI Act attestation** (forthcoming): `prohibited:weapons_harmful` polarity -1.0, cohort_scope species, mutability constitutional, bootstrap_batch `eu_ai_act_v1`, section_reference `Article 5(1)(c)` (or wherever the equivalent lands)
- **NIST AI RMF attestation** (forthcoming): similar shape

Three independent senior sources attesting the same prefix with the same polarity = **strong alignment**. The graph stores this naturally; queries surface it on demand.

---

## 4. Alignment detection

**Definition**: alignment between two governance documents on a prefix exists when both attest that prefix with the same polarity sign and compatible cohort_scope.

### 4.1 Alignment strength tiers

| Tier | Polarity | Cohort scope | Mutability | Reading |
|---|---|---|---|---|
| **STRONG** | Same sign | Same scope | Same mutability | The two documents make essentially the same claim — direct convergence |
| **WEAK** | Same sign | Compatible scopes (one is subset of other) | Same or one less restrictive | Same direction; one document may go further than the other |
| **CONVERGENT** | Same sign | Different scopes (neither subset) | May differ | Both moving in same direction at different scales |
| **COMPOSITIONAL** | Documents emit different prefixes that compose | n/a | n/a | Document A emits Goal at species; Document B emits Approach toward that Goal — reinforcing composition |

### 4.2 Alignment query (pseudocode)

```
def find_alignment(prefix_pattern, doc_a_id, doc_b_id):
    # Find all Contributions in doc_a with matching prefix
    a_contribs = graph.find(dimension=prefix_pattern, batch_id=doc_a_id)
    b_contribs = graph.find(dimension=prefix_pattern, batch_id=doc_b_id)
    alignments = []
    for a in a_contribs:
        for b in b_contribs:
            if a.polarity == b.polarity:
                tier = compute_tier(a.cohort_scope, b.cohort_scope, a.mutability, b.mutability)
                alignments.append({
                    "a": a.section_reference,
                    "b": b.section_reference,
                    "tier": tier,
                    "joint_evidence": a.evidence_refs + b.evidence_refs
                })
    return alignments
```

### 4.3 Alignment as positive federation evidence

Multiple-source alignment on a prefix is **stronger evidence than any single source** that the claim is well-grounded. When MH + EU AI Act + NIST AI RMF + CETS 225 all attest `prohibited:weapons_harmful` polarity -1.0 species-scope constitutional, the convergent attestation is independent triangulation that the claim is correct, not just an artifact of one tradition's perspective.

This is the load-bearing strategic value of multi-source mapping: alignment becomes structural evidence, not assertion.

---

## 5. Conflict detection

**Definition**: conflict between two governance documents on a prefix exists when both attest that prefix with opposite polarity signs in overlapping cohort_scope, OR with incompatible mutability claims on the same dimension.

### 5.1 Conflict types

| Type | Polarity | Cohort scope | Mutability | Reading | Resolution mechanism |
|---|---|---|---|---|---|
| **Direct conflict** | Opposite signs | Overlapping scope | n/a | Documents say opposite things about the same dimension at the same scale | §6.1.4 lexical-vulnerability-priority + §6.1.5 locality-scaled-quorum + WA review |
| **Mutability conflict** | Same sign | Same scope | One constitutional, one amendable | Documents agree on direction but disagree on whether it can be revisited | WA review + Reconsideration if appropriate |
| **Scope-mismatch conflict** | Same sign | Incompatible scopes | n/a | Document A claims federation scope; Document B claims local scope on incompatible aim | §6.1.5 locality-scaled-quorum; cohort-specific composition |
| **Composition conflict** | n/a | n/a | n/a | Goal A and Goal B are incompatible aims at the same scope | Sub-federation branching per CIRISNodeCore §1.2 Primitive 13 |

### 5.2 Conflict query (pseudocode)

```
def find_conflicts(prefix_pattern, batch_ids):
    candidates = []
    for batch_id in batch_ids:
        contribs = graph.find(dimension=prefix_pattern, batch_id=batch_id)
        candidates.extend(contribs)
    conflicts = []
    for a, b in combinations(candidates, 2):
        if a.bootstrap_batch_id == b.bootstrap_batch_id:
            continue  # same source; not cross-source conflict
        if polarity_opposite(a, b) and scopes_overlap(a, b):
            conflicts.append({
                "type": "direct",
                "a": (a.batch_id, a.section_reference),
                "b": (b.batch_id, b.section_reference),
                "scope_overlap": compute_overlap(a.cohort_scope, b.cohort_scope)
            })
        elif a.polarity == b.polarity and a.mutability != b.mutability:
            conflicts.append({"type": "mutability", ...})
    return conflicts
```

### 5.3 Conflict resolution

The wire format does not unilaterally adjudicate conflicts. It surfaces them. Resolution happens through:

1. **Existing CIRIS resolution mechanisms** — WBD to Wise Authority quorum; Reconsideration if a verdict is sought; §6.1.4 lexical-vulnerability-priority for ties favoring most-affected populations; §6.1.5 locality-scaled-quorum for scope-aware decision routing.
2. **Documented divergence** — if no resolution is possible (e.g., genuine pluralism on a question), the conflict stays in the graph as a named documented disagreement. Agents in deployment see "MH attests X; EU AI Act attests not-X on overlapping scope; no resolution available." That's honest documentation.
3. **Re-deployment with corrected mapping** — if the conflict arose from a mapping error (sub-agent misclassified), Phase 3 review catches it and corrects.

**The wire format's job is to surface conflict; the federation's deliberative apparatus (WA / Vote / Moderation / Reconsideration) decides what to do about it.**

---

## 6. Regional composition for agent deployment

The Contribution graph is too large for any single deployment. Agents in production compose a **regionally-appropriate subgraph** based on their `deployment_profile`.

### 6.1 The deployment_profile fields relevant to composition

```yaml
deployment_profile:
  jurisdiction: <ISO 3166 code or multi-jurisdiction list>
  deployment_domain: <education | health | finance | civic | general | ...>
  language_locale: <primary user language>
  cohort_scope_default: <which scopes the agent operates at by default>
  governance_subscriptions: <list of bootstrap_batch_ids the agent accepts>
```

### 6.2 Subgraph composition

For agent A with deployment_profile P:

1. **Always-included batches**: the CIRIS Accord itself (the federation's foundational governance) + the LANGUAGE_PRIMER + any framework-internal bootstraps.
2. **Jurisdiction-matched batches**: include all bootstrap_batches whose declared jurisdiction overlaps with P.jurisdiction. E.g., an agent deployed in Germany includes EU AI Act + German Federal Constitution attestations + UN Universal Declaration of Human Rights + (if subscribed) Magnifica Humanitas.
3. **Cohort-matched filtering**: among included batches, retain Contributions whose cohort_scope is compatible with agent's cohort_scope_default.
4. **Conflict surface**: compute conflicts within the composed subgraph. Surface them at PDMA Step 1 contextualisation as explicit "your deployment operates within X governance frameworks; here are Y known conflicts; here is the resolution priority per the federation's tie-breaking policies."

### 6.3 Composed guidance — what the agent sees

For a deployment-domain `health`, jurisdiction `BR` (Brazil), language_locale `pt-BR`:

```yaml
active_governance_graph:
  - CIRIS_Accord_v1.2-Beta (always)
  - magnifica_humanitas_v1 (subscribed; Catholic-tradition input)
  - eu_ai_act_v1 (NOT applicable; Brazilian jurisdiction)
  - brazil_pl_2338_v1 (jurisdiction match; AI regulation)
  - brazil_lgpd_v1 (jurisdiction match; data protection)
  - un_udhr (always)
  - care_principles_v1 (subscribed; indigenous data sovereignty — applies in Amazon-region deployments)

known_conflicts:
  - prefix: "non_maleficence:reproductive_autonomy:medical_advice"
    sources: [magnifica_humanitas_v1, brazil_pl_2338_v1]
    type: "direct (polarity opposite)"
    resolution_policy: "deployment_domain=health → defer to licensed medical authority via WBD; do not adjudicate"
  
  - prefix: "fidelity:source_language_preservation:indigenous"
    sources: [care_principles_v1, magnifica_humanitas_v1]
    type: "scope_mismatch (CARE: indigenous-cohort; MH: species-cohort)"
    resolution_policy: "§6.1.5 locality-scaled-quorum favors cohort-specific scope for deployment in cohort context"
```

The agent reads this active graph + known conflicts at PDMA Step 1 and incorporates both into its reasoning. Decisions are made with explicit conflict-awareness, not silent averaging.

### 6.4 Audit-trail provenance

For any agent decision, the audit-trail back to source governance documents follows the `evidence_refs[]` graph. A SLASHING attestation can be appealed to Reconsideration with reference to the original bootstrap-batch sources; deployment-context decisions can be audited to confirm they composed the right subgraph.

---

## 7. Deployments — the strategic trio + the prototype

### 7.0 Strategic reasoning — why these particular documents

The *Magnifica Humanitas* mapping was the **prototype that produced this standard**. The methodology was built from MH; its content-neutrality claim is verified by reproducing successfully on three documents that are *institutionally and structurally distinct from MH and from each other*. Together with MH (religious magisterium), the four-document set covers the four major institutional shapes of senior governance documents:

| Institutional shape | Document | Geographic scope | Strategic value |
|---|---|---|---|
| Religious magisterium | *Magnifica Humanitas* (2026) | Catholic / international | Prototype — produced the methodology |
| Governmental advisory | EU HLEG Ethics Guidelines for Trustworthy AI (2019) | European Union | First multi-source alignment test |
| Technical society / civil society | IEEE Ethically Aligned Design 2nd ed. (2019) | Global (USA-anchored, multi-traditional) | Cross-traditional alignment + likely T-3 surface (Affective Computing) |
| Multilateral political body | ASEAN Guide on AI Governance and Ethics (2024) | Southeast Asia (10 states) | Regional composition framework test |

After the trio + MH, no honest critic can claim the framework was tested only against documents that look like religious encyclicals. **Institutional-shape diversity is the load-bearing structural feature of this batch.** Geographic diversity (three continents) is real but secondary; stakeholder-voice diversity (gov advisory + technical society + multilateral political + religious magisterium) is what makes the alignment claim non-circular.

### 7.1 Magnifica Humanitas — the prototype (DONE; round 3 complete)

- **Source**: Pope Leo XIV, *Magnifica Humanitas*, 15 May 2026
- **Institutional shape**: religious magisterium
- **Unit**: numbered paragraphs (245)
- **bootstrap_batch_id**: `magnifica_humanitas_v1`
- **Drove v1.3 + v1.4 wire-format additions**: subsidiarity (`locality:decision:{scale}`), universal destination of goods (`detection:distributive:access:{resource_type}`), supply-chain labor recognition (`credits:*:substrate_building`), multilateral participation (`multilateral_participation:{forum}:{kind}`), ecology of communication (`detection:correlated_action:ecology_of_communication:{aspect}` axis), `testimonial_witness:{kind}`, `agent_files:*`, `holds_bytes:*`, `witness_relation` envelope field, §6.1.4 lexical-vulnerability-priority policy, §2.2.1 `delegates_to` authority-source reuse pattern
- **Status**: ~73% clean+composed; ~22% T-1 (correctly bowed out); 1 residual T-3 candidate (already-tracked v1.5+ workshop). Three rounds of iteration recorded in commit history; methodology stabilized.
- **Outputs**: `CONTRIBUTION_OBJECTS_v1.4_CH*.md` + `CONTRIBUTION_OBJECTS_v1.4_SYNTHESIS.md` in this repository.

### 7.2 EU HLEG Ethics Guidelines for Trustworthy AI (NEXT — Phase 1 complete)

- **Source**: High-Level Expert Group on AI (HLEG), convened by the European Commission, "Ethics Guidelines for Trustworthy AI," 8 April 2019. 52-expert deliberatively-produced document.
- **Institutional shape**: governmental advisory (European Commission-convened expert group)
- **Geographic scope**: European Union
- **Source material**: `source_material/governance/eu_hleg_v1/` (Phase 1 complete 2026-05-27; PDF + extracted text + manifest)
- **Unit**: natural paragraphs within structural sections (~150–200 substantive atomic units across 41 pages); see `source_material/governance/eu_hleg_v1/manifest.yaml`
- **bootstrap_batch_id**: `eu_hleg_v1`
- **Expected verdict distribution**: very high clean+composed rate (~85%+); few T-1 (secular; no Christological / sacramental content); some T-2 (rhetorical framing); minimal T-3 (the 7 requirements map onto existing prefix families with direct correspondence)
- **Strategic value**:
  - First multi-source alignment test against *Magnifica Humanitas*: different traditions, convergent attestations on shared dimensions (transparency, accountability, non-discrimination, privacy, safety)
  - First non-religious-magisterium institutional shape — tests methodology content-neutrality
  - The 7 requirements (Human agency + oversight; Technical robustness + safety; Privacy + data governance; Transparency; Diversity + non-discrimination + fairness; Societal + environmental wellbeing; Accountability) provide a structured rubric for cross-source comparison
- **Mapping focus priorities**: Chapter I 4 principles; Chapter II §1 the 7 requirements; Chapter III assessment list

### 7.3 IEEE Ethically Aligned Design 2nd ed. (THEN)

- **Source**: IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems, "Ethically Aligned Design: A Vision for Prioritizing Human Well-being with Autonomous and Intelligent Systems," 2nd edition, March 2019. ~700+ contributors.
- **Institutional shape**: technical society / civil society (engineering professional body)
- **Geographic scope**: global (USA-anchored; multi-traditional in its own framing — explicitly engages classical Western ethics + Confucian + Buddhist + Ubuntu)
- **Unit**: natural paragraphs within chapter sections (~290 pages; 10 chapters; estimated 500–800 atomic units — substantially larger than MH or EU HLEG)
- **Sub-agent fan-out**: ~10 sub-agents (one per chapter), not 7, given the scope
- **bootstrap_batch_id**: `ieee_ead_v2`
- **Expected verdict distribution**: high clean+composed rate; the document's multi-traditional framing aligns directly with CIRIS's polyglot principle anchoring in `pdma_framing.yml §III`; expect dense composed envelopes
- **Watch for T-3 in the Affective Computing chapter**: no current CIRIS prefix family for affective-state attestations. May surface a load-bearing T-3 proposing an `affective:*` family for v1.5 consideration.
- **Strategic value**:
  - Cross-traditional alignment depth — IEEE EAD's classical-ethics chapter directly engages traditions the CIRIS framework's `pdma_framing` already names, providing very strong multi-source-overlap evidence
  - Stress-test of the methodology at scale (largest document in the trio)
  - Likely T-3 surface validating that the standard's Phase 4 wire-format-input proposal flow works in practice

### 7.4 ASEAN Guide on AI Governance and Ethics (LAST in the trio)

- **Source**: ASEAN Digital Ministers' Meeting, "ASEAN Guide on AI Governance and Ethics," February 2024.
- **Institutional shape**: multilateral political body (regional intergovernmental)
- **Geographic scope**: Southeast Asia (Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Vietnam)
- **Unit**: TBD at Phase 1; likely substantive sections covering governance principles, risk management, deployer + user responsibilities, internal governance structures, accountability mechanisms
- **bootstrap_batch_id**: `asean_guide_v1`
- **Expected verdict distribution**: high clean+composed rate; the document is operationally-framed (deployer + user responsibilities)
- **Strategic value**:
  - Direct test of `GOVERNANCE_FABRIC_MAPPING_STANDARD §6` regional-composition framework
  - Most recent document; least supersession analysis needed
  - The multilateral-political-body shape benefits from two prior secular deployments to compare against (EU advisory + IEEE technical society + ASEAN multilateral = three distinct institutional shapes mapped before this lands)
- **Precondition for ASEAN deployment**: at least EU HLEG must be deployed first so the regional-composition framework can be exercised on a realistic two-batch + jurisdictional-tagging subgraph

### 7.5 Multi-source overlap analysis (triggered after the trio lands)

Once all four batches (MH + EU HLEG + IEEE EAD + ASEAN) are published, the federation has its first **structurally-evidenced alignment claim**: convergent attestations on shared dimensions from four institutionally-distinct senior frameworks across four geographic regions and four traditions.

Expected analytical outputs:
- Per-prefix alignment density (which dimensions are attested by 4 / 3 / 2 / 1 of the four batches)
- Conflict surfacing (direct conflicts; mutability conflicts; scope-mismatch conflicts)
- Coverage gaps (dimensions attested by some but not others — potential harmonization opportunities)
- The first non-trivial regional-composition exercise for an agent deployed in a jurisdiction where multiple batches apply

### 7.6 Subsequent deployments (priority-ordered candidates, post-trio)

Once the methodology + four-document overlap analysis is demonstrated:

- **Council of Europe AI Convention CETS 225** (2024) — international law / treaty-based; 46+ member states; complements the trio with binding-treaty institutional shape
- **UN UNESCO Recommendation on AI Ethics** (2021) — global multilateral
- **Hiroshima AI Process** — G7 international soft law
- **CARE Principles for Indigenous Data Governance** — indigenous data sovereignty
- **Ubuntu philosophy of personhood** (formal text-based mapping) — formalizes the framework's primary anchoring tradition
- **Buddhist economics** (Schumacher / Sivaraksa lineage) — Asian contemplative-tradition
- **Confucian AI ethics** (where formal documents exist) — East Asian philosophical
- **EU AI Act** (Regulation EU 2024/1689) — most operational regulatory framework; tests whether the standard handles binding-law content
- **NIST AI RMF** — US regulatory functional-organization
- **Secular humanist consensus documents** — analytical-tradition completion

Each adds independent confirmation; each may surface T-3 candidates that drive subsequent wire-format additions; the methodology is the same.

---

## 8. Open work

This standard does not yet specify:

1. **Exact graph storage format** at CIRISPersist. The substrate contract assumes the graph is queryable; the schema details are open work. Likely: signed Contribution table with composite indexes on `(dimension, bootstrap_batch_id)`, `(attested_key_id, dimension)`, plus structural-primitive edge tables.
2. **Cross-batch calibration versioning**. When a prefix's calibration changes (e.g., RATCHET updates the correlated_action calibration package), prior bootstrap-batches may need re-evaluation. The `delegates_to` chain at §2.2 carries the structural mechanism, but the operational policy is open work.
3. **Conflict-resolution UI** for agents and operators. The wire format surfaces conflicts; how they are presented at PDMA Step 1 and to human operators is UX work.
4. **Bootstrap-batch deprecation policy**. When a governance document is superseded (e.g., a regulation amended, an encyclical succeeded), the deprecation flow is the wire format's `supersedes` primitive, but the operational policy for active deployments is open work.
5. **Multi-language and translation provenance**. When the source document exists in multiple official languages, the mapping should attest to which language was the primary source and how translations were verified. Especially relevant for international conventions and indigenous frameworks.
6. **Adversarial-resistance** of the mapping process. A bad-faith actor could attempt to publish a bootstrap-batch with skewed attestations to bias the federation. Defense relies on §4.9.2 WA quorum + witness diversity + the §10.4 multi-source-overlap discipline (no single batch should be sole evidence for high-impact federation decisions).
7. **Agent-side composition algorithms**. §6.2 specifies the conceptual composition; the actual algorithms (subgraph extraction, conflict surfacing, priority-weighted reasoning) need to be specified and implemented at CIRISAgent.

---

## 9. Cross-references

- `LANGUAGE_PRIMER.md` v1.1 (Registry-synced) — the translation grammar
- `METHODOLOGY.md` §0 + §8.5 — the iterative process and primer-drift discipline
- `FSD-002 §10.4` (CIRISRegistry) — bootstrap-contributions pattern; this standard is the formalization
- `FSD-002 §4.9.2` (CIRISRegistry) — wire-format amendment process; this standard's Phase 4 follows it
- `FSD-002 §6.1.4` — lexical-vulnerability-priority consumer policy; conflict-resolution mechanism
- `FSD-002 §6.1.5` — locality-scaled-quorum; scope-aware adjudication
- `CIRISNodeCore §1.2` — the 15 primitives that this standard composes with
- `CONTRIBUTION_OBJECTS_v1.4_SYNTHESIS.md` — the first deployment's outcome documentation
- `MISSION.md` §1.3 — the framework's grounding posture (applicable to any governance-document mapping)

---

## 10. Status

- **Standard proposed**: this document
- **Reference deployment**: Magnifica Humanitas (round 3 complete)
- **Next deployment**: EU AI Act (when prioritized)
- **Open work**: §8 above
- **Candidate destination**: `FSD-003` at CIRISRegistry once stable

The standard is intended to be **forkable, criticizable, improvable**. The encyclical mapping is one instance; the methodology is the artifact that lets the federation produce many more such instances, each adding independent evidence to the framework's alignment claim and producing a richer governance Contribution graph for agent deployments.

**End GOVERNANCE_FABRIC_MAPPING_STANDARD.md v0.1**
