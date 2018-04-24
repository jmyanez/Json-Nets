# Json-Nets

Output of Client:

C:\Users\manue\PycharmProjects\s18-nets-tcp-file-transfer-jmyanez\venv\Scripts\python.exe C:/Users/manue/PycharmProjects/nets-jsonrpc-jmyanez/graph/Client.py
Traceback (most recent call last):
myDict is  {}
  File "C:/Users/manue/PycharmProjects/nets-jsonrpc-jmyanez/graph/Client.py", line 43, in <module>
[<node.node instance at 0x04F57148>, <node.node instance at 0x04F57148>, <node.node instance at 0x04F57170>]
    dictRoot = convert(root,dict())
myDict is  {'name': 'root', 'val': 0, 'children': [<node.node instance at 0x04F57148>, <node.node instance at 0x04F57148>, <node.node instance at 0x04F57170>]}
  File "C:/Users/manue/PycharmProjects/nets-jsonrpc-jmyanez/graph/Client.py", line 38, in convert
    child = convert(c,myDict)
  File "C:/Users/manue/PycharmProjects/nets-jsonrpc-jmyanez/graph/Client.py", line 27, in convert
myDict is  {'name': 'root', 'val': 0, 'children': [<node.node instance at 0x04F57148>, <node.node instance at 0x04F57148>, <node.node instance at 0x04F57170>, {'name': 'leaf1', 'val': 0, 'children': []}]}
    elif graph.name != "root":
AttributeError: 'dict' object has no attribute 'name'
myDict is  {'name': 'root', 'val': 0, 'children': [<node.node instance at 0x04F57148>, <node.node instance at 0x04F57148>, <node.node instance at 0x04F57170>, {'name': 'leaf1', 'val': 0, 'children': []}, {'name': 'leaf1', 'val': 0, 'children': []}]}
myDict is  {'name': 'root', 'val': 0, 'children': [<node.node instance at 0x04F57148>, <node.node instance at 0x04F57148>, <node.node instance at 0x04F57170>, {'name': 'leaf1', 'val': 0, 'children': []}, {'name': 'leaf1', 'val': 0, 'children': []}, {'name': 'leaf2', 'val': 0, 'children': []}]}
