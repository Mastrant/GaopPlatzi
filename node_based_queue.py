class TwoWayNode(object):
    def __init__(self, data=None, previusNode=None, nextNode=None):
        self.data: data
        self.nextNode = nextNode
        self.previusNode = previusNode


class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        newNode = TwoWayNode(data, None, None)

        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.previusNode = self.tail
            newNode.nextNode = newNode

        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previusNode = None
            self.count -= 1

        return current.data
