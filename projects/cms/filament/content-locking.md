# CMS: Content Locking Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-locking). Observed identity: [`liberusoftware/module-cms-content-locking-filament`](../../../modules/source/liberusoftware--module-cms-content-locking-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-locking-filament`  
**Matching domain module:** `cms-content-locking`  
**Application:** CMS  
**Source feature:** [Content Locking](../features/content-locking.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-locking` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Optimistic concurrency:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Edit presence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Takeover policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflict comparison:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Merge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recovery:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-locking-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `optimistic-concurrency`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `edit-presence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `takeover-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflict-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `merge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-locking` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-locking-filament`](https://github.com/liberusoftware/module-cms-content-locking-filament) (`liberusoftware/cms-content-locking-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/content-locking.md) · [API plan](../api/content-locking.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Optimistic concurrency** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `optimistic concurrency`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Edit presence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `edit presence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Takeover policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `takeover policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conflict comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conflict comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Merge** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `merge`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentLockingFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-locking-filament/src/ContentLockingFilamentServiceProvider.php) · [ContentLockResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-locking-filament/src/Resources/ContentLockResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentLockingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-locking/src/Services/ContentLockingService.php) | `public function acquire(string $subjectType, string $subjectKey, ?int $teamId, ?int $holderId, array $snapshot = [], ?int $ttlMinutes = null): ContentLock`<br>`public function renew(ContentLock $lock, string $token, ?int $ttlMinutes = null): ContentLock`<br>`public function release(ContentLock $lock, string $token): void`<br>`public function compare(ContentLock $lock, array $current): array`<br>`public function merge(ContentLock $lock, array $current, string $token): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentLock.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-locking/src/Models/ContentLock.php) | `team_id`, `subject_type`, `subject_key`, `holder_id`, `token`, `version`, `snapshot`, `expires_at` |
<!-- layer-implementation-plan:end -->
