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
def convert(graph, myDict,EmptyDictionary):
    #print "myDict is ", myDict

    if graph == None:
        return myDict

    elif graph.children != None:
        EmptyDictionary["name"]= graph.name
        EmptyDictionary["val"]= graph.val
        for c in graph.children:
            child = c.__dict__
            EmptyDictionary["children"].append(child)


        #print EmptyDictionary

    return EmptyDictionary


dictionary = {"name":None,"val":None,"children":[]}
dictRoot = convert(root,root,dictionary)
print dictRoot


print "graph after increment"
#print(result)
rpc.close() # Closes the socket 's' also


