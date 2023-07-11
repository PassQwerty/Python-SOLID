import os

# O - Open/Closed Principle (Принцип открытости / закрытости)

# Принцип открытости/закрытости
# Программные сущности должны быть открытыми для расширения, но закрытыми для модификации.

# Пример без принципа:


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


def main():
    car = Car("Toyota", "Corolla", 2021)
    car.start()
    car.stop()

    car = Car("Tesla", "Model S", 1966)  # нужен мод
    car.start()
    car.stop()


if __name__ == '__main__':
    os.system('cls||clear')
    main()

# для того чтобы сделать новую машину нам необходимо вносить изменения в текущий класс
