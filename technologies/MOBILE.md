# Mobile technology reference

Mobile clients are optional presentation layers over Liberu APIs. React Native/Expo and Flutter/Dart may share API contracts and product terminology, but each platform owns its navigation, local state, device integration, accessibility behavior, release process, and offline experience.

## Choose a client

| Need                                  | React Native + Expo      | Flutter             |
| ------------------------------------- | ------------------------ | ------------------- |
| Share TypeScript with web clients     | Strong fit               | Requires Dart       |
| Reuse native modules and React skills | Strong fit               | Use Flutter plugins |
| Consistent cross-platform rendering   | Shared native components | Flutter widget tree |
| Existing Liberu contract              | REST/OpenAPI API         | REST/OpenAPI API    |

The choice must be recorded in the project scope and compatibility matrix. Do not add both clients solely to duplicate functionality; use both when product requirements, team boundaries, or platform distribution justify it.

## Shared rules

- Keep business rules, authorization, tenancy, consent, and audit on the Laravel/API boundary.
- Use versioned API schemas, stable identifiers, idempotent writes, pagination, and RFC 9457-compatible error mapping.
- Store credentials only in platform-secure storage; use short-lived access and refresh policies appropriate to the threat model.
- Model loading, empty, unauthorized, offline, stale, queued, conflict, and recovery states explicitly.
- Support localization, timezone/currency formatting, right-to-left layouts, dynamic text, reduced motion, screen readers, and platform conventions.
- Test supported OS versions, permission denial, interrupted connectivity, app restarts, deep links, upgrades, and release builds.

See [mobile architecture](../architecture/MOBILE.md), [React Native](REACT-NATIVE.md), [Flutter](FLUTTER.md), [React Native standard](../standards/REACT-NATIVE.md), and [Flutter standard](../standards/FLUTTER.md).
