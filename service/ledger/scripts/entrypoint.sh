#!/bin/bash

set -e

here=`pwd`

echo "============= Applying Database Migrations ============="
python ./service/ledger/manage.py migrate

echo "=================== Running Commands ==================="
python ./service/ledger/manage.py createadmin

echo "=================== Starting Servers ==================="
python ./service/ledger/manage.py runserver 0.0.0.0:8201 & \
celery -A service.ledger.config worker -l info -n dmm-ledger-worker
