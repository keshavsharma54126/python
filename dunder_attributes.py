# Common __attr__ Attributes in Python

# 1. __dict__ – Object Attribute Dictionary
# Stores all instance attributes in a dictionary.
# Useful for dynamically accessing attributes.
# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.__dict__)
# Output: {'name': 'Alice', 'age': 25}

# 2. __name__ – Name of a Module or Function
# Stores the name of a function, class, or module.
# Example:
def hello():
    pass

print(hello.__name__)  # Output: hello
print(__name__)  # If run directly, Output: "__main__"

# 3. __class__ – Class of an Object
# Returns the class/type of an object.
# Example:
class Dog:
    pass

d = Dog()
print(d.__class__)  # Output: <class '__main__.Dog'>

# 4. __doc__ – Documentation String
# Stores the docstring of a class, function, or module.
# Example:
class Animal:
    """This is an Animal class."""
    pass

print(Animal.__doc__)  # Output: "This is an Animal class."

# 5. __module__ – Module Name of a Class
# Shows where a class is defined.
# Example:
class Cat:
    pass

print(Cat.__module__)  # Output: "__main__"

# 6. __bases__ – Parent Classes of a Class
# Returns a tuple of base classes (used in inheritance).
# Example:
class A:
    pass

class B(A):
    pass

print(B.__bases__)  # Output: (<class '__main__.A'>,)

# 7. __mro__ – Method Resolution Order
# Shows the order in which Python looks for methods in a class hierarchy.
# Example:
class X: pass
class Y(X): pass
class Z(Y): pass

print(Z.__mro__)
# Output: (<class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class 'object'>)

# 8. __annotations__ – Type Annotations
# Stores type hints for function arguments and return values.
# Example:
def add(x: int, y: int) -> int:
    return x + y

print(add.__annotations__)
# Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}