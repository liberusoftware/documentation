# Roles Permissions React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#roles-permissions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-boilerplate-roles-permissions-react-native
**Matching core package:** module-boilerplate-roles-permissions ([implementation](../core/roles-permissions.md))
**Matching API package:** module-boilerplate-roles-permissions-api ([contract](../api/roles-permissions.md))

## Implementation plan

This adapter presents Roles Permissions for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Roles Permissions API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/roles-permissions.md), and [API module](../api/roles-permissions.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `roles-permissions`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/roles-permissions.md)) |
| Capability React Native module skeleton | [`module-roles-permissions-react-native`](https://github.com/liberusoftware/module-roles-permissions-react-native) (`@liberusoftware/module-roles-permissions-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Permission definitions** | Progressive mobile list/detail/sheet flow for `permission definitions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assignments** | Progressive mobile list/detail/sheet flow for `assignments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contextual scope** | Progressive mobile list/detail/sheet flow for `contextual scope` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policies** | Progressive mobile list/detail/sheet flow for `policies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Caches** | Progressive mobile list/detail/sheet flow for `caches` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Safeguards** | Progressive mobile list/detail/sheet flow for `safeguards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Audit** | Progressive mobile list/detail/sheet flow for `audit` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-boilerplate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PrivilegedActor.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Contracts/PrivilegedActor.php) | `public function authorizationIdentifier(): int\|string`<br>`public function authorizationType(): string`<br>`public function hasRoleInAnyTeam(string\|array $roles): bool`<br>`public function isSuperAdmin(): bool` |
| [RolePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Policies/RolePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Role $role): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Role $role): bool`<br>`public function delete(AuthUser $authUser, Role $role): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Role $role): bool`<br>`public function forceDelete(AuthUser $authUser, Role $role): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Role $role): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [AnyTeamRoleLookup.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/AnyTeamRoleLookup.php) | `public function hasRoleInAnyTeam(PrivilegedActor $actor, string\|array $roles): bool` |
| [BreakGlass.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/BreakGlass.php) | `public function grant(string\|int $actorId, string $permission, string $reason, \DateTimeImmutable $expiresAt, bool $stronglyAuthenticated): int`<br>`public function active(string\|int $actorId, string $permission): bool` |
| [SeparationOfDuty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions/src/Services/SeparationOfDuty.php) | `public function permits(string\|int $requester, string\|int $approver, bool $material = true): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Permission.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions/src/Models/Permission.php) | No literal fillable array detected; inspect the model and API schema. |
| [Role.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions/src/Models/Role.php) | No literal fillable array detected; inspect the model and API schema. |

**Observed route declarations:**

[modules/roles-permissions-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions-api/routes/api.php)

```php
Route::prefix('api/v1/roles-permissions')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('roles-permissions-api.status');
```
<!-- layer-implementation-plan:end -->
