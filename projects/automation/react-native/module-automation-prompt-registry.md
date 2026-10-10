# Module Automation Prompt Registry React Native + Expo

**Package:** module-automation-module-automation-prompt-registry-react-native
**Matching core package:** module-automation-module-automation-prompt-registry ([implementation](../core/module-automation-prompt-registry.md))
**Matching API package:** module-automation-module-automation-prompt-registry-api ([contract](../api/module-automation-prompt-registry.md))

## Implementation plan

This adapter presents Module Automation Prompt Registry for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Automation Prompt Registry API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-automation-prompt-registry.md), and [API module](../api/module-automation-prompt-registry.md).
