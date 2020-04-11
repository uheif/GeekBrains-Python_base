from random import randint

with open("5.5.txt", 'w+') as ouf:
    my_line = ' '.join([str(randint(1, 100)) for i in range(10)])
    print(my_line)
    ouf.write(my_line)
    ouf.seek(0)
    print(sum(list(map(int, ouf.readline().split()))))
