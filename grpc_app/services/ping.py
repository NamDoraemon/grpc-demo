#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grpc_app.proto import pings_pb2, pings_pb2_grpc


class PingService(pings_pb2_grpc.PingsServicer):
    def Call(self, request, context):
        return pings_pb2.ResponseMessage(msg=request.msg)
