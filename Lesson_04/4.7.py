def fact(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
        yield acc


gen = fact(20)
print(gen)
cnt = 0
for el in gen:
    if cnt > 15:
        break
    print(el)
    cnt += 1
