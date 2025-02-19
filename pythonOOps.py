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
