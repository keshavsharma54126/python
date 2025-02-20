from pydantic import BaseModel, Field, validator
from typing import Optional


class Person(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50)
    address: str
    age: int = Field(..., gt=0, lt=120)
    parents_name: Optional[str] = None


p = Person(id=1, name="keshav", address="gzb", age=1)
print(p.age)
data = {"id": 2, "name": "lakshya", "address": "delhi", "age": "19"}
p1 = Person(**data)
print(p1.age)

invalid_data = {"id": 2, "name": "ashutosh",
                "address": "gurugram", "age": "20"}
p2 = Person(**invalid_data)

try:
    p2 = Person(**invalid_data)
    print(f"age of p2 is {p2.age}")
    print(f"p2's parent name is {p2.parents_name}")

except Exception as e:
    print(e)

# nested pydantic models


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    name: str
    age: int
    address: Address


user_data = {
    "name": "Keshav",
    "age": 24,
    "address": {
        "street": "cc-112",
        "city": "delhi",
        "zip_code": "201002"
    }
}

nested_user = User(**user_data)
print(nested_user.address.city)

# aliases in models


class NewUser(BaseModel):
    full_name: str = Field(..., alias="FullName")
    first_name: str
    last_name: str
    email: str
# @property for custom property in a pydantic model

    @property
    def full_func(self):
        return f"{self.first_name} {self.last_name}"

    @validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            return "email is not valid"
        else:
            return "email is valid"


new_user = NewUser(FullName="Keshav Sharma",
                   first_name="Keshav", last_name="Sharma", email="keshav@gmail.com")
print(new_user)
full_name = new_user.full_func
print(full_name)
