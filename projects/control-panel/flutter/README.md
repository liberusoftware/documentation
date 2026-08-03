# Control Panel Flutter + Dart implementations

**Scope:** [Control Panel](../CONTROL-PANEL.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Control Panel project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-flutter`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [Flutter + Dart module standard](../../../modules/flutter/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 15 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                      | Package                                         | Core                                  | API                                 |
| ------------------------------------------- | ----------------------------------------------- | ------------------------------------- | ----------------------------------- |
| [Accounts](accounts.md)                     | module-control-panel-accounts-flutter           | [Core](../core/accounts.md)           | [API](../api/accounts.md)           |
| [Api And Automation](api-and-automation.md) | module-control-panel-api-and-automation-flutter | [Core](../core/api-and-automation.md) | [API](../api/api-and-automation.md) |
| [Backups](backups.md)                       | module-control-panel-backups-flutter            | [Core](../core/backups.md)            | [API](../api/backups.md)            |
| [Certificates](certificates.md)             | module-control-panel-certificates-flutter       | [Core](../core/certificates.md)       | [API](../api/certificates.md)       |
| [Containers](containers.md)                 | module-control-panel-containers-flutter         | [Core](../core/containers.md)         | [API](../api/containers.md)         |
| [Control Core](control-core.md)             | module-control-panel-control-core-flutter       | [Core](../core/control-core.md)       | [API](../api/control-core.md)       |
| [Databases](databases.md)                   | module-control-panel-databases-flutter          | [Core](../core/databases.md)          | [API](../api/databases.md)          |
| [Dns](dns.md)                               | module-control-panel-dns-flutter                | [Core](../core/dns.md)                | [API](../api/dns.md)                |
| [Files](files.md)                           | module-control-panel-files-flutter              | [Core](../core/files.md)              | [API](../api/files.md)              |
| [Kubernetes](kubernetes.md)                 | module-control-panel-kubernetes-flutter         | [Core](../core/kubernetes.md)         | [API](../api/kubernetes.md)         |
| [Mail](mail.md)                             | module-control-panel-mail-flutter               | [Core](../core/mail.md)               | [API](../api/mail.md)               |
| [Monitoring](monitoring.md)                 | module-control-panel-monitoring-flutter         | [Core](../core/monitoring.md)         | [API](../api/monitoring.md)         |
| [Os Adapters](os-adapters.md)               | module-control-panel-os-adapters-flutter        | [Core](../core/os-adapters.md)        | [API](../api/os-adapters.md)        |
| [Security](security.md)                     | module-control-panel-security-flutter           | [Core](../core/security.md)           | [API](../api/security.md)           |
| [Web Hosting](web-hosting.md)               | module-control-panel-web-hosting-flutter        | [Core](../core/web-hosting.md)        | [API](../api/web-hosting.md)        |
