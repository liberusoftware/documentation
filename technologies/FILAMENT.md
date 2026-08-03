# Filament 5 technology reference

Filament 5 is the server-driven Laravel UI used for administration, operations, forms, tables, resources, and dashboards. A Filament package is an optional adapter over one core module.

## Adapter example

```php
final class RecordResource extends Resource
{
    protected static ?string $model = Record::class;

    public static function form(Form $form): Form
    {
        return $form->schema([
            TextInput::make('name')->required()->maxLength(160),
        ]);
    }
}
```

Resources must use core actions and policies, apply tenant/team scope, expose only permitted fields, confirm destructive actions, and provide accessible loading, empty, validation, and failure states. Do not move domain invariants into resource callbacks.

Official references: [Filament 5 getting started](https://filamentphp.com/docs/5.x/getting-started), [resources](https://filamentphp.com/docs/5.x/resources/overview), [forms](https://filamentphp.com/docs/5.x/forms), [tables](https://filamentphp.com/docs/5.x/tables), and [Filament GitHub](https://github.com/filamentphp/filament). Related local guides: [Filament standard](../standards/FILAMENT.md), [Filament module index](../modules/filament/README.md), and [themes](../standards/THEMES.md).
