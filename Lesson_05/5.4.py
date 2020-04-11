translate = {"One": "Один",
             "Two": "Два",
             "Three": "Три",
             "Four": "Четыре"}

with open("5.4.txt") as inf, \
     open("5.4_translate.txt", 'w') as ouf:
    for line in inf:
        eng = line.split()[0]
        if eng in translate:
            ouf.write(line.replace(eng, translate[eng]))