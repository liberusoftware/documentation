# CMS: Comments and Discussion Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#comments-and-discussion). Observed identity: [`liberusoftware/module-cms-comments-and-discussion-filament`](../../../modules/source/liberusoftware--module-cms-comments-and-discussion-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-comments-and-discussion-filament`  
**Matching domain module:** `cms-comments-and-discussion`  
**Application:** CMS  
**Source feature:** [Comments and Discussion](../features/comments-and-discussion.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-comments-and-discussion` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Threaded comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Guest/member policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Subscriptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mentions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spam control:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Editing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-comments-and-discussion-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `threaded-comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `guest-member-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `subscriptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mentions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spam-control`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `editing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-comments-and-discussion` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-comments-and-discussion-filament`](https://github.com/liberusoftware/module-cms-comments-and-discussion-filament) (`liberusoftware/cms-comments-and-discussion-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/comments-and-discussion.md) · [API plan](../api/comments-and-discussion.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Threaded comments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `threaded comments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Guest/member policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guest/member policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Moderation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `moderation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Subscriptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `subscriptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mentions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mentions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Spam control** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `spam control`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Editing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `editing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CommentsAndDiscussionFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-comments-and-discussion-filament/src/CommentsAndDiscussionFilamentServiceProvider.php) · [CommentResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-comments-and-discussion-filament/src/Resources/CommentResource.php) · [ListComments.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-comments-and-discussion-filament/src/Resources/Pages/ListComments.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CommentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Services/CommentService.php) | `public function list(string $type, string $id, ?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $authorId = null, ?int $teamId = null): Comment`<br>`public function update(Comment $comment, string $body, ?int $actorId = null, bool $moderator = false): Comment`<br>`public function moderate(Comment $comment, string $status): Comment`<br>`public function report(Comment $comment, string $reason, ?int $reporterId = null): CommentReport`<br>`public function subscribe(Comment $comment, int $subscriberId): CommentSubscription`<br>`public function prune(int $retentionDays = 0): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Comment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Models/Comment.php) | `team_id`, `commentable_type`, `commentable_id`, `parent_id`, `author_id`, `guest_name`, `guest_email`, `body`, `status`, `metadata` |
| [CommentReport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Models/CommentReport.php) | `comment_id`, `reporter_id`, `reason`, `status` |
| [CommentSubscription.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Models/CommentSubscription.php) | `comment_id`, `subscriber_id` |
<!-- layer-implementation-plan:end -->
