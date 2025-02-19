# magic methods or dunder(double underscore methods) are very important part of python
# oops magic methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 23)
print(p.name)

# __new__ is used for singleton patter


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

# string representation
1. Understanding Magic Methods
Magic methods define behavior for built-in Python operations.
They are not called explicitly
Python calls them automatically.
They customize object behavior, such as:
Initialization(__init__)
String representation(__str__, __repr__)
Arithmetic operations(__add__, __sub__)
Comparison(__eq__, __lt__, __gt__)
Length(__len__)
Indexing(__getitem__, __setitem__)
Context management(__enter__, __exit__)
2. Categories of Magic Methods
Magic methods can be grouped into different categories based on their purpose.

2.1. Object Construction and Initialization
These methods control how objects are created and initialized.

Magic Method	Purpose
__new__(cls, ...)	Creates a new instance before initialization.
__init__(self, ...)	Initializes an instance after creation.
__del__(self)	Called when an object is deleted.
Example: __init__(Constructor)
python
Copy
Edit


class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age


p = Person("Alice", 25)  # __init__ is automatically called
print(p.name)  # Output: Alice
Example: __new__(Used for Singleton Pattern)
python
Copy
Edit


class Singleton:
    _instance = None

    def __new__(cls):  # Controls object creation
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True (same instance)
2.2. String Representation
These methods define how objects are represented as strings.

Magic Method	Purpose
__str__()	Defines a human-readable string representation(for print()).
__repr__()	Defines an official representation for debugging(repr()).
Example: __str__ vs __repr__
python
Copy
Edit


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # User-friendly output
        return f"{self.name}, {self.age} years old"

    def __repr__(self):  # Debugging representation
        return f"Person('{self.name}', {self.age})"


p = Person("Alice", 25)
print(str(p))   # Output: Alice, 25 years old
print(repr(p))  # Output: Person('Alice', 25)
2.3. Arithmetic Operators
These methods define how objects behave with arithmetic operations.

Magic Method	Purpose
__add__(self, other)	Implements self + other.
__sub__(self, other)	Implements self - other.
__mul__(self, other)	Implements self * other.
__truediv__(self, other)	Implements self / other.
__floordiv__(self, other)	Implements self // other.
__mod__(self, other)	Implements self % other.
Example: Overloading + Operator
python
Copy
Edit


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Defines behavior for +
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__
print(v3.x, v3.y)  # Output: 6, 8
2.4. Comparison Operators
These methods define how objects are compared.

Magic Method	Purpose
__eq__(self, other)	Implements self == other.
__ne__(self, other)	Implements self != other.
__lt__(self, other)	Implements self < other.
__le__(self, other)	Implements self <= other.
__gt__(self, other)	Implements self > other.
__ge__(self, other)	Implements self >= other.
Example: Overloading == and <
python
Copy
Edit


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):  # Defines behavior for ==
        return self.age == other.age

    def __lt__(self, other):  # Defines behavior for <
        return self.age < other.age


p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1 == p2)  # False (calls __eq__)
print(p1 < p2)   # True (calls __lt__)
2.5. Length and Indexing
These methods define behavior for objects that behave like sequences.

Magic Method	Purpose
__len__(self)	Implements len(self).
__getitem__(self, key)	Implements self[key].
__setitem__(self, key, value)	Implements self[key] = value.
__delitem__(self, key)	Implements del self[key].
Example: Custom List-Like Class
python
Copy
Edit


class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):  # Implements len()
        return len(self.items)

    def __getitem__(self, index):  # Implements indexing
        return self.items[index]


my_list = CustomList([10, 20, 30])
print(len(my_list))  # Output: 3 (calls __len__)
print(my_list[1])  # Output: 20 (calls __getitem__)
2.6. Context Managers(with Statement)
These methods are used to define custom behavior when using the with statement.

Magic Method	Purpose
__enter__(self)	Defines what happens when entering a with block.
__exit__(self, exc_type, exc_value, traceback)	Defines cleanup when exiting a with block.
Example: Custom Context Manager
python
Copy
Edit


class FileManager:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):  # Entering the with block
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):  # Exiting the block
        self.file.close()


with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")  # __enter__ is called here
# __exit__ is automatically called at the end of the block
Conclusion
Magic methods allow Python classes to interact with built-in operations and standard behaviors seamlessly. By overriding these methods, you can make your classes behave like built-in types, allowing greater flexibility and intuitive usage.

Would you like a real-world project demonstrating magic methods? 🚀
