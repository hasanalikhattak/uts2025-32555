class Polygon:
    def __init__(self, sides):
        self.type = type

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Square(Polygon):
    def __init__(self, side_length):
        super().__init__("Square")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
class Shapes:
    def __init__(self):
        self.shapes = []

    def load_shapes(self):
        self.shapes.append(Square(5))
        self.shapes.append(Square(10))
        self.shapes.append(Circle(7))
        self.shapes.append(Circle(10))
        self.shapes.append(Triangle(5, 3))
        self.shapes.append(Triangle(5, 5))

    def show(self):
        for shape in self.shapes:
            print(f"{shape.type} area: {shape.area()}")

if __name__ == "__main__":
    shapes = Shapes()
    shapes.load_shapes()
    shapes.show()