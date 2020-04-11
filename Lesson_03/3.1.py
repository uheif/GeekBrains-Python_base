def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Вы пытаетесь делить на ноль")


# a, b = (int(i) for i in input().split())
print(division(a=int(input("Введите делимое: ")), b=int(input("Введите делитель: "))))

'****************************************************************************************'


def division2():
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    try:
        return print(a / b)
    except ZeroDivisionError:
        print("Вы пытаетесь делить на ноль")


division2()
