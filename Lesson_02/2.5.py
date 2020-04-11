rating = [7, 5, 3, 3, 2]
user_grade = int(input("Введите вашу целую положительную оценку: "))    # Саша, начни уже добавлять проверку!
rating_len = len(rating) - 1

if user_grade <= rating[rating_len]:
    rating.append(user_grade)
elif rating[0] < user_grade:
    rating.insert(0, user_grade)
else:
    for i in range(rating_len):
        if rating[i] >= user_grade > rating[i + 1]:
            rating.insert(i + 1, user_grade)
            break
print(rating)

# написать вариант решения с созданием нового списка
