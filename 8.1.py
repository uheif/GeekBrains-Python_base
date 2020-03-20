class Date:
    date_str = None

    def __init__(self, date_str):
        self.date_str = date_str
        Date.date_str = self.date_str

    @classmethod    # решительно непонятно зачем так делать...
    def date_int(cls):
        date_int_lst = [int(el) for el in Date.date_str.split('-') if el.isdigit()]
        Date.day = date_int_lst[0]
        Date.month = date_int_lst[1]
        Date.year = date_int_lst[2]
        return Date.date_check()

    @staticmethod
    # сначала случайно сделал сеттер, не выкидвать же :) (в голове каша...)
    def date_check():
        if Date.year > 2020:
            Date.year = 2020
            print("эко вы махнули с годом!")
        elif Date.year < 1920:
            Date.year = 1920
            print("эко вы махнули с годом!")

        if Date.month > 12:
            Date.month = 12
            print("эко вы махнули с месяцем!")

        if Date.month in (1, 3, 5, 7, 8, 10, 12) and Date.day > 30:
            date.day = 30
        elif Date.month == 2 and (Date.year % 4 != 0 or (Date.year % 100 == 0 and Date.year % 400 != 0)):
            if Date.day > 28:
                Date.day = 28
                print("февраль же!")
        # для високосного года:
        elif Date.month == 2 and Date.day > 29:
            Date.day = 29
            print("февраль же! да ещё и год високосный!")
        elif Date.day > 31:
            Date.day = 31
            print("эко вы махнули с днём!")
        return Date.day, Date.month, Date.year


date = Date("-32-02-2020")
print(date.date_str)
print(Date.date_int())
