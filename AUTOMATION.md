# Liberu Automation

## Product Scope

**Purpose:** Provider-neutral automation and AI capabilities for Liberu products.
**Architecture:** Implement every capability as modules conforming to [MODULES.md](MODULES.md); presentation follows [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope defines automation behavior only.

## Outcomes

- Build governed workflows from triggers, conditions, approvals, actions, delays, and failure paths.
- Offer text, reasoning, extraction, voice, image, and video capabilities without coupling products to one provider.
- Make every automated decision reviewable, measurable, cost-controlled, and safe to retry.

## Module plan

| Module | Responsibilities |
|---|---|
| Automation Core | Workflow definitions, versions, triggers, state, runs, variables, schedules, retries, cancellation, and compensation |
| Rules | Typed conditions, expressions, validation, simulation, and reusable decision tables |
| Approvals | Human review queues, separation of duties, expiry, escalation, delegation, and evidence |
| AI Gateway | Provider contracts, model catalog, routing, fallback, structured output, tool policy, and usage metering |
| Prompt Registry | Versioned prompts, variables, evaluation sets, brand/tenant overrides, approvals, and rollback |
| Data Processing | Classification, extraction, summarization, translation, enrichment, redaction, and batch processing |
| Voice | Speech-to-text, text-to-speech, streaming sessions, interruption, transcripts, and consent controls |
| Image | Generation/editing requests, source assets, moderation, provenance, variants, and delivery |
| Video | Generation/editing jobs, scripts, captions, audio, moderation, provenance, and delivery |
| Connectors | Authenticated triggers/actions, webhooks, rate limits, cursor sync, replay, and reconciliation |
| Evaluation | Quality suites, regression comparison, latency/cost metrics, safety checks, and release gates |

## Required workflows

1. **Design and publish:** draft workflow → validate dependencies and permissions → simulate → approve → version and publish.
2. **Execute:** receive trigger → deduplicate → evaluate rules → obtain approvals → perform actions → record outputs and cost.
3. **Provider failure:** classify error → retry/back off → route to permitted fallback → pause or request operator action.
4. **Model change:** evaluate candidate → compare quality, safety, latency, and cost → approve rollout → monitor → roll back if thresholds fail.
5. **Sensitive-data handling:** classify input → minimize/redact → enforce provider/region policy → process → apply retention/deletion rules.

## Product requirements

- Support event, webhook, schedule, manual, and data-change triggers.
- Provide sync and queued actions, parallel branches, waits, timeouts, loops with limits, sub-workflows, and compensating actions.
- Require schemas for workflow inputs/outputs and validate structured AI responses.
- Enforce per-workflow provider, model, tool, budget, rate, region, retention, and human-approval policies.
- Prevent AI tools from exceeding the initiating actor's permissions.
- Store run timelines, prompt/model versions, provider request identifiers, approvals, errors, tokens, duration, and estimated cost.
- Provide test mode, fixtures, deterministic stubs, replay with redaction, and side-effect-free simulation.
- Expose APIs, events, Filament operations, and embeddable approval/run-status Livewire components.

## Integrations

Initial drivers may cover OpenAI, Anthropic, Google, local models, email, SMS, telephony, storage, HTTP/webhooks, and Liberu module events. Each driver declares capabilities and compliance constraints; provider availability is configuration, not a domain assumption.

## Quality and safety gates

- Defend against prompt injection, unsafe tool use, secret disclosure, malformed structured output, excessive spend, and unbounded execution.
- Obtain explicit consent for recording, biometric processing, or sensitive-media use where required.
- Record provenance and usage rights for generated media; watermark or label output when policy requires it.
- Test duplicate triggers, partial failures, fallback, cancellation, approval races, tenant isolation, quotas, and provider outages.
- Alert on failure rate, queue delay, quality regression, policy violation, abnormal cost, and exhausted budget.

## Delivery phases

1. Automation Core, Rules, run history, scheduling, and approvals.
2. AI Gateway, Prompt Registry, text/data processing, metering, and evaluation.
3. Connectors and governed product-module actions.
4. Voice and real-time sessions.
5. Image/video pipelines, provenance, and advanced evaluations.

## Definition of done

The product is ready when workflows are versioned, authorized, tenant-safe, idempotent, observable, recoverable, budget-enforced, provider-replaceable, and covered by evaluation and failure-path tests. Each module must be independently installable and documented for conversion into a GitHub epic.
