# Flutter + Dart module implementations

Each Flutter package presents exactly one matching API/core module. Use the naming convention module-{independent-module-name}-flutter and keep domain behavior in the core package.

## Implementation requirements

Use sound null safety, typed DTOs, stable Flutter plugins, secure credential storage, explicit offline/retry/conflict state, adaptive accessible widgets, and platform-aware permission boundaries. Test Dart logic, widgets, API mapping, integration flows, and release builds.

| Concern                                               | Owner                   |
| ----------------------------------------------------- | ----------------------- |
| Domain invariants, authorization, tenancy, audit      | Core/API packages       |
| Navigation, widgets, platform plugins, secure storage | Flutter package         |
| API schema and error contract                         | Matching API package    |
| Device release, signing, store metadata               | Host mobile application |

See [Flutter technology](../../technologies/FLUTTER.md), [Flutter standard](../../standards/FLUTTER.md), [mobile architecture](../../architecture/MOBILE.md), and [project indexes](../mobile/README.md).
