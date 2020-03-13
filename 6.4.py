class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Go!")

    def stop(self):
        print("Stop!")

    def turn(self, is_left, is_right=True):
        print("Go left!") if is_left else print("Go right!")

    def show_speed(self, cur_speed):
        print(f"Current speed is {cur_speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, cur_speed):
        if cur_speed > 60:
            print(f"Current speed is {cur_speed}. Get a fine!")
        else:
            print(f"Current speed is {cur_speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, cur_speed):
        if cur_speed > 40:
            print(f"Current speed is {cur_speed}. Get a fine!")
        else:
            print(f"Current speed is {cur_speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

town_car = TownCar(230, "yellow", "volvo c30")
sport_car = SportCar(420, "blue", "bugatti veyron")
work_car = WorkCar(90, "blue", "zil 130")
police_car = PoliceCar(220, "police_color", "ford crown victoria")

print(town_car.name)
town_car.go()
town_car.turn(1)
town_car.show_speed(62)
town_car.stop()

print(police_car.name, police_car.is_police)

sport_car.show_speed(250)

print(work_car.color)
