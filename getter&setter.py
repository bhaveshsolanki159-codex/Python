class Fruit:
    def __init__(self, name):
        self._name = name
    
    @property
    def fruit_name(self):
        print(f"{self._name} was accessed")
        return self._name
    
    @fruit_name.setter
    def fruit_name(self, value):
        print(f"{value} was set")
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print(f"{self._name} was deleted")
        del self._name

if __name__ == "__main__":
    Fruit1 = Fruit("Apple")
    print(Fruit1.fruit_name)

    Fruit1.fruit_name = "Mango"
    del Fruit1.fruit_name
    # print(Fruit1.fruit_name)

    