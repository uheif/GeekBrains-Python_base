class MyExt(Exception):
    def __init__(self, message):
        self.message = message


my_lst = []
el = ''
while True:
    try:
        el = input("Введите число (для выхода введите 'q'): ")
        if el == 'q':
            break
        if not el.isdigit():  # по условию надо проверять тип вводимых данных, но это же всегда строка...
            raise MyExt("То не число и не 'q', что ввели вы!")
    except MyExt as err:
        print(err)
    my_lst.append(el)
print(my_lst)

# прикрутить отрицательные числа
