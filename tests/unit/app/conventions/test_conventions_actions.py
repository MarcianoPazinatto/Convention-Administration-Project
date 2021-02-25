from app.conventions.actions import create, get, get_by_id, validate_name, validate_capacity, delete_conventions, \
    update, validate_delete_conventions_room, get_by_id_all_profile_in_the_same_convention_room
from app.conventions.models import Convention
from database.repository import save
import pytest
from exceptions import BadRequestException
from app.profiles.models import Profile
from app.coffe_room.models import CoffeRoom


def test_create_conventions(app_context, mocker):
    with app_context:
        # Arrange
        mock_uuid = mocker.patch('app.conventions.actions.uuid4')
        mock_uuid.return_value = 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        # Action
        conventions = create({"name": "Great Hall", "capacity": 30})
        # Assert
        assert conventions.id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert conventions.name == 'Great Hall'
        assert conventions.capacity == 30


def test_get_all_conventions(app_context):
    with app_context:
        # Arrange
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hall',
            capacity=23))
        # Action
        conventions = get()

        # Assert
        assert isinstance(conventions, list)
        assert len(conventions) == 1
        assert isinstance(conventions[0], Convention)


def test_get_by_id_conventions(app_context):
    with app_context:
        # Arrange
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Great Hall',
            capacity=23))
        # Action
        conventions = get_by_id('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        # Assert
        assert conventions.id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert conventions.name == 'Great Hall'
        assert conventions.capacity == 23


def test_validate_name(app_context):
    with app_context:
        with pytest.raises(BadRequestException) as ex:
            validate_name('')

        assert (str(ex.value) == '400 Bad Request: Convention name is incorrect.')


def test_validate_capacity(app_context):
    with app_context:
        with pytest.raises(BadRequestException) as ex:
            validate_capacity("nove")

        assert (str(ex.value) == '400 Bad Request: Convention room capacity has to be an integer.')


def test_validates_update_conventions(app_context):
    with app_context:
        # Arrange
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hall',
            capacity=23))
        # Action
        conventions = update('6b6ce977-1339-4461-9e7c-1a930a57dbdb', {'name': 'Best Hall', 'capacity': '50'})

        # Asserts

        assert conventions.name == 'Best Hall'
        assert conventions.capacity == 50


def test_delete_conventions(app_context):
    with app_context:
        # Arrange
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Clubest',
            capacity=23))
        # Action
        delete_conventions('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        # Assert
        conventions = get()
        assert len(conventions) == 0


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
            validate_delete_conventions_room('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        assert (str(ex.value) == '400 Bad Request: Convention table cannot be deleted, there are data in it.')


def test_get_all_profile_with_same_id_convention_room(app_context):
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

        profile = get_by_id_all_profile_in_the_same_convention_room('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        assert len(profile) == 1
        assert profile[0].name == 'Jon'
        assert profile[0].last_name == 'Snow'
        assert profile[0].id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
