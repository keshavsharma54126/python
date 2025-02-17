# basic types in python

import re
import math
brand = "Toyota"
model_year = 1999
mileage = 123.3251
is_insured = True
cars = ["Toyota", "Honda", "Ford"]
car_info = {
    "brand": "Toyota",
    "year": 2022,
    "color": "red"
}

# strings in python
car_info = "The car is" + " " + "30 years old"
print(car_info)

car_age = 40
more_car_info = "The car is " + str(car_age) + "years old"
print(more_car_info)

even_more_car_info = f"The car is {car_age} years old"
print(even_more_car_info)

# working with numbers
x = 5+3
y = 10-7
z = 4*2
div = 10/2
floor_div = 10//2
exp = 2**4
mod = 10 % 3

# working with lists
print(cars[1])
print(cars[0])
cars.append("Chevrolet")
cars.remove("Honda")
print(cars)

# working with dictionary
car_info = {
    "brand": "Honda",
    "year": 2022,
    "color": "red"
}

print(car_info)
print(car_info["color"])
car_info["color"] = "pink"
print(car_info["color"])


# variables name use snake case in pythong as convention
max_speed = 1000
max_speed = 100
print(max_speed)

# constant convention is to use allcaps
MAX_SPEED = 1000

# functions in python


def start_cars(car1="Chevrolet", car2="Chevrolet"):
    print(f"Attempting to start {car1} ")
    print(f"Attempting to start {car2} ")


start_cars("Toyota", "Honda")
start_cars()


def start_car():
    return f"Attempting to return"


result = start_car()
print(result)


def start_many_cars():
    pass


# control flow
speed = 67
if speed > 55:
    print("you are driving above the speed limit")
elif speed == 67:
    print("you are driving at the speed limit")
else:
    print("you are driving below speed limti")

# ternary for controlflow
speed = 10
status = "Above limit" if speed > 55 else "within limit"
print(status)

# comparison operators
speed = 80
print(speed == 80)
print(speed != 66)
print(speed > 55)
print(speed < 44)
print(speed >= 34)
print(speed <= 243)

# for loops
for car in cars:
    print("I love", car)

for i in range(10):
    print(i)

cars_with_love = ["I love" + car for car in cars]
print(cars_with_love)

# while loops
fuel = 9
while fuel > 0:
    print("Driving...")
    fuel = fuel-1

while True:
    command = input("Enter 'stop' to stop the car: ")
    if command == "stop":
        print("Car stopped")
        break
    else:
        print("car is still running ")

# set in python (only takes unique values)
car_brands = {"Toyota", "Honda", "Ford", "Toyota"}
print(car_brands)

# tuples (these are immutables )
my_tuple = ("Toyota", "Honda", "Ford")
print(my_tuple)

# my_tuple[0] = "Honda"
print(my_tuple)

# you can assign explicit types also in python
year: int = 1123


def get_car_info(brand: str, year: int) -> str:
    return f"A {brand} manufactured in {year}"


result = get_car_info("toyota", 2009)
print(result)


# oop in python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"{self.brand} from {self.year} is starting")


new_car = Car("Toyota", 2003)
print(new_car)
print(new_car.brand)
print(new_car.year)
new_car.start()


if __name__ == "__main__":
    print("Running directly as a script")
else:
    print("Imported as a module")

# exceptions
try:
    x = 10/0
    print(x)
except Exception as e:
    print("Cannot divid by zero", e)

# you can also import pacakges
tire_diameter = 23
circumference = math.pi * tire_diameter
print(circumference)


text = "My car is a toyota. My friend drives a Honda"
pattern = r"(Toyota)"

match = re.search(pattern, text)
if match:
    print("Found", match.group())
