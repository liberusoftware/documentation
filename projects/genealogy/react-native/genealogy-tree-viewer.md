# Genealogy Tree Viewer React Native + Expo

**Package:** module-genealogy-genealogy-tree-viewer-react-native
**Matching core package:** module-genealogy-genealogy-tree-viewer ([implementation](../core/genealogy-tree-viewer.md))
**Matching API package:** module-genealogy-genealogy-tree-viewer-api ([contract](../api/genealogy-tree-viewer.md))

## Implementation plan

This adapter presents Genealogy Tree Viewer for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Genealogy Tree Viewer API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/genealogy-tree-viewer.md), and [API module](../api/genealogy-tree-viewer.md).
