from time import sleep

from fastapi import APIRouter, Depends

from schemas.schemas import CreatePerson, Person
from services.auth_service import security
from services.database_service import create_database
from services.services import create_person, get_all_people, get_person_id
from utils.decorators import handle_exceptions, log_return

router = APIRouter(prefix="/peoples", tags=["People"])
database = APIRouter(prefix="/database", tags=["DataBase"])


@router.get(
    "/root",
    summary="Main",
    tags=["Main"],
    dependencies=[Depends(security.access_token_required)],
)
@log_return
@handle_exceptions
def root():
    return "Hello world"


@router.get(
    "/{id}",
    summary="Получить конкретного человека по id",
    tags=["People"],
    dependencies=[Depends(security.access_token_required)],
)
@log_return
@handle_exceptions
def get_people_by_id(id: int) -> Person:
    return get_person_id(id)


@router.get(
    "",
    summary="Получить всех людей",
    tags=["People"],
    dependencies=[Depends(security.access_token_required)],
)
@log_return
@handle_exceptions
def get_people() -> list[Person]:
    return get_all_people()


@router.post(
    "",
    tags=["People"],
    summary="Создать нового человека",
    dependencies=[Depends(security.access_token_required)],
)
@log_return
@handle_exceptions
def create_new_person(person: CreatePerson) -> Person:
    sleep(1)
    return create_person(person)


@database.post(
    "",
    tags=["DataBase"],
    summary="Создаем базу данных",
    dependencies=[Depends(security.access_token_required)],
)
@log_return
@handle_exceptions
async def setup_database():
    return await create_database()
