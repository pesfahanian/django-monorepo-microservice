#!/bin/bash

set -e

echo "=================== Starting Servers ==================="
python ./service/wallet/manage.py runserver 0.0.0.0:8200
