# minimalistic server example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from node import *
import json


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

    @request
    def increment(self, graph):
        graph.val += 1
        for c in graph.children:
            increment(c)
        return graph

    @request
    def toGraph(self, dictionary):
        root = node()

        for key in dictionary:
            if key == 'name':
                print dictionary[key]
                root = node(dictionary[key])


# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
    s, _ = ss.accept()
    # JSONRpc object spawns internal thread to serve the connection.
    JSONRpc(s, ServerServices())
Client


