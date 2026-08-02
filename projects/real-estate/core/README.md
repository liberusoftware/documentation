# Real Estate Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Real Estate domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                            | Core package                             | Domain specification                            |
| ------------------------------------------------- | ---------------------------------------- | ----------------------------------------------- |
| [Instructions](instructions.md)                   | module-real-estate-instructions          | [Feature](../features/instructions.md)          |
| [Lettings](lettings.md)                           | module-real-estate-lettings              | [Feature](../features/lettings.md)              |
| [Listings](listings.md)                           | module-real-estate-listings              | [Feature](../features/listings.md)              |
| [Marketing](marketing.md)                         | module-real-estate-marketing             | [Feature](../features/marketing.md)             |
| [Matching](matching.md)                           | module-real-estate-matching              | [Feature](../features/matching.md)              |
| [Media And Documents](media-and-documents.md)     | module-real-estate-media-and-documents   | [Feature](../features/media-and-documents.md)   |
| [Offers](offers.md)                               | module-real-estate-offers                | [Feature](../features/offers.md)                |
| [Parties](parties.md)                             | module-real-estate-parties               | [Feature](../features/parties.md)               |
| [Portals And Reporting](portals-and-reporting.md) | module-real-estate-portals-and-reporting | [Feature](../features/portals-and-reporting.md) |
| [Properties](properties.md)                       | module-real-estate-properties            | [Feature](../features/properties.md)            |
| [Property Management](property-management.md)     | module-real-estate-property-management   | [Feature](../features/property-management.md)   |
| [Real Estate Core](real-estate-core.md)           | module-real-estate-real-estate-core      | [Feature](../features/real-estate-core.md)      |
| [Sales Progression](sales-progression.md)         | module-real-estate-sales-progression     | [Feature](../features/sales-progression.md)     |
| [Valuations](valuations.md)                       | module-real-estate-valuations            | [Feature](../features/valuations.md)            |
| [Viewings](viewings.md)                           | module-real-estate-viewings              | [Feature](../features/viewings.md)              |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
