# Evidence Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#evidence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-evidence-flutter
**Matching core package:** module-genealogy-evidence ([implementation](../core/evidence.md))
**Matching API package:** module-genealogy-evidence-api ([contract](../api/evidence.md))

## Implementation plan

This adapter presents Evidence for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Evidence API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/evidence.md), and [API module](../api/evidence.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `evidence`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) | [`module-genealogy-evidence-flutter`](https://github.com/liberusoftware/module-genealogy-evidence-flutter) (`module_genealogy_evidence_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) | [`module-genealogy-evidence-dart-mobile`](https://github.com/liberusoftware/module-genealogy-evidence-dart-mobile) (`module_genealogy_evidence_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) | [`module-genealogy-evidence-dart-desktop`](https://github.com/liberusoftware/module-genealogy-evidence-dart-desktop) (`module_genealogy_evidence_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | [API plan](../api/evidence.md) · [Core plan](../core/evidence.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Sources** | Adaptive mobile cards/sheets for `sources` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sources` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Repositories** | Adaptive mobile cards/sheets for `repositories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `repositories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Citations** | Adaptive mobile cards/sheets for `citations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `citations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Extracts** | Adaptive mobile cards/sheets for `extracts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `extracts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Assertions** | Adaptive mobile cards/sheets for `assertions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `assertions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Confidence** | Adaptive mobile cards/sheets for `confidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `confidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Proof conclusions** | Adaptive mobile cards/sheets for `proof conclusions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `proof conclusions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/ArchiveEvidenceRecord.php) | `public function execute(EvidenceRecord $record): EvidenceRecord` |
| [CreateAssertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateAssertion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Assertion` |
| [CreateCitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitation.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Citation` |
| [CreateCitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitationLink.php) | `public function execute(array $attributes): CitationLink` |
| [CreateEvidenceEntity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceEntity.php) | `public function execute(string $modelClass, array $attributes): Model`<br>`public function validate(array $values, string $modelClass): void` |
| [CreateEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceRecord.php) | `public function execute(array $attributes): EvidenceRecord`<br>`public function validate(array $values): void` |
| [CreateExtract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateExtract.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Extract` |
| [CreateProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateProofConclusion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): ProofConclusion` |
| [CreateRepository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateRepository.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Repository` |
| [CreateSource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateSource.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Source` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Assertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Assertion.php) | `subject_person_id`, `citation_id`, `extract_id`, `statement`, `confidence`, `status`, `metadata` |
| [Citation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Citation.php) | `source_id`, `repository_id`, `title`, `volume`, `page`, `text`, `confidence`, `event_date`, `metadata` |
| [CitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/CitationLink.php) | `team_id`, `citation_id`, `subject_person_id`, `group`, `page`, `quality`, `text`, `metadata` |
| [EvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/EvidenceRecord.php) | `team_id`, `name`, `kind`, `repository`, `citation`, `extract`, `assertion`, `proof_conclusion`, `confidence`, `source_url`, `event_date`, `subject_person_id`, `reviewed_at`, `status`, `metadata` |
| [Extract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Extract.php) | `citation_id`, `content`, `transcription`, `page`, `metadata` |
| [ProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/ProofConclusion.php) | `assertion_id`, `conclusion`, `confidence`, `status`, `metadata` |
| [Repository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Repository.php) | `source_id`, `name`, `description`, `address`, `url`, `email`, `is_active`, `metadata` |
| [Source.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Source.php) | `name`, `description`, `url`, `archive_metadata`, `record_type`, `is_active`, `metadata` |
<!-- layer-implementation-plan:end -->
