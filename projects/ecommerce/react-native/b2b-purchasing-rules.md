# B2b Purchasing Rules React Native + Expo

**Package:** module-ecommerce-b2b-purchasing-rules-react-native
**Matching core package:** module-ecommerce-b2b-purchasing-rules ([implementation](../core/b2b-purchasing-rules.md))
**Matching API package:** module-ecommerce-b2b-purchasing-rules-api ([contract](../api/b2b-purchasing-rules.md))

## Implementation plan

This adapter presents B2b Purchasing Rules for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test B2b Purchasing Rules API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/b2b-purchasing-rules.md), and [API module](../api/b2b-purchasing-rules.md).
