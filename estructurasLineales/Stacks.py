from estructurasLineales.Nodos import Nodo
from estructurasLineales.Array import Array


class StackNode:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Nodo(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        # En caso de que haya un elemento
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.nextNode:
                self.top = self.top.nextNode
            else:
                self.top = None
            return data

        else:
            return "empy"

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "empy"

    def clear(self):
        while self.top:
            self.pop()


class StackArray:
    def __init__(self, Size: int = 1):
        self.top = None
        self.size = Size

    def push(self, data):
        array = Array(self.size, data)
        for e in array.__iter__():
            if array.items[e + 1] is None:
                array.items[e] = data
