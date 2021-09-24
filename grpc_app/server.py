#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import sys
from concurrent import futures
import grpc
from loguru import logger


class GRPCServer(object):

    def __init__(self, address='[::]', port=50051):
        self.__address = address
        self.__port = port
        self.__server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        def signalHandler(signal, frame):
            self.__server.stop()
            sys.exit()

        signal.signal(signal.SIGINT, signalHandler)

    @property
    def instance(self):
        return self.__server

    def serve(self):
        endpoint = f'{self.__address}:{self.__port}'

        logger.info(f'Starting grpc server at port {self.__port}')
        logger.info(f'Serving at {endpoint}...')

        self.__server.add_insecure_port(endpoint)
        self.__server.start()
        self.__server.wait_for_termination()
