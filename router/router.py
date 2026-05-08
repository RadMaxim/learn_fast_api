from fastapi import APIRouter

from schemas.schemas import CreatePerson
from services.services import create_person, get_all_people, get_person_id
from utils.decorators import handle_exceptions, log_return

router = APIRouter(prefix="/peoples", tags=["People"])


@router.get("/root", summary="Main", tags=["Main"])
@log_return
@handle_exceptions
def root():
    return "Hello world"


@router.get("/{id}", summary="Получить конкретного человека по id", tags=["People"])
@log_return
@handle_exceptions
def get_people_by_id(id: int):
    return get_person_id(id)


@router.get("", summary="Получить всех людей", tags=["People"])
@log_return
@handle_exceptions
def get_people():
    return get_all_people()


@router.post("", tags=["People"], summary="Создать нового человека")
@log_return
@handle_exceptions
def create_new_person(person: CreatePerson):
    return create_person(person)
