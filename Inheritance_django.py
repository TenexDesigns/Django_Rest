In Python, inheritance allows you to create new classes (derived or child classes) based on existing classes (base or parent classes).
The derived class inherits the attributes and methods of the base class,
and you can add or modify them as needed. Here are some code samples to demonstrate inheritance in Python:


Basic Inheritance:

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.name)        # Output: Buddy
print(dog.sound())     # Output: Woof!

cat = Cat("Kitty")
print(cat.name)        # Output: Kitty
print(cat.sound())     # Output: Meow!



In this example, the Animal class is the base class, and Dog and Cat are derived classes.
Both derived classes inherit the name attribute and the sound() method from the base class.
Each derived class overrides the sound() method to provide a specific implementation.


Multiple Inheritance:


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        return "Charging"

class ElectricCar(Car, Electric):
    pass

electric_car = ElectricCar("Tesla", 75)
print(electric_car.brand)              # Output: Tesla
print(electric_car.drive())            # Output: Driving a car
print(electric_car.battery_capacity)   # Output: 75
print(electric_car.charge())           # Output: Charging



In this example, we have multiple inheritance. The Vehicle class represents a generic vehicle, 
the Car class inherits from Vehicle and provides a specific implementation of the drive() method. 
The Electric class represents an electric vehicle with a battery, and the ElectricCar class inherits from both Car and Electric.
The ElectricCar class inherits attributes and methods from both parent classes.




Method Overriding:


  class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(4, 5)
print(rectangle.area())     # Output: 20

circle = Circle(3)
print(circle.area())        # Output: 28.26




In this example, the Shape class is a base class with a generic implementation of the area() method.
The Rectangle class and Circle class are derived classes that override the area() method to provide specific implementations 
for calculating the area of a rectangle and a circle, respectively.

Inheritance allows you to reuse and extend existing code, promote code reusability,
and create hierarchical relationships between classes. It is a fundamental concept in 
object-oriented programming that enables you to create more specialized classes based on existing ones.




























































































































...
