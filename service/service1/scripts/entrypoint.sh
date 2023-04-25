#!/bin/bash

set -e

echo "=================== Starting Servers ==================="
python ./service/service1/manage.py runserver 0.0.0.0:8200
