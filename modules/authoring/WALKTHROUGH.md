# Walkthrough: a domain package, from nothing to a tagged release

**Reader:** a developer creating a new `liberu-module` package.

The worked example is `payment-core`, a capability package owning payment orchestration. Substitute your own name throughout. Rules referenced here live in [MODULES.md](../../architecture/MODULES.md); this document is the order to apply them in.

Every step ends in something you can run. If a step's command does not pass, do not proceed — each later step assumes the earlier one holds.

---

## Step 0 — Decide the boundary before the repository

Answer these four before creating anything. Getting them wrong is a rename across every consumer later.

| Question | Where the answer is constrained |
| --- | --- |
| What single capability does this own? | [§28](../../architecture/MODULES.md#28-package-implementation-process) |
| Which category — foundation, contract, capability, adapter, product, presentation? | [§5](../../architecture/MODULES.md#5-package-categories) |
| What is its Composer name and namespace? | [§9](../../architecture/MODULES.md#9-naming-conventions) |
| Which packages does it depend on, and does that introduce a cycle? | [§4](../../architecture/MODULES.md#4-mandatory-architecture-rules) |

Two decisions are worth making explicitly rather than by default:

**Presentation is a separate package.** A domain package never contains a `src/Filament` directory. If the capability needs an admin surface, that is a second repository — see [PRESENTATION.md](PRESENTATION.md).

**A provider-specific implementation is a separate package too**, and it depends on a contract package rather than on the domain package. `payment-stripe` requires `payment-contracts`, never `payment-core`.

---

## Step 1 — Create the repository and the skeleton

Create only the directories the package uses. The full permitted layout is [§7](../../architecture/MODULES.md#7-standard-package-layout); a first domain package usually needs four directories and six files.

```bash
gh repo create liberusoftware/module-payment-core --public --clone
cd module-payment-core
mkdir -p src config database/migrations tests/{Unit,Feature} .github/workflows
```

Note the repository name carries the `module-` prefix and the Composer name does not. `liberusoftware/module-payment-core` on GitHub is `liberusoftware/payment-core` on Packagist.

### `.gitignore`

A package repository ships **no lock file**: `install.yml` resolves it from nothing, the way a consumer first installs it, and a committed lock would hide a broken constraint.

```gitignore
/vendor/
/composer.lock
/.phpunit.cache/
/.phpunit.result.cache
```

### `tests/.gitkeep`

```bash
printf '%s\n' \
  '# Git does not track an empty directory, so without this file a package with no' \
  '# tests of its own publishes without tests/ at all — and Pest aborts before any' \
  '# suite runs with "The test directory [tests] does not exist."' \
  > tests/.gitkeep
```

**This file is load-bearing.** A package whose own tests are all in the shared boundary suite has an empty `tests/` directory, Git does not track empty directories, and the published tarball therefore has no `tests/` at all. Pest then aborts before running anything. In the reference fleet this shipped in **34 packages at once**, and passed the pre-release sweep, because the directory still existed on the machine that ran it. Only a fresh install exposed it.

---

## Step 2 — `composer.json`

```json
{
  "name": "liberusoftware/payment-core",
  "description": "Provider-neutral payment orchestration.",
  "type": "liberu-module",
  "license": "MIT",
  "version": "1.0.0",
  "require": {
    "php": "^8.5",
    "illuminate/database": "^13.0",
    "illuminate/support": "^13.0",
    "liberusoftware/module-manager": "^1.0",
    "liberusoftware/payment-contracts": "^1.0"
  },
  "require-dev": {
    "liberusoftware/package-testbench": "^1.7",
    "pestphp/pest": "^5.0"
  },
  "autoload": {
    "psr-4": { "Liberu\\Payment\\Core\\": "src/" }
  },
  "autoload-dev": {
    "psr-4": { "Liberu\\Payment\\Core\\Tests\\": "tests/" }
  },
  "extra": {
    "liberu": { "name": "payment-core" }
  },
  "config": {
    "allow-plugins": { "pestphp/pest-plugin": true }
  },
  "scripts": { "test": "pest" }
}
```

Three things about this file are not obvious:

**There is no `extra.laravel.providers`, and there must not be.** Laravel's package discovery has to find nothing, so that installing a module never boots it. An architecture rule in the host asserts this stays true across the whole fleet.

**`version` is present, and that is deliberate** even though Composer's own guidance is to omit it for packages published from a VCS tag. The module resolver compares each manifest's version against `Composer\InstalledVersions` and fails the boot on a mismatch, and the boundary suite asserts `composer.json` and `module.json` agree. Because of this, CI runs `composer validate` **without** `--strict`: `--strict` promotes the "version should be omitted" warning to an error and fails every package in the fleet for carrying a field they are required to carry.

**Do not add `orchestra/testbench`.** It arrives through `package-testbench`, which owns the Testbench application so that a change to it is one release rather than a fleet-wide sweep.

---

## Step 3 — `module.json`

```json
{
  "$schema": "https://schemas.liberu.dev/module/v1.json",
  "name": "payment-core",
  "display_name": "Payments",
  "description": "Provider-neutral payment orchestration.",
  "version": "1.0.0",
  "category": "capability",
  "provider": "Liberu\\Payment\\Core\\PaymentServiceProvider",
  "requires": {
    "php": "^8.5",
    "laravel": "^13.0",
    "packages": { "liberusoftware/payment-contracts": "^1.0" }
  },
  "suggests": { "liberusoftware/payment-stripe": "^1.0" },
  "capabilities": ["payments.orchestrate"],
  "default_enabled": false,
  "features": ["Provider-neutral payment orchestration"]
}
```

`version` must equal `composer.json`'s. `requires.packages` must not contradict `require`.

**`default_enabled` is the enablement decision**, and it is made here rather than in the host's configuration. A host's `config/modules.php` names no modules at all — it holds only an enable list and a disable list, both empty by default, for deployments that need to override. Set `default_enabled: false` when the module cannot function without credentials or configuration the composition must supply; `true` otherwise.

---

## Step 4 — The service provider

```php
<?php

namespace Liberu\Payment\Core;

use Illuminate\Support\ServiceProvider;

final class PaymentServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->mergeConfigFrom(__DIR__.'/../config/payment.php', 'payment');
    }

    public function boot(): void
    {
        $this->loadMigrationsFrom(__DIR__.'/../database/migrations');
        $this->publishes([__DIR__.'/../config/payment.php' => config_path('payment.php')], 'payment-config');
    }
}
```

The manifest names this class; nothing else registers it.

### Never name another package's concrete types

A domain package that hard-codes the set of things it operates on binds itself to whatever supplied them. Expose a **registry** and let each owner register into it — [§14](../../architecture/MODULES.md#14-registries-strategies-and-factories).

The failure mode is specific and worth recognising, because it survives the obvious refactor. In the reference fleet the `search` package's `searchAll()` named three types in a `match`; two of them belonged to a demo package. Deleting the demo's *methods* without introducing a registry would have left the coupling behind in the shape of a match arm — still naming types that no longer existed. The registry is what let those types leave:

```php
final class SearcherRegistry
{
    /** @var array<string, callable(array<string, mixed>): LengthAwarePaginator<int, mixed>> */
    private array $searchers = [];

    public function register(string $type, callable $searcher): void
    {
        if (isset($this->searchers[$type])) {
            throw new InvalidArgumentException("Search type [{$type}] already exists.");
        }

        $this->searchers[$type] = $searcher;
    }

    /** @return list<string> */
    public function types(): array
    {
        return array_keys($this->searchers);
    }
}
```

Bind it as a singleton in `register()`, and register your own entries in `boot()`. An unregistered type should be **absent** from a result rather than present and empty, so that a caller can distinguish "this composition has no such type" from "no matches".

---

## Step 5 — `phpunit.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="vendor/phpunit/phpunit/phpunit.xsd"
         bootstrap="vendor/autoload.php"
         colors="true"
>
    <testsuites>
        <testsuite name="Package">
            <directory>tests</directory>
        </testsuite>
        <!-- Shipped by the testbench, not by this repository: a new boundary rule is a
             testbench release every package picks up, rather than a fleet-wide sweep.
             Opting out of a rule means editing this file. -->
        <testsuite name="Boundary">
            <directory suffix="Test.php">vendor/liberusoftware/package-testbench/tests/Boundary/Module</directory>
        </testsuite>
    </testsuites>
    <source>
        <include><directory>src</directory></include>
    </source>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="DB_CONNECTION" value="sqlite"/>
        <env name="DB_DATABASE" value=":memory:"/>
    </php>
</phpunit>
```

Theme packages point at `tests/Boundary/Theme`; contract packages at `tests/Boundary/Contract`.

**Do not copy the boundary tests into the repository.** A package holding its own copy pins the rules of the day it was written, and adding a rule becomes a sweep across every repository instead of one release. This is the same reason `src/` is the only thing in `<source>`: a package measures itself.

---

## Step 6 — Tests

Most packages need no test bootstrap at all. Two lines bind Pest to the shared case:

```php
<?php

use Liberu\PackageTestbench\PackageTestCase;

pest()->extend(PackageTestCase::class)->in('Feature', 'Unit');
```

`PackageTestCase` boots Testbench, registers the provider your manifest names, and registers the providers of your dependencies. Read [TEST-BOOTSTRAP.md](TEST-BOOTSTRAP.md) **before** writing a `tests/TestCase.php` — the six situations that need one are enumerated there, and every other override is a symptom.

Two rules decide where a test belongs:

- **A test that needs nothing from a host belongs in the package.** If it uses the host's `App\Models\User`, reads the host's directories, or asserts across several packages, it is a composition test and stays in the host.
- **A rule the owning package could check about itself belongs in the testbench**, not in a host architecture suite. A host rule for a package-local property can only ever fail in the host, which is not where the fault is.

---

## Step 7 — CI

Three workflow files, not one file with three jobs. Each is a thin caller of a reusable workflow in `liberusoftware/.github`.

`.github/workflows/tests.yml`:

```yaml
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

# A publish sweep pushes every package within seconds of the others. Superseding
# this repository's previous run keeps a re-publish from stacking on a sweep that
# has not finished.
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  tests:
    uses: liberusoftware/.github/.github/workflows/package-tests.yml@main
```

`install.yml` and `compatibility.yml` are the same shape, calling `package-install.yml` and `package-compatibility.yml`, and both trigger on tags rather than pushes:

```yaml
on:
  push:
    tags: ['[0-9]+.[0-9]+.[0-9]+']
  workflow_dispatch:
```

Resolving from nothing and resolving `--prefer-lowest` are **release** questions: they change when the declared constraints change, not when a line of code does. Running them on every push is four jobs where one is warranted. See [RELEASING.md](RELEASING.md#4-why-the-triggers-differ) for the arithmetic.

---

## Step 8 — Run it

```bash
composer update --no-interaction --prefer-dist
vendor/bin/pest
```

This must pass with **no host application anywhere**. That is the whole point of the package boundary, and it is the step that finds the defects a host was hiding.

Two examples from the reference fleet, both invisible until the package ran on its own tree:

- A controller selected `profile_photo_path`, which is Jetstream's column. Nothing in the package's dependency graph created it, so the endpoint returned a 500 in any application without Jetstream. It had shipped that way for four releases; the only thing exercising it was a host that happened to have Jetstream.
- A provider threw while *registering* because a directory it expected was absent, so the package could not boot in any application that did not have that directory — including its own test application. A hand-written test bootstrap had been papering over it.

---

## Step 9 — README, changelog, release

[§29](../../architecture/MODULES.md#29-documentation-requirements) states what the README must contain. Then:

```bash
git add -A && git commit -m "Initial release"
git push origin main
git tag -a 1.0.0 -m 1.0.0 && git push origin 1.0.0
```

Registering the package on Packagist is a one-time manual submission at <https://packagist.org/packages/submit>. Subsequent tags update through the repository webhook.

See [RELEASING.md](RELEASING.md) for what a version bump obliges you to do in consuming applications.

---

## Step 10 — Compose it

Add it to a host with `composer require`, then verify the three separate things installation is *not*:

```bash
composer require liberusoftware/payment-core
php artisan module:list      # installed, and enabled per its manifest
php artisan test             # the host's own suite still passes
git status --porcelain       # no unexpected Composer-generated diff
```

The last check is [§6.2](../../architecture/MODULES.md#62-tracked-modules-policy): a clean locked install must reproduce the tracked source byte-for-byte. A non-empty diff means the published package and the tracked tree disagree, and the published side is authoritative.
