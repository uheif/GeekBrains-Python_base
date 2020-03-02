def my_func(x, y):
    # return print(x ** y)

    raised = x
    degree = 2
    while degree <= abs(y):
        raised *= x
        degree += 1
    return print(1 / raised)


my_func(2, -4)
