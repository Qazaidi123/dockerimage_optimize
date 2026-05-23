FROM php:8.2

COPY . /var/www/html/

# Permissions
RUN chmod -R 755 /var/www/html
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
