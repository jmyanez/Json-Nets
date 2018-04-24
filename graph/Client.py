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
def convert(graph,EmptyDictionary):
    #print "myDict is ", myDict

    if graph == None:
        return EmptyDictionary

    elif graph.children != None:
        EmptyDictionary["name"]= graph.name
        EmptyDictionary["val"]= graph.val
        for c in graph.children:
            child = c.__dict__
            EmptyDictionary["children"].append(child)
        #print EmptyDictionary
    return EmptyDictionary

def toGraph(Dictionary):
    root = node("root", [])

    for key in dictionary:
        if key == 'name':
            root.name = dictionary[key]
            # print "root name is:" ,root.name

        elif key == 'val':
            root.val = dictionary[key]
            # print "root value is:", root.val

        elif key == 'children':
            # print "Children are:", root.children
            leaf1 = node("leaf1")
            leaf2 = node("leaf2")
            for x in dictionary[key]:
                root.children = leafx = node("x")
                for y in x:
                    if x["name"] == 'leaf1':
                        leaf1.name = x["name"]
                        leaf1.val = x["val"]
                        leaf1.children = x["children"]
                    # print "leaf 1 name is:" , leaf1.name

                    elif x["name"] == 'leaf2':
                        leaf2.name = x["name"]
                        leaf2.val = x["val"]
                        leaf2.children = x["children"]
                        # print "leaf 2 name is:" , leaf2.name

            root = node("root", [leaf1, leaf1, leaf2])
            root.show()
            return root

dictionary = {"name":None,"val":None,"children":[]}
dictRoot = convert(root,dictionary)
#print dictRoot
#dictRoot = json.dumps(dictRoot,sort_keys=True)
result = server.toGraph(dictRoot)
x =  toGraph(result)
x.show()
#print resultGraph




rpc.close() # Closes the socket 's' also


