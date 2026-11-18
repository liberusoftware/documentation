# Boilerplate: Jetstream Bridge Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#jetstream-bridge). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-jetstream-bridge-filament`
**Matching core package:** [`module-jetstream-bridge`](../core/jetstream-bridge.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Jetstream-compatible profile, security, team, token, session, and account-deletion action contracts.

## Adapter implementation plan

This package presents the Jetstream Bridge core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Jetstream Bridge core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
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
