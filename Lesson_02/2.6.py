specs = {"название": None, "цена": None, "количество": None, "eд": None}    # тут мог быть список, но хотелось потренить словари)
goods = []

for i in range(int(input("Введите целое положительное количество товаров: "))):
    item_num = i + 1
    item_specs = {}
    for spec in specs:
        item_specs[spec] = input(f"{spec} товара: ")
    goods.append((item_num, item_specs))
print(goods)

analytics = {}

for spec in specs:
    analytics[spec] = []
    for i in range(len(goods)):
        if goods[i][1][spec] not in analytics[spec]:    # наверное, не очень правильно, что здесь в индексе циферка, а не переменная
            analytics[spec].append(goods[i][1][spec])    # и здесь)
print(analytics)
