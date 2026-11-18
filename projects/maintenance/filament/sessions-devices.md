# Maintenance: Sessions Devices Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sessions-devices). Observed identity: [`liberusoftware/sessions-devices-filament`](../../../modules/source/liberusoftware--sessions-devices-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-sessions-devices-filament`  
**Matching domain module:** `sessions-devices`  
**Application:** Maintenance  
**Source feature:** [Sessions Devices](../features/sessions-devices.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `sessions-devices` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Active sessions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Device metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timeout policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suspicious access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-sessions-devices-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `active-sessions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `device-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timeout-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suspicious-access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `sessions-devices` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-sessions-devices-filament`](https://github.com/liberusoftware/module-sessions-devices-filament) (`liberusoftware/sessions-devices-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sessions-devices.md) · [API plan](../api/sessions-devices.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Active sessions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `active sessions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Device metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `device metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Timeout policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timeout policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suspicious access** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suspicious access`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountSecurity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices-filament/src/Pages/AccountSecurity.php) · [SessionsDevicesFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices-filament/src/SessionsDevicesFilamentPlugin.php) · [SessionsDevicesFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices-filament/src/SessionsDevicesFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SessionReader.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/src/Queries/SessionReader.php) | `public function forActor(string\|int $actorId, ?string $currentId = null): Collection`<br>`public function revoke(string\|int $actorId, string $sessionId, ?string $currentId = null): bool`<br>`public function revokeOthers(string\|int $actorId, string $currentId): int` |
<!-- layer-implementation-plan:end -->
