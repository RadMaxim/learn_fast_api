"""
Schemas module.

Содержит Pydantic модели приложения.
"""

from pydantic import BaseModel, ConfigDict, Field


class CreatePerson(BaseModel):
    """
    Модель создания пользователя.

    Attributes:
        name: Имя пользователя.
        age: Возраст пользователя.
        photo: URL фотографии.
        password: Пароль пользователя.
    """

    name: str = Field(max_length=30)
    age: int = Field(le=120, ge=0)
    photo: str | None
    password: str = Field(min_length=4)
    model_config = ConfigDict(extra="forbid")


class Person(CreatePerson):
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


class UserLoginSchema(BaseModel):
    username: str
    password: str
