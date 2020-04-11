def int_func(word):
    if type(word) is str:
        return word.capitalize()
    else:
        print("Передаваемый аргумент должен быть строкой")


print(int_func("kjhdsf"))

my_str = input("Введите строку из слов, разделенных пробелом: ").lower().split()
for i in my_str:
    print(int_func(i), end=' ')
