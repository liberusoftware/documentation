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
