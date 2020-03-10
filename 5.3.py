salary_sum = 0
people = 0
salary_min = 20000

with open("5.3.txt") as inf:
    for line in inf:
        name = line.split()[0]
        salary = float(line.split()[-1])
        salary_sum += salary
        people += 1
        if salary < salary_min:
            print(name)
print(f"Средняя зарплата по больнице: {round(salary_sum / people, 2)}")
