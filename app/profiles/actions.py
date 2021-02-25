from app.profiles.models import Profile
from database.repository import save, commit,delete
from uuid import uuid4
from app.coffee_room.actions import get_by_id as get_by_id_coffee_room
from app.conventions.actions import get_by_id as get_by_id_conventions

_LIMITE_LEN_FIELD = 36
from typing import NoReturn
from app.utils import is_empty_or_none
from exceptions import BadRequestException


def get():
    profile = Profile.query.all()
    return profile


def create(data):
    coffee_room = get_by_id_coffee_room(data['coffee_room_id'])
    _limite_coffee_room = coffee_room.capacity
    conventions = get_by_id_conventions(data['conventions_id'])
    _limite_conventions = conventions.capacity
    validate_name(data['name'])
    validate_last_name(data['last_name'])
    validate_maximum_profiles_in_same_conventions_room(data['conventions_id'], _limite_conventions)
    validate_maximum_profiles_in_same_coffee_room(data['coffee_room_id'], _limite_coffee_room)
    return save(Profile(id=str(uuid4()), name=data['name'], last_name=data['last_name'],
                        conventions_id=data['conventions_id'], coffee_room_id=data['coffee_room_id']))


def get_by_id(profile_id):
    validate_id_exist_in_database(profile_id)
    return Profile.query.filter_by(id=profile_id).first()


def validate_name(name) -> NoReturn:
    msg: str = f'Profile name is incorrect'
    if len(name) > _LIMITE_LEN_FIELD or is_empty_or_none(name):
        raise BadRequestException(msg)


def validate_last_name(last_name) -> NoReturn:
    msg: str = f'Profile last name is incorrect'
    if len(last_name) > _LIMITE_LEN_FIELD or is_empty_or_none(last_name):
        raise BadRequestException(msg)


def validate_maximum_profiles_in_same_conventions_room(_profile_conventions_id: str, _limite_conventions) -> NoReturn:
    msg: str = f'Maximum number of profiles in same conventions room.'
    _profile_saved = Profile.query.filter_by(conventions_id=_profile_conventions_id).all()
    if len(_profile_saved) > _limite_conventions: raise BadRequestException(msg)


def validate_maximum_profiles_in_same_coffee_room(_profile_coffee_room_id: str, _limite_coffee_room) -> NoReturn:
    msg: str = f'Maximum number of profiles in same coffee room.'
    _profile_saved = Profile.query.filter_by(coffee_room_id=_profile_coffee_room_id).all()
    if len(_profile_saved) > _limite_coffee_room: raise BadRequestException(msg)


def get_by_id_all_profile_in_the_same_convention_room(convention_id: str) -> Profile:
    return Profile.query.filter_by(conventions_id=convention_id).all()


def get_by_id_all_profile_in_the_same_coffee_room(coffee_room_id: str) -> Profile:
    return Profile.query.filter_by(coffee_room_id=coffee_room_id).all()


def update(id, data):
    profile = get_by_id(id)
    profile.name = data.get('name')
    profile.last_name = data.get('last_name')
    profile.conventions_id = data.get('conventions_id')
    profile.coffee_room_id = data.get('coffee_room_id')
    commit()
    return profile


def delete_profiles(id):
    profile = get_by_id(id)
    return delete(profile)


def validate_id_exist_in_database(profiles_id: str) -> NoReturn:
    msg: str = f'Convention room id: {profiles_id} does not exist in the database'
    profiles = Profile.query.filter_by(id=profiles_id).first()
    if profiles is None: raise BadRequestException(msg)