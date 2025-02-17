class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"Employee name is {self.name}"
    
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    def __call__(self):
        print("Calling",self.name)

e = Employee("Harry")
print(str(e))
print(repr(e))
print(len(e))
e()