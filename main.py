#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grpc_app import create_app

host = '0.0.0.0'
port = 50051
server = create_app(host, port)
server.serve()
