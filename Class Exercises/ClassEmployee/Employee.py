class Employee:

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def display(self):
        print(f'Name: {self.name} \nSalary: {self.salary}R$')


class SalaryIncrease(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def increase(self, increase_percentage):
        self.salary += (self.salary * increase_percentage) / 100

    def display(self):
        print(f'Name: {self.name} \nIncreased salary: {self.salary}')


employee1 = Employee('Inacio', 2500)
employee1.display()
print()
employee1 = SalaryIncrease(employee1.name, employee1.salary)
employee1.increase(10)
employee1.display()
