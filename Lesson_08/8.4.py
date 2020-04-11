from abc import ABC


class OfficeEq(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.name = f"{brand} {model}"

    def __str__(self):
        return self.name


class Printer(OfficeEq):
    """Привет, я принтер! Я умею распечатывать!"""

    @staticmethod
    def printing():
        print("Бзз! Бзз! Вжжуухх!")


class Scanner(OfficeEq):
    """Привет, я сканер! Я умею сканировать!"""

    @staticmethod
    def scanning():
        print("Жжжжжжжжжж! КхКх!")


class Copier(Printer, Scanner):
    """Привет, я ксерокс! Я умею сканировать и распечатывать!"""


class OfficeEqStorage:

    def __init__(self):
        self.departments = ["панды", "носухи", "котики"]  # сделать input()
        self.departments_transfer = {}
        self.printer_section = {}
        self.scanner_section = {}
        self.copier_section = {}

    def section_choose(self, item):
        if type(item) is Printer:
            section = self.printer_section
        elif type(item) is Scanner:
            section = self.scanner_section
        elif type(item) is Copier:
            section = self.copier_section
        return section    # интерпретатор хочет, чтобы это было глобальной переменной, зачем - непонятно...

    @staticmethod
    def amount_val(item, direction):
        while True:
            amount = input(f"сколько {item} {direction}?: ")
            if amount.isdigit():
                break
            print("Введите целое положительное число")
        return int(amount)

    def getting(self, item):
        section = self.section_choose(item)
        amount = self.amount_val(item, "принять на склад")
        if item.name not in section:
            section[item.name] = amount    # __str__ в таких случая не срабатывает, хорошо бы разобраться
        else:
            section[item.name] += amount
        print(f"получен {item} в количестве {amount} шт.")

    def transfer(self, item):
        section = self.section_choose(item)
        if item.name in section and section[item.name] > 0:
            in_stock = section[item.name]
            amount = self.amount_val(item, "передать со склада")
            departament = input(f"в какой отдел? ({' / '.join(self.departments)}): ").lower()  # нужна валидация
            if amount > in_stock:
                print(f"На складе не хватает {amount - in_stock} ед. техники, будет передано {in_stock} ед.")
                section[item.name] = 0
                if item.name not in self.departments_transfer:
                    self.departments_transfer[item.name] = {departament: in_stock}
                else:
                    self.departments_transfer[item.name][departament] += in_stock
                print(f"{item} передан в отдел {departament} в количестве {in_stock} шт.")
            else:
                section[item.name] -= amount
                if item.name not in self.departments_transfer:
                    self.departments_transfer[item.name] = {departament: amount}
                else:
                    self.departments_transfer[item.name][departament] += amount
                print(f"{item} передан в отдел {departament} в количестве {amount} шт.")
        else:
            print(f"{item} нету. Зайдите на недельке")


new_copier = Copier("cool copier", "cop1")
new_copier.scanning()
new_copier.printing()
my_storage = OfficeEqStorage()
new_printer = Printer("epson", "super print")
new_printer2 = Printer("canon", "omg42")
my_storage.getting(new_printer)
my_storage.getting(new_printer2)
my_storage.transfer(new_printer)
my_storage.transfer(new_printer2)
my_storage.transfer(new_copier)
print(my_storage.printer_section)
print(my_storage.departments_transfer)
