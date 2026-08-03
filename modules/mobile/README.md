# Mobile module implementations

Mobile modules are optional presentation packages for React Native/Expo and Flutter/Dart applications. They consume the matching API or approved core contracts and never own domain rules, persistence, authorization, tenancy, or audit decisions.

## Package shape

```text
module-{independent-module-name}-react-native
module-{independent-module-name}-flutter
        |
        v
module-{independent-module-name}-api
        |
        v
module-{independent-module-name}
```

Create one adapter per independently installable domain capability. Keep API schemas, actions, queries, policies, and error semantics aligned across web and mobile surfaces. A mobile package should document platform permissions, offline behavior, cache classification, deep links, push events, accessibility, supported OS versions, release configuration, and tests.

## Project indexes

| Project        | React Native                                                         | Flutter                                                    |
| -------------- | -------------------------------------------------------------------- | ---------------------------------------------------------- |
| Accounting     | [React Native](../../projects/accounting/react-native/README.md)     | [Flutter](../../projects/accounting/flutter/README.md)     |
| Automation     | [React Native](../../projects/automation/react-native/README.md)     | [Flutter](../../projects/automation/flutter/README.md)     |
| Billing        | [React Native](../../projects/billing/react-native/README.md)        | [Flutter](../../projects/billing/flutter/README.md)        |
| Browser Game   | [React Native](../../projects/browser-game/react-native/README.md)   | [Flutter](../../projects/browser-game/flutter/README.md)   |
| CMS            | [React Native](../../projects/cms/react-native/README.md)            | [Flutter](../../projects/cms/flutter/README.md)            |
| Control Panel  | [React Native](../../projects/control-panel/react-native/README.md)  | [Flutter](../../projects/control-panel/flutter/README.md)  |
| CRM            | [React Native](../../projects/crm/react-native/README.md)            | [Flutter](../../projects/crm/flutter/README.md)            |
| Ecommerce      | [React Native](../../projects/ecommerce/react-native/README.md)      | [Flutter](../../projects/ecommerce/flutter/README.md)      |
| Genealogy      | [React Native](../../projects/genealogy/react-native/README.md)      | [Flutter](../../projects/genealogy/flutter/README.md)      |
| Liberu         | [React Native](../../projects/liberu/react-native/README.md)         | [Flutter](../../projects/liberu/flutter/README.md)         |
| Maintenance    | [React Native](../../projects/maintenance/react-native/README.md)    | [Flutter](../../projects/maintenance/flutter/README.md)    |
| Real Estate    | [React Native](../../projects/real-estate/react-native/README.md)    | [Flutter](../../projects/real-estate/flutter/README.md)    |
| SAP            | [React Native](../../projects/sap/react-native/README.md)            | [Flutter](../../projects/sap/flutter/README.md)            |
| Social Network | [React Native](../../projects/social-network/react-native/README.md) | [Flutter](../../projects/social-network/flutter/README.md) |

See [mobile architecture](../../architecture/MOBILE.md), [mobile standard](../../standards/MOBILE.md), [React Native](../../technologies/REACT-NATIVE.md), and [Flutter](../../technologies/FLUTTER.md).
