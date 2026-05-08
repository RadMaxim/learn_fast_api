from fastapi import HTTPException

from data.data import peoples
from schemas.schemas import CreatePerson, Person


def get_person_id(id: int) -> Person:
    for people in peoples:
        if int(people.id) == id:
            return people
    raise HTTPException(status_code=404, detail="Не существует пользователя с таким id")


def get_all_people() -> list[Person]:
    return peoples


def create_person(person: CreatePerson) -> Person:
    new_person = {"id": len(peoples) + 1, **person.model_dump()}
    peoples.append(new_person)
    return new_person
