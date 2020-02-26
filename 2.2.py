number_of_elements = int(input("Введите количество элементов списка: "))
my_list = []
for i in range(number_of_elements):
    my_list.append(input("Введите элемент списка: "))

print(my_list)

if len(my_list) % 2 == 0:
    len_my_list = len(my_list)
else:
    len_my_list = len(my_list) - 1

for i in range(0, len_my_list, 2):
    a = my_list[i]
    my_list[i] = my_list[(i + 1)]
    my_list[(i + 1)] = a

print(my_list)

# написать вариант решения с созданием нового списка