# Automation: AI Gateway Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#ai-gateway). Observed identity: [`liberusoftware/automation-ai-gateway-filament`](../../../modules/source/liberusoftware--automation-ai-gateway-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-ai-gateway-filament`  
**Matching domain module:** `automation-ai-gateway`  
**Application:** Automation  
**Source feature:** [AI Gateway](../features/ai-gateway.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `automation-ai-gateway` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Model catalog:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fallback:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Structured output:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tool policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage metering:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-ai-gateway-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `provider-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `model-catalog`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fallback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `structured-output`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tool-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage-metering`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `automation-ai-gateway` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-automation-ai-gateway-filament`](https://github.com/liberusoftware/module-automation-ai-gateway-filament) (`liberusoftware/automation-ai-gateway-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/ai-gateway.md) · [API plan](../api/ai-gateway.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Provider contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Model catalog** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `model catalog`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fallback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fallback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Structured output** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `structured output`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tool policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tool policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage metering** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage metering`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AiGatewayFilamentPlugin.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-filament/src/AiGatewayFilamentPlugin.php) · [AiGatewayFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-filament/src/AiGatewayFilamentServiceProvider.php) · [AiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-filament/src/Resources/AiGatewayResource.php) · [CreateAiGateway.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-filament/src/Resources/AiGatewayResource/Pages/CreateAiGateway.php) · [EditAiGateway.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-filament/src/Resources/AiGatewayResource/Pages/EditAiGateway.php) · [ListAiGateway.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway-filament/src/Resources/AiGatewayResource/Pages/ListAiGateway.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway/src/Actions/CreateAiGatewayResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): AiGatewayResource` |
| [TransitionAiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway/src/Actions/TransitionAiGatewayResource.php) | `public function execute(AiGatewayResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): AiGatewayResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AiGatewayResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-ai-gateway/src/Models/AiGatewayResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
