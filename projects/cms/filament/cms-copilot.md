# CMS: CMS Copilot Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-copilot). Observed identity: [`liberusoftware/module-cms-copilot-filament`](../../../modules/source/liberusoftware--module-cms-copilot-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-copilot-filament`  
**Matching domain module:** `cms-copilot`  
**Application:** CMS  
**Source feature:** [CMS Copilot](../features/cms-copilot.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-copilot` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-bounded search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Summaries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drafting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transforms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Internal links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Action confirmation via Automation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-copilot-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `permission-bounded-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `summaries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drafting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transforms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `internal-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `action-confirmation-via-automation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-copilot` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-cms-copilot-filament`](https://github.com/liberusoftware/module-cms-cms-copilot-filament) (`liberusoftware/cms-cms-copilot-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-copilot.md) · [API plan](../api/cms-copilot.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Permission-bounded search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permission-bounded search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Summaries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `summaries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drafting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drafting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transforms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transforms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Internal links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `internal links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Action confirmation via Automation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `action confirmation via automation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CopilotFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-copilot-filament/src/CopilotFilamentServiceProvider.php) · [CopilotRequestResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-copilot-filament/src/Resources/CopilotRequestResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CopilotHandlerInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Contracts/CopilotHandlerInterface.php) | `public function capability(): string`<br>`public function handle(string $prompt, array $input): array` |
| [CopilotService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Services/CopilotService.php) | `public function submit(?int $teamId, string $capability, string $prompt, array $input = [], ?string $idempotencyKey = null): CopilotRequest`<br>`public function execute(CopilotRequest $request): CopilotRequest`<br>`public function requireConfirmation(CopilotRequest $request): string`<br>`public function confirm(CopilotRequest $request, string $token): CopilotRequest`<br>`public function registerHandler(CopilotHandlerInterface $handler): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotRequest.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Models/CopilotRequest.php) | `team_id`, `capability`, `prompt`, `input`, `result`, `status`, `idempotency_key`, `confirmation_hash`, `confirmed_at`, `failure_reason` |
<!-- layer-implementation-plan:end -->
