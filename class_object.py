# Create a simple class and object

class car:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def car_info(self):
        return f"{self.brand} {self.model} {self.year}"
    
car_detail = car("Toyota", "Corolla", 2019)
print(car_detail.car_info())


# Problem: Define a class Student with a class variable school_name and instance variables name and age.

class student:
    school_name = "Parul University"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        return f"Student:{self.name}, Age:{self.age}, College:{self.school_name}"

s1 = student("Rahul", 20)
s2 = student("rohit", 21)

print(s1.student_info())
print(s2.student_info())

# Modify Object Attributes

class BankAccount:
    def __init__(self, AC , balance=0):
        self.account_holder = AC
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Account holder: {self.account_holder}", "\n",f"Balance: {self.balance}","\n",f"Amount Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Account holder: {self.account_holder}","\n",f"Balance: {self.balance}","\n",f"Amount Withdrawn: {amount}")

holder = BankAccount("Rahul", 1000)
holder.deposit(500)

# Class vs Instance Variables Experiment

class Employee:
    company = "Google"
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary

    def employee_info(self):
        print(f"Employee Name: {self.name}","\n",f"Employee Salary: {self.salary}","\n",f"Company: {self.company}")


if __name__ == "__main__":
    e1 = Employee("Rahul", 10000)
    e2 = Employee("Rohit", 20000)

    e1.employee_info()
    e2.employee_info()

    e1.company = "Microsoft"
    e1.employee_info()
    e2.employee_info()

    Employee.company = "Amazon"
    e1.employee_info()
    e2.employee_info()