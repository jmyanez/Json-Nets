class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print "%s%s val=%d:" % (level*"  ", self.name, self.val)
        for c in self.children: 
            c.show(level + 1)
#Modified increment function to only increment a child once
def increment(graph,nodeName):
  if graph.name not in nodeName:
      graph.val += 1
      nodeName.append(graph.name)
      for c in graph.children:
          increment(c,nodeName)
      return graph
  else:
      return graph

#Function to convert graph to dictionary
def toDictionary(graph,Dictionary):
  if graph == None:
      return Dictionary

  elif graph.children != None:
      Dictionary["name"] = graph.name
      Dictionary["val"] = graph.val
      for c in graph.children:
          child = c.__dict__
          Dictionary["children"].append(child)
      # print EmptyDictionary
  return Dictionary

#Function to convert dictionary to graph
def toGraph(dictionary):
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