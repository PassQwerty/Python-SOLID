import os

# S - Single Responsibility Principle (Принцип единной ответственности)

# SingleResponsibilityPrinciple
# Принцип единственной обязанности/ответственности
# необходим для того чтобы каждый класс делал только свою работу, а не брал ответственности других классов.

# Пример без принципа:


class Employee:  # Сотрудник
    def __init__(self, name, salary):
        self.__name = name  # инкапсуляция
        self.__salary = salary

    def calculate_tax(self):  # рассчитать налог
        return self.__salary * 0.2

    def get_details(self):  # получить детали
        return f"Имя: {self.__name}, Налог: {self.__salary}"


def main():
    employee = Employee("Василий", 14000)
    print("Налог сотрудника = " + str(employee.calculate_tax()))
    print(employee.get_details())


if __name__ == '__main__':
    os.system('cls||clear')
    main()
