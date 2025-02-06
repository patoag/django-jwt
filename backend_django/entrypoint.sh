#!/bin/sh

# Esperar a que la base de datos esté lista antes de ejecutar las migraciones
echo "Esperando a que la base de datos esté disponible..."
while ! nc -z db_postgres 5432; do   
  sleep 1
done
echo "Base de datos disponible!"

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Ejecutar Gunicorn
echo "Iniciando Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 backend_django.wsgi:application
