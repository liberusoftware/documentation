# CMS: Cms Drupal Migration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-drupal-migration). Observed identity: [`liberusoftware/module-cms-drupal-migration-livewire`](../../../modules/source/liberusoftware--module-cms-drupal-migration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-drupal-migration-livewire`  
**Matching domain module:** `cms-drupal-migration`  
**Application:** CMS  
**Source feature:** [Cms Drupal Migration](../features/cms-drupal-migration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Entity/bundle/field data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Revisions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Moderation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Taxonomy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Media:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Menus:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Views mapping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Translations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Configuration evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-drupal-migration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsDrupalMigration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `entity-bundle-field-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `revisions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `moderation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `taxonomy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `media`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `menus`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `views-mapping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `translations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `configuration-evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-drupal-migration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-drupal-migration.md) · [API plan](../api/cms-drupal-migration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Entity/bundle/field data** | Expose a focused Livewire 4 component and namespaced Blade default view for `entity/bundle/field data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Revisions** | Expose a focused Livewire 4 component and namespaced Blade default view for `revisions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Moderation** | Expose a focused Livewire 4 component and namespaced Blade default view for `moderation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Taxonomy** | Expose a focused Livewire 4 component and namespaced Blade default view for `taxonomy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Media** | Expose a focused Livewire 4 component and namespaced Blade default view for `media` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Menus** | Expose a focused Livewire 4 component and namespaced Blade default view for `menus` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Views mapping** | Expose a focused Livewire 4 component and namespaced Blade default view for `views mapping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Translations** | Expose a focused Livewire 4 component and namespaced Blade default view for `translations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Configuration evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `configuration evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [DrupalMigrationList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-drupal-migration-livewire/src/Livewire/DrupalMigrationList.php) · [DrupalMigrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-drupal-migration-livewire/src/DrupalMigrationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DrupalMigrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-drupal-migration/src/Services/DrupalMigrationService.php) | `public function __construct(private MigrationFrameworkService $framework)`<br>`public function start(string $source, array $options = [], ?int $teamId = null): MigrationJob`<br>`public function add(MigrationJob $job, string $type, string $sourceId, array $payload = []): MigrationRecord`<br>`public function process(MigrationRecord $record, bool $success, ?string $reason = null): MigrationRecord`<br>`public function complete(MigrationJob $job): MigrationJob` |
<!-- layer-implementation-plan:end -->
