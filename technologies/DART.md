# Dart technology reference

Dart is the language used by Flutter mobile clients. Use sound null safety, immutable value types where practical, explicit async error handling, and package constraints from pubspec.lock.

## Example

```dart
sealed class LoadState<T> {
  const LoadState();
}

final class Loading<T> extends LoadState<T> {
  const Loading();
}

final class Ready<T> extends LoadState<T> {
  const Ready(this.value);
  final T value;
}
```

Official references: [Dart overview](https://dart.dev/overview), [language tour](https://dart.dev/language), [Dart libraries](https://dart.dev/libraries), [Dart API](https://api.dart.dev/), and [Dart GitHub](https://github.com/dart-lang/sdk). Related local guides: [Flutter](FLUTTER.md), [Flutter standard](../standards/FLUTTER.md), and [mobile architecture](../architecture/MOBILE.md).
