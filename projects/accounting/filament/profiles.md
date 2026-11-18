# Accounting: Profiles Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#profiles). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-profiles-filament`  
**Matching domain module:** `profiles`  
**Application:** Accounting  
**Source feature:** [Profiles](../features/profiles.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `profiles` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Names:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Avatars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contact preferences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locale/timezone:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Completion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Controlled profile updates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-profiles-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `names`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `avatars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contact-preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locale-timezone`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `completion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `controlled-profile-updates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `profiles` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-profiles-filament`](https://github.com/liberusoftware/module-profiles-filament) (`liberusoftware/profiles-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/profiles.md) · [API plan](../api/profiles.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Names** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `names`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Avatars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `avatars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contact preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contact preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locale/timezone** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locale/timezone`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Completion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `completion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Controlled profile updates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `controlled profile updates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/src/Actions/UpdateProfile.php) | `public function handle(Model $profile, ProfileUpdate $update): Model` |
<!-- layer-implementation-plan:end -->
