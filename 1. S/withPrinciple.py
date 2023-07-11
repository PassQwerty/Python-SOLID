import os

# S - Single Responsibility Principle (Принцип единой ответственности)

# SingleResponsibilityPrinciple
# Принцип единственной обязанности/ответственности
# необходим для того чтобы каждый класс делал только свою работу, а не брал ответственности других классов.

# Пример без принципа:


class Employee:  # Сотрудник
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def calculate_tax(self):  # рассчитать налог
        return self.__salary * 0.2


class EmployeeDetails:  # Детали о сотруднике
    def __init__(self, employee: 'Employee'):
        self.__employee = employee

    def get_details(self):  # получить детали
        return f"Имя: {self.__employee.name}, Налог: {self.__employee.calculate_tax()}"


def main():
    employee = Employee("Василий", 14000)
    print("Налог сотрудника = " + str(employee.calculate_tax()))

    emp_details = EmployeeDetails(employee)
    print(emp_details.get_details())


if __name__ == '__main__':
    os.system('cls||clear')
    main()

# В этом примере мы разделили две ответственности, создав отдельный класс для получения информации о сотруднике.
# Теперь класс Employee отвечает только за расчет налогов, а EmployeeDetails - за предоставление информации о сотруднике.
