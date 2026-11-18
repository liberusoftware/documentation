# Automation: Module Automation Voice Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-automation-voice). Observed identity: [`liberusoftware/automation-voice-filament`](../../../modules/source/liberusoftware--automation-voice-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-module-automation-voice-filament`  
**Matching domain module:** `module-automation-voice`  
**Application:** Automation  
**Source feature:** [Module Automation Voice](../features/module-automation-voice.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-automation-voice` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Speech-to-text:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Text-to-speech:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Streaming sessions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Interruption:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transcripts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent controls:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-module-automation-voice-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `speech-to-text`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `text-to-speech`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `streaming-sessions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `interruption`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transcripts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-automation-voice` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-automation-voice-filament`](https://github.com/liberusoftware/module-automation-voice-filament) (`liberusoftware/automation-voice-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-automation-voice.md) · [API plan](../api/module-automation-voice.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Speech-to-text** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `speech-to-text`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Text-to-speech** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `text-to-speech`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Streaming sessions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `streaming sessions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Interruption** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `interruption`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transcripts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transcripts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [VoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-filament/src/Resources/VoiceResource.php) · [CreateVoice.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-filament/src/Resources/VoiceResource/Pages/CreateVoice.php) · [EditVoice.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-filament/src/Resources/VoiceResource/Pages/EditVoice.php) · [ListVoice.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-filament/src/Resources/VoiceResource/Pages/ListVoice.php) · [VoiceFilamentPlugin.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-filament/src/VoiceFilamentPlugin.php) · [VoiceFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-filament/src/VoiceFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateVoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice/src/Actions/CreateVoiceResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): VoiceResource` |
| [TransitionVoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice/src/Actions/TransitionVoiceResource.php) | `public function execute(VoiceResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): VoiceResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice/src/Models/VoiceResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
