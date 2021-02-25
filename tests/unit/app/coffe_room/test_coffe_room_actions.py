from app.coffe_room.actions import create, get, get_by_id, validate_name, validate_capacity, update, \
    delete_coffe_room, validate_delete_coffe_room, get_by_id_all_profile_in_the_same_coffe_room
from app.conventions.models import Convention
from app.coffe_room.models import CoffeRoom
from app.profiles.models import Profile
from database.repository import save
import pytest
from exceptions import BadRequestException


def test_create_coffe_room(app_context, mocker):
    with app_context:
        # Arrange
        mock_uuid = mocker.patch('app.coffe_room.actions.uuid4')
        mock_uuid.return_value = 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        # Action
        coffe_room = create({ "name":"Coffe in House",
                              "capacity": 30 })
        # Assert
        assert coffe_room.id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert coffe_room.name == 'Coffe in House'
        assert coffe_room.capacity == 30


def test_get_all_coffe_room(app_context):
    with app_context:
        # Arrange
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        coffe_room = get()

        # Assert
        assert isinstance(coffe_room, list)
        assert len(coffe_room) == 1
        assert isinstance(coffe_room[0], CoffeRoom)


def test_get_by_id_coffe_room(app_context):
    with app_context:
        # Arrange
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        coffe_room = get_by_id('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        # Assert
        assert coffe_room.id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert coffe_room.name == 'CafeClub'
        assert coffe_room.capacity == 23


def test_validate_name(app_context):
    with app_context:

        with pytest.raises(BadRequestException) as ex:
            validate_name('')

        assert (str(ex.value) == '400 Bad Request: Coffe Room name is incorrect.')


def test_validate_capacity(app_context):
    with app_context:
        with pytest.raises(BadRequestException) as ex:
            validate_capacity("nove")

        assert (str(ex.value) == '400 Bad Request: Coffe room capacity has to be an integer.')


def test_validates_update_coffe_room(app_context):
    with app_context:
        # Arrange
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        coffe_room = update('6b6ce977-1339-4461-9e7c-1a930a57dbdb', {'name':'Best Coffe', 'capacity':'50'})

        # Asserts

        assert coffe_room.name == 'Best Coffe'
        assert coffe_room.capacity == 50


def test_delete_coffe_room(app_context):
    with app_context:
        # Arrange
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Action
        delete_coffe_room('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        # Assert
        coffe_room = get()
        assert len(coffe_room) == 0


def test_validate_delete_room(app_context):
    with app_context:
        # Arrange
        save(CoffeRoom(
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
            coffe_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        with pytest.raises(BadRequestException) as ex:
            validate_delete_coffe_room('e3383c48-9b89-472f-9086-9cb21feaad7f')

        assert (str(ex.value) == '400 Bad Request: Convention table cannot be deleted, there are data in it.')


def test_get_all_profile_with_same_id_coffe_room(app_context):
    with app_context:
        # Arrange
        save(CoffeRoom(
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
            coffe_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        profile = get_by_id_all_profile_in_the_same_coffe_room('e3383c48-9b89-472f-9086-9cb21feaad7f')

        assert len(profile) == 1
        assert profile[0].name == 'Jon'
        assert profile[0].last_name == 'Snow'
        assert profile[0].id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'

