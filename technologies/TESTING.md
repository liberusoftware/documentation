# Testing technology reference

Liberu uses layered tests: fast domain tests, Laravel feature/integration tests, adapter contract tests, browser/accessibility checks, architecture tests, and deployment verification.

## Example

```php
it('does not allow a record from another organization', function (): void {
    $record = Record::factory()->for($otherOrganization)->create();

    actingAs($userFromOrganization)
        ->getJson("/api/v1/records/{$record->id}")
        ->assertForbidden();
});
```

Test authorization, tenant isolation, validation, idempotency, concurrency, migrations, queued work, failure recovery, and user-visible loading/empty/error states. Keep tests close to the owning module and run the full compatibility matrix in CI.

Official references: [Laravel testing](https://laravel.com/docs/13.x/testing), [Pest installation](https://pestphp.com/docs/installation), [Pest expectations](https://pestphp.com/docs/expectations), [Playwright](https://playwright.dev/docs/intro), and [axe-core](https://github.com/dequelabs/axe-core). Related local guides: [testing standard](../standards/TESTING.md), [CI](../standards/CI.md), and [Pest](https://pestphp.com/).
