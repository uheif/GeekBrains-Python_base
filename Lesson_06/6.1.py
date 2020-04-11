from time import sleep
from itertools import cycle

# class Color:
#     Red = '\033[91m'
#     Green = '\033[92m'
#     Yellow = '\033[93m'
#     END = '\033[0m'
# не успеваю)))

class TrafficLight:
    def __init__(self, color):
        self._color = color
        '''Полагаю, что color должен быть связан с методом running, (начать цикл с этого аргумента?)
        но из условия задачи это неочевидно и на все задания у меня часа полтора, поэтому реализовать это я, видимо, не успею :)'''

    def running(self):
        uptime = 0
        pause = None
        colors = ["Red", "Yellow", "Green", "Yellow"]
        for el in cycle(colors):
            if uptime > 30:
                break
            print(el)
            if el == "Red" or el == "Green":
                pause = 7
            else:
                pause = 2
            sleep(pause)
            uptime += pause


my_light = TrafficLight("Black")
print(my_light._color)
sleep(1)
my_light.running()
