# Wayfinder technical specification: Dart desktop

This is the technology-specific implementation specification for `dart-desktop` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-dart-desktop
- Reusable module foundation: https://github.com/liberusoftware/module-boilerplate-dart-desktop
- Capability skeleton catalog: [`modules/skeletons/dart-desktop.md`](../../modules/skeletons/dart-desktop.md)
- Presentation layer directory in product docs: `flutter/`
- Adapter identity pattern: `module-{capability}-dart-desktop`
- Consumes product `-laravel-api`: yes

## Delivery boundary

A distinct desktop host/release using Flutter/Dart and the product `-laravel-api`; verify keyboard/focus, resizing, multi-window consistency, platform storage and safe printing/export independently.

## Authoritative documentation

- [Flutter standard](../../standards/FLUTTER.md)
- [Dart presentation guide](../../guides/presentation/DART.md)
- [API architecture](../../architecture/API.md)
- [Laravel API backends](../../guides/LARAVEL-API-BACKENDS.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [Dart mobile/desktop initialization](../../guides/presentation/DART.md)
- [Flutter implementation runbook](../../guides/presentation/FLUTTER.md)
- [Module index](../../modules/flutter/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Treat this repository as a separate desktop application root: independent release identity and OS packaging from mobile hosts.
2. Use the pinned Flutter/Dart toolchain; enable Linux/macOS/Windows targets as product support requires; `flutter pub get`, `analyze`, `test`.
3. Point desktop builds at `project-{product}-laravel-api`; implement desktop-safe credential storage and session lifecycle for the threat model.
4. Design for keyboard navigation, focus order, resizing, window close/reopen and optional multi-window concurrency without corrupting drafts.
5. Inject typed API repositories; validate DTOs; keep domain authority on the server; define print/export as authorized, audience-safe operations.
6. Deliver one vertical journey with desktop interaction evidence; expand via Flutter-layer plans and SOURCE-MAPPING.md.
7. Build native artifacts (`flutter build linux|macos|windows`) on the matching OS tooling; record installer/notarization requirements separately.
8. Replace path dependencies with reviewed module versions before release; keep `publish_to: none` on the application pubspec.
9. Prove clean lock installs, API compatibility and operational recovery notes for desktop deployments.

## Technical specification

### Host ownership
- `-dart-desktop` is a dedicated desktop product host using Flutter for windowing/rendering. It consumes the product Laravel API.
- Desktop UX requirements (keyboard, focus, windowing, printing/export) are mandatory acceptance—even when sharing Flutter module plans with mobile.

### Transport and session
- Reviewed HTTP contracts; environment-specific API base; secure local credential storage appropriate to desktop OS.
- Handle connectivity loss without implying server success for local-only state.

### Package and directory contracts
- Application owns platform runners and packaging; reusable UI/contracts are Dart/pub modules with desktop platform support declared.
- Do not assume mobile plugins work on desktop—review each dependency’s platforms.

### Security and tenancy
- Authorize exports/prints/files access; avoid writing private data to shared desktop paths without scoping.
- Clear session-scoped caches on logout; protect local drafts per account.

### Verification and release
- Verify keyboard/focus/resize/window lifecycle on each supported OS; signed/notarized installers as required by the distribution channel.
- Unit/widget tests do not replace native desktop build verification.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)
