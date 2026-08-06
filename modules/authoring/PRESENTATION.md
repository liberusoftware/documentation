# The presentation companion

**Reader:** a developer adding a Filament (or Livewire) surface to an existing domain capability.

Domain packages stay presentation-agnostic — [§20](../../architecture/MODULES.md#20-filament-livewire-api-and-themes). A capability's admin UI is a **second repository**, named for the surface it provides, and a boundary rule fails a domain package that imports Filament.

---

## 1. Naming and dependency direction

| | |
| --- | --- |
| Repository | `module-payment-core-filament` |
| Composer | `liberusoftware/payment-core-filament` |
| Namespace | `Liberu\Payment\Core\Filament\` |
| Category | `presentation` |
| Depends on | `payment-core`, `filament/filament` |
| Depended on by | nothing |

The dependency runs one way only. The domain package must not know its surface exists, and must not gain an optional dependency on it.

---

## 2. Declare the plugin in the manifest

The manifest's `presentation.filament` key maps a panel id to the plugin classes for it. This is what an application reads to compose its panels; nothing scans for plugins.

```json
{
  "name": "payment-core-filament",
  "category": "presentation",
  "provider": "Liberu\\Payment\\Core\\Filament\\PaymentFilamentServiceProvider",
  "requires": {
    "packages": { "liberusoftware/payment-core": "^1.0" }
  },
  "presentation": {
    "filament": {
      "admin": ["Liberu\\Payment\\Core\\Filament\\PaymentFilamentPlugin"]
    }
  },
  "default_enabled": true
}
```

A package may declare plugins for more than one panel. The host instantiates only the plugins of **enabled** modules, rejects duplicate plugin ids, and rejects anything that is not a Filament `Plugin`.

Two boundary rules cover this without a host: that a `-filament` package declares at least one plugin, and that every class it declares exists.

---

## 3. Tenancy: the rule that bites

**Any Filament resource whose model has no `team()` relationship must override `isScopedToTenant()`:**

```php
public static function isScopedToTenant(): bool
{
    return false;
}
```

Without it, a tenant-scoped panel returns a 500 on that resource. This is not something your package's own suite will catch unless its fixture panel is tenant-scoped, and it should not be — see §4. Document the requirement in the package README instead, and state which of your resources are tenant-scoped.

---

## 4. Testing a resource needs a panel

A Filament resource is only reachable through a panel. Your package ships a plugin; the host composes the panel. So the suite composes the smallest panel that registers your plugin:

```php
final class TestPanelProvider extends PanelProvider
{
    public function panel(Panel $panel): Panel
    {
        return $panel
            ->default()
            ->id('admin')
            ->path('admin')
            ->plugins([PaymentFilamentPlugin::make()]);
    }
}
```

The id matches the `presentation.filament` key in your manifest. Put it in `tests/Fixtures/`, which PHPUnit does not collect — a directory suite only picks up files ending `Test.php`.

**Do not copy the host's panel provider.** The reference host's is tenant-scoped to a `Team`, gated by Shield, and themed from site settings. Reproducing that makes the tests assert on the host's composition rather than on your resource, and it is exactly the scaffolding worth deleting: two adopted tests in the reference fleet spent most of their lines building a team, setting a tenant and creating a role inside its permission context, all to reach one line of a `CreatePost` page.

Set the panel current in `setUp()`, because no route has been visited to resolve one:

```php
protected function setUp(): void
{
    parent::setUp();

    Filament::setCurrentPanel('admin');
}
```

### Filament needs more providers than the testbench registers by default

`PackageTestCase` registers `extra.laravel.providers` of your **direct** dependencies, which for `filament/filament` is one provider. Support, schemas, forms, tables, actions, notifications, widgets, Livewire and the blade icon packages are all transitive, and a panel cannot function without them.

Widen the walk to everything installed — which is what Laravel's own discovery does in an application — rather than hand-listing a stack that changes with each Filament release:

```php
private function discoveredProviders(): array
{
    $installed = json_decode(
        (string) file_get_contents($this->packageRoot().'/vendor/composer/installed.json'),
        true,
        flags: JSON_THROW_ON_ERROR,
    );

    $providers = [];

    foreach ($installed['packages'] ?? [] as $package) {
        foreach ((array) ($package['extra']['laravel']['providers'] ?? []) as $provider) {
            $providers[] = $provider;
        }
    }

    return $providers;
}
```

Sibling Liberu modules are unaffected: their manifests declare that array empty precisely so installation never implies boot, so this picks up framework packages and nothing else.

> **Status.** This lives in the one package that needs it rather than in `package-testbench`. When a second presentation package needs the same walk, that is when it moves — a helper with one caller is a guess about the second.

---

## 5. Assert something that can fail

An empty table renders successfully whatever is wrong with its columns. Create a record and assert the cells:

```php
it('renders the post list', function () {
    $post = Post::factory()->create(['title' => 'First post']);

    livewire(ListPosts::class)
        ->assertOk()
        ->assertSee('First post')
        ->assertSee($post->author->name);
});
```

Two habits from host-era tests are worth dropping when the test moves into the package:

- **`Gate::before(fn () => true)` is usually unnecessary.** Filament permits an action when no policy is registered for the model, and a package suite normally registers none. If you need it, the thing under test is authorization, and it should say so.
- **A test that only calls `assertOk()` on an empty page cannot fail on the thing it is named for.** Give it a record.
