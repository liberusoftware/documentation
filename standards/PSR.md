# PHP Standards Recommendations

## Liberu PSR policy

Liberu follows accepted PHP-FIG standards at interoperability boundaries and uses PSR-12 as the PHP coding baseline. Framework-specific Laravel conventions remain required where they add behavior, but they must not break a published PSR contract. The authoritative status list is the [PHP-FIG PSR index](https://www.php-fig.org/psr/).

“Follow” means that owned PHP code and public package boundaries satisfy the applicable standard. A PSR interface is not added merely for decoration: use it when the corresponding boundary is genuinely replaceable or interoperable. Draft, abandoned, and deprecated documents are not normative dependencies.

## Accepted standards we follow

| PSR | Standard | Liberu application |
|---|---|---|
| [PSR-1](https://www.php-fig.org/psr/psr-1/) | Basic Coding Standard | UTF-8 PHP-only files, declarations/imports, class naming, constants, and method naming |
| [PSR-3](https://www.php-fig.org/psr/psr-3/) | Logger Interface | Package and infrastructure services type against `Psr\\Log\\LoggerInterface` when they accept a logger; contextual structured logging remains required |
| [PSR-4](https://www.php-fig.org/psr/psr-4/) | Autoloading Standard | Composer namespace-to-path mapping for applications, modules, themes, tests, and generated clients |
| [PSR-6](https://www.php-fig.org/psr/psr-6/) | Caching Interface | Cache-pool integrations where a PSR-6 library boundary is used; cache keys remain scope-qualified and values must not leak secrets |
| [PSR-7](https://www.php-fig.org/psr/psr-7/) | HTTP Message Interface | HTTP middleware, adapters, and integrations that exchange PSR HTTP messages |
| [PSR-11](https://www.php-fig.org/psr/psr-11/) | Container Interface | Libraries consume a PSR container only when they need container interoperability; application services use Laravel's composition root |
| [PSR-12](https://www.php-fig.org/psr/psr-12/) | Extended Coding Style Guide | PHP formatting, file endings, imports, indentation, braces, declarations, visibility, and line whitespace; enforced by the repository formatter |
| [PSR-13](https://www.php-fig.org/psr/psr-13/) | Hypermedia Links | Hypermedia link objects when a package exposes link-rich HTTP representations; ordinary Laravel URLs need not invent links |
| [PSR-14](https://www.php-fig.org/psr/psr-14/) | Event Dispatcher | Event package boundaries use `Psr\\EventDispatcher\\EventDispatcherInterface` where decoupling is needed; Laravel events remain the application adapter |
| [PSR-15](https://www.php-fig.org/psr/psr-15/) | HTTP Handlers | Middleware/handler packages that expose PSR-15 pipelines; Laravel middleware remains the host integration |
| [PSR-16](https://www.php-fig.org/psr/psr-16/) | Simple Cache | Small cache consumers that need a key/value cache independent of a full PSR-6 pool |
| [PSR-17](https://www.php-fig.org/psr/psr-17/) | HTTP Factories | Portable creation of PSR-7 requests, responses, streams, and URIs in reusable HTTP integrations |
| [PSR-18](https://www.php-fig.org/psr/psr-18/) | HTTP Client | Reusable outbound HTTP clients accept `Psr\\Http\\Client\\ClientInterface` where transport substitution matters |
| [PSR-20](https://www.php-fig.org/psr/psr-20/) | Clock | Time-sensitive domain services accept `Psr\\Clock\\ClockInterface` rather than calling wall-clock time directly, especially for expiry, retries, invitations, settings, and security |

These standards complement, rather than replace, Laravel contracts. For example, an application may adapt Laravel's request/response, cache, event, container, and HTTP client services to PSR interfaces at a package boundary while keeping Laravel-specific composition in the host application.

## Coding rules

PSR-12 is mandatory for PHP source, tests, migrations, configuration classes, and package examples:

- use Unix LF endings, UTF-8 without a BOM, and one final newline;
- omit the closing PHP tag in PHP-only files;
- use four spaces, never tabs, and no trailing whitespace;
- keep the soft line limit at 120 characters and split long code where clarity improves;
- use `declare(strict_types=1);` in new executable PHP files unless a documented framework/bootstrap constraint prevents it;
- order file headers, `declare`, namespace, and imports consistently;
- declare visibility and useful parameter/return types; use short PHP type keywords;
- use `PascalCase` classes/interfaces/traits, `camelCase` methods, and `UPPER_SNAKE_CASE` constants;
- keep one class/interface/trait/enum per file unless a tightly coupled private exception is documented;
- do not rely on deprecated PSR-0/PSR-2 formatting or underscore autoloading.

PSR-12 does not define architecture, security, validation, tenancy, or test quality. Those remain governed by [MODULES.md](../architecture/MODULES.md), [SECURITY.md](../architecture/SECURITY.md), [TENANCY.md](../architecture/TENANCY.md), and [TESTING.md](TESTING.md).

## Package boundaries

Reusable modules must:

- expose PSR-4 Composer autoloading with stable namespaces and no runtime filesystem scanning;
- depend on interfaces at replaceable infrastructure boundaries and keep framework adapters at the edge;
- avoid leaking Laravel models, container lookups, global state, secrets, or mutable authorization context through generic PSR interfaces;
- document which PSR interfaces are implemented, consumed, or intentionally not applicable;
- preserve exception, immutability, stream, request, response, cache, event, and clock semantics required by the relevant PSR;
- test both the concrete Laravel adapter and the portable package contract where a PSR boundary is public.

## Statuses we do not adopt as normative standards

| PSR | Status | Policy |
|---|---|---|
| PSR-0 | Deprecated | Do not add underscore-based autoloading; use PSR-4 |
| PSR-2 | Deprecated | Use PSR-12, which supersedes it |
| PSR-5 | Draft | PHPDoc style may follow current tooling, but PSR-5 is not a release contract |
| PSR-8 | Abandoned | No implementation requirement |
| PSR-9 | Abandoned | Use [SECURITY.md](../architecture/SECURITY.md) and repository-specific disclosure procedures |
| PSR-10 | Abandoned | Use repository security policy and current PHP-FIG guidance |
| PSR-19 | Draft | Use project localization contracts and [DOCUMENTATION.md](DOCUMENTATION.md) until accepted |
| PSR-21 | Draft | Use explicit tracing/correlation contracts defined by [API.md](../architecture/API.md) and observability documentation |
| PSR-22 | Draft | Use the repository's supported tracing implementation until the PSR is accepted |

Draft PSRs may inform design reviews but must not be cited as stable compatibility promises. The PSR index is the source for status changes.

## Verification

CI should run the repository formatter, static analysis, Composer autoload validation, architecture checks, and tests for every changed PHP package. Contract tests cover PSR interfaces at public boundaries; integration tests prove the Laravel adapter. Dependency updates must verify that a library still implements the declared PSR version and does not silently change exception, cache, event, HTTP, or time semantics.

## References

- [PHP-FIG](https://www.php-fig.org/)
- [PHP-FIG PSR index and statuses](https://www.php-fig.org/psr/)
- [PSR-12 full specification](https://www.php-fig.org/psr/psr-12/)
- [PSR naming conventions](https://www.php-fig.org/bylaws/psr-naming-conventions/)
- [Composer PSR-4 autoloading](https://getcomposer.org/doc/04-schema.md#psr-4)
- [Laravel service container](https://laravel.com/docs/13.x/container)
