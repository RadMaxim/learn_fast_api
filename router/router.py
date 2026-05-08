from schemas.schemas import  CreatePerson
from services.services import get_person_id,get_all_people, create_person
from fastapi import APIRouter
from utils.decorators import log_return, handle_exceptions

router = APIRouter(
    prefix="/peoples",
    tags=["People"]
)

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


@router.get("", summary="Получить всех людей", tags =["People"])
@log_return
@handle_exceptions

def get_people():
    return get_all_people()


@router.post("", tags=["People"], summary="Создать нового человека")
@log_return
@handle_exceptions

def create_new_person(person:CreatePerson):
    return create_person(person)
