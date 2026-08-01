# NGINX

Use NGINX as the public HTTP/TLS server and reverse proxy to PHP-FPM. Serve only Laravel's `public/` directory; never expose the repository root, `.env`, `vendor/`, or storage internals.

## Document root and PHP-FPM

Set the document root to `/var/www/app/public`, pass only existing PHP scripts to PHP-FPM, and use a Unix socket or private network address. A minimal server block is:

```nginx
server {
    listen 80;
    server_name app.example.test;
    root /var/www/app/public;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass unix:/run/php/php8.5-fpm.sock;
    }

    location ~ /\. {
        deny all;
    }
}
```

Use the correct PHP-FPM socket for the host. Terminate HTTPS with a valid certificate, redirect HTTP to HTTPS, and preserve the original scheme/host headers when a trusted load balancer is in front.

## Production rules

- Validate configuration with `nginx -t` before reload; reload gracefully.
- Set bounded client body size, request/read timeouts, buffering, and upload limits appropriate to the application.
- Do not cache authenticated, session, or authorization-bearing responses.
- Send access/error logs to centralized storage with sensitive headers and query data redacted.
- Keep PHP-FPM private, size its pool for available CPU/memory, and monitor saturation.
- Add rate limiting and security headers at the appropriate trusted boundary.
- Use a separate configuration for each site and protect certificate/private-key permissions.

## Verification

Check the TLS certificate, application health endpoint, static assets, PHP execution, queue/realtime routes, upload limits, denied dotfiles, Laravel storage link, logs, and graceful reload behavior.

## References

- [NGINX documentation](https://nginx.org/en/docs/)
- [NGINX FastCGI module](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html)
- [Laravel deployment](https://laravel.com/docs/13.x/deployment)
- [Deployment index](README.md)
