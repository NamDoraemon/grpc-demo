build:
    # Linux
    python -m grpc_tools.protoc -I=./protobuf/ --python_out=./grpc_app/proto --grpc_python_out=./grpc_app/proto ./protobuf/*.proto
    # Windwos
    python -m grpc_tools.protoc --proto_path=./protobuf/ --python_out=./grpc_app/proto --grpc_python_out=./grpc_app/proto ./protobuf/*.proto