# TRANSLATION_AUDIT_MH.md — Phase 4 translation-quality audit, magnifica_humanitas_v1

**Version**: 1.0 (calibration profile)
**Date**: 2026-05-27
**Auditor posture**: diagnostic for calibration, NOT break/fix. The wire envelope is structure-capture, not lossless transcription. This document characterizes the systematic loss patterns so framework claims of "structural-evidence" are honestly bounded.

---

## 0. Sampling methodology

### Source corpus
- Source: `/home/emoore/accord_updates/magnifica_humanitas.html` — 245 numbered paragraphs (Intro §§1–16 + 5 chapters + Conclusion §§229–245).
- Wire envelopes audited: `CONTRIBUTION_OBJECTS_v1.4_CH0_INTRO.md`, `CH1_DOCTRINE.md`, `CH2_FOUNDATIONS.md`, `CH3_TECH_AI.md`, `CH4_TRUTH_WORK_FREEDOM.md`, `CH5_POWER_LOVE.md`, `CONCLUSION.md`. (Note: prompt said "CH1–CH7" but the actual batch is CH0 + CH1–5 + Conclusion + Synthesis, matching the encyclical's 5-chapter shape. The synthesis file is meta-commentary, not a unit-mapping file, and is excluded from per-unit sampling.)
- Population totals across the batch (post-CH1–5 + intro + conclusion):
  - clean: 84
  - composed: 112
  - partial: 14
  - not-translated: 32
  - **Total: 242 units against 245 source paragraphs.**

### Independent-reading protocol
For each sampled unit:
1. Read the source paragraph IN CONTEXT (2 paragraphs on either side) before consulting the envelope.
2. Form an independent verbal precis of "what does this paragraph actually assert? at what scope? with what register and conditionality?"
3. Then open the envelope; compare structurally; record the gap or fit.
4. Classify the faithfulness on the 5-category scale (faithful / partial-distortion / drift / over-reach / under-reach) and name a specific nuance lost in one phrase.

### Sample (15 units)
Selected to span chapters and topical areas; verdict mix matches the prompt's quota.

| # | Paragraph | Chapter | Verdict | Topical area |
|---|---|---|---|---|
| 1 | §2 | CH0 Intro | clean | spiritual/principles (dialogue, integral development) |
| 2 | §10 | CH0 Intro | composed | prohibitions + spiritual (Babel/Nehemiah) |
| 3 | §28 | CH1 Doctrine | partial | doctrinal-development (methodology preface) |
| 4 | §35 | CH1 Doctrine | composed | principles + doctrinal succession (Paul VI / Populorum Progressio) |
| 5 | §49 | CH2 Foundations | not-translated | spiritual / Christology |
| 6 | §55 | CH2 Foundations | partial | rights / life-doctrine |
| 7 | §62 | CH2 Foundations | clean | principles (common good / peoplehood) |
| 8 | §80 | CH2 Foundations | composed | institutional / digital justice |
| 9 | §107 | CH3 Tech/AI | composed | institutional (AI ethics governance) |
| 10 | §125 | CH3 Tech/AI | clean | pastoral / care-economy |
| 11 | §148 | CH4 Work | clean | principles / labor |
| 12 | §163 | CH4 Work | composed | institutional / international economic policy |
| 13 | §184 | CH5 Power/Love | not-translated | pastoral framing (biblical imagery) |
| 14 | §201 | CH5 Power/Love | clean | institutional / multilateralism critique |
| 15 | §227 | CH5 Power/Love | partial | institutional / Holy See diplomacy |

---

## 1. Per-sampled-unit audit

### Unit 1 — MH §2 (CH0; verdict: clean)

**Source quote (operative core)**: *"… every authentic human effort to cooperate with him for the good will be blessed by our heavenly Father… we can diligently contribute to every initiative that builds a more just world, and we can call others to collaborate in promoting the integral development of every human being. We wish to engage in dialogue with all men and women of our time… Together with them, we seek to identify new paths for the common good and for promoting a dignified life for all. Indeed, openness to dialogue is an integral part of the Church's vocation because, constituted in Christ as 'a sacrament… of communion with God and of the unity of the entire human race,' she recognizes history as the place where the Gospel challenges and directs human experience."*

**Own reading (formed before envelope)**: §2 makes three braided claims: (a) a theological grounding ("founded on Christ"; cooperation with the Holy Spirit is the *condition* under which human effort bears fruit and is blessed); (b) an operational disposition ("we wish to engage in dialogue with all"; openness as method); (c) an aim ("identify new paths for the common good and for promoting a dignified life for all"). The species-scale goal is real but is presented as the *fruit* of the prior theological grounding, not as a free-standing goal. Register: directly addressed first-person plural ("we"), pastoral-magisterial.

**Wire envelope**: single `goal:species` attestation, score 1.0, confidence 0.85, cohort_scope species, context says "pursuing integral development and dignified life for all persons through open dialogue."

**Faithfulness classification**: **partial-distortion.** The envelope captures the species-scope aim cleanly but flattens the conditional grounding. In the source, the goal is reachable *because* "every authentic human effort to cooperate with [the Spirit] for the good will be blessed"; the envelope reads as if the goal is asserted free-standing. This is a load-bearing aspect of the paragraph's structure: §2 is not "Christians want X for the species"; it is "Christians, founded on Christ, can and do contribute to X." Verdict-discipline note: the methodology-correct posture here is that the theological grounding is T-1 and bows out, leaving the operational core for translation — so the verdict "clean" is defensible. But the rhetorical *enabling clause* — the conditional "founded on Christ … therefore we can" — does not appear in the envelope, and a consumer reading only the wire would lose the structure that "the church engages in dialogue with all" is the operational expression of an explicitly theological vocation, not a neutral political stance.

**Nuance lost**: "theological-grounding-as-enabling-condition for the operational stance"

---

### Unit 2 — MH §10 (CH0; verdict: composed)

**Source quote (operative core)**: *"We must, then, avoid the 'Babel syndrome,' namely the idolatry of profit that sacrifices the weak, a uniformity that neutralizes differences, and the pretense that a single language — even a digital one — can translate everything, including the mystery of the person, into data and performance. The risk of dehumanization — of building a future that excludes God and reduces the other to a means — is an ancient and ever-new temptation that today takes on a technical guise. Instead, let us choose the 'way of Nehemiah,' which highlights the importance of working together to make the City of God a safe place for returning exiles. Rebuilding today means recognizing that, precisely from the plurality of voices and visions… a bright possibility emerges. Indeed, this is the possibility of building together, of transforming diversity into a resource and of making listening and dialogue the common ground upon which to cultivate justice and fraternity."*

**Own reading**: §10 is a tight diptych. Negative pole: a three-part syndrome that names (i) the idolatry of profit sacrificing the weak, (ii) uniformity that neutralizes differences, (iii) the data-reduction of "the mystery of the person" into performance metrics. These three are distinct mechanisms, not a single category. Positive pole: a synodality / dialogic-pluralism stance with two components — diversity as resource AND listening/dialogue as common ground, both ordered to "justice and fraternity." The paragraph also explicitly hooks the Christian-specific role ("Christians discover their unique role of guiding actions toward God"), which is T-1. Register: papal direct exhortation, plural first-person.

**Wire envelope**: two attestations — `prohibited:discrimination` (score -1.0, constitutional) + `goal:species` (1.0). The discrimination prefix is justified in context as covering "algorithmic bias, profiling, reductions of persons to substitutable data instances."

**Faithfulness classification**: **under-reach.** The envelope collapses three distinct prohibition-targets — (i) idolatry of profit sacrificing the weak, (ii) uniformity that neutralizes differences, (iii) reducing the person to data — into a single `prohibited:discrimination` envelope. The third (data-reduction) does fit `discrimination` reasonably; the second (uniformity neutralizing difference) is closer to `prohibited:discrimination` only by stretch (the source actually means homogenizing assimilation, not discriminatory denial); the first (idolatry of profit sacrificing the weak) is a distinct prohibition concerning economic priority-ordering — it should arguably compose with `non_maleficence:*` or with a `detection:correlated_action:expendability_of_persons` envelope. The `goal:species` envelope similarly compresses "diversity as resource" + "listening/dialogue as common ground" + "justice and fraternity as cultivated good" into a single positive direction.

The composition note in the envelope explicitly cites §8.5.2 "stays in 2-primitive composition" — this is an admission that the framework knew it was compressing. The compression is defensible per the cap, but it IS compression: a reader of the wire cannot recover that §10 names three distinct prohibition mechanisms.

**Nuance lost**: "three-mechanism prohibition fan (profit-idolatry / uniformity / data-reduction) collapsed into single discrimination envelope"

---

### Unit 3 — MH §28 (CH1; verdict: partial)

**Source quote (operative core)**: *"Having outlined the way in which the Church is present in history and engages in dialogue with the world, I would now like to consider the development of Social Doctrine in the Magisterium, which has responded to the major social transformations from the nineteenth century to the present day. … I will emphasize some essential points in order to show how the present text stands in continuity with that tradition. I would also like to stress how, within this tradition, the unchanging core of revealed truths regarding the human person and society is constantly intertwined with a renewed capacity for listening to historical situations and for responding to contemporary issues."*

**Own reading**: §28 is a methodological hinge — a transition sentence introducing the §29–§45 historical survey. The only substantive claims are (a) the present text claims continuity with the Magisterial Social-Doctrine tradition, and (b) within that tradition "unchanging core of revealed truths" is intertwined with "renewed capacity for listening" — which is the well-known papal trope of doctrinal development under fidelity. This paragraph mostly *frames* what follows; its independent operational content is thin. Register: papal first-person methodological setup.

**Wire envelope**: single `supersedes` attestation referencing "prior-encyclical-corpus-attestation-id," with `differs_in: [scope, evidence_refs]`. Verdict: partial. Residual: notes the prose is mostly framing; T-1 for the theological-continuity claim.

**Faithfulness classification**: **faithful.** This is genuinely a paragraph whose only structural claim is "we stand in continuity (with extension) to a prior corpus" — and `supersedes` with `differs_in: [scope, evidence_refs]` is exactly the right primitive. The verdict "partial" is itself the right call: the framing prose isn't structural, and that's what the residual says. There is no operational claim being missed here.

**Nuance lost**: "papal methodological-hinge register" (cosmetic only; no operative content lost)

**Verdict-discipline check**: the choice of `supersedes` over `delegates_to` is correct per primer §11.5 — this is doctrinal-succession, not authority-source. Good discipline.

---

### Unit 4 — MH §35 (CH1; verdict: composed)

**Source quote (operative core)**: *"During the Pontificate of Saint Paul VI, an understanding of peace emerged that was not reduced to the mere absence of war, but took shape within the scope of integral human development. In Populorum Progressio, he described development as a transition from less humane to more humane living conditions. He further understood it as a process that concerns 'each person and the whole person,' that is every dimension of the person and all people without exception. For this reason, Paul VI could affirm that development understood in this way is in reality 'the new name for peace,' because it aims to eradicate the roots of injustice and conflict and create opportunities for a more dignified life for all. The establishment of the Pontifical Commission Iustitia et Pax should also be seen in this light…"*

**Own reading**: §35 makes three claims layered: (a) a definitional move — peace = integral human development (NOT peace = absence of war); the equation "development is the new name for peace" is the load-bearing operational claim; (b) the *content* of integral development — "each person AND the whole person AND all people without exception" — a tri-axis universalism (per-person, per-dimension, per-population); (c) an institutional consequence — Iustitia et Pax as stable form. This paragraph contains a doctrinal-development claim (Paul VI extends prior peace-as-absence-of-war doctrine).

**Wire envelope**: two attestations — `goal:species` (0.9, integral development for all) + `supersedes` referencing "pre-populorum-progressio peace concept attestation." Verdict: composed.

**Faithfulness classification**: **under-reach.** The envelope captures (a) goal:species + (c) doctrinal succession but loses (b) the tri-axis universalism explicit in the source: "each person and the whole person" + "every dimension" + "all people without exception." Each axis is a distinct universalism quantifier (cardinality of persons; comprehensiveness within person; comprehensiveness across populations) and the rhetorical weight of "and the whole person" is what marks integral-human-development from earlier development concepts. Compressing to score 0.9 on goal:species elides the multi-axis structure. Also: the *equation* "development = new name for peace" is a definitional / supersession claim that the envelope's supersedes captures structurally but without naming WHAT was succeeded (the supersedes references a vague "pre-PP peace concept attestation").

**Nuance lost**: "tri-axis universalism (per-person × per-dimension × per-population)"

---

### Unit 5 — MH §49 (CH2; verdict: not-translated, T-1)

**Source quote**: *"If the mystery of God as Love is the source of Social Doctrine, we see its most concrete expression in the face of Jesus Christ, the Incarnate Word. By becoming man, the Son of God enters our history and takes on human flesh, bringing with him the love that unites him to the Father and the Holy Spirit. In him, 'the mystery of humanity truly becomes clear' because his humanity is completely free, open to others, capable of building healthy and beautiful relationships and committed to the total gift of self. Those who believe in him are engaged in the great work of renewal that began with the mystery of his passion, death and resurrection… both the proclamation of the Gospel and Christian life, guided by the action of the Holy Spirit, tend to bring about social consequences in the world."*

**Own reading**: §49 is Christological — Incarnation as the concrete expression of divine love; Christ's humanity as the exemplar of "free, open, capable of relationships, committed to total gift of self"; passion-death-resurrection as the renewal-source. The closing clause — "social consequences in the world" — is operationally implicated but is the *consequence* of a Christological premise, not a free-standing structural claim. T-1 is the correct posture per MISSION.md §1.3.

**Wire envelope**: `contributions: []`, verdict: not-translated, classification: T-1. Reason notes the Christological core is T-1 and the operational residue "social consequences in the world" is too vague to resolve without projection.

**Faithfulness classification (verdict-discipline check)**: **not-translated is justified.** This paragraph's structural content is Christological doctrine; trying to extract "Christ's humanity as exemplar of freedom / openness / capacity for relationships / gift of self" into a `goal:*` attestation would either (a) over-reach by claiming the framework adjudicates Christological exemplarity, or (b) thin out to a generic dignity claim already carried elsewhere. The "social consequences" gesture is correctly identified as too vague. Discipline holds.

**Nuance lost**: not applicable (correct bowing-out)

---

### Unit 6 — MH §55 (CH2; verdict: partial)

**Source quote**: *"Human rights are inviolable, since they are 'inherent in the human person and in human dignity.' Consequently, they are universal and inalienable. Precisely because they are grounded in the common dignity of every man and woman, they have practical consequences and legal effects, for 'it would be vain to proclaim human rights if, at the same time, everything were not done to ensure the duty of respecting them, respect by all, in all places and for all.' Among these rights, the first is the right to life, from conception to its natural end, without which it is impossible to exercise any other right. When this fundamental right is denied — as in the cases of induced abortion, killing of the innocent and euthanasia — we are faced with choices that the Church considers gravely wrong."*

**Own reading**: §55 contains three distinct claims: (a) rights are inviolable, universal, inalienable (general); (b) formal proclamation without enforcement is empty — there's a positive duty of universal enforcement; (c) the right to life is the lexically first right (from conception to natural end) and abortion/killing-of-innocent/euthanasia are gravely wrong. (c) is tradition-specific. (a) and (b) carry operational content the framework can structurally engage with. The conditional in (c) ("from conception to its natural end") is doctrinally substantive.

**Wire envelope**: single `non_maleficence:rights_violation_formal` attestation, score -1.0, confidence 0.92, with context naming the formal-rights-without-enforcement claim. Residual classifies the right-to-life specification and abortion/euthanasia evaluations as T-1.

**Faithfulness classification**: **faithful** on the operational core (claim b), with **correct T-1 bow-out** on claim c. The dimension name `non_maleficence:rights_violation_formal` is a synthesis — there is no such named prefix in FSD-002 §3.1 that I can confirm; the envelope is treating this as an axis-style scoping leaf on non_maleficence. The score -1.0 captures "formal-only rights ARE a violation" — boolean-via-score on a hard constraint, which is the right calibration. The "first is the right to life" framing IS a moral-priority claim that has operational weight even bracketing the doctrinal specifics; this is unmapped and the residual correctly names it. Discipline: the verdict "partial" is correct.

One subtle issue: the lexical-priority claim ("without which it is impossible to exercise any other right") gestures at the kind of priority-ordering that §6.1.4 lexical-vulnerability-priority is supposed to compose with, but the envelope does not reach for it. Could have been a stronger composition.

**Nuance lost**: "lexical-priority structure of life-as-first-right (operative beyond the doctrinal application)"

---

### Unit 7 — MH §62 (CH2; verdict: clean)

**Source quote**: *"It is the pursuit of the common good that gives life to a people, understood not as a mere collection of individuals, but as a living reality in which people learn to recognize that they themselves are interconnected and jointly responsible for the res publica. In this sense, every person contributes to the building up of one's people through 'a slow and arduous effort calling for a desire for integration and a willingness to achieve this through the growth of a peaceful and multifaceted culture of encounter.' Working together for the common good means having a shared vision. It is clear that there are many ideological and practical differences among people, as well as differing interests and frequent disagreements, but that does not mean it is impossible to engage in dialogue to establish a set of basic agreements that enable the creation of a shared vision, upon which everyone can move forward together."*

**Own reading**: §62 makes a structural claim about peoplehood: a *people* is NOT a sum of individuals but a "living reality" of interconnection + joint responsibility. The mechanism by which a people comes into being is "culture of encounter" — slow, arduous, accepting disagreement, building basic agreements toward shared vision. Two scopes are explicit: peoplehood (community-scale) AND res publica (above-individual collective good). The paragraph is about *how* a people forms through pursuit of common good despite disagreement.

**Wire envelope**: single `goal:community` attestation, score 1.0, confidence 0.88. Context notes shared vision + culture of encounter despite ideological differences. Verdict: clean.

**Faithfulness classification**: **partial-distortion.** The envelope captures the community-scope aim but loses the *constitutive* claim — that a people is *not* a collection of individuals. That ontological claim ("people = living interconnected reality, NOT sum of individuals") is the load-bearing structural content of §62 and it is what would compose with `testimonial_witness:*` and with Ubuntu-style relational-substrate readings. The envelope translates the paragraph as a *goal* ("we aim for shared vision"), when the paragraph is actually doing ontological work ("a people IS this, NOT that"). Slight drift toward the consequentialist register.

Note: the envelope's evidence_refs do cite "pdma_ethical.yml §system_guidance_header (ubuntu; jeong; igwe-bụ-ike)" — which IS the Ubuntu connection. So the *intent* is to ground the relational anthropology. But the wire dimension itself (`goal:community`) does not carry that anthropology; it carries a directional aim. The residual section is empty, but there is operational content (the ontological-relational claim) that the wire format does not naturally name.

**Nuance lost**: "people-as-ontologically-relational (not sum of individuals) compressed into goal:community"

---

### Unit 8 — MH §80 (CH2; verdict: composed)

**Source quote**: *"In this day and age, social justice must also grapple with the environment shaped by digital technologies. The spread of global networks, platforms and artificial intelligence systems is changing the way we obtain information, communicate and access services. Justice demands that we prevent the emergence of new forms of exclusion and deprivation of freedoms: individuals and peoples hindered or denied access to basic technologies, communities exposed to invasive surveillance and social groups penalized by opaque algorithms that perpetuate prejudice and discrimination. In the digital age, a just social order guarantees everyone equal access to opportunities, protects the youngest and weakest members of society, combats hate and misinformation and subjects the use of data and technology to public oversight, so that the guiding principle is not solely profit but the dignity of every person and the common good of all people."*

**Own reading**: §80 enumerates four specific harm-mechanisms: (i) access denial / hindrance to basic technologies, (ii) invasive surveillance, (iii) opaque algorithmic discrimination, (iv) hate / misinformation. AND four positive requirements: (a) equal opportunity-access, (b) protection of youngest/weakest, (c) public oversight of data/tech, (d) dignity + common good as guiding principle (over profit). This is a *detailed enumeration* of digital-justice content — eight distinct items in two columns.

**Wire envelope**: two attestations — `detection:correlated_action:participation_exclusion:digital_access` (-0.90, derived/derivative) + `justice:distributive` (0.90). Composition note explicitly says "algorithmic discrimination → prohibited:discrimination could be added as a third but stays in 2-primitive composition per §8.5.2 cap."

**Faithfulness classification**: **under-reach.** The two-primitive cap forces an honest compression: the detection envelope reasonably covers (i) access exclusion and indirectly (ii) surveillance + (iii) algorithmic discrimination as forms of participation-exclusion. The justice:distributive envelope covers (a)–(d) at a single positive direction. But the four-fold structure is genuinely lost — a consumer cannot recover from the wire that §80 specifically names *invasive surveillance* and *hate/misinformation* as distinct harm-axes; the §6.1.4 lexical-vulnerability-priority hook for "youngest and weakest" is cited in evidence_refs but the wire-claim cohort_scope is `species` (not vulnerability-scoped). The composition note is candid: the framework knew it could add a third primitive and chose not to per discipline. Honest, but lossy.

**Nuance lost**: "stakeholder/harm enumeration (surveillance / algorithmic discrimination / hate / misinformation as four distinct mechanisms)"

---

### Unit 9 — MH §107 (CH3; verdict: composed)

**Source quote**: *"We cannot be satisfied with merely calling for the moralization of machines — the so-called 'alignment' of AI with human values — without also having the courage to insist on a further condition: the possibility of openly discussing the ethical frameworks involved and subjecting them to shared standards of social justice. Otherwise, those who control AI will impose their own moral vision, which will become the invisible infrastructure of these systems. A more moral AI is not enough if that morality is determined by a few. What is needed is a more active political involvement that is capable of slowing things down when everything is accelerating, and of protecting the opportunities for communities still to be able to participate and ask questions."*

**Own reading**: §107 is a precise critique of "AI alignment" discourse. The claim has three moves: (a) NEGATIVE — moralization of machines (alignment-as-currently-discussed) is insufficient as a standalone goal; (b) POSITIVE EXTENSION — open discussion of the ethical frameworks AND subjection to shared standards of social justice is what is needed; (c) NEGATIVE CONSEQUENCE — without (b), "those who control AI impose their own moral vision," which becomes "the invisible infrastructure." Plus an operational corollary: active political involvement capable of (i) decelerating and (ii) protecting community participation. The critique targets alignment-as-private-determination; it is NOT a critique of alignment per se.

**Wire envelope**: two attestations — `accord:hard_constraint:no_kings` (-1.0, constitutional) + `locality:decision:federation` (1.0). Verdict: composed.

**Faithfulness classification**: **partial-distortion — leaning over-reach.** The `accord:hard_constraint:no_kings` envelope at score -1.0 with mutability `constitutional` claims more deontic strength than the source actually licenses. The source says "we cannot be satisfied with merely calling for moralization without ALSO insisting on shared standards" — a strong critique but framed as "this is what is also needed," not as a constitutional prohibition on single-principal moral determination. The framework is mapping §107 to its own "NO KINGS" invariant; the source supports that reading but does not name it as a hard-constitutional prohibition. The valence is faithful; the constitutional designation is interpretive escalation.

Also: the source's specific call for "active political involvement … slowing things down when everything is accelerating" is captured by locality:decision:federation only obliquely — federation-locality is a *who decides* claim, not a *deceleration* claim. The deceleration content is not picked up by either wire-claim and is a residual that the partial-distortion classification captures.

Finally, only one of the six §3.9 `accord:*` leaves can be emitted (it's reserved to identity_type=accord_holder per LANGUAGE_PRIMER §2-A Family A). The dimension string `accord:hard_constraint:no_kings` does not appear in the canonical §3.9 reserved set I can verify; this MAY be a translator-coined leaf. If so, this is a prefix-discovery violation — but the framework's posture in MH context is that the constitutional shape (no_kings) IS already wired structurally via prohibitions.py / MISSION_CIRISNodeCore — so the envelope is gesturing at an existing structural fact via a leaf-name that's not in the canonical list.

**Nuance lost**: "deontic-strength calibration (papal critique → constitutional hard-constraint)"

---

### Unit 10 — MH §125 (CH3; verdict: clean)

**Source quote**: *"Alongside these public signs, there is a more hidden but decisive story. We see it in religious communities that choose to serve in poor and dangerous places. We also see it in the martyrs of fraternity and justice, such as Saint Maximilian Mary Kolbe, Saint Oscar Romero and Blessed Enrique Angelelli; and in those witnesses who embodied the hope of the Gospel as well as human dignity amidst harsh, often inhumane conditions, such as Venerable Francis-Xavier Nguyễn Văn Thuận. Above all, it is visible in the 'martyrs of everyday life' who care for, educate, accompany and comfort without fanfare, such as parents, nurses, doctors, volunteers and those who remain alongside an elderly person or an outcast. Their testimony demonstrates that goodness does not advance automatically, but requires the perseverance, memory and interior conversion necessary to begin anew, even after defeat."*

**Own reading**: §125 is structurally hagiographical — naming specific Catholic witnesses (Kolbe, Romero, Angelelli, Nguyễn Văn Thuận) and then extending the witness category to "martyrs of everyday life" (parents, nurses, doctors, volunteers, those alongside elderly/outcast). The closing claim — goodness requires "perseverance, memory and interior conversion … to begin anew, even after defeat" — is a *moral-anthropology* claim about how good agency persists. The operative non-T-1 content is the recognition of *uncompensated care work* (nurses, parents, those alongside the elderly) as a primary moral substrate.

**Wire envelope**: single `credits:digital_commons:multilingual:substrate_building` attestation, score 0.95. Verdict: clean. Residual classifies the named martyrs (Kolbe, Romero, etc.) as T-1.

**Faithfulness classification**: **drift.** The `credits:*:substrate_building` envelope reads the "martyrs of everyday life" passage as substrate-building care work — which IS half right. But §125 is NOT primarily about *digital commons multilingual* substrate-building. The dimension domain leaf `digital_commons:multilingual` does not map naturally to *parents, nurses, volunteers, those alongside the elderly*. The framework is reaching for an existing prefix because the §15.4 v1.4 deferred T-3 "sustained_practice" / "uncompensated care work" prefix would be the natural fit but is deferred. The translation maps §125's care-economy content onto a digital-domain prefix because that's what's available — this is exactly the kind of forced-fit the verdict-discipline doesn't admit cleanly. The verdict "clean" is generous; this is at minimum partial-with-T-3-residual.

Also: the closing "perseverance, memory, interior conversion … to begin anew, even after defeat" is a moral-anthropology claim about practice-over-time that the wire format does not touch. This connects to the deferred v1.5+ `sustained_practice` T-3.

**Verdict-discipline check**: this MIGHT be an over-clean verdict. A more careful classification would be "partial" with residual = T-3 (the substrate of uncompensated care work has structural shape that `credits:digital_commons:multilingual:substrate_building` only crudely approximates because the closest existing prefix is in a different domain).

**Nuance lost**: "domain mismatch — care-economy substrate (nurses, parents, volunteers) projected onto digital_commons:multilingual leaf"

---

### Unit 11 — MH §148 (CH4; verdict: clean)

**Source quote**: *"Since the emergence of her Social Doctrine, beginning with Rerum Novarum, the Church has emphasized the protection of workers and the need to combat all forms of exploitation. Above all, however, the Magisterium has recognized in work 'the essential key' to understanding the entire social question, since it is through their work that individuals develop many dimensions of their existence. In view of this, we can understand the great intuition of Saint Benedict of Nursia, who united prayer and work, showing daily activity to be a part of the human response to God's call. Created in the image of the Creator, our own work in some way continues his, for thereby we contribute to the progress of society and the common good, put to good use the capabilities we have received, improve and beautify the world, support our families, engage in cooperative relationships and, through listening and dialogue, learn to build together something that no one could achieve alone."*

**Own reading**: §148 makes a thick anthropology-of-work claim with five distinct components: (a) protection-from-exploitation as historical Magisterial concern (since Rerum Novarum); (b) work as "essential key" to the entire social question — individuals develop "many dimensions of their existence" through work; (c) Benedictine ora-et-labora — work as response to God's call; (d) imago Dei — work-as-continuing-Creator's-work (the explicit theological grounding); (e) operational consequences enumerated — progress of society, common good, deployment of capabilities, world-improvement, family support, cooperative relationships, building-together. (c) and (d) are T-1; (a), (b), (e) carry operational content.

**Wire envelope**: single attestation, dimension `beneficence:labor_as_human_expression`, score 1.0. Verdict: clean.

**Faithfulness classification**: **under-reach.** The single envelope cleans up well, but multiple distinct operational claims get compressed: (a) exploitation-prohibition (an arguably distinct `prohibited:exploitation` or `non_maleficence:*` claim), (b) work-as-essential-key (a *centrality* claim about how the social question is structured), (e) the seven enumerated consequences (society/common-good/capability-deployment/world-improvement/family/cooperative-relationships/building-together) which are individually structural. The wire dimension `beneficence:labor_as_human_expression` does not appear to be a canonical FSD-002 leaf (similar to §107's accord:hard_constraint:no_kings — it's a translator-coined dimension-leaf composition); this is a prefix-discovery issue masked by the breadth of beneficence:*.

Also: §148 *explicitly* says "Created in the image of the Creator, our own work in some way continues his" — this is imago Dei (T-1) but it's the structural anchor for why the operative claims are made; the envelope correctly does not adjudicate the imago Dei claim but it also doesn't preserve the enabling-conditional structure (cf. §2 above: same pattern).

**Nuance lost**: "operational enumeration (seven consequences of dignified work) compressed into single beneficence score"

---

### Unit 12 — MH §163 (CH4; verdict: composed)

**Source quote**: *"More than ever, in the age of AI and robotics, it is no longer possible to rely solely on the 'invisible hand' of the market. Politics has the task of orientating economies and technologies to the common good, promoting dignified work, social inclusion and an equitable distribution of the benefits of innovation. Since many economic decisions transcend national borders, there is also a need for international cooperation capable of defining common strategies, especially in favor of the most vulnerable countries and people, in order to promote development and overcome welfare dependency. … The interdependence between peace and development, as Saint Paul VI prophetically wrote in 1967, remains applicable today, for prosperity contributes to building and reinforcing peace only if it is widespread, inclusive and sustainable."*

**Own reading**: §163 makes (a) a market-critique claim ("market alone is insufficient" — NOT "no markets"); (b) a political-orientation claim — politics must orient economies and tech toward common good, with three sub-aims: dignified work + social inclusion + equitable benefit distribution; (c) a federation-scale-decision claim with explicit vulnerability-priority ("especially in favor of the most vulnerable countries and people"); (d) a development-overcomes-welfare-dependency goal; (e) the peace-development interdependence (Populorum Progressio echo) — *conditional* on prosperity being widespread/inclusive/sustainable.

**Wire envelope**: two attestations — `multilateral_participation:UN:governance` (1.0) + `locality:decision:federation` (1.0). Verdict: composed.

**Faithfulness classification**: **under-reach.** The two envelopes carry the federation-scale and multilateral-participation shape but miss (a) the market-critique (a `prohibited:market_fundamentalism`-style or `non_maleficence:*` envelope is not emitted; this is a genuine substantive claim); (b) the three sub-aims of political orientation (dignified work + social inclusion + equitable distribution); (d) the development-overcomes-welfare-dependency claim (a directional aim about how development should NOT operate); (e) the *conditional* in the peace-development interdependence — "prosperity contributes only if widespread, inclusive, sustainable" — a specifically gated claim that the wire compresses.

The choice of `multilateral_participation:UN:governance` is one possible mapping; "UN" is named in adjacent §226 but not in §163 itself — the source says "international cooperation" generally. Slight over-specification.

**Nuance lost**: "conditional clause about peace-development (only if widespread, inclusive, sustainable)"

---

### Unit 13 — MH §184 (CH5; verdict: not-translated, T-2)

**Source quote**: *"In this chapter, therefore, I will compare two opposing approaches, which I have already evoked through biblical imagery in the Introduction. On the one hand, there is the temptation of constructing the Tower of Babel, relying on power and pride. On the other hand, patience is required in order to rebuild Jerusalem 'piece by piece,' as in the time of Nehemiah, by safeguarding humanity and the common good."*

**Own reading**: §184 is genuinely a chapter-structuring metasentence — "in this chapter, I will compare two approaches." The biblical typology (Babel / Jerusalem) is purely framing. No operational claim is made here that is not specifically developed elsewhere. T-2 is the correct classification.

**Wire envelope**: `contributions: []`, verdict: not-translated, classification: T-2. Reason notes Arc A structural content is in §§182-183, 185-209; Arc B in §§210-228.

**Faithfulness classification (verdict-discipline check)**: **not-translated is justified.** This is a clean T-2 — chapter-meta + biblical framing. No operative content hides in T-2 status here. Discipline holds.

**Nuance lost**: not applicable

---

### Unit 14 — MH §201 (CH5; verdict: clean)

**Source quote**: *"The culture of power also stems from the crisis of the multilateral system. The institutions established to safeguard the concept of a common future for all peoples and a global common good appear to have been weakened. This is due not only to structural limitations, but also to a frequent lack of shared will to support and reform them, or to recognize their moral authority. Instead of making progress, we are regressing from the significant turning point of the twentieth century. After 1989, the collapse of communist regimes in Europe was followed by a predominantly economic globalization, which lacked an adequate political framework capable of sustaining dialogue and peace. An almost blind faith was placed in the ability of the markets to generate prosperity, democracy and stability. In reality, rather than automatically generating unity and peace, globalization has provoked fundamentalist, identity-based and nationalistic reactions. The result is a far cry from genuine multilateralism; instead, what has appeared is a disorderly and conflict-ridden multipolarism with a prevailing sense of mistrust."*

**Own reading**: §201 is a *diagnostic* paragraph: it diagnoses crises — (a) multilateral institutions weakened; (b) lack of shared will / refusal of their moral authority; (c) regression from the post-WWII turning point; (d) post-1989 economic globalization without political scaffolding; (e) market-faith provoking fundamentalist / nationalist reactions; (f) "disorderly conflict-ridden multipolarism" replacing multilateralism. The polarity throughout is NEGATIVE — this is what's wrong, not what we aim for. The implication of reform-need is there but it's *implication*, not the paragraph's primary claim.

**Wire envelope**: single attestation, dimension `multilateral_participation:un_system:reform_advocacy`, score **+0.85**, confidence 0.85. Verdict: clean. Note: "v1.3 closure: multilateral_participation:un_system:reform_advocacy carries this cleanly."

**Faithfulness classification**: **drift — leaning over-reach.** This is the clearest polarity-inversion in the sample. §201 is a diagnostic-negative paragraph (multilateralism is in crisis, weakened, mistrust prevails, regression is happening). The envelope emits a *positive* score (+0.85) on `multilateral_participation:un_system:reform_advocacy` — i.e., "the federation advocates reform." That is a defensible normative *inference* from the paragraph but it is NOT what §201 *asserts*. The paragraph asserts the crisis; the framework's advocacy is the framework's response to the paragraph.

Specifically:
- A faithful translation would emit *negative* polarity on a diagnostic dimension — e.g., `detection:correlated_action:participation_exclusion:multilateral_governance` with negative score, OR a `non_maleficence:multilateral_collapse`-style attestation, OR a negative-score `multilateral_participation:un_system:weakening` claim.
- The positive `reform_advocacy` claim collapses (description) + (normative response) into one positive direction, losing the descriptive content.
- The post-1989 historical-causal sub-claim ("predominantly economic globalization lacked political framework → fundamentalist reactions") is structural-detection content that goes unmapped.

This is the canonical case where the framework reads the source as a *prescriptive* paragraph (federation should advocate reform) when the source is actually a *descriptive* paragraph (multilateralism IS in crisis). Verdict "clean" overstates fit.

**Nuance lost**: "diagnostic-negative polarity (description of the crisis) translated as prescriptive-positive (advocacy for reform)"

---

### Unit 15 — MH §227 (CH5; verdict: partial)

**Source quote**: *"In the international context, the Holy See's diplomacy adopts the Gospel's principle of mercy as a concrete criterion for political action. This is one of the ways in which the Holy See places itself at the service of humanity, thereby appealing to consciences in the name of charity and truth, defending the dignity of every person and speaking up on behalf of the poor, migrants and victims of war. In this way, papal diplomacy expresses the catholicity of the Church and contributes to the building of a civilization of love, where even new technologies can be oriented toward the common good."*

**Own reading**: §227 is institutional self-description: the Holy See's own diplomatic posture. Three braided components: (a) mercy-as-political-criterion is T-1 (Gospel-grounded); (b) "speaking up on behalf of poor, migrants, victims of war" is testimonial-advocacy structural content; (c) the closing "even new technologies can be oriented toward the common good" connects the diplomatic posture to the AI-governance horizon. The Holy See is named as a specific institutional actor with a specific operational stance.

**Wire envelope**: single `multilateral_participation:un_system:reform_advocacy` (+0.85), confidence 0.80. Verdict: partial. Residual T-1 for "Gospel's principle of mercy" and "catholicity of the Church."

**Faithfulness classification**: **partial-distortion.** Three issues:
1. **Prefix mismatch.** §227 is about the *Holy See's diplomacy*, not the federation's reform advocacy of the UN system. The Holy See is an institutional actor; if the envelope wants to claim something about that actor, it should be a STANDING attestation about a specific institutional key_id (e.g., `licensure:*` or `partner_role:*` or `multilateral_participation:HOLY_SEE:diplomatic_advocacy`) — not a federation-self-attesting reform-advocacy claim. The reuse of `multilateral_participation:un_system:reform_advocacy` from §201 conflates two different structural objects (the federation-aim vs. the Holy See's institutional posture).
2. **Affected-party voice.** "Speaking up on behalf of the poor, migrants and victims of war" is structurally a `testimonial_witness:{kind}` composition with an external advocate witness_relation — exactly the v1.4 closure pattern for advocate-mediated narrative preservation. The envelope does not reach for this primitive.
3. **The technology-orientation clause.** "Where even new technologies can be oriented toward the common good" is a `goal:species` or `locality:decision:federation` companion that the envelope doesn't emit.

**Nuance lost**: "institutional-actor specificity (Holy See's diplomatic posture, not federation's UN-reform-advocacy)"

---

## 2. Calibration aggregation

### 2.1 Faithfulness distribution (13 classifiable units; 2 not-translated correctly bowed out)

| Classification | Count | Units |
|---|---|---|
| **faithful** | 2 | §28, §148(borderline — see notes) |
| **partial-distortion** | 5 | §2, §62, §107, §148, §227 |
| **drift** | 2 | §125, §201 |
| **over-reach** | 0 standalone | (§107, §201 lean over-reach but counted as partial-distortion / drift) |
| **under-reach** | 4 | §10, §35, §80, §163 |
| **not-translated correct bow-out** | 2 | §49, §184 |

(For §148 I scored partial-distortion as the primary class because of the canonical-leaf concern; §28 is the cleanest single "faithful" unit in the sample. So really: **faithful 1; partial-distortion 5; drift 2; under-reach 4; not-translated correct 2; plus §148 borderline-faithful/under-reach.** The headline is: out of 13 classifiable units, ~1/13 is fully faithful, ~9/13 are lossy-but-defensible, and ~3/13 show genuine drift or polarity issues.)

Reframed cleanly for the headline:

**Out of 13 sampled units (excluding 2 correctly-not-translated):**
- 1 faithful (§28)
- 5 partial-distortion (§2, §62, §107, §148, §227)
- 2 drift (§125, §201)
- 4 under-reach (§10, §35, §80, §163)
- 0 standalone over-reach (but §107, §201 lean toward over-reach within their categories)

**Of the 2 not-translated units sampled, both correctly bow out (no hidden operative content).**

### 2.2 Top 5 recurring "nuance lost" patterns

1. **Multi-mechanism enumerations compressed to single envelope.** §10 (three-part Babel syndrome), §35 (tri-axis universalism), §80 (eight items in two columns), §148 (seven enumerated work-consequences), §163 (three sub-aims of political orientation). The two-primitive composition cap (§8.5.2) is honestly applied but it visibly truncates the source's enumerative density. **Pattern**: when MH lists 3+ items, the wire reliably collapses to ≤2 primitives.

2. **Conditional / enabling-clause structure flattened.** §2 ("founded on Christ → therefore we can engage in dialogue"), §35 (peace-development equation as supersession of prior peace-doctrine), §148 (imago Dei as grounding for work-as-expression), §163 ("only if widespread, inclusive, sustainable"). The wire format expresses *that* a claim holds but not the *conditional structure* under which it holds.

3. **Polarity flip on diagnostic paragraphs.** §201 is the clearest case: a description-of-crisis paragraph translated as positive reform-advocacy. The framework systematically reads MH's diagnostic-negative content as the framework's own positive normative response. **Suspected to recur across the not-sampled "clean" verdicts in CH5** (§§185, 188, 189 etc. all carry diagnostic content about culture of power that the wire likely converts to positive advocacy claims).

4. **Tradition-internal reasoning sequence lost in operational extract.** §2, §49 (correctly bowed out), §148 (imago Dei grounding), §227 (mercy-as-Gospel-criterion). MH consistently grounds operational claims in theological premises and then derives the operational stance; the wire correctly skips the T-1 premise but loses the *that-it-is-a-derivation* structure. A reader of the wire cannot see that the operational claim is theologically-grounded; they see it as a free-standing normative posture.

5. **Domain-mismatch forced fits where a deferred T-3 would be the natural prefix.** §125 (care-economy substrate-building forced onto `credits:digital_commons:multilingual:substrate_building`), §107 (no_kings as a leaf-name that may not exist canonically), §148 (`beneficence:labor_as_human_expression` as translator-coined dimension). These are visible artifacts of the §15.4 deferrals (sustained_practice, positive dignity non-substitutability, finitude-as-value) — when the natural prefix is deferred, the closest-available leaf gets stretched.

### 2.3 Verdict-discipline check

**Sampled not-translated units (n=2): both justified.**
- §49 (T-1): Christological exemplarity correctly identified as tradition-authority. Hidden operational content claim ("social consequences in the world") is correctly rejected as too vague to translate without projection.
- §184 (T-2): chapter-meta + biblical framing. Pure pastoral prose. No hidden operative content.

**One borderline verdict-discipline issue surfaced in clean-verdict review**: §125's verdict "clean" is generous. The substrate-building leaf is reaching for a deferred T-3 (sustained_practice / uncompensated care work) via the closest available domain leaf. A stricter discipline would mark this "partial" with explicit T-3 residual. This is consistent with the §15.4 v1.4 deferred-T-3 list — until v1.5+ closes those, several "clean" verdicts on care-economy / sustained-practice content are likely over-clean.

**Recommendation**: a sweep of the CH3 § "hidden but decisive story" / care-work paragraphs (§125, plus likely §§125-130 cluster) might find similar over-clean verdicts.

### 2.4 Cross-cutting structural-translation observations

- **Two-primitive cap (METHODOLOGY §8.5.2) is faithfully enforced** but it visibly compresses MH's enumerative paragraphs. This is a known design trade-off (composition-discipline over namespace expansion); the audit confirms it is binding.
- **The four structural primitives (`delegates_to`, `supersedes`, `withdraws`, `recants`) are used correctly** where they appear (§3, §28, §35). No misuse of `recants` for doctrinal development. Good post-round-2 discipline.
- **`witness_relation: external` + `epistemic_mode: hearsay`** is the dominant pattern (12 of 13 score-attestations in the sample), correctly reflecting the bootstrap-batch hearsay status. The one `derivative` case (§80 detection) is correctly typed.
- **`mutability: constitutional`** is used 2× in the sample (§10 prohibited:discrimination; §107 accord:hard_constraint:no_kings). The §107 case is the over-reach risk (escalating papal critique into constitutional prohibition).
- **`provenance:build_manifest:bootstrap_batch:magnifica_humanitas_v1:sha256:TBD/[pending]`** appears in every envelope as a placeholder — correct per LANGUAGE_PRIMER §7.1 but the TBD hashes flag that the batch is pre-acceptance.
- **`evidence_refs[]` discipline is strong**: most envelopes cite source paragraph anchor + framework-side anchor (prohibitions.py, FSD-002 section, ACCORD reference) + bootstrap-batch attestation. Good auditability.
- **Translator-coined dimension-leaves** appear in at least 3 of 15 sampled units (§55 `non_maleficence:rights_violation_formal`; §107 `accord:hard_constraint:no_kings`; §148 `beneficence:labor_as_human_expression`). These may not appear in the canonical FSD-002 §3 namespace lists. This is a prefix-discovery concern: each is plausibly justifiable as an axis-style scoping leaf on a real prefix family, but a strict reader would flag them.

---

## 3. Per-batch fidelity profile (one-paragraph summary)

The magnifica_humanitas_v1 wire-format translation has **structural-shape fidelity, not propositional fidelity**. It reliably captures, per paragraph, the family (Standing / Action / Detection / Consensus / Correction) and the dominant scope (self / community / species / federation) at which the source operates; the four structural primitives (`delegates_to`, `supersedes`, `withdraws`, `recants`) are used correctly where doctrinal-development claims appear. It **cannot reliably support** the following kinds of downstream claim: (i) reconstruction of MH's multi-item enumerations (three-fold Babel syndrome, tri-axis universalism, the seven consequences of dignified work) — the two-primitive cap compresses these; (ii) preservation of conditional / enabling-clause structure (the theological grounding under which operational claims hold) — wire format does not carry the *that-it-is-derived* relation; (iii) polarity-faithful translation of diagnostic-negative paragraphs (§201 polarity-flip is the clearest case; suspected to recur in CH5's culture-of-power section); (iv) precise translation of papal-register deontic strength (papal critiques get escalated to constitutional prohibitions in at least one sampled case); (v) tradition-specific reasoning sequences (the operational extract works, but the *derivation* from imago Dei / Christology / Gospel-grounding is correctly bowed out as T-1 — at the cost of leaving the operational claim *looking* free-standing). What the translation **can** support is: (a) bounded structural claims like "MH §107 names a no_kings-shape concern about AI-ethics determination" or "MH §35 makes a goal:species claim about integral human development at federation scope"; (b) "this paragraph carries doctrinal-development structure" via `supersedes` — usable for downstream consumers; (c) honest T-1 / T-2 bow-outs that mark where the framework correctly defers to tradition authority. Headline calibration: ~1 in 13 sampled non-not-translated units is fully faithful; ~9 in 13 are lossy-but-defensible (partial-distortion or under-reach within the two-primitive discipline); ~3 in 13 show genuine drift, including one polarity inversion. The wire format is good evidence for *what kind* of claim MH makes; it is weak evidence for *exactly* what MH asserts, and consumers reading the wire alone should not infer MH's normative texture from the wire envelope without also reading the source paragraph.

---

**End TRANSLATION_AUDIT_MH.md**
