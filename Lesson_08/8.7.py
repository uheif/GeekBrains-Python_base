class ComplexNums:
    i = 'i'  # простите, я гуманитарий :(

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        str_a = str(self.a)
        str_b = str(self.b)
        return f"{str_a} + {str_b + ComplexNums.i}"

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNums(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.a * other.b
        return ComplexNums(a, b)


my_num = ComplexNums(2, -3)
new_num = ComplexNums(5, 2)
sum_num = my_num + new_num
print(sum_num)
print(my_num * new_num)
