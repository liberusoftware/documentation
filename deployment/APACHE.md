# Apache

Use Apache HTTP Server as the public HTTP/TLS server and connect Laravel to PHP-FPM through `mod_proxy_fcgi`. Set the document root to Laravel's `public/` directory and keep the application source outside the public path.

## Virtual host

Enable the required modules for the distribution, normally `rewrite`, `headers`, `ssl`, `proxy`, and `proxy_fcgi`. A minimal virtual host is:

```apache
<VirtualHost *:80>
    ServerName app.example.test
    DocumentRoot /var/www/app/public

    <Directory /var/www/app/public>
        AllowOverride None
        Require all granted
        DirectoryIndex index.php
        FallbackResource /index.php
    </Directory>

    <FilesMatch "\\.php$">
        SetHandler "proxy:unix:/run/php/php8.5-fpm.sock|fcgi://localhost/"
    </FilesMatch>

    <DirectoryMatch "^/var/www/app/(?!public/)" >
        Require all denied
    </DirectoryMatch>

    ErrorLog ${APACHE_LOG_DIR}/app-error.log
    CustomLog ${APACHE_LOG_DIR}/app-access.log combined
</VirtualHost>
```

Adapt the PHP-FPM socket, paths, and log locations to the host. Prefer explicit Apache configuration over broad `.htaccess` permissions. Add a separate HTTPS virtual host or trusted load-balancer configuration and redirect HTTP to HTTPS.

## Production rules

- Run `apachectl configtest` before a graceful reload.
- Do not enable forward proxying; `ProxyRequests` must remain off unless a secured, explicit use case requires otherwise.
- Keep PHP-FPM on a private socket/network and size its pool for available resources.
- Restrict access to `.env`, `.git`, `vendor/`, storage internals, and all non-public application files.
- Set request, upload, timeout, header, and process limits deliberately.
- Redact sensitive headers, query parameters, and request bodies from logs.
- Use valid TLS certificates, secure headers, backups, health checks, and monitoring.

## Verification

Check configuration syntax, TLS, Laravel routes, PHP-FPM execution, static files, uploads, denied application files, logs, queue/realtime integration, and graceful reload behavior.

## References

- [Apache HTTP Server documentation](https://httpd.apache.org/docs/2.4/)
- [Apache `mod_proxy_fcgi`](https://httpd.apache.org/docs/2.4/mod/mod_proxy_fcgi.html)
- [Apache `mod_proxy` security warning](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html)
- [Laravel deployment](https://laravel.com/docs/13.x/deployment)
- [Deployment index](README.md)
