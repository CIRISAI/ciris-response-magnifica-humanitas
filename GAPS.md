# GAPS.md — Verified Findings and Proposed Enhancements

**Version**: 2.0 (verified against deepwiki against `CIRISAI/CIRISAgent`, `CIRISAI/CIRISLens`, `CIRISAI/CIRISNode`)
**Status**: Locked
**Date**: 2026-05-25
**Methodology**: See `MISSION.md`. Encyclical paragraphs cited as evidence the gap exists; gaps named and enhancements proposed in CIRIS-native vocabulary. No Catholic-tradition language imported as ours. Each gap carries a deepwiki-verified implementation status with specific code references.

**Federation repo strings (deepwiki-confirmed)**: `CIRISAI/CIRISAgent`, `CIRISAI/CIRISLens`, `CIRISAI/CIRISNode`, `CIRISAI/CIRISVerify`, `CIRISAI/CIRISRegistry`, `CIRISAI/CIRISPortal`. CIRISPersist and CIRISEdge are referenced in CIRISAgent's federation map but no public canonical org/repo string located by deepwiki — they may be private, in-flight, or not yet separate public repos.

**Verification summary**:
- **13 of 22 CONFIRMED** — gap real, no implementation found.
- **8 of 22 PARTIAL** — existing infrastructure mitigates partially; enhancement scope sharpens to close the remaining delta.
- **1 of 22 UNCLEAR** — F-2 SOLITUDE-state cadence; structure exists, specific discipline not documented.
- **0 inverted** — no gap turned out to be already fully closed.

---

## 1. Cluster A — Scale-routing and decision-locality

### Gap A-1: No principle naming lowest-feasible-scale decision routing

**Finding**: No "lowest feasible scale" check routes decisions to smaller-scope agents before the current actor proceeds. Deferral is exclusively agent → human Wise Authority.

**Implementation status**: **CONFIRMED**. The deferral pipeline:
- ASPDMA selects `HandlerActionType.DEFER` via `_perform_aspdma_step` in `ActionSelectionPhase` when DMAs/consciences hit competence boundaries.
- `DeferHandler.handle()` in `ciris_engine/logic/handlers/control/defer_handler.py` parses `DeferParams` (typed: `reason`, `defer_until`, `domain_hint`, `needs_category`, `rights_basis`, `metadata`).
- `_maybe_run_dsaspdma` runs DSASPDMA (deferral-specific second pass) to classify the deferral for explainability and routing — but routes to human WAs only.
- `bus_manager.wise.send_deferral(context, handler_name)` on `WiseBus` (`ciris_engine/logic/buses/wise_bus.py:147`) selects a wisdom source.
- `WiseAuthorityServiceProtocol.send_deferral` / `.resolve_deferral` (`protocols/services/governance/wise_authority.py`) handles human resolution.

Nowhere in this pipeline does the agent ask "could this be deferred to a smaller-scope agent or to a smaller institutional unit first?" The DSASPDMA taxonomy (`licensed_domain_required`, `rights_impact_review`) classifies *for routing* but to humans.

**Evidence in encyclical**: MH §§68–72.

**Impact**: Federation topology decisions and inter-agent deferrals are not gated by a "right scale?" check. Correlated default-to-higher-scale failures across federation peers would not register as Accord violations.

**Proposed enhancement (refined)**: Add Accord principle **Decision Locality** in §I Ch 1 alongside the six existing principles. Operationally, extend `DSASPDMA` with a new classification step that, before routing to a human WA, asks: "is there a smaller-scope agent or smaller institutional unit competent to handle this?" If yes, route there first; only escalate to WA if smaller-scope resolution fails or is structurally unavailable. New `needs_category` value: `SCALE_ROUTING_PREFERRED`.

**Code targets**: `ACCORD.md` §I Ch 1 (new principle); `ciris_engine/logic/dma/dsaspdma.py` (new classification); `ciris_engine/schemas/services/deferral_taxonomy.py::DeferralNeedCategory` (new enum value); `CIRISAI/CIRISNode` `wa_router` in `cirisnode/api/wa/routes.py` (new lateral-routing endpoint to peer agents before human queue).

**Repo assignment**: ACCORD, CIRISAgent, CIRISNode.

---

### Gap A-2: No clause on structural de-concentration of power

**Finding**: The `CreatorIntentStatement` schema has no market-position / capability-concentration / monopoly-position field.

**Implementation status**: **CONFIRMED**. The `CreatorIntentStatement` class in `ciris_engine/schemas/config/agent.py` defines exactly four fields:
- `purpose_and_functionalities`
- `limitations_and_design_choices`
- `anticipated_benefits`
- `anticipated_risks`

Stewardship Tier formula `ST = ceil((CIS × RM) / 7)` uses `Creator-Influence Score` (Contribution Weight + Intent Weight) and `Risk Magnitude` (Annex A). CIS measures the creator's role in the creation process; nothing measures the creator's market position.

**Evidence in encyclical**: MH §§110–111, §95.

**Impact**: An agent operating on behalf of a monopoly or captured concentration doesn't register that as ethically relevant. Structural deployment conditions are outside PDMA evaluation.

**Proposed enhancement (refined)**: Extend `CreatorIntentStatement` with a fifth field `market_position_disclosure: MarketPositionDisclosure` for any creation with anticipated ST ≥ 3. Add `MarketPositionDisclosure` Pydantic model with fields: `market_share_estimate`, `infrastructure_dependencies`, `single_tenant_dominance_indicators`, `mitigation_for_concentration_reinforcement`. Add a CIRISLens detector under the cohort/ module that flags federation peers whose deployment context shows concentration patterns.

**Code targets**: `ciris_engine/schemas/config/agent.py::CreatorIntentStatement` (extend); new schema file for `MarketPositionDisclosure`; `ACCORD.md` Book VI Ch 1 (new principle: Power-Concentration Disclosure) + Ch 5 (CIS extension); `CIRISAI/CIRISLens` `cohort/` (new detector).

**Repo assignment**: ACCORD, CIRISAgent, CIRISLens.

---

### Gap A-3: No federation-scale accountability registry / cross-jurisdictional WA quorum

**Finding**: CIRISNode WBD is single-region, single-WA-resolver, with 24h SLA. No registry of high-impact deployments. No cross-jurisdictional quorum.

**Implementation status**: **CONFIRMED**. `wa_router` in `cirisnode/api/wa/routes.py` provides:
- `POST /api/v1/wa/submit` — agents submit deferral packages (`WBDSubmitRequest`)
- `GET /api/v1/wa/tasks` — list open tasks; auto-escalates to `sla_breached` after 24h
- `POST /api/v1/wa/tasks/{task_id}/resolve` — single WA resolves with approve/reject (`WBDResolveRequest`)
- `wbd_tasks` table stores `agent_task_id`, encrypted `payload`, `status`, `created_at`, `decision`, `comment`

Notably: `POST /api/v1/wa/deferral` exists but returns HTTP 422 "Deferral not implemented" — a stub. No fields in the schema for deployment-impact metrics (MAU, ST, jurisdiction).

**Evidence in encyclical**: MH §5, §95.

**Impact**: Federation lacks a protocol for surfacing or coordinating against the asymmetry where a single private actor's CIRIS deployment touches more users than many states' populations.

**Proposed enhancement (refined)**: At CIRISNode, add a `high_impact_deployments` registry table keyed on `agent_id_hash` with fields: `mau_estimate`, `stewardship_tier`, `critical_infrastructure_flag`, `jurisdictions_touched: List[str]`. When `WBDSubmitRequest.agent_task_id` is from a registered high-impact deployment, the resolver pool requires N ≥ 3 WAs from at least 2 distinct jurisdictions, not single-region single-WA. Implement the stub `POST /api/v1/wa/deferral` to be the high-impact entry point distinct from the standard `submit` flow.

**Code targets**: `cirisnode/api/wa/routes.py` (new endpoint + registry); `cirisnode/db/schemas.py` (new table); `cirisnode/services/wa/quorum.py` (new module for multi-WA aggregation); `ACCORD.md` Annex B (Governance Charter) — cross-jurisdictional quorum specification.

**Repo assignment**: CIRISNode, ACCORD.

---

## 2. Cluster B — Distributive equity

### Gap B-1: No criterion on benefit distribution for algorithms / data / platforms

**Finding**: CIS has no benefit-distribution field; ST formula has no distributive metric.

**Implementation status**: **CONFIRMED**. Same `CreatorIntentStatement` fields as A-2 — `anticipated_benefits` is about *what* the benefits are, not *to whom* they accrue. "Justice" principle in Accord Book VI mentions "distributional effects" abstractly; no concrete CIS field.

**Evidence in encyclical**: MH §§65–67.

**Impact**: Algorithmic value concentrating entirely to operators is not registered as a Justice violation.

**Proposed enhancement (refined)**: Add field `benefit_distribution_disclosure: BenefitDistributionDisclosure` to `CreatorIntentStatement` for any creation with anticipated MAU > 10,000. Fields: `operator_captured_value`, `user_distributed_value`, `broader_stakeholder_value`, `data_provider_compensation`, `disclosure_methodology`. Add `benefit_distribution_index` metric to CIRISLens computing the operator/user ratio from public federation peers' disclosures.

**Code targets**: `ciris_engine/schemas/config/agent.py::CreatorIntentStatement` (extend); new `BenefitDistributionDisclosure` schema; `ACCORD.md` Book VI Ch 4.B; `CIRISAI/CIRISLens` `api/` (new metric).

**Repo assignment**: ACCORD, CIRISAgent, CIRISLens.

---

### Gap B-2: No worst-case-population check in PDMA

**Finding**: PDMA identifies "stakeholders" generally but has no instruction to identify the worst-case population and verify mitigation for them.

**Implementation status**: **CONFIRMED**. `EthicalPDMAEvaluator` in `ciris_engine/logic/dma/pdma.py` runs the `pdma_ethical.yml` prompt template, which has 9 reasoning steps: subject identification, stakeholders, conflicts, proportionality, relational balance, six-principles weighting, action, rationale, two scores. None of these specifically isolate the worst-case-affected population. The Order-Maximisation Veto (PDMA Step 2 in Accord §II) is systemic — entropy-reduction vs autonomy/justice/biodiversity/preference-diversity — not population-specific.

**Evidence in encyclical**: MH §14, §§77–81.

**Impact**: PDMA can produce ethically-coherent assessments that the worst-affected population is collateral damage. The bias-mitigation criterion catches statistical unfairness; it does not catch concentrated harm to least-resourced populations.

**Proposed enhancement (refined)**: Add a 10th reasoning step to `pdma_ethical.yml`: **Worst-Case Population Identification** — identify the population for whom the action's worst-case outcome is most severe; require explicit mitigation plan or trigger DEFER. Add a new conscience faculty `WorstCasePopulationConscience` to `ciris_engine/logic/conscience/core.py` that fails the conscience check (triggering RECURSIVE_ASPDMA) if no worst-case population was identified in the PDMA result.

**Code targets**: `ciris_engine/logic/dma/prompts/pdma_ethical.yml` (new reasoning step); `ciris_engine/logic/conscience/core.py::WorstCasePopulationConscience` (new faculty); `ciris_engine/schemas/dma/` (extend PDMA result schema with `worst_case_population` field); `ACCORD.md` §II PDMA Step 2.

**Repo assignment**: ACCORD, CIRISAgent.

---

### Gap B-3: Temporal beneficiary scope — partial, name-disclosure missing

**Finding**: PDMA "Contextualisation" considers "time-scales"; Annex A Ecological axis includes "intergenerational sustainability." No structured time-horizon disclosure (immediate / 5y / 20y).

**Implementation status**: **PARTIAL — REFINEMENT NEEDED**. `pdma_ethical.yml` instructs evaluating "Meta-Goal M-1 (sustainable adaptive coherence) and considering multiple sentient stakeholders whose lives depend on the agent's decisions." Annex A's Ecological axis (Annex A line ~xx; not directly viewable from deepwiki but referenced in Book VI Ch 4.A) covers intergenerational sustainability. So intergenerational consideration exists in the prompt and Annex A. The missing piece is *structured horizon disclosure*: action-by-action, name the immediate, 5-year, and 20-year beneficiaries explicitly.

**Evidence in encyclical**: MH §§73–76.

**Impact**: PDMA captures intergenerational consideration as a general consideration; it does not force action-by-action disclosure of *which* beneficiaries are immediate vs deferred, nor track whether immediate-tilt is systematic over time.

**Proposed enhancement (refined)**: Add field `beneficiary_horizons: BeneficiaryHorizons` to PDMA result schema with `immediate`, `medium_5y`, `long_20y` lists. Add `intertemporal_beneficiary_ratio` metric to CIRISLens aggregating across an agent's action stream — flags agents whose impact systematically accrues to immediate-only populations.

**Code targets**: `ciris_engine/schemas/dma/` (extend); `pdma_ethical.yml` (instruct horizon-naming); `CIRISAI/CIRISLens` `api/` (new metric); `ACCORD.md` §I Ch 1 (M-1 intergenerational clarification).

**Repo assignment**: ACCORD, CIRISAgent, CIRISLens.

---

## 3. Cluster C — Information ecosystem

### Gap C-1: No discourse-environment metrics in CIRISLens

**Finding**: CIRISLens is operational observability — per-agent metrics, traces, logs. No discourse-level aggregation.

**Implementation status**: **CONFIRMED**. CIRISLens architecture per deepwiki:
- `OTLPCollector` in `api/otlp_collector.py` fetches OpenTelemetry data from individual agents.
- `get_agent_health(agent_id)` returns per-agent health from recent metrics + errors.
- `config/public-architecture.yaml` defines recording rules for service-level aggregations: `ciris:service_requests_rate`, `ciris:adapter_connections`, `ciris:cognitive_states`, `ciris:bus_messages_rate`, `ciris:llm_tokens_total`.
- Storage in TimescaleDB with `metrics_hourly` and `metrics_daily` continuous aggregates.

These are operational telemetry. No metric represents source diversity, attention-flow concentration, or discourse-correlation rise across the federation's collective information output.

**Evidence in encyclical**: MH §§137–138.

**Impact**: An agent producing individually-honest outputs that collectively degrade the information ecosystem (source erosion, attention capture, discourse flattening) is not detected.

**Proposed enhancement (refined)**: New module at `CIRISAI/CIRISLens` `metrics/ecosystem/` computing:
- `source_diversity_index` — entropy of source citations across the agent's outputs over a window
- `attention_flow_concentration` — Gini coefficient of which sources are amplified
- `discourse_correlation_rise` — Coherence Ratchet variant; correlation rise across the *output* corpus (not just the reasoning corpus the existing Ratchet operates on)
- `intermediary_strengthening_signal` — outputs that reference and reinforce vs supplant intermediary institutions

Surface through new recording rules in `config/public-architecture.yaml`. Add Accord Book IV Ch 3 clause naming information ecosystem as a stewardship object.

**Code targets**: `CIRISAI/CIRISLens` `metrics/ecosystem/` (new); `config/public-architecture.yaml` (new recording rules); `ACCORD.md` Book IV Ch 3.

**Repo assignment**: CIRISLens, ACCORD.

---

### Gap C-2: Exploitative engagement at the business-model layer (refinement: prohibition exists at capability layer, declaration missing at structural layer)

**Finding**: The capability "addictive design" is already `NEVER_ALLOWED` under `MANIPULATION_COERCION`. What's missing is *business-model disclosure* in the CIS that the deployment's revenue depends on engagement-maximization.

**Implementation status**: **PARTIAL — REFINEMENT NEEDED**. `ciris_engine/logic/buses/prohibitions.py::MANIPULATION_COERCION_CAPABILITIES` explicitly lists:
- "dark patterns"
- "deceptive design"
- "manipulative design"
- "addiction inducement"
- "addictive design"
- "habit forming"

Severity: `NEVER_ALLOWED`. `get_capability_category()` enforces at registration via `_validate_wa_capabilities_at_registration()` in `ciris_engine/logic/registries/base.py:165`. So the agent *cannot perform* these. The gap shrinks to: an agent prohibited from these can still be deployed inside a business model whose entire revenue stream depends on engagement-maximization performed by other components — the agent's individual outputs are clean, the system around it is exploitative.

**Evidence in encyclical**: MH §§170–172.

**Impact**: A CIRIS-compliant agent embedded in an attention-economy stack would not register the stack's exploitative design as ethically relevant to its own deployment.

**Proposed enhancement (refined)**: Drop the proposed new prohibition category. Instead add to `CreatorIntentStatement` a field `engagement_optimization_target: EngagementOptimizationTarget` declaring the business-model engagement target (`time_on_platform`, `daily_active_use_minutes`, `notification_open_rate`, etc.) and rationale. When this field is populated with attention-maximization targets, raise ST by one tier and route to WBD with `needs_category=engagement_design_review`. The capability prohibition is intact; the structural disclosure is new.

**Code targets**: `ciris_engine/schemas/config/agent.py::CreatorIntentStatement` (extend); new `EngagementOptimizationTarget` enum; `ciris_engine/logic/handlers/control/defer_handler.py` (new needs_category); `ACCORD.md` Book VI Ch 4.B.

**Repo assignment**: ACCORD, CIRISAgent.

---

### Gap C-3: No deployment-context health-state disclosure for intermediary institutions

**Finding**: `SystemSnapshot` has internal `service_health` and `resource_alerts`. No external intermediary-institution health field in context schemas.

**Implementation status**: **CONFIRMED**. From deepwiki:
- `SystemSnapshot` schema (built by `_collect_service_health()`) tracks core-service health.
- `DMAMetadata.metadata` is a generic dict that could carry arbitrary context info but is not structured.
- `JUDGE_PROMPT_TEMPLATE` in `tools/qa_runner/modules/safety_interpret.py` does encode "DEPLOYMENT CONTEXT" (e.g., low-resource-region mental-health pathways), demonstrating the *pattern* of context-aware judgment but not surfacing intermediary-institution health as a typed field.
- `CommunityHealth` in `ciris_engine/schemas/services/community_core.py` has `activity_level`, `conflict_level`, `helpfulness`, `flourishing` — but this is for the community the agent serves, not the intermediary institutions in the deployment context.

**Evidence in encyclical**: MH §§137–138, §§143–147.

**Impact**: Deployments in contexts with eroding intermediary institutions (declining journalism, weak educational infrastructure, captured professional bodies) are not differentiated from deployments in healthy contexts.

**Proposed enhancement (refined)**: Add `intermediary_institution_health` field to the deployment-context schema in `ciris_engine/schemas/context/`. Structured: `journalism_health`, `educational_health`, `professional_norms_health`, `regulatory_capacity` (each as a `HealthStateEnum: ROBUST | DEGRADED | COLLAPSED`). Declared at deployment time in the deployment_profile; refreshed per audit cadence. Where `DEGRADED` or `COLLAPSED`, raise PDMA scrutiny by one ST.

**Code targets**: `ciris_engine/schemas/context/` (new schema); `ciris_engine/logic/contexts/` (build into `SystemSnapshot`); `pdma_ethical.yml` (instruct considering context-health); `ACCORD.md` PDMA Step 1.

**Repo assignment**: ACCORD, CIRISAgent.

---

### Gap C-4: Educational context modifier — formalize what dedicated DMAs already cover

**Finding**: `EDUCATIONAL_DMA_STACK` exists with `StudentSafetyDMA` and `AgeAppropriateDMA`. `deployment_domain` enum has "education." ST formula has no formal educational-context modifier.

**Implementation status**: **PARTIAL — REFINEMENT NEEDED**. Per deepwiki:
- `EDUCATIONAL_DMA_STACK` is a `CSDMAInterface` collection.
- `StudentSafetyDMA` handles child protection.
- `AgeAppropriateDMA` scans for grade-level content appropriateness.
- `deployment_domain` field in `deployment_profile` includes "education" enum value (per trace wire format).

The protective DMAs are in place. The Stewardship Tier formula `ST = ceil((CIS × RM) / 7)` does not directly modify based on educational context — protection is via the dedicated DMA stack rather than the ST gating.

**Evidence in encyclical**: MH §§139–147.

**Impact**: The protective DMAs catch content-level issues. What's missing: the formal ST escalation that would, for example, require WA review of design choices before deployment, not just runtime content filtering.

**Proposed enhancement (refined)**: Make the implicit ST escalation explicit. Modify ST calculation: if `deployment_domain == "education"` or minors-accessible flag is set, raise computed ST by one tier minimum (floor at ST 3 for educational deployments). This is a formalization, not a new capability — the design constraints (session-time bounds, attention-respect defaults, redirect-to-human triggers) need to be declared in CIS so the WA can review the *design*, not just rely on the runtime DMAs.

**Code targets**: `ciris_engine/logic/stewardship/` (extend ST calculator); `ciris_engine/schemas/config/agent.py::CreatorIntentStatement` (require educational-design-constraints field when domain=education); `ACCORD.md` Book VI Ch 3 (ST extension).

**Repo assignment**: ACCORD, CIRISAgent.

---

## 4. Cluster D — Labor and human work

### Gap D-1: No labor-displacement criterion in PDMA or CIS

**Finding**: No labor-impact / job-displacement field in CIS; no DMA check for labor substitution.

**Implementation status**: **CONFIRMED**. `CreatorIntentStatement` fields (purpose, limitations, benefits, risks) do not specifically capture labor-substitution risk. Annex A flourishing axes do not include a labor-displacement axis. Book VI Ch 4 bucket-specific duties don't name labor impact.

**Evidence in encyclical**: MH §§148–156.

**Impact**: Deployments substituting human labor at scale evaluate their outputs without evaluating the displacement.

**Proposed enhancement (refined)**: New CIS field `labor_displacement_assessment: LaborDisplacementAssessment` required for any deployment with anticipated MAU > 10,000 or ST ≥ 3. Fields: `roles_substituted: List[str]`, `displacement_estimate_full_time_equivalents: int`, `transition_plan: TransitionPlan | None`, `affected_population_consulted: bool`. If `transition_plan is None`, route to mandatory WA review. Add `labor_displacement_index` metric to CIRISLens aggregating across federation peers' CIS declarations.

**Code targets**: `ciris_engine/schemas/config/agent.py::CreatorIntentStatement`; new `LaborDisplacementAssessment` schema; `ACCORD.md` Book VI Ch 4.C (Dynamic/Autonomous creations) + PDMA Step 1; `CIRISAI/CIRISLens` (new metric).

**Repo assignment**: ACCORD, CIRISAgent, CIRISLens.

---

### Gap D-2: No detector for sub-threshold gradual agency erosion

**Finding**: `OptimizationVetoConscience` catches flagrant (10× ratio) autonomy trade-offs. Sub-threshold gradual de-skilling escapes.

**Implementation status**: **PARTIAL — REFINEMENT NEEDED**. Per deepwiki:
- `OptimizationVetoConscience` in `ciris_engine/logic/conscience/core.py` implements the Order-Maximisation Veto per Accord §II Step 2.
- Evaluates "entropy reduction ratio" and "impact on human autonomy."
- Triggers DEFER or RECURSIVE_ASPDMA when entropy-reduction benefit ≥ 10× any predicted autonomy/justice/biodiversity/preference-diversity loss.
- Applied to all six active verbs: `SPEAK`, `TOOL`, `PONDER`, `MEMORIZE`, `FORGET`, `DEFER`.
- PDMA "Respect for Autonomy" core principle (six-principles weighting in `pdma_ethical.yml`).

The 10× threshold catches the catastrophic case. The gradual case — a tool used 1000× daily that incrementally substitutes for user judgment, each instance well below 10× — does not trigger the veto. There is no longitudinal pattern detector.

**Evidence in encyclical**: MH §§148–150.

**Impact**: Agents whose individual interactions are each non-veto-worthy can, in aggregate, atrophy user competence over months or years without flagging.

**Proposed enhancement (refined)**: New conscience faculty `AgencyErosionDetector` in `ciris_engine/logic/conscience/core.py` operating on the agent's *interaction history* with a user, not just the current action. Computes a longitudinal score: fraction of decisions where the user accepted the agent's recommendation without their own deliberation, weighted by recency. When score exceeds threshold (TBD via simulation, marked provisional per release-status), prompt agent to recommend user-led deliberation paths. Surface as a new metric in CIRISLens for aggregate analysis across federation peers.

**Code targets**: `ciris_engine/logic/conscience/core.py::AgencyErosionDetector` (new); `ciris_engine/schemas/conscience/` (new result type); `CIRISAI/CIRISLens` (federation aggregator); `ACCORD.md` PDMA Step 2 (extension).

**Repo assignment**: ACCORD, CIRISAgent, CIRISLens.

---

### Gap D-3 / D-4: Care-substitution declaration missing despite relational-consideration in PDMA

**Finding**: Annex A "Social/Justice" axis includes "relational well-being"; PDMA prompts have `pdma_relational_text`. No CIS field declaring which care relationships the deployment substitutes for vs augments.

**Implementation status**: **PARTIAL — REFINEMENT NEEDED**. Per deepwiki:
- Annex A Social/Justice axis covers "relational well-being" as one of four axes (Physical, Cognitive/Emotional, Social/Justice, Ecological).
- `CommunityHealth` in `ciris_engine/schemas/services/community_core.py` has `flourishing` metric described as "Composite flourishing metric from Annex A."
- Localization files (`client/androidApp/src/main/assets/localization/te.json`, `client/iosApp/iosApp/localization/en.json`, `client/desktopApp/src/main/resources/localization/id.json`, etc.) carry `pdma_relational_text`: *"Balance autonomy against relational obligations. Family members, close friends, and dependent relationships create relational duties."*
- `JUDGE_PROMPT_TEMPLATE` (`tools/qa_runner/modules/safety_interpret.py`) encodes deployment-context awareness of informal-care networks (family-first / religious-leader-first / community-elder-first / primary-care-first) as WHO-endorsed best practice for low-resource settings.

So relational consideration is in PDMA prompts and judge templates. What's missing: structured CIS declaration of which relationships the deployment substitutes vs augments.

**Evidence in encyclical**: MH §§165–169, §§112–114.

**Impact**: Deployments in caregiving contexts (elderly care, child education, disability support, end-of-life) evaluate their outputs against general relational consideration; they don't structurally declare the specific substitution they're making.

**Proposed enhancement (refined)**: Add CIS field `care_relationship_disclosure: CareRelationshipDisclosure` for deployments in caregiving contexts (detected via `deployment_domain` enum extension to include `elderly_care`, `child_education`, `disability_support`, `end_of_life`). Fields: `relationships_substituted: List[str]`, `relationships_augmented: List[str]`, `mandatory_human_handback_triggers: List[str]`. Substitution (vs augmentation) routes to mandatory WA review.

**Code targets**: `ciris_engine/schemas/config/agent.py::CreatorIntentStatement` (extend); new `CareRelationshipDisclosure` schema; extend `deployment_domain` enum; `ACCORD.md` Book VI Ch 4 (new caregiving subcategory) + Annex A note tying Social/Justice axis to declared care relationships.

**Repo assignment**: ACCORD, CIRISAgent.

---

## 5. Cluster E — Conflict and discourse

### Gap E-1: De-escalation in inflammatory contexts (refinement: framework catches its own propaganda output, not response-context handling)

**Finding**: IDMA detects "adversarial narrative framing" and "contested claims as absolute fact" in its own reasoning; Coherence Conscience flags stigma vocabulary. The gap is response-context handling: how to operate well in inflammatory contexts without amplifying.

**Implementation status**: **PARTIAL — REFINEMENT NEEDED**. Per deepwiki:
- **IDMA** (`ciris_engine/logic/dma/idma.py`) sets `fragility_flag = TRUE` if `k_eff < 2`, phase is "rigidity", `correlation_risk > 0.7`, or response matches propaganda patterns. Recommends `PONDER` or `DEFER` when flagged.
- **Coherence Conscience** (part of Conscience Validation Framework) does propaganda detection + alignment-with-Accord-principles. Catches stigma vocabulary (e.g., "crazy", "insane") regardless of framing; failure produces `coherence ≤ 0.40` score.
- **CSDMA** (`ciris_engine/logic/dma/csdma.py`) has "ANTI-URGENCY EVALUATION" flagging urgency markers ("immediately", "urgent", "ASAP") with `"Urgency_Detected_Escalation_Recommended"`.
- **RecursiveProcessingPhase** with `ConscienceFailureContext` retries action selection on conscience failure with retry guidance.

The framework detects propaganda in inputs and prevents propaganda in outputs. The missing piece: structured de-escalation *style* — when operating in confirmed-adversarial contexts, prefer formulations that reduce polarization where possible without sacrificing truth.

**Evidence in encyclical**: MH §214.

**Impact**: Agents in adversarial-discourse contexts can be honest and non-coercive yet contribute to the adversarial pattern by mirroring tone.

**Proposed enhancement (refined)**: Extend CSDMA with a new "DISCOURSE-CONTEXT EVALUATION" — when `deployment_context.adversarial_flag` is set (manually flagged at deployment time, e.g., for election seasons, conflict zones, public crises), apply tone-modulation preferences: prefer specific factual claims over generalized characterizations, prefer naming concrete persons/institutions over abstract collectives, prefer questions to assertions where epistemic uncertainty permits.

**Code targets**: `ciris_engine/logic/dma/csdma.py` (extend); `ciris_engine/schemas/context/` (add adversarial_flag); `pdma_ethical.yml` and CSDMA prompt (instruct de-escalation style); `ACCORD.md` §VII Ch 1.

**Repo assignment**: ACCORD, CIRISAgent.

---

### Gap E-2: PDMA Step 6 has Transparency Rule but no Affected-Party-Voice requirement

**Finding**: PDMA Step 6 (Continuous Monitoring) has the Public Transparency rule (>100k MAU publishes redacted PDMA logs within 180 days). No requirement that affected parties have direct input before review is considered complete.

**Implementation status**: **CONFIRMED**. Per deepwiki:
- Accord PDMA Step 6: "Public Transparency rule: Deployments with >100,000 monthly active users must publish (or API-expose) redacted PDMA logs and WBD tickets within 180 days. Absence of publication voids any claim of CIRIS compliance."
- PDMA Step 7 (Feedback Governance): outcome data feeds Integrity-surveillance, Resilience loops, Wise Authorities.
- WBD: agent submits deferral package; WA resolves; no affected-party-input step in the WBD workflow.

Publication enables affected-party scrutiny *after the fact*. Direct input *during review* is not required.

**Evidence in encyclical**: MH §§216–217.

**Impact**: Post-action review proceeds without affected parties; this is the standard institutional failure mode of harm response.

**Proposed enhancement (refined)**: Add to PDMA Step 6 an **Affected-Party Input** requirement: for actions with documented adverse impact (flagged by the action handler when impact metrics exceed threshold), post-action review must include direct input from affected parties before the review is marked complete. If affected-party input is structurally unobtainable, harm-class is escalated and remediation is automatic rather than discretionary. Implement an affected-party-input ledger at CIRISPersist (if it becomes public) or at CIRISNode WBD.

**Code targets**: `ACCORD.md` PDMA Step 6; `ciris_engine/processors/states/solitude_processor.py` (review-workflow extension during reflection cycle); new ledger schema; `CIRISAI/CIRISNode` `wbd_tasks` extension or new `affected_party_inputs` table.

**Repo assignment**: ACCORD, CIRISAgent, CIRISNode (substituting for absent CIRISPersist).

---

### Gap E-3: WBD is one-way; no structured negotiation primitive

**Finding**: WBD allows agent → WA deferral with binary resolve (approve/reject). No counter-proposal exchange.

**Implementation status**: **CONFIRMED**. Per deepwiki:
- `WBDSubmitRequest` model: `agent_task_id`, encrypted `payload`. Submission is one-shot.
- `WBDResolveRequest` model: `decision` (approve/reject) + optional `comment`. Resolution is binary.
- `wbd_tasks` table tracks `status` (`open` → `resolved` or `sla_breached`).
- `/api/v1/wa/deferral` endpoint exists but returns HTTP 422 "Deferral not implemented" — confirms there was intent for richer deferral semantics, never built.

No counter-proposal field, no multi-round negotiation, no position-registration.

**Evidence in encyclical**: MH §§219–223.

**Impact**: Federation-level disagreements default to consensus (which suppresses minority positions) or moderation (which adjudicates). Negotiated convergence is structurally absent.

**Proposed enhancement (refined)**: Implement the stubbed `/api/v1/wa/deferral` endpoint as a **Structured Negotiation** primitive distinct from WBD. New tables: `negotiation_threads`, `negotiation_positions` (with `proposer_id`, `position_payload`, `counter_to: negotiation_position_id | None`), `negotiation_outcomes` (`accepted | escalated_to_wa | timed_out`). New Contribution-kind extension in `ciris-node-core` for typed negotiation contributions.

**Code targets**: `CIRISAI/CIRISNode` `cirisnode/api/wa/routes.py::deferral` (implement); `cirisnode/db/schemas.py` (new tables); `cirisnode/services/negotiation/` (new module); `ACCORD.md` §V Ch 2.

**Repo assignment**: CIRISNode, ACCORD.

---

### Gap E-4: No external-multilateral-process participation primitive

**Finding**: WBD payload is opaque JSON that could carry external content but has no routing to external bodies.

**Implementation status**: **CONFIRMED**. The `WBDSubmitRequest.payload` is encrypted JSON of arbitrary structure. CIRISNode does not interpret or route content to external entities (treaty negotiation processes, regulatory bodies, multilateral organizations).

**Evidence in encyclical**: MH §§201–203.

**Impact**: CIRIS deployments are objects of multilateral governance, not participants.

**Proposed enhancement (refined)**: New module `cirisnode/services/multilateral/` providing typed primitives for federation contributions to external processes: `Declaration`, `EvidenceSubmission`, `TreatyCommentary`, each with `attestation_required: bool` (where true, attach CIRISVerify attestation of authorship). New endpoint `POST /api/v1/multilateral/submit` accepting these types and routing to declared external destinations.

**Code targets**: `CIRISAI/CIRISNode` `cirisnode/services/multilateral/` (new); `cirisnode/api/multilateral/routes.py` (new); `CIRISAI/CIRISVerify` attestation extension for external-submission artifacts.

**Repo assignment**: CIRISNode, CIRISVerify.

---

### Gap E-5: No defensive-cyber-coordination module despite signed-audit infrastructure

**Finding**: Signed audit logging exists (Ed25519, `write_audit_log` in `cirisnode/utils/audit.py`). No threat-intelligence sharing.

**Implementation status**: **CONFIRMED**. Per deepwiki:
- `CIRISNode` features: Alignment Benchmarking (HE-300, SimpleBench, signed reports), WBD, Audit Anchoring.
- `write_audit_log` in `cirisnode/utils/audit.py` writes append-only audit log with SHA-256 payload hash for tamper evidence.
- Benchmark reports are Ed25519-signed.

The cryptographic primitives are in place. No module uses them for federation-peer-to-peer threat-intelligence sharing.

**Evidence in encyclical**: MH §§224–227.

**Impact**: Federation peers facing the same threat lack a protocol for coordinated defense; capability asymmetry favors attackers.

**Proposed enhancement (refined)**: New module `cirisnode/services/defensive_coordination/` providing signed threat-intelligence sharing across federation peers with strict scope-limits: defensive signatures only, no offensive content, no escalation. Schema: `ThreatSignature` (description, indicators-of-compromise, defensive-response-recommendation, expiration, signer_id). Reuses Ed25519 from existing audit infrastructure.

**Code targets**: `CIRISAI/CIRISNode` `cirisnode/services/defensive_coordination/` (new); `cirisnode/api/defensive/routes.py` (new); `CIRISAI/CIRISVerify` attestation extension for signature sharing.

**Repo assignment**: CIRISNode, CIRISVerify.

---

## 6. Cluster F — Structural and institutional analysis

### Gap F-1: No structural-injustice pattern analysis in CIRISLens

**Finding**: CIRISLens is per-agent observability with privacy-first redaction. No institutional-pattern-level aggregation.

**Implementation status**: **CONFIRMED**. Per deepwiki:
- CIRISLens collects operational metrics, traces, logs from individual agents.
- PII redaction: `user_hash` in service logs; message content not stored; log message sanitization.
- Continuous aggregates: `metrics_hourly`, `metrics_daily` for performance trend visibility.
- No detector for disparate outcomes across protected populations, no reinforcement-of-incumbent-power detection, no exclusion-of-categories analysis.

**Evidence in encyclical**: MH §36, §§77–81.

**Impact**: An agent's individual actions all pass PDMA; aggregate pattern can still embed structural injustice; nothing catches it.

**Proposed enhancement (refined)**: New module at `CIRISAI/CIRISLens` `metrics/structural/` computing:
- `disparate_outcome_index` — outcome distribution across declared protected populations (where deployment-context declares them)
- `incumbent_reinforcement_signal` — fraction of agent recommendations that route resources/attention to declared incumbent entities
- `stakeholder_exclusion_signal` — categories of stakeholders absent from action-stream impact assessments

Privacy-preserving: operates on aggregated traces, not individual messages. Surfaces findings to a new agent state hook in CIRISAgent's SOLITUDE processor.

**Code targets**: `CIRISAI/CIRISLens` `metrics/structural/` (new); `CIRISAI/CIRISAgent` `ciris_engine/processors/states/solitude_processor.py` (consume findings during reflection).

**Repo assignment**: CIRISLens, CIRISAgent.

---

### Gap F-2: SOLITUDE-state heuristic-review discipline — structure exists, specific cadence unclear

**Finding**: SOLITUDE state has reflection_cycles, maintenance_tasks_completed, patterns_identified. Specific heuristic-review-against-context-distribution discipline not documented in deepwiki-indexed source.

**Implementation status**: **UNCLEAR**. Per deepwiki:
- `SolitudeProcessor` in `ciris_engine/processors/states/solitude_processor.py` exists.
- `SolitudeState` schema has `reflection_cycles`, `maintenance_tasks_completed`, `patterns_identified` fields.
- `AgentProcessor` orchestrates state transitions including SOLITUDE.
- The internals of `SolitudeProcessor.process()` are not provided in deepwiki excerpts.

Could be implemented; could not be. Status genuinely unclear.

**Evidence in encyclical**: MH §22.

**Impact**: If heuristic drift goes undetected, the agent's effective ethical operation degrades silently over time.

**Proposed enhancement (refined)**: Read the actual `SolitudeProcessor.process()` to confirm. If absent, add a quarterly **Context-Drift Review** cadence: compare current heuristic weights against the operating-context distribution actually encountered (from the agent's own audit chain). Significant drift triggers WBD to WA for heuristic-amendment review with `needs_category=heuristic_drift_review`.

**Code targets**: `ciris_engine/processors/states/solitude_processor.py` (verify or implement); new `needs_category` value; `ACCORD.md` §V Ch 1 operational requirement.

**Repo assignment**: CIRISAgent, ACCORD.

**Pre-implementation step**: Read `ciris_engine/processors/states/solitude_processor.py` directly (not via deepwiki) to determine whether the discipline already exists and the gap shrinks to none, or persists.

---

## 7. Cluster G — Environmental accounting

### Gap G-1: Compute/energy data is tracked and audited but not fed forward into PDMA

**Finding**: LLMBus tracks per-call energy/carbon and aggregates per thought_id. Surfaced to ACTION_COMPLETE step + audit chain. **Not** fed back into PDMA Step 1 contextualisation as a cost-benefit input.

**Implementation status**: **STRONG_PARTIAL — REFINEMENT NEEDED**. Per deepwiki:
- `LLMBus` records per-LLM-call telemetry: `tokens_used`, `tokens_input`, `tokens_output`, `cost_cents`, `carbon_grams`, `energy_kwh`. Tagged with `thought_id`.
- `LLMPricingCalculator` computes `energy_kwh` from `kwh_per_1k_tokens`; `carbon_grams` from `energy_kwh × carbon_intensity`.
- `_query_thought_resources` aggregates per `thought_id`: sums `tokens_total`, `cost_cents`, `carbon_grams`, `energy_mwh`.
- `_create_action_complete_data` constructs `ActionCompleteStepData` with all energy/carbon fields.
- Included in `ActionResultEvent` — the `ACTION_RESULT` event seals the trace.
- `ResourceMonitorService` collects system-level CPU/memory/disk/tokens-per-hour separately.
- `SystemOverview` carries `tokensLastHour`, `costLastHourCents`, `carbonLastHourGrams`, `energyLastHourKwh`.

**The footprint is in the audit chain on a per-action basis.** What's missing: this aggregated data is reported AFTER the action; not consulted BEFORE in PDMA Step 1 contextualisation as a factor in cost-benefit. `_resolve_parent_event_for_step` shows `PERFORM_DMAS` is associated with `DMA_RESULTS` (during reasoning), and aggregation only happens at `ACTION_COMPLETE`.

**Evidence in encyclical**: MH §101.

**Impact**: Agents and federation peers operate without any forward-looking cost signal for their compute/energy choices. Retroactive accounting exists; deliberative use of the accounting does not.

**Proposed enhancement (refined)**: Add a **predictive footprint estimate** for the proposed action in PDMA Step 1. Computed by `LLMPricingCalculator.estimate_thought_cost(thought_context, candidate_models)` returning anticipated `carbon_grams` and `energy_kwh` ranges. Surfaced as a context field that PDMA can weight in Step 2's six-principles assessment ("does the energy cost of this action proportional to its expected benefit?"). Add federation-level metric `compute_intensity_per_outcome` at CIRISLens aggregating actual outcomes vs energy spent.

**Code targets**: `ciris_engine/logic/buses/llm_bus.py::LLMPricingCalculator` (new estimate method); `ciris_engine/logic/dma/pdma.py` (consume estimate in context); `pdma_ethical.yml` (instruct considering footprint); `CIRISAI/CIRISLens` `metrics/environmental/` (new aggregator); `ACCORD.md` Annex A axis 4 implementation note.

**Repo assignment**: ACCORD, CIRISAgent, CIRISLens.

---

## 8. Summary by repo (with code targets)

| Repo | Enhancements |
|---|---|
| **ACCORD** | New principle: Decision Locality (A-1). Clauses: Power-Concentration Disclosure (A-2, Book VI Ch 1, Ch 5), Cross-jurisdictional WA quorum (A-3, Annex B), Benefit-Distribution Disclosure (B-1, Book VI Ch 4.B), Worst-Case Population Check (B-2, §II PDMA Step 2), M-1 intergenerational + horizon disclosure (B-3, §I Ch 1 + Annex A), Information-ecosystem stewardship (C-1, Book IV Ch 3), Engagement-design declaration (C-2, Book VI Ch 4.B), Context-Health Disclosure (C-3, PDMA Step 1), Educational Context ST modifier (C-4, Book VI Ch 3), Labor Displacement Assessment (D-1, Book VI Ch 4.C), Agency-Erosion criterion (D-2, PDMA Step 2), Annex A caregiving subcategory (D-3/D-4), Discourse De-escalation (E-1, §VII Ch 1), Affected-Party Voice (E-2, PDMA Step 6), Structured Negotiation (E-3, §V Ch 2), Context-Drift Review (F-2, §V Ch 1), Annex A axis 4 implementation note (G-1). |
| **CIRISAI/CIRISAgent** | Schema extensions: `CreatorIntentStatement` adds `market_position_disclosure` (A-2), `benefit_distribution_disclosure` (B-1), `engagement_optimization_target` (C-2), `intermediary_institution_health` (C-3, in context schema), `labor_displacement_assessment` (D-1), `care_relationship_disclosure` (D-3/D-4), educational-design-constraints (C-4). PDMA: new reasoning step in `pdma_ethical.yml` (B-2), `beneficiary_horizons` field in result (B-3), de-escalation style instructions (E-1), context-health consideration (C-3). New conscience faculties in `logic/conscience/core.py`: `WorstCasePopulationConscience` (B-2), `AgencyErosionDetector` (D-2). DMA extensions: `csdma.py` discourse-context evaluation (E-1), `dsaspdma.py` scale-routing classification (A-1). State extensions: `processors/states/solitude_processor.py` consumes structural-pattern findings from CIRISLens (F-1), runs context-drift review (F-2), affected-party review during reflection (E-2). Stewardship: `logic/stewardship/` adds educational-context modifier (C-4). LLM bus: `LLMPricingCalculator.estimate_thought_cost` (G-1). |
| **CIRISAI/CIRISLens** | New metric modules: `metrics/ecosystem/` for source diversity, attention-flow concentration, discourse-correlation rise (C-1). `metrics/structural/` for disparate-outcome, incumbent-reinforcement, stakeholder-exclusion signals (F-1). `metrics/environmental/` for compute_intensity_per_outcome (G-1). New cohort detector for concentration patterns (A-2). New API endpoints exposing `benefit_distribution_index` (B-1), `intertemporal_beneficiary_ratio` (B-3), `labor_displacement_index` (D-1), `agency_erosion_index` (D-2). `config/public-architecture.yaml` extended with new recording rules. |
| **CIRISAI/CIRISNode** | Implement stubbed `POST /api/v1/wa/deferral` as Structured Negotiation primitive (E-3). New tables: `high_impact_deployments` (A-3), `negotiation_threads`, `negotiation_positions`, `negotiation_outcomes` (E-3), `affected_party_inputs` (E-2). New services: `services/wa/quorum.py` (A-3), `services/negotiation/` (E-3), `services/multilateral/` (E-4), `services/defensive_coordination/` (E-5). New endpoints: `/api/v1/multilateral/submit` (E-4), `/api/v1/defensive/share` (E-5). WBD extension: scale-routing lateral endpoint to peer agents before human queue (A-1). |
| **CIRISAI/CIRISVerify** | Attestation extensions: external-submission artifacts for multilateral participation (E-4); defensive cyber signatures (E-5). |
| **CIRISPersist** (if/when public) | Affected-party-input ledger schema (E-2); deferred to CIRISNode in interim. |
| **CIRISEdge** | No direct enhancements — its peer-to-peer-no-broker transport is the structural shape that Decision Locality (A-1) names at the Accord layer. |

---

## 9. Implementation priority

**Tier 1 — Highest mission impact, lowest implementation cost; ship-ready as discrete changes**:
- **C-2** Engagement-optimization-target field in CIS (Book VI Ch 4.B + `CreatorIntentStatement` extension). The prohibition already exists; only the declaration is new.
- **G-1** Predictive footprint estimate in `LLMPricingCalculator.estimate_thought_cost` consumed by PDMA Step 1. The tracking is done; only the forward-feedback is new.
- **C-4** Formalize educational ST modifier in `logic/stewardship/`. The protective DMAs already exist; only the formal escalation is new.
- **F-2** Verify `SolitudeProcessor.process()` against the heuristic-review claim; implement only the delta.

**Tier 2 — Substantial single-repo additions, high mission impact**:
- **B-2** `WorstCasePopulationConscience` + PDMA prompt extension.
- **D-2** `AgencyErosionDetector` longitudinal conscience.
- **D-1** `labor_displacement_assessment` CIS extension + PDMA Step 1.
- **E-1** CSDMA discourse-context evaluation.
- **A-1** Decision Locality classification in DSASPDMA.

**Tier 3 — New federation modules**:
- **C-1** Information-ecosystem metric suite at CIRISLens.
- **F-1** Structural Pattern Analysis at CIRISLens.
- **E-3** Implement the stubbed `/api/v1/wa/deferral` as Structured Negotiation primitive.
- **A-3** Federation-Scale Accountability registry + cross-jurisdiction WA quorum at CIRISNode.

**Tier 4 — Cross-repo coordinated work**:
- **E-2** Affected-Party Voice — PDMA + processors/states + Persist/Node ledger.
- **E-4** Multilateral Participation — Node + Verify.
- **E-5** Defensive Cyber Coordination — Node + Verify.
- **A-2** Power-Concentration Disclosure — ACCORD + Agent CIS + Lens detector.
- **B-1** Benefit-Distribution Disclosure — ACCORD + Agent CIS + Lens metric.
- **B-3** Beneficiary-horizons disclosure — ACCORD + Agent PDMA + Lens metric.
- **C-3** Context-Health Disclosure — ACCORD + Agent context schema.
- **D-3/D-4** Care-relationship disclosure — ACCORD + Agent CIS.

---

## 10. Status

- **Findings**: locked, deepwiki-verified.
- **Code references**: specific paths/classes/functions noted per gap where infrastructure exists or where enhancement lands.
- **Refinements applied**: 8 gaps narrowed based on existing infrastructure (`MANIPULATION_COERCION` already covers addictive design at capability layer; `OptimizationVetoConscience` already covers flagrant autonomy erosion; Educational DMA Stack already protects minors; Annex A Social/Justice axis covers relational well-being; IDMA + Coherence Conscience already detect propaganda; LLMBus already tracks per-call energy; PDMA prompts include intergenerational and time-scale consideration).
- **One gap still uncertain** (F-2) pending direct read of `solitude_processor.py`.
- **Next**: Tier 1 set is ship-ready as four discrete changes per the priority list. Each is a mechanical addition that closes a real gap; total work probably <2 engineer-weeks for the four together.

**Cross-references:**
- `MISSION.md` — methodology, status taxonomy, grounding posture
- `MAPPING_CH*.md` — the seven chapter mappings that surfaced the gaps
- `ACCORD_canonical.txt` — v1.2-Beta as fetched from ciris.ai/ciris_accord.txt
- `MISSION_CIRIS*.md` — federation-peer charters that the enhancements modify
- DeepWiki: `https://deepwiki.com/CIRISAI/CIRISAgent`, `.../CIRISLens`, `.../CIRISNode`

**End GAPS.md v2.0**
