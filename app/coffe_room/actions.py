from app.coffe_room.models import CoffeRoom
from database.repository import save, commit, delete
from uuid import uuid4
from typing import NoReturn
from app.utils import is_empty_or_none
from exceptions import BadRequestException
_LIMITE_LEN_FIELD = 36
from app.profiles.models import Profile

def get():
    return CoffeRoom.query.all()


def create(data):
    validate_name(data['name'])
    validate_capacity(data['capacity'])
    return save(CoffeRoom(id=str(uuid4()), name=data['name'], capacity=data['capacity']))


def get_by_id(coffe_room_id):
    validate_id_exist_in_database(coffe_room_id)
    return CoffeRoom.query.filter_by(id=coffe_room_id).first()


def validate_name(name) -> NoReturn:
    msg: str = f'Coffe Room name is incorrect.'
    if len(name) > _LIMITE_LEN_FIELD or is_empty_or_none(name):
        raise BadRequestException(msg)


def validate_capacity(capacity) -> NoReturn:
    msg: str = f'Coffe room capacity has to be an integer.'
    try:
        int(capacity)
    except ValueError:
        raise BadRequestException(msg)


def update(id, data):
    coffe_room = get_by_id(id)
    coffe_room.name = data.get('name')
    coffe_room.capacity = data.get('capacity')
    commit()
    return coffe_room


def delete_coffe_room(id):
    coffe_room = get_by_id(id)
    validate_delete_coffe_room(id)
    return delete(coffe_room)


def validate_delete_coffe_room(coffe_room_id):
    msg: str = 'Convention table cannot be deleted, there are data in it.'
    if len(get_by_id_all_profile_in_the_same_coffe_room(coffe_room_id)) > 0:
        raise BadRequestException(msg)


def get_by_id_all_profile_in_the_same_coffe_room(coffe_room_id: str) -> Profile:
    return Profile.query.filter_by(coffe_room_id=coffe_room_id).all()


def validate_id_exist_in_database(coffe_room_id: str) -> NoReturn:
    msg: str = f'Coffe room id: {coffe_room_id} does not exist in the database'
    coffe_room = CoffeRoom.query.filter_by(id=coffe_room_id).first()
    if coffe_room is None: raise BadRequestException(msg)