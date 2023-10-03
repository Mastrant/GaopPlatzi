class Node:
    def __init__(self, data, nextnode=None):
        self.data: data
        self.next = nextnode


class TwoWayNode(Node):
    def __init__(self, data, previusNode=None, nextNode=None ):
        Node.__init__(self, data, nextNode)
        self.previusNode = previusNode

