# Небольшой тест по мотивам первой лекции :)

print("Давайте вспомним, что мы узнали на первой лекции. Вводите, пожалуйста, ваши ответы в нижнем регистре.")
print()
points = 0

count = 1
while count <= 3:
    user_answer = input(f"Вопрос 1. Попытка {count} (из 3х). Угадайте к какому типу данных относится номер попытки: ")
    if type(count) is int and user_answer == "int" or user_answer == "integer":
        points += 1
        print("Вы молодец!")
        break
    count += 1
if points == 0:
    print('Правильный ответ "int" или "integer"')

answer = "нет"
user_answer = input('Вопрос 2. Корректно ли такое название переменной? - "3tankista" (да/нет): ')
if user_answer == "нет":
    print("Вы молодец!")
    points += 1
elif user_answer == "да":
    print("Неверно.")
else:
    print("Ах вы проказник(ца)!")

count = 1
while True:
    user_answer = input("Вопрос 3. Введите символ операции присваивания: ")
    if user_answer == '=':
        print("Вы молодец!")
        points += 1
        break
    if count == 3:
        if input("Хотите подсказку? (да/нет): ") == "да":
            print("Равенство, но не равенство О_о")
        else:
            print("Как хотите...")
    if count == 5:
        print("Надоело! Учите матчасть!")
        break
    count += 1
print(f"Ваш результат: {points} из 3х.")
