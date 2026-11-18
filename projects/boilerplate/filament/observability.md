# Boilerplate: Observability Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#observability). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-observability-filament`
**Matching core package:** [`module-observability`](../core/observability.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Structured logs, correlation, metrics, traces, exception reporting, health checks, redaction, and SLO hooks.

## Adapter implementation plan

This package presents the Observability core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Observability core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-observability-filament`](https://github.com/liberusoftware/module-observability-filament) (`liberusoftware/observability-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/observability.md) · [API plan](../api/observability.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Structured logs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `structured logs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Correlation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `correlation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Metrics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `metrics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Traces** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `traces`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exception reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exception reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redaction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redaction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SLO hooks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `slo hooks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [Metrics.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/observability/src/Contracts/Metrics.php) | `public function increment(string $name, int $value = 1, array $labels = []): void`<br>`public function observe(string $name, float $value, array $labels = []): void` |
| [ObservabilityActor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/observability/src/Contracts/ObservabilityActor.php) | `public function isAdmin(): bool` |
<!-- layer-implementation-plan:end -->
