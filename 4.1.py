from sys import argv, exit

"""Сначала сделал, чтобы с ошибками скрипт отрабатывал до конца, но, думаю, тут правильнее делать sys.exit"""


def point_float(string):
    """Заменяем запятую на точку и применяем float()"""
    return float(string.replace(',', '.'))


def salary_calc(your_hours, your_rate, your_bonus):
    """Рассчет зарплаты"""
    return round((point_float(your_hours) * point_float(your_rate) + point_float(your_bonus)), 2)


try:
    script_name, hours, rate, bonus = argv
except ValueError:
    print("""Вы указали неверное количество параметров. Укажите три числа через пробел в качестве параметров,
а то айайай.""")
    # hours, rate, bonus = input("Давайте ка ещё раз: ").split()
    exit()

# params = list(map(point_float, argv[1:]))
# params = (point_float(i) for i in argv[1:])
# for i in params:
#     print(i)

try:
    print(f"Вот та самая зарплата, которую вы просили: {salary_calc(hours, rate, bonus)}")
except ValueError:
    print("Укажите числовые значения в качестве параметров, а то айайай.")
    exit()
# except NameError:
#     print("Невозможно рассчитать зарплату при неверноем количестве параметров.")
