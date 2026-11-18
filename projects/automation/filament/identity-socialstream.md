# Automation: Identity Socialstream Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#identity-socialstream). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-identity-socialstream-filament`  
**Matching domain module:** `identity-socialstream`  
**Application:** Automation  
**Source feature:** [Identity Socialstream](../features/identity-socialstream.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `identity-socialstream` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Social provider redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Callbacks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identity linking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Protected credentials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account synchronization:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-identity-socialstream-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `social-provider-redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `callbacks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identity-linking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `protected-credentials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-synchronization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `identity-socialstream` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-identity-socialstream-filament`](https://github.com/liberusoftware/module-identity-socialstream-filament) (`liberusoftware/identity-socialstream-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/identity-socialstream.md) · [API plan](../api/identity-socialstream.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Social provider redirects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `social provider redirects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Callbacks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `callbacks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identity linking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identity linking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Protected credentials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `protected credentials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account synchronization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account synchronization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/CreateConnectedAccount.php) | `public function create(mixed $user, string $provider, ProviderUser $providerUser): ConnectedAccount` |
| [CreateUserFromProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/CreateUserFromProvider.php) | `public function __construct(CreatesConnectedAccounts $createsConnectedAccounts)`<br>`public function create(string $provider, ProviderUserContract $providerUser): User` |
| [GenerateRedirectForProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/GenerateRedirectForProvider.php) | `public function generate(string $provider): RedirectResponse` |
| [HandleInvalidState.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/HandleInvalidState.php) | `public function handle(InvalidStateException $exception): Response` |
| [ResolveSocialiteUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/ResolveSocialiteUser.php) | `public function resolve(string $provider): User` |
| [SetUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/SetUserPassword.php) | `public function set(mixed $user, array $input): void` |
| [UpdateConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/UpdateConnectedAccount.php) | `public function update(mixed $user, ConnectedAccount $connectedAccount, string $provider, User $providerUser): ConnectedAccount`<br>`public function updateRefreshToken(ConnectedAccount $connectedAccount): ConnectedAccount` |
| [ConnectedAccountOwner.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Contracts/ConnectedAccountOwner.php) | `public function ownsConnectedAccount($account)` |
| [ConnectedAccountPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Policies/ConnectedAccountPolicy.php) | `public function viewAny(ConnectedAccountOwner $user): bool`<br>`public function view(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function create(ConnectedAccountOwner $user): bool`<br>`public function update(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function delete(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConnectedAccount.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-socialstream/src/Models/ConnectedAccount.php) | `provider`, `provider_id`, `name`, `nickname`, `email`, `avatar_path`, `token`, `secret`, `refresh_token`, `expires_at` |
<!-- layer-implementation-plan:end -->
