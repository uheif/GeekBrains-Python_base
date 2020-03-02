def user(**kwargs):
    user_data = kwargs
    for i in user_data:
        print(f"{i}: {user_data[i]}", end=' ')


user(name=input("Имя: ").capitalize(), surname=input("Фамилия: ").capitalize(), birth=input("Дата рождения: "),
     city=input("Город: ").capitalize(), email=input("Email: "), tel=input("Телефон: "))

# Надо бы сделать, чтобы вместо ключей-переменных выводился какой-то приличный текст, но пока красивых идей нет)