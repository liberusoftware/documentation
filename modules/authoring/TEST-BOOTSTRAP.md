# The shared test bootstrap

**Reader:** a developer writing a package's tests, or diagnosing why a package will not boot in its own suite.

`liberusoftware/package-testbench` is the one test bootstrap for module and theme packages. It owns the Orchestra Testbench application, the shared actor, and the boundary suites every repository runs against its own files. A package that writes its own bootstrap pins the conventions of the day it was written; a package that uses this one picks up a new rule as a release.

---

## 1. What you get without writing anything

`tests/Pest.php`, two lines:

```php
<?php

use Liberu\PackageTestbench\PackageTestCase;

pest()->extend(PackageTestCase::class)->in('Feature', 'Unit');
```

`PackageTestCase` does four things:

1. **Locates the package root** from the working directory, so nothing is hard-coded to a path.
2. **Sets an application key.** Testbench boots without one, so anything that renders a view — a Livewire component, a mailable — otherwise dies on `No application encryption key has been specified` rather than on anything the package did.
3. **Registers the provider your `module.json` names.** This is why `getPackageProviders()` overrides are not the norm.
4. **Registers the providers of your dependencies**, by the rules in §2.

Plus the boundary suite, which your `phpunit.xml` points at rather than copying. For a module it asserts seven things about the package's own files:

| Rule | Catches |
| --- | --- |
| internally consistent package metadata | `composer.json` and `module.json` disagreeing on name or version |
| ships every file a package repository requires | a missing `README.md`, `CHANGELOG.md`, workflow, or `tests/` directory |
| registers its declared service provider | a manifest naming a class that does not boot |
| does not depend on the host application | any reference to `App\` |
| keeps Filament out of a domain module | presentation leaking into a non-presentation package |
| does not import domain models into an `-api` adapter | an adapter reaching past its contract |
| declares panel plugins when it is a Filament module | a `-filament` package with no `presentation.filament` entry |

---

## 2. Which providers get booted, and which deliberately do not

Testbench runs **no package discovery**. A provider that reaches for a framework binding — Livewire's component finder, Filament's panel registry — cannot boot unless something registers the package supplying it. Two sources do, and neither is a new convention:

**`extra.laravel.providers` of any direct dependency**, whether in `require` or `require-dev`. This is Laravel's own discovery, scoped to what the package actually requires. Sibling Liberu modules contribute nothing here, because their manifests declare that array empty precisely so installation never implies boot.

**The manifest provider of a sibling declared in `require-dev`** — and deliberately **not** of one declared only in `require`.

That asymmetry is the rule most likely to surprise you, so it is worth stating as intent rather than mechanism:

> A `require-dev` entry on a sibling module is a statement about what this package is *tested against*. A `require` entry is a statement about what it *runs against*. Booting the latter would contradict the enablement rule the whole architecture rests on — installing a module never boots it.

### The sanctioned way to boot a `require` sibling

Some packages genuinely need one. A package that *extends* a dependency's registry is the clear case: a searcher registered against an unbound registry is registered on an instance nothing else will ever read, so the suite would pass while testing nothing.

Name the provider:

```php
protected function getPackageProviders($app): array
{
    return [SearchServiceProvider::class, ...parent::getPackageProviders($app)];
}
```

**Do not list the same package in both `require` and `require-dev` to get around this.** It works, and it was the first design in the reference fleet, but it earns a `composer validate` warning for a duplication that says nothing true — the package is not a development dependency, and the metadata should not claim it is.

---

## 3. The actor

No package owns the `users` table; the application does. In the reference fleet one package adds `locale`, `theme_preference` and `timezone` to it and another adds search indexes, but neither creates it.

The testbench supplies one for tests that need it:

```php
use Liberu\PackageTestbench\TestUser;
use Liberu\PackageTestbench\UsesTestUser;

abstract class TestCase extends PackageTestCase
{
    use UsesTestUser;
}
```

`UsesTestUser` loads the base `users` migration and brings `RefreshDatabase` with it — the migration is worthless without one.

**`TestUser` implements none of the fleet's actor contracts**, and that is a decision rather than an omission. Implementing the four one-method interfaces would make the testbench require Horizon, Pulse, Telescope, Jetstream, Socialite and Socialstream in **every** package's development tree, for four methods. A package needing a contract subclasses `TestUser` in its own `tests/Fixtures`:

```php
final class PrivilegedTestUser extends TestUser implements PrivilegedActor
{
    public function isSuperAdmin(): bool
    {
        return true;
    }
}
```

The same applies to model scopes a dependency expects. If a package resolves a model from configuration and then calls a scope on it, the scope is part of a contract the *composition* satisfies — stand up a subclass supplying it rather than widening `TestUser`.

---

## 4. When you do need a `tests/TestCase.php`

Six situations, and no others. Anything else is a symptom.

| Situation | What the case does |
| --- | --- |
| The package reads configuration a host would supply | sets it in `defineEnvironment()` |
| The package needs a user | `use UsesTestUser` |
| The package needs an actor contract or a model scope | points configuration at a fixture subclass |
| The package extends a `require` sibling's registry | names that provider in `getPackageProviders()` |
| The package needs migrations beyond its own | `loadMigrationsFrom()` in `defineDatabaseMigrations()` |
| The package is a Filament presentation package | registers a fixture panel — see [PRESENTATION.md](PRESENTATION.md) |

Bind it from `tests/Pest.php`:

```php
pest()->extend(Liberu\Payment\Core\Tests\TestCase::class)->in('Feature', 'Unit');
```

### Always call the parent

```php
protected function defineEnvironment($app): void
{
    parent::defineEnvironment($app);   // ← without this you lose the application key

    $app['config']->set('payment.default_currency', 'GBP');
}
```

Omitting `parent::` here produces `No application encryption key has been specified` from somewhere unrelated to the change that caused it.

---

## 5. Six failures, and what each one means

Every one of these occurred in the reference fleet. They are listed by the message you will actually see.

### `Target class [livewire.finder] does not exist`

The package's provider needs Livewire, and nothing registered it. Livewire is not a direct dependency, or it is and the package was relying on a host to supply it. Add it to `require` if the package genuinely needs it at runtime, `require-dev` if only the tests do.

### `Target [SomeInterface] is not instantiable`

An adapter package boots against a contract that nothing in its graph binds. This is the correct design at runtime — the adapter must stay free of any implementation — so the fix is a `require-dev` on a package that binds one. That keeps the adapter clean and lets its own suite boot a real implementation.

### `Composer package is not installed`

The manifest's version and `Composer\InstalledVersions` disagree. You bumped `module.json` and have not published and re-installed. This fails at boot, before any test body runs, which is why it never presents as a test failure.

### `The test directory [tests] does not exist`

The published tarball has no `tests/` directory. See `tests/.gitkeep` in [WALKTHROUGH.md](WALKTHROUGH.md#step-1--create-the-repository-and-the-skeleton). **This will not reproduce locally** — the directory exists on the machine that built it. Reproduce it by installing the published package into a clean directory.

### `No application encryption key has been specified`

A `defineEnvironment()` override that did not call `parent::`.

### `Cannot bind an instance to a static closure`

A `static fn` passed to Pest's `skip()`. Pest binds those closures to the test case, so they cannot be static. Worth naming because it is invisible until the condition is evaluated.

---

## 6. Where a test belongs

Two questions, in order.

**Does it need anything from a host?** If it uses the host's `App\Models\User`, reads the host's directories, or asserts across several packages at once, it is a composition test and belongs in the host's suite. Several suites that look package-shaped are not.

**Could the owning package check this about itself?** If so it is a boundary rule and belongs in `package-testbench`, not in a host architecture suite. A host rule for a package-local property can only ever fail in the host, which is not where the fault is — and the fix has to be made in a repository the failing run never touched.

What is left for a host architecture suite is the **whole-graph** properties: that every package installs standalone, that enablement derives from manifests, that theme parents resolve, that Composer owns every autoload boundary. No single package can run those, because no single package can see the graph.

Before adding a rule anywhere, check that it can be the thing that catches the fault rather than the second thing to notice it. A rule that cannot fire reads as coverage it does not provide.
