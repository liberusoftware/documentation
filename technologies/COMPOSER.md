# Composer technology reference

Composer is the PHP dependency manager for Liberu. Core modules publish independently installable Composer packages; applications select compatible versions and presentation adapters.

## Safe workflow

1. Declare runtime constraints and package dependencies in `composer.json`.
2. Run `composer update` only when intentionally changing the dependency graph.
3. Commit `composer.lock` for applications and install with `composer install` in CI/deployments.
4. Review scripts, plugins, abandoned packages, licenses, advisories, and transitive changes.
5. Use PSR-4 autoloading and package-local service providers; do not require an application `App\\` namespace from a reusable module.

```bash
composer validate --strict
composer install --prefer-dist --no-interaction
composer audit
composer show --direct
```

A minimal core package declaration is documented in the [module implementation guide](../modules/features/IMPLEMENTATION.md). See the official [Composer documentation](https://getcomposer.org/doc/), [basic usage](https://getcomposer.org/doc/01-basic-usage.md), [schema](https://getcomposer.org/doc/04-schema.md), and [Composer GitHub repository](https://github.com/composer/composer). Related local rules: [PHP](PHP.md), [PHP standard](../standards/PHP.md), and [repository architecture](../architecture/REPOSITORIES.md).
