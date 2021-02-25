from app.profiles.actions import create, get, get_by_id, validate_name, validate_last_name,\
    validate_maximum_profiles_in_same_coffee_room, validate_maximum_profiles_in_same_conventions_room, \
    get_by_id_all_profile_in_the_same_coffee_room, get_by_id_all_profile_in_the_same_convention_room,\
    update, delete_profiles
from app.coffee_room.models import CoffeeRoom
from app.conventions.models import Convention
from app.profiles.models import Profile
from database.repository import save
import pytest
from exceptions import BadRequestException


def test_create_profile(app_context, mocker):
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

        mock_uuid = mocker.patch('app.profiles.actions.uuid4')
        mock_uuid.return_value = 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        # Action
        profile = create({ "name":"Paul",
                              "last_name": "Anka",
                              "conventions_id": "6b6ce977-1339-4461-9e7c-1a930a57dbdb",
                              "coffee_room_id": "e3383c48-9b89-472f-9086-9cb21feaad7f"})
        # Assert
        assert profile.id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert profile.name == 'Paul'
        assert profile.last_name == "Anka"
        assert profile.coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'
        assert profile.conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'


def test_get_all_profiles(app_context):
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
        # Action
        profile = get()

        # Assert
        assert isinstance(profile, list)
        assert len(profile) == 1
        assert isinstance(profile[0], Profile)


def test_get_by_id_profile(app_context):
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

        # Actions
        profile = get_by_id('d74052ac-cf9f-4baa-a49a-3993cdf0e50f')

        # Asserts
        assert profile.id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert profile.name == 'Jon'
        assert profile.last_name == 'Snow'
        assert profile.conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert profile.coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'


def test_validate_name(app_context):
    with app_context:

        with pytest.raises(BadRequestException) as ex:
            validate_name('')

        assert (str(ex.value) == '400 Bad Request: Profile name is incorrect')


def test_validate_last_name(app_context):
    with app_context:

        with pytest.raises(BadRequestException) as ex:
            validate_last_name('')

        assert (str(ex.value) == '400 Bad Request: Profile last name is incorrect')


def test_validate_maximum_profiles_in_same_conventions_room(app_context):
    with app_context:
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
        save(Profile(
            id='A74052ac-cf9f-4baa-a49a-3993cdf0e50t',
            name='Marcos',
            last_name='Nor',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        with pytest.raises(BadRequestException) as ex:
            validate_maximum_profiles_in_same_conventions_room('6b6ce977-1339-4461-9e7c-1a930a57dbdb', 1)

        assert (str(ex.value) == '400 Bad Request: Maximum number of profiles in same conventions room.')


def test_validate_maximum_profiles_in_same_coffee_room(app_context):
    with app_context:
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
        save(Profile(
            id='A74052ac-cf9f-4baa-a49a-3993cdf0e50t',
            name='Hanna',
            last_name='Barbara',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        with pytest.raises(BadRequestException) as ex:
            validate_maximum_profiles_in_same_coffee_room('e3383c48-9b89-472f-9086-9cb21feaad7f', 1)

        assert (str(ex.value) == '400 Bad Request: Maximum number of profiles in same coffee room.')


def test_get_by_id_all_profiles_in_the_same_coffee_room(app_context):
    with app_context:
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
        save(Profile(
            id='A74052ac-cf9f-4baa-a49a-3993cdf0e50t',
            name='Hanna',
            last_name='Barbara',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        profile = get_by_id_all_profile_in_the_same_coffee_room('e3383c48-9b89-472f-9086-9cb21feaad7f')

        assert profile[0].id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert profile[0].name == 'Jon'
        assert profile[0].last_name == 'Snow'
        assert profile[0].conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert profile[0].coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'
        assert profile[1].id == 'A74052ac-cf9f-4baa-a49a-3993cdf0e50t'
        assert profile[1].name == 'Hanna'
        assert profile[1].last_name == 'Barbara'
        assert profile[1].conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert profile[1].coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'


def test_get_by_id_all_profiles_in_the_same_conveention_room(app_context):
    with app_context:
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
        save(Profile(
            id='A74052ac-cf9f-4baa-a49a-3993cdf0e50t',
            name='Hanna',
            last_name='Barbara',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        profile = get_by_id_all_profile_in_the_same_convention_room('6b6ce977-1339-4461-9e7c-1a930a57dbdb')

        assert profile[0].id == 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f'
        assert profile[0].name == 'Jon'
        assert profile[0].last_name == 'Snow'
        assert profile[0].conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert profile[0].coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'
        assert profile[1].id == 'A74052ac-cf9f-4baa-a49a-3993cdf0e50t'
        assert profile[1].name == 'Hanna'
        assert profile[1].last_name == 'Barbara'
        assert profile[1].conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert profile[1].coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'


def test_update_profile(app_context):
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
        # Action
        profile = update('d74052ac-cf9f-4baa-a49a-3993cdf0e50f', {'name': 'João', 'last_name': 'Neves',
                                                        'conventions_id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                                                        'coffee_room_id': 'e3383c48-9b89-472f-9086-9cb21feaad7f'})
        # Assert
        assert profile.name == 'João'
        assert profile.last_name == 'Neves'
        assert profile.conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'
        assert profile.coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'


def test_delete_profile(app_context):
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
        # Action
        delete_profiles('d74052ac-cf9f-4baa-a49a-3993cdf0e50f')

        # Assert
        profile = get()
        assert len(profile) == 0