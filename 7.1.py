class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx
        self.width = len(min(mtx, key=len))
        self.height = len(mtx)

    def __str__(self):
        # найдём самый длинный элемент в матрице, чтоб красиво пробелы
        max_el_len = 0
        for lst in self.mtx:
            if len(max(list(map(str, lst)), key=len)) > max_el_len:
                max_el_len = len(max(list(map(str, lst)), key=len))

        str_mtx = ''
        for row in range(self.height):
            # str_mtx += ''.join([str(el) + (' ' * ((max_el_len - len(str(el))) + 1)) for el in self.mtx[row]]) + '\n'
            for el in self.mtx[row]:
                space = ' ' * ((max_el_len - len(str(el))) + 1)
                str_mtx += str(el) + space
            str_mtx += '\n'
        return str_mtx

    def __add__(self, other):
        add_mtx = []
        for row in range(min(self.height, other.height)):
            add_mtx.append(
                [self.mtx[row][i] + other.mtx[row][i] for i in range(min(self.width, other.width))]
            )
        return Matrix(add_mtx)


my_mtx = Matrix([[el for el in range(3)] for row in range(3)])
my_mtx2 = Matrix([[el for el in range(4)] for row in range(4)])
print(my_mtx)
print(my_mtx + my_mtx2)
my_mtx3 = Matrix([[-33, 2, 11, 4, 0], [1224, 145664564, 11, 4]])
print(my_mtx3 + my_mtx2)
