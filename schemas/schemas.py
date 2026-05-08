from pydantic import BaseModel


class Person(BaseModel):
    id: int
    name: str
    age: int
    photo: str
    password: str

class CreatePerson(BaseModel):
    name: str
    age: int
    photo: str
    password: str
