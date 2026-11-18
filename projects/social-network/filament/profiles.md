# Social Network: Profiles Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#profiles). Observed identity: [`liberusoftware/module-social-network-profiles-filament`](../../../modules/source/liberusoftware--module-social-network-profiles-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-profiles-filament`  
**Matching domain module:** `social-network-profiles`  
**Application:** Social Network  
**Source feature:** [Profiles](../features/profiles.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-profiles` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Handles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bios:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attributes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Avatars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Blocking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profile lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-profiles-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `handles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bios`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attributes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `avatars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `blocking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profile-lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-profiles` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-profiles-filament`](https://github.com/liberusoftware/module-profiles-filament) (`liberusoftware/profiles-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/profiles.md) · [API plan](../api/profiles.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Handles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `handles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bios** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bios`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attributes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attributes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Avatars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `avatars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Blocking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `blocking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Profile lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profile lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EditProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-filament/src/Pages/EditProfile.php) · [ProfilesFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-filament/src/ProfilesFilamentPlugin.php) · [ProfilesFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-filament/src/ProfilesFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/src/Actions/UpdateProfile.php) | `public function handle(Model $profile, ProfileUpdate $update): Model` |
<!-- layer-implementation-plan:end -->
