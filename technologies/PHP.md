# PHP technology reference

Liberu targets PHP 8.5 for the current Laravel application baseline. Implementation rules live in [standards/PHP.md](../standards/PHP.md); this page points to the language and package-management references.

- [PHP manual](https://www.php.net/docs.php) — language, standard library, security, extensions, and runtime behavior.
- [PHP supported versions](https://www.php.net/supported-versions.php) — release and security-support status.
- [PHP 8.5 migration guide](https://www.php.net/migration85) — language and runtime changes to verify during upgrades.
- [Composer](https://getcomposer.org/doc/) — dependency resolution, autoloading, scripts, and package publishing; see the local [Composer guide](COMPOSER.md).
- [PHP-FIG](https://www.php-fig.org/psr/) — interoperability standards.

## Liberu usage

Use strict types, typed properties and return values, constructor injection, immutable value objects where appropriate, and explicit exceptions at boundaries. A core module keeps domain rules independent of Laravel presentation packages:

```php
<?php

declare(strict_types=1);

final readonly class Money
{
    public function __construct(
        public int $minorUnits,
        public string $currency,
    ) {}
}
```

Representative examples are the [core module implementation guide](../modules/core/README.md), [DDD standard](../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [Liberu core modules](../projects/liberu/core/README.md). Use the application's lock file and CI matrix as the final authority for supported patch versions and extensions.
