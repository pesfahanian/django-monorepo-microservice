#!/bin/bash

echo "============== PG ==============="
watchmedo auto-restart --directory=./ --pattern='*.py' --recursive -- python $1/manage.py grpcserver --port 50150
