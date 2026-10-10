# Crm Prospecting Agent Flutter + Dart

**Package:** module-crm-crm-prospecting-agent-flutter
**Matching core package:** module-crm-crm-prospecting-agent ([implementation](../core/crm-prospecting-agent.md))
**Matching API package:** module-crm-crm-prospecting-agent-api ([contract](../api/crm-prospecting-agent.md))

## Implementation plan

This adapter presents Crm Prospecting Agent for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Prospecting Agent API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-prospecting-agent.md), and [API module](../api/crm-prospecting-agent.md).
