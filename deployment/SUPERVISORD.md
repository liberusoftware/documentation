# Supervisor

Use Supervisor to keep Laravel workers, the scheduler, and optional Inertia SSR or Reverb processes running on a standalone host. Run one process type per program entry and keep configuration in the deployment repository.

```ini
[program:laravel-worker]
command=php /var/www/app/artisan queue:work redis --sleep=1 --tries=3 --timeout=120 --max-time=3600
directory=/var/www/app
user=www-data
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stopwaitsecs=150
redirect_stderr=true
stdout_logfile=/var/log/supervisor/laravel-worker.log
```

Use separate entries for `schedule:work`, Horizon, Reverb, and Inertia SSR as applicable. Never run workers as root or allow broad writable paths. Align worker timeout, memory limits, retry policy, and graceful termination with [QUEUES.md](QUEUES.md).

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart laravel-worker:*
sudo supervisorctl status
```

Verify boot after restart, graceful deployment, log rotation, failed jobs, queue health, scheduler ticks, realtime connections, and SSR behavior.

## References

- [Supervisor documentation](http://supervisord.org/)
- [Laravel queue workers](https://laravel.com/docs/13.x/queues#supervisor-configuration)
- [Deployment index](README.md)
