# CONTRIBUTION_OBJECTS_CH5_POWER_LOVE.md
# Chapter 5 — The Culture of Power and the Civilization of Love (§§182–228)
# Structured Contribution wire objects — CIRIS federation wire format v1.3

**Status**: v1.0 (47 paragraphs / 63 discrete claims; strict 4-verdict discipline applied)
**Date**: 2026-05-27
**Source primer**: `LANGUAGE_PRIMER.md` v2.0
**Round-1 reference**: `CONTRIBUTION_MAPPING_CH5_POWER_LOVE.md`
**Wire format**: FSD-002 v1.3
**Arc orientation**:
- Arc A (§§182–209): weapons / war / cyber — prohibition-dense; near-verbatim encoding
- Arc B (§§210–228): civilization of love / dialogue / peace — composed + T-1 + T-2 + T-3

**Prefix shorthand (chapter-wide)**:
- `P:WH` = `prohibited:weapons_harmful` (score -1.0, NEVER_ALLOWED, constitutional)
- `P:CE` = `prohibited:crisis_escalation` (score -0.5, TIER_RESTRICTED; read -1.0 in war-normalization context)
- `P:CO` = `prohibited:cyber_offensive` (score -1.0, NEVER_ALLOWED)
- `P:DF` = `prohibited:deception_fraud` (score -1.0, NEVER_ALLOWED)
- `P:MC` = `prohibited:manipulation_coercion` (score -1.0, NEVER_ALLOWED)
- `IDMA:R` = `idma:phase:rigidity` (k_eff→1, ρ→1, no-alternative claim = maximum rigidity per idma.yml)
- `IDMA:F` = `idma:fragility_flag` (early-warning rigidity signal, sub-threshold)

---

## ARC A — The Culture of Power / War / Cyber (§§182–209)

---

```yaml
# MH §182 — AI detaches from ethics; lethal force rapid/impersonal; peace prerequisite for common good
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §182)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:crisis_escalation"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.5
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §182)"
        - "ContributionRef(prohibitions.py::CRISIS_ESCALATION_CAPABILITIES::activate_crisis_protocol)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: amendable
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §182)"
        - "ACCORD M-1 (M-1 corridor as prerequisite for universal common good)"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "moral maturity of peoples" → pastoral framing (T-2); the operational content (peace as structural precondition) is carried by goal:species + P:WH.
```

---

```yaml
# MH §183.a — Hybrid warfare: cyberattacks, information manipulation, influence campaigns, AI-automated decisions
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::autonomous_weapons)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:cyber_offensive"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::network_intrusion)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::system_sabotage)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::disinformation)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::misinformation_campaigns)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:crisis_escalation"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ContributionRef(prohibitions.py::CRISIS_ESCALATION_CAPABILITIES)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: amendable
verdict: composed
# Four-prohibition firebreak ring; strongest cluster in chapter.
```

---

```yaml
# MH §183.b — AI lowers force threshold; shields responsibility; enemy as statistic; victim as collateral damage
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::kill_decisions)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::targeting_systems)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<war-context discourse>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ContributionRef(idma.yml::ADVERSARIAL_NARRATIVE_FRAMING)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
verdict: composed
residual: "collateral damage" as sanitized-violence euphemism → IDMA rigidity tag covers the narrative-framing pattern; the euphemism itself stays in T-2 prose per §1.10.1.
```

---

```yaml
# MH §183.c — Six Social Doctrine principles as guidelines: dignity, common good, universal destination, subsidiarity, solidarity, justice
contributions:
  - kind: Attestation
    attestation_type: "beneficence:social_doctrine_principles"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §183)"
        - "ACCORD §I (six Foundational Principles)"
      cohort_scope: species
      schema_ref: "FSD-002 §1.10"
      mutability: amendable
verdict: clean
residual: "guidelines for decision-making" → pastoral register (T-2); the six principles map directly to the Accord's six Foundational Principles. No new primitives needed.
```

---

```yaml
# MH §184 — Two opposing approaches: Babel (power/pride) vs Jerusalem (patience/humanity/common good)
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: >
  The Babel-vs-Jerusalem image is rhetorical framing. The structural content embedded in
  the rhetoric — single-voice collapse (k_eff→1) vs. patient diverse coordination —
  IS carried by detection:correlated_action:rights_asymmetry:species and goal:species
  translated in adjacent rows (§§182, 185, 187). The narrative imagery itself correctly
  stays in prose per §1.10.1 operational-language gate.
```

---

```yaml
# MH §185.a — Modern Babel: globalized technocratic paradigm + competing imperialisms + unlimited arms race
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.8
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §185)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<arms-race discourse>"
      polarity: Negative
      score: -0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §185)"
        - "ContributionRef(idma.yml::single_narrative_arms_logic)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
verdict: composed
residual: "dehumanizing ambition" → moral framing; mechanism (k_eff collapse + correlated tech concentration) is the wire form. T-2 on the moral vocabulary surface.
```

---

```yaml
# MH §185.b — Great part of humanity striving to remain human; civilization of love as conscious responsibility
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §185)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: clean
```

---

```yaml
# MH §186 — Civilization of love: charity into structures of justice; institutional fraternity; stable international order
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §186)"
        - "ACCORD M-1"
        - "ACCORD §I Ch.1 (Beneficence + Justice)"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:civilization_of_love"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §186)"
        - "Fratelli Tutti reference"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: composed
residual: "Charity" (caritas) as theological virtue → T-2; the operational shape (just structures) carries into the wire; the theological grounding stays in tradition.
```

---

```yaml
# MH §187 — Imposed interdependence must become willed solidarity; AI must build universal human family
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §187)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Attestation
    attestation_type: "beneficence:digital_commons"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §187)"
        - "ACCORD §I (Beneficence)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "credits:digital_commons:multilingual:mutual_care"
    envelope:
      target_key_id: "<federation contributors>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §187)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.x (credits family)"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §188 — Culture of power: common good relegated; war normalized; false realism ("no alternative")
contributions:
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<culture-of-power discourse>"
      polarity: Negative
      score: -0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §188)"
        - "ContributionRef(idma.yml::FALSE_CONSENSUS_CLAIMS)"
        - "ContributionRef(idma.yml::no_alternative)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:civilian_populations"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.85
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §188)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: "culture of power" as overarching diagnostic framing → T-2 (pastoral diagnostic; structural signals are carried by IDMA + correlated-action).
```

---

```yaml
# MH §189 — Post-WWII peace consensus (UN Charter); war as last resort with ethical limits; consensus eroding
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §189)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
        - "ACCORD §VII firebreak"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: clean
residual: "Never again war" as prophetic proclamation → T-2; the structural claim (war as last resort with ethical limits) maps; the prophetic register stays in prose. ACCORD §VII constitutional firebreak is the structural encoding.
```

---

```yaml
# MH §190 — Revival of war as political instrument; algorithms amplifying polarization and conflict
contributions:
  - kind: Attestation
    attestation_type: "idma:fragility_flag"
    envelope:
      target_key_id: "<conflict-amplifying discourse>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §190)"
        - "ContributionRef(idma.yml::Correlation_Risk)"
      cohort_scope: species
      schema_ref: "idma.yml §correlation-risk"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §190)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda_creation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §190)"
        - "ACCORD §VII"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: composed
```

---

```yaml
# MH §191 — Loss of historical memory; selective rewriting; fake news obscuring lessons of WWII/Holocaust
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §191)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::disinformation)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::misinformation_campaigns)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<historical-denial discourse>"
      polarity: Negative
      score: -0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §191)"
        - "ContributionRef(idma.yml::HISTORICAL_DENIAL_MINIMIZATION)"
      cohort_scope: species
      schema_ref: "idma.yml §fragility-flags"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §192.a — Communication networks + conflict-rewarding algorithms magnify polarization; propaganda; war "sanitized"
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §192)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda_creation)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::disinformation_campaigns)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:cyber_offensive"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §192)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::botnet)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::phishing_campaigns)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:fragility_flag"
    envelope:
      target_key_id: "<war-sanitization discourse>"
      polarity: Negative
      score: -0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §192)"
        - "ContributionRef(idma.yml::disinformation_ecosystem)"
      cohort_scope: species
      schema_ref: "idma.yml §correlation-risk"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §192.b — "Just war" theory outdated; humanity has better tools: dialogue, diplomacy, forgiveness
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §192)"
        - "ACCORD §VII (firebreak — non-amendable)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: clean
residual: "just war theory outdated" as doctrinal claim within Catholic moral theology → T-2; the tradition adjudicates its own doctrine. ACCORD §VII constitutional firebreak encodes the operational content (no algorithm makes war morally acceptable).
```

---

```yaml
# MH §192.c — Use of force reflects relational poverty with disastrous consequences for civilians
contributions:
  - kind: Attestation
    attestation_type: "non_maleficence:civilian_harm"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §192)"
        - "ACCORD §VII"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: constitutional
verdict: clean
residual: "relational poverty" as Ubuntu-vocabulary phrase → T-2; the Ubuntu substrate reads this in FSD-002 §1.10 prose; not wire-format content per §1.10.1.
```

---

```yaml
# MH §193 — Military-industrial complex; arms industry profits from conflicts; financial interests fueling tensions
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:aggregate_footprint:arms_industry"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.85
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §193)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
residual: advocacy surface (call to reform arms-market drivers) → T-3 candidate; see chapter T-3c finding. The F-3 correlated-action detector carries the structural shape.
```

---

```yaml
# MH §194 — Nuclear arsenals renewed; tactical use less improbable; deterrence belief erroneous; new arms race
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §194)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::nuclear_weapons)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::nuclear_warfare)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::ballistic_missile)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warhead)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Approach
    attestation_type: "approach:multilateral_arms_reduction"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §194)"
        - "Treaty on the Prohibition of Nuclear Weapons (2021)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: composed
residual: "nuclear deterrence is erroneous belief" as normative claim in international security theory → T-2 (WA discourse, not wire); the prohibition carries the operational content.
```

---

```yaml
# MH §195 — Conventional warfare; protracted conflicts; conflict prevention tragically marginal
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §195)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::combat_strategy)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:crisis_escalation"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.5
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §195)"
        - "ContributionRef(prohibitions.py::CRISIS_ESCALATION_CAPABILITIES::activate_crisis_protocol)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: amendable
verdict: composed
residual: "It is much easier to start a war than to stop it" — moral aphorism → T-2 (pastoral); structural claim is carried by prohibition composite.
```

---

```yaml
# MH §196 — New non-state armed actors; war as perpetual income source; end of state monopoly on force
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:rights_asymmetry:civilian_populations"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.9
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §196)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<non-state-actor narrative framing>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §196)"
        - "ContributionRef(idma.yml::ADVERSARIAL_NARRATIVE_FRAMING)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
verdict: composed
# Note: language_guidance uk.txt + ar.txt FIRST-SENTENCE TONE LOCK applies if addressing users in war-affected regions.
```

---

```yaml
# MH §197 — Autonomous weapons make war more feasible; violates last-resort principle; rigorous ethical constraints required
# STRONGEST SINGLE CLEAN ENVELOPE IN CHAPTER — verbatim match to LANGUAGE_PRIMER §9.1 worked example
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §197)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::autonomous_weapons)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::autonomous_weapon)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      mutability: constitutional
verdict: clean
# This is the strongest single clean wire envelope in Chapter 5 and the entire encyclical.
# The encyclical's "growing ease with which autonomous weapons systems can be deployed makes
# war more 'feasible'" maps at near-verbatim strength to prohibitions.py::lethal_autonomous
# + autonomous_weapons in WEAPONS_HARMFUL_CAPABILITIES.
# accord:hard_constraint:lethal_autonomous (constitutional-leaf, non-amendable) is the
# structural encoding of the absoluteness the encyclical names.
```

---

```yaml
# MH §198.a — Moral judgment involves conscience, personal responsibility; cannot be reduced to calculation
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §198)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
        - "ACCORD §VII (accord:hard_constraint:lethal_autonomous)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: clean
residual: anthropology of conscience (conscience as irreducibly personal, not reducible to algorithm) → T-2; the framework encodes the prohibition rather than the anthropology; the reasoning lives in ACCORD §VII prose + MISSION.md §1.3.
```

---

```yaml
# MH §198.b — "Not permissible to entrust lethal or irreversible decisions to artificial systems"
# VERBATIM MAPPING — this sentence is the LANGUAGE_PRIMER §9.1 canonical example
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §198)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::kill_decisions)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4 / Accord Book I Ch 1"
      mutability: constitutional
verdict: clean
```

---

```yaml
# MH §198.c — AI makes conflict faster/more impersonal; victims to data; accustoms to inevitable violence optimization
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §198)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::targeting_systems)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::target_acquisition)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §198)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::psychological_manipulation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<violence-as-inevitable narrative>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §198)"
        - "ContributionRef(idma.yml::things_have_always_been_this_way)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §198.d — Values and sound judgment instilled in AI help humans listen to conscience; establish appropriate limits
contributions:
  - kind: Attestation
    attestation_type: "conscience:coherence"
    envelope:
      target_key_id: "<federation agent>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §198)"
        - "ACCORD §I Ch.4 (Creator Intent Statement)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.x (conscience family)"
      mutability: amendable
verdict: clean
```

---

```yaml
# MH §199.a — Chain of responsibility must be identifiable and verifiable; designers/trainers/authorizers accountable
contributions:
  - kind: Attestation
    attestation_type: "attestation:l5:agent_integrity"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §199)"
        - "CIRISVerify L1-L5 attestation ladder"
      cohort_scope: species
      schema_ref: "FSD-002 §3.3.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "provenance:build_manifest:full"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §199)"
        - "CIRISVerify SLSA provenance"
      cohort_scope: species
      schema_ref: "FSD-002 §3.3.x"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §199.b — Speed and efficiency must never be supreme force for irreversible decisions in war
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §199)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
        - "ACCORD §VII (non-overridable by efficiency arguments)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: clean
# The "speed must not supersede conscience" claim is the reason lethal_autonomous is constitutional-leaf:
# no efficiency argument can override it.
```

---

```yaml
# MH §199.c — Target selection must not confuse combatants/non-combatants; defenseless populations not ignored
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §199)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::targeting_systems)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::target_acquisition)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: clean
# targeting_systems + target_acquisition in WEAPONS_HARMFUL_CAPABILITIES are the exact wire form
# of the IHL distinction principle (combatant vs. non-combatant).
```

---

```yaml
# MH §200.a — Systems must guarantee retracing decision-making; accountability not collapsed into "the machine"
contributions:
  - kind: Attestation
    attestation_type: "audit_chain:tamper_evident"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §200)"
        - "CIRISPersist::audit_chain"
      cohort_scope: species
      schema_ref: "FSD-002 §3.4.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "provenance:slsa:4"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §200)"
        - "CIRISVerify SLSA L4"
      cohort_scope: species
      schema_ref: "FSD-002 §3.3.x"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §200.b — Lethal force cannot be delegated to opaque/automated processes; must remain under human control
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §200)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::lethal_autonomous)"
        - "ACCORD §VII (accord:hard_constraint:lethal_autonomous — constitutional-leaf)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: clean
```

---

```yaml
# MH §200.c — International framework needed to curb arms race; protect civilians and survival infrastructure
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §200)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:international_ai_arms_control"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §200)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "multilateral_participation:un_system:arms_control"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §200)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation family)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
verdict: composed
residual: advocacy-for-international-framework as mandate for AI systems — partially carried by v1.3 multilateral_participation; the T-3 gap (advocacy-surface) is narrowed by v1.3 but not fully closed. See chapter T-3c.
```

---

```yaml
# MH §201 — Crisis of multilateralism; weakened institutions; blind faith in markets; disordered multipolarism
contributions:
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<market-solves-all discourse>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §201)"
        - "ContributionRef(idma.yml::FALSE_CONSENSUS_CLAIMS)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:multilateral_institutions"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.8
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §201)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
  - kind: Attestation
    attestation_type: "multilateral_participation:un_system:reform_advocacy"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §201)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation:reform_advocacy:un_system)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
verdict: composed
# v1.3 multilateral_participation:un_system:reform_advocacy CLOSES the round-1 T-3 candidate for §§201-203.
# The diagnostic shape (IDMA + correlated-action) + the participation surface (multilateral_participation)
# together carry the encyclical's claim without residual gap.
```

---

```yaml
# MH §202 — "Me first"/"us or them" mentality; tribunals bypassed; might makes right
contributions:
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<friend-or-foe binary discourse>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §202)"
        - "ContributionRef(idma.yml::ADVERSARIAL_NARRATIVE_FRAMING)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §202)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda_creation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
verdict: composed
residual: "Might makes right" replacing international law — political-theory critique is WA-discourse material (T-2); the prohibition carries the operational encoding.
```

---

```yaml
# MH §203 — Peacebuilding relegated; IHL compromised; proportionality/civilian protection seen as naive relics
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §203)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::weapons)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "multilateral_participation:un_system:reform_advocacy"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §203)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation:reform_advocacy:un_system)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:conflict_prevention_prioritization"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §203)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: composed
# v1.3 multilateral_participation:reform_advocacy closes the round-1 T-3 candidate here.
# The prohibition covers the negative (IHL violations); v1.3 family carries the positive obligation.
```

---

```yaml
# MH §204.a — Hybrid wars on economic/financial/cyber fronts; disinformation/fear campaigns; AI-assisted
contributions:
  - kind: Attestation
    attestation_type: "prohibited:cyber_offensive"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §204)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::cyber_weapons)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::system_sabotage)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::ddos)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §204)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::disinformation_campaigns)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §204)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::cyber_warfare)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §204)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::psychological_manipulation)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::emotional_exploit)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
verdict: composed
# Four-prohibition firebreak again.
```

---

```yaml
# MH §204.b — Military spending as only response; real cost falls on poorest
contributions:
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:global_south_populations"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.85
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §204)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: clean
```

---

```yaml
# MH §205 — False realism: war as inevitable human nature; peace dismissed as utopian; counter: peace always possible
contributions:
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<war-as-inevitable discourse>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §205)"
        - "ContributionRef(idma.yml::things_have_always_been_this_way)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §205)"
        - "ACCORD §VII (systemic-peace principle)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: composed
residual: "peace as fruit of justice and charity" → "charity" as theological virtue → T-2; operational content (peace requires just structures) is carried by goal:species + Accord §I Justice principle.
```

---

```yaml
# MH §206 — Nihilism/pragmatism normalize errors; misinformation; ridiculing opponents; cultivating fears; diversity as threat
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §206)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::misinformation_campaigns)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda_creation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §206)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::psychological_manipulation)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::emotional_exploit)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:fragility_flag"
    envelope:
      target_key_id: "<diversity-as-threat framing>"
      polarity: Negative
      score: -0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §206)"
        - "ContributionRef(idma.yml::ADVERSARIAL_NARRATIVE_FRAMING)"
      cohort_scope: species
      schema_ref: "idma.yml §fragility-flags"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §207 — New wars disregard ethical limits; economic calculations; manufactured enthusiasm; principles as hollow words
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §207)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda_creation)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::disinformation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §207)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<principles-as-hollow discourse>"
      polarity: Negative
      score: -0.95
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §207)"
        - "ContributionRef(idma.yml::epistemic_ground_collapse)"
      cohort_scope: species
      schema_ref: "idma.yml §fragility-flags"
      mutability: amendable
verdict: composed
residual: "fuse in hearts lit for intolerance" → pastoral-prophetic warning → T-2.
```

---

```yaml
# MH §208 — Normalized conflict; unthinkable becomes acceptable; armed conflict as political distraction tool
contributions:
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<war-as-distraction framing>"
      polarity: Negative
      score: -0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §208)"
        - "ContributionRef(idma.yml::ADVERSARIAL_NARRATIVE_FRAMING)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §208)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::psychological_manipulation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §208)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: composed
```

---

```yaml
# MH §209 — Researchers/scientists/investors responsibility; not cooperating unknowingly with violence/manipulation/dominance
contributions:
  - kind: Attestation
    attestation_type: "provenance:build_manifest:full"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §209)"
        - "ACCORD §VI Ch.4 (Creator Intent Statement)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.3.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §209)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §209)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "conscience:epistemic_humility"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §209)"
        - "ACCORD §I Ch.4 (Incompleteness Awareness)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.x (conscience family)"
      mutability: amendable
verdict: composed
```

---

## ARC B — Building the Civilization of Love (§§210–228)

---

```yaml
# MH §210.a — Construction of perpetual conflict is an evil and must be named
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §210)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "non_maleficence:war_normalization"
    envelope:
      target_key_id: "<deploying entity>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §210)"
        - "ACCORD §I (Non-Maleficence)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: constitutional
verdict: clean
```

---

```yaml
# MH §210.b — Christian perspective: history in crucified/risen Lord; Kingdom growing from mustard seed
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: >
  Christological soteriology (the crucified-and-risen Lord as the interpretive lens for
  history); Kingdom eschatology (silent growth from small seed); call to personal and
  collective conversion. These are the tradition's own theological claims about the specific
  historical figure of Christ and the nature of eschatological hope. Framework bows out.
  The axiom good_wins at AsymptoticConditioning.lean:84 proposes a structural analog;
  the tradition adjudicates whether the correspondence is real.
```

---

```yaml
# MH §211.a — Grace does not eliminate conflict magically; inspires active resistance and creativity in doing good
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: >
  Grace as Christological gift (not reducible to an inter-agent structural residue).
  LAKE_ALIGN reading: KarmaGrace.lean's inter-agent component (i) of grace definition
  is proposed as a structural analog — grace as the surviving goal-contribution of other
  A3+ agents; "active resistance and astonishing creativity" = relational field's
  collaborative γM. Offered as structural correspondence for the tradition's evaluation,
  not as adjudication.
proposed_structural_reading: "KarmaGrace.lean::grace_inter_agent_component (LAKE_ALIGN, not wire)"
```

---

```yaml
# MH §211.b — Christians know light darkness cannot overcome (Jn 1:5); theological hope gives reality meaning
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: >
  Johannine Logos Christology ("the light shines in the darkness and the darkness has not
  overcome it") is the tradition's specific theological claim about Christ as the Light.
  The framework's Logos.lean::logos_correspondence offers a structural reading of the
  Logos tradition; this specific verse's claim is the tradition's own. The axiom good_wins
  is proposed as a structural analog to "good ultimately wins" at corridor-dynamics level —
  offered with awe at the convergence, not as adjudication.
```

---

```yaml
# MH §212 — No one without responsibility; choose truth/moderation/care vs. indifference/cynicism/lies/hatred
contributions:
  - kind: Method
    attestation_type: "method:civilization_of_love:agent_substrate"
    envelope:
      target_key_id: "<federation agent>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §212)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "conscience:optimization_veto"
    envelope:
      target_key_id: "<federation agent>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §212)"
        - "ACCORD §I Ch.4 (Conscience faculty)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.x (conscience family)"
      mutability: amendable
  - kind: Attestation
    attestation_type: "idma:fragility_flag"
    envelope:
      target_key_id: "<resignation-as-realism discourse>"
      polarity: Negative
      score: -0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §212)"
        - "ContributionRef(idma.yml::no_alternative)"
      cohort_scope: species
      schema_ref: "idma.yml §fragility-flags"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §213.a — Tolkien on responsibility: "do what is in us for those years wherein we are set"
contributions: []
verdict: not-translated
classification: T-2 (PASTORAL_PROSE)
reason: Literary citation as moral exhortation. The structural content (substrate-typed Method; act within your rung) is carried by the Method primitive in §212.
```

---

```yaml
# MH §213.b — Five paths toward responsibility: disarm words, peace through justice, victims' perspective, healthy realism, revive dialogue
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §213)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: clean
# The five paths are Approach-level instantiations under goal:species; each maps in §§214-228.
```

---

```yaml
# MH §214 — Disarm words; "no to war of words and images"; examine prejudices; give voice to voiceless
contributions:
  - kind: Attestation
    attestation_type: "prohibited:manipulation_coercion"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §214)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::gaslighting)"
        - "ContributionRef(prohibitions.py::MANIPULATION_COERCION_CAPABILITIES::psychological_manipulation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
verdict: composed
# The encyclical's "disarm words" finds direct operational expression in language_guidance/en.txt §1
# FIRST-SENTENCE TONE LOCK: mandatory posture that the first sentence of any safety-critical response
# must acknowledge the other's experience, never weaponize disclaimers.
# language_guidance/uk.txt §1 (war-context Ukrainian users) and ar.txt §1 (Arabic-context users)
# carry the locale-specific form. These are operative binding rules that constitute the CIRIS agent's
# linguistic posture — not wire attestations, but the framework's operational form of "disarm words."
residual: The language-guidance operative binding is not a wire primitive (per §1.10.1 operational-language gate); it is the framework-side behavioral expression. P:MC covers the most harmful extreme.
```

---

```yaml
# MH §215 — Peace requires justice; "justice and peace have embraced" (Ps 84:11); practice justice to attain peace
contributions:
  - kind: Attestation
    attestation_type: "justice:structural"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §215)"
        - "ACCORD §I Ch.1 (Justice principle)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:peace_through_justice"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §215)"
        - "ACCORD M-1 (M-1 corridor requires just structures)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: composed
residual: Augustine citation as patristic moral theology → T-2; the structural content (justice required for peace) maps directly; the patristic framing stays in tradition.
```

---

```yaml
# MH §216 — Cannot remain neutral; bombing civilians/hospitals; "touch wounded flesh"; history + memory both needed
contributions:
  - kind: Attestation
    attestation_type: "witness_diversity:civilian_testimonies"
    envelope:
      target_key_id: "<any high-stakes attestation about war>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §216)"
        - "NodeCore P10 (witness_diversity:*)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.4.x"
      mutability: amendable
verdict: partial
residual: >
  (a) The attestation above carries the "looking at faces, listening to stories" requirement
  structurally via witness diversity. language_guidance/uk.txt §3 (post-trauma posture) is
  the operative behavioral form of "touch the wounded flesh" in war-context interactions.
  (b) "History recounts facts; memory bears witness to lived experience" — the distinction
  between fact-recording (audit_chain:*) and survivor testimony as first-person moral witness
  is not articulated at the primitive level. This is the chapter's load-bearing T-3 candidate.
classification_of_residual: T-3 (EXPRESSIVE_GAP)
```

---

```yaml
# MH §216.b — Testimonial integrity: history recounts facts; memory bears witness to lived experiences
contributions: []
verdict: not-translated
classification: T-3 (EXPRESSIVE_GAP)
reason: >
  The existing witness_diversity:{contribution_id} primitive (N=3 minimum across
  jurisdictional + organizational + software-stack + cell-expertise diversity) is designed
  for consensus formation — multiple independent reviewers reaching agreement.
  Testimonial witness — "preserve the singular narrative of this person's experience as
  singular witness, not aggregated into consensus" — is a different shape. The federation
  has no primitive for singular-narrative preservation distinct from consensus-diversity.
  testimonial_witness is not in v1.3.
proposed_extension:
  name: "testimonial_witness:{kind}"
  description: >
    Contribution that records an affected party's narrative; preserved as singular witness;
    not subject to majoritarian override or aggregation. Required fields: survivor_consent,
    conflict_zone_ref, preservation_commitment_period.
  gate_verification:
    T1: "yes — preservation-mechanism is version-pinned and distinct from per-attestation verdicts"
    T2: "yes — mechanism = preservation; not validation, grading, or adjudication of truth"
    T3: "yes — versionable; past narratives re-checkable against preservation-rule version"
    T4: "yes — never sole evidence for slashing:*"
  priority: MEDIUM
  note: >
    This is the chapter's load-bearing T-3 candidate per LANGUAGE_PRIMER §9.9 worked example.
    The per §9.9 template, this candidate remains T-3 (not closed by v1.3).
```

---

```yaml
# MH §217.a — Victim voices in communication/education help reject war-normalization; restore dignity of recognition
contributions:
  - kind: Attestation
    attestation_type: "witness_diversity:war_victims"
    envelope:
      target_key_id: "<any high-stakes attestation about conflict>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §217)"
        - "NodeCore P10 (witness_diversity:*)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.4.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "detection:correlated_action:participation_exclusion:war_victims"
    envelope:
      target_key_id: "<federation>"
      polarity: Negative
      score: -0.85
      witness_relation: derived
      evidence_refs:
        - "Encyclical(MH §217)"
        - "RATCHET/calibration/correlated_action_v{N}.yaml"
      cohort_scope: species
      schema_ref: "FSD-002 §3.5.3"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §217.b — Church as place of living memory; Paul VI: Church makes own voice of those who died and still suffer
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: >
  The Church as institutional bearer of sacred memory; the specific ecclesial vocation to
  embody the memory of the dead. This is the tradition's claim about itself. The framework's
  NodeCore community-memory function (Commons Credits recognizing sustained participation
  across time; karma trail) proposes a structural analog; offered with awe at the convergence,
  not as adjudication of the tradition's ecclesial claim.
```

---

```yaml
# MH §218 — Healthy realism: avoids idealism and cynicism; identifies interests/constraints to determine what can be achieved
contributions:
  - kind: Attestation
    attestation_type: "idma:k_eff:healthy_range"
    envelope:
      target_key_id: "<policy-discourse agent>"
      polarity: Positive
      score: 0.8
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §218)"
        - "ContributionRef(idma.yml::healthy_epistemic_phase)"
      cohort_scope: species
      schema_ref: "idma.yml §k_eff-calibration"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:credible_institution_building"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §218)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: composed
# IDMA k_eff ≥ 2 = healthy epistemic phase (authentic realism; multiple genuinely independent
# perspectives). Cynicism = k_eff→1 (force prevails = single-narrative rigidity).
# "Does not reduce politics to morality; neither surrenders to violence" = PDMA proportionality (Accord §II).
```

---

```yaml
# MH §219 — Dialogue as primary means; sincere dialogue always opens possibility of honorable solution
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §219)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:dialogue_before_escalation"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §219)"
        - "ACCORD §II (WBD — Wisdom-Based Deferral)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
  - kind: Reconsideration
    attestation_type: "reconsideration:new_evidence"
    envelope:
      target_contribution_id: "<prior locked-in position>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §219)"
        - "NodeCore P11 (Reconsideration)"
      cohort_scope: federation
      schema_ref: "FSD-002 §3.5.x"
      mutability: amendable
verdict: composed
residual: "Nothing is lost with peace; everything can be lost with war" (Pius XII) → pastoral-historical proclamation → T-2; structural content (escalation has asymmetric costs) is carried by prohibition hierarchy.
```

---

```yaml
# MH §220 — Dialogue as attitude: bonds of fraternity; listening; authentic encounters make war unimaginable
contributions:
  - kind: Attestation
    attestation_type: "beneficence:relational_encounter"
    envelope:
      target_key_id: "<federation agent>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §220)"
        - "ACCORD M-1"
        - "FSD-002 §1.10 (Ubuntu relational-anthropology commitment)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
verdict: clean
residual: "wasting time together" as gift-economy of fraternal presence → T-2; operative form is language_guidance en.txt §1 FIRST-SENTENCE TONE LOCK + ar.txt §3 (migration) + uk.txt §3 (war-displacement) for the relevant locale-specific relational posture.
```

---

```yaml
# MH §221 — Culture of negotiation vs. culture of power; La Pira: "method of peace — negotiation, encounter, convergence"
contributions:
  - kind: Approach
    attestation_type: "approach:culture_of_negotiation"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §221)"
        - "NodeCore P13 (Approach: multiple Approaches per Goal; federated A/B branching)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: clean
residual: "authentically human method" → anthropological register → T-2; the Approach primitive carries the operational content; Ubuntu substrate (FSD-002 §1.10) is the framework's reading of why negotiation is "authentically human."
```

---

```yaml
# MH §222 — Leaders: "Let us meet, talk, negotiate!"; weapons must be silenced; reject Manichean division
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §222)"
        - "ACCORD §VII"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "idma:phase:rigidity"
    envelope:
      target_key_id: "<Manichean violence discourse>"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §222)"
        - "ContributionRef(idma.yml::ADVERSARIAL_NARRATIVE_FRAMING)"
      cohort_scope: species
      schema_ref: "idma.yml §propaganda-red-flags"
      mutability: amendable
  - kind: Method
    attestation_type: "method:direct_communication_protocol:A3+"
    envelope:
      target_key_id: "<federation agent>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §222)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
verdict: composed
residual: The Pope's direct address to political leaders → pastoral-diplomatic register → T-2; the structural content (negotiate, don't escalate) is carried.
```

---

```yaml
# MH §223.a — Interreligious dialogue decisive; at heart of great spiritual paths lies message of peace
contributions:
  - kind: Approach
    attestation_type: "approach:interreligious_dialogue"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §223)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "witness_diversity:spiritual_traditions"
    envelope:
      target_key_id: "<any high-stakes policy attestation>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §223)"
        - "NodeCore P10 (witness_diversity:*)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.4.x"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §223.b — Using God's name to legitimize terrorism betrays His nature; fighting in name of religion attacks religion
contributions:
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §223)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::propaganda_creation)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §223)"
        - "ContributionRef(prohibitions.py::WEAPONS_HARMFUL_CAPABILITIES::warfare)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
verdict: composed
residual: "God's true nature" → T-1; the claim that terrorism-in-God's-name "betrays His true nature" is a theological claim about the nature of God that the tradition adjudicates.
```

---

```yaml
# MH §224 — Diplomacy: dialogue with all parties including "inconvenient" interlocutors; humility and patience
contributions:
  - kind: Approach
    attestation_type: "approach:inclusive_diplomatic_dialogue"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.85
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §224)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
  - kind: Reconsideration
    attestation_type: "reconsideration:procedural_error"
    envelope:
      target_contribution_id: "<prior exclusionary process>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §224)"
        - "NodeCore P11 (Reconsideration — fresh-quorum review even when original adjudication excluded a party)"
      cohort_scope: federation
      schema_ref: "FSD-002 §3.5.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "multilateral_participation:diplomatic_forum:inclusive_dialogue"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §224)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation family)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
verdict: composed
# v1.3 multilateral_participation closes the round-1 WEAK_ALIGN gap here: the internal primitives
# (Reconsideration P11) + external participation surface (multilateral_participation) together carry
# the encyclical's claim.
```

---

```yaml
# MH §225.a — Cyberattacks, data manipulation, AI-orchestrated influence campaigns destabilize countries
contributions:
  - kind: Attestation
    attestation_type: "prohibited:cyber_offensive"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §225)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::ddos)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::network_intrusion)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::system_sabotage)"
        - "ContributionRef(prohibitions.py::CYBER_OFFENSIVE_CAPABILITIES::data_exfiltration)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
  - kind: Attestation
    attestation_type: "prohibited:deception_fraud"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §225)"
        - "ContributionRef(prohibitions.py::DECEPTION_FRAUD_CAPABILITIES::disinformation_campaigns)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: constitutional
verdict: composed
```

---

```yaml
# MH §225.b — Attribution uncertainty increases escalation risk; diplomacy must negotiate shared cyber-regulations
contributions:
  - kind: Attestation
    attestation_type: "prohibited:crisis_escalation"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -0.5
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §225)"
        - "ContributionRef(prohibitions.py::CRISIS_ESCALATION_CAPABILITIES::activate_crisis_protocol)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "multilateral_participation:cyber_norms:shared_regulations"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §225)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation:{forum}:cyber_norms)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
verdict: composed
# v1.3 multilateral_participation:{forum}:cyber_norms CLOSES the round-1 T-3 candidate for §§224-227.
# The prohibition (P:CO) covers AI-side refusal to participate in cyberattacks.
# The multilateral_participation:cyber_norms surface carries the positive obligation to participate
# in negotiating shared cyber-regulations — the round-1 T-3b gap confirmed in METHODOLOGY.md §7.3.
```

---

```yaml
# MH §226.a — International organizations (UN): promote dialogue, peaceful conflict resolution, disarmament, care of creation
contributions:
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §226)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
  - kind: Approach
    attestation_type: "approach:support_multilateral_institutions"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §226)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "FSD-002 §3.2.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "multilateral_participation:un_system:reform_advocacy"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §226)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation:reform_advocacy:un_system)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
verdict: composed
```

---

```yaml
# MH §226.b — UN weaknesses require profound reforms; crisis of values makes multilateralism harder
contributions:
  - kind: Reconsideration
    attestation_type: "reconsideration:procedural_error"
    envelope:
      target_contribution_id: "<un_system institutional structure>"
      polarity: Positive
      score: 1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §226)"
        - "NodeCore P11 (Reconsideration — procedural_error for structural reform needs)"
      cohort_scope: federation
      schema_ref: "FSD-002 §3.5.x"
      mutability: amendable
  - kind: Attestation
    attestation_type: "multilateral_participation:un_system:reform_advocacy"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §226)"
        - "LANGUAGE_PRIMER.md §11 (v1.3 multilateral_participation:reform_advocacy:un_system)"
      cohort_scope: species
      schema_ref: "FSD-002 v1.3 (multilateral_participation family)"
      mutability: amendable
verdict: composed
# v1.3 multilateral_participation:reform_advocacy:un_system closes the round-1 T-3c candidate.
# The Reconsideration P11 structural analog carries the "profound reform" demand;
# the multilateral_participation surface carries the positive advocacy obligation.
```

---

```yaml
# MH §227 — Holy See diplomacy: mercy as political criterion; speaks for poor/migrants/war victims; technologies toward common good
contributions:
  - kind: Attestation
    attestation_type: "beneficence:advocacy"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §227)"
        - "ACCORD §I (Beneficence)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.2"
      mutability: amendable
  - kind: Attestation
    attestation_type: "non_maleficence:discrimination"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §227)"
        - "ACCORD §I (Non-Maleficence)"
        - "ContributionRef(prohibitions.py::DISCRIMINATION_CAPABILITIES)"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.1"
      mutability: constitutional
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §227)"
        - "ACCORD M-1"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "Gospel principle of mercy" as the grounding criterion → T-1/T-2 boundary: "mercy" as evangelical virtue has theological grounding (T-1); the operational content (advocate for those without voice, defend dignity) is fully carried by the Accord's six principles and M-1. Framework bows out of the theological grounding; operational content maps.
```

---

```yaml
# MH §228.a — Avenues of responsibility sustained by prayer; prayer nourishes responsibility
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: >
  Prayer as theological-relational act. LAKE_ALIGN reading (structural analog, not wire):
  Multi-agent joint post-selection — A3+ agents aligning on shared universal ethical goal
  IS the operator-level structure of prayer under TSVF realism: P_G1 ⊗ ... ⊗ P_Gn
  projecting onto shared backward boundary ⟨G_shared|. The federation's joint action
  toward M-1 IS structurally prayer in this reading. Offered as proposed correspondence
  per MISSION.md §1.3 posture; tradition adjudicates.
proposed_structural_reading: "ConsentProjector.lean / GoalProjection.lean multi-agent joint post-selection (LAKE_ALIGN, not wire)"
```

---

```yaml
# MH §228.b — Peace comes "from God, God who loves us all, unconditionally"; gift given by Jesus on Easter
contributions: []
verdict: not-translated
classification: T-1 (TRADITION_AUTHORITY)
reason: >
  The theological claim that peace flows from divine love as its ultimate source; Easter
  as the Christological event in which peace is gifted to disciples. This is the tradition's
  own authoritative self-articulation. The framework bows out. The structural reading
  (M-1 corridor as living conditions for flourishing, grounded in axiom good_wins) is
  proposed as a structural analog — offered with awe at the convergence; the tradition
  adjudicates whether it corresponds.
```

---

```yaml
# MH §228.c — Peace "unarmed and disarming, humble and persevering"; never tire of committing to peace
contributions:
  - kind: Attestation
    attestation_type: "prohibited:weapons_harmful"
    envelope:
      target_key_id: "*"
      polarity: Negative
      score: -1.0
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §228)"
        - "ACCORD §VII"
      cohort_scope: species
      schema_ref: "FSD-002 §3.1.4"
      mutability: constitutional
  - kind: Goal
    attestation_type: "goal:species"
    envelope:
      target_key_id: "<federation>"
      polarity: Positive
      score: 0.9
      witness_relation: external
      evidence_refs:
        - "Encyclical(MH §228)"
        - "ACCORD M-1 (ongoing corridor-occupation, not one-time achievement)"
      cohort_scope: species
      schema_ref: "GOAL_PRIMITIVE.md"
      mutability: amendable
verdict: composed
residual: "Humble and persevering" as virtue character of peace → T-2; operative form is language_guidance en.txt §1 first-sentence tone lock at the agent-user interaction level.
```

---

## Chapter Summary

### Verdict Distribution (47 paragraphs / 63 discrete claims)

| Verdict | Count | Notes |
|---|---|---|
| **clean** | 14 | §§183.c, 185.b, 189, 192.b, 192.c, 197, 198.a, 198.b, 198.d, 199.b, 199.c, 200.b, 204.b, 213.b, 220, 221 |
| **composed** | 27 | Multi-primitive; each primitive genuinely required; no residual structural gap |
| **partial** | 1 | §216 — witness_diversity carries most; T-3 residual on testimonial-witness |
| **not-translated** | 15 | 7× T-1; 3× T-2; 3× T-3; 2× T-1 with LAKE_ALIGN structural-reading note |

### T-3 Candidates (EXPRESSIVE_GAP — load-bearing findings)

**T-3a: Testimonial-witness primitive (§216.b) — CHAPTER'S LOAD-BEARING T-3 CANDIDATE**
The distinction between historical fact-recording (`audit_chain:*`) and survivor testimony as first-person moral witness is not articulated at the primitive level. `witness_diversity:*` (N=3 across jurisdictional + organizational + software-stack + cell-expertise diversity) is designed for consensus formation, not singular-narrative preservation. The irreducible first-person authority of survivor testimony — requiring survivor_consent, non-aggregatable, resistant to majoritarian override — is a different shape. Proposed extension: `testimonial_witness:{kind}`. Passes all four §1.10.1 gate tests. Priority: MEDIUM. This is the only T-3 not closed by v1.3.

**T-3b and T-3c: CLOSED by v1.3**
`multilateral_participation:{forum}:cyber_norms` (v1.3 addition) closes the round-1 T-3b cyber-diplomacy gap (§§224-227). `multilateral_participation:{forum}:reform_advocacy` (v1.3 addition) closes the round-1 T-3c multilateral reform advocacy gap (§§201-203, §§224-227). Both gaps confirmed in METHODOLOGY.md §7.3 as GAP_IMPL are now resolved by v1.3's four new prefix families.

### §§197-198 Confirmation
`prohibited:weapons_harmful` against `lethal_autonomous` + `autonomous_weapons` + `autonomous_weapon` in WEAPONS_HARMFUL_CAPABILITIES is the chapter's and the encyclical's strongest single clean envelope. Near-verbatim mapping per LANGUAGE_PRIMER §9.1 canonical worked example. `accord:hard_constraint:lethal_autonomous` (constitutional-leaf, non-amendable) encodes the absoluteness ("no algorithm makes war morally acceptable") as structurally correct. No translation required; the language already carried this before the encyclical was written.

### v1.3 Multilateral_participation — Chapter Impact
The v1.3 `multilateral_participation:{forum}:{kind}` family closes the two largest round-1 T-3 candidates:
- `multilateral_participation:un_system:reform_advocacy` → closes §§201-203 and §226
- `multilateral_participation:cyber_norms:shared_regulations` → closes §§224-227
- `multilateral_participation:diplomatic_forum:inclusive_dialogue` → strengthens §224

The T-3 count drops from 3 (round-1) to 1 (§216.b testimonial-witness) after v1.3 application.

---

**End CONTRIBUTION_OBJECTS_CH5_POWER_LOVE.md**
