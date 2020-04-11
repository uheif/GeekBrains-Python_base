def make_my_list(some_list):
    """
    Функция создаёт список из чисел на основе ввода пользователя
    и вычисляет сумму этих чисел
    """
    # my_list = [int(i) for i in my_input if i.isdigit()]    # баловство!

    my_list = []
    for i in some_list:
        """
        прикрутил костыль, чтобы работало с отрицательными числами, 
        наверное, есть более правильный способ :)
        """
        if i[0] == '-':
            if i[1:].isdigit():
                my_list.append(int(i[1:]) * -1)
        else:
            if i.isdigit():
                my_list.append(int(i))

    return my_list

my_input = ['']
my_sum = 0
while my_input[-1] != 'q':
    my_input = input("Введите числа через пробел. Для выхода ввыедите 'q': ").lower().split()
    if not my_input:
        continue
    my_sum += sum(make_my_list(my_input))
    # хотелось сделать sum() в самой функции, но не придумал как тогда следующую проверку провернуть)
    # это чтобы не выводить результат повторно, и не выводить 0, если пользователь захотел выйти в первой же итерации
    if len(make_my_list(my_input)) > 0:
        print(my_sum)

print("Программа завершена.")
