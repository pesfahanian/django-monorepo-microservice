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

echo "=================== Starting Servers ==================="
python ./service/pg/manage.py grpcserver --port 50150
