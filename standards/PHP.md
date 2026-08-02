# PHP 8.5 standard

Liberu applications and packages target PHP 8.5 and Composer 2, with exact patch versions controlled by the repository lock file and CI matrix. PHP language behavior is governed by the [official PHP manual](https://www.php.net/docs.php); package interoperability follows [PSR.md](PSR.md).

## Required practices

- Use `declare(strict_types=1);` in new executable PHP files.
- Use typed properties, parameters, and return values; represent constrained values with enums or value objects.
- Prefer immutable data transfer objects and `readonly` state where mutation is not required.
- Use exceptions for exceptional failures, never sentinel values that hide authorization or data loss.
- Avoid dynamic properties, variable variables, `eval`, unsafe deserialization, and broad catch blocks.
- Use `password_*`, `random_bytes`, and framework cryptography rather than custom security primitives.
- Keep secrets out of source, logs, URLs, serialized props, tests, and exception messages.
- Use Composer autoloading and dependency constraints; never scan directories to invent an autoloader.

## Quality

Format with PHP-CS-Fixer or Laravel Pint according to the repository configuration, analyze with the supported static-analysis level, and test public contracts at unit, integration, and feature boundaries. See [PSR.md](PSR.md), [GUIDELINES.md](GUIDELINES.md), and the [PHP-FIG PSR index](https://www.php-fig.org/psr/).
