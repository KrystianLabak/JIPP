from EmployeesManager import *
from pythonProject.utility import inputValue


class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeeManager()

    def printMenu(self):
        print("\nZarządzanie pracownikami\n")
        message = [
            '1. Dodaj pracownika',
            '2. Wyświetl liste pracowników',
            '3. Usuń pracownika',
            '4. Zaaktualizuj wynagrodzenie',
            '5. Wyjście'
        ]

        print('\n'.join(message))
        msg = f"Wybierz opcje (1 - {len(message)}): "
        return inputValue(msg,1,len(message))

    def run(self):
        while True:
            choice = self.printMenu()

            if choice == 1:
                self.EmployeesManager.addEmployees()
            elif choice == 2:
                self.EmployeesManager.viewEmployees()
            elif choice == 3:
                ageFrom = int(input("Podaj początek przedziału wieku pracownika"))
                ageTo = int(input("Podaj koniec przedziału wieku pracownika"))
                self.EmployeesManager.removeEmployees(ageFrom, ageTo)
            elif choice == 4:
                name = input("Podaj imię: ")
                surname = input("Podaj nazwisko: ")
                salary = int(input("Podaj nowe wynagrodzenie: "))
                self.EmployeesManager.updateEmployeeSalary(name, surname, salary)
            else:
                break