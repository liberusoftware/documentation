# Wayfinder technical specification: Dart mobile

This is the technology-specific implementation specification for `dart-mobile` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-dart-mobile
- Reusable module foundation: https://github.com/liberusoftware/module-boilerplate-dart-mobile
- Capability skeleton catalog: [`modules/skeletons/dart-mobile.md`](../../modules/skeletons/dart-mobile.md)
- Presentation layer directory in product docs: `flutter/`
- Adapter identity pattern: `module-{capability}-dart-mobile`
- Consumes product `-laravel-api`: yes

## Delivery boundary

A distinct mobile host/release using Flutter/Dart and the product `-laravel-api`; verify touch navigation, platform lifecycle, secure local state and signed iOS/Android delivery independently of `-mobile-flutter`.

## Authoritative documentation

- [Flutter standard](../../standards/FLUTTER.md)
- [Mobile architecture](../../architecture/MOBILE.md)
- [Dart presentation guide](../../guides/presentation/DART.md)
- [Laravel API backends](../../guides/LARAVEL-API-BACKENDS.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [Dart mobile/desktop initialization](../../guides/presentation/DART.md)
- [Flutter implementation runbook](../../guides/presentation/FLUTTER.md)
- [Module index](../../modules/flutter/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Treat this repository as a separate mobile application root from `-mobile-flutter`: independent release identity, bundle IDs and store listing.
2. Use the Flutter/Dart versions pinned in `.flutter-version` / `.fvmrc`; `flutter pub get`, `analyze`, `test`, then run on iOS/Android targets.
3. Consume `project-{product}-laravel-api` with typed clients and secure storage; reuse Flutter-layer plans for widgets/clients while keeping host-specific acceptance mandatory.
4. Inject session/transport at composition; keep policy and persistence on the server; validate DTOs and error maps against the published contract.
5. Verify touch navigation, safe areas, permissions, deep links, background/resume, logout clearing and offline reconciliation on both OS families.
6. Implement one vertical journey before expanding checklist items; link child issues when ownership and acceptance are actionable.
7. Build signed artifacts (`appbundle`/`ipa`) with reviewed signing config; record store-oriented evidence separately from unit tests.
8. Keep reusable Dart/Flutter modules in their own pubspecs; replace path dependencies before release.
9. Prove clean installs from locks and compatibility with the supported API contract versions.

## Technical specification

### Host ownership
- `-dart-mobile` is a dedicated mobile product host. Shared Flutter module plans inform widgets/clients; this host still proves its own navigation, storage and release.
- Laravel API backend remains authoritative for domain rules; this app is an API consumer only.

### Transport and session
- Same HTTP contract family as other independent clients; configure API base per environment.
- Platform-secure credentials; explicit reconnect and refresh behavior; no embedded confidential client secrets.

### Package and directory contracts
- Application `publish_to: none`; reusable modules via Dart/pub with declared platforms.
- Flutter supplies the native mobile host (rendering, accessibility, plugins)—not a console-only Dart app.

### Security and tenancy
- Account-isolated local state; purge on logout; validate deep links.
- Never present queued local writes as completed server transactions.

### Verification and release
- Dual-OS mobile acceptance; signed build evidence; API compatibility window documented in the host README.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)
