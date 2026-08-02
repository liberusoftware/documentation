# Laravel Reverb

Use Laravel Reverb for first-party WebSocket broadcasting when the application needs realtime updates. Run Reverb as a separate supervised process and place it behind TLS and a trusted reverse proxy.

## Configuration

- Keep Reverb credentials, host, ports, and allowed origins in runtime secret/configuration storage.
- Bind Reverb privately and expose only the proxy endpoint; use `wss://` in production.
- Authorize private and presence channels through Laravel policies and team context. Never trust client-supplied channel membership.
- Use a shared broadcast backend and durable queues when running more than one Reverb instance.
- Bound connections, message sizes, event rates, and idle timeouts. Do not broadcast secrets or unnecessary personal data.

```bash
php artisan reverb:start --host=127.0.0.1 --port=8080
```

Supervise the process with [Supervisor](SUPERVISORD.md), containers, or Kubernetes. Monitor connections, rejected handshakes, event latency, queue delay, memory, restarts, and proxy upgrade failures. Test reconnect, deploy drain, authorization denial, and multi-instance delivery.

## References

- [Laravel Broadcasting](https://laravel.com/docs/13.x/broadcasting)
- [Laravel Reverb](https://laravel.com/docs/13.x/reverb)
- [NGINX](NGINX.md)
- [Deployment index](README.md)
