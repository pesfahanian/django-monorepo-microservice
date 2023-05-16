#!/bin/bash

echo "============ Ledger ============="
python $1/manage.py runserver 0.0.0.0:8201 & \
watchmedo auto-restart --directory=./ --pattern='*.py' --recursive -- celery -A service.ledger.config worker -l info -n dmm-ledger-worker.%h
# TODO: Try to make `service.ledger.config` work with `$1`.
