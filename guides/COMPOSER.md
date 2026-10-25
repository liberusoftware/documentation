# PHP modules with Composer

This guide covers installing, changing, updating, and releasing PHP packages. Start with the [source inventory](../architecture/SOURCE-INVENTORY.md) for exact manifest names. A documentation name such as `module-example-core` is a design identifier unless the source manifest confirms it. Commands below use placeholder packages; replace them with a verified identity and compatible version.

## Understand the checkout

The application root owns its `composer.json`, repositories, plugin permissions, and `composer.lock`. A module's own `composer.json` describes that library's dependencies and autoloading. Running Composer in one directory does not install dependencies for every other independent package.

Before installation, inspect the application's README, PHP constraints, required extensions, Composer scripts, and plugin configuration. Use the PHP version required by the actual checkout. For example, many scanned modules require PHP `^8.5`; a generic Laravel installation guide does not override that constraint.

From the application root:

```bash
composer validate
composer install
composer check-platform-reqs
composer show --direct
```

`install` restores the locked versions when a lockfile exists. Commit application lockfiles. Use `update` deliberately when changing resolved versions, review the lockfile diff, and run the consuming application's checks. See the [Composer command reference](https://getcomposer.org/doc/03-cli.md).

## Liberu installer and runtime enablement

The application root selects and trusts `liberusoftware/composer-installer` through its `allow-plugins` configuration. PHP modules declare their package type and installer name. They can be installed under tracked `modules/` paths rather than `vendor/`; the independent package repository and the application lockfile still govern their source and resolved version. See the [tracked-module policy](../architecture/MODULES.md#62-tracked-modules-policy).

Installing a package, discovering its manifest, enabling its provider, running migrations, and granting user permission are separate operations. Do not infer that `composer require` makes every feature available. The scanned Boilerplate module manager takes application selection from `config/modules.php`, with `MODULES_ENABLED` and `MODULES_DISABLED` inputs. Check the actual deployment configuration and dependencies before enabling a provider. Do not copy a package's `default_enabled` value into deployment policy blindly.

After a compatible application's dependencies and environment are configured, the observed module-manager implementation declares these inspection commands:

```bash
php artisan module:list
php artisan module:status audit
php artisan module:features audit
php artisan module:validate
```

`module:status` reports installation, resolved enablement, version, provider, dependencies, capabilities, features, and source path. `module:features` takes an optional search query. These names are verified against [the module-manager command sources](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/module-manager/src/ModuleManagerServiceProvider.php); availability in a different package version must be checked with `php artisan list`. There is no basis here to invent `module:enable` or `module:install` commands.

The same implementation provides `module:clear` and `module:cache`. Apply them through the application's deployment/cache procedure after changing module configuration; rebuilding module cache alone does not refresh Laravel configuration cache, migrate the database, or restart long-lived workers. Follow the host's documented migration and worker rollout sequence. The [configuration source](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/module-manager/config/modules.php) and [status command](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/module-manager/src/Console/ModuleStatusCommand.php) are pinned to the inventory commit; these commands were inspected, not executed against an installed host in this documentation review.

For installed tracked trees, use the release process's clean locked-install check to detect differences. Do not resolve a conflict by deleting the module tree or hand-editing generated autoload metadata. For local path development, keep the override clearly separated from production dependency configuration and verify the released artifact without that override before promotion.

## Develop a module inside a clone

Inspect root repositories first. If modules already resolve through `modules/*`, retain that configuration. If developing a separate local checkout, add a narrowly scoped path repository in the consuming application's root manifest, preserving existing entries:

```json
{
  "repositories": [
    {
      "type": "path",
      "url": "../module-example",
      "options": { "symlink": true }
    }
  ]
}
```

The path is relative to the application root. The module's manifest `name` must match the required package. Its inferred or declared version must satisfy the consumer's constraint. For a development branch, use an explicit development constraint or a documented branch alias; do not relabel development code as an actual stable release. Root repository priority can shadow registry packages: inspect the resolved source before accepting an update. See [Composer path repositories](https://getcomposer.org/doc/05-repositories.md#path).

After configuration, use the real package name:

```bash
composer update vendor/example --with-all-dependencies --dry-run
composer update vendor/example --with-all-dependencies
composer show vendor/example
```

Review all changed dependencies because `--with-all-dependencies` can update more than the named package. A symlink makes source edits visible immediately; a mirrored path install requires reinstallation to copy changed files. Rebuild autoload metadata after changing namespace mappings. Run module checks from the module's declared test environment and integration checks in the application. Do not edit `vendor/` as the permanent source of a change.

## Keep application and module changes together

1. Check `git status` in each checkout and preserve uncommitted work before switching branches or pulling.
2. Fetch the application's remote, review incoming changes, and integrate according to its contribution policy. For an independent module checkout, repeat there. Application Git updates do not update an independently cloned module automatically.
3. Identify whether a tracked module is application-owned development source or an installed copy of an independently released package. Unextracted application code is committed with its application. For installed independent packages, make the durable fix in the canonical module repository, release it, and update the consumer; committing a local installed-tree edit alone creates drift. If submodules are used, publish the child commit before updating the parent pointer. Inspect manifests, lockfiles, installer configuration, and `.gitmodules` rather than guessing.
4. Run `composer install` after a pull that changes the lockfile. To evaluate newer package versions, run `composer outdated --direct`, select a package, dry-run a targeted update, then review constraints and migration notes.
5. Run declared format, static-analysis, unit, and application integration checks. Exercise migrations on a disposable database and verify a recovery path before production rollout.
6. Commit manifest and application lockfile changes together with the integration change. A shared module fix also needs tests against other consuming products before release.

When resolution fails, use `composer why vendor/example` and `composer prohibits vendor/example 2.0.0`, replacing the example package and version with the actual target. Check PHP/extensions, constraints, repository priority, and authentication before deleting caches or broadening stability settings. Never use `--ignore-platform-reqs` to claim a supported deployment.

## Release to Packagist

Composer is the dependency client; Packagist indexes package repositories. Public release is separate from local development. Do these steps only as the authorized package maintainer:

1. Identify the canonical package repository. A nested module directory in an application repository needs an established subtree split or release pipeline that exposes its manifest at the package repository root. An application tag alone does not independently release every nested package.
2. Validate the package manifest, license, autoload mapping, dependency ranges, README, changelog, upgrade notes, and supported PHP/framework matrix. Follow the package's actual version contract. Many Liberu packages carry explicit versions in both `composer.json` and `module.json`; synchronize those with the release tag and verify the consuming resolver's installed-version checks. Do not remove explicit fields merely because another Composer library derives versions from VCS.
3. Run the package's declared checks and an installation test in a clean consumer. Inspect the distribution contents for credentials, local configuration, and unintended files.
4. Merge the reviewed change through the repository's release process. Create an immutable semantic version tag for the intended commit and push through that process. Breaking public contracts require the appropriate version and migration guide.
5. Submit the canonical repository URL to Packagist when first registering the package. Configure its documented GitHub integration so subsequent tags are indexed. See [Packagist publishing instructions](https://packagist.org/about).
6. Confirm the version is indexed and install it in a fresh consumer without local path overrides. Test it, then update application constraints and lockfiles deliberately.

Keep registry credentials outside Git. Private packages need a private registry or authenticated VCS configuration available to developers and CI. A release failure should stop promotion; fix and issue a new version rather than moving a tag already consumed by applications.

When a module changes, also follow the [documentation synchronization guide](DOCUMENTATION-MAINTENANCE.md) so consumers can find its current source identity, behavior and migration requirements.
