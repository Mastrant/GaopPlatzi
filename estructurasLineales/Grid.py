from estructurasLineales.Array import Array


class Grid:
    def __init__(self, rows: int, col: int, data=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(col, data)

    def lenth(self):
        return len(self.data)

    def witdh(self):
        return len(self.data[0])

    def __str__(self):
        items = " "
        for row in range(self.lenth()):
            for col in range(self.witdh()):
                items += str(self.data[row][col]) + " "
            items += "\n"
        return items

    def __getitem__(self, index):
        return self.data[index]

    def firt(self):
        return self.data[0]