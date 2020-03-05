def fact(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
        yield acc


gen = fact(5)
print(gen)
for el in gen:
    print(el)
