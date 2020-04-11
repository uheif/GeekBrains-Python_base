class MyErr(Exception):
    def __init__(self, message):
        self.message = message


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise MyErr("На ноль хотите поделить вы")
except ValueError:
    print("Не число ввели вы")
except MyErr as err:
    print(err)
else:
    print(round(a / b, 2))
