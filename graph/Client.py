# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart
from node import node
import socket
from bsonrpc import JSONRpc
import json
from collections import OrderedDict

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s)
server = rpc.get_peer_proxy()

"""Convert node into something that can be passed by jason and viceversa """
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

# Execute in server:
def convert(graph, myDict):
    print "myDict is ", myDict
    if not graph:
        return myDict

    elif graph.name != "root":
        child = graph.__dict__
        if "children" not in myDict:
            myDict["children"] = []
        return child

    elif graph.children != None:
        myDict = graph.__dict__
        temp = graph
        print temp.children
        for c in graph.children:
            child = convert(c,myDict)
            myDict["children"].append(child)
        return myDict

 #   for c in graph.children:
dictRoot = convert(root,dict())
print dictRoot
#result = server.increment(dictRoot)

print "graph after increment"
#print(result)
rpc.close() # Closes the socket 's' also


