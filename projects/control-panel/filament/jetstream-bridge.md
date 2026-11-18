# Control Panel: Jetstream Bridge Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#jetstream-bridge). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-jetstream-bridge-filament`  
**Matching domain module:** `jetstream-bridge`  
**Application:** Control Panel  
**Source feature:** [Jetstream Bridge](../features/jetstream-bridge.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `jetstream-bridge` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Jetstream-compatible profile:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Security:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Team:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Token:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Session:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account-deletion action contracts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-jetstream-bridge-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `jetstream-compatible-profile`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `security`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `team`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `token`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `session`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-deletion-action-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `jetstream-bridge` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-jetstream-bridge-filament`](https://github.com/liberusoftware/module-jetstream-bridge-filament) (`liberusoftware/jetstream-bridge-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/jetstream-bridge.md) · [API plan](../api/jetstream-bridge.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Jetstream-compatible profile** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `jetstream-compatible profile`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Security** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `security`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Team** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `team`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Token** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `token`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Session** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `session`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account-deletion action contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account-deletion action contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateNewUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/CreateNewUser.php) | `public function __construct( private readonly RegistrationPolicy $registration, private readonly InvitationValidator $invitations, private readonly IdentifierNormalizer $normalizer, )`<br>`public function create(array $input): User` |
| [PasswordValidationRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/PasswordValidationRules.php) | No named public method detected by the static index. |
| [ResetUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/ResetUserPassword.php) | `public function reset(User $user, array $input): void` |
| [UpdateUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/UpdateUserPassword.php) | `public function update(User $user, array $input): void` |
| [UpdateUserProfileInformation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Fortify/UpdateUserProfileInformation.php) | `public function __construct(private readonly IdentifierNormalizer $normalizer)`<br>`public function update(User $user, array $input): void` |
| [DeleteUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge/src/Actions/Jetstream/DeleteUser.php) | `public function __construct(DeletesTeams $deletesTeams)`<br>`public function delete($user)` |
<!-- layer-implementation-plan:end -->
