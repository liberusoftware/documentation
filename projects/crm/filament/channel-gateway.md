# CRM: Channel Gateway Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#channel-gateway). Observed identity: [`liberusoftware/module-crm-channel-gateway-filament`](../../../modules/source/liberusoftware--module-crm-channel-gateway-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-channel-gateway-filament`  
**Matching domain module:** `crm-channel-gateway`  
**Application:** CRM  
**Source feature:** [Channel Gateway](../features/channel-gateway.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-channel-gateway` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider-neutral email:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SMS/MMS:** resource/table/form/action or page behavior for this module's authorized workflow.
- **WhatsApp:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Web chat:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Social messaging:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Push contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider selection:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-channel-gateway-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `provider-neutral-email`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sms-mms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `whatsapp`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `web-chat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `social-messaging`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `push-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-selection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-channel-gateway` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-channel-gateway-filament`](https://github.com/liberusoftware/module-crm-channel-gateway-filament) (`liberusoftware/crm-channel-gateway-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/channel-gateway.md) · [API plan](../api/channel-gateway.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Provider-neutral email** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider-neutral email`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SMS/MMS** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sms/mms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **WhatsApp** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `whatsapp`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Web chat** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `web chat`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Social messaging** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `social messaging`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Push contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `push contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider selection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider selection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ChannelGatewayFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-filament/src/ChannelGatewayFilamentPlugin.php) · [ChannelGatewayFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-filament/src/ChannelGatewayFilamentServiceProvider.php) · [GatewayChannelResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-filament/src/Resources/GatewayChannelResource.php) · [CreateGatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-filament/src/Resources/GatewayChannelResource/Pages/CreateGatewayChannel.php) · [ListGatewayChannels.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-filament/src/Resources/GatewayChannelResource/Pages/ListGatewayChannels.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GatewayQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Queries/GatewayQuery.php) | `public function channels(int $teamId): Builder`<br>`public function deliveries(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [QueueGatewayDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/QueueGatewayDelivery.php) | `public function execute(int $teamId, GatewayChannel $channel, string $idempotencyKey, string $address, string $body, array $metadata = []): GatewayDelivery` |
| [RegisterGatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/RegisterGatewayChannel.php) | `public function execute(int $teamId, string $key, string $kind, string $provider, array $configuration = []): GatewayChannel` |
| [UpdateGatewayHealth.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/UpdateGatewayHealth.php) | `public function execute(int $teamId, GatewayChannel $channel, bool $healthy, ?string $failure = null): GatewayChannel` |
| [ChannelAdapter.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Contracts/ChannelAdapter.php) | `public function send(string $address, string $body, array $metadata = []): string`<br>`public function health(): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Models/GatewayChannel.php) | No literal fillable array detected; inspect the model and API schema. |
| [GatewayDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Models/GatewayDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
