# CMS: Drupal Migration Vue + Inertia

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-cms-drupal-migration-vue-inertia`
**Matching domain module:** `cms-drupal-migration`
**Application:** CMS
**Source feature:** [Drupal Migration](../features/drupal-migration.md)
**Architecture:** [VUE-INERTIA.md](../../../architecture/VUE-INERTIA.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/drupal-migration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../architecture/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Entity/bundle/field data:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Revisions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Moderation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Taxonomy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Media:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Menus:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Views mapping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Translations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Configuration evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-cms-drupal-migration-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `entity-bundle-field-data`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `revisions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `moderation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `taxonomy`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `media`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `menus`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `views-mapping`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `translations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `configuration-evidence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `cms-drupal-migration` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
