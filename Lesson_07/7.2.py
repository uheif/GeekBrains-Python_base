from abc import ABC, abstractmethod


class Clothes(ABC):
    cloth = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def exp(self):
        pass


class Coat(Clothes):
    def __init__(self, V, name="пальтишко"):
        super().__init__(name)
        self.V = V
        Clothes.cloth += self.exp
        Clothes.cloth = round(Clothes.cloth, 2)

    @property
    def exp(self):
        return round(self.V / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, H, name="костюмчик"):
        Clothes.__init__(self, name)
        self.H = H
        Clothes.cloth += self.exp
        Clothes.cloth = round(Clothes.cloth, 2)

    @property
    def exp(self):
        return 2 * self.H + 0.3


my_coat = Coat(46)
print(my_coat.name, my_coat.V)
print(my_coat.exp)
print(Suit(1.73).exp)
print(Clothes.cloth)
my_coat_2 = Coat(52, name="пальтишко 2")
print(my_coat_2.name)
new_suit = Suit(1.80)
print(new_suit.name)
print(Clothes.cloth)

