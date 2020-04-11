class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


ivanov = Position('Джон', 'Смит', 'руководитель начальников', 100, 55)
print(f"{type(ivanov)} {ivanov.get_full_name()} - {ivanov.position}, зарабатывает {ivanov.get_total_income()} тугриков")
