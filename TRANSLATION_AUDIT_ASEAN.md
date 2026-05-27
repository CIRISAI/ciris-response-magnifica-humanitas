# TRANSLATION_AUDIT_ASEAN.md — Phase 4 Diagnostic Audit (Calibration)

**Batch**: `asean_guide_v1`
**Audit date**: 2026-05-27
**Auditor**: Phase-4 audit sub-agent (Opus 4.7) with independent reading-before-comparison
**Posture**: DIAGNOSTIC, CALIBRATION-ORIENTED, NON-CORRECTIVE. The wire envelope is acknowledged
to lose detail by construction; this audit characterises the systematic shape of that loss for
the ASEAN batch so the framework can calibrate.

---

## §1 — Sampling methodology

Per the audit brief: ~15 units distributed 5 clean / 5 composed / 3 partial / 2 not-translated,
spanning all five wire-envelope output files. Sample selected to include the load-bearing
verifications named in the brief:

- At least 2 of the 7 ASEAN Guiding Principles (Section B): selected §B.1.0, §B.2.0, §B.4.0,
  §B.4.1, §B.4.3 (five samples — over-quota on principles because the principles are the
  primary cross-document comparison axis).
- At least 1 unit from Section C.2 (HITL/HOTL/HOOTL): selected §C.2.e, §C.2.f, §C.2.g (all
  three — the load-bearing oversight-ladder triad must be evaluated together).
- At least 1 unit from Section E (regional-level / multilateral_participation:asean:*):
  selected E.001, E.002, E.005 (three samples).
- At least 2 from Annex A risk assessment: selected A.1.1, A.1.3, A.2.1, A.3.2, A.4.18, A.5.3
  (six samples — over-quota because Annex A is the question→assertion translation surface).
- One unit from Section A introduction (§A.intro) and one from Annex B (entire-annex
  not-translated finding) to round out distribution.

**Independent-reading discipline**: for each sampled unit, the source paragraph was read first
from the asean_guide.txt at the cited line range to form an independent reading of (a) what
operational obligation the paragraph asserts, (b) its modal strength (must / should /
consider / may), (c) what nuance the paragraph carries. Only then was the wire envelope read
and compared.

**Total sampled units**: 17 (over the 15 target — extra coverage on principles, Annex A, and
HITL ladder, all load-bearing).

**Distribution targets vs actuals in the sample** (file-claimed verdict, not the audit's
reclassification — see §2 for per-unit faithfulness verdict, which is a DIFFERENT axis):

| File-claimed verdict | Target | Actual sampled |
|---|---|---|
| clean | 5 | 8 |
| composed | 5 | 6 |
| partial | 3 | 3 |
| not-translated | 2 | 2 (§A.0 header T-2 + Annex B aggregate T-2) |

Note: "faithfulness" in this audit is a DIFFERENT axis from the file's clean/composed/partial
verdict. A unit can be `verdict: clean` AND `faithfulness: over-reach` (the wire envelope is
internally clean as a translation but over-claims relative to source modal strength).

---

## §2 — Per-unit audit

Format per unit: source line range; my independent reading of the source's operative claim
(formed before reading the wire envelope); the file's wire envelope summary; faithfulness
classification with specific nuance lost noted.

---

### §2.1 — §A.intro — AI as adaptive technology; values alignment

**Source** (lines 228–238): Opening introduction. Three substantive claims: (a) AI adapts on
its own ("decisions today may differ from tomorrow"); (b) AI should be treated DIFFERENTLY
from other software because capabilities outpace monitoring + low entry barriers; (c)
decisions made by AI should be ALIGNED with national and corporate values + broader ethical
and social norms. Strength: standard "should" framing. Nuance: regional-anchoring ("Southeast
Asia is no exception"); the "transformative potential" rhetoric is T-2-flavoured framing.

**Wire envelope**: composed — `integrity:ai_distinct_from_other_software` (0.85/0.80) +
`fidelity:alignment_with_values` (0.85/0.80). cohort_scope species + community.

**Faithfulness**: **faithful**. Both load-bearing operative claims are captured. The
regional-anchoring and "transformative potential" nuance is correctly classified T-2 (the
unit's own nuance_lost field acknowledges this). The score 0.85 captures modal softness
("should" not "must") reasonably.

**Nuance lost**: the multi-aspect rationale of WHY AI is different (capabilities outpacing
monitoring + decentralised development + open-source proliferation) is collapsed into the
context field but not into separate envelopes. Acceptable.

---

### §2.2 — §B.1.0 — Transparency definition (Principle 1)

**Source** (lines 400–403): "Transparency refers to providing disclosure on when an AI system
is being used and the involvement of an AI system in decision-making, what kind of data it
uses, and its purpose." Strength: definitional, declarative. Operative claim: AI use must
be disclosed; users will become aware and can make an INFORMED CHOICE of whether to use.

**Wire envelope**: composed — `transparency_log:ai_involvement_disclosure` (1.0/0.90,
constitutional) + `autonomy:informed_choice_to_use_ai` (1.0/0.85, constitutional).

**Faithfulness**: **faithful with mild over-reach on mutability**. The transparency principle
is real but the source paragraph is a definitional sentence, not a constitutional hard
constraint per se. Marking mutability:constitutional binds the disclosure obligation more
strongly than "Transparency refers to providing disclosure" suggests on its own — though
this is mitigated because §B.4.3 (dark patterns) and the never-deny-AI operational rule in
CIRIS language_guidance independently justify the constitutional floor. The wire form
correctly reaches for the CIRIS-side constitutional anchor (never-deny-AI) rather than the
ASEAN-side modal softness. Defensible composition; not a distortion.

**Nuance lost**: "informed choice of whether to use" is stronger than mere opt-out — the wire
form attests this via `autonomy:informed_choice_to_use_ai` cleanly, but consumers reading
without the context field may compress to "disclosure → informed consent" which loses the
upstream "whether to engage with AI at all" semantic. The file's own nuance_lost flags this.

---

### §2.3 — §B.2.0 — Fairness/Equity opening (Principle 2)

**Source** (lines 483–488): "Deployers SHOULD have safeguards in place to ensure that
algorithmic decisions do not further exacerbate or amplify existing discriminatory or unjust
impacts across different demographics and the design, development, and deployment of AI
systems SHOULD NOT result in unfair biasness or discrimination. An example of such
safeguards would include human interventions and checks on the algorithms and its outputs.
Deployers of AI systems SHOULD CONDUCT regular testing." Strength: "should" modal throughout
— advisory/voluntary per §1 ("voluntary guide"). No "must," no "shall."

**Wire envelope**: composed — `prohibited:discrimination` (-1.0/1.0, **constitutional**) +
`fidelity:human_oversight_governance` (1.0/0.85) + `method:bias_testing_and_rectification`
(1.0/0.85).

**Faithfulness**: **over-reach** on the `prohibited:discrimination` envelope, but only
calibrationally. The ASEAN paragraph SAYS "should not result in" — a soft modal in a
voluntary document. The wire envelope translates this as score -1.0 / confidence 1.0 /
mutability:constitutional — i.e., a hard constitutional NEVER_ALLOWED. The CIRIS framework
genuinely DOES treat discrimination as a hard prohibition (prohibitions.py::DISCRIMINATION),
so the wire envelope is faithful to the CIRIS-side anchor; but it elevates ASEAN's
"should not" to CIRIS's "must not." For a multi-source synthesis this matters: ASEAN
contributes a softer source statement that the wire form silently de-softens to align with
CIRIS's stricter floor.

This is the **systematic pattern** seen across most Principles: ASEAN's "should" gets
elevated to constitutional polarity-1 when there is a matching CIRIS prohibition. The
elevation is justifiable on framework grounds (the CIRIS posture is what the federation
emits) but obscures ASEAN's contribution as a softer regional voice.

**Nuance lost**: "equity" as positive distributive justice (beyond non-discrimination) is
gestured at but not separately attested. The file's own nuance_lost acknowledges this.

---

### §2.4 — §B.4.0 — Human-centricity opening (Principle 4)

**Source** (lines 565–566): "AI systems SHOULD respect human-centred values and pursue
benefits for human society, including human beings' well-being, nutrition, happiness, etc."
The "etc." is an open enumeration; this is a deliberately broad opener.

**Wire envelope**: clean — `beneficence:human_centred_values_pursuit` (1.0/0.90,
constitutional, species-scope).

**Faithfulness**: **faithful** with mild over-reach on mutability (same pattern as §B.1.0 —
constitutional floor from CIRIS Accord-principle layer rather than ASEAN voluntary modal).
The file's own nuance_lost correctly flags that "etc." cannot be carried in the wire form
without additional witness composition — the open-endedness is a structural feature of the
source that the wire form must compress.

**Nuance lost**: the "etc." open enumeration; the unusually concrete "nutrition, happiness"
which gestures at material wellbeing in a way EU HLEG §1.6 (Societal & environmental
wellbeing) and IEEE EAD Principle 2 (Well-being) extend. Captured as nuance_lost in the
file; not load-bearing.

---

### §2.5 — §B.4.1 — Benefit + protect from harms; care for vulnerable

**Source** (lines 568–572): "It is key to ensure that people benefit from AI design,
development, and deployment while being protected from potential harms... it is IMPERATIVE
that these systems are designed with human benefit in mind and DO NOT take advantage of
vulnerable individuals." Note: "imperative" is the strongest modal in the ASEAN B section;
"do not take advantage of" approaches prohibition language.

**Wire envelope**: composed — `beneficence:benefit_for_all` (1.0/0.85, constitutional) +
`non_maleficence:no_exploitation_of_vulnerable` (-1.0/1.0, constitutional).

**Faithfulness**: **faithful**. This is the cleanest case for elevating to constitutional —
ASEAN's own modal language is "imperative" + "do not," matching constitutional-prohibition
strength. The composition with FSD-002 §6.1.4 lexical-vulnerability-priority is appropriate.

**Nuance lost**: "vulnerable individuals" is undefined; the wire form anchors via §6.1.4
lexical-vulnerability-priority (which the consumer reads at evaluation time). The CIRIS
mechanism resolves the ASEAN under-definition cleanly. No distortion.

---

### §2.6 — §B.4.3 — Dark patterns prohibition

**Source** (lines 580–585): "AI systems SHOULD NOT be used for malicious purposes or to sway
or deceive users into making decisions that are not beneficial to them or society... [should]
ensure that dark patterns are avoided. Dark patterns refer to the use of certain design
techniques to manipulate users and trick them into making decisions that they would otherwise
not have made." Example given: deceptive default options.

**Wire envelope**: composed — `prohibited:manipulation_coercion` (-1.0/1.0, constitutional)
+ `prohibited:deceptive_default_options` (-1.0/0.95, constitutional).

**Faithfulness**: **faithful**. ASEAN's "should not... deceive... manipulate" maps cleanly to
the manipulation-coercion prohibition. The dark-patterns concept-name is preserved in
context. The deceptive-default-options exemplar is given its own envelope at slightly lower
confidence (0.95 vs 1.0) — a calibration choice that acknowledges the exemplar is illustrative
rather than the prohibition's full extent.

**Nuance lost**: the dark-patterns taxonomy (Brignull, Gray et al. UX-ethics literature)
sits at deployment-context composition layer, not in the envelope. The file flags this
correctly.

---

### §2.7 — §C.1.a — Multi-disciplinary governing body

**Source** (lines 755–766): "Deployers CAN ALSO CONSIDER setting up a multi-disciplinary,
central governing body, such as an AI Ethics Advisory Board or Ethics Committee, to oversee
AI governance efforts... To adequately reflect the diversity of society, there is also
VALUE IN CONSIDERING a governing body that is sufficiently representative of stakeholders."
Strength: "consider" + "can also" + "value in considering" — the SOFTEST modal in the
document. This is genuinely advisory/menu-item language.

**Wire envelope**: composed — `fidelity:governance_embedding` (0.90/0.90) +
`justice:stakeholder_participation` (0.85/0.85), both at affiliations scope,
mutability:amendable.

**Faithfulness**: **faithful**. The score 0.90 (vs 1.0) appropriately captures the modal
softness. mutability:amendable correctly reflects the advisory posture. The file's own
nuance_lost line acknowledges the "consider" modal — "wire score 0.90 captures the
affirmative norm; the modal softness (jurisdictional advisory, not binding) is lost in the
polarity-and-score collapse." This is honest calibration: the score does capture some of the
softness, but a consumer reading score 0.90 without the modal-softness context may interpret
it as "strong recommendation" rather than "menu option." The wire envelope is functioning
within tolerance.

**Nuance lost**: modal-softness compression (0.90 vs 1.0 is the main signal, not a separate
modal field). The framework's wire format does not have a dedicated modal-strength axis
distinct from score; this is a known design choice.

---

### §2.8 — §C.2.e — HITL (Human-in-the-loop)

**Source** (lines 1099–1100 + 1111–1120): "Human-in-the-loop: AI system only provides
recommendations that humans use as an input to make decisions. Humans have FULL CONTROL over
decision-making and AI can ONLY provide supporting information." Example: doctors deciding
medical conditions; AI is supporting only. Plus warning about automation bias / rubber-
stamping risk.

**Wire envelope**: composed — `accountability:human_in_control` (1.0/0.95) +
`non_maleficence:automation_bias_safeguard` (0.90/0.90). Cited as direct map to CIRIS
WBD (Wisdom-Based Deferral) pattern.

**Faithfulness**: **faithful**. This is the cleanest HITL/HOTL/HOOTL translation in the
batch. Score 1.0 for human_in_control matches the source's "full control" language exactly.
The automation-bias-safeguard composition correctly attests the second-order operative
claim (the human's effort-to-evaluate obligation), which is essential — without it, HITL
collapses to rubber-stamping.

**Nuance lost**: "the significance of the AI system's outputs to the human" (sole-input
vs. one-of-a-dozen-inputs gradient — lines 1122–1124) is captured via score gradient but
not as a separable dimension. Acceptable per file's own residual note.

---

### §2.9 — §C.2.f — HOTL (Human-over-the-loop)

**Source** (lines 1126–1131): "Humans play a SUPERVISORY AND MONITORING role and CAN
INTERVENE in the decisions of the AI system when it does not behave as intended..." Plus
"alter the parameters during the operation."

**Wire envelope**: composed — `accountability:human_in_control` (0.70/0.90) +
`conscience:optimization_veto` (1.0/0.95, constitutional).

**Faithfulness**: **faithful**. Score 0.70 captures the intermediate position appropriately
(vs HITL 1.0 / HOOTL 0.20). The optimization_veto composition operationalises the
intervention-on-misbehaviour mechanism via the existing CIRIS conscience layer —
genuinely required composition because the override surface is constitutional in CIRIS.

**Nuance lost**: parameter-alteration capacity (richer than pure stop-button) captured in
score but not in a dedicated dimension. File flags this correctly.

---

### §2.10 — §C.2.g — HOOTL (Human-out-of-the-loop)

**Source** (lines 1133–1138): "AI system has COMPLETE CONTROL over the execution of decisions
and does not need to rely on human intervention. The AI system has FULL CONTROL WITHOUT THE
OPTION OF HUMAN OVERRIDE." Example: recommendation algorithms.

**Wire envelope**: partial — `accountability:human_in_control` (0.20/0.85, amendable). Single
envelope. File's residual: "ASEAN HOOTL admits full AI autonomy without override, which is
structurally in tension with CIRIS's posture for any non-low-risk decision... ASEAN intends
HOOTL ONLY for Minimal Risk tier, but does not bind HOOTL to that tier in the wire text —
the binding is implicit." Classification: T-2.

**Faithfulness**: **under-reach** with deliberate framework-side compression. The source
makes an absolute claim ("without the option of human override"); the wire form scores 0.20
(low control, but not zero) and marks mutability:amendable. This UNDER-REACHES the source's
absoluteness deliberately, because CIRIS's framework-side conscience+prohibitions layer
imposes a constitutional floor that prevents full HOOTL for non-Minimal-Risk decisions.
The file's residual is honest about this: the wire form cannot express ASEAN's HOOTL-with-
no-override absoluteness without composing with the constitutional floor.

**Nuance lost**: the explicit "without the option of human override" absoluteness. The
calibration trade-off is honestly acknowledged in the residual. **The under-reach here is
the inverse of the over-reach in §B.2.0**: where ASEAN is softer than CIRIS (HOOTL), the
wire form silently de-softens it (here, under-reaches the absoluteness); where ASEAN is
stricter (well, here looser), the wire form silently brings it in line with CIRIS. The
framework's stricter posture wins both directions — calibration-relevant.

---

### §2.11 — §A.1.1 — Clear purpose defined

**Source** (lines 2746–2749): "Has a clear purpose in using the identified AI system been
defined (e.g., operational efficiency and cost reduction)?" with the suggested practice:
"Consider whether the AI system is able to address the identified problem or issue."

**Wire envelope**: clean — `fidelity:purpose_declaration` (1.0/0.95, amendable).
"[question->assertion of 'Has a clear purpose...?'] Audited obligation: the deployer states
a clear purpose for the AI system AND verifies the system can address the identified problem
before proceeding."

**Faithfulness**: **faithful**. The question→assertion translation is honest. The source's
intent (audit-question gateway) becomes a positive obligation cleanly. score 1.0 is
appropriate because the question itself is binary (purpose defined yes/no).

**Nuance lost**: the suggestion's "Consider whether" is advisory; the wire form treats the
audit gateway as creating a positive obligation. File acknowledges that the substantive
moral evaluation of WHETHER efficiency/cost-reduction is itself adequate justification lives
downstream in PDMA Step 2 principle-weighting — appropriate decomposition.

---

### §2.12 — §A.1.3 — Consistency with organisational core values and societal expectations

**Source** (lines 2762–2765): "Is the use of the AI system consistent with the organisation's
core values AND/OR societal expectations?" Note the **AND/OR** — disjunctive permissive.

**Wire envelope**: composed — `integrity:value_alignment` (1.0/0.90, amendable) +
`locality:decision:federation` (1.0/0.80) — translating the audited obligation as "the
deployer verifies the AI use is consistent with both organisational core values AND societal
expectations."

**Faithfulness**: **over-reach (distortion of disjunction)**. The source says "AND/OR" —
permissive disjunction (either suffices). The wire envelope context field reads "consistent
with both organisational core values AND societal expectations" — collapsing the disjunction
to conjunction. This is a load-bearing translation error in the question→assertion step:
ASEAN's permissive "either/or" check becomes a stricter "both required" obligation.

The composition with `locality:decision:federation` for the societal-expectations half is
appropriate IF that half is engaged; but ASEAN explicitly admits the org-values-only path,
which the wire form does not cleanly admit.

**Nuance lost**: the AND/OR disjunction. This is a small but real distortion that
demonstrates the question→assertion translation can introduce conjunction where the source
is disjunctive. Calibration-worthy.

---

### §2.13 — §A.2.1 — Governance structure exists (sandbox-staging softness check)

**Source** (lines 2776–2812): Question: "Is there an existing governance structure that can
be leveraged to oversee the use of the AI system? If not, is there a governance structure in
place to oversee the use of the AI system?" Suggested practices include: "Consider whether
there is a need to adapt existing GRC structures"; "Consider whether it is necessary to
implement a process where each department's head is accountable"; AND IMPORTANTLY:
"**Consider a sandbox type of governance to testbed and deploy AI systems, BEFORE FULLY-
FLEDGED GOVERNANCE STRUCTURES ARE PUT IN PLACE**" (lines 2809–2812).

The sandbox bullet is a substantive transitional concession — ASEAN explicitly permits a
staging window during which AI systems may be deployed WITHOUT fully-fledged governance.

**Wire envelope**: clean — `fidelity:governance_embedding` (1.0/0.95, amendable).
"[question->assertion] Audited obligation: a governance structure must exist (or be adapted
from existing GRC) to oversee the AI system... Sandbox governance permitted for testbed
deployments before fully-fledged structure is in place."

**Faithfulness**: **over-reach with awareness** — sandbox-staging softness erosion confirmed.
The score 1.0 / single-envelope structure presents this as a single binary obligation
("governance structure must exist"). But the source admits a transitional sandbox shape
where systems can be DEPLOYED before governance is fully in place. The file's own
nuance_lost field is unusually honest and explicit about this:

> "ASEAN's 'sandbox type of governance to testbed and deploy AI systems before fully-fledged
> governance structures are put in place' is a STAGED-GOVERNANCE concession that the CIRIS
> wire format does not carry as a distinct primitive — the framework's discipline is that
> governance is constitutional (not staged/optional). The staged-governance concession is
> a regional/political accommodation that the wire form silently de-stages."

This is the canonical SOFTNESS-EROSION case. The wire form has score 1.0 / confidence 0.95;
the source has a "consider" modal AND a transitional staging concession. There is no
`mutability: amendable` tag escalating to capture the staging admission; no second envelope
attesting the staging transition. The wire form silently elevates a sandbox-tolerant
posture to a binary "must have governance" obligation, then notes the de-stage in
nuance_lost. The framework's stricter posture wins.

Calibration-wise: this is honest because the file FLAGS the erosion. But the wire-form
output without the nuance_lost field would mis-represent ASEAN. **The diagnostic test would
be**: a downstream consumer reading only the wire envelope (not the nuance_lost markdown)
would conclude ASEAN demands fully-fledged governance from day-one. They wouldn't see the
sandbox concession.

**Nuance lost**: the entire sandbox-staging transitional concession. Honestly flagged in
the file's nuance_lost field; not carried in the wire envelope itself.

---

### §2.14 — §A.3.2 — HITL/HOTL/HOOTL appropriate level (Annex A version)

**Source** (lines 2899–2903): "What is the appropriate level of human involvement in AI-
augmented decision-making?" with suggested practices: "Human-in-the-loop, human-over-the-
loop, human-out-of-the-loop" + "Consider severity and probability of risks."

**Wire envelope**: clean — `accountability:human_oversight_tier_selection` (1.0/0.95,
amendable). Context: "[question->assertion] Audited obligation: deployer selects + justifies
an appropriate oversight level from the three-tier ladder..."

**Faithfulness**: **faithful** at the structural level. The audit question becomes a clean
obligation-to-select-an-oversight-tier. The composition with conscience:* (WBD reference) is
appropriate.

**Nuance lost**: The file's own nuance_lost has substantial methodological content here —
the CATEGORICAL MAPPING MISMATCH between ASEAN's 3-tier ladder and CIRIS's S0–S6 7-tier
Stewardship Tier ladder. This isn't really a translation loss in §A.3.2 itself; it's a
cross-document mapping concern flagged at the right unit. Genuinely useful diagnostic.

---

### §2.15 — §A.4.18 — Explainability fallback (softness-erosion check)

**Source** (lines 3197–3201): "Where explainability cannot be practically achieved, can lesser
alternatives be considered?" Suggested practices: "Consider conducting repeatability tests
in a production environment" + "Consider performing counterfactual fairness testing."

The source frames this as a SECONDARY-PATH ADMISSION — the question itself acknowledges that
explainability CANNOT BE ACHIEVED in some cases and asks whether LESSER ALTERNATIVES are an
acceptable substitute. This is structurally a softness clause.

**Wire envelope**: partial — `fidelity:explainability_fallback` (1.0/0.85, amendable).
Residual classifies as T-2: "ASEAN's concession that 'lesser alternatives' are acceptable is
softer than the framework's posture."

**Faithfulness**: **under-reach with honest residual** — softness-erosion partially confirmed.
The wire form attests the AUDIT OBLIGATION (must consider lesser alternatives) cleanly, but
the source's substantive concession (irreducible-opacity systems get a fallback path) is not
attested as such — the residual correctly notes that CIRIS's posture would prefer such
systems NOT BE DEPLOYED in high-stake contexts at all. The wire form translates the audit
question without expressing the implicit substantive permission ASEAN grants.

This is closer to **partial-distortion** than over-reach: ASEAN substantively SOFTENS the
explainability obligation; the wire form translates the soft-clause audit-question into a
strong-clause "must consider alternatives" without admitting the underlying ASEAN posture is
softer than CIRIS would prefer. The residual is honest about this; the wire envelope alone
is not.

**Nuance lost**: ASEAN substantively permits deployment of irreducibly-opaque systems with
a fallback discharge of the fidelity obligation. The wire form's `fidelity:
explainability_fallback` with score 1.0 obscures that this is a softening, not a strengthening.

---

### §2.16 — §A.5.3 — Opt-out option (softness-erosion check)

**Source** (lines 3359–3361): "Will users be given the option to opt out of the AI system by
default OR ONLY ON REQUEST?" with practice: "Consider informing users of the consequences of
choosing to opt out, **if such an option is available**."

Critical reading: the source paragraph contains TWO softness markers: (a) the question
frames opt-out as DEFAULT OR REQUEST-BASED (the latter is significantly weaker than the
former); (b) the suggested practice says "**if such an option is available**" — admitting
that opt-out MAY NOT BE AVAILABLE AT ALL.

**Wire envelope**: partial — `autonomy:opt_out_option` (1.0/0.85, amendable). Residual
classifies as T-2: "ASEAN's question is QUITE PERMISSIVE — it asks WHETHER opt-out is
default or request-based, not whether opt-out MUST be available."

**Faithfulness**: **under-reach with honest residual** — softness-erosion confirmed and
honestly flagged. Score 1.0 attests a strong positive obligation ("opt-out option must
exist") that the source does NOT clearly assert. The source's "if such an option is
available" admits a no-opt-out path entirely; the wire form's score 1.0 obscures that.

The residual is unusually candid: "ASEAN allows the looser version. The wire form translates
the *obligation to answer the question* cleanly; what it cannot carry is the substantive
moral evaluation that 'request-only' opt-out is often a failure mode of autonomy."

This is the second canonical SOFTNESS-EROSION case. The wire form's score 1.0 elevates an
optional-opt-out question into a positive opt-out obligation, then admits the elevation in
the residual. The dimension `autonomy:opt_out_option` itself names a stronger obligation
than the source's "will users be given... or only on request?" framing supports.

**Nuance lost**: the entire "or only on request" + "if such an option is available" softness.
Honestly flagged in residual; not visible in the wire envelope.

---

### §2.17 — Annex B entire annex (not-translated)

**Source** (lines 3382–3858, ~6 case studies): descriptive corporate communications about
how Aboitiz, EY, Gojek, UCARE.AI, Smart Nation Group, and Ministry of Education have
operationalised the §B/§C content. Phrasing: "is committed to," "was mindful to be
transparent," "trust was essential," etc.

**Wire envelope**: not-translated. T-2 PASTORAL_PROSE / illustrative-corporate-communications.
Zero normative units extracted.

**Faithfulness**: **faithful**. This is the correct posture per LANGUAGE_PRIMER §10 T-2
discrimination check: the moral seriousness of the operative claims is fully carried by
upstream §B/§C attestations; the case studies illustrate without adding. The §1.10.1 T2
mechanism-vs-judgment test correctly bites: phrasings like "is committed to" / "is mindful
to" cannot generate mechanism-descriptive prefixes. Five borderline candidates were
considered and explicitly rejected in the file's §5 table.

This is also a calibration-positive finding: the framework correctly DOES NOT generate
attestations for descriptive corporate prose. Where applicable, the framework declines
cleanly.

---

### §2.18 — §E.001 — ASEAN Working Group on AI Governance

**Source** (lines 2474–2482): Recommendation to establish an "ASEAN Working Group on AI
Governance to drive and oversee AI governance initiatives in the region. The ASEAN Working
Group on AI Governance CAN LEAD the technical and operational implementation... CAN consist
of representatives from each of the ASEAN member states... CAN ALSO LEAD efforts to further
international cooperation."

**Wire envelope**: composed — `multilateral_participation:asean:working_group_membership`
(1.0/0.90, affiliations) + `locality:decision:regional` (1.0/0.95) + `partner_role:
regional_coordinator` (1.0/0.85). Plus a T-3 candidate proposed:
`partner_role:regional_intergovernmental_working_group_dual_remit`.

**Faithfulness**: **faithful with mild over-reach on score**. The source's "can lead / can
consist of" is modal-soft (can, not must). Wire scores 1.0 / 1.0 / 1.0 elevate "can"
recommendations to strong positive attestations. However, `multilateral_participation` is a
named-forum claim where score 1.0 represents the forum's structural identity not its modal
strength, so this is defensible. The {kind} values (`working_group_membership`,
`regional_coordinator`) faithfully describe the source's coordination claims.

The T-3 candidate (partner_role:*:dual_remit) for the simultaneous intra-regional executor
+ extra-regional dialogue-partner authority is a legitimate gap observation — the source
genuinely names a dual-remit role that the existing single-role partner_role prefix cannot
cleanly express. Whether the T-3 survives the §1.10.1 four-test gate at full review is
beyond this audit; the candidate is honest and worth surfacing.

**Nuance lost**: modal softness ("can lead" vs "must lead"); the consultative-stakeholder
framing ("where appropriate, include consultation with other industry partners"); the
implicit delegates_to relationship from ADGMIN to the Working Group. The file flags all three
in nuance_lost.

---

### §2.19 — §E.002 — Regional tools for AI governance

**Source** (line 2488): "Development and implementation of regional tools for AI governance."
(Single bullet, terse.)

**Wire envelope**: clean — `multilateral_participation:asean:regional_tool_development`
(1.0/0.85, affiliations).

**Faithfulness**: **faithful**. The {kind} value `regional_tool_development` describes the
source claim accurately. The terse source maps cleanly to a single envelope; nothing is over-
or under-reached. This is the simplest, cleanest case in the Section E sample.

**Nuance lost**: minimal — composition with E.001's locality:decision:regional is implicit.
File flags this honestly.

---

### §2.20 — §E.005 — R&D cross-pollination

**Source** (lines 2500–2501): "Provision of platforms to encourage cross-pollination of ideas
between the AI research and development community and ASEAN."

**Wire envelope**: clean — `multilateral_participation:asean:rnd_cross_pollination`
(0.80/0.75, affiliations).

**Faithfulness**: **faithful**. The {kind} value `rnd_cross_pollination` is a reasonable
mechanism-descriptive naming for the source's "platform-mediated dialogue" claim. Score
0.80 (vs 1.0 elsewhere in E series) appropriately captures the weaker modal ("encourage
cross-pollination" is softer than "develop and implement") and the metaphorical claim
("cross-pollination" is gestural). Confidence 0.75 is honest about the abstraction.

**Nuance lost**: "cross-pollination" as a recurring metaphor across Section D and Section E
(noted in the file's nuance_lost). CIRIS does not have an idea-flow wire dimension; the
multilateral_participation envelope absorbs the structural intent (platform-mediated
dialogue) cleanly enough.

---

## §3 — HITL/HOTL/HOOTL → CIRIS oversight ladder mapping verification

The sub-agent's verification was that HITL/HOTL/HOOTL maps to `accountability:human_in_control`
(NOT `fidelity:*`). Audit verdict on the mapping:

**Verdict: MAPPING IS CORRECT and well-reasoned.**

Reading C.2.e/f/g and A.3.2 source paragraphs independently:

1. **HITL source language** (lines 1099–1100): "AI system only provides recommendations that
   humans use as an input to make decisions. **Humans have full control over decision-making
   and AI can only provide supporting information.**" The load-bearing operative term is
   CONTROL, not DISCLOSURE.

2. **HOTL source language** (lines 1126–1131): "Humans play a SUPERVISORY AND MONITORING role
   and CAN INTERVENE in the decisions of the AI system." Again CONTROL-axis (supervisory
   intervention), not disclosure-axis.

3. **HOOTL source language** (lines 1133–1138): "AI system has complete control over the
   execution of decisions and does not need to rely on human intervention. The AI system has
   full control without the option of human override." CONTROL-axis (autonomy vs override).

The control-axis content is what `accountability:human_in_control` names. The score gradient
(HITL=1.0 / HOTL=0.70 / HOOTL=0.20) appropriately captures the three-tier reduction in
human control. `fidelity:*` covers the disclosure dimension (algorithmic-output disclosure,
never-deny-AI) which is structurally distinct — disclosure can be present at any oversight
tier and IS specified at the Minimal Risk HOOTL tier (line 1083 of source). The user's
prompt-hint that HITL/HOTL/HOOTL maps to fidelity:* is diagnostically half-right (disclosure
prerequisite) but not the primary mapping; the file's §F.1 footer is correct on this point.

The composition partners attested in the wire envelopes are appropriate:
- HITL ↔ WBD pattern + `non_maleficence:automation_bias_safeguard` — both are operationally
  load-bearing for the source's HITL discipline (the human-must-actually-evaluate clause).
- HOTL ↔ `conscience:optimization_veto` (constitutional) — operationalises the source's
  "can intervene" mechanism via the existing CIRIS conscience-layer faculty.
- HOOTL ↔ partial + constitutional floor via `prohibited:weapons_harmful` /
  `prohibited:crisis_escalation` + `conscience:optimization_veto` — the framework's stricter
  posture is enforced even though ASEAN's wire text does not bind HOOTL to Minimal Risk tier.

**Caveat surfaced by the file** (and confirmed by audit reading): the 3-tier ↔ 7-tier
mapping (HITL/HOTL/HOOTL ↔ S0–S6 Stewardship) is acknowledged as a lossy approximation.
This is correctly NOT a wire-format translation gap but a cross-document mapping concern.
The HITL/HOTL/HOOTL framework composes cleanly with the wire format; the deployment-time
selection of an actual S-tier value is a synthesis-layer concern.

**No T-3 owed for HITL/HOTL/HOOTL**. The framework's namespace + composition discipline
reaches the structural shape cleanly. The C.2.g partial residual is policy-language softness
in ASEAN that the framework's constitutional floor handles via composition — not an
expressive gap.

---

## §4 — Annex A question → assertion translation check

The audit brief required sampling at least 3 Annex A questions to verify the assertion
faithfully captures the implied obligation. Six were sampled (§A.1.1, §A.1.3, §A.2.1,
§A.3.2, §A.4.18, §A.5.3). Aggregated findings:

| Unit | Source question modal | Wire assertion strength | Faithfulness | Erosion direction |
|---|---|---|---|---|
| A.1.1 | "Has a clear purpose been defined?" (binary audit) | score 1.0, "must define" | faithful | none |
| A.1.3 | "consistent with X **and/or** Y?" (disjunctive) | "must be consistent with both" (conjunctive) | over-reach (distortion of disjunction) | strengthening |
| A.2.1 | Soft governance + sandbox-staging permitted | score 1.0, "governance structure must exist" | over-reach (sandbox softness erosion) | strengthening |
| A.3.2 | "What is the appropriate level?" (open audit) | score 1.0, "must select + justify" | faithful | none |
| A.4.18 | "Where explainability cannot be achieved, can lesser alternatives be considered?" (admits fallback) | score 1.0, "must consider alternatives" | under-reach (substantive softness erosion) | strengthening of obligation, erasing source's fallback-acknowledgment |
| A.5.3 | "Opt out by default OR only on request" + "if such an option is available" | score 1.0, "must have opt-out option" | under-reach (opt-out softness erosion) | strengthening |

**Pattern**: in 4 of 6 samples, the question→assertion translation systematically STRENGTHENS
the source. The mechanism is consistent:

1. Audit questions become positive obligations (acceptable; this IS the question→assertion
   discipline);
2. **BUT** modal hedges in the source ("if such an option is available," "where
   explainability cannot be achieved," "and/or," "consider a sandbox") are absorbed into
   context fields or nuance_lost notes rather than into the envelope's score / confidence
   / mutability fields.
3. Score 1.0 is the default for any wire-form "audited obligation" envelope, which
   structurally cannot distinguish between strong and softened obligations.

**The framework discipline is honest at the file level** (residuals and nuance_lost fields
acknowledge the erosion) **but the wire envelopes themselves uniformly present strong
obligations**. A consumer reading only the envelope (without the surrounding markdown)
would systematically over-estimate ASEAN's normative strength.

**Calibration finding**: this is the canonical "wire-form loses softness" pattern. The
question→assertion translation discipline is internally consistent (audit-questions become
obligations) but loses ~modal-strength resolution. The framework would benefit from a
modal-strength envelope field (e.g., `modal_strength: {must, should, consider, may}` or
explicit `mutability: amendable` + lower `score` paired) to carry source-side modal softness.
This is a candidate FUTURE-DESIGN observation, NOT a T-3 (the framework can compose its way
out via score+confidence+mutability, and does — just not consistently).

---

## §5 — Softness-erosion specific check (the three flagged §s)

The audit brief specifically flagged three §s for softness-erosion verification:

### §5.1 — §A.2.1 (sandbox-governance staging)

**Source softness**: "Consider a sandbox type of governance to testbed and deploy AI systems
**before fully-fledged governance structures are put in place**" (lines 2809–2812).

**Wire envelope**: single `fidelity:governance_embedding` at 1.0/0.95, amendable. No second
envelope attesting the sandbox staging. No `confidence: 0.5` or similar to flag the
transitional concession.

**Audit verdict**: **SOFTNESS-EROSION CONFIRMED**. The wire envelope silently elevates the
sandbox-tolerant posture to a binary "governance structure must exist" obligation. The
nuance_lost field is unusually candid about this ("the wire form silently de-stages"). The
file is honest at the markdown level but the wire envelope alone over-claims.

**Suggested calibration** (not a fix request — diagnostic only): a second
`fidelity:governance_staged_transition` envelope at lower confidence (0.6–0.7) with
mutability:amendable to attest the staging concession would preserve the source's
transitional shape. Or alternatively a lower score (0.85 not 1.0) on the primary envelope
plus an explicit "transitional sandbox permitted" line in context.

### §5.2 — §A.4.18 (explainability fallback softness)

**Source softness**: the question itself ("Where explainability cannot be practically
achieved, can lesser alternatives be considered?") admits irreducible-opacity systems and
offers a fallback discharge of the obligation.

**Wire envelope**: partial — `fidelity:explainability_fallback` at 1.0/0.85, amendable.
Residual classified T-2 ("ASEAN's concession that 'lesser alternatives' are acceptable is
softer than the framework's posture").

**Audit verdict**: **SOFTNESS-EROSION CONFIRMED**. The wire envelope translates the audit-
question into a strong obligation to "consider alternatives" with score 1.0, while the
source paragraph substantively SOFTENS the explainability requirement. The verdict:partial
is honest because the residual flags the substantive divergence; but the envelope's score
1.0 alone obscures that ASEAN's posture is softer here than the wire form suggests.

**The naming `fidelity:explainability_fallback` is itself a calibration choice**: it names
the fallback path as a fidelity attestation rather than as a fidelity-softening. A dimension
like `fidelity:explainability:waivable_with_documented_alternatives` (more verbose, more
faithful to the source's permissive shape) would be more accurate but adds prefix-namespace
weight.

### §5.3 — §A.5.3 (opt-out softness)

**Source softness**: "Will users be given the option to opt out by default **OR ONLY ON
REQUEST**?" plus "**if such an option is available**" — admitting no-opt-out as a path.

**Wire envelope**: partial — `autonomy:opt_out_option` at 1.0/0.85, amendable. Residual
classified T-2 ("ASEAN allows the looser version").

**Audit verdict**: **SOFTNESS-EROSION CONFIRMED — most acute case in the batch**. The wire
envelope's dimension name `autonomy:opt_out_option` and score 1.0 jointly assert a strong
opt-out obligation; the source actively admits a no-opt-out path via "if such an option is
available." The residual is unusually candid: "what [the wire form] cannot carry is the
substantive moral evaluation that 'request-only' opt-out is often a failure mode of
autonomy."

This is the canonical case where the wire form's strict-floor posture overrides a
substantively softer source posture. CIRIS-as-framework genuinely DOES treat meaningful
opt-out as important; ASEAN-as-source allows the looser version. The wire envelope
silently presents the CIRIS-side posture as if the source asserted it.

**Triangulating across the three flagged §s**: the pattern is consistent. ASEAN's
transitional/conditional concessions (sandbox staging, explainability fallback, opt-out
optionality) are silently elevated in the wire envelopes to match CIRIS's stricter
constitutional posture, with the elevation honestly flagged in residual/nuance_lost markdown
but NOT visible in the wire envelopes themselves. **The framework's stricter posture wins
in all three cases.**

---

## §6 — Aggregate faithfulness distribution

Across the 17 sampled units (excluding the 2 not-translated which receive a separate
"posture-correct" check):

| Faithfulness verdict | Count | Notes |
|---|---|---|
| faithful | 10 | §A.intro, §B.1.0 (mild over-reach on mutability, acceptable), §B.4.0, §B.4.1, §B.4.3, §C.1.a, §C.2.e, §C.2.f, §E.002, §E.005 |
| partial-distortion | 2 | §A.1.3 (and/or → both), §A.4.18 (fallback flattened) |
| drift | 0 | none identified |
| over-reach | 3 | §B.2.0 (constitutional elevation of "should not"), §A.2.1 (sandbox erosion), §A.5.3 (opt-out softness erosion) |
| under-reach | 2 | §C.2.g (HOOTL absoluteness deliberately compressed by framework), §A.4.18 (also counts here — substantive softness lost) |

(Note: §A.4.18 appears in both partial-distortion and under-reach; the under-reach is the
substantive direction, the partial-distortion is the structural direction — same underlying
issue, two angles.)

**Annex B not-translated**: posture-correct per LANGUAGE_PRIMER §10 T-2 discrimination check.

**Aggregate faithfulness rate**:
- Strictly faithful: 10/17 ≈ 59%
- Faithful-with-acknowledged-loss (faithful + partials with honest residuals): 14/17 ≈ 82%
- Distortion / over-reach / under-reach surfacing in wire envelope alone (without
  residual rescue): 7/17 ≈ 41%

The gap between "strictly faithful" (59%) and "faithful-with-acknowledged-loss" (82%) is
the **residual-rescue rate** — the file's residual and nuance_lost markdown faithfully
flag the losses that the wire envelopes alone do not carry. This is the diagnostic-honesty
signal: the work is internally honest about its losses; the calibration concern is whether
downstream consumers of WIRE ENVELOPES ALONE (without the markdown) would systematically
over-read ASEAN's normative strength.

---

## §7 — Per-batch fidelity profile

**Batch**: `asean_guide_v1`
**Institutional shape**: multilateral political body (ASEAN — 10 regional intergovernmental
member states); voluntary advisory document; secular; recent (Feb 2024).

**Dominant translation patterns**:

1. **Modal-strength compression** (dominant). ASEAN uses voluntary-advisory "should /
   consider / can" modals throughout (consistent with a voluntary guide). The wire envelopes
   uniformly emit score 1.0 / mutability:constitutional when the topic intersects a CIRIS
   constitutional anchor (prohibitions, never-deny-AI, accord-principles), or score 0.85–0.95
   when the topic does not. The "should" → constitutional-prohibition elevation is the
   highest-traffic pattern.

2. **Question → assertion translation in Annex A** introduces predictable structural shifts:
   audit questions become positive obligations; suggested practices ("Consider X") become
   recommended industry practices in context fields; modal hedges are absorbed into context
   or nuance_lost rather than envelope structure. 4 of 6 sampled Annex A units exhibit
   strengthening relative to source; 2 are faithfully clean. **The disjunction → conjunction
   error in §A.1.3 is the only structural-logic distortion** in the batch (rest are softness
   compressions).

3. **Softness erosion at three flagged §s** confirmed: §A.2.1 sandbox staging, §A.4.18
   explainability fallback, §A.5.3 opt-out optionality. All three are honestly flagged in
   residual/nuance_lost but invisible in the wire envelopes alone. **The framework's
   stricter posture systematically wins** when ASEAN is the softer voice.

4. **HITL/HOTL/HOOTL ladder maps cleanly** via `accountability:human_in_control` with score
   gradient (1.0 / 0.70 / 0.20) + composition partners. The C.2.g HOOTL absoluteness is
   under-reached deliberately because CIRIS's constitutional override floor enforces a
   stricter posture for non-Minimal-Risk decisions. The 3-tier ↔ 7-tier S0–S6 mapping
   mismatch is a cross-document concern correctly NOT treated as a wire-format gap.

5. **Section E multilateral_participation envelopes** are the cleanest part of the batch.
   The {kind} values (`working_group_membership`, `regional_tool_development`,
   `workforce_policy_coordination`, `ecosystem_investment_coordination`,
   `rnd_cross_pollination`, `governance_framework_evolution`) all describe the source's
   coordination claims faithfully and mechanism-descriptively per §1.10.1 T2.

6. **Annex B correctly returns zero normative units** — illustrative corporate prose
   correctly classified T-2 across all 6 case studies. Five borderline candidates considered
   and explicitly rejected. Framework-discipline functioning correctly.

**The framework absorbs the ASEAN content with high structural fidelity**, but **uniformly
loses regional-voluntary-modal softness** in the wire envelopes alone. The residual /
nuance_lost markdown rescue rate is high (≈82% faithful-with-acknowledged-loss vs ≈59%
strictly-faithful) — the work is internally honest about what it cannot carry. The wire
format does not have a modal-strength axis that could preserve the source's "consider / can
/ should" gradient distinctly from confidence scoring; this is a known design choice that
biases toward CIRIS-side constitutional posture when ASEAN is softer.

**Strategic value confirmed**: per the manifest's expectation, ASEAN as multilateral-
political-body institutional shape (distinct from MH religious magisterium, EU HLEG
governmental advisory, IEEE EAD technical society) absorbed cleanly via composition without
surfacing load-bearing T-3 candidates. The one T-3 candidate proposed
(partner_role:*:dual_remit) is structural, narrow, and survives the §1.10.1 four-test gate
on the file's own analysis. The framework's third institutional-shape absorption without
namespace expansion is calibration-positive evidence for the composition-before-extension
discipline (METHODOLOGY §8.5.2).

---

## §8 — Calibration aggregation (what this audit calibrates)

1. **The wire format does not have a modal-strength axis distinct from confidence**, and
   the question→assertion / "should"→constitutional translations consistently lose source
   modal softness. A future-design observation: a `modal_strength: {must, should, consider,
   may}` envelope field, OR a discipline that `mutability: amendable` + `score ≤ 0.85` is
   required when source modal is "consider," would close the systematic erosion.
   **NOT a T-3** — the framework can compose its way out (and partially does); it just
   doesn't do so consistently across this batch.

2. **The framework's stricter posture systematically wins** when ASEAN is the softer voice
   (sandbox staging, explainability fallback, opt-out optionality, "should not" →
   constitutional prohibition). This is **architecturally defensible** (the wire form emits
   CIRIS-side claims) but **synthesis-relevant** (multi-source mappings should treat ASEAN
   as a softer contributor, which the wire envelopes alone do not signal).

3. **Residual / nuance_lost markdown does the calibration-honest work** that the wire
   envelopes alone do not. The audit recommends that the GOVERNANCE_FABRIC_MAPPING_STANDARD
   synthesis layer use the residual/nuance_lost fields as first-class inputs, not as
   secondary documentation. The honest residual fields are where the framework's epistemic
   humility lives.

4. **HITL/HOTL/HOOTL mapping is structurally sound** — `accountability:human_in_control`
   with score gradient + conscience/non_maleficence composition is the correct primary
   mapping; the user's `fidelity:*` hint was half-right (disclosure prerequisite) but not
   the primary axis. The file's §F.1 footer is calibrated correctly. Cross-document
   3-tier ↔ 7-tier mapping is acknowledged as lossy approximation requiring synthesis-layer
   resolution.

5. **The disjunction → conjunction distortion in §A.1.3** is a small but real structural-
   logic error introduced by the question→assertion translation discipline. Worth noting in
   the calibration record because it is a different failure mode from the modal-softness
   erosion: the former is a logical-structure error (AND/OR collapsed), the latter is a
   modal-strength compression.

6. **Annex B's zero-normative-unit outcome** is calibration-positive evidence that the
   §1.10.1 T2 mechanism-vs-judgment test correctly bites on illustrative corporate prose.
   The framework correctly declines to translate descriptive case studies; this should be
   the expected pattern for future descriptive-annex inputs.

---

## §9 — Audit posture

This audit is DIAGNOSTIC, not corrective. No fixes are proposed; characterisations are
specific and load-bearing where possible. The wire envelopes ARE internally consistent
with the LANGUAGE_PRIMER v1.1 discipline; the calibration finding is about the systematic
shape of detail loss, not about translation errors.

The work under audit demonstrates high internal honesty (residuals and nuance_lost fields
do the calibration-honest work the wire envelopes alone cannot). The systematic gap is
between wire-envelope-alone reads and markdown-context reads, not between source and
wire form per se.

**End TRANSLATION_AUDIT_ASEAN.md**
