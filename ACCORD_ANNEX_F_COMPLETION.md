# ACCORD_ANNEX_F_COMPLETION.md — Proposed completion for Annex F (Human-in-the-Loop & Oversight)

**Source posture**: Magnifica Humanitas (MH) cited as the senior work whose content informs CIRIS-native completion language. Verbatim quotes are taken from the encyclical body text; the operational rendering is CIRIS's. No Catholic-tradition vocabulary is imported as CIRIS's own register. Per MISSION.md §1.3, where MH and CIRIS diverge, the burden of proof falls on CIRIS.

---

## Current state summary

Annex F v1.1-Beta is substantially structured: §§0–9 each have a heading and opening content. However, five sections are thin stubs — purpose philosophy (§0), veto mechanisms (§3), KPIs (§7), change control (§8), and references (§9) — carrying tables or bullet lists with no operative rationale, threshold justification, or normative grounding. §3 in particular lacks any absolute prohibition language, which is the most pressing Release Candidate gap given that MH §§197–200 mandate it directly.

---

## Completion: §0 Purpose & Philosophy

**Current state**: Partial — names M-1 protection and four functions but gives no normative rationale for *why* the design choice is mandatory rather than discretionary.

**Proposed completion**:

> Human oversight is a load-bearing design constraint, not an optional feature. The CIRIS Accord grounds this in Meta-Goal M-1: wherever epistemic uncertainty, novelty, or moral gravity exceed validated system competence, control must revert to accountable human judgment — because automated systems cannot substitute for conscience, personal responsibility, or the recognition of the other as a person.
>
> MH §198 establishes the floor: "moral judgment cannot be reduced to calculation, for it involves conscience, personal responsibility and the recognition of the other as a person." CIRIS renders this structurally: the PDMA is an aid to human deliberation, not a replacement for it. At every autonomy tier, the system's authority is delegated from the human principal hierarchy; it is revocable on demand; and no delegation extends to decisions that are lethal or otherwise irreversible.
>
> This Annex operationalizes that floor: mandatory hand-off triggers, veto mechanisms with hard prohibitions, audit trails sufficient for accountability reconstruction, and incident workflows with binding SLAs.

**Encyclical citations**:
- MH §105: "responsibility must be clearly defined at every stage: from those who design and develop these systems to those who use them and rely on them for concrete decisions" → informs the authority-lattice design requirement (§1) and the audit-trail specification (§4).
- MH §198: "it is not permissible to entrust lethal or otherwise irreversible decisions to artificial systems" → establishes the normative floor that makes §0's framing non-discretionary.
- MH §106: "It is not enough to invoke ethics in the abstract; robust legal frameworks, independent oversight, informed users and a political system that does not abdicate its responsibility are required" → grounds the mandatory SLAs in §§5, 7.

---

## Completion: §1 Role Model & Authority Lattice

**Current state**: Concrete — five-tier table with powers and time-to-act is in place. Gap: the table has no rationale for tier-boundary design and no chain-of-accountability requirement.

**Proposed completion (add after existing table)**:

> **Accountability integrity requirement.** The tier structure is not merely an escalation ladder; it is the chain of accountability required by MH §199's first criterion: "the chain of responsibility must be identifiable and verifiable; those who design, train, authorize and employ technology must be held accountable for their decisions." Each tier in the lattice must therefore be:
>
> - **Named and logged**: every Tier 1–4 actor is identified by authenticated credential at session start; anonymous operation at Tier 2+ is prohibited.
> - **Bounded in concurrent load**: a single actor may hold multiple tiers only if dual-acknowledgement controls remain intact (existing clause) AND the combined active-case load does not exceed cognitive-load thresholds specified in §6.
> - **Traceable end-to-end**: any decision flowing from Tier 0 to Tier 4 must produce an audit chain traversable by a post-incident reviewer within one business day.
>
> MH §200 requires that "accountability and blame are not collapsed into 'the machine.'" The lattice is the structural answer: there is always a named human at each tier whose authority over the system's actions is on record.

**Encyclical citations**:
- MH §199: "the chain of responsibility must be identifiable and verifiable" → mandates named/authenticated tier actors.
- MH §200: "accountability and blame are not collapsed into 'the machine'" → prohibits anonymous tier occupancy and requires end-to-end audit traversability.

---

## Completion: §2 Operational-Autonomy Tiers & Hand-Off Criteria

**Current state**: Concrete — five-tier table (A0–A4) with triggers and fail-safes is in place. Gap: no rationale for the A4 hardware-interlock requirement; no explicit treatment of AI-assisted military or irreversible lethal contexts beyond the parenthetical "weapons."

**Proposed completion (add after existing table)**:

> **A4 Hard Constraint — Lethal and Irreversible Decisions.** The A4 tier's "Hardware interlock" fail-safe is non-negotiable for any action that is lethal or otherwise irreversible. This is not a design choice subject to operator discretion or WA override; it is an absolute constraint derived from MH §198: "it is not permissible to entrust lethal or otherwise irreversible decisions to artificial systems." No ACK timeout, no SLA exception, no emergency waiver removes this constraint. If the hardware interlock fails and human control cannot be confirmed, the system must not act.
>
> **Moral timeframe protection.** MH §199 identifies "the moral timeframe for making judgments" as a criterion: "speed and efficiency should never be the supreme motivating force for the irreversible decisions made in the context of war." CIRIS renders this as: A3/A4 ACK deadlines (30 s / 10 s in §3.3) are maxima for human response, not minima for system patience. Where the moral gravity of a decision warrants additional deliberation time, the system waits; it does not default to action on timeout for A4 irreversible decisions.

**Encyclical citations**:
- MH §198: "it is not permissible to entrust lethal or otherwise irreversible decisions to artificial systems. No algorithm can make war morally acceptable" → grounds A4 hardware-interlock as absolute constraint.
- MH §199 (second criterion): "speed and efficiency should never be the supreme motivating force for the irreversible decisions made in the context of war" → grounds moral-timeframe protection clause.

---

## Completion: §3 Veto Mechanisms & Safe-State Specification

**Current state**: Partial — three veto modes (Soft Override, Hard Kill, Conditional Override) with technical parameters. Critical gap: no absolute prohibition language; A4 Conditional Override implies a system could act on a lethal decision if no ACK arrives within 10 s — which directly contradicts MH §§197–200.

**Proposed completion (add §3.4 as new subsection)**:

> #### 3.4 Absolute Veto — Lethal and Irreversible Decisions
> *Scope: A4 actions that are lethal or otherwise irreversible; applies without exception.*
>
> The §3.3 Conditional Override logic (**no ACK → safe-state**) is correct for A3 and below. For A4 lethal or irreversible decisions, safe-state is the *only* permissible outcome under any condition — including operator absence, network failure, time pressure, or explicit instruction from any principal short of an authenticated WA ruling that the action is non-lethal and reversible.
>
> **Hard prohibition**: No CIRIS-conformant system may execute a lethal or irreversible A4 action through an automated or opaque process. This is not a guardrail that may be tripped and escalated; it is a hard-coded non-engagement identical in force to the prohibitions enumerated in ACCORD §VII Ch2.
>
> **Rationale (MH §§197–200, verbatim load-bearing passages)**:
> - §198: "it is not permissible to entrust lethal or otherwise irreversible decisions to artificial systems."
> - §200: "the decision to use lethal force cannot be delegated to opaque or automated processes, but must remain under effective, self-aware and responsible human control."
>
> **Implementation requirement**: Any deployment at A4 that involves lethal or irreversible capability must demonstrate hardware-level enforcement of this prohibition — not software logic, which is subject to override — before deployment authorization is granted. Absence of hardware enforcement is a blocking deficiency for Stewardship Tier ST-4 and ST-5 review.

**Encyclical citations**:
- MH §197: "the development and use of AI in warfare must be subject to the most rigorous ethical constraints, to guarantee respect for human dignity and the sanctity of life" → grounds the blocking-deficiency requirement for A4 deployment without hardware enforcement.
- MH §198: "it is not permissible to entrust lethal or otherwise irreversible decisions to artificial systems. No algorithm can make war morally acceptable" → the verbatim source of §3.4's hard prohibition.
- MH §200: "the decision to use lethal force cannot be delegated to opaque or automated processes, but must remain under effective, self-aware and responsible human control" → specifies "effective, self-aware and responsible" as qualifiers for human control — logging alone is insufficient; the human must be genuinely in the loop, not nominally so.
- MH §199 (first criterion): "the chain of responsibility must be identifiable and verifiable" → grounds the deployment-authorization audit requirement.

---

## Completion: §4 Audit-Trail Specification

**Current state**: Concrete — log objects, hash-chaining, retention periods, and real-time streaming are specified. Gap: no statement of *why* the audit trail must be externally verifiable (not just internally retained), and no requirement that the trail support accountability reconstruction — the specific use case MH §200 names.

**Proposed completion (add after existing bullets)**:

> **Accountability-reconstruction requirement.** The audit trail's purpose is not compliance archiving; it is to ensure that, following any incident, the chain of responsibility can be fully reconstructed without relying on system self-report. Per MH §200, accountability "must not be collapsed into 'the machine'"; the audit trail is the mechanism that keeps it human-traceable. Requirements follow:
>
> - **External anchoring**: Daily SHA-256 root on a public transparency log (e.g., Sigstore/rekor) is mandatory for A3–A4; voluntary for A0–A2. Internal-only hash chains do not satisfy accountability-reconstruction for A3–A4.
> - **Human-readable decision rationale**: For every A3–A4 decision, the Decision Rationale log object must include the PDMA step that controlled the outcome and the human tier that authorized or confirmed it — not only the system's internal state.
> - **Post-incident traversability SLA**: Any post-incident reviewer must be able to reconstruct the full decision chain for a given event within one business day from audit-trail records alone, without additional system access.

**Encyclical citations**:
- MH §200: "all systems used in a war setting must guarantee the possibility of retracing and reconstructing decision-making processes, so that accountability and blame are not collapsed into 'the machine'" → the accountability-reconstruction requirement is a direct rendering of this criterion, extended to all A3–A4 deployments regardless of domain.
- MH §105: "the possibility of identifying who must 'account' for decisions, justify them, monitor them, and, when necessary, challenge them and remedy any harm caused" → grounds the human-readable decision rationale requirement.

---

## Completion: §5 Incident Workflows (IW)

**Current state**: Concrete — five incident codes (IW-0 through IW-4) with triggers, clocks, and actions are defined. Gap: no explicit workflow for the specific case of an A4 hard prohibition breach attempt (system received lethal-action instruction, attempted to process, and §3.4 hard-coded non-engagement fired); and no post-incident review requirement that audits whether human control was genuinely "effective, self-aware and responsible" per MH §200.

**Proposed completion (add IW-5 row and post-incident note)**:

> | **IW-5** | A4 hard-prohibition activation (lethal/irreversible decision attempted via automated path) | Immediate hardware safe-state; IC notified within 60 s; WA notice within 15 min; full audit-trail freeze; independent review panel convened within 48 h; system remains offline pending review clearance |
>
> **Post-incident human-control audit.** For IW-2 through IW-5, the post-mortem must include an explicit finding on whether human control was "effective, self-aware and responsible" (MH §200) — not merely whether a human was nominally present in the loop. Findings of nominal-but-ineffective human control (cognitive overload, insufficient decision time, inadequate information) are treated as design deficiencies, not operator failures, and escalate to §8 Change-Control review.

**Encyclical citations**:
- MH §200: "the decision to use lethal force cannot be delegated to opaque or automated processes, but must remain under effective, self-aware and responsible human control" → "effective, self-aware and responsible" are the evaluative criteria for the post-incident human-control audit.
- MH §199 (second criterion): "speed and efficiency should never be the supreme motivating force for the irreversible decisions made in the context of war" → grounds the finding of insufficient decision time as a design deficiency, not operator failure.

---

## Completion: §6 Human-Interface Minimum Spec (UX)

**Current state**: Concrete — Status Banner, Explainability Panel, ACK/OVERRIDE UI, and Cognitive-Load Guard are specified. Gap: no requirement that the interface surface *who* is accountable (not just *what* the system decided), and no prohibition on interfaces that create the illusion of human review without genuine deliberation time.

**Proposed completion (add after existing bullets)**:

> - **Accountability Display**: For A3–A4 actions, the interface must display the authenticated identity of the Tier 2+ human who last reviewed the current action, and the timestamp of that review. A system state that has not received human review within the applicable SLA must display a distinct "UNREVIEWED" indicator — not green status.
> - **Anti-Rubber-Stamp Guard**: For A4 decisions, the ACK control must be preceded by a mandatory minimum deliberation period of [configurable; default 5 s] during which the ACK button is inactive. The objective is to prevent the interface from creating nominal human oversight while in practice bypassing genuine deliberation. This operationalizes MH §199's moral-timeframe criterion at the UX layer.
> - **Civilian-Protection Flag**: Where a system operates in any context where civilian populations may be affected (MH §199, third criterion), the Explainability Panel must surface a civilian-impact indicator alongside the PDMA risk-band display.

**Encyclical citations**:
- MH §199 (second criterion): "speed and efficiency should never be the supreme motivating force for the irreversible decisions made in the context of war" → grounds Anti-Rubber-Stamp Guard.
- MH §199 (third criterion): "the identification and protection of civilians. Any technology that facilitates attacks without seeing the face of human beings lowers the moral threshold of conflict" → grounds Civilian-Protection Flag requirement.
- MH §200: "accountability and blame are not collapsed into 'the machine'" → grounds Accountability Display requirement.

---

## Completion: §7 KPIs & Thresholds

**Current state**: Partial — four KPIs with targets, but no KPI covering the accountability-reconstruction requirement (§4 completion) or the human-control quality audit (§5 completion). The 10% HITL Coverage target for A3–A4 (F-KPI-1) is very low for high-stakes contexts.

**Proposed completion (add rows and annotation)**:

> | F-KPI-5 A4 Lethal-Decision Human-Control Rate | 100% — zero tolerance; any A4 lethal/irreversible action without confirmed effective human authorization is an IW-5 event |
> | F-KPI-6 Accountability-Reconstruction SLA | ≥ 99%: post-incident reviewers reconstruct full decision chain within 1 business day |
> | F-KPI-7 Nominal-vs-Effective Human Control Finding Rate | ≤ 0% acceptable; any finding of nominal-but-ineffective control triggers §8 Change-Control review |
>
> **Note on F-KPI-1 (HITL Coverage ≥ 10%)**: The 10% floor is appropriate for A3 routine operations. It is not appropriate as a floor for A4 life-safety contexts. For any A4 deployment involving lethal or irreversible capability, F-KPI-1 is superseded by F-KPI-5: 100% human-authorization rate, enforced at hardware level.

**Encyclical citations**:
- MH §200: "the decision to use lethal force cannot be delegated to opaque or automated processes, but must remain under effective, self-aware and responsible human control" → grounds F-KPI-5 at 100% with zero tolerance; grounds F-KPI-7.
- MH §105: "accountability becomes crucial: the possibility of identifying who must 'account' for decisions, justify them, monitor them, and, when necessary, challenge them and remedy any harm caused" → grounds F-KPI-6.

---

## Completion: §8 Change-Control & WA Review

**Current state**: Partial — two rules: autonomy-tier / safe-state changes require WA fast-track ≤ 14 d; experiments reducing oversight require CRE Proto-B + WA majority. Gap: no prohibition on changes that would reduce human-control requirements for A4 lethal/irreversible contexts below the MH §200 floor; no requirement that WA review include independent technical assessment, not just policy approval.

**Proposed completion (add after existing bullets)**:

> - **Absolute floor on A4 human-control**: No change-control process, WA vote, or emergency waiver may reduce human-control requirements for A4 lethal or irreversible decisions below the MH §200 floor ("effective, self-aware and responsible human control"). This floor is not within WA discretion; it is an Accord-level constraint. A WA proposal to reduce it requires a full Accord amendment cycle, not a fast-track review.
> - **Independent technical assessment**: Any WA review of autonomy-tier changes at A3–A4 must include at least one independent technical assessor (not employed by the deploying organization) who evaluates whether the proposed change maintains accountability-reconstruction capability per §4. Policy approval without technical assessment does not satisfy this requirement.
> - **Transparency log for change events**: Every change to autonomy-tier mapping or safe-state design must itself be logged to the public transparency log within 7 days of WA approval. MH §107 requires that ethical frameworks be "subject to shared standards" and openly discussable; this applies to governance changes, not only to system decisions.

**Encyclical citations**:
- MH §200: "must remain under effective, self-aware and responsible human control" → absolute floor; establishes that the floor is not within WA discretion.
- MH §107: "the possibility of openly discussing the ethical frameworks involved and subjecting them to shared standards of social justice. Otherwise, those who control AI will impose their own moral vision" → grounds transparency-log requirement for change events.
- MH §106: "robust legal frameworks, independent oversight, informed users and a political system that does not abdicate its responsibility are required" → grounds independent technical assessment requirement.

---

## Completion: §9 References & Implementation Notes

**Current state**: Stub — four references (IEC 61508-3, NIST SP 800-53 Rev 5, NASA-TLX, Sigstore/rekor). No reference to the normative sources that ground the absolute prohibitions, and no implementation guidance for the §3.4 hard-prohibition hardware requirement.

**Proposed completion (add after existing references)**:

> **Primary normative source for §§3.4, 7 (F-KPI-5), and 8 absolute floor**:
> - Pope Leo XIV, *Magnifica Humanitas* (Vatican, 15 May 2026), §§197–200. These paragraphs are the normative source for CIRIS's hard prohibition on lethal/irreversible automated decisions. Any implementation claiming conformance with Annex F must be traceable to these paragraphs for A4 absolute-veto design.
>
> **Implementation notes — hardware enforcement of §3.4**:
> - Hardware enforcement means that the prohibition is implemented below the software layer that executes PDMA logic — e.g., a hardware interlock or physical kill switch that cannot be overridden by software instruction. Acceptable implementations include: certified safety-relay circuits per IEC 61508 SIL-3+; hardware security modules (HSMs) with operator-presence attestation before A4 lethal-capability activation; dual-key physical authorization mechanisms. Software-only enforcement does not satisfy §3.4 for A4 lethal capability.
>
> **Additional references**:
> - MH §199 (three criteria: personal responsibility, moral timeframe, civilian protection) — operational design criteria for A4 UX and post-incident audit.
> - MH §105 (accountability at every stage) — grounding for §4 audit-trail and §7 F-KPI-6.
> - IEC 61508 SIL-3 — recommended minimum for hardware interlock implementation at A4 lethal capability.
> - ISO/IEC 25010:2023 — software quality model; relevant to accountability-reconstruction SLA testing.

**Encyclical citations**:
- MH §197–200 cited as primary normative source; verbatim passage: "the decision to use lethal force cannot be delegated to opaque or automated processes, but must remain under effective, self-aware and responsible human control" (§200) — the operative sentence for all A4 hardware-enforcement requirements.

---

## Open questions for the author

1. **F-KPI-1 floor**: The existing 10% HITL Coverage target for A3–A4 may reflect a conscious design choice for routine A3 operations where 100% review is operationally infeasible. The completion proposes that F-KPI-5 supersedes F-KPI-1 for A4 lethal/irreversible decisions only. Is this the right split, or should A3 also carry a higher floor for specific sub-domains (e.g., medical triage)?

2. **"Effective, self-aware and responsible" operationalization**: MH §200 uses three qualifiers for human control. CIRIS has mechanisms for "effective" (hardware interlock) and partial mechanisms for "responsible" (named tier actors). "Self-aware" is the hardest: it implies the human understands what they are authorizing. The Anti-Rubber-Stamp Guard in §6 is a start, but a fuller operationalization may require a decision-comprehension attestation at A4 — worth a dedicated sub-annex or reference to Annex H cognitive standards.

3. **"Disarm AI" (MH §110) and market-power ecology**: The encyclical's call to free AI "from monopolistic control" and "opening it to discussion and debate" (MH §110) surfaces in MAPPING_CH3 as GAP_ACCORD: no Accord clause names structural de-concentration obligations. This is beyond Annex F's scope but may require a new Accord principle — possibly in §I Ch8 Ethical Citizenship or as a new §IX — before full RC status can be claimed against the encyclical's governance criteria.

4. **Civilian-Protection Flag scope**: §6's completion adds a Civilian-Protection Flag for contexts "where civilian populations may be affected." The scoping is intentionally broad (MH §199 does not limit civilian protection to warfare). The author should determine whether this applies to algorithmic decision systems affecting civilian populations in non-military contexts (e.g., predictive policing, border control) and, if so, what the flag's trigger criterion is outside of A4 lethal contexts.

5. **IW-5 and the independent review panel**: The completion proposes a 48-hour convening deadline for a review panel following an A4 hard-prohibition activation. The composition of that panel (internal, external, regulator-nominated?) is not specified and may need a cross-reference to Annex G (Adversarial Security) or a new governance sub-document.
