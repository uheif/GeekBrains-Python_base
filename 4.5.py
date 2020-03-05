from functools import reduce

my_list = [i for i in range(100, 1001, 2)]
result = reduce(lambda acc, x: acc * x, my_list)
print(result)