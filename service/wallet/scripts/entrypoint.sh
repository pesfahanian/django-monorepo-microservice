#!/bin/bash

set -e

echo "============= Applying Database Migrations ============="
python ./service/wallet/manage.py migrate

echo "=================== Running Commands ==================="
python ./service/wallet/manage.py createadmin
python ./service/wallet/manage.py seed

echo "=================== Starting Servers ==================="
python ./service/wallet/manage.py runserver 0.0.0.0:8200
