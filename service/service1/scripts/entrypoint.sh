#!/bin/bash

set -e

echo "============= Applying Database Migrations ============="
python manage.py migrate

echo "=================== Running Commands ==================="

echo "=================== Starting Servers ==================="
python manage.py runserver 0.0.0.0:8200 & \
python manage.py grpcserver --port 50150
