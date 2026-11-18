# CRM: Consent and Preferences Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#consent-and-preferences). Observed identity: [`liberusoftware/module-crm-consent-and-preferences-filament`](../../../modules/source/liberusoftware--module-crm-consent-and-preferences-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-consent-and-preferences-filament`  
**Matching domain module:** `crm-consent-and-preferences`  
**Application:** CRM  
**Source feature:** [Consent and Preferences](../features/consent-and-preferences.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-consent-and-preferences` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Lawful basis:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Subscriptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel/topic preferences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suppression:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quiet hours:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recording consent:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Proof:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Withdrawal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policy evaluation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-consent-and-preferences-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `lawful-basis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `subscriptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel-topic-preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suppression`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quiet-hours`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recording-consent`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `proof`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `withdrawal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policy-evaluation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-consent-and-preferences` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-consent-and-preferences-filament`](https://github.com/liberusoftware/module-crm-consent-and-preferences-filament) (`liberusoftware/crm-consent-and-preferences-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/consent-and-preferences.md) · [API plan](../api/consent-and-preferences.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Lawful basis** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lawful basis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Subscriptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `subscriptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channel/topic preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channel/topic preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suppression** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suppression`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quiet hours** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quiet hours`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recording consent** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recording consent`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Proof** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `proof`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expiry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expiry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Withdrawal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `withdrawal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policy evaluation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policy evaluation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ConsentAndPreferencesFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-filament/src/ConsentAndPreferencesFilamentPlugin.php) · [ConsentAndPreferencesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-filament/src/ConsentAndPreferencesFilamentServiceProvider.php) · [ConsentRecordResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-filament/src/Resources/ConsentRecordResource.php) · [CreateConsentRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-filament/src/Resources/ConsentRecordResource/Pages/CreateConsentRecord.php) · [EditConsentRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-filament/src/Resources/ConsentRecordResource/Pages/EditConsentRecord.php) · [ListConsentRecords.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-filament/src/Resources/ConsentRecordResource/Pages/ListConsentRecords.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/GrantConsent.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): ConsentRecord` |
| [SetPreference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SetPreference.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic, array $values, ?int $actorId = null): PreferenceRecord` |
| [SuppressSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SuppressSubject.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): SuppressionRecord` |
| [WithdrawConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/WithdrawConsent.php) | `public function execute(ConsentRecord $record): ConsentRecord` |
| [PolicyEvaluator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Services/PolicyEvaluator.php) | `public function evaluate(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic = 'general', ?Carbon $at = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConsentRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/ConsentRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `lawful_basis`, `status`, `source`, `proof`, `consented_at`, `expires_at`, `withdrawn_at`, `actor_id` |
| [PolicyEvaluation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PolicyEvaluation.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `allowed`, `reasons`, `evaluated_at` |
| [PreferenceRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PreferenceRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `state`, `quiet_hours`, `timezone`, `actor_id` |
| [SuppressionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/SuppressionRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `reason`, `source`, `expires_at`, `withdrawn_at`, `actor_id` |
<!-- layer-implementation-plan:end -->
