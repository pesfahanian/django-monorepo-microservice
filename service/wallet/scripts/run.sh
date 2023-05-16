#!/bin/bash

echo "============ Wallet ============="
python $1/manage.py runserver 0.0.0.0:8200 & \
watchmedo auto-restart --directory=./ --pattern='*.py' --recursive -- celery -A service.wallet.config worker -l info -n dmm-wallet-worker.%h
# TODO: Try to make `service.wallet.config` work with `$1`.
