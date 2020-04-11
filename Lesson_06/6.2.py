class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_amount(self, height):
        kgm = 25
        return print(
            f"Для вашей дороги потребуется {round((self._length * self._width * kgm * height) / 1000, 2)} тонн асфальта")


my_road = Road(5000, 20)
my_road.asphalt_amount(5)
