# React Native + Expo module implementations

Each React Native package presents exactly one matching API/core module. Use the naming convention module-{independent-module-name}-react-native and keep domain behavior in the core package.

## Implementation requirements

Use TypeScript strict mode, typed navigation, schema-validated API responses, secure credential storage, platform permission boundaries, explicit offline/retry/conflict state, and accessible native controls. Test iOS and Android behavior separately where platform APIs differ.

| Concern                                                 | Owner                   |
| ------------------------------------------------------- | ----------------------- |
| Domain invariants, authorization, tenancy, audit        | Core/API packages       |
| Navigation, screens, native permissions, secure storage | React Native package    |
| API schema and error contract                           | Matching API package    |
| Device release, signing, store metadata                 | Host mobile application |

See [React Native technology](../../technologies/REACT-NATIVE.md), [Expo build and publishing](../../technologies/EXPO.md), [frontend testing](../../technologies/FRONTEND-TESTING.md), [React Native standard](../../standards/REACT-NATIVE.md), [mobile architecture](../../architecture/MOBILE.md), and [project indexes](../mobile/README.md).

## Project specification indexes

These counts describe documents, not released packages. Consult the [source inventory](../../architecture/SOURCE-INVENTORY.md) for actual manifests.

| Project | Specification documents |
| --- | ---: |
| [accounting](../../projects/accounting/react-native/README.md) | 241 |
| [automation](../../projects/automation/react-native/README.md) | 57 |
| [billing](../../projects/billing/react-native/README.md) | 81 |
| [boilerplate](../../projects/boilerplate/react-native/README.md) | 43 |
| [browser-game](../../projects/browser-game/react-native/README.md) | 61 |
| [cms](../../projects/cms/react-native/README.md) | 252 |
| [control-panel](../../projects/control-panel/react-native/README.md) | 61 |
| [crm](../../projects/crm/react-native/README.md) | 218 |
| [ecommerce](../../projects/ecommerce/react-native/README.md) | 107 |
| [genealogy](../../projects/genealogy/react-native/README.md) | 62 |
| [liberu](../../projects/liberu/react-native/README.md) | 4 |
| [maintenance](../../projects/maintenance/react-native/README.md) | 60 |
| [real-estate](../../projects/real-estate/react-native/README.md) | 70 |
| [sap](../../projects/sap/react-native/README.md) | 16 |
| [social-network](../../projects/social-network/react-native/README.md) | 59 |

## Build the application and adapter

Follow the [implementation runbook](../../guides/presentation/REACT-NATIVE.md) for a skeleton, concrete integration steps, package builds and releases. Begin with the [shared architecture/foundation setup](../../guides/presentation/README.md); the module plans above do not imply registry availability.
