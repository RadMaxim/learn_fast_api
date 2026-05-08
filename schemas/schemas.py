from pydantic import BaseModel


class Person(BaseModel):
    """
    Модель для get - запроса
    """

    id: int
    name: str
    age: int
    photo: str
    password: str


class CreatePerson(BaseModel):
    """
    Модель для post - запроса, создания нового пользователя
    """

    name: str
    age: int
    photo: str
    password: str
