"""
Schemas module.

Содержит Pydantic модели приложения.
"""

from pydantic import BaseModel


class Person(BaseModel):
    """
    Полная модель пользователя.

    Attributes:
        id: Уникальный идентификатор пользователя.
        name: Имя пользователя.
        age: Возраст пользователя.
        photo: Ссылка на фотографию.
        password: Пароль пользователя.
    """

    id: int
    name: str
    age: int
    photo: str
    password: str


class CreatePerson(BaseModel):
    """
    Модель создания пользователя.

    Attributes:
        name: Имя пользователя.
        age: Возраст пользователя.
        photo: URL фотографии.
        password: Пароль пользователя.
    """

    name: str
    age: int
    photo: str
    password: str
