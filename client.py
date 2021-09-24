#!/usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import loguru

from grpc_app.proto import pings_pb2, pings_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = pings_pb2_grpc.PingsStub(channel)
response = stub.Call(pings_pb2.RequestMessage(msg='pong'))
loguru.logger.info(response)
