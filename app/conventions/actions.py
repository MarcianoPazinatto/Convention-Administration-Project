from app.conventions.models import Convention
from database.repository import save, commit, delete
from uuid import uuid4
from typing import NoReturn, Dict, List
from app.utils import is_empty_or_none
from exceptions import BadRequestException
from app.profiles.models import Profile

_LIMITE_LEN_NAME = 36


def get():
    return Convention.query.all()


def create(data: dict) -> List[Convention]:
    validate_name(data['name'])
    validate_capacity(data['capacity'])
    return save(Convention(id=str(uuid4()), name=data['name'], capacity=data['capacity']))


def get_by_id(conventions_id: str) -> Convention:
    validate_id_exist_in_database(conventions_id)
    return Convention.query.filter_by(id=conventions_id).first()


def validate_name(name: str) -> NoReturn:
    msg: str = f'Convention name is incorrect.'
    if len(name) > _LIMITE_LEN_NAME or is_empty_or_none(name):
        raise BadRequestException(msg)


def validate_capacity(capacity: int) -> NoReturn:
    msg: str = f'Convention room capacity has to be an integer.'
    try:
        int(capacity)
    except ValueError:
        raise BadRequestException(msg)


def update(id: str, data: Dict) -> Convention:
    conventions = get_by_id(id)
    conventions.name = data.get('name')
    conventions.capacity = data.get('capacity')
    commit()
    return conventions


def delete_conventions(id: str) -> NoReturn:
    conventions = get_by_id(id)
    validate_delete_conventions_room(id)
    return delete(conventions)


def validate_delete_conventions_room(conventions_id: str) -> NoReturn:
    msg: str = 'Convention table cannot be deleted, there are data in it.'
    if len(get_by_id_all_profile_in_the_same_convention_room(conventions_id)) > 0:
        raise BadRequestException(msg)


def get_by_id_all_profile_in_the_same_convention_room(convention_id: str) -> Profile:
    return Profile.query.filter_by(conventions_id=convention_id).all()


def validate_id_exist_in_database(conventions_id: str) -> NoReturn:
    msg: str = f'Convention room id: {conventions_id} does not exist in the database'
    conventions = Convention.query.filter_by(id=conventions_id).first()
    if conventions is None: raise BadRequestException(msg)
