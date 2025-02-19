from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(sefl):
        return "Generic Animal Sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return "Woof!"

    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers")

print(my_dog.name)
print(my_dog.breed)
print(my_dog.bark())
print(my_dog.speak())

print(my_cat.name)
print(my_cat.speak())


class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def save_to_database(self):
        print(f"Order saved to database: {self.items}")

    def send_confirmation_email(self, email):
        print(f"confirmation email send to: {email}")

# the above class violates the SRP(single responsiblity principle )


class OrderCorrected:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = sum(item.price for item in self.items)


class OrderDatabase:
    def save(self, order):
        print(f"order saved to database: {order.items}")


class OrderNotifier:
    def send_configuration(self, order, email):
        print(f"confirmation email send to  : {email}")


order = Order([{"name": "Item 1", "price": 10},
              {"name": "Item2", "price": 40}])
db = OrderDatabase()
notifier = OrderNotifier()

db.save(order)
notifier.send_configuration(order, "user@exmaple.com")

# O - Open/Closed Principle (OCP): "Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification." This means you should be able to add new functionality without modifying existing code.  This is often achieved through inheritance and interfaces (or abstract base classes in Python).


class Shape:
    def __init__(self, type):
        self.type = type

    def draw(self):
        if self.type == "rectangle":
            print("Drawing a rectangle")
        elif self.type == "circle":
            print("Drwaing a circle")

# the above class violates the Open/closed principle of the solid principles
# open/closed principles says that your oops entitites should be open to extension but not for modification
# below is the correct approach


class ShapeCorrected:
    def draw(self):
        pass


class Rectangle(ShapeCorrected):
    def draw(self):
        print("Drawing a rectangle")


class Circle(ShapeCorrected):
    def draw(self):
        print("Drawing a circle")


def render_shapes(shapes):
    for shape in shapes:
        shape.draw()


shapes = [Rectangle(), Circle()]
render_shapes(shapes)

# L - Liskov Substitution Principle (LSP): "Objects of a superclass should be replaceable with objects of its subclasses without breaking the application."  This means that if you have a function that works with objects of a base class, it should also work correctly with objects of any derived class.  Subclasses should extend the base class behavior without changing its fundamental contract.


class Rectangle:
    def __init__(self):
        self._width = 0
        self._height = 0

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_area(self):
        return self._width * self._height


class Square(Rectangle):  # Square IS-A Rectangle (mathematically), but...
    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)  # Enforce square property

    def set_height(self, height):
        super().set_width(height)  # Enforce square property
        super().set_height(height)


# Function expecting Rectangle behavior
def increase_rectangle_width_by_10(rect):
    original_width = rect.get_width()
    rect.set_width(original_width + 10)
    return rect.get_area() > original_width * rect.get_height()  # Expect area to increase


# Usage
rect = Rectangle()
rect.set_width(5)
rect.set_height(10)
print(increase_rectangle_width_by_10(rect))  # Output: True (as expected)

square = Square()
square.set_width(5)
print(increase_rectangle_width_by_10(square))  # Output: False (LSP violation!)

# In this example, mathematically, a square is a rectangle. However, in terms of behavior, the Square class violates LSP. The increase_rectangle_width_by_10 function expects that increasing the width of a rectangle will always increase its area. But when we pass a Square object, setting the width also sets the height, so the area might not increase as expected (or at least not in the way a rectangle's area would).  Square is not truly substitutable for Rectangle in all contexts.

# Solution (LSP Applied - Rethinking the Hierarchy):

# In this case, a better approach might be to rethink the class hierarchy.  Perhaps Square and Rectangle should not have an inheritance relationship if their behaviors are not truly substitutable in all contexts.  Alternatively, if they must be related, the set_width and set_height methods in Square should be carefully designed to maintain LSP, or a different abstraction might be needed.  For example, you could have a more general Shape class and then Rectangle and Square as separate specializations without a direct inheritance relationship between them if their behaviors diverge significantly.  The key is to ensure that subclasses truly behave as expected by the base class in all relevant scenarios.


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(sleep):
        pass


class HumanWorker(Worker):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")

    def sleep(self):
        print("Human worker sleeping")


class RobotWorker(Worker):
    def work(self):
        print("robot worker working")

    def eat(self):
        print("robot worker eating")

    def sleep(self):
        print("robot worker sleeping")


# The Worker interface is too broad. RobotWorker is forced to implement eat and sleep methods, even though robots don't perform these actions. This violates ISP.

# Solution (ISP Applied):


class Workable(ABC):  # Smaller, specific interfaces
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass


class HumanWorker(Workable, Eatable, Sleepable):  # Implements all relevant interfaces
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")

    def sleep(self):
        print("Human worker sleeping")


class RobotWorker(Workable):  # Only implements the Workable interface
    def work(self):
        print("Robot worker working")

# Dependeny Inversion principle


class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

    def turn_off(self):
        print("LightBulb : Bulb turned off")


class Switch:
    def __init__(self):
        self.bulb = LightBulb()

    def operate(self, on):
        if on:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()


switch = Switch()
switch.operate(True)

# in the above example a highlevel module is using a lowlevel module which should not be the case because it
# violtates the dip principle
# below is the solution of the above problem


class BulbCorrected(ABC):  # Abstraction (interface/abstract class)
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulbCorrected(BulbCorrected):  # Concrete implementation
    def turn_on(self):
        print("LightBulb: Bulb turned on")

    def turn_off(self):
        print("LightBulb: Bulb turned off")


class FancyLightBulb(BulbCorrected):  # Another concrete implementation
    def turn_on(self):
        print("FancyLightBulb: Bulb turned on with extra flair!")

    def turn_off(self):
        print("FancyLightBulb: Bulb turned off gently")


class SwitchCorrected:  # High-level module, depends on abstraction (Bulb)
    def __init__(self, bulb: BulbCorrected):  # Dependency injection through constructor
        self.bulb = bulb  # Depends on the Bulb abstraction

    def operate(self, on):
        if on:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()


# Usage
bulb1 = LightBulbCorrected()
bulb2 = FancyLightBulb()

switch1 = SwitchCorrected(bulb1)  # Inject LightBulb dependency
switch2 = SwitchCorrected(bulb2)  # Inject FancyLightBulb dependency

switch1.operate(True)  # Output: LightBulb: Bulb turned on
# Output: FancyLightBulb: Bulb turned on with extra flair!
switch2.operate(True)
