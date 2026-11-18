# Matching Intelligence: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-matching-intelligence`.<br>
**Matching domain module:** `matching-intelligence`

**Proposed design identifier:** `module-accounting-matching-intelligence-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/matching-intelligence.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-accounting-erp-next-react`](https://github.com/liberusoftware/project-accounting-erp-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/matching-intelligence.md)) |
| Capability Next.js module skeleton | [module-accounting-matching-intelligence-nextjs](https://github.com/liberusoftware/module-accounting-matching-intelligence-nextjs) (`@liberusoftware/module-accounting-matching-intelligence-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-matching-intelligence](../../../modules/source/liberusoftware--module-accounting-matching-intelligence.md) |
| API | [liberusoftware/module-accounting-matching-intelligence-api](../../../modules/source/liberusoftware--module-accounting-matching-intelligence-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Bank/document/payment/settlement matching suggestions** | Server Component loads authorized `bank/document/payment/settlement matching suggestions` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Confidence** | Server Component loads authorized `confidence` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Evidence** | Server Component loads authorized `evidence` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Feedback** | Server Component loads authorized `feedback` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Safe automation thresholds** | Server Component loads authorized `safe automation thresholds` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [MatchingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Queries/MatchingQuery.php) | `public function suggestions(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function automationEligible(?int $teamId = null, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConfigureThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): AutomationThreshold` |
| [CreateSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/CreateSuggestion.php) | `public function handle(array $attributes, array $evidence = []): MatchingSuggestion` |
| [DecideSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/DecideSuggestion.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, bool $accept = true, bool $automate = false): MatchingSuggestion` |
| [RecordFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/RecordFeedback.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, string $type, ?string $comment = null): MatchingFeedback` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [AutomationThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/AutomationThreshold.php) | `team_id`, `match_type`, `minimum_confidence`, `maximum_amount`, `require_evidence`, `active`, `metadata` |
| [MatchingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingEvidence.php) | `suggestion_id`, `kind`, `field`, `source_value`, `target_value`, `weight`, `metadata` |
| [MatchingFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingFeedback.php) | `suggestion_id`, `actor_ref`, `feedback_type`, `comment`, `features`, `metadata` |
| [MatchingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingSuggestion.php) | `team_id`, `suggestion_ref`, `source_type`, `source_id`, `target_type`, `target_id`, `match_type`, `confidence`, `score`, `status`, `automation_threshold`, `explanation`, `algorithm_version`, `expires_at`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-matching-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/matching-intelligence')->group(function (): void {
Route::get('/suggestions', [MatchingIntelligenceController::class, 'index'])->name('accounting.matching-intelligence.list');
Route::post('/suggestions', [MatchingIntelligenceController::class, 'store'])->name('accounting.matching-intelligence.create');
Route::get('/suggestions/{suggestion}', [MatchingIntelligenceController::class, 'show'])->name('accounting.matching-intelligence.show');
Route::post('/suggestions/{suggestion}/decide', [MatchingIntelligenceController::class, 'decide'])->name('accounting.matching-intelligence.decide');
Route::post('/suggestions/{suggestion}/feedback', [MatchingIntelligenceController::class, 'feedback'])->name('accounting.matching-intelligence.feedback');
Route::post('/thresholds', [MatchingIntelligenceController::class, 'threshold'])->name('accounting.matching-intelligence.threshold');
```

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
