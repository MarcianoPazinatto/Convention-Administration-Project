from app.coffee_room.models import CoffeeRoom
from database.repository import save, commit, delete
from uuid import uuid4
from typing import NoReturn, List, Dict
from app.utils import is_empty_or_none
from exceptions import BadRequestException

_LIMITE_LEN_FIELD = 36
from app.profiles.models import Profile


def get():
    return CoffeeRoom.query.all()


def create(data: dict) -> List[Profile]:
    validate_name(data['name'])
    validate_capacity(data['capacity'])
    return save(CoffeeRoom(id=str(uuid4()), name=data['name'], capacity=data['capacity']))


def get_by_id(coffee_room_id: str) -> Profile:
    validate_id_exist_in_database(coffee_room_id)
    return CoffeeRoom.query.filter_by(id=coffee_room_id).first()


def validate_name(name) -> NoReturn:
    msg: str = f'Coffee Room name is incorrect.'
    if len(name) > _LIMITE_LEN_FIELD or is_empty_or_none(name):
        raise BadRequestException(msg)


def validate_capacity(capacity) -> NoReturn:
    msg: str = f'Coffee room capacity has to be an integer.'
    try:
        int(capacity)
    except ValueError:
        raise BadRequestException(msg)


def update(id: str, data: Dict) -> Profile:
    coffee_room = get_by_id(id)
    coffee_room.name = data.get('name')
    coffee_room.capacity = data.get('capacity')
    commit()
    return coffee_room


def delete_coffee_room(id: str) -> NoReturn:
    coffee_room = get_by_id(id)
    validate_delete_coffee_room(id)
    return delete(coffee_room)


def validate_delete_coffee_room(coffee_room_id: str) -> NoReturn:
    msg: str = 'Convention table cannot be deleted, there are data in it.'
    if len(get_by_id_all_profile_in_the_same_coffee_room(coffee_room_id)) > 0:
        raise BadRequestException(msg)


def get_by_id_all_profile_in_the_same_coffee_room(coffee_room_id: str) -> Profile:
    return Profile.query.filter_by(coffee_room_id=coffee_room_id).all()


def validate_id_exist_in_database(coffee_room_id: str) -> NoReturn:
    msg: str = f'Coffee room id: {coffee_room_id} does not exist in the database'
    coffee_room = CoffeeRoom.query.filter_by(id=coffee_room_id).first()
    if coffee_room is None: raise BadRequestException(msg)
