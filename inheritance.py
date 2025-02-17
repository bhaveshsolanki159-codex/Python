class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Company:
    def __init__(self, name, address):
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Address: {self.address}")
class Manager(Employee, Company):
    def __init__(self, name, salary, address):
        Employee.__init__(self, name, salary)
        Company.__init__(self, name, address)

    def display(self):
        Employee.display(self)
        Company.display(self)

m = Manager("John", 50000, "123 Main St")
m.display()
print(Manager.__mro__)