# Flutter and Dart standard

## Boundary

Flutter packages are optional presentation clients. They consume matching API contracts and do not move Laravel domain behavior, authorization, tenancy, persistence, or audit rules into Dart.

## Implementation requirements

- Use sound null safety, flutter_lints, typed DTOs, explicit state models, and pubspec.lock for application reproducibility.
- Separate API clients, repositories, application state, and widgets; keep widgets focused on rendering and interaction.
- Store credentials using platform-secure storage and validate all remote responses, deep links, files, and plugin results.
- Make retries, offline mutations, conflicts, background work, and app lifecycle transitions observable and recoverable.
- Use Material/Cupertino semantics deliberately, support screen readers, text scaling, contrast, RTL, localization, and reduced motion.
- Test Dart logic, widgets, API mapping, authorization outcomes, offline behavior, platform permissions, integration flows, and release builds.

```dart
Future<Record> loadRecord(String id) async {
  final response = await client.get('/api/v1/records/' + id);
  if (response.statusCode != 200) {
    throw const ApiException('Unable to load record');
  }
  return Record.fromJson(response.json);
}
```

Review [MOBILE.md](MOBILE.md), [security architecture](../architecture/SECURITY.md), [API architecture](../architecture/API.md), [Flutter technology reference](../technologies/FLUTTER.md), and [Flutter documentation](https://docs.flutter.dev/).
