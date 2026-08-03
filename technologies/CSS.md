# CSS technology reference

CSS controls layout, responsive behavior, themes, motion, and visual state. Liberu centralizes design decisions in the technology-neutral [theme standard](../standards/THEMES.md), with framework-specific adapters where necessary.

## Practical baseline

- Prefer logical properties, fluid layouts, design tokens, and component-scoped styles.
- Support keyboard focus, high contrast, reduced motion, dark mode where the theme requires it, and right-to-left direction.
- Avoid selectors that leak across modules and avoid using color as the only state signal.
- Keep content readable at zoom and test narrow, wide, touch, and keyboard layouts.

```css
:root {
  --color-focus: #1d4ed8;
}

:focus-visible {
  outline: 3px solid var(--color-focus);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto;
    transition-duration: 0.01ms;
  }
}
```

Official references: [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [CSS specifications](https://www.w3.org/Style/CSS/), [web.dev responsive design](https://web.dev/learn/design/), and [web.dev accessibility](https://web.dev/learn/accessibility/). Related local guides: [themes](../standards/THEMES.md), [HTML](HTML.md), and [accessibility](ACCESSIBILITY.md).
