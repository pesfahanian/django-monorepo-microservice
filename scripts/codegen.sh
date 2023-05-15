#!/bin/bash

set -e

here=`pwd`

protos=`ls ./proto/*.proto`
for proto in $protos
do
    python -m grpc_tools.protoc \
        -I . \
        --python_out="$here/generated" \
        --grpc_python_out="$here/generated" \
        "$proto"
done

mv "$here/generated/proto"/* "$here/generated"
rm -r "$here/generated/proto"
