from abc import ABC, abstractmethod
import os

# I - Interface Segregation Principle
# Принцип разделения интерфейсов
# Клиенты не должны вынужденно зависеть от методов, которыми не пользуются.
# При нарушении этого принципа клиент, использующий некоторый интерфейс со всеми его методами, зависит от методов, которыми не пользуется,
# и поэтому оказывается восприимчив к изменениям в этих методах.
# В итоге мы приходим к жесткой зависимости между различными частями интерфейса, которые могут быть не связаны при его реализации.


class IAttackWeapon(ABC):
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

    @abstractmethod
    def PerformAttack(self):
        print(f"{self.name}: Perform Attack")


class IAlternateAttackWeapon():
    def __init__(self, name):
        self.__name = name
        super().__init__(self.__name)

    @abstractmethod
    def PerformAlternateAttack(self):
        print(f"{self.name}: Perform Alternate Attack")


class IReloadableWeapon():
    def __init__(self, name):
        self.__name = name
        super().__init__(self.__name)

    @abstractmethod
    def Reload(self):
        print(f"{self.__name}: Reload")


class Pistol(IAttackWeapon):
    def __init__(self, name):
        self.__name = name
        super().__init__(self.__name)

    def PerformAttack(self):
        print(f"{self.name}: Perform Attack")


class Knife(IAttackWeapon, IAlternateAttackWeapon):
    def __init__(self, name):
        self.__name = name
        super().__init__(self.__name)

    def PerformAttack(self):
        print(f"{self.name}: Perform Attack")

    def PerformAlternateAttack(self):
        print(f"{self.name}: Perform Alternate Attack")


class Shotgun(IAttackWeapon, IAlternateAttackWeapon, IReloadableWeapon):
    def __init__(self, name):
        self.__name = name
        super().__init__(self.__name)

    def PerformAttack(self):
        print(f"{self.name}: Perform Attack")

    def PerformAlternateAttack(self):
        print(f"{self.name}: Perform Alternate Attack")

    def Reload(self):
        print(f"{self.name}: Reload")


def main():
    pistol = Pistol('Desert Eagle')
    pistol.PerformAttack()

    pistol = Knife('Hunting Knife')
    pistol.PerformAttack()
    pistol.PerformAlternateAttack()

    shotgun = Shotgun('Auto-Shotgun')
    shotgun.PerformAttack()
    shotgun.PerformAlternateAttack()
    shotgun.Reload()


if __name__ == '__main__':
    os.system('cls||clear')
    main()
