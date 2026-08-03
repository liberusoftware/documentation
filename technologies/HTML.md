# HTML technology reference

HTML is the accessibility and structure contract for every Liberu web surface, whether rendered by Blade, Livewire, Filament, Inertia, or Nuxt.

## Practical baseline

- Use landmarks such as `header`, `nav`, `main`, and `footer`.
- Use native controls before custom widgets and associate every form control with a label.
- Preserve heading hierarchy, meaningful link text, document language, and valid names/roles/states.
- Render server-provided text escaped by default; sanitize explicitly approved rich text.
- Make status, validation, and asynchronous changes perceivable without relying on color alone.

```html
<label for="record-name">Record name</label>
<input id="record-name" name="name" autocomplete="off" required />
<p id="record-name-error" role="alert"></p>
```

Official references: [MDN HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [WHATWG HTML](https://html.spec.whatwg.org/), [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/), and [HTML validator](https://validator.w3.org/). Related local guides: [views](../standards/VIEWS.md), [Blade](../standards/BLADE.md), and [themes](../standards/THEMES.md).
