from app.coffee_room.actions import create, get, get_by_id, validate_name, validate_capacity, update, \
    delete_coffee_room, validate_delete_coffee_room, get_by_id_all_profile_in_the_same_coffee_room
from app.conventions.models import Convention
from app.coffee_room.models import CoffeeRoom
from app.profiles.models import Profile
from database.repository import save
import pytest
from exceptions import BadRequestException
from typing import NoReturn


def test_create_coffee_room(app_context, mocker) -> NoReturn:
    with app_context:
        # Arrange
        mock_uuid = mocker.patch('app.coffee_room.actions.uuid4')
        mock_uuid.return_value = 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        # Action
        coffee_room = create({ "name":"Coffee in House",
                              "capacity": 30 })
        # Assert
        assert coffee_room.id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert coffee_room.name == 'Coffee in House'
        assert coffee_room.capacity == 30


def test_get_all_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        coffee_room = get()

        # Assert
        assert isinstance(coffee_room, list)
        assert len(coffee_room) == 1
        assert isinstance(coffee_room[0], CoffeeRoom)


def test_get_by_id_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        coffee_room = get_by_id('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        # Assert
        assert coffee_room.id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert coffee_room.name == 'CafeClub'
        assert coffee_room.capacity == 23


def test_validate_name(app_context) -> NoReturn:
    with app_context:

        with pytest.raises(BadRequestException) as ex:
            validate_name('')

        assert (str(ex.value) == '400 Bad Request: Coffee Room name is incorrect.')


def test_validate_capacity(app_context) -> NoReturn:
    with app_context:
        with pytest.raises(BadRequestException) as ex:
            validate_capacity("nove")

        assert (str(ex.value) == '400 Bad Request: Coffee room capacity has to be an integer.')


def test_validates_update_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        coffee_room = update('6b6ce977-1339-4461-9e7c-1a930a57dbdb', {'name':'Best Coffee', 'capacity':'50'})

        # Asserts

        assert coffee_room.name == 'Best Coffee'
        assert coffee_room.capacity == 50


def test_delete_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        delete_coffee_room('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        # Assert
        coffee_room = get()
        assert len(coffee_room) == 0


def test_validate_delete_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='e3383c48-9b89-472f-9086-9cb21feaad7f',
            name='CafeClub',
            capacity=23))

        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hall',
            capacity=23))

        save(Profile(
            id='d74052ac-cf9f-4baa-a49a-3993cdf0e50f',
            name='Jon',
            last_name='Snow',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        with pytest.raises(BadRequestException) as ex:
            validate_delete_coffee_room('e3383c48-9b89-472f-9086-9cb21feaad7f')

        assert (str(ex.value) == '400 Bad Request: Convention table cannot be deleted, there are data in it.')


def test_get_all_profile_with_same_id_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='e3383c48-9b89-472f-9086-9cb21feaad7f',
            name='CafeClub',
            capacity=23))

        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hall',
            capacity=23))

        save(Profile(
            id='d74052ac-cf9f-4baa-a49a-3993cdf0e50f',
            name='Jon',
            last_name='Snow',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        coffee_room = get_by_id_all_profile_in_the_same_coffee_room('e3383c48-9b89-472f-9086-9cb21feaad7f')

        assert len(coffee_room) == 1
        assert coffee_room[0].name == 'Jon'
        assert coffee_room[0].last_name == 'Snow'
        assert coffee_room[0].id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'

