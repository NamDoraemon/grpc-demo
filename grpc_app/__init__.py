#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grpc_app.server import GRPCServer
from grpc_app.proto import pings_pb2, pings_pb2_grpc

from grpc_app.services.ping import PingService


def create_app(address='0.0.0.0', port=50051):
    server = GRPCServer(address, port)
    addServices(server.instance)
    return server


def addServices(server_grpc):
    pings_pb2_grpc.add_PingsServicer_to_server(PingService(), server_grpc)
