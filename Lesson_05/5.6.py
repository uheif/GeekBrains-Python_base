my_dict = {}
with open("5.6.txt") as inf:
    for line in inf:
        classes = []
        for el in line.split()[1:]:
            for i in el:
                if not i.isdigit():
                    el = el.replace(i, '')
            if el.isdigit():
                classes.append(el)
        my_dict[line.split()[0]] = sum(list(map(int, classes)))
print(my_dict)
