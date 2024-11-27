class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def getInfo(self):
        return (f"Pracownik: {self.name} \t"
                f" {self.surname} \t"
                f"Wiek:  {self.age} \t"
                f"Wynagrodzenie: {self.salary}")
