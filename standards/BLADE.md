# Blade standard

Blade is Laravel's server-rendered view layer. Use it for document structure, accessible progressive enhancement, and theme-owned presentation.

- Keep components small, explicit, escaped by default, and independent of ambient database queries.
- Use layouts, slots, components, translation strings, locale-aware formatting, and semantic HTML.
- Use `@csrf`, safe URL generation, authorization directives only for presentation, and policy checks in the server action.
- Keep Livewire behavior in Livewire components and domain mutations in authorized application actions.
- Follow [THEMES.md](THEMES.md) for tokens, assets, inheritance, CSP, accessibility, and overrides.

See [Blade templates](https://laravel.com/docs/13.x/blade) and [Laravel views](https://laravel.com/docs/13.x/views).

## Delivery checklist

For each view, identify its owner, required data, authorization boundary, empty/loading/error states, localization needs, and accessibility path. Prefer reusable components and theme tokens over copied markup. Verify output escaping, CSRF, links, forms, keyboard/focus behavior, responsive behavior, and the no-JavaScript fallback where the workflow is business-critical.
