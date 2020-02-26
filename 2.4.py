list_from_user_str = input("Введите нескольких слов, разделённых пробелами: ").split()

count = 1    # без range() для разнообразия, зато тернарный оператор!

for i in list_from_user_str:
    print(count, i) if len(i) <= 10 else print(count, i[:10])
    count += 1
