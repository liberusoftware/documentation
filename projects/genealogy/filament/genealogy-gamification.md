# Genealogy: Genealogy Gamification Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-gamification). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-genealogy-gamification-filament`  
**Matching domain module:** `genealogy-gamification`  
**Application:** Genealogy  
**Source feature:** [Genealogy Gamification](../features/genealogy-gamification.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-gamification` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Genealogy gamification points:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Genealogy gamification achievements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Genealogy gamification progress:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Genealogy gamification leaderboard:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-genealogy-gamification-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `genealogy-gamification-points`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `genealogy-gamification-achievements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `genealogy-gamification-progress`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `genealogy-gamification-leaderboard`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-gamification` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-gamification-filament`](https://github.com/liberusoftware/module-genealogy-gamification-filament) (`liberusoftware/genealogy-gamification-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-gamification.md) · [API plan](../api/genealogy-gamification.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Genealogy gamification points** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `genealogy gamification points`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Genealogy gamification achievements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `genealogy gamification achievements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Genealogy gamification progress** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `genealogy gamification progress`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Genealogy gamification leaderboard** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `genealogy gamification leaderboard`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AwardPoints.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Actions/AwardPoints.php) | `public function execute(Model $user, string $activityType, int $points, ?string $description = null, array $metadata = [], ?Model $related = null): UserPoint` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Achievement.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/Achievement.php) | `key`, `name`, `description`, `category`, `points`, `requirements`, `is_active`, `sort_order` |
| [UserAchievement.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/UserAchievement.php) | `team_id`, `user_id`, `achievement_id`, `unlocked_at`, `progress_data` |
| [UserPoint.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/UserPoint.php) | `team_id`, `user_id`, `activity_type`, `points`, `description`, `metadata`, `related_id`, `related_type` |
| [UserProgress.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/UserProgress.php) | `team_id`, `user_id`, `achievement_id`, `current_progress`, `target_progress`, `progress_data`, `started_at`, `last_updated_at` |
<!-- layer-implementation-plan:end -->
