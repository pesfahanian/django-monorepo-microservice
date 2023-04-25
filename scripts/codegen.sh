#!/bin/bash

protos=`ls ./proto/*.proto`
for proto in $protos
do
    python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. "$proto"
done
