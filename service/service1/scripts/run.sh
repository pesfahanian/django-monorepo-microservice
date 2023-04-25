#!/bin/bash

echo "============ Service1 ============="

python $1/manage.py runserver 0.0.0.0:8200
