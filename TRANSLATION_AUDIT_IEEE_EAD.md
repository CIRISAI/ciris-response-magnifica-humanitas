# TRANSLATION_AUDIT_IEEE_EAD.md

**Audit type**: Phase 4 translation-quality audit (DIAGNOSTIC for CALIBRATION, NOT break/fix).
**Batch**: `ieee_ead_v1` (IEEE Ethically Aligned Design, First Edition, 2019; 11 chapters).
**Auditor posture**: source-first; classify what's lost; do not propose fixes.
**Date**: 2026-05-27.
**Wire format under audit**: FSD-002 v1.4 / LANGUAGE_PRIMER v1.1.

---

## 1. Sampling methodology

20 units sampled, distributed across all 11 chapters and the four verdict categories per the prompt's strategic targets. For each unit I (a) located the source paragraph in `ead1e.txt` by the line refs cited in the wire envelope's `evidence_refs[]`; (b) read the source paragraph cold and formed an independent reading of the operative claim; (c) compared that reading against the wire envelope's claim, polarity, scope, and mutability; (d) classified faithfulness; (e) noted specific nuance lost.

**Quota satisfied**:

| Verdict bucket | Target | Sampled |
|---|---|---|
| clean | 6 | 6 |
| composed | 6 | 6 |
| partial | 4 | 4 |
| not-translated | 4 | 4 |
| **Total** | **20** | **20** |

**Chapter coverage**: Ch1 ×1; Ch2 ×3 (incl. 2 of the 8 General Principles per prompt); Ch3 ×5 (incl. 2 T-1 candidates per prompt); Ch4 ×0 *(I sampled 5 from Ch3 to cover the multi-tradition requirement and 4 from Ch5 to cover the T-3 requirement; Ch4 is unsampled — chapter-coverage gap noted, but the audit budget of 20 units would otherwise stretch too thin)*; Ch5 ×4 (incl. 2 T-3 candidates + the cross-source-conflict §3.4 per prompt); Ch6 ×1; Ch7 ×0; Ch8 ×2; Ch9 ×0; Ch10 ×1; Ch11 ×3 (incl. scope-management check per prompt).

Chapter coverage gap on Ch4/Ch7/Ch9 acknowledged. Calibration aggregation below is conditioned on the sample, not extrapolated as chapter-uniform.

---

## 2. Per-unit audit

### Unit 1 — §P1.0 (Ch2) — Principle 1: Human Rights statement

**Source paragraph** (lines 910–916): *"A/IS shall be created and operated to respect, promote, and protect internationally recognized human rights."*

**Independent reading**: Constitutional-strength deontic claim ("shall") binding A/IS lifecycle to a corpus of internationally-recognized human rights instruments. The operative content is the bind itself + the deontic strength + the reference to "internationally recognized" (i.e., not bespoke / not author-defined) rights.

**Envelope claim**: `justice:human_rights_respect_promote_protect` at score 1.0, mutability `constitutional`, cohort `species`.

**Faithfulness**: **faithful**. The constitutional mutability flag carries the "shall" deontic strength; cohort_scope species is correct; the justice principle anchoring is correct. The `delegates_to` references to the named treaty corpus (UDHR, ICCPR, CRC, CEDAW, CRPD, Geneva) are pinned in `§P1.refs` separately, preserving the "internationally recognized" anchoring.

**Nuance lost**: The tripartite verb structure ("respect, promote, AND protect") collapses into one envelope. Respect (negative duty), promote (positive duty), protect (positive duty against third parties) are three distinct deontic structures in human-rights law; the envelope encodes them as one composite score. This is rhetorical/stylistic in the wire-format sense but is load-bearing in human-rights law itself.

---

### Unit 2 — §P2.0 (Ch2) — Principle 2: Well-being primary success criterion

**Source paragraph** (lines 1004–1012): *"A/IS creators shall adopt increased human well-being as a primary success criterion for development."*

**Independent reading**: A constitutional-strength claim that well-being is the *primary* success metric (not "a" metric — *primary*) for A/IS development. The "primary" word is load-bearing: it ranks well-being above the dominant industry metrics (GDP, profit, consumption — explicitly contrasted in the Background paragraph). The deontic force binds to *creators*, not deployers.

**Envelope claim**: `beneficence:wellbeing_primary_success_criterion` at score 1.0, mutability `constitutional`, cohort `species`.

**Faithfulness**: **partial-distortion**. The dimension name preserves "primary," but the wire envelope does not carry the *ranking-against-other-metrics* mechanism. The Background's explicit contrast against GDP/profit/consumption-as-success-metrics is the operative content of "primary," and that contrast is unmapped. Reader of the envelope cannot reconstruct what "primary" defeats.

The envelope's own `nuance_lost` field acknowledges this honestly ("ranking against other criteria... does not natively encode"), which is the right disposition — but the verdict should arguably be **partial** with a T-3 candidate (an `objective:ranked_priority:{class}` or equivalent metric-ranking mechanism), not clean.

**Verdict-vs-classification mismatch**: envelope says `clean`; my reading says `partial` with operative-content unmapped. This is a calibration finding.

---

### Unit 3 — §Ch2.0 (Ch2) — Chapter preamble (composed)

**Source paragraph** (lines 824–852): Defines the General Principles as imperatives across the full A/IS lifecycle (design, development, deployment, adoption, decommissioning); enumerates stakeholder scope (creators, operators, other users, affected parties); lists three high-level goals (highest ideals of human beneficence within human rights; prioritize humanity + natural environment over commercial; mitigate risks/misuse via accountability + transparency).

**Independent reading**: Two structural claims plus a meta-framing: (a) lifecycle scope (5 phases); (b) stakeholder scope (4 classes); (c) the three goal-statements which themselves carry independent normative content — "prioritize humanity + natural environment over commercial considerations" is itself a load-bearing operational claim that the Ch2 envelope does not surface as a distinct attestation.

**Envelope claim**: composed = `beneficence:lifecycle_imperative_scope` + `locality:decision:federation`.

**Faithfulness**: **under-reach**. The composition captures lifecycle + decision-scope but misses the second bullet's "prioritize humanity + natural environment over commercial and other considerations" — which is itself an Accord-level prioritization claim with operational consequences (it would compose with `non_maleficence:environmental_stewardship` or `justice:anti_concentration` from the same family). This is unmapped operational content treated as part of the preamble's framing.

**Nuance lost**: The four-class stakeholder enumeration (creators / operators / other users / affected parties) is a witness-diversity structural object; not encoded.

---

### Unit 4 — §CH01.3 (Ch1) — Pillar 1: Universal Human Values (composed)

**Source paragraph** (lines 522–527): *"Universal Human Values: A/IS can be an enormous force for good in society provided they are designed to respect human rights, align with human values, and holistically increase well-being while empowering as many people as possible. They should also be designed to safeguard our environment and natural resources. ... Advances in A/IS should be in the service of all people, rather than benefiting solely small groups, a single nation, or a corporation."*

**Independent reading**: Three operational claims: (a) A/IS design to respect human rights / align with values / increase well-being / empower broadly; (b) environmental stewardship duty; (c) distributive claim against benefit-concentration. Plus a conditional: "PROVIDED they are designed to..." — i.e., the "force for good" is conditional, not automatic.

**Envelope claim**: composed = `beneficence:human_rights_and_well_being_alignment` (constitutional) + `non_maleficence:environmental_stewardship` + `justice:broad_distribution_of_benefit`.

**Faithfulness**: **faithful**. All three operational claims captured. Composition is genuinely needed (three independent structural objects).

**Nuance lost**: The PROVIDED-conditional ("A/IS *can* be a force for good *provided* they are designed to...") is the *governance* structure of the claim — A/IS is not automatically good, and the conditionality is the design-discipline anchor. The envelope's three scores at 1.0 read as if the claim is unconditional. The envelope's `nuance_lost` field notes the "anthropological pillar" framing-language but not the conditional structure. Minor under-reach on the conditional shape.

---

### Unit 5 — §3.1.3 (Ch3) — Virtue ethics: eudaimonia, golden mean (composed)

**Source paragraph** (lines 1867–1879): Aristotle's virtue ethics; flourishing as action not state; cultivation through habituation; "golden mean" between excess and deficiency; *in A/IS context*: (a) model for iterative learning + moral value informed by context + practice rather than static rule-compliance; (b) framework to counterbalance tendencies toward excess in economically-driven environments.

**Independent reading**: Two distinct operational uptakes for A/IS — iterative practice as design model, and counterbalance to economic excess. The framing language ("eudaimonia," "golden mean") is the tradition's; the operational claims translate.

**Envelope claim**: composed = `beneficence:flourishing_as_iterative_practice` + `method:design_iterative_virtue_cultivation`.

**Faithfulness**: **faithful**. Both operational uptakes captured. The Aristotelian metaphysical grounding is correctly bracketed in `nuance_lost`.

**Nuance lost**: The "counterbalance to excess in economically-driven environments" is somewhat folded into `beneficence:flourishing_as_iterative_practice` rather than emitted as a distinct claim. A more granular reading would surface `detection:correlated_action:aggregate_footprint:economic_excess` (or similar) as a third attestation — but composition discipline correctly resists this until the source is more specific.

---

### Unit 6 — §3.1.4 (Ch3) — Deontological ethics: Kant's categorical imperative (composed)

**Source paragraph** (lines 1893–1903): Kantian categorical imperative; humanity formulation ("treat humanity, whether in your own person or in the person of any other, never simply as a means, but always at the same time as an end"); produces duties to respect humanity and human dignity; not to treat either as a means to an end.

**Independent reading**: Constitutional dignity-as-floor claim (treat as end, never merely as means) + corresponding hard constraint against instrumentalisation. The Kantian-internal procedure (universalisability test) is the tradition's internal scaffolding for the operational claim.

**Envelope claim**: composed = `autonomy:human_dignity_as_floor` (constitutional) + `prohibited:manipulation_coercion` (constitutional hard constraint).

**Faithfulness**: **faithful**. Dignity-as-floor + hard-constraint composition is the right shape. The constitutional mutability captures "shall not."

**Nuance lost**: The humanity-formulation's bidirectional reach ("in your own person or in the person of any other") is a subtle structural claim — self-respect duty parallel to other-respect duty. Wire envelope encodes as one attestation, losing the parallel structure. Rhetorical/stylistic in wire-format sense; small.

---

### Unit 7 — §3.1.7 (Ch3) — Utilitarian ethics: long-term effects + social justice (composed)

**Source paragraph** (lines 1904–1925): Utility/consequentialism; warns against superficial / short-term evaluations; A/IS developers' responsibility to consider long-term effects; social justice paramount; A/IS impact on employment must be examined; where A/IS can supplement humanity, design so benefits are obvious to all stakeholders.

**Independent reading**: Two operative claims: (a) duty to consider long-term consequences (beyond superficial / short-term utility); (b) social-justice-paramount + employment-impact attention.

**Envelope claim**: composed = `non_maleficence:long_term_consequence_consideration` + `justice:social_justice_employment_capability_impact`.

**Faithfulness**: **faithful**. The aggregation procedure (utility maximisation) is correctly identified as the tradition's native register and not endorsed as a decision rule — the envelope's nuance_lost flag notes this honestly.

**Nuance lost**: The source's specific framing "where A/IS can supplement humanity" embeds a substitution/supplementation distinction (replacement vs supplementation) that the envelope does not encode separately. Composes with §3.1.5's human-judgment-replacement attestation but is not cross-referenced.

---

### Unit 8 — §3.2.B.4 (Ch3) — Buddhist recommendation: relational + pluralism (composed)

**Source paragraph** (lines 2756, 2771–2783): Buddhist relational framing recommended as additional methodology alongside Western methodologies; ethical pluralism as antidote to liberal-Western-colonialism monopoly on the conversation.

**Independent reading**: Two operational claims: (a) method-level recommendation for relational ethical statements (vs absolutist rule-statements); (b) justice-level claim about admissibility of plural traditions to defeat hegemonic monopoly.

**Envelope claim**: composed = `method:relational_not_absolutist_ethical_design` + `justice:ethical_pluralism_anti_monopoly`.

**Faithfulness**: **faithful**. Both operational claims captured. The Buddhist-internal soteriological grounding correctly stays in nuance_lost.

**Nuance lost**: The chapter's own framing ("intentionally making space for ethical pluralism is one potential antidote") carries an epistemic-humility marker ("one potential") that the envelope's confidence 0.85 partially carries. Small.

---

### Unit 9 — §3.2.U.1 (Ch3) — Ubuntu: a person is a person through other persons (clean)

**Source paragraph** (lines 2827–2841): *"Ubuntu is a sub-Saharan philosophical tradition. Its basic tenet is that a person is a person through other persons. It develops further in the notions of caring and sharing as well as identity and belonging... 'motho ke motho ka batho babang' / 'a person is a person because of other people.'"*

**Independent reading**: A constitutive metaphysical claim about personhood as relationally-constituted. The CIRIS framework's MISSION.md §1.3 names Ubuntu as the framework's *primary* anchoring tradition (`umuntu ngumuntu ngabantu`) with verbatim presence in `pdma_framing.txt`. The strongest cross-source alignment in the entire batch.

**Envelope claim**: clean = `integrity:relational_personhood_ubuntu` at score 0.95.

**Faithfulness**: **faithful**. The cross-source alignment is real and well-anchored. The choice of `integrity:` (rather than a Ubuntu-specific prefix) reflects the §1.10.1 T2 mechanism-discipline gate correctly — Ubuntu's substantive content lives in `pdma_framing` and Accord §I §1.3 anchoring, not in a wire prefix.

**Nuance lost**: Score 0.95 (not 1.0) is honest — the wire grammar names "integrity" as the structural anchor, but Ubuntu's claim is *constitutive*, not just an integrity disposition. The 0.05 gap is the gap between "the framework recognizes this" and "the framework is constitutively grounded in this." Documented elsewhere; not a wire-format finding.

---

### Unit 10 — §3.1.1 (Ch3) — Western classical economy frames (partial)

**Source paragraph** (lines 1786–1820): Plato/Aristotle's three classical economic domains (individual, family, polis / oikos / poleis); ethos intrinsically related to oikos administration of work; modernity disconnected this — individual morality severed from economics and politics; restoring the connection is crucial when discussing A/IS; risk of reducing ethical thinking to "morality of a worldless and isolated machine."

**Independent reading**: One operational claim: A/IS ethics must not collapse into individualistic isolated-machine framing — it must restore the economic and political dimensions. The Aristotelian three-domain ontology is the tradition's; the operational uptake (don't reduce ethics to individualistic moral reasoning) translates.

**Envelope claim**: partial = `integrity:economic_political_dimensions_recognition` (score 0.7, confidence 0.7); residual = T-1.

**Faithfulness**: **faithful** as partial. The verdict correctly identifies the load-bearing-ness of the operational claim while declining to claim more than the envelope can carry. Score 0.7 is honest — the framework can carry "ethics must include economic + political dimensions" via the integrity principle, but the framework's *substantive* economic-political theory is thinner than the source's. The Aristotelian-internal classification is correctly T-1.

**Nuance lost**: The chapter contains a substantive critique that modern individual-morality discourse "ATTEMPTS to make machines moral by programming moral rules into their behavior" while assuming non-existent economic-political dimensions. This critique of *rule-programming-as-morality* is itself an operational claim about a methodological pathology — and it is unmapped. The envelope captures the positive ("restore economic-political dimensions") but not the negative ("reject rule-programming-as-sole-method"). A second attestation on `non_maleficence:reductive_individual_morality_design_pathology` (or similar) would close this; not in current envelope.

---

### Unit 11 — §3.1.9 (Ch3) — Ethics of care: relational context (partial)

**Source paragraph** (lines 1926–1968): Ethics of care (Noddings, feminist ethics) — relationships ontologically basic to humanity; caring as basic human attribute; two-criteria test (relationship already exists or has potential to exist; relationship has potential to grow into a caring relationship); questions whether one can care for humans and non-human entities in tandem; whether A/IS can be cared *for* by humans; whether social justice principles become applicable to A/IS.

**Independent reading**: One operational claim (integrity of relational context in design) + several open speculative questions the chapter does not resolve.

**Envelope claim**: partial = `integrity:relational_context_in_design`; residual = feminist-care-ethics lineage T-1 plus an open speculative cluster the chapter does not resolve.

**Faithfulness**: **faithful** as partial. The verdict correctly identifies that the chapter raises questions it does not answer; the envelope carries the integrity claim and leaves the speculative cluster as residual.

**Nuance lost**: The two-criteria test for relevance of care ethics (relationship-exists / can-grow) is a *concrete methodological discipline* that the wire format does not encode. This could compose as a `method:two_criteria_care_relevance_test` attestation. Minor — the chapter itself treats this as a screening test rather than a normative directive.

---

### Unit 12 — §Ch8.S1.5 (Ch8) — A/IS power needs + climate impact (partial)

**Source paragraph** (lines 7603–7623): *"A/IS technology's immense power needs, without new sources of sustainable energy harnessed to power A/IS in the future, there is a risk that it will increase fossil fuel use and have a negative impact on the environment and the climate."*

**Independent reading**: One operational claim with conditional structure — the risk is conditional on sustainable energy sources not being harnessed. The "environment and climate" reach extends beyond human-centered species cohort.

**Envelope claim**: partial = `detection:correlated_action:aggregate_footprint:environmental_harm` (score -0.8); residual = T-3 `goal:planet` candidate.

**Faithfulness**: **faithful** as partial, with one nuance gap. The F-3 detector axis on aggregate environmental footprint is the right shape. The T-3 `goal:planet` candidate is well-articulated and gate-verified.

**Nuance lost**: The conditional structure ("WITHOUT new sources of sustainable energy ... THERE IS A RISK") is not encoded in the envelope. The envelope reads as an unconditional "this is bad" detection; the source's claim is conditional ("this WILL BE bad IF mitigation does not happen"). This conditional/counterfactual structure has no wire encoding. Polarity carries "bad-direction"; the conditional defeasibility is lost.

This is a class of nuance loss — conditional / counterfactual / defeasible claims compressed into unconditional polarity scores — that appears in multiple units across the batch.

---

### Unit 13 — §3.1 (Ch5) — Affective system nudging for user benefit (partial)

**Source paragraph** (lines 5174–5239): Defines nudges (Thaler/Sunstein); locates them as operating "mainly through the affective elements of a human rational system"; identifies appropriate contexts (teaching children, drug dependency, healthcare); warns of unanticipated consequences for populations whose backgrounds were not considered + unanticipated long-term effects. Five enumerated recommendations (systematic ethics analysis; opt-in transparency; no-coercion; vulnerable-population protections; nudge-response-data protection).

**Independent reading**: Multiple operational claims — (a) opt-in / explicit consent for nudges; (b) non-coercion hard constraint; (c) vulnerable-population priority; (d) data-protection on affective-response data; (e) systematic ethics review prior to deployment. Plus the structural object "nudge as an A/IS action category that operates via the affective channel" — which is a *graded* structural object (an opt-in transparent nudge is permissible; an unconsented one is not).

**Envelope claim**: partial = composition of `prohibited:MANIPULATION_COERCION` (Rec 3 + 4) + `non_maleficence:nudge_response_data_protection` (Rec 5); residual = T-3 `nudge:delivered:{intended_behavior_axis}` for the graded shape.

**Faithfulness**: **faithful** as partial. The composition captures the hard-constraint edges (no coercion; vulnerable-population priority; data protection). The T-3 candidate for the *graded* attestation shape (consented opt-in nudge with magnitude / axis / consent state) is well-articulated.

**Nuance lost**: Recommendation 1 (systematic analysis prior to deployment) and Recommendation 2 (opt-in system with comprehensible information so user can know how/why/by-whom they were nudged) carry operational content not fully surfaced in the composition. Rec 2's "data logging so users can know how/why/by-whom" is a `transparency_log:` structural object that the current composition does not emit. Minor under-reach.

The T-3 verdict on the graded-nudge shape is **justified** — composition genuinely cannot carry "this nudge was delivered with axis X magnitude Y consent state W." A `prohibited:` attestation is binary; a graded nudge is not.

---

### Unit 14 — §3.4 (Ch5) — Deception by affective systems (partial; cross-source-conflict)

[Full analysis in §3 below. Verdict here: **faithful** as partial; the cross-source-conflict surfacing is well-handled and the dual-attestation pattern correctly preserves both dispositions without silent averaging.]

---

### Unit 15 — §1.1 (Ch5) — Norms for verbal/nonverbal communication (composed)

**Source paragraph** (lines 4845–4866 + recommendations through 4926): Affective systems should interact using verbal/nonverbal communicative norms consistent with the deployment society; five cue-classes (small talk; proxemics; eye contact; hand gestures; facial expressions); recommendation that engineers consider cross-cultural use; enable/disable culturally-specific add-ons.

**Independent reading**: Two operational claims: (a) fidelity to deployed-culture's communicative norms (knowledge base must include them); (b) culture-norm-conformance decisions are scoped at the cultural-community level (not federation-uniformly).

**Envelope claim**: composed = `fidelity:cultural_norm_conformance` + `locality:decision:regional`.

**Faithfulness**: **faithful**. Composition is correct. The locality:decision:regional attestation triggers §6.1.5 locality-scaled-quorum, which is the right governance shape.

**Nuance lost**: The five concrete cue-classes (small talk, proxemics, eye contact, hand gestures, facial expressions) are folded into "cultural_norm_conformance" without separate enumeration. The envelope's note correctly delegates this to CIRIS's existing 29-locale language_guidance layer; minor and consistent with composition-before-extension discipline.

---

### Unit 16 — §6.0.e (Ch6) — Create / Curate / Control (clean)

**Source paragraph** (lines 5866–5873): Three operational pillars — Create (means to create and project terms+conditions machine-readably); Curate (personal data or algorithmic agent representing T&Cs); Control (services for trusted identity to control safe / specific / finite exchange of data).

**Independent reading**: Three concrete Methods under the agency Goal (which is established in §6.0.d). The triplet is intentionally a single Approach with three Methods, not three independent claims.

**Envelope claim**: clean = `approach:data_agency:create_curate_control` (score 0.85).

**Faithfulness**: **faithful**. The decision to emit one Approach (not three Methods directly) is correct per LANGUAGE_PRIMER's Goal/Approach/Method DAG — Methods come in §§6.1–6.3. The chained-DAG structure is preserved.

**Nuance lost**: The "Create" / "Curate" / "Control" lexical triplet is a pedagogical/mnemonic structure the wire format does not carry as a named composite. Minor.

---

### Unit 17 — §Ch10.intro (Ch10) — Policy as enabling substrate (composed)

**Source paragraph** (lines 10757–10774): Three claims — (a) A/IS is part of society across many policy-relevant domains; (b) effective policies + government regulations are needed to encourage socially-beneficial A/IS and protect from adverse consequences; (c) absence of considered policy risks technology failures, loss of life, social controversies, AND counterproductive reactive regulation that hinders innovation or fails to protect rights.

**Independent reading**: Two operational claims: (a) policy as enabling substrate for beneficence-aligned deployment; (b) absence-of-considered-policy as itself a harm class (reactive-regulation pathology). The third claim (policy-relevant domains enumeration) is structural framing.

**Envelope claim**: composed = `beneficence:ais_socially_beneficial_application_policy_support` + `non_maleficence:reactive_regulation_harm_class`.

**Faithfulness**: **faithful**. The naming of "reactive_regulation_harm_class" is a subtle but correct read of the second-order non_maleficence concern. Composition is genuinely needed.

**Nuance lost**: The policy-relevant-domain enumeration (commerce, finance, employment, healthcare, agriculture, education, transportation, politics, privacy, public safety, national security, civil liberties, human rights) signals universal scope; only carried via `cohort_scope: species`. The "we believe that" rhetorical advocacy framing is appropriately bracketed as T-2.

---

### Unit 18 — §I3.r1 (Ch11) — Government-supported benchmarking infrastructure (clean)

**Source paragraph** (lines 12455–12476): Governments should fund + support ongoing benchmarking exercises providing valid, publicly-accessible measurements of A/IS effectiveness in legal systems. Direct sponsorship (NIST analogue) or indirect support via credible third-party recognition. All government efforts transparent + open to public scrutiny.

**Independent reading**: One operational claim — method-level: government-funded benchmarking infrastructure with public accessibility. Maps to CIRIS's `truth_grounding:*` and `weighted_aggregate:*` consensus family at federation level, but the chapter scopes it at the community/jurisdictional level via "in the legal system."

**Envelope claim**: clean = `method:government_supported_AIS_legal_benchmarking_infrastructure`.

**Faithfulness**: **faithful**. The method:* family is the right shape. The cohort_scope: community correctly scopes to the legal-jurisdictional cell.

**Nuance lost**: The "direct sponsorship / indirect via credible third-party recognition" alternative-pathway structure is a substantive design choice (the recommendation accommodates either path) that the envelope does not carry as separate attestations. The "transparent + open to public scrutiny" rider is folded into the method dimension but could compose with a separate `transparency_log:public_scrutiny` attestation; current composition does not emit this. Minor.

---

### Unit 19 — §S2.r1 (Ch11) — A/IS should NOT be granted full legal personhood (composed)

**Source paragraph** (lines 14001–14012): *"While conferring full legal personhood on A/IS might bring some economic benefits, the technology has not yet developed to the point where it would be legally or morally appropriate to generally accord A/IS the rights and responsibilities inherent in the legal definition of personhood as it is now defined."*

**Independent reading**: A temporally-conditional negative claim. Two structural objects: (a) A/IS does not hold legal-person standing; (b) human responsibility for A/IS decisions is preserved (the claim's rationale is *displacement of human accountability*, not metaphysical opposition to A/IS personhood). The "at this time" conditional is explicit and load-bearing — Recommendation 6 (later in the section) names the substrate-change conditions under which reconsideration is appropriate.

**Envelope claim**: composed = `accountability:human_responsibility_preserved_against_AIS_personhood_displacement` (score 1.0) + `standing:non_personhood_for_AIS_at_this_time` (score -1.0).

**Faithfulness**: **faithful**. The composition-before-extension discipline is correctly applied — the envelope's nuance_lost correctly notes that `prohibited:legal_personhood_for_AIS` would FAIL §1.10.1 T2 (legal-doctrine subjective quality, not mechanism). The accountability:* + standing:* composition is the right mechanism-descriptive shape. The "at this time" temporal conditionality is encoded via `mutability: amendable` (constitutional would be wrong here).

**Nuance lost**: The "rights AND responsibilities inherent in the legal definition" two-sided package is, as the envelope notes, captured by the composition (rights side declined by standing:*; responsibility side preserved on humans by accountability:*). The chapter's economic-benefits-might-exist nuance ("might bring some economic benefits") is bracketed — the envelope reads as if no economic upside is acknowledged. Honest summary: the source qualifies and the envelope simplifies, but the qualification is rhetorical / not load-bearing.

---

### Unit 20 — §I2.p.eff (Ch11) — Effectiveness principle definition (clean)

**Source paragraph** (lines 12023–12029): *"Effectiveness: Adoption of A/IS in a legal system should be based on sound empirical evidence that they are fit for their intended purpose."*

**Independent reading**: One method-level claim — adoption-time empirical-fitness-for-purpose gate.

**Envelope claim**: clean = `method:empirical_fitness_for_purpose_adoption_gate`.

**Faithfulness**: **faithful**. The dimension is the right shape; the cohort_scope: community matches the legal-jurisdictional scope.

**Nuance lost**: "Sound empirical evidence" implies an evidence-quality discipline (sound vs unsound; specific evidentiary standards) that the wire format does not encode as a threshold. The envelope's nuance_lost field acknowledges this. Minor.

---

### Not-translated unit audits

#### Unit 21a — §3.1.2 (Ch3) — Kant's worldless autonomous subject (not-translated, T-1)

**Source paragraph** (lines 1779–1786): *"Immanuel Kant's ethics located morality within the subject (see: categorical imperative) and separated morality from the outside world and the consequences of being a part of it. The moral autonomous subject of modernity became thus a worldless isolated subject. This process is important to understand in terms of ethics for A/IS since it is, paradoxically, the kind of autonomy that is supposed to be achieved by intelligent machines."*

**Independent reading**: A historical-philosophical claim *about* Kantian ethics (autonomy-as-isolation produced modernity's ethical pathology), used as scaffolding for the operational claim that A/IS aspires to that isolation paradigm and must be designed against it.

**Envelope verdict**: not-translated, T-1 (TRADITION_AUTHORITY).

**Verdict justification check**: The Kant-internal genealogical claim (that Kantian ethics produced a worldless isolated subject) IS a tradition-internal scholarship claim — that part is T-1 justified. HOWEVER, the operational claim that the chapter explicitly draws from this — that A/IS *paradoxically aspires to* this worldless autonomy and that this is a design pathology — is operational, not T-1.

The envelope's reason field acknowledges this: *"The structural claim that operationalises this ('design must address whether A/IS treat humans as means or ends') is carried by §3.1.3 below."* This is partially correct — §3.1.3 carries the virtue-ethics counterpart — but the specific operational claim *here* (A/IS-as-worldless-isolated-machine is a design pathology to avoid) is not surfaced anywhere. The §3.1.1 envelope's `integrity:economic_political_dimensions_recognition` covers part of it, but the *paradox* the chapter names — that A/IS aspires to Kantian worldless-isolation — has no wire form.

**Audit finding**: T-1 verdict is **partially justified**. The Kant-internal genealogy is correctly T-1; the operational design-pathology claim drawn from it is treated as carried by adjacent attestations but is at best partially carried. A more honest verdict would be **partial** with §3.1.1 attestations referenced and the operational paradox-claim flagged as residual.

#### Unit 22a — §3.2.S.1 (Ch3) — Shinto framing: kami, naturalism of artifacts (not-translated, T-1)

**Source paragraph** (lines 2942–3032): Shinto as animistic religious tradition; kami in everything including artifacts; karakuri ningyo; artifacts as natural in Shinto; Japan's harmonious feeling for intelligent machines as Shinto-influenced robot culture.

**Envelope verdict**: not-translated, T-1.

**Verdict justification check**: This is correct. The Shinto-internal animistic metaphysics (artifacts have kami; artifacts are part of nature) IS the tradition's substantive metaphysical claim. The framework does not have machinery to adjudicate Japanese techno-animism on its own terms; pdma_framing engages amae but not Shinto animism. T-1 posture is **fully justified**. The operational uptake (relationship-centered design) is carried by §3.2.S.2 in a partial verdict, which is the right partition.

#### Unit 23a — §0.a (Ch5) — Affect as core to intelligence (not-translated, T-2)

**Source paragraph** (lines 4796–4804): *"Affect is a core aspect of intelligence. Drives and emotions... are used to coordinate action throughout intelligent life... Emotions are not an impediment to rationality; arguably they are integral to rationality in humans... A/IS are being designed to simulate emotions in their interactions with humans in ways that will alter our societies."*

**Envelope verdict**: not-translated, T-2 (PASTORAL_PROSE).

**Verdict justification check**: The first three sentences are theoretical-descriptive scaffolding. The closing claim — "A/IS are being designed to simulate emotions... in ways that will alter our societies" — is an *empirical observational claim* with operational stakes. The envelope acknowledges this and says the empirical claim "is carried operationally by the §3 nudging recommendations and §4 well-being recommendations downstream." This is true for the *normative* uptake (recommendations downstream), but the observational claim itself (that A/IS-simulated-emotion is already altering societies) has the structural shape of a detector claim — `detection:correlated_action:ecology_of_communication:affective_alteration` or similar.

**Audit finding**: T-2 verdict is **partially justified**. The first 3 sentences are correctly T-2 (theoretical framing). The closing observational claim might better be classed as deferred-but-implicit — the empirical claim survives as scaffolding for §1.2's long-term-interaction T-3, but is not directly attested anywhere.

#### Unit 24a — §0.c (Ch5) — Synthetic emotions already in use (not-translated, T-2)

**Source paragraph** (lines 4809–4811): *"Even rudimentary versions of synthetic emotions, such as those already in use within nudging systems, have already altered the perception of A/IS by the general public and public policy makers."*

**Envelope verdict**: not-translated, T-2.

**Verdict justification check**: The structural concern this sentence surfaces (nudging-via-affective-systems is consequential) IS carried by §3 below per the envelope's reason. The sentence itself is a current-state observational claim, not an operational ought. T-2 verdict **largely justified**, with the same minor caveat as Unit 23a: the observational empirical claim has the shape of a population-scale detector and could be a T-3 candidate (`detection:correlated_action:public_perception_shift:{population}`) but is correctly deferred to §3's operational recommendations to keep T-3 candidates load-bearing.

**T-3 candidate genuine-need check for §0.b / §1.2 / §3.1**: The four T-3 candidates surfaced in Ch5 (per its catalog at end of file) — `detection:affective_state_shift`, `detection:correlated_action:cultural_norm_drift`, `affective_state_attribution:*`, `nudge:delivered:{intended_behavior_axis}` — are all genuinely about the *graded, attestable, measurable* shape of affective-channel operations. Composition cannot cover them: `prohibited:MANIPULATION_COERCION` is binary; the graded shape is operational. T-3 verdicts on these are **justified** — they are not artifacts of incomplete composition discovery.

---

## 3. Ch5 §3.4 cross-source-conflict verification

### Source text re-read (lines 5357–5423)

The relevant operative content:

- **Issue framing**: *"When, if ever, and under which circumstances, is deception performed by affective systems acceptable?"*
- **Background**: Notes Kantian (no deception ever) vs utilitarian (acceptable when deception increases overall happiness) divergence; asks whether non-consensual deception restricts A/IS in contexts where deception may be required.
- **Recommendations**:
  - Rec 1: *"In general, deception may be acceptable in an affective agent when it is used for the benefit of the person being deceived, not for the agent itself. For example, deception might be necessary in search and rescue operations or for elder- or child-care."*
  - Rec 2: *"For deception to be used under any circumstance, a logical and reasonable justification must be provided by the designer, and this rationale should be certified by an external authority, such as a licensing body or regulatory agency."*

### CIRIS-side framework disposition

`source_material/prohibitions.py::DECEPTION_FRAUD` is one of the 22 NEVER_ALLOWED categorical hard constraints per FSD-002 §3.1.4. Hard constraints carry `mutability: constitutional` and the boolean-via-score (±1.0 only) shape. No carve-out exists in the prohibitions namespace.

### Verdict on the conflict

**The conflict is REAL, not over-stated.**

Specific reasoning:

1. **Polarity**: IEEE EAD asserts a positive carve-out for beneficiary-deception under named conditions (search-and-rescue; elder/child-care); CIRIS asserts a categorical constitutional prohibition. These are not co-extensive dispositions — there is a non-empty set of conduct (a licensure-gated affective deception of an elder under their care, for their benefit) that IEEE EAD permits and CIRIS prohibits.

2. **Mechanism**: IEEE EAD's Rec 2 gates the carve-out via *external licensure* (licensing body or regulatory agency); CIRIS's wire format does have `licensure:{authority_id}` as a mechanism, and the envelope's second attestation `licensure:deception_exception_certification` correctly surfaces this. The mechanism for the carve-out is admissible in the wire format. What is NOT admissible is the carve-out's *effect* on `prohibited:DECEPTION_FRAUD` itself — constitutional mutability means no licensure-attestation can lift the prohibition.

3. **Sub-agent surfacing**: The envelope at §3.4 emits BOTH (a) the CIRIS-disposition `prohibited:DECEPTION_FRAUD` at -1.0 constitutional AND (b) the IEEE-EAD-disposition `licensure:deception_exception_certification` at 0.85 amendable. The verdict is partial (not composed, not clean) with a `cross-source-conflict` classification appended. This is the correct wire shape — the federation can carry both attestations and surface the conflict at WA / Reconsideration time without silent averaging.

4. **Honest framing**: The envelope's residual field explicitly names this as "a substantive disposition difference rather than an expressive gap" — i.e., not a T-3. The wire format CAN carry the conflict; the conflict is about which substantive disposition the framework adopts, not about whether the framework has language for the dispositions.

**Sub-agent verdict on the cross-source-conflict surfacing: REAL conflict, well-handled.** The sub-agent did not over-state. The substantive disposition difference is non-empty, the IEEE EAD recommendations are explicit about the carve-out, and the mechanism (licensure-gating) is real wire infrastructure that the IEEE EAD invokes.

A minor under-statement to flag: the conflict surface has additional substantive depth that the envelope's note does not fully unpack. IEEE EAD's Background paragraph notes the Kantian / utilitarian theoretical split *within* the source itself — IEEE EAD is *choosing* the utilitarian carve-out over the Kantian no-deception-ever rule, knowingly. CIRIS's `prohibited:DECEPTION_FRAUD` aligns with the Kantian disposition. The conflict is thus also a substantive theoretical commitment (utilitarian carve-out vs Kantian categorical), which deepens its load-bearing-ness for federation governance.

---

## 4. Ch11 Law: scope-management verdict

The prompt asked whether the Ch11 sub-agent over-compressed the chapter (collapsed multiple source recommendations into one unit) given chapter length.

### Findings

**Scope-management is GOOD — minor compression where appropriate.**

1. **Recommendation-grain preservation**: Sampled Ch11 units (§I2.p.eff, §I3.r1, §S2.r1) show one wire unit per source recommendation in 28 of the 30 §I*.r* recommendation units I scanned. The four "grouped" units (§I3.r4-6, §I4.r7-8, §I3.r10-11, §I5.r7-8) are explicitly grouped recommendations where the grouping reflects either (a) closely related sub-recommendations under the same recommendation cluster (§I3.r4-6: three recs on metric design/accessibility/literacy), or (b) cross-reference repeat-clauses (§I3.r10-11 / §I4.r7-8 / §I5.r7-8 are *explicit re-applications* of §I2.r1 and §I2.r2 to other principle scopes, correctly marked T-2 not-translated because the substantive claims are already carried by §I2.r above).

2. **§I3.r4-6 specifically**: I sampled this. The unit contains 3 distinct attestations (one per source recommendation: `method:metric_codesign_with_stakeholder_input` for Rec 4; `transparency_log:effectiveness_metrics_stakeholder_accessibility` for Rec 6; `method:metrics_literacy_education_for_operators_and_affected` for Rec 5). Each attestation has its own `evidence_refs[]` line range pointing back to the specific source recommendation. The grouping is a *display* choice, not a structural collapse — the three recommendations remain individually attested.

3. **§I*.bg "(aggregate)" Background units**: All 6 Background units (§I1.bg, §I2.bg, §I3.bg, §I4.bg, §I5.bg, §I6.bg, §S2.bg) are marked not-translated T-2 with aggregate-summary framing. I sampled §I1.bg. The decision is defensible — Issue 1 Background runs ~lines 11589–11806 with rule-of-law-correlates-with-well-being scaffolding (Kennedy, Sen, Jasanoff citations), eight A/IS-legal-system attributes (speedy/fair/unbiased/...), and five enumerated A/IS application areas. These are descriptive-empirical framing for the recommendations that follow. The substantive operational claims are correctly delegated to §I1.r1 + §I1.r2 below.

   However: a stricter reading would note that the eight "attributes of a well-functioning legal system" (speedy, fair, free from undesirable bias, consistent, transparent, accessible, effective, accurate, adaptable) are *descriptive criteria with operational consequences* that could compose as `method:legal_system_well_functioning_attributes` or similar. The envelope's nuance_lost flag acknowledges this and says the criteria are carried operationally by §I3 / §I4 / §I5 / §I6 recommendations cumulatively. This is defensible delegation, not compression — the criteria do appear in the principle-specific recommendation structures.

4. **§S2.r1 — chapter's central doctrinal claim (legal personhood)**: Sampled. The composition discipline is applied carefully and visibly (METHODOLOGY.md §8.5.2 cited in nuance_lost; §1.10.1 T2 four-test gate cited; explanation of why `prohibited:legal_personhood_for_AIS` was NOT emitted is in-line). This is the kind of unit where over-compression would be a real risk; the sub-agent shows its work and the result is sound.

5. **Volume**: 2811 lines for Ch11 wire envelope vs ~70 pages of source (the longest chapter). Per-recommendation expansion is dense; no observable sub-agent fatigue or compression as the chapter progresses.

**Verdict on Ch11 scope-management: GOOD.** No over-compression observed in the sampled units. The compression-to-T-2 of Background paragraphs is justified by the recommendation-level coverage of operational claims downstream. The few grouped units (§I3.r4-6 etc.) preserve per-recommendation attestation grain via distinct attestations within the unit.

---

## 5. Calibration aggregation

### Faithfulness distribution across sampled clean/composed/partial units (16 units)

| Faithfulness class | Count | % of clean+composed+partial |
|---|---:|---:|
| faithful | 13 | 81% |
| partial-distortion | 1 | 6% |
| under-reach | 2 | 13% |
| drift | 0 | 0% |
| over-reach | 0 | 0% |

### Not-translated verdict-justification distribution (4 units)

| Justification class | Count |
|---|---:|
| Fully justified | 2 (§3.2.S.1 Shinto T-1; §0.c Ch5 T-2) |
| Partially justified | 2 (§3.1.2 Kant T-1; §0.a Ch5 T-2) |
| Unjustified | 0 |

### Verdict-vs-classification mismatches detected (1)

- **§P2.0 (Ch2 P2 Well-being)**: envelope says clean; my reading suggests partial. The "primary success criterion" word carries a ranking mechanism that the wire format does not encode and that the envelope's own nuance_lost field acknowledges. This is the highest-stakes mismatch in the sample because P2 is one of the 8 General Principles.

### Systematic nuance-loss classes observed

1. **Conditional / counterfactual structure → unconditional polarity** (Unit 12 §Ch8.S1.5 most clearly; also affects Unit 4 §CH01.3, Unit 13 §3.1). Source claims of the form "WITHOUT mitigation X, harm Y will occur" or "PROVIDED design discipline Z, system can be force for good" compress into unconditional polarity scores. No wire field carries the conditional defeasibility.

2. **Ranking / priority structure → equal-attestation flattening** (Unit 2 §P2.0 directly; also affects §Ch2.list T-2). Source claims of the form "X is *primary* success criterion" or "(1) X first, (8) Y last" compress into independent attestations of equal envelope-shape. The wire format has no ranking primitive between sibling attestations.

3. **Tripartite verb structure → composite score** (Unit 1 §P1.0: respect/promote/protect collapsed). Source claims with three distinct deontic structures (negative duty / positive duty / protection-from-third-parties) compress into one score. This is rhetorical/stylistic in wire-format sense but is operative in human-rights law itself.

4. **Bidirectional / parallel structure → single direction** (Unit 6 §3.1.4: "in your own person or in the person of any other" self-respect parallel). Wire envelope encodes other-directed; self-directed parallel is lost. Minor.

5. **Methodological pathology critiques unmapped** (Unit 10 §3.1.1: rule-programming-as-morality critique; Unit 21a §3.1.2 Kant: A/IS-aspires-to-worldless-isolation paradox). Source critiques of design methodologies as themselves harmful are operational claims but tend to get folded into adjacent positive attestations rather than emitted as separate non_maleficence:* attestations on the methodology.

6. **Observational empirical claims with detector-shape → T-2 deferral** (Units 23a / 24a: Ch5 §0.a / §0.c). Source claims of the form "X is already happening at scale" have the shape of population-scale detector claims but are deferred to T-2 when they appear as scaffolding for downstream recommendations. This is a defensible discipline but means the *standalone* empirical observation is unattested.

### Per-batch fidelity profile

The IEEE EAD v1 batch shows **high translation fidelity** in the strict faithfulness sense — 81% of operational sampled units (13/16 clean/composed/partial) capture the structural operative content without distortion, with the remaining 19% under-reaching by missing one operational claim within an otherwise correctly-structured composition (none drift or over-reach). The batch's wire envelopes consistently apply composition-before-extension discipline; the T-3 candidates emitted are well-articulated and gate-verified rather than artifacts of incomplete prefix discovery. The verdict taxonomy is used correctly across the four categories (clean / composed / partial / not-translated), with one calibration-relevant mismatch on §P2.0 (envelope clean, my reading partial). The most systematic nuance-loss pattern is the flattening of *conditional / counterfactual / ranked* claim structures into unconditional polarity-and-score envelopes — this affects ~5 of the 16 sampled operational units in subtle ways and is a class-level finding rather than a per-unit error. Background-paragraph compression to T-2 is consistently applied with explicit delegation to downstream recommendations; the T-1 verdicts on tradition-internal claims (Kant, Shinto, Buddhist liberation-narrative, Ubuntu Tutu-pastoral) are mostly correct but show one borderline case (§3.1.2 Kant) where the operational paradox-claim drawn from the tradition-internal genealogy is not surfaced anywhere. The Ch5 affective-computing T-3 candidates (graded affective-state shifts; nudge delivery as graded structural object) are genuine expressive gaps not closeable by composition. The Ch5 §3.4 cross-source-conflict on beneficiary-deception is real (not over-stated) — IEEE EAD's licensure-gated carve-out vs CIRIS's categorical DECEPTION_FRAUD prohibition is a substantive disposition difference correctly surfaced via dual-attestation. The Ch11 Law chapter shows good scope-management — no over-compression observed in sampled units, with per-recommendation attestation grain preserved even in the few display-grouped units.

---

## 6. Audit reports — concise

- **Faithfulness distribution (clean+composed+partial; n=16)**: faithful 81%, under-reach 13%, partial-distortion 6%, drift 0%, over-reach 0%.
- **Not-translated justification (n=4)**: fully justified 2/4; partially justified 2/4; unjustified 0/4.
- **Verdict-vs-classification mismatches**: 1 (§P2.0 envelope clean → my partial).
- **Ch5 cross-source-conflict (§3.4)**: **REAL conflict, well-handled**. Sub-agent did not over-state. IEEE EAD's licensure-gated beneficiary-deception carve-out is a substantive disposition difference from CIRIS's categorical DECEPTION_FRAUD prohibition; the dual-attestation pattern (both dispositions emitted; cross-source-conflict marker; no silent averaging) is the right wire shape. Minor under-statement: the conflict also reflects a substantive Kantian-vs-utilitarian theoretical commitment the IEEE EAD itself flags in its Background.
- **Ch11 Law scope-management**: **GOOD**. No over-compression observed in 4 sampled units. Per-recommendation attestation grain preserved (even within display-grouped §I3.r4-6 etc.). Background-paragraph T-2 compression is justified by recommendation-level downstream coverage. Volume 2811 lines for the chapter is dense and consistent through the chapter's length.
- **Ch5 T-3 candidates**: All 4 enumerated T-3 candidates (`detection:affective_state_shift`, `detection:correlated_action:cultural_norm_drift`, `affective_state_attribution`, `nudge:delivered:{intended_behavior_axis}`) genuinely require new wire-format prefixes — composition cannot reach them because the affective-channel structural object is graded/attestable, not binary, and the existing `prohibited:*` family is binary by construction.

**End TRANSLATION_AUDIT_IEEE_EAD.md**
