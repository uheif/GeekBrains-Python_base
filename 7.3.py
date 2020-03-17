class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            return "Ой!"

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_row):
        return ('*' * cells_in_row + r'\n' + '\n') * (self.cells // cells_in_row) + \
               ('*' * (self.cells % cells_in_row))


print(Cell(17).make_order(5))
cell_1, cell_2 = Cell(12), Cell(7)
print((cell_1 + cell_2).cells)
print((cell_1 - cell_2).cells)
no_cell = cell_2 - cell_1
print(no_cell)
print((cell_1 * cell_2).cells)
print((cell_1 / cell_2).cells)
