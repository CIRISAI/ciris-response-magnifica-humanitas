# Website integration — content surface for the cross-walk browser

Brief for the website team building a single cohesive graph browser over the four-batch governance-fabric mapping. Users should be able to enter from any source work (an encyclical paragraph, an EU HLEG requirement, an IEEE EAD recommendation, an ASEAN principle) and traverse out to the CIRIS Agent control that implements compliance — or enter from a CIRIS Agent control and traverse out to every regulatory parent that attests its dimension.

This document explains what content exists, what its stable identifiers are, what the graph shape is, and what navigation patterns to support.

---

## 1. The graph at a glance

```
                            ┌──────────────────────┐
                            │  Accord principle    │  (6 nodes)
                            │  beneficence /       │
                            │  non_maleficence /   │
                            │  integrity /         │
                            │  fidelity /          │
                            │  autonomy / justice  │
                            └──────────┬───────────┘
                                       │ encompasses
                                       ▼
┌──────────────┐  attests  ┌────────────────────────┐  implemented_by  ┌────────────────────┐
│  Source      ├──────────▶│  Dimension             ├─────────────────▶│  CIRIS Agent       │
│  paragraph   │           │  D01..D27 (stable IDs) │                  │  control           │
│  (~921 nodes)│◀──────────┤  STRONG-4 or STRONG-3  │◀─────────────────┤  (~27 nodes)       │
└──────┬───────┘  is_attested_by                     implements        └─────────┬──────────┘
       │                   └───────┬────────────────┘                            │
       │ belongs_to                │ carried_by                                  │ references
       ▼                           ▼                                             ▼
┌──────────────┐             ┌──────────────┐                          ┌────────────────────┐
│  Batch       │             │  Wire        │                          │  CIRISAgent code   │
│  (4 nodes)   │             │  primitive   │                          │  path / policy /   │
│  MH / EU /   │             │  (CIRIS      │                          │  test / config     │
│  IEEE /      │             │  prefix      │                          └────────────────────┘
│  ASEAN       │             │  family)     │
└──────────────┘             └──────────────┘

  Plus secondary nodes that decorate the graph:
  - Conflict (5 nodes — CONF-01..CONF-05)
  - T-3 candidate (9 nodes — T3-01..T3-09)
  - Specialization issue (e.g., CIRISMedical#1)
```

---

## 2. Entity types (the graph nodes)

### 2.1 Batch — the source work

| Field | Example | Source file |
|---|---|---|
| id (stable) | `magnifica_humanitas_v1` | `SEED_DIMENSIONS.yaml` `batches[]` |
| short label | `MH` | same |
| title | "Magnifica Humanitas (On Safeguarding the Human Person in the Time of Artificial Intelligence)" | same |
| institutional shape | `religious_magisterium` / `governmental_advisory` / `technical_society` / `multilateral_political` | same |
| jurisdiction | `catholic_international` / `european_union` / `global_USA_anchored` / `southeast_asia` | same |
| publication date | `2026-05-15` | same |
| authority | `Pope Leo XIV` | same |
| atomic units mapped | 245 | same |

**Detail page**: title + author + date + shape + jurisdiction; table of contents that drills into the source paragraphs (see §2.2); aggregate stats (how many atomic units, how many dimensions attested, how many STRONG-4 vs STRONG-3).

### 2.2 Source paragraph (atomic unit)

The grain of the corpus. Each is a unit of normative claim drawn from a chapter / section of a source work. **~921 nodes total** across the 4 batches.

| Field | Example | Source file |
|---|---|---|
| batch_id | `magnifica_humanitas_v1` | `CONTRIBUTION_OBJECTS_v1.4_CH4_*.md` |
| citation (stable for that batch) | `§76` (MH) / `§1.2` (EU) / `Ch4 §0.a` (IEEE) / `§B.3` (ASEAN) | embedded in each unit's `Source` field |
| source quote (≤2 sentences) | "deception with intention to deceive is structurally excluded..." | same |
| verdict | `clean` / `composed` / `partial` / `not-translated` | same |
| wire envelope (YAML) | embedded — the operative claim as Contribution YAML | same |
| nuance_lost (one-line) | "tradition-internal reasoning sequence" | same |
| dimension references | `D01`, `D04` (one paragraph may instantiate multiple dimensions) | inferred from the seed's `regulatory_attestations[].citation` matching |

**Detail page**: batch + citation + source quote + verdict + wire envelope (rendered) + nuance_lost + outgoing links to dimensions attested.

**Important**: source quotes are ≤2 sentences and act as fair-use anchor text. The full source documents are NOT in this repo (third-party content); the website should link out to the canonical source where appropriate (manifests in `source_material/governance/*/manifest.yaml` carry the authoritative URLs).

### 2.3 Dimension — the load-bearing node

The 27 structural-evidence dimensions. **STABLE IDS D01-D27** (with D28+ reserved for future batches). These IDs are the graph's spine.

| Field | Example | Source file |
|---|---|---|
| id (STABLE, never renumber) | `D04` | `SEED_DIMENSIONS.yaml` `dimensions[]` |
| prefix family | `prohibited:*` | same |
| tier | `STRONG-4` or `STRONG-3` | same |
| gloss | "Categorical floor — polarity-(-1)/constitutional/species — the absolute moral form the wire format admits" | same |
| attestation counts (per batch) | `{MH: 50, EU: 17, IEEE: 28, ASEAN: 9, total: 104}` | same |
| regulatory_attestations[] | 4 entries (or 3 for STRONG-3) with `{batch_id, citation, language, wire_form}` | same |
| wire_primitives[] | `["prohibited:*"]` | same |
| accord_principle | `non_maleficence` | same |
| absent_batch (STRONG-3 only) | `{batch_id, absence_note, functional_analogue}` | same |
| convergence_note | "STRONGEST single structural-evidence claim..." | same |
| ciris_compliance | block with status + proposed_pointer | same (when filled by agent team, populates from compliance docs) |

**Detail page**: id + prefix + tier + gloss + attestation density chart (4-bar histogram) + 4 (or 3) regulatory attestations as expandable cards + wire primitives + Accord principle + convergence note + conflicts involving this dimension + T-3 candidates affecting it + outgoing link to the CIRIS Agent control that implements it.

### 2.4 Accord principle

The 6 CIRIS Accord principles. Hub nodes for the Annex K traversal.

| Field | Value |
|---|---|
| id (STABLE) | `beneficence` / `non_maleficence` / `integrity` / `fidelity` / `autonomy` / `justice` |
| operative dimensions | array of dimension IDs from `SEED_DIMENSIONS.yaml` `aggregate_indices.by_accord_principle` |

**Detail page**: the Annex K section for that principle — render via `render_annex_k.py` or pull directly from `ANNEX_K.md`.

### 2.5 Wire primitive

The CIRIS prefix family (e.g., `non_maleficence:*`, `prohibited:*`, `locality:decision:{scale}`). Bridges the dimension layer to the federation runtime layer.

| Field | Example | Source |
|---|---|---|
| prefix family | `prohibited:*` | inferred from `dimensions[].wire_primitives` |
| owning component | usually inferred from prefix (e.g., `prohibited:*` → CIRIS Agent prohibitions module) | LANGUAGE_PRIMER.md + per-dimension `ciris_compliance.proposed_pointer` |
| dimensions using this primitive | array of dimension IDs | inverse of `dimensions[].wire_primitives` |

**Detail page**: prefix + owning component + which dimensions use it + LANGUAGE_PRIMER.md cross-reference.

### 2.6 CIRIS Agent control

The implementation surface — one per dimension. Lives in **CIRISAgent's `compliance/` directory** (not this repo).

| Field | Example | Source |
|---|---|---|
| dimension_id | `D04` | `CIRISAgent/compliance/D04_prohibited.md` filename |
| filename | `D04_prohibited.md` | same |
| auto-rendered structural region | regulatory attestations + wire primitives + convergence + conflicts | regenerated from `SEED_DIMENSIONS.yaml` via `generate_ciris_compliance_stubs.py` |
| human-authored region | code references + observability hooks + known gaps (between `<!-- BEGIN HUMAN -->` / `<!-- END HUMAN -->` fences) | maintained by CIRISAgent team |

**Detail page**: render the markdown. The fences distinguish auto-rendered (canonical from seed) from human-authored (canonical from CIRISAgent maintainers).

### 2.7 Conflict — cross-source disagreements

5 nodes (CONF-01 to CONF-05). Surfaced when batches disagree on a dimension's disposition.

| Field | Example |
|---|---|
| id (STABLE) | `CONF-01` |
| type | `direct` / `substrate_disposition` / `mutability` / `scope_mismatch` |
| severity | `HIGH` / `MEDIUM` / `LOW_MEDIUM` / `LOW` |
| dimensions[] | dimensions involved (graph edges) |
| sources[] | batch IDs involved |
| claim | the conflict statement |
| disposition | resolution route (e.g., "Federation-level categorical posture stays. Specialization-layer consideration at CIRISMedical#1") |

Source: `SEED_DIMENSIONS.yaml` `aggregate_indices.conflicts_surfaced`.

### 2.8 T-3 candidate — expressive-gap proposals for v1.5+

9 nodes (T3-01 to T3-09). Future wire-format additions surfaced by the trio mapping.

| Field | Example |
|---|---|
| id (STABLE) | `T3-01` |
| proposed_prefix | `detection:affective_state_shift:{axis}` |
| priority | `HIGH` / `MEDIUM_HIGH` / `MEDIUM` / `MEDIUM_LOW` / `LOW` |
| source[] | batches that surfaced it |
| affects_dimension | optional dimension ID (graph edge to existing dimension) |

Source: `SEED_DIMENSIONS.yaml` `aggregate_indices.t3_candidates_v1_5`.

### 2.9 Specialization issue (external)

E.g., [CIRISMedical#1](https://github.com/CIRISAI/CIRISMedical/issues/1). Where conflicts get routed for specialization-layer disposition.

---

## 3. Relationship types (the graph edges)

| Source type | Edge | Target type | Where defined |
|---|---|---|---|
| Batch | contains | Source paragraph | `CONTRIBUTION_OBJECTS_*.md` membership |
| Source paragraph | attests | Dimension | match `paragraph.citation` against `dimension.regulatory_attestations[].citation` |
| Source paragraph | invokes | Wire primitive | parse `paragraph.wire_envelope` YAML |
| Dimension | is_attested_by | Source paragraph | inverse of attests |
| Dimension | serves | Accord principle | `dimension.accord_principle` |
| Dimension | carried_by | Wire primitive | `dimension.wire_primitives[]` |
| Dimension | implemented_by | CIRIS Agent control | filename matches `D{id}_*.md` in CIRISAgent/compliance/ |
| Dimension | surfaces_conflict | Conflict | `dimension.id in conflict.dimensions[]` |
| Dimension | surfaces_t3 | T-3 candidate | `t3.affects_dimension == dimension.id` |
| Accord principle | encompasses | Dimension | inverse of serves |
| CIRIS Agent control | implements | Dimension | inverse of implemented_by |
| Conflict | involves | Dimension | inverse of surfaces_conflict |
| Conflict | routed_to | Specialization issue | parse `conflict.disposition` for issue URL |

---

## 4. Source files to ingest

All in `https://github.com/CIRISAI/ciris-response-magnifica-humanitas` (this repo) except CIRIS Agent controls:

| File | Format | What you get | Refresh discipline |
|---|---|---|---|
| `SEED_DIMENSIONS.yaml` | YAML | All 27 dimensions + corpus + indices + conflicts + T-3 candidates. **Single source of truth for the dimension layer.** | Bumped on seed_version change; subscribe to commits |
| `CONTRIBUTION_OBJECTS_v1.4_*.md` (8 MH files) | Markdown with embedded YAML | MH paragraphs with wire envelopes, verdicts, nuance_lost | Stable after v1.4 round-3 lock |
| `CONTRIBUTION_OBJECTS_EU_HLEG_*.md` (5 files) | same | EU HLEG paragraphs | stable |
| `CONTRIBUTION_OBJECTS_IEEE_EAD_*.md` (11 files) | same | IEEE EAD paragraphs | stable |
| `CONTRIBUTION_OBJECTS_ASEAN_*.md` (5 files) | same | ASEAN paragraphs | stable |
| `source_material/governance/{batch_id}/manifest.yaml` | YAML | Authoritative source URL, sha256, publication metadata for each batch | stable |
| `ANNEX_K.md` | Markdown (auto-rendered) | Pre-rendered Accord principle → dimension → regulatory-attestation traversal. **Useful as a fallback if you don't want to traverse the seed yourself.** | Regenerated from seed on every seed bump via `render_annex_k.py` |
| `FOUR_BATCH_OVERLAP_ANALYSIS.md` | Markdown | The full Phase 3 synthesis (longer-form context for any dimension's detail page) | stable |
| `TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md` + 4 `TRANSLATION_AUDIT_*.md` | Markdown | Phase 4 calibration profile per batch | stable |
| `DIMENSIONS_GUIDE.md` | Markdown | Quick-reference for the 27 (shorter than seed; good as a tooltip / overview) | regenerated alongside seed |
| `CIRISAgent/compliance/D{id}_*.md` (27 files, **other repo**) | Markdown with `<!-- BEGIN HUMAN -->` fences | CIRIS Agent control: regulatory attestations (auto-rendered) + code references / observability / gaps (human-authored) | Auto-rendered region regenerates on seed bump; human-authored region maintained by CIRISAgent team |

### Parsing notes

**`SEED_DIMENSIONS.yaml`**: standard YAML. Use any YAML parser. Top-level keys: `metadata`, `batches`, `dimensions`, `aggregate_indices`, `downstream_bindings`, `maintenance`.

**`CONTRIBUTION_OBJECTS_*.md`**: markdown with fenced YAML code blocks for the wire envelopes. Each unit is delimited by `## Unit NNN` or `## §X.Y.Z` headers. Source quotes are in `**Source** (lines X-Y): "..."` lines. Verdicts in `**Verdict**: ...` lines. Wire envelopes in ```yaml fenced blocks. You'll want a small parser that walks the file and emits structured records — happy to provide one if useful.

**`CIRISAgent/compliance/D{id}_*.md`**: structured per the stub generator. Auto-rendered region is everything before `---\n<!-- BEGIN HUMAN -->`; human-authored region is between the fences. Render both.

**Manifests in `source_material/governance/*/`**: small YAML, authoritative URL + sha256 + page count + section structure. Use for the "open source document" outbound links.

---

## 5. Stable identifier scheme

| Layer | ID format | Stability |
|---|---|---|
| Batch | snake_case slug (e.g., `magnifica_humanitas_v1`) | STABLE |
| Source paragraph | `{batch_id}:{citation}` (e.g., `magnifica_humanitas_v1:§76`) | STABLE per batch (citations are how the document refers to itself) |
| Dimension | `D01` through `D27` (zero-padded) | STABLE FOREVER — never renumber. New batches allocate D28+. |
| Accord principle | snake_case (`non_maleficence`, etc.) | STABLE |
| Wire primitive | the prefix family string (e.g., `prohibited:*`) | STABLE within FSD-002 version; tracks LANGUAGE_PRIMER.md |
| CIRIS Agent control | matches dimension ID; filename is `D{id}_{slugified_prefix}.md` | STABLE (dimension ID is stable) |
| Conflict | `CONF-01` through `CONF-05` (zero-padded) | STABLE |
| T-3 candidate | `T3-01` through `T3-09` | STABLE |

URL pattern suggestion (for the browser):
- `/batch/{batch_id}` — work detail
- `/batch/{batch_id}/{citation}` — source paragraph detail (URL-encode the §)
- `/dimension/{id}` — dimension detail
- `/principle/{name}` — Accord principle hub
- `/primitive/{prefix}` — wire primitive cross-reference
- `/control/{id}` — CIRIS Agent control (mirror of CIRISAgent/compliance/D{id}_*.md)
- `/conflict/{id}` — conflict detail
- `/t3/{id}` — T-3 candidate detail

---

## 6. Navigation patterns to support (worked examples)

### 6.1 "I'm reading Magnifica Humanitas §76 — what does CIRIS Agent do about it?"

Path: MH §76 → D03 `justice:*` (the lexical_vulnerability_priority anchor) → CIRIS Agent control D03 → code references inside CIRISAgent (e.g., the PDMA Step 1 stakeholder analysis + the `justice:lexical_vulnerability_priority` policy implementation).

Sidebar should show: the **other 3 batches' attestations of D03** (EU §1.7.d, IEEE Ch10 §I1, ASEAN §B.2) so the user sees the convergence in context.

### 6.2 "I'm looking at this piece of CIRIS Agent code — what regulatory frameworks require it?"

Path: code path → CIRIS Agent control (the compliance/ doc that references it) → dimension(s) → 3-4 regulatory parent attestations.

This is the **provenance walk**. Output: "this code implements D04 `prohibited:*` which is attested by 4 sources: MH §§197-198 (LAWS); EU AI Act preamble; IEEE EAD Ch4-5; ASEAN §B.3 + Annex A. Plus 1 cross-source conflict (CONF-01, routed to CIRISMedical#1)."

### 6.3 "I want to understand how the EU HLEG 7 requirements map to CIRIS"

Path: EU HLEG batch → table of contents → §1.1 through §1.7 → each row links to the dimensions it attests. Or: principle correspondence table (Annex K §K.1-K.6) showing the Accord principle traversal.

### 6.4 "Show me everything tagged `prohibited:*`"

Path: wire primitive `prohibited:*` → dimensions using it (D04) → all attestations across batches → all source paragraphs invoking the primitive.

### 6.5 "Where are the disagreements between the 4 sources?"

Path: conflicts index → 5 CONF-* entries → each linked to involved dimensions + source paragraphs + disposition (e.g., CONF-01 → CIRISMedical#1).

### 6.6 "What's coming in CIRIS v1.5?"

Path: T-3 candidates index → 9 T3-* entries → each linked to source surfacing + priority + affected existing dimension (if any) + [CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20) for the formal proposal.

### 6.7 "Explain the methodology that produced this"

Path: top-level reading order (from README) — MISSION → METHODOLOGY → GOVERNANCE_FABRIC_MAPPING_STANDARD → LANGUAGE_PRIMER → batches → overlap analysis → audit → seed.

---

## 7. Search / filter facets

Suggested faceted-browse axes:
- **By Accord principle** (6 facets)
- **By tier** (STRONG-4 / STRONG-3)
- **By batch** (MH / EU / IEEE / ASEAN)
- **By institutional shape** (religious_magisterium / governmental_advisory / technical_society / multilateral_political)
- **By verdict** (clean / composed / partial / not-translated)
- **By wire-format family** (e.g., all `detection:*`, all `multilateral_participation:*`)
- **By conflict involvement** (dimensions involved in any CONF-*)
- **By T-3 surface** (dimensions with pending v1.5+ candidates)

Free-text search should index: glosses, source quotes, citations, regulatory-attestation language, convergence notes.

---

## 8. Calibration callouts to surface prominently

The Phase 4 audit found systematic translation losses. These should be **prominently displayed**, not hidden, so users don't over-read individual envelopes:

- **Per-dimension warning where applicable**: dimensions with absent batches (STRONG-3) should clearly show "absent from {batch} — reason" so users understand why coverage is 3-of-4, not 4-of-4.
- **Convergence note** field is load-bearing; render it as a callout, not body text.
- **Conflicts involving a dimension** should be flagged at the dimension detail page (not buried).
- **Source paragraphs with verdict `partial` or `not-translated`** should be marked so users know the wire envelope is incomplete.
- **`nuance_lost` annotations** should be visible alongside each wire envelope.
- **The Phase 4 audit synthesis** (`TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md`) should be linkable from every detail page as a "what's NOT captured" reference.

The framework's claim is that **convergence is on structural concern, not propositional agreement**. The browser should embody this — never let convergent attestations imply "all four sources say the same thing."

---

## 9. Out of scope / what NOT to display

- **Do NOT republish full third-party source documents.** Source quotes are ≤2 sentences each (fair use). For the full text of MH / EU HLEG / IEEE EAD / ASEAN, link to the authoritative URLs in the per-batch manifests.
- **Do NOT claim the Accord is "validated by" these documents.** Per [PRIOR_ART.md](PRIOR_ART.md) §5: convergent attestations are structural evidence, not validation; the four sources are not commenting on CIRIS. We mapped onto them.
- **Do NOT silently merge softness-erosion cases.** ASEAN's softer modals (3 confirmed cases) should be flagged where they appear, not silently elevated to the wire format's stricter strength.
- **Do NOT promote T-3 candidates as decided.** They are proposals filed at [CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20) for workshop discussion; not adopted.

---

## 10. Update discipline

The content surface updates through the seed. Triggers:

| Trigger | What changes | Browser action |
|---|---|---|
| New batch added (Phase 1-4 against a new source) | Seed `batches[]` adds entry; affected dimensions' `regulatory_attestations[]` gain entries; tier promotions possible (STRONG-3 → STRONG-4); new D28+ dimensions possible | Re-ingest seed; re-render dimension detail pages; new batch detail pages |
| Seed version bump | Stable IDs unchanged; regulatory attestations + wire primitives may refine | Re-ingest seed |
| CIRISAgent compliance docs filled (per-dimension PRs) | The `<!-- BEGIN HUMAN --> ... <!-- END HUMAN -->` regions populate with code references / observability / gaps | Re-pull CIRISAgent compliance docs |
| New conflict surfaced | `aggregate_indices.conflicts_surfaced` gains entry | Re-ingest seed |
| New T-3 candidate added | `aggregate_indices.t3_candidates_v1_5` gains entry | Re-ingest seed |

**Subscribe to**: commits to `SEED_DIMENSIONS.yaml` and `CIRISAgent/compliance/*` (the latter is in the other repo). For the response-side content (CONTRIBUTION_OBJECTS_*, manifests, audits) the v1.4 round-3 outputs are stable; future updates come through seed bumps.

---

## 11. Quick checklist before launch

- [ ] All 4 batches' source paragraphs rendered as detail pages, linked to their dimensions
- [ ] All 27 dimensions rendered with attestation density, regulatory attestations, wire primitives, Accord principle, convergence note
- [ ] All 6 Accord principles linked to their operative dimensions (the Annex K traversal)
- [ ] All 27 CIRIS Agent controls (when available from CIRISAgent) linked from their dimensions
- [ ] 5 conflicts surfaced with disposition (especially CONF-01 → CIRISMedical#1 routing)
- [ ] 9 T-3 candidates linked to the [CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20) workshop issue
- [ ] Bidirectional traversal: work → dimension → control AND control → dimension → works
- [ ] Stable URLs use the D01-D27 IDs (and CONF-NN, T3-NN) directly
- [ ] Calibration callouts present (nuance_lost, partial verdicts, softness-erosion notes)
- [ ] Source documents link out to authoritative URLs (per manifests), not re-hosted in the browser
- [ ] PRIOR_ART references rendered so users see this work in context (Jobin et al., Floridi & Cowls, Rome Call, Policy Cards, OSCAL-for-AI)

---

## 12. Contacts / questions

- **Content questions** (seed schema, calibration findings, dimension semantics): file an issue on this repo
- **Wire-format questions** (FSD-002 v1.4 grammar, runtime envelope format): file on [CIRISRegistry](https://github.com/CIRISAI/CIRISRegistry)
- **CIRIS Agent control questions** (code references, observability hooks): file on [CIRISAgent](https://github.com/CIRISAI/CIRISAgent)
- **Specialization questions** (e.g., CIRISMedical carve-outs): file on the relevant specialization repo

This document itself is maintained alongside the rest of the response artifacts — updates as the browser team identifies gaps.
