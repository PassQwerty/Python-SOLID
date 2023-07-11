import os

# O - Open/Closed Principle (Принцип открытости / закрытости)

# Принцип открытости/закрытости
# Программные сущности должны быть открытыми для расширения, но закрытыми для модификации.

# Пример c принципом:


class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def start(self):
        print(f"{self.__make} {self.__model} включена.")

    def stop(self):
        print(f"{self.__make} {self.__model} отключена.")

    # Геттеры
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Сеттеры
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.__battery_level = 100

    def charge(self):
        print(f"Зарядка {self.get_make()} {self.get_model()}...")

    def check_charging(self):
        print(f"Текущий заряд {self.get_model()}: {self.__battery_level}%")

    # Геттер новой версии python
    @property
    def battery_level(self):
        return self.__battery_level

    # Сеттер новой версии python
    @battery_level.setter
    def battery_level(self, battery_level):
        if 0 <= battery_level <= 100:
            self.__battery_level = battery_level
        else:
            raise ValueError("Некорректная установка заряда батареи!!")


def main():
    car = Car("Toyota", "Corolla", 2021)
    car.start()
    car.stop()

    electric_car = ElectricCar("Tesla", "Model S", 2021)
    electric_car.start()
    electric_car.charge()
    electric_car.battery_level = 80
    electric_car.check_charging()
    electric_car.stop()


if __name__ == '__main__':
    os.system('cls||clear')
    main()

# Теперь можно создавать модификацию класса машина
