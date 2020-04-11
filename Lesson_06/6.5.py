class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}-запустючка!")


class Pencil(Stationery):
    def draw(self):
        print(f"Ваш {self.title} успешно запущен с орбиты искусственного спутника земли")


class Handle(Stationery):
    def draw(self):
        print(f"Это первый {self.title}, совершивший беспосадочный перелёт через северный полюс!")


hole_puncher = Stationery("дырокол")
hole_puncher.draw()
new_pen = Pen("ручка")
new_pen.draw()
new_pencil = Pencil("карандаш")
new_pencil.draw()
new_handle = Handle("маркер")
new_handle.draw()
