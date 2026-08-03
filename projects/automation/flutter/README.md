# Automation Flutter + Dart implementations

**Scope:** [Automation](../AUTOMATION.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Automation project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 11 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                | Package                                   | Core                               | API                              |
| ------------------------------------- | ----------------------------------------- | ---------------------------------- | -------------------------------- |
| [Ai Gateway](ai-gateway.md)           | module-automation-ai-gateway-flutter      | [Core](../core/ai-gateway.md)      | [API](../api/ai-gateway.md)      |
| [Approvals](approvals.md)             | module-automation-approvals-flutter       | [Core](../core/approvals.md)       | [API](../api/approvals.md)       |
| [Automation Core](automation-core.md) | module-automation-automation-core-flutter | [Core](../core/automation-core.md) | [API](../api/automation-core.md) |
| [Connectors](connectors.md)           | module-automation-connectors-flutter      | [Core](../core/connectors.md)      | [API](../api/connectors.md)      |
| [Data Processing](data-processing.md) | module-automation-data-processing-flutter | [Core](../core/data-processing.md) | [API](../api/data-processing.md) |
| [Evaluation](evaluation.md)           | module-automation-evaluation-flutter      | [Core](../core/evaluation.md)      | [API](../api/evaluation.md)      |
| [Image](image.md)                     | module-automation-image-flutter           | [Core](../core/image.md)           | [API](../api/image.md)           |
| [Prompt Registry](prompt-registry.md) | module-automation-prompt-registry-flutter | [Core](../core/prompt-registry.md) | [API](../api/prompt-registry.md) |
| [Rules](rules.md)                     | module-automation-rules-flutter           | [Core](../core/rules.md)           | [API](../api/rules.md)           |
| [Video](video.md)                     | module-automation-video-flutter           | [Core](../core/video.md)           | [API](../api/video.md)           |
| [Voice](voice.md)                     | module-automation-voice-flutter           | [Core](../core/voice.md)           | [API](../api/voice.md)           |
