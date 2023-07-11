import os

# L - Liskov Substitution Principle (Принцип подстановки Лисков)
#
# Должна быть возможность вместо базового типа подставить любой его подтип.
# Фактически принцип подстановки Лисков помогает четче сформулировать иерархию классов,
# определить функционал для базовых и производных классов и избежать возможных проблем при применении полиморфизма.


class ICanAttack():
    def __init__(self, name):
        self.name = name

    def Attack(self, name):
        print(f"{self.name} Attacking the {name}")


class ICanMove():
    def __init__(self, name):
        self.name = name

    def Move(self):
        print(f"{self.name} is moving")


class ICanHeal():
    def __init__(self, name):
        self.name = name

    def Heal(self):
        print(f"The {self.name} started to be treated")


class ICanBuilding():
    def __init__(self, name):
        self.name = name

    def Building(self):
        print(f"The {self.name} player builds a house")


class Player(ICanMove, ICanAttack):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, setName):
        if setName is not '':
            self.__name = setName
            print(f"The {self.__name} name has been changed to {setName}")
        else:
            raise ValueError("The value must not be empty")


def main():
    player = Player('Humanoid')
    player.Move()

    player2 = Player('Player2')
    player2.Move()

    player2.name = 'Ork'
    player.Attack(player2.name)


if __name__ == '__main__':
    os.system('cls||clear')
    main()
