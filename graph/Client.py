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

#Generate the Graph that we will user for increment
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

#Convert the graph into a Dictionary to be send by Json
def convert(graph,EmptyDictionary):
    if graph == None:
        return EmptyDictionary
    elif graph.children != None:
        EmptyDictionary["name"]= graph.name
        EmptyDictionary["val"]= graph.val
        for c in graph.children:
            child = c.__dict__
            EmptyDictionary["children"].append(child)
    return EmptyDictionary

#Convert dictionary to Graph
def toGraph(dictionary):
    root = node("root", [])
    leaf1 = node("leaf1")
    leaf2 = node("leaf2")

    for key in dictionary:
        if dictionary["name"] == "root":
            root.name = dictionary["name"]
            root.val = dictionary["val"]
            #print "Root name is:",root.name
            if key == 'children':
                # print "Children are:", root.children
                for x in dictionary[key]:
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
                root.children = [leaf1,leaf1,leaf2]
                #root = node("root",[leaf1,leaf1,leaf2])
                # root.show()
        return root

#Declare an empty dictionary that will serve as container for dictionary with graph values
dictionary = {"name":None,"val":None,"children":[]}
dictRoot = convert(root,dictionary)
#Before Increment
print "Before:"
root.show()
# Execute in server:
result = server.toGraph(dictRoot)
x = toGraph(result)
print "After:"
x.show()
#print resultGraph
rpc.close() # Closes the socket 's' also


