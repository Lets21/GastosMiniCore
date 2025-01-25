#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Limpiar migraciones existentes (excepto __init__.py)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Crear y aplicar migraciones
python manage.py makemigrations gestion
python manage.py migrate
python manage.py migrate gestion zero
python manage.py migrate gestion

# Archivos estáticos y datos iniciales
python manage.py collectstatic --no-input
python manage.py loaddata initial_data.json
