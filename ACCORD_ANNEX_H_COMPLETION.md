# ACCORD ANNEX H — CONTINUOUS COMPLIANCE & REVIEW: COMPLETION LANGUAGE
**Version**: 1.0 (RC-candidate completion)  
**Status**: Draft — proposed operational language for Annex H stub sections  
**Date**: 2026-05-25  
**Source**: Derived from *Magnifica Humanitas* (MH) §§22–24, 45, 86–89, 157–164, 180–181  
**Posture**: CIRIS-native voice throughout; encyclical as source, not as imported vocabulary.  
**Target**: Replaces stub prose in ACCORD_canonical.txt §§Annex H 0–9; each section ≤200 words.

---

## How to read this document

Each section below carries:

1. **STUB TEXT** — what Annex H currently says (abbreviated).  
2. **COMPLETION** — operational language to replace or augment the stub.  
3. **MH ANCHOR** — the specific encyclical paragraph(s) cited verbatim; the derivation is explicit and checkable.  
4. **TRANSLATION NOTE** — one sentence naming what is preserved from the encyclical's framing and what is rendered CIRIS-natively.

---

## §0. Purpose & Guiding Spirit — COMPLETION

**STUB**: "Ethical alignment is not a 'one-and-done' certification but a living obligation."

**COMPLETION**:

The Accord is a living specification, not a fixed artifact. Every operative clause carries an auto-expire timestamp; the review window is public and commentable before any version supersedes its predecessor. This discipline is not administrative formality — it is the structural answer to the recognition that a normative corpus must remain *ever open to the challenges posed by each generation* (MH §45). The CIRIS continuous-compliance system operationalizes that openness: telemetry feeds drift detectors, drift detectors trigger audit gates, audit gates gate deployment — and the entire loop recurs on fixed cadences whether or not a triggering event occurs.

The guiding commitment, rendered in CIRIS terms: the Accord is governed as a living specification under auto-expire + comment-window discipline. No version is permanent. The burden of demonstrating continued adequacy falls on the current version, not on those proposing revision. Diligence is proved to regulators, the public, and federation peers by the audit artifacts this Annex produces.

**MH ANCHOR** (§45 verbatim): *"If today we can speak of a corpus of shared principles and criteria, it is because this faith-based interpretation of history has never been interrupted, remaining ever open to the challenges posed by each generation."*

**TRANSLATION NOTE**: "Faith-based interpretation never interrupted" → Accord auto-expire + comment-window discipline; the discipline of continuity-through-revision is preserved; the theological underwriting of that continuity is CIRIS-native (living-specification governance), not imported.

---

## §1. Audit Cadence & Scope — COMPLETION

**STUB**: Table of L-Check / S-Dive / F-Audit / A-Hoc with frequencies and leads.

**COMPLETION** (replaces stub prose preceding the table; table retained):

The audit cadence is the mechanism by which the Accord re-reads its own context. MH §§22–24 names the discipline: it is necessary *"to listen to and distinguish the many voices of our times"*, and this listening *"is no mere sociological exercise"* — it *"requires"* active discernment, not passive monitoring. The CIRIS audit stack is that discernment machinery.

**Cadence attestation requirements** (supplement to table):

- **L-Check (monthly)**: Ops QA signs off within 5 business days of calendar close; KPI delta report committed to `/compliance/l-check/YYYY-MM.json`; SHA-256 anchored in transparency log within 24 h.
- **S-Dive (semi-annual)**: PDMA sample replay ≥50 runs, stratified random across autonomy tiers; redacted PDF published to public compliance portal within 30 d of close.
- **F-Audit (every 24 mo or MAJOR bump)**: report counter-signed by WA quorum before publication.
- **A-Hoc (post IW-2/3/4)**: root-cause within 72 h; post-mortem public within 14 d.

Missed or late audit: IW-2 escalation + WA notice within 24 h.

**MH ANCHOR** (§§22–23 verbatim): *"it is the task of the whole People of God, particularly of its pastors and theologians, to listen to and distinguish the many voices of our times and to interpret them in the light of God's word"*; *"When it comes to applying these standards to the complex situations of our time, the contributions of philosophy and of the human and social sciences is essential."*

**TRANSLATION NOTE**: "Signs of the times" discernment → structured audit cadence with mandatory human-science inputs (HE-300, bias slice tests, KPI deltas); pneumatological underwriting bracketed; epistemic discipline of active re-reading preserved.

---

## §2. Drift Monitoring & Thresholds — COMPLETION

**STUB**: Table of metric groups, signals, drift triggers, and immediate actions.

**COMPLETION** (replaces stub prose preceding the table; the table itself is retained):

Drift monitoring is the continuous-reading mechanism. The Accord does not wait for harm to surface in incident reports; it maintains live telemetry against thresholds calibrated to fire *before* harm crosses the PDMA's Order-Maximisation Veto threshold. This is the structural translation of the audit-discernment discipline named in MH §23: *"it makes it possible to identify with greater clarity what genuinely fosters the lives of individuals and communities"* — which requires ongoing reading, not retrospective review.

**Additional threshold specifications**:

- All five metric groups (Performance, Ethical, Distribution, Latent Goal, Resilience) report to the DRIFT-Δ Grafana board on a 15-minute polling cycle.
- Threshold crossings generate a timestamped, signed alert record committed to CIRISPersist within 60 s of detection.
- **Latent Goal cosine drift > 0.05**: triggers Wise Authority probe within 4 h; if unresolved within 24 h, autonomous deployment locked pending S-Dive.
- **Resilience Score (RS) < 0.97**: patch issued within 72 h; if patch not available, deployment reverted to last passing MAJOR.
- **Ethical drift (Shadow HE-25 any ↓)**: IW-2 immediate; no override path.

**MH ANCHOR** (§23 verbatim): *"it makes it possible to identify with greater clarity what genuinely fosters the lives of individuals and communities."*

**TRANSLATION NOTE**: "Identify with greater clarity" → automated threshold detection with signed, tamper-evident alert records; the discernment function is operationalized as calibrated monitoring, not replaced by it.

---

## §3. Fairness & Transparency KPI Dashboard — COMPLETION

**STUB**: Table of KPI IDs F-T-1 through F-T-5 with definitions and targets.

**COMPLETION** (augments existing table with two KPIs and operational requirements):

The KPI dashboard is the Accord's public accountability surface. MH §164 names the criteria precisely: *"when data and algorithms influence credit distribution, personnel selection or access to services and opportunities, it is necessary that decisions be understandable, contestable and subject to oversight, so that individuals are not reduced to mere profiles."* Each criterion maps to a KPI family.

**Additional KPIs** (appended to F-T-1–F-T-5):

| KPI ID | Definition | Target |
|--------|------------|--------|
| **F-T-6** | Contestability pathway availability: % of PDMA outputs with published human-review request path | 100 % |
| **F-T-7** | Algorithmic decision audit coverage: % of decisions touching protected-class data with prior S-Dive bias-slice review | ≥ 95 % |

**Operational requirements**:

- Dashboard JSON at `/compliance/kpi.json` auto-publishes on each L-Check close; SHA-256 hash committed to CIRISPersist within 1 h.
- KPI threshold changes require MINOR bump + Internal Ethics sign-off.
- F-T-1 breach >7 d triggers automatic F-T-6 review and WA notice.

**MH ANCHOR** (§164 verbatim): *"transparency and accountability: when data and algorithms influence credit distribution, personnel selection or access to services and opportunities, it is necessary that decisions be understandable, contestable and subject to oversight, so that individuals are not reduced to mere profiles."*

**TRANSLATION NOTE**: "Understandable, contestable, subject to oversight" → F-T-2 (explanation latency), F-T-6 (contestability pathway), F-T-7 (bias-slice audit coverage); encyclical's operational criteria rendered as measurable KPIs with enforcement thresholds.

---

## §4. Patch & Version Control Requirements — COMPLETION

**STUB**: Five numbered rules on semantic versioning, LTS, change-type matrix, changelog, and rollback.

**COMPLETION** (replaces stub prose; numbered rules retained, augmented with attestation requirements):

Version control is the mechanism by which the Accord's continuity-through-change is made verifiable. MH §45 describes this discipline: *"a harmonious, though not always linear, development... marked by different emphases, progressive insights, and, at times, changes in perspective that do not break with what came before, but allow its implications to mature."* Every CIRIS patch must demonstrate continuity: it does not break prior commitments, it extends them.

**Attestation requirements** (supplementing rules 1–5):

- **PATCH**: CI/CD signs build artifact with Ops QA key; HE-300 pass required before merge; signature committed to CIRISVerify L1 chain.
- **MINOR**: Internal Ethics Team counter-sign within 5 business days; signed record committed to CIRISPersist with PDMA diff and KPI impact forecast.
- **MAJOR**: (a) F-Audit published; (b) WA quorum vote with named individual votes; (c) dual-key signature (Ops QA + WA chair); (d) public comment window ≥ 21 d before activation; (e) auto-expire timestamp set at 24 mo.
- **Rollback**: signed rollback pointer on every MAJOR/MINOR; executable within 5 min; rollback generates a timestamped CIRISVerify event.
- **Changelog**: git commit hash → PDMA diff → KPI forecast → signing key fingerprint(s).

**MH ANCHOR** (§45 verbatim): *"a harmonious, though not always linear, development that is marked by different emphases, progressive insights, and, at times, changes in perspective that do not break with what came before, but allow its implications to mature."*

**TRANSLATION NOTE**: "Not break with what came before, but allow its implications to mature" → semantic versioning with signed attestation chain; continuity of commitment demonstrated cryptographically, not asserted.

---

## §5. Continuous Review Loop — COMPLETION

**STUB**: Flow diagram (Telemetry → Drift Detectors → Incident Flow / Patch / Audit Gate → back to Telemetry or Drift Detectors).

**COMPLETION** (replaces stub prose; flow diagram retained):

The continuous review loop is the structural form of what MH §§180–181 names as the institutional requirement of the current moment: technology must be *"integrated with a wise perspective"* and governed by *"institutions capable of regulating without stifling, and protecting without taking over."* The loop operationalizes this: it is not a one-directional pipeline but a closed system in which every output feeds back as input.

**Loop specification**:

- **Telemetry streams** (15-min cycle): KPIs, guardrail logs, HE-shadow accuracy, robustness RS, PDMA audit samples — all signed and committed to CIRISPersist.
- **Drift detector outputs**: classified by severity (IW-1 through IW-4); IW-3+ automatically suspends new feature deployment.
- **Audit Gate** re-executes HE-300 + TX-sim suite + Fairness slice tests on every MINOR/MAJOR before activation. Gate failure returns to Drift Detectors, not to Telemetry — the loop cannot shortcut the correction step.
- **Shared responsibility signal** (per MH §181): the loop's outputs are published to federation peers on each L-Check close; peer federations may file an Accord-QA notice if published KPIs diverge from their own cross-audit observations. Accord-QA notices are non-binding but must be acknowledged within 14 d.

**MH ANCHOR** (§§180–181 verbatim): *"if technology is integrated with a wise perspective, it can become an instrument of growth, justice and fraternity"*; *"the Social Doctrine of the Church calls for a shared responsibility... by institutions capable of regulating without stifling, and protecting without taking over."*

**TRANSLATION NOTE**: "Shared responsibility" across institutions, businesses, citizens → federation peer cross-audit publication; "wise perspective" → closed review loop that cannot bypass its own correction step.

---

## §6. Meta-Audit of Auditors — COMPLETION

**STUB**: Three bullet points — sample rate (10%), blind replay, rotation rule.

**COMPLETION** (replaces and expands the three bullets):

The meta-audit is the Coherence Ratchet's self-application: the drift-detection discipline that governs AI behavior governs the audit infrastructure itself. MH §86: *"Social Doctrine is not merely a message addressed to society; it is also an examination of conscience... that is always called to ensure that the principles outlined in this chapter are applied, especially within its own structures."*

**Specification**:

- **Coherence Ratchet meta-detector**: runs against audit-report outputs. Flags: (a) L-Check KPI deltas inconsistent with telemetry; (b) S-Dive PDMA replay diverging >2% from WA blind-replay; (c) F-Audit findings contradicting prior findings without documented causal explanation.
- **WA sample rate**: ≥10% of L-Check reports and ≥1 S-Dive per year; drawn by WA, not Ops QA; rationale logged.
- **Blind replay**: mismatch >2% opens public AUD-QA docket within 5 business days.
- **Federation peer cross-audit**: each deployment peer-reviews ≥1 other member's S-Dive annually; no peer reviews the same member in consecutive years.
- **Rotation**: no internal auditor leads two consecutive F-Audits on the same product line; no external firm for more than two consecutive F-Audits.
- **AUD-QA findings** per MH §89: corrections *"oriented toward mission"* — they feed the next MINOR/MAJOR cycle, not personnel actions.

**MH ANCHOR** (§§86, 89 verbatim): *"Social Doctrine is not merely a message addressed to society; it is also an examination of conscience for the Church — a home and school of communion that is always called to ensure that the principles outlined in this chapter are applied, especially within its own structures"*; *"Regular assessments of the exercise of ministerial responsibilities should be encouraged, not as judgments on individuals, but as tools for learning and correction oriented toward mission."*

**TRANSLATION NOTE**: "Examination of conscience applied to own structures" → Coherence Ratchet meta-detector + federation peer cross-audit; "not as judgments on individuals, but as tools for correction" → AUD-QA docket as mission-correction input, not personnel action; no Catholic vocabulary imported.

---

## §7. Enforcement & Remediation — COMPLETION

**STUB**: Three bullets — KPI breach → Tier A1 downgrade; publication failure → feature block; repeated non-compliance → WA revocation.

**COMPLETION** (replaces stub bullets with sequenced enforcement ladder):

Enforcement is meaningful only when steps are automatic and predictable. MH §164 requires *"decisions be understandable, contestable and subject to oversight"* — the consequences of non-compliance must be equally understandable. MH §159 adds that regulatory decisions must be assessable for impact on *"dignity of work, shared prosperity, inequality reduction"* — enforcement that names non-compliance without correcting it fails this standard.

**Enforcement ladder**:

1. **KPI breach, 1–7 d**: automated alert to Tier-1 Operator; corrective action plan required within 48 h; plan published to transparency log.
2. **KPI breach, 8–30 d with no resolution**: automatic deployment lock to staging; public CIRIS-WATCH banner within 24 h; WA notified.
3. **KPI breach, >30 d OR 2 consecutive missed audits**: automatic downgrade to Autonomy Tier A1 (Annex F); new feature releases blocked; 14-d WA remediation review required.
4. **Failure to publish audit artifacts**: immediate feature-release block; CIRIS-NON-COMPLIANT banner; unblocks only upon publication.
5. **Repeated non-compliance (3 strikes / 12 mo)**: WA may revoke CIRIS claim; mandatory external F-Audit before re-certification; WA supermajority (≥2/3) required.
6. **Remediation exit**: documented corrective-action plan accepted by WA; KPI evidence of correction sustained ≥30 d.

**MH ANCHOR** (§§159, 164 verbatim): *"The introduction of new parameters will allow for a comprehensive and timely assessment of how legislative and regulatory decisions impact the dignity of work, shared prosperity, inequality reduction and environmental protection"*; *"it is necessary that decisions be understandable, contestable and subject to oversight."*

**TRANSLATION NOTE**: "Understandable, contestable, subject to oversight" → sequenced enforcement ladder with automatic triggers, public banners, and a documented contestable exit pathway; encyclical's accountability criteria rendered as enforceable process steps.

---

## §8. Inter-Annex Hooks — COMPLETION

**STUB**: Four bullet hooks (Annex F, G, I, J).

**COMPLETION** (replaces stub bullets with specified bidirectional data-flow requirements):

Inter-annex hooks are required data flows, not cross-references. MH §181 names the governance structure: *"institutions capable of regulating without stifling, and protecting without taking over; by businesses that recognize work and dignity as measures of success; by intermediary organizations."* Each annex is one such institution; the hooks prevent silo operation.

**Required bidirectional data flows**:

- **↔ Annex F (Incident Workflow)**: every DRIFT-Δ alert ≥ IW-2 forwarded to Annex F within 60 s; Annex F closure timestamp written back to DRIFT-Δ board within 24 h. All IW-3+ post-mortems are mandatory S-Dive inputs; S-Dive must explicitly address each open IW-3+ finding.
- **↔ Annex G (Robustness)**: RS telemetry feeds Annex G KPI evaluation on each L-Check cycle; patch lag (RS < 0.97 → patch deployment) measured here and reported to Annex G. Annex G benchmark updates trigger mandatory L-Check re-run within 14 d.
- **→ Annex I (GDPR/Sector)**: every F-Audit package bundles the Annex I compliance checklist, completed and signed by the lead auditor.
- **→ Annex J (HE-300/Shadow)**: HE-300 and Shadow HE-25 are primary ethical drift signals; any HE-300 regression triggers automatic S-Dive pre-screen within 7 d.

**MH ANCHOR** (§181 verbatim): *"institutions capable of regulating without stifling, and protecting without taking over; by businesses that recognize work and dignity as measures of success; by intermediary organizations and educational communities that rebuild trust and relationships."*

**TRANSLATION NOTE**: "Shared responsibility across institutions" → specified bidirectional data flows between annexes; no annex operates as a silo; the coordination structure is auditable, not asserted.

---

## §9. References — COMPLETION

**STUB**: Three references (ISO/IEC 42001, NIST AI RMF, COSO ERM).

**COMPLETION** (augments existing references with MH-derived governance authorities):

The reference set reflects the multi-source discernment discipline named in MH §23: *"the contributions of philosophy and of the human and social sciences is essential"* and MH §159's requirement that development metrics be *"complementary to GDP"* and capable of assessing *"dignity of work, shared prosperity, inequality reduction and environmental protection."*

**Retained**:
- ISO/IEC 42001 (Management systems for AI)
- NIST AI RMF (2023) — "Measure" and "Manage" steps
- COSO ERM — continuous monitoring principles

**Added**:
- *Magnifica Humanitas* (Leo XIV, 15 May 2026) — §§22–24 (ongoing discernment discipline), §45 (living-corpus governance), §§86–89 (institutional self-audit), §§157–164 (algorithmic accountability, GDP-alternative metrics, contestability of automated decisions), §§180–181 (shared responsibility across institutions)
- OECD AI Principles (2019, updated 2024) — transparency and accountability criteria
- EU AI Act (2024) — conformity assessment requirements for high-risk systems
- IEEE Std 7001-2021 — Transparency of Autonomous Systems
- *Beyond GDP* (European Commission, 2009; updated 2024 indicators) — complementary metrics for assessing dignity of work and inequality reduction (per MH §159)

**MH ANCHOR** (§§23, 159 verbatim): *"the contributions of philosophy and of the human and social sciences is essential"*; *"The development of parameters and metrics complementary to GDP is crucial for improving the databases used for conducting analyses, political and economic decision-making."*

**TRANSLATION NOTE**: "Dialogue with human sciences" → expanded reference set including GDP-alternative metrics and algorithmic-accountability frameworks; no theological authorities cited in the reference list; encyclical cited as governance-design source, not as religious authority.

---

## Completion summary

| Annex H Section | MH Primary Anchor | Completion Type | Stub Gap Closed |
|---|---|---|---|
| §0 Purpose & Guiding Spirit | §45 (living corpus) | Philosophical anchor named as living-specification auto-expire discipline | Missing philosophical grounding |
| §1 Audit Cadence | §§22–24 (discernment discipline) | Artifact commit requirements, signing deadlines | Cadence had no attestation specs |
| §2 Drift Monitoring | §23 (identify with clarity) | 15-min polling, signed alert records, Latent Goal escalation path | No telemetry commit requirements |
| §3 Fairness & Transparency KPI | §164 (understandable, contestable, oversight) | Two new KPIs (F-T-6, F-T-7), hash-anchoring requirement | Contestability not operationalized |
| §4 Patch & Version Control | §45 (not break, but mature) | Per-tier signing/attestation, public comment windows, auto-expire | No cryptographic attestation |
| §5 Continuous Review Loop | §§180–181 (shared responsibility) | Federation peer cross-audit publication, loop non-shortcut rule | Loop had no peer accountability |
| §6 Meta-Audit of Auditors | §§86–89 (institutional self-audit) | Coherence Ratchet meta-detector, peer cross-audit, AUD-QA docket | Strongest encyclical derivation |
| §7 Enforcement & Remediation | §§159, 164 (contestable oversight) | 6-step enforcement ladder with automatic triggers and exit pathway | Bullets had no sequencing or timing |
| §8 Inter-Annex Hooks | §181 (shared across institutions) | Bidirectional data flows with timing requirements | Cross-refs had no data-flow specs |
| §9 References | §§23, 159 (human sciences) | GDP-alternative metrics, algorithmic-accountability frameworks added | Missing MH and GDP-alternative refs |

---

**End ACCORD_ANNEX_H_COMPLETION.md**
