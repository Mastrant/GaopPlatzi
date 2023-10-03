from estructurasLineales.Nodos import Nodo


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Nodo(data)

        if self.tail is None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current.next = node

        self.size += 1

    def size(self):
        return str(self.size)

    def iter(self):
        puntero = self.tail
        while puntero:
            value = puntero.data
            puntero = puntero.nextNode
            yield value

    def __delete__(self, instance):
        current = self.tail
        nodePrevius = self.tail

        while current:
            if current.data == instance:
                if current == self.tail:
                    self.tail = current.nextNode
                else:
                    nodePrevius.nextNode = current.nextNode
                    self.size -= 1
                    return current.data
            nodePrevius = current
            current = current.nextNode

    def search(self, dato):
        for puntero in self.iter():
            if dato == puntero:
                return True
        return False
