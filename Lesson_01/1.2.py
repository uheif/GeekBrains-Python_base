seconds = int(input("Введите время в секундах: "))

remain_seconds = seconds % 60
minutes = seconds // 60
remain_minutes = minutes % 60
hours = minutes // 60

print(f"{hours}:{remain_minutes}:{remain_seconds}")
