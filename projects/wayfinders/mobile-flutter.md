# Wayfinder technical specification: Flutter mobile

This is the technology-specific implementation specification for `mobile-flutter` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-mobile-flutter
- Presentation layer directory in product docs: `flutter/`
- Adapter identity pattern: `module-{capability}-flutter`
- Consumes product `-laravel-api`: yes

## Delivery boundary

Consume the product `-laravel-api` with typed Dart clients, secure device credentials, native widget semantics, account-isolated drafts and lifecycle/reconnect handling.

## Authoritative documentation

- [Flutter standard](../../standards/FLUTTER.md)
- [Mobile architecture](../../architecture/MOBILE.md)
- [Mobile standard](../../standards/MOBILE.md)
- [Laravel API backends](../../guides/LARAVEL-API-BACKENDS.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [Flutter implementation runbook](../../guides/presentation/FLUTTER.md)
- [Module index](../../modules/flutter/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Start from the Flutter mobile Boilerplate; use the pinned Flutter/Dart toolchain; `flutter pub get`, `analyze`, `test`, then run on a listed device.
2. Replace skeleton application IDs/display names/signing with product-owned identifiers; keep `publish_to: none` and commit `pubspec.lock`.
3. Configure the API base (for example `--dart-define`) to `project-{{product}}-laravel-api`; treat that value as public configuration, not a secret store.
4. Implement reviewed mobile auth; store long-lived secrets in platform-secure storage; coordinate refresh in one place; clear credentials and scoped caches on logout.
5. Separate `data`/`presentation`/`contracts`; inject repositories; widgets emit intent and render state—they do not authorize or open database connections.
6. Validate JSON into checked DTOs; preserve pagination and error mapping; document real HTTP cancellation behavior (future timeouts alone are insufficient).
7. Build mobile layouts with semantics, safe areas and platform navigation; define offline/draft reconciliation explicitly before enabling queued writes.
8. Ship one vertical journey with tests and device evidence; expand using `flutter/` plans and SOURCE-MAPPING.md without duplicating domain rules.
9. Prove evidence: analyze/test, auth lifecycle, tenant denial, background/resume, and signed `appbundle`/`ipa` build notes for release candidates.

## Technical specification

### Host ownership
- This repository is the general Flutter mobile foundation for the product. Domain ownership stays in Laravel modules and the product API host.
- Application owns composition, routes, environment and platform projects; packages own reusable widgets and DTO mapping.
- Do not copy desktop/web layouts; implement native mobile information architecture.

### Transport and session
- Typed Dart HTTP (or approved client) against reviewed OpenAPI operations.
- Secure credential storage and bounded refresh; reauthenticate when refresh fails.
- Local drafts are non-authoritative until the server confirms the transition.

### Package and directory contracts
- Capability packages use Dart/pub (`module-{capability}-flutter` or documented identity) with explicit supported platforms.
- Path dependencies are for temporary integration only; releases use reviewed hosted/Git versions.
- Avoid adding `package.json` to represent Dart packages.

### Security and tenancy
- Every API call carries the established actor/workspace context required by the contract.
- Isolate caches and draft queues per account/workspace; purge on logout.
- Validate deep links and permission-gated platform features before use.

### Verification and release
- `flutter analyze` and widget tests are necessary but not sufficient—record device and signed-build evidence.
- Support both iOS and Android acceptance for products that ship both stores.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)
