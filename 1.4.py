num = int(input("Введите целое положительное число: "))

div = 10
max_digit = 0
while num != 0:
    last_digit = num % div
    if last_digit > max_digit:
        max_digit = last_digit
    num //= div
#print(max_digit)