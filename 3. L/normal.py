import os


# L - Liskov Substitution Principle (Принцип подстановки Лисков)
#
# Должна быть возможность вместо базового типа подставить любой его подтип.
# Фактически принцип подстановки Лисков помогает четче сформулировать иерархию классов,
# определить функционал для базовых и производных классов и избежать возможных проблем при применении полиморфизма.


class Player():
    def __init__(self, name):
        self.__name = name
        print(f'Creating a {self.name}')

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

    def Move(self):
        print(f"{self.name} is moving")

    def Heal(self):
        print(f"The {self.name} started to be treated")

    def Building(self):
        pass

    def Attack(self, name):
        print(f"{self.name} Attacking the {name}")


def main():
    player = Player('Humanoid')
    player2 = Player('Player2')
    player2.name = 'Ork'

    player.Move()
    player.Heal()
    player.Building()
    player.Attack(player2.name)


if __name__ == '__main__':
    os.system('cls||clear')
    main()
