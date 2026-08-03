# Flutter technology reference

Flutter and Dart provide a cross-platform client for iOS, Android, web, and desktop. Liberu Flutter applications consume versioned APIs and core-module contracts through a mobile-appropriate client boundary; they do not duplicate Laravel domain rules.

## Example

```dart
class EmptyState extends StatelessWidget {
  const EmptyState({required this.onRetry, super.key});

  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: 'No records are available',
      child: Column(
        children: [
          const Text('No records are available.'),
          ElevatedButton(onPressed: onRetry, child: const Text('Try again')),
        ],
      ),
    );
  }
}
```

Use flutter_lints, stable platform plugins, typed response models, secure credential storage, explicit loading/error/empty/offline states, localization, adaptive layouts, and platform-aware permissions. Test domain-independent client logic, widgets, integration flows, accessibility, and release builds.

Official references: [Flutter documentation](https://docs.flutter.dev/), [Flutter learning pathway](https://docs.flutter.dev/get-started/learn-flutter), [Flutter cookbook](https://docs.flutter.dev/cookbook), [Flutter accessibility](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility), [Flutter testing](https://docs.flutter.dev/testing/overview), and [Flutter GitHub](https://github.com/flutter/flutter). Related local guides: [Flutter standard](../standards/FLUTTER.md), [mobile standard](../standards/MOBILE.md), and [Flutter module index](../modules/flutter/README.md).
