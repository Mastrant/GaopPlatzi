class Array:
    def __init__(self, length, dato=None):
        self.items = list()
        for e in range(length):
            self.items.append(dato)

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, item):
        self.items[index] = item

    def __iter__(self):
        return iter(self.items)
