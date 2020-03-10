with open("5.2.py") as inf:
    lines = inf.readlines()

lines_len = len(lines)
for i in range(lines_len):
    print(f"Строка {i + 1} содержит {len(lines[i].split())} слов")

'''**********************************************************************************************'''

inf = open("5.2.py")
cnt = 1
for line in inf:
    print(f"Строка {cnt} содержит {len(line.split())} слов")
    cnt += 1
inf.close()

'''**********************************************************************************************'''

with open("5.2.py") as inf:
    cnt = 1
    while True:
        line = inf.readline()
        if not line:
            break
        print(f"Строка {cnt} содержит {len(line.split())} слов")
        cnt += 1
