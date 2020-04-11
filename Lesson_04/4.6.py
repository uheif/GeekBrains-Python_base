from random import random
from itertools import count
from itertools import cycle

start = int(random() * 4)
finish = int(start + random() * 10)

my_list = ['a', 'b', 'c']

"""Лесенка :)"""
for num in count(start):
    if num > finish:
        break
    else:
        print(num, end=' ')
    i = 0
    for el in cycle(my_list):
        if i == num:
            break
        else:
            print(el, end=' ')
        i += 1
    print()
