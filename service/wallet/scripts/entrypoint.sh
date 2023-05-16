#!/bin/bash

set -e

here=`pwd`

echo "================= Running gRPC Codegen ================="
protos=`ls ./proto/*.proto`
for proto in $protos
do
    python -m grpc_tools.protoc \
        -I . \
        --python_out=. \
        --grpc_python_out=. \
        "$proto"
done

echo "============= Applying Database Migrations ============="
python ./service/wallet/manage.py migrate

echo "=================== Running Commands ==================="
python ./service/wallet/manage.py createadmin

echo "=================== Starting Servers ==================="
python ./service/wallet/manage.py runserver 0.0.0.0:8200 & \
celery -A service.wallet.config worker -l info -n dmm-wallet-worker
