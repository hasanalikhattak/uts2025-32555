class Animal:
    def __init__(self, species, position):
        self.species = species
        self.position = position

    def walk(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def __init__(self, position=0):
        super().__init__("Dog", position)

    def walk(self):
        self.position += 4
        return (str)(self.position)
    
class Cat(Animal):
    def __init__(self, position=0):
        super().__init__("Cat", position)

    def walk(self):
        self.position += 2
        return (str)(self.position)

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    for _ in range(5):
        print(f"{dog.species} position: {dog.walk()}")
        print(f"{cat.species} position: {cat.walk()}")