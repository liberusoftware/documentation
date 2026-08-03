# Livewire 4 technology reference

Livewire 4 provides server-driven interactive Laravel components. Liberu uses it for focused workflows where server-side state, authorization, and progressive enhancement are valuable.

## Component example

```php
<?php

use Livewire\\Component;

new class extends Component {
    public string $search = '';

    public function render()
    {
        return view('livewire.records.index', [
            'records' => Record::query()
                ->where('name', 'like', "%{$this->search}%")
                ->paginate(25),
        ]);
    }
};
```

Validate and authorize every action on the server, lock or validate component state, avoid exposing secrets, preserve tenant context, and make loading, empty, denied, and failure states accessible. Components coordinate a core action; they do not become the domain model.

Official references: [Livewire 4 installation](https://livewire.laravel.com/docs/4.x/installation), [components](https://livewire.laravel.com/docs/4.x/components), [security](https://livewire.laravel.com/docs/4.x/security), [testing](https://livewire.laravel.com/docs/4.x/testing), and [Livewire GitHub](https://github.com/livewire/livewire). Related local guides: [Livewire standard](../standards/LIVEWIRE.md) and [module index](../modules/livewire/README.md).
