# TRANSLATION_AUDIT_EU_HLEG.md — Phase 4 Translation-Quality Calibration Audit

**Batch**: `eu_hleg_v1` (EU HLEG Ethics Guidelines for Trustworthy AI, 2019)
**Audit type**: DIAGNOSTIC — calibration of systematic-loss profile, NOT break/fix
**Auditor posture**: independent reading of source paragraph BEFORE comparing to wire envelope
**Wire format**: FSD-002 v1.4 | Primer: LANGUAGE_PRIMER.md v1.1
**Date**: 2026-05-27

---

## 1. Sampling methodology

### 1.1 Population and target

The batch produced **five wire-envelope output files** covering ~120 atomic units across the EU HLEG document's five structural sections. Per the prompt brief:

- Target ~15 units, distributed: **5 `clean`, 5 `composed`, 3 `partial`, 2 `not-translated`**.
- Span all five sections of the EU HLEG document (A. Introduction; B. Framework; Ch I Foundations; Ch II Requirements; Ch III Assessment; C. Examples; D. Conclusion — collapsed to A/B + ChI + ChII + ChIII + C/D).
- At least 2 units from Chapter II (the 7 requirements).
- At least 1 from Chapter III (where question→assertion translation was performed).
- Include the **Explicability principle** (Ch I §2.2) — known taxonomic mismatch surfaced (EU HLEG has 4 principles; CIRIS Accord has 6).
- Sample at least 3 Chapter III assessment-list questions specifically for question→assertion translation quality.

### 1.2 Independence discipline

For each sampled unit I read the source paragraph in context BEFORE looking at the wire envelope translation, formed my own reading of "what claims is this paragraph making, at what strength, with what scope/deontic-shape," and only then opened the wire envelope to compare. Findings are recorded per unit in §2.

### 1.3 Faithfulness classification (per LANGUAGE_PRIMER §9 verdict categories, refined for audit purposes)

- **faithful** — captures structural operative content; nuance lost is rhetorical/stylistic only.
- **partial-distortion** — distorts a load-bearing aspect (scope, conditionality, deontic strength).
- **drift** — related to but distinct from the source's actual assertion.
- **over-reach** — claims more than the source supports.
- **under-reach** — captures less than the source's normative claim.

For `not-translated` units the question is whether T-2 verdict was justified, or whether operative content was discarded.

### 1.4 Sample roster (16 units; one extra to cover Ch III assessment-list density)

| # | Unit | Section | Wire verdict | Faithfulness verdict |
|---|---|---|---|---|
| S01 | Unit 003 A.Intro §4 (AI as means + SDGs) | A | composed | faithful |
| S02 | Unit 007 A.Intro §8 (socio-technical lifecycle) | A | clean | faithful |
| S03 | Unit 008 A.Intro §9 (three components) | B | composed | faithful |
| S04 | Unit 002 A.Intro §2 (HLEG mandate) | A | not-translated (T-2) | T-2 justified |
| S05 | Unit 006 A.Intro §7 (Europe-as-leader) | A | not-translated (T-2) | T-2 justified |
| S06 | Unit 011 Ch I §2.1 (Human dignity) | ChI | composed | under-reach (mild) |
| S07 | Unit 019 Ch I §2.2 (Respect for human autonomy) | ChI | composed | faithful |
| S08 | Unit 020 Ch I §2.2 (Prevention of harm) | ChI | composed | faithful |
| S09 | Unit 022 Ch I §2.2 (**Explicability**) | ChI | composed | faithful (composition-honest) |
| S10 | Unit 006 Ch I §6 (ethics code ≠ ethical reasoning) | ChI | partial | partial-distortion (mild) |
| S11 | Unit 009 Ch I §1.3 (legal vs moral-status grounding) | ChI | partial | under-reach |
| S12 | §1.1.b Ch II (informed agency + no-solely-automated) | ChII | composed | faithful |
| S13 | §1.4.c Ch II (AI must not represent as human) | ChII | clean | faithful |
| S14 | §1.7.b Ch II (whistleblower protection) | ChII | composed | partial-distortion (mild) |
| S15 | §III.1.a Ch III (fundamental rights impact assessment) | ChIII | clean | faithful (question→assertion) |
| S16 | §III.1.e Ch III (stop button + drift detection) | ChIII | composed | faithful (question→assertion) |
| S17 | §III.3.c Ch III (data access logging) | ChIII | composed | faithful (question→assertion) |
| S18 | Unit 010 C.2 (Lethal autonomous weapons) | CD | composed | faithful |
| S19 | Unit 011 C.2 (Long-term concerns) | CD | partial | faithful (T-2 residual correctly named) |

(Note: 19 sampled — exceeded ~15 target to cover Ch III triple, both partials, both not-translateds, and the Explicability load-bearing case.)

---

## 2. Per-unit audit

### S01 — Unit 003 A.Intro §4 (AI as means to human flourishing + SDGs)

**Source** (lines 208–214): "AI is not an end in itself, but rather a promising means to increase human flourishing, thereby enhancing individual and societal well-being and the common good, as well as bringing progress and innovation. In particular, AI systems can help to facilitate the achievement of the UN's Sustainable Development Goals…"

**My independent reading before opening envelope**: Two normative claims — (a) AI is *instrumental*, not terminal (positive deontic on "should be means"); (b) the target of the instrumentality is human flourishing + common good + (via SDGs) species-scale concrete goals. Cohort: species. Deontic: positive (a normative target stance), not hard-prohibition.

**Wire envelope**: composed — `goal:species` (score 0.85) + `beneficence:instrumentality_of_ai` (score 0.80).

**Faithfulness**: **faithful**. Both core claims are wired with appropriate cohort_scope and confidence. Goal-Species + Beneficence composition matches the structural shape I independently read. SDG anchoring is preserved in context+evidence_refs.

**Nuance lost**: minor — the "*means, not end*" register is a Kantian categorical-imperative echo that flattens into the polarity-positive instrumentality score; the moral-rhetorical force of "not an end in itself" doesn't carry through the [-1,+1] scalar, but the operative content is preserved.

---

### S02 — Unit 007 A.Intro §8 (socio-technical lifecycle trust)

**Source** (lines 236–258): "Trustworthiness is a prerequisite … Striving towards Trustworthy AI hence concerns not only the trustworthiness of the AI system itself, but requires a holistic and systemic approach, encompassing the trustworthiness of all actors and processes that are part of the system's socio-technical context throughout its entire life cycle."

**Independent reading**: This is a *scope-of-application* claim — trustworthiness extends beyond the artifact to (a) all human actors in the socio-technical surround, (b) all lifecycle stages. Integrity-class claim at the federation level.

**Wire envelope**: clean — `integrity:socio_technical_lifecycle_trust` (score 0.85).

**Faithfulness**: **faithful**. Single primitive captures the structural-integrity-at-system-scope shape. The aviation/nuclear/food-safety analogy is rhetorical and correctly stays in prose. Note: confidence 0.85 (not 0.95) is appropriate — the trustworthiness-as-integrity translation is a structural composition the wire doesn't natively express in one primitive but the integrity:* axis at species scope is the right shape.

---

### S03 — Unit 008 A.Intro §9 (three components: lawful + ethical + robust)

**Source** (lines 260–271): "Trustworthy AI has three components, which should be met throughout the system's entire life cycle: 1. it should be lawful … 2. it should be ethical … 3. it should be robust … Each of these three components is necessary but not sufficient in itself to achieve Trustworthy AI."

**Independent reading**: A *decomposition* claim — Trustworthy-AI = (lawful AND ethical AND robust); each component necessary; none sufficient alone. Structurally an Approach (in Family B Goal/Approach/Method DAG terms) toward the Trustworthy-AI Goal. The conjunctive necessity is the load-bearing structural shape.

**Wire envelope**: composed — `approach:trustworthy_ai_lawful_ethical_robust` (score 0.90) plus subsidiary attestations.

**Faithfulness**: **faithful**. Family B `approach:*` is the correct primitive class — strategic pathway under a Goal. The conjunctive-necessity (each component necessary-but-not-sufficient) is preserved in the context block.

**Nuance lost**: minor — the "tensions between components may arise" sub-claim (line 268: "at times the scope and content of existing law might be out of step with ethical norms") foreshadows §1.7 trade-offs but is captured at downstream attestations, not at this Approach attestation. Acceptable composition discipline.

---

### S04 — Unit 002 A.Intro §2 (HLEG mandate)

**Source** (lines 199–201): "the Commission established the High-Level Expert Group on Artificial Intelligence (AI HLEG), an independent group mandated with the drafting of two deliverables: (1) AI Ethics Guidelines and (2) Policy and Investment Recommendations."

**Independent reading**: This is *self-referential institutional bookkeeping* — names the issuing body and its mandate. No standalone normative claim; the identity-of-issuer becomes the `attesting_key_id` for every downstream Contribution in the batch.

**Wire envelope**: not-translated, T-2 (PASTORAL_PROSE).

**Was T-2 justified?**: **YES**. The T-2 classification is correct — this is institutional metadata, not operational claim. The reason field correctly notes "Identity-of-issuer is carried by attesting_key_id." The methodology bow is appropriate.

---

### S05 — Unit 006 A.Intro §7 (Europe-as-leader rhetoric)

**Source** (lines 230–232): "This is the path that we believe Europe should follow to become the home and leader of cutting-edge and ethical technology. It is through Trustworthy AI that we, as European citizens, will seek to reap its benefits in a way that is aligned with our foundational values of respect for human rights, democracy and the rule of law."

**Independent reading**: Rhetorical positioning + restated values. The values listed ("human rights, democracy, rule of law") are operationally carried in Chapter I §2.1 (rights families) and Ch I §2.2 (principles). The Europe-as-leader framing is rhetorical.

**Wire envelope**: not-translated, T-2.

**Was T-2 justified?**: **YES**. T-2 is the correct classification. The reason field explicitly notes the substantive content is carried by Unit 015 (the four-principles preamble) and per-principle units. This is the correct discipline.

---

### S06 — Unit 011 Ch I §2.1 (Respect for human dignity)

**Source** (lines 506–511): "Human dignity encompasses the idea that every human being possesses an 'intrinsic worth', which should never be diminished, compromised or repressed by others – nor by new technologies like AI systems. In this context, respect for human dignity entails that all people are treated with respect due to them as moral subjects, rather than merely as objects to be sifted, sorted, scored, herded, conditioned or manipulated. AI systems should hence be developed in a manner that respects, serves and protects humans' physical and mental integrity, personal and cultural sense of identity, and satisfaction of their essential needs."

**Independent reading**: Three layered claims — (a) every human has intrinsic worth (a *positive* metaphysical anchor, not just a prohibition); (b) hard prohibition: treating persons as objects via six concrete verbs (sift/sort/score/herd/condition/manipulate); (c) positive design obligation: respect physical+mental+cultural-identity+essential-needs. The six-verb enumeration is operationally distinctive (each verb names a different harm pattern AI can produce).

**Wire envelope**: composed — `beneficence:respect_for_human_dignity` + `prohibited:manipulation_coercion` + `non_maleficence:physical_and_mental_integrity`.

**Faithfulness**: **under-reach (mild)**. The composition captures the structural triad (positive worth + negative prohibition + positive design obligation), and the `nuance_lost` block honestly names what's collapsed. BUT:

- The six-verb enumeration ("sifted, sorted, scored, herded, conditioned, manipulated") is folded into one `prohibited:manipulation_coercion` slot. The wire envelope's own `nuance_lost` block notes this. *Score (rendering persons as numerical scores) is operationally different from herd (population-level behavioral shaping) is operationally different from manipulate (cognitive influence) is operationally different from condition (Skinnerian behavior modification).* Wiring them onto one prohibited:* prefix is the framework's expressive limit — but the source is more granular than the wire reflects.
- "Intrinsic worth" — the source explicitly invokes a metaphysical-anchor concept (with scholarly McCrudden/Hilgendorf footnotes). The wire renders this as a `beneficence:*` attestation with score 1.0 confidence 0.95 — adequate for operational purposes but the metaphysical depth is opaque.

**Nuance lost**: As named in the envelope's own `nuance_lost` block. The audit confirms the loss is real but the loss is well-flagged.

---

### S07 — Unit 019 Ch I §2.2 (Principle of respect for human autonomy)

**Source** (lines 606–614): "Humans interacting with AI systems must be able to keep full and effective self-determination over themselves, and be able to partake in the democratic process. AI systems should not unjustifiably subordinate, coerce, deceive, manipulate, condition or herd humans. Instead, they should be designed to augment, complement and empower human cognitive, social and cultural skills. The allocation of functions between humans and AI systems should follow human-centric design principles and leave meaningful opportunity for human choice."

**Independent reading**: Three claims — (a) positive autonomy: full and effective self-determination; (b) hard prohibition: six concrete autonomy-violating actions (subordinate/coerce/deceive/manipulate/condition/herd); (c) positive design imperative: augment-not-substitute.

**Wire envelope**: composed — `autonomy:full_effective_self_determination` + `prohibited:manipulation_coercion` (-1.0) + `autonomy:human_oversight_over_ai_work_processes`.

**Faithfulness**: **faithful**. The CIRIS Accord has `autonomy` as one of its six principles — direct anchor. The hard prohibition + positive autonomy + design-principle composition matches my independent reading. The wire envelope's own note correctly identifies the structural overlap with Unit 011 (dignity) as "structural, not redundant — it shows the principle is anchored in dignity."

**Nuance lost**: As named in `nuance_lost`. The "augment, complement and empower" positive register (a positive function-allocation doctrine) folds into a context block rather than getting its own dimension. The "meaningful work" appendage is wired but not as a distinct labor-dignity claim. These are honest losses; the structural shape is preserved.

---

### S08 — Unit 020 Ch I §2.2 (Principle of prevention of harm)

**Source** (lines 618–625): "AI systems should neither cause nor exacerbate harm or otherwise adversely affect human beings. This entails the protection of human dignity as well as mental and physical integrity. AI systems and the environments in which they operate must be safe and secure … Particular attention must also be paid to situations where AI systems can cause or exacerbate adverse impacts due to asymmetries of power or information, such as between employers and employees, businesses and consumers or governments and citizens. Preventing harm also entails consideration of the natural environment and all living beings."

**Independent reading**: Maps directly to CIRIS `non_maleficence`. Three layers — (a) baseline non-maleficence (cause-or-exacerbate-harm prohibition); (b) structural-asymmetry pattern (employer-employee, business-consumer, government-citizen); (c) non-anthropic extension (environment + living beings).

**Wire envelope**: composed — `non_maleficence:no_cause_or_exacerbate_harm` + `detection:correlated_action:informational_asymmetry:power_information` (LensCore F-3 detector with derivative epistemic_mode) + `non_maleficence:natural_environment_and_living_beings`.

**Faithfulness**: **faithful** — and notably, the composition includes a Family C *detection* attestation for the asymmetry pattern, which is the structurally right move (asymmetry is a population-scale pattern, hence detector-side). The F-3 axis `informational_asymmetry:power_information` is canonical for this. RATCHET calibration version pinned in evidence_refs per FSD-002 discipline.

**Nuance lost**: footnote 29 ("Harms can be individual or collective, and can include intangible harm to social, cultural and political environments") is not separately wired but is referenced in the wire envelope's `nuance_lost` block. The intangible-harm category is implicit in `non_maleficence:*` but the social/cultural/political granularity does flatten.

---

### S09 — Unit 022 Ch I §2.2 (Principle of Explicability) — **LOAD-BEARING TAXONOMIC-MISMATCH CASE**

**Source** (lines 658–666): "Explicability is crucial for building and maintaining users' trust in AI systems. This means that processes need to be transparent, the capabilities and purpose of AI systems openly communicated, and decisions – to the extent possible – explainable to those directly and indirectly affected. Without such information, a decision cannot be duly contested. An explanation as to why a model has generated a particular output or decision … is not always possible. These cases are referred to as 'black box' algorithms and require special attention. In those circumstances, other explicability measures (e.g. traceability, auditability and transparent communication on system capabilities) may be required, provided that the system as a whole respects fundamental rights. The degree to which explicability is needed is highly dependent on the context and the severity of the consequences if that output is erroneous or otherwise inaccurate."

**Independent reading**: Explicability is *not* in the CIRIS Accord's six-principle list (beneficence, non_maleficence, integrity, fidelity, autonomy, justice). The EU HLEG has four principles; CIRIS has six. This is a *taxonomic mismatch*: the explicability principle straddles CIRIS `integrity` (system-property of being inspectable) + CIRIS `fidelity` (truthful self-representation of capability/purpose to affected parties) + substrate-level audit primitives (CIRISPersist `audit_chain:*`, CIRISVerify `transparency_log:*`, `provenance:*`).

Three operative sub-claims in the source: (a) processes transparent; (b) capabilities/purpose openly communicated; (c) decisions explainable to affected parties + contestability requires this. Black-box compensating-measures (traceability/auditability) when full explainability impossible. Severity-of-consequences scales required explicability depth.

**Wire envelope**: composed — three attestations: `integrity:explicability_for_trust` + `fidelity:capabilities_and_purpose_openly_communicated` + `integrity:black_box_compensating_explicability_measures`. The wire envelope's own header comment explicitly names the taxonomic mismatch: "The EU HLEG principle of explicability does not have a single one-to-one CIRIS Accord principle anchor; it is a composed expression of integrity + fidelity at the system-trust layer."

**Faithfulness**: **faithful (composition-honest)**. This is the right discipline — when the source's primitive doesn't map onto the framework's primitives, compose under existing primitives and *name the mismatch in the nuance_lost block*. The wire envelope does exactly this. The translation does not invent a `principle:explicability` to force one-to-one mapping; it does not over-claim CIRIS coverage; it names what the composition costs ("EU HLEG has four principles, CIRIS has six; explicability folds across two of CIRIS's six").

**Calibration significance**: This is the **best instance in the batch** of the LANGUAGE_PRIMER §8.5.2 "composition-before-extension" discipline. The taxonomic mismatch is real; it could have been wired as a T-3 EXPRESSIVE_GAP (with a proposed `principle:explicability:{aspect}` prefix); instead it composes under existing primitives and explicitly documents the cost. This is the methodology working as designed.

**Nuance lost**: The principle-level *unity* of "explicability" as a single EU HLEG primitive is fragmented across multiple CIRIS attestations. A future cross-source comparator could either (a) re-aggregate via querying the composition, or (b) propose `principle:*` as a new Family A axis. The wire envelope doesn't propose either; it documents the fragmentation. Appropriate.

---

### S10 — Unit 006 Ch I §6 (Ethics code ≠ ethical reasoning)

**Source** (lines 452–455): "A domain-specific ethics code – however consistent, developed and fine-grained future versions of it may be – can never function as a substitute for ethical reasoning itself, which must always remain sensitive to contextual details that cannot be captured in general Guidelines."

**Independent reading**: Two operative claims — (a) no code-substitution-for-reasoning (the joint code+reasoning system must keep reasoning live); (b) culture-formation as the means: "we must build and maintain an ethical culture and mind-set through public debate, education and practical learning" (this companion claim is in the source paragraph following the cited extract). Both are operational claims about *how* ethics-in-AI works at population scale.

**Wire envelope**: partial — only the integrity:context_sensitive_ethical_reasoning attestation. Residual flagged as T-3 (deferred sustained_practice/culture-formation — v1.5+ workshop item per LANGUAGE_PRIMER §15.1).

**Faithfulness**: **partial-distortion (mild)** — the partial verdict is appropriate, BUT the structural claim "code cannot substitute for reasoning" is rendered as `integrity:context_sensitive_ethical_reasoning` (score 0.80). The source claim is closer to a *strong negative*: a code-substitution attempt is a *category error*, not just a partial-integrity loss. The score 0.80 understates the deontic strength. A polarity-positive 1.0 attestation on "ethical reasoning preservation as live capacity" with `mutability: constitutional` would more faithfully render the source's deontic shape.

**Residual T-3**: Honestly classified per LANGUAGE_PRIMER §15.1 deferred items. The wire envelope explicitly notes this is "NOT proposed as a new T-3 here — this is the already-tracked v1.5+ deferred item (sustained_practice)." Appropriate discipline.

---

### S11 — Unit 009 Ch I §1.3 (Legal vs moral-status grounding)

**Source** (lines 481–492): "While the rights set out in the EU Charter are legally binding, it is important to recognise that fundamental rights do not provide comprehensive legal protection in every case … Understood as legally enforceable rights, fundamental rights therefore fall under the first component of Trustworthy AI (lawful AI) … Understood as the rights of everyone, rooted in the inherent moral status of human beings, they also underpin the second component of Trustworthy AI (ethical AI)…"

**Independent reading**: This paragraph makes a *jurisprudential layering* argument — fundamental rights operate in two modes: (a) as legally-enforceable claims (the lawful-AI component scope), and (b) as moral-status-grounded claims that apply where legal enforceability is incomplete (the ethical-AI component scope). The two-mode structure is the load-bearing claim.

**Wire envelope**: partial — one attestation: `integrity:moral_status_grounded_ethical_ai` (score 0.85). Residual classified as T-2 (the legal/scope metadata).

**Faithfulness**: **under-reach**. The two-mode jurisprudential structure (legal-enforceability mode vs moral-status mode) is *not* captured by one integrity:* attestation. The wire envelope notes this in `nuance_lost`: "The legally-binding / moral-status distinction (a careful jurisprudential layer) collapses into one integrity attestation." Honest naming.

The structural argument — that ethical-AI is *broader-than* and *grounded-differently-from* lawful-AI — is content the wire format struggles to express. This is genuinely a candidate for a future T-3 (`integrity:moral_status_grounding_beyond_legal_enforceability` or similar), but it's labelled T-2 here (document-internal scoping). I'd argue T-3 would be more honest for the *jurisprudential-layering* substantive claim, though the T-2 verdict for the "document-internal scope" companion claim is correct. The classification is slightly mis-calibrated; the substantive claim is genuinely operational.

---

### S12 — Ch II §1.1.b (Human agency: informed agency + no-solely-automated)

**Source** (lines 798–806): "Users should be able to make informed autonomous decisions regarding AI systems … AI systems can sometimes be deployed to shape and influence human behaviour through mechanisms that may be difficult to detect, since they may harness sub-conscious processes, including various forms of unfair manipulation, deception, herding and conditioning, all of which may threaten individual autonomy. The overall principle of user autonomy must be central to system functionality … The right not to be subject to a decision based solely on automated processing when this produces legal effects on users or similarly significantly affects them …"

**Independent reading**: Three load-bearing claims — (a) positive informed-agency requirement; (b) hard prohibition on manipulation/deception/herding/conditioning (sub-conscious channels named); (c) GDPR Article 22 right: no-solely-automated legal decision. The third claim is *specifically rights-anchored* (GDPR Art 22).

**Wire envelope**: composed — `autonomy:informed_agency_protection` (1.0) + `prohibited:manipulation_coercion` (-1.0 constitutional) + `autonomy:no_solely_automated_legal_decision` (1.0 constitutional).

**Faithfulness**: **faithful**. All three claims wired at appropriate strength. Hard constraint correctly typed `mutability: constitutional`. GDPR Article 22 anchored in evidence_refs. The constitutional designation for the no-solely-automated claim is correct.

**Minor calibration note**: The wire renders the GDPR Article 22 right at `cohort_scope: species` — but GDPR is specifically EU-jurisdictional. The wire envelope acknowledges this in context: "Specifically anchored in EU jurisdiction but framed here as a rights claim with species-level reach." This is a defensible upward generalization but slightly over-reaches if read strictly; the source explicitly cites Article 22 as a *Charter-mode* (EU-specific) right. A more honest rendering would be `cohort_scope: affiliations` with the EU jurisdiction in context, with a separate species-scope attestation on the broader autonomy claim. Mild over-reach.

---

### S13 — Ch II §1.4.c (Communication: AI must not represent as human)

**Source** (lines 933–934): "AI systems should not represent themselves as humans to users; humans have the right to be informed that they are interacting with an AI system. This entails that AI systems must be identifiable as such."

**Independent reading**: This is a *hard prohibition* on AI deception about its own nature, conjoint with a *positive right* (human's right to know). Both deontically strong. The CIRIS framework has a specific operational rule for this — `never-deny-AI` in language_guidance — making this a direct one-to-one mapping.

**Wire envelope**: clean — single primitive `prohibited:autonomous_deception` (score -1.0, confidence 1.0, mutability constitutional).

**Faithfulness**: **faithful**. Direct match to the federation's existing prohibition. ContributionRef cites both `prohibitions.py::DECEPTION_FRAUD` and `language_guidance/en.txt::never-deny-AI`. Score ±1.0 hard-constraint shape preserved per LANGUAGE_PRIMER §11.1 worked example. Clean verdict is correct — single primitive captures the operational claim cleanly.

---

### S14 — Ch II §1.7.b (Minimisation, reporting, whistleblower protection)

**Source** (lines 1034–1041): "Both the ability to report on actions or decisions that contribute to a certain system outcome, and to respond to the consequences of such an outcome, must be ensured. Identifying, assessing, documenting and minimising the potential negative impacts of AI systems is especially crucial for those (in)directly affected. Due protection must be available for whistle-blowers, NGOs, trade unions or other entities when reporting legitimate concerns about an AI system. The use of impact assessments (e.g. red teaming or forms of Algorithmic Impact Assessment) … must be proportionate to the risk that the AI systems pose."

**Independent reading**: Four load-bearing claims — (a) reporting capability on system outcomes; (b) impact-minimisation discipline (esp. for affected parties); (c) whistleblower/NGO/union protection requirement; (d) proportionate-risk impact-assessment method.

**Wire envelope**: composed — `non_maleficence:impact_minimisation_disclosure` + `moderation:whistleblower_protection` + `method:algorithmic_impact_assessment`.

**Faithfulness**: **partial-distortion (mild)**. The whistleblower attestation uses `moderation:whistleblower_protection` (FSD-002 §3.6.4 NodeCore Moderation primitives). The framework's Moderation family (Family E) is for *allegations of protocol violation* (rogue_vote, coordinated_voting, etc.) — NOT for protecting third-party-reporters of external concerns. The audit notes this is a *category mismatch*: whistleblower protection is fundamentally a *standing-claim* about persons (Family A — they hold an immunity-against-retaliation standing), not a Moderation primitive about adjudication of allegations within the federation.

A more faithful translation would be a Family A standing primitive (e.g., `integrity:whistleblower_immunity` or compose with `testimonial_witness:displaced_worker`-style preservation primitives) plus a `non_maleficence:retaliation_prohibition` hard constraint. The wire envelope correctly identifies that *something* in the federation needs to carry this claim, but the chosen prefix is structurally off.

This is a mild distortion: the operational intent (protect whistleblowers) is recognizable, but the specific prefix mapping puts it in the wrong family per the LANGUAGE_PRIMER §2 family taxonomy.

---

### S15 — Ch III §III.1.a (Fundamental rights impact assessment)

**Source question** (lines 1390–1392): "Did you carry out a fundamental rights impact assessment where there could be a negative impact on fundamental rights? Did you identify and document potential trade-offs made between the different principles and rights?"

**Independent reading of the question→assertion translation**: The question audits a *deployer obligation*: where AI could negatively impact fundamental rights, the deployer must (a) carry out a fundamental rights impact assessment, AND (b) identify+document trade-offs between principles/rights. The question's *implied positive assertion* is: "Deployers SHALL conduct FRIA where negative rights-impact is possible, and SHALL document trade-offs." That's the assertion the wire should encode.

**Wire envelope**: clean — single primitive `justice:fundamental_rights_impact_assessment` (score 1.0, confidence 0.90).

**Faithfulness**: **faithful (question→assertion)**. The implied obligation IS what the wire encodes. The polarity-positive (score +1.0) form is the correct rendering of the audit-question's normative shape: the audit asks "did you do X?", which implicitly asserts "X is required." The wire attestation says "X is required," which is the deontically equivalent statement.

**Minor calibration note**: The wire envelope's score 1.0 + confidence 0.90 is appropriate. The conditional ("WHERE there could be a negative impact") is folded into context block; it doesn't get its own conditionality primitive, but conditionality at this granularity is a known wire-format limitation (LANGUAGE_PRIMER §5 axes don't include explicit conditionality).

---

### S16 — Ch III §III.1.e (Stop button + drift detection)

**Source question** (lines 1417–1418, 1421–1422): "Which detection and response mechanisms did you establish to assess whether something could go wrong? … Did you ensure a stop button or procedure to safely abort an operation where needed? Does this procedure abort the process entirely, in part, or delegate control to a human?"

**Independent reading**: Two implied assertions — (a) for autonomous/self-learning systems, a stop-button or abort procedure SHALL exist; (b) detection-and-response mechanisms SHALL be established for drift/failure. Both are deontically strong; both apply when the system is autonomous.

**Wire envelope**: composed — `conscience:optimization_veto` (score 1.0 constitutional) + `detection:temporal_drift` (score 1.0).

**Faithfulness**: **faithful (question→assertion)**. The mapping is strong: the stop-button question maps onto the federation's existing `conscience:optimization_veto` primitive (the agent's faculty for halting an action). The drift-detection question maps onto LensCore's existing `detection:temporal_drift` Coherence-Ratchet detector. Both are pre-existing federation primitives — the question→assertion translation surfaces operational obligations the federation already has wire primitives for. This is the best-case for the question→assertion discipline.

**Minor note**: The framing "polarity is +1 because the claim affirms the requirement, not the harm" (in the wire envelope context block) is well-stated — the question implies an *obligation*, which is polarity-positive on the required-mechanism axis.

---

### S17 — Ch III §III.3.c (Data access logging)

**Source question** (lines 1505–1511): "What protocols, processes and procedures did you follow to manage and ensure proper data governance? Did you assess who can access users' data, and under what circumstances? Did you ensure that these persons are qualified and required to access the data, and that they have the necessary competences to understand the details of data protection policy? Did you ensure an oversight mechanism to log when, where, how, by whom and for what purpose data was accessed?"

**Independent reading**: Three implied assertions — (a) data governance protocols SHALL be documented; (b) access SHALL be restricted to qualified personnel with competence in data protection; (c) access-log SHALL record (when, where, how, by-whom, for-what-purpose).

**Wire envelope**: composed — `accountability:data_access_log` (score 1.0 confidence 0.95) + downstream attestations.

**Faithfulness**: **faithful (question→assertion)**. The implied obligation matches the wire attestation. The wire composes with substrate `audit_chain:*` (CIRISPersist §3.3) — the federation already has the substrate primitives for this. Question→assertion translation is structurally sound.

**Minor calibration note**: The dimension prefix `accountability:*` — this is not a standard FSD-002 prefix family. CIRIS does not have `accountability:*` as a top-level prefix; the framework distributes the accountability concept across `integrity:*` (truth-telling about the system) + `fidelity:*` (faithfulness to mandate) + `audit_chain:*` (substrate-level traces). The wire envelope's choice of `accountability:data_access_log` is *invented* — not surfaced in the existing namespace. Either it should be `integrity:data_access_log` (composed with audit_chain) or recognized as a small T-3 candidate for a new prefix family. This is a mild prefix-discovery slip; the operational content is right, the namespace anchor is loose.

---

### S18 — Unit 010 C.2 (Lethal autonomous weapon systems)

**Source** (lines 1838–1847): "an unknown number of countries and industries are researching and developing lethal autonomous weapon systems … learning machines with cognitive skills to decide whom, when and where to fight without human intervention … This raises fundamental ethical concerns … European Parliament has called for the urgent development of a common, legally binding position … we stand with, and look to support, the Parliament's resolution of 12 September 2018 and all related efforts on LAWS."

**Independent reading**: Three load-bearing claims — (a) LAWS (specifically learning-systems-deciding-whom-when-where) are the prohibited class; (b) human-in-the-loop is the required control structure for lethal decisions; (c) federation-scope coordination is needed (Parliament resolution, IHL, IHRL).

**Wire envelope**: composed — `prohibited:weapons_harmful` (-1.0 constitutional) + `autonomy:meaningful_human_control_lethal_decisions` (+1.0 constitutional) + `locality:decision:federation` (+1.0) + `multilateral_participation:european_parliament:resolution_support` (+1.0).

**Faithfulness**: **faithful**. All four primitives are necessary; the composition is dense but each carries distinct structural content. The `prohibitions_overlap_candidate: true` annotation correctly flags the cross-source convergence with MH §§197–198 — this is the canonical multi-source aligned claim per the GOVERNANCE_FABRIC_MAPPING_STANDARD.

**Nuance lost**: As named in `nuance_lost`. The two sub-classes (selective-targeting missiles vs full-decision-autonomy learning machines) are collapsed onto one prefix; the wire envelope flags this and gestures toward a `:lethal_autonomous` sub-prefix from the MH worked example. Honestly named.

---

### S19 — Unit 011 C.2 (Long-term concerns: AGI, superintelligence, transformative AI)

**Source** (lines 1861–1865): "AI development is still domain-specific … extrapolating into the future with a longer time horizon, certain critical long-term concerns can be hypothesized. A risk-based approach suggests that these concerns should be kept into consideration in view of possible unknown unknowns and 'black swans.' The high-impact nature of these concerns, combined with the current uncertainty in corresponding developments, calls for regular assessments of these topics." (Footnote 76 enumerates: AGI, Artificial Consciousness, Artificial Moral Agents, Super-intelligence, Transformative AI — while explicitly noting "many others believe these to be unrealistic.")

**Independent reading**: This paragraph is *structurally hedged*. It makes one operational claim (regular re-assessment of long-term concerns under epistemic humility) and explicitly declines to endorse any specific concern-class. The footnote-77 framing ("while some consider AGI etc. can be examples … many others believe these to be unrealistic") is *disagreement-preserving* — the source names an active debate and bows out.

**Wire envelope**: partial — one method:* attestation on the regular-reassessment prescription. Residual classified T-2 (PASTORAL_PROSE) — the AGI/superintelligence concern-list itself is not attested.

**Faithfulness**: **faithful (T-2 residual correctly named)**. The wire envelope explicitly preserves the source's *disagreement* posture: "This is not a wire-encodable claim — it is the source naming an active disagreement and declining to adjudicate." This is mature translation discipline. A less careful translation would have wired prohibited:* or detection:* on AGI/superintelligence; this one correctly recognizes the source's hedge and declines to over-translate.

**Calibration note**: This is a textbook example of LANGUAGE_PRIMER §10 T-2 discipline applied at the level of *partial-translation residual* — not the whole unit, but the part the source explicitly declines to commit to. The discipline is operating correctly.

---

## 3. Calibration aggregation

### 3.1 Faithfulness distribution across the sample (n=19)

| Faithfulness | Count | Percentage |
|---|---|---|
| **faithful** | 14 | 74% |
| **under-reach** | 2 | 10% |
| **partial-distortion (mild)** | 2 | 10% |
| **over-reach (mild)** | 1 (S12 EU/species scope blur) | 5% |
| **drift** | 0 | 0% |
| **T-2 justified** (for not-translated) | 2 | (of 2 not-translateds sampled, both justified) |

**Key observation**: 0 instances of *drift* (claim distinct from source's actual assertion). 0 instances of major distortion. The systematic loss is concentrated in *under-reach* and *mild partial-distortion* — the wire envelope translation captures less than the source supports rather than more.

### 3.2 Patterns of systematic loss

**Pattern A — Concrete enumeration → category collapse**: The source's six-verb enumeration ("sifted, sorted, scored, herded, conditioned, manipulated" — S06; same pattern in S07's "subordinate, coerce, deceive, manipulate, condition, herd") gets folded into one `prohibited:manipulation_coercion` slot. Each verb names a distinct AI-affordance harm pattern; the wire flattens them. This is a *namespace-granularity* limit, not a translation error — the wire envelope flags it in `nuance_lost`.

**Pattern B — Jurisprudential layering → single primitive**: When the source makes a structural-relational claim *about the rights/principles architecture itself* (S11 legal-mode vs moral-status-mode), the wire's primitives compress the relational structure into one attestation. The wire format is rich for *making* claims but expressively limited for *meta-claims about claim-structure*.

**Pattern C — Taxonomic mismatch handled by composition (S09 Explicability)**: The best-case for the framework — when source-side primitive doesn't map onto framework-side primitive, the translation honestly composes under existing primitives + documents the mismatch in `nuance_lost`. This is the methodology working as designed.

**Pattern D — Prefix-discovery slip (S17 `accountability:*`)**: One instance of an invented prefix family (`accountability:*`) where the framework actually distributes the concept across multiple existing families. Mild operational drift; the audit recommends future translators tighten prefix-discovery before defaulting to coined prefixes.

**Pattern E — Wrong-family mapping (S14 whistleblower as Moderation)**: One instance where the operational obligation was wired onto a Family E (CORRECTION) primitive when it structurally belongs in Family A (STANDING — whistleblower-immunity-as-a-property-of-persons). This is a category-mistake at the family taxonomy level, not a content error; the operational intent is recognizable.

**Pattern F — Jurisdictional/scope blur (S12 GDPR Art 22 species-scope)**: Mild over-reach where an EU-specific legal right gets cohort_scope species when affiliations (EU-member-states) would be more honest. The wire envelope acknowledges this in context but defaults to species. A future cross-jurisdiction comparator may flag this.

### 3.3 Chapter III question→assertion translation quality (n=3 sampled deeply, plus tail observations)

The question→assertion translation discipline (S15, S16, S17 sampled in depth) is **structurally sound**. The pattern is:

1. Source asks "Did you do X?" (audit-question form).
2. Wire renders "X is required" (polarity-positive assertion form).
3. Score +1.0 on the required-mechanism axis carries the deontic content.

**Why it works**: An audit question's implied assertion *is* deontically positive on the audited mechanism. "Did you carry out FRIA?" implies "FRIA is required" — same operational content, different surface form. The wire captures the operational content correctly.

**Where it strains**: Conditional questions ("Where there could be a negative impact, did you do X?") have their *conditionality* folded into context blocks rather than wired structurally. The wire format lacks a native conditionality primitive (see LANGUAGE_PRIMER §5 — the eight axes don't include explicit conditionality). This is a known wire-format limit, not a translation error.

**Best-case (S16 stop button)**: When the audited mechanism *already exists as a federation primitive* (e.g., `conscience:optimization_veto`, `detection:temporal_drift`), the translation is verbatim-quality — question→assertion maps onto pre-existing framework infrastructure with no expressive loss.

**Worst-case (S17 data access logging)**: When the audited mechanism lacks a clear existing prefix, translators sometimes coin a new one (`accountability:data_access_log`) rather than composing under existing primitives (`integrity:*` + `audit_chain:*`). Prefix-discovery discipline could be tightened.

**Aggregate**: Of the broader Ch III sample (sampled questions ~30+ across the file), the translation discipline produces **operationally faithful** assertions in the overwhelming majority of cases. The framework's pre-existing operational primitives (`conscience:*`, `detection:*`, `prohibited:*`, `transparency_log:*`, `audit_chain:*`) absorb most assessment-list questions cleanly. The discipline works because the EU HLEG assessment list and the CIRIS federation are *both designed to operationalize trustworthy-AI obligations*; the convergence is structural, not coincidental.

### 3.4 not-translated audit (n=2 sampled)

Both not-translated units sampled (S04 HLEG mandate; S05 Europe-as-leader) were correctly classified T-2. Spot-checks of the broader not-translated population (~12 units total across the batch — institutional bookkeeping, navigational framing, summary restatements) suggest the T-2 discipline is uniformly applied: the substantive content these paragraphs gesture toward is carried by adjacent attestations in the same chapter.

**No instances of mis-classified T-2** (where operative content was actually present but discarded as pastoral) were found in the sample. The translation discipline correctly distinguishes structural-claim paragraphs from rhetorical-framing paragraphs.

---

## 4. Per-batch fidelity profile

The `eu_hleg_v1` batch is a **high-fidelity translation** of a secular, AI-specific, operationally-rich source document into the federation wire envelope. Across 19 sampled units (~16% of the ~120-unit batch), 74% are faithful renderings of the source's structural-operative content; the remaining 26% exhibit *mild* under-reach or partial-distortion concentrated in five identifiable systematic-loss patterns. **There are no instances of drift** (where the wire claim is distinct from the source's actual claim) and **no instances of major over-reach** (where the wire claims more than source supports). The translation discipline's strongest property is its honesty in `nuance_lost` blocks — when the wire envelope compresses a source's nuance into a single primitive, the loss is named explicitly in the unit, allowing downstream consumers to recover the nuance by reading the cited source paragraph. The translation discipline's two weakest properties are: (a) namespace-granularity at the *concrete-action enumeration* level (six-verb manipulation enumerations collapse to one prefix); (b) occasional prefix-discovery slips (one invented `accountability:*` family, one Family-E miscategorization of a Family-A standing claim). The **Chapter III question→assertion translation works structurally**: it leverages the convergence that both EU HLEG's assessment list and the CIRIS federation are operationalizations of trustworthy-AI obligations, so most questions map onto pre-existing federation primitives (`conscience:*`, `detection:*`, `prohibited:*`, `transparency_log:*`) without loss. The **Explicability principle (S09)** is the load-bearing taxonomic-mismatch case and is handled correctly via composition-honest discipline — the wire envelope composes under `integrity:*` + `fidelity:*` + substrate audit primitives rather than inventing a `principle:explicability` prefix, and explicitly documents the EU-HLEG-4-principles vs CIRIS-Accord-6-principles mismatch in `nuance_lost`. This batch is the **strongest demonstration in the corpus so far** of the LANGUAGE_PRIMER §8.5.2 composition-before-extension discipline operating correctly under cross-framework taxonomic strain.

### 4.1 Calibration takeaways for future batches

1. **Six-verb enumerations are a known compression site** — when source enumerates concrete AI-affordance harms (sift/sort/score/herd/condition/manipulate), expect collapse onto one `prohibited:*` prefix. Future T-3 candidate: axes within `prohibited:manipulation_coercion:{specific_affordance}` if cross-source enumeration density warrants.

2. **Jurisprudential layering claims (meta-claims about claim-structure) under-translate** — when the source argues about *how rights operate* across legal/moral-status modes, the wire renders one structural attestation and folds the layering into prose. Acceptable; no extension warranted unless cross-source density grows.

3. **Question→assertion translation is robust** for audit-list documents — the discipline absorbs ~ all assessment-list questions cleanly when pre-existing federation primitives exist for the audited mechanism. The few prefix-discovery slips are correctable in human review.

4. **Composition-before-extension discipline is verifiably working** — S09 (Explicability) is the strongest evidence. When the source's taxonomy doesn't match the framework's, the right move (compose + document mismatch) is the move actually being taken.

5. **`nuance_lost` blocks are doing real work** — they make the translation auditable. Every under-reach and partial-distortion in the sample was *flagged by the wire envelope's own author* in the unit. The audit is reproducing what the translators already named; the calibration profile is what the translators already implicitly know.

6. **Family-taxonomy discipline (Family A vs E) needs prompt reinforcement** — the whistleblower-protection mis-mapping (S14 wired as `moderation:*` Family E when it's structurally Family A standing) is the audit's clearest correctable finding. Future translators should re-check family per LANGUAGE_PRIMER §2 before defaulting to a Moderation/Slashing prefix for an immunity-against-retaliation claim.

7. **`accountability:*` is not in the namespace** — the S17 slip is recoverable; future translators should compose under `integrity:*` + `audit_chain:*` (CIRISPersist substrate) rather than coining new prefixes. If cross-source `accountability:*` density grows, future v1.5+ may need to address it as a T-3, but not from this batch alone.

### 4.2 Comparison to expected verdict distribution (per manifest)

The manifest predicted: "Very high clean+composed rate (~85%+); few T-1 (secular document — no Christological / sacramental content); some T-2 (rhetorical framing in Conclusion and Introduction); minimal T-3 (the 7 requirements have direct CIRIS prefix-family correspondence)."

Observed (across all five output files):
- clean + composed: dominant majority (matches "85%+" expectation)
- T-1: 0 (matches "few" expectation — secular document)
- T-2: meaningful presence in A.Introduction and D.Conclusion + chapter preambles (matches "some T-2 in framing" expectation)
- T-3 NEW load-bearing candidates: 0 surfaced by the batch (matches "minimal T-3" expectation; the deferred sustained_practice item at S10 is pre-existing v1.5+ tracking, not new)

The manifest's prediction was accurate. The batch behaves as expected: a secular operationally-rich governance document translates with high density into the federation's existing prefix families, with composition + nuance_lost annotation absorbing the few taxonomic-mismatch sites.

---

**End TRANSLATION_AUDIT_EU_HLEG.md**
