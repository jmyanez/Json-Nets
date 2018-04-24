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
  def increment(self,graph):
      graph.val += 1
      for c in graph.children:
          increment(c)
      return graph

  @request
  def toGraph(self,dictionary):
    root = node("root",[])

    for key in dictionary:
     if key == 'name':
         root.name= dictionary[key]
         #print "root name is:" ,root.name

     elif key=='val':
         root.val= dictionary[key]
         #print "root value is:", root.val

     elif key=='children':
         #print "Children are:", root.children
         leaf1 = node("leaf1")
         leaf2 = node("leaf2")
         for x in dictionary[key]:
            root.children = leafx=node("x")
            for y in x:
              if x["name"]=='leaf1':
                    leaf1.name = x["name"]
                    leaf1.val = x["val"]
                    leaf1.children=x["children"]
                   # print "leaf 1 name is:" , leaf1.name

              elif x["name"]=='leaf2':
                    leaf2.name = x["name"]
                    leaf2.val = x["val"]
                    leaf2.children=x["children"]
                    #print "leaf 2 name is:" , leaf2.name

         root = node("root",[leaf1,leaf1,leaf2])
         root.show()
         increment(root)
         root.show()
         dictionary = {"name": None, "val": None, "children": []}
         dictionary= toDictionary(root,dictionary)
         return dictionary



# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices())
Client


#