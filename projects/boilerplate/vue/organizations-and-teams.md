# Boilerplate: Organizations and Teams Vue presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#organizations-and-teams). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `organizations-teams`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-organizations-and-teams-vue`
**Matching core package:** [`module-organizations-and-teams`](../core/organizations-and-teams.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Organizations, teams, memberships, invitations, ownership, switching, transfer, and lifecycle.

## Adapter implementation plan

This package presents the Organizations and Teams core capability through Vue. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Organizations and Teams core boundary.

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-organizations-teams-vue-inertia`](https://github.com/liberusoftware/module-organizations-teams-vue-inertia) (`@liberusoftware/module-organizations-teams-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/organizations-and-teams.md) · [Core plan](../core/organizations-and-teams.md) · [API plan](../api/organizations-and-teams.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Organizations** | Render `organizations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Teams** | Render `teams` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Memberships** | Render `memberships` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Invitations** | Render `invitations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Ownership** | Render `ownership` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Switching** | Render `switching` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Transfer** | Render `transfer` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Lifecycle** | Render `lifecycle` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptInvitation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [InviteMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [TransferOwnership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [OrganizationActor.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [TeamPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [CurrentTeamResolver.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Membership.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Membership.php) | No literal fillable array detected; inspect the model and API schema. |
| [Organization.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Organization.php) | `name`, `slug`, `owner_id`, `status`, `archived_at` |
| [Team.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Team.php) | `name`, `personal_team`, `organization_id`, `status` |
| [TeamInvitation.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/TeamInvitation.php) | `email`, `role`, `token_hash`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |

**Observed route declarations:**

[modules/organizations-teams-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams-api/routes/api.php)

```php
Route::prefix('api/v1/organizations-teams')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('organizations-teams-api.status');
```
<!-- layer-implementation-plan:end -->
