# Multiple Inheritance

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

print("\n\n")

# multilevel inheritance

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def display(self):
        print(f"Name: {self.name}, Species: {self.species}")
class Dog(Animal):
    def __init__(self,name,bread):
        Animal.__init__(self,name,species = "Dog")
        self.bread = bread
    def display(self):
        Animal.display(self)
        print(f"Bread: {self.bread}")
class pomeloen(Dog):
    def __init__(self, name):
        super().__init__(name, bread = "Pomeloen")

    def display(self):
        Dog.display(self)
        print(f"Name: {self.name}, Bread: {self.bread}, species: {self.species}")

p = pomeloen("Tommy")
p.display()
print(pomeloen.__mro__)







# print(Manager.__mro__)# method resolution order in tuple
# print(Manager.mro())# method resolution order in list
# print(Manager.__bases__)# base classes in tuple
# print(Manager.__subclasses__())# subclasses in list
# print(Manager.__base__)# base class
# print(Manager.__name__)# class name
# print(Manager.__module__)# module name
# print(Manager.__dict__)# dictionary of class
# print(Manager.__doc__)# documentation of class