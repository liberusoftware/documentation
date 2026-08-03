# React Native technology reference

React Native provides native iOS and Android applications from React and TypeScript. Liberu mobile clients use it as an optional API-consuming presentation layer; Laravel core modules and APIs remain the source of domain behavior, authorization, tenancy, and audit.

## Example

```tsx
import { Pressable, Text, View } from "react-native";

export function EmptyState({ onRetry }: { onRetry: () => void }) {
  return (
    <View accessibilityRole="summary">
      <Text>No records are available.</Text>
      <Pressable accessibilityRole="button" onPress={onRetry}>
        <Text>Try again</Text>
      </Pressable>
    </View>
  );
}
```

Use Expo when it meets the native capability and release requirements; use development builds for native libraries and production-like testing. Keep tokens in platform-secure storage, never log credentials, validate API responses, handle offline and retry states, support screen readers and dynamic text, and test both platform-specific behavior and shared flows.

Official references: [React Native getting started](https://reactnative.dev/docs/getting-started), [core components and APIs](https://reactnative.dev/docs/components-and-apis), [accessibility](https://reactnative.dev/docs/accessibility), [Expo tutorial](https://docs.expo.dev/tutorial/introduction/), [Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/), and [React Native GitHub](https://github.com/facebook/react-native). Related local guides: [React Native standard](../standards/REACT-NATIVE.md), [mobile standard](../standards/MOBILE.md), and [React Native module index](../modules/react-native/README.md).
