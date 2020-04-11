def my_func(a, b, c):
    # my_list = sorted([a, b, c])
    # return my_list[-1] + my_list[-2]

    my_list = [a, b, c]
    my_sum = 0
    for i in range(2):
        """За такое в продакшн наверное пальцы ломают :)"""
        my_sum += my_list.pop(my_list.index(max(my_list)))
    return my_sum


print(my_func(5, 67, 655))
