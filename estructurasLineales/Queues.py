class ListQueues:
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        for item in range(self.size):
            print(self.items[item])


class StackQueues:
    def __init__(self):
        self.internoStack = []
        self.externoStack = []

    def enqueue(self, data):
        self.internoStack.append(data)


    def dequeue(self):
        if not self.externoStack:
            while self.internoStack:
                self.externoStack.append(self.internoStack.pop())

