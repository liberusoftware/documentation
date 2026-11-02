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

## Project specification indexes

These counts describe documents, not released packages. Consult the [source inventory](../../architecture/SOURCE-INVENTORY.md) for actual manifests.

| Project | Specification documents |
| --- | ---: |
| [accounting](../../projects/accounting/flutter/README.md) | 241 |
| [automation](../../projects/automation/flutter/README.md) | 57 |
| [billing](../../projects/billing/flutter/README.md) | 81 |
| [boilerplate](../../projects/boilerplate/flutter/README.md) | 43 |
| [browser-game](../../projects/browser-game/flutter/README.md) | 61 |
| [cms](../../projects/cms/flutter/README.md) | 252 |
| [control-panel](../../projects/control-panel/flutter/README.md) | 61 |
| [crm](../../projects/crm/flutter/README.md) | 218 |
| [ecommerce](../../projects/ecommerce/flutter/README.md) | 107 |
| [genealogy](../../projects/genealogy/flutter/README.md) | 62 |
| [liberu](../../projects/liberu/flutter/README.md) | 4 |
| [maintenance](../../projects/maintenance/flutter/README.md) | 60 |
| [real-estate](../../projects/real-estate/flutter/README.md) | 70 |
| [sap](../../projects/sap/flutter/README.md) | 16 |
| [social-network](../../projects/social-network/flutter/README.md) | 59 |

## Build the application and adapter

Follow the [implementation runbook](../../guides/presentation/FLUTTER.md) for a skeleton, concrete integration steps, package builds and releases. Begin with the [shared architecture/foundation setup](../../guides/presentation/README.md); the module plans above do not imply registry availability.
