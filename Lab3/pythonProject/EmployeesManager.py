from Employee import Employee


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def addEmployees(self):
        print('Podaj dane pracownika')
        name = input('Podaj imię: ')
        surname = input('Podaj nazwisko: ')
        age = input('Podaj wiek: ')
        salary = input('Podaj wynagrodzenie: ')
        self.employees.append(Employee(name, surname, age, salary))

    def viewEmployees(self):
        if len(self.employees) == 0:
            print("\nbrak pracowników w bazie")
            return
        else:
            for emp in self.employees:
                print(emp)

    def removeEmployees(self, ageFrom, ageTo):
        for emp in self.employees:
            if ageFrom <= emp.age <= ageTo:
                print(f"\tUsunięto pracownika: {emp.name}")
                self.employees.remove(emp)

    def findEmployees(self, name, surname):
        for emp in self.employees:
            if emp.name == name and emp.surname == surname:
                return emp
            return None

    def updateEmployeeSalary(self, name, surname, salary):
        emp = self.findEmployees(name, surname)
        if emp is None:
            print("Błąd: Nie znaleziono pracownika w bazie")
        else:
            emp.salary = salary