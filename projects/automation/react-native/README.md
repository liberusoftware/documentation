# Automation React Native + Expo implementations

**Scope:** [Automation](../AUTOMATION.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the Automation project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-react-native`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [React Native + Expo module standard](../../../modules/react-native/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 11 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                | Package                                        | Core                               | API                              |
| ------------------------------------- | ---------------------------------------------- | ---------------------------------- | -------------------------------- |
| [Ai Gateway](ai-gateway.md)           | module-automation-ai-gateway-react-native      | [Core](../core/ai-gateway.md)      | [API](../api/ai-gateway.md)      |
| [Approvals](approvals.md)             | module-automation-approvals-react-native       | [Core](../core/approvals.md)       | [API](../api/approvals.md)       |
| [Automation Core](automation-core.md) | module-automation-automation-core-react-native | [Core](../core/automation-core.md) | [API](../api/automation-core.md) |
| [Connectors](connectors.md)           | module-automation-connectors-react-native      | [Core](../core/connectors.md)      | [API](../api/connectors.md)      |
| [Data Processing](data-processing.md) | module-automation-data-processing-react-native | [Core](../core/data-processing.md) | [API](../api/data-processing.md) |
| [Evaluation](evaluation.md)           | module-automation-evaluation-react-native      | [Core](../core/evaluation.md)      | [API](../api/evaluation.md)      |
| [Image](image.md)                     | module-automation-image-react-native           | [Core](../core/image.md)           | [API](../api/image.md)           |
| [Prompt Registry](prompt-registry.md) | module-automation-prompt-registry-react-native | [Core](../core/prompt-registry.md) | [API](../api/prompt-registry.md) |
| [Rules](rules.md)                     | module-automation-rules-react-native           | [Core](../core/rules.md)           | [API](../api/rules.md)           |
| [Video](video.md)                     | module-automation-video-react-native           | [Core](../core/video.md)           | [API](../api/video.md)           |
| [Voice](voice.md)                     | module-automation-voice-react-native           | [Core](../core/voice.md)           | [API](../api/voice.md)           |
