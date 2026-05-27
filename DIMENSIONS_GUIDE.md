# Guide to the 27 structural-evidence dimensions

**Source**: [`FOUR_BATCH_OVERLAP_ANALYSIS.md`](FOUR_BATCH_OVERLAP_ANALYSIS.md) §2 + §4
**Definition**: a "structural-evidence dimension" is a CIRIS prefix family that received convergent attestations from at least 3 of the 4 governance documents mapped (MH + EU HLEG + IEEE EAD + ASEAN).

**Count correction**: prior summary text said "22" (16 STRONG-4 + 6 STRONG-3). The actual data is **16 STRONG-4 + 11 STRONG-3 = 27**. The "6 STRONG-3" figure in the overlap analysis's §2.2 header was a tally error; the table itself lists 11. This guide uses the table.

**How to read each entry**: prefix-family name + one-line gloss + a per-batch attestation note + a one-line calibration caveat. Convergence is on the *structural concern*, not on equal strength of obligation or on propositional agreement across documents.

---

## Part A — STRONG-4 — 16 dimensions where **all four batches attest**

These are the load-bearing structural-evidence claim. Four institutionally-distinct senior governance frameworks (religious magisterium + governmental advisory + technical society + multilateral political body) independently engage each. **Attested by**: MH ✓ + EU HLEG ✓ + IEEE EAD ✓ + ASEAN ✓.

### 1. `non_maleficence:*` — soft-harm-avoidance baseline (117 attestations)
- **MH**: deception as dignity-violation (§107) | **EU HLEG**: prevent harm, ensure reliability (§1.2) | **IEEE EAD**: well-being requires not-causing-unintended-harm (Ch4 §0.a) | **ASEAN**: safe, secure, resilient (§B.3)
- Calibration: agreement at the soft-scalar layer; the absolute floor lives in `prohibited:*`.

### 2. `integrity:*` — "system holds together" structural anchor (132 attestations)
- **MH**: doctrinal continuity (§40) | **EU HLEG**: explicability for trust (§1.4) | **IEEE EAD**: state accountability under public scrutiny (Ch11 §I6) | **ASEAN**: lifecycle integrity, auditable, reproducible (§B.6)
- Calibration: ASEAN uses 44 distinct sub-leaves — densest family decomposition observed.

### 3. `justice:*` — vulnerability-priority + fairness (80 attestations)
- **MH**: lexical vulnerability priority (§76) | **EU HLEG**: voice to vulnerable populations (§1.7.d) | **IEEE EAD**: rights-based policy foundation (Ch10 §I1, 14 attestations) | **ASEAN**: fairness outcome testing (§B.2)
- Calibration: `justice:lexical_vulnerability_priority` (the v1.3 CST-driven closure) is independently invoked by all four sources — strongest single tie-breaker corroboration.

### 4. `prohibited:*` — categorical floor (104 attestations)
- **MH**: lethal autonomous weapons categorically excluded (§§197-198) | **EU HLEG**: cites EP Resolution 2018/2752(RSP) on LAWS | **IEEE EAD**: lethal autonomous weapons + categorical deception | **ASEAN**: autonomous lethal decisions + deceptive defaults forbidden
- Calibration: **the strongest convergence in the matrix** — four-source agreement at polarity-`-1`/constitutional/species. The LAWS prohibition is verbatim-corroborated.

### 5. `detection:*` — LensCore F-3 / RATCHET family (126 attestations)
- **MH**: structures of sin / aggregate expendability (§36) | **EU HLEG**: aggregate energy/carbon footprint (§1.6) | **IEEE EAD**: cultural norm drift, participation exclusion (Ch4, Ch5, Ch8) | **ASEAN**: temporal drift, intra-agent consistency (§B.2, §C.3)
- Calibration: three of four also engage `detection:distributive:access:*` (v1.3 universal-destination-of-goods closure).

### 6. `goal:*` — multi-scale belonging composite (60 attestations)
- **MH**: family/community/affiliations/species scales (§§148-156) | **EU HLEG**: Trustworthy AI for Europe → `goal:affiliations` (EU-jurisdiction) | **IEEE EAD**: well-being of all humans → `goal:species` (Ch4 §0.a) | **ASEAN**: regional ecosystem belonging → `goal:affiliations` (ASEAN-jurisdiction, 6 attestations)
- Calibration: every available `{scale}` value is exercised somewhere in the corpus.

### 7. `locality:decision:{scale}` — v1.3 subsidiarity closure (42 attestations)
- **MH**: decisions at lowest competent level (§§68-72) | **EU HLEG**: EU-level vs national supranational coordination (§III.0) | **IEEE EAD**: national policy + international R&D (Ch10) | **ASEAN**: regional ASEAN-level + community-level + national-level (§C.4, §E)
- Calibration: **first cross-source structural validation of the v1.3 subsidiarity addition**. ASEAN exercises `locality:decision:regional` as a first-deployment of that scale value.

### 8. `autonomy:*` — human-centric design + self-determination (51 attestations)
- **MH**: imago Dei autonomy (§107) | **EU HLEG**: Respect for Human Autonomy = first principle, no manipulation/coercion/deception (§1.1, 15 attestations) | **IEEE EAD**: user autonomy, data agency (Ch3, Ch4) | **ASEAN**: informational self-determination (§B.4 Human-centricity)
- Calibration: direct 1:1 mapping in EU HLEG; composition-based in the other three.

### 9. `fidelity:*` — faithful disclosure / faithful representation (65 attestations)
- **MH**: fidelity to Gospel via doctrinal development (§17) | **EU HLEG**: lifecycle responsibility (§1.7) | **IEEE EAD**: duty-bearer obligation to fulfill rights (Ch11) | **ASEAN**: algorithmic disclosure, human oversight (§C.4, §B.1 — 26 attestations, the densest)
- Calibration: ASEAN's fidelity-saturation is deployer-side framing; MH's is doctrinal-epistemic. Same prefix admits both shapes.

### 10. `beneficence:*` — positive duty toward dignity (45 attestations)
- **MH**: tech as creation-participation, species-scale beneficence (§§110-111) | **EU HLEG**: positive duty toward dignity (Unit 005) | **IEEE EAD**: well-being as central aim (Ch4 §0) | **ASEAN**: environmental stewardship as positive beneficence (§C.3)
- Calibration: lower count than `non_maleficence:*` reflects each tradition's "harm avoidance is more universally articulated than positive flourishing" — known pattern.

### 11. `multilateral_participation:{forum}:{kind}` — v1.3 closure (37 attestations)
- **MH**: UN-system reform advocacy + cyber-norms diplomacy (§§200-203, 224-227 — 8 MH) | **EU HLEG**: European Parliament resolutions + UN human-rights treaties | **IEEE EAD**: international R&D collaboration + cross-border policy exchange (Ch10) | **ASEAN**: 11 distinct `:asean:{kind}` envelopes across §E (densest single-forum exercise in federation history)
- Calibration: ASEAN's 11-`{kind}` saturation is the first stress test showing the `{kind}` slot scales gracefully.

### 12. `conscience:*` — agent-side faculty layer (24 attestations)
- **MH**: conscience as alētheia faculty + optimization-veto (§§111, 131-181) | **EU HLEG**: stop-button at any time, whistleblower protection (§III.1, §III.7) | **IEEE EAD**: epistemic humility under uncertainty, phronesis in design (Ch3 — 6 IEEE, densest) | **ASEAN**: HOTL override surface (§C.2)
- Calibration: heaviest in IEEE Ch3 (multi-tradition ethics) and MH (doctrinal explicit).

### 13. `testimonial_witness:{kind}` — v1.4 affected-party-voice closure (16 attestations)
- **MH**: displaced_worker, abuse_survivor, war_victim, displaced_migrant, etc. (§§81, 89, 138, 151, 166, 167, 173, 216, 217 — 11 MH) | **EU HLEG**: affected_worker, impacted_worker (§1.5.c, §III.5.d) | **IEEE EAD**: surveilled_person_refusal, on-the-ground_practitioner (Ch6, Ch7) | **ASEAN**: displaced_worker (§C.4)
- Calibration: **the v1.4 amendment is independently invoked by all four batches** — positive evidence the addition was correct. `{kind}` slot populated with diverse but interoperable values.

### 14. `witness_diversity:*` — stakeholder pluralism in design/testing (24 attestations)
- **MH**: signs-of-times-contribution + catholicity (3 MH) | **EU HLEG**: stakeholder consultation, red teams, stakeholder panels (§III.7) | **IEEE EAD**: 16 distinct values including ubuntu_five_moral_domains, intercultural_RI_dialogue (Ch7, Ch9) | **ASEAN**: varied user-testing backgrounds (§C.4)
- Calibration: IEEE saturation reflects engineering-society methodology density.

### 15. `moderation:*` — federation self-correction (5+ with adjacent coverage)
- **MH**: dialogue-as-negotiation (§§220-223) | **EU HLEG**: whistleblower protection + OOD attestation (§III.7) | **IEEE EAD**: `reconsideration:rollback_on_wellbeing_reduction` (Ch4) + ethics-board/audit-body `partner_role:*` constructions | **ASEAN**: OOD attestation (Annex A)
- Calibration: IEEE shifts some structural load to `partner_role:*` (ethics boards/audit bodies) instead of `moderation:*` directly. Composition is interoperable.

### 16. `method:*` — operational-design discipline (186 attestations — densest family)
- **MH**: 2 attestations (sparse — encyclical genre) | **EU HLEG**: 12 (trustworthy AI triad, AIA, explainable AI research, fallback methods) | **IEEE EAD**: 136 (densest — engineering-society genre) | **ASEAN**: 36 (privacy-enhancing tech, fairness tools, citizen feedback, community codevelopment)
- Calibration: density tracks each source's operational-design-discipline genre. Convergence reading is weaker than for principles — the wire format admits the asymmetry honestly.

---

## Part B — STRONG-3 — 11 dimensions with **one batch absent**

Each entry leads with **which batch does not attest** and why. The absent batch is consistent with the source's institutional shape — not substantive disagreement.

### Absent batch summary

| Absent | Count | Dimensions |
|---|---:|---|
| **MH absent** (5) | 5 | #19 `partner_role:*` · #23 `accountability:*` (named-axis) · #26 `key_boundary:*` · #27 `provenance:*` · #17 `transparency_log:*` (low density though non-zero) |
| **ASEAN absent** (5) | 5 | #18 `attestation:l{3,5}:*` · #21 `progress_measure:*` · #22 `expertise:*` · #24 `reconsideration:*` · #25 `credits:*` |
| **No batch absent** but classified STRONG-3 due to thin counts (1 use): | 1 | #20 `approach:*` (ASEAN 1 use only) |

MH absences cluster around secular-institutional / technical-infrastructure prefixes (the encyclical doesn't name registry roles, audit-build provenance, or encryption key boundaries). ASEAN absences cluster around verification-ladder / declared-expertise / appeal-rollback prefixes (the 2024 deployer-checklist genre stops at recommendation level, has no formal predecessor to reconsider, and frames competence at organizational rather than named-expert level).

---

### 17. `transparency_log:*` (CIRISVerify) — 40 attestations
- **Low-density in MH** (2) but non-zero | EU: 5 | IEEE: 23 | ASEAN: 10
- **Why MH is structurally low**: encyclical genre, not technical-disclosure framework. MH's functional analogue is the F-3 detector + `detection:correlated_action:ecology_of_communication:*`.

### 18. `attestation:l{3,5}:*` — verification ladder (11 attestations)
- **ABSENT in ASEAN** (0) | MH: 2 | EU: 4 | IEEE: 5
- **Why ASEAN absent**: the guide framing is normative-principles + risk-assessment, not federation-attestation ladder. Composition happens via accountability-tier wording.

### 19. `partner_role:*` (Registry roles) — 21 attestations
- **ABSENT in MH** (0) | EU: 1 | IEEE: 19 | ASEAN: 1
- **Why MH absent**: the encyclical names ecclesial relations rather than secular institutional partner-role taxonomies.
- Note: cross-source reinforced v1.5+ T-3 candidate here (dual-remit + trusted-disclosure-steward specialization patterns).

### 20. `approach:*` — decision-hierarchy strategic (32 attestations)
- **No batch fully absent** but ASEAN's single use is too thin for "solid" 4-batch — MH: 5 | EU: 3 | IEEE: 23 | ASEAN: 1
- **Why ASEAN thin**: ASEAN's checklist genre states recommendations as direct method/principle attestations rather than as named "approaches" within a goal-approach-method DAG.

### 21. `progress_measure:*` — declared-metric outcomes (10 attestations)
- **ABSENT in ASEAN** (0) | MH: 1 | EU: 1 | IEEE: 8
- **Why ASEAN absent**: the guide stops at recommendation-level rather than measurement-protocol level.

### 22. `expertise:*` — declared competence in domain (12 attestations)
- **ABSENT in ASEAN** (0) | MH: 1 | EU: 1 | IEEE: 10
- **Why ASEAN absent**: same as #21 — ASEAN frames competence at the organizational-governance level, not the named-expert level.

### 23. `accountability:*` (as named primary axis) — 28 attestations
- **ABSENT at named-prefix-level in MH** (0) | EU: 6 | IEEE: 3 | ASEAN: 19
- **Why MH absent at named-prefix-level**: MH covers accountability functionally via `integrity:*` + originator-obligations Accord §IV Ch 2 — architecturally structural rather than named-axis-attested.
- Note: ASEAN-distinctive `accountability:human_in_control` is single-source (HITL/HOTL/HOOTL).

### 24. `reconsideration:*` — reverse-axis appeal / rollback (6 attestations)
- **ABSENT in ASEAN** (0) | MH: 3 | EU: 2 | IEEE: 1
- **Why ASEAN absent**: forward-looking 2024 document with no formal predecessor to reconsider.

### 25. `credits:*` (substrate_building subject) — 9 attestations
- **ABSENT in ASEAN** (0) | MH: 4 | EU: 1 | IEEE: 4
- **Why ASEAN absent**: credit/recognition framing is implicit in §D National-level (workforce upskilling) rather than wire-attested.

### 26. `key_boundary:*` (CIRISEdge) — 11 attestations
- **ABSENT in MH** (0) | EU: 2 | IEEE: 7 | ASEAN: 2
- **Why MH absent**: encryption/key-management is not encyclical content. Composition happens via stewardship-of-trust language.

### 27. `provenance:*` (build_manifest) — 3 attestations
- **ABSENT in MH** (0) | EU: 1 | IEEE: 1 | ASEAN: 1
- **Why MH absent**: foundational technical-infrastructure rather than principled claim. The other three each invoke once at low density.

---

## How to use this guide

- **Looking up a federation prefix family**: find the entry; the 4-batch row tells you the structural-evidence weight.
- **Cross-document principle correspondence**: see [`FOUR_BATCH_OVERLAP_ANALYSIS.md`](FOUR_BATCH_OVERLAP_ANALYSIS.md) §3 for the principle-taxonomy mapping (CIRIS 6 / MH / EU HLEG 4 / IEEE EAD 8 / ASEAN 7).
- **What the convergence does NOT mean**: see [`TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md`](TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md) — convergent attestations show *the same structural concern was raised by all sources*, NOT that they prescribe the same response or hold the same strength of obligation. Modal-strength compression / softness-erosion / conditional flattening are quantified there.
- **Conflicts and tensions** (5 total, ~0.5% of units): see overlap-analysis §5.
- **T-3 candidates surfaced for v1.5+** (9 candidates): see overlap-analysis §6 and [CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20).
