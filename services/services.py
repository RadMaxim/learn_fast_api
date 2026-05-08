from data.data import peoples
from fastapi import  HTTPException
from schemas.schemas import CreatePerson


def get_person_id(id: int):
    for people in peoples:
        if int(people.id) == id:
            return people
    raise HTTPException(status_code=404, detail="Не существует пользователя с таким id")
def get_all_people():
    return peoples
def create_person(person:CreatePerson):
    new_person = {
        "id":len(peoples) + 1,
        **person.model_dump()
    }
    peoples.append(new_person)
    return new_person