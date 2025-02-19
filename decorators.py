# decorators are a thing in python mainly used for the following things
# logging,Authentication,performance measurement,code modification on runtime

# type of decorators
# 1) function decorators to modify the behaviour of functions

def my_decorator(func):
    def wrapper():
        print("something before the function")
        func()
        print("somethingg after the function")
    return wrapper


@my_decorator
def say_hello():
    print("hello keshav")


say_hello()


# class decorators
def add_extra_method(cls):
    cls.new_method = lambda self: "New Method Added"
    return cls


@add_extra_method
class Myclass:
    def original_method(self):
        return "original method"


obj = Myclass()
print(obj.original_method())
print(obj.new_method())


# method decorators
# python has three inbuild method decorators
# @staticmethod
# @classmethod
# @property

class Myclass:
    class_var = "I am a class variable"

    def __init__(self, name):
        self._name = name

    @staticmethod
    def static_method():
        print("This is a static method")

    @classmethod
    def show_class_var(cls):
        return cls.class_var

    @property
    def name(self):
        return self._name


Myclass.static_method()

print(Myclass.show_class_var())
p = Myclass("Keshav")
print(p.name)
