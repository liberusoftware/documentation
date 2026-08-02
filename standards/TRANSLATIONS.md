# Liberu translation standard

Liberu localization is a shared foundation capability. The boilerplate localization module owns locale availability, locale negotiation, fallback policy, translation loading, pluralization, formatting context, and user preferences. Product modules own their message keys and domain wording; themes and presentation adapters render translated values without creating competing catalogs.

## Ownership

- **Boilerplate localization module:** supported locales, fallback chain, locale context, translation loading/caching, pluralization rules, direction (`ltr`/`rtl`), and locale-aware date/number/currency services.
- **Domain modules:** namespaced message keys, validation/error messages, notification copy, enum labels, and domain terminology required by their capability.
- **Applications:** default locale, enabled locale set, tenant/team/site/brand overrides, user preference policy, and operational configuration.
- **Themes and presentation adapters:** translated layouts/components, locale switchers, RTL-safe composition, localized assets, and accessible language changes.

## Rules

- Use namespaced stable keys such as `modules.billing.invoices.status.paid`; never use mutable English copy as a public key.
- Keep user-visible strings out of domain classes and controllers; pass translation keys and interpolation data to the presentation boundary.
- Use ICU/Laravel-compatible pluralization and interpolation with named variables. Never concatenate translated fragments to form sentences.
- Format dates, times, numbers, currencies, addresses, names, and timezones through the shared locale context.
- Resolve locale from trusted application/team/site/user configuration and validate it against the enabled locale set. Fall back deterministically when a locale or key is missing.
- Do not expose untranslated developer errors, secrets, identifiers, or personal data through fallback messages.
- Support bidirectional layouts with logical CSS properties, translated assets where text is embedded, and language-appropriate fonts.
- A locale change must preserve authorization, tenant context, form state, and audit semantics.

## Catalog and release quality

Translation catalogs are versioned with their owning module/theme. CI checks key uniqueness, placeholder parity, missing keys, invalid plural forms, encoding, stale keys, and locale coverage. Pseudo-localization and representative RTL browser tests verify expansion, truncation, focus order, dates, numbers, validation errors, notifications, and screen-reader announcements.

Adding or changing a public key is a documented contract change. Removing a key requires a migration period or a fallback mapping. Machine translation may assist drafting but requires human review for legal, financial, security, accessibility, and brand-sensitive content.

## References

- [Boilerplate foundation](../projects/boilerplate/BOILERPLATE.md)
- [Laravel localization](https://laravel.com/docs/13.x/localization)
- [Unicode CLDR](https://cldr.unicode.org/)
- [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/)
- [Themes](THEMES.md)
- [Vue](VUE.md) · [React](REACT.md) · [Nuxt](NUXT.md) · [Inertia](INERTIA.md)
