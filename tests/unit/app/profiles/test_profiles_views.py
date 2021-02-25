from app.profiles.models import Profile
from typing import NoReturn
from database.repository import save
from app.coffe_room.models import CoffeRoom
from app.conventions.models import Convention


def test_get_all_profiles(app_context) -> NoReturn:
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

        test_client = app_context.app.test_client()
        # Actions
        request = test_client.get('/profiles')

        response = request.get_json()
        # Assert
        assert len(response) == 1

def test_create_profiles(app_context) -> NoReturn:
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
        payload = {
            'id': '07e7eced-e56b-47fe-94e4-d4c24fb4d191',
            'name': 'aycon',
            'last_name': 'Jack',
            'conventions_id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            'coffe_room_id': 'e3383c48-9b89-472f-9086-9cb21feaad7f'}
        test_client = app_context.app.test_client()

        request = test_client.post('/profiles', json=payload)
        response = request.get_json()
        assert len(response) == 5


def test_get_by_id_profile(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_profile = "d74052ac-cf9f-4baa-a49a-3993cdf0e50f"

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
        test_client = app_context.app.test_client()

        request = test_client.get(f'/profiles/{id_profile}')
        response = request.get_json()
        assert len(response) == 5


def test_get_all_profiles_with_id_convention(app_context) -> NoReturn:
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
        test_client = app_context.app.test_client()

        request = test_client.get('/convention/6b6ce977-1339-4461-9e7c-1a930a57dbdb/profiles')

        response = request.get_json()
        # Assert
        assert len(response) == 1


def test_get_all_profiles_with_id_coffe_room(app_context) -> NoReturn:
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
        test_client = app_context.app.test_client()

        request = test_client.get('/coffe-room/e3383c48-9b89-472f-9086-9cb21feaad7f/profiles')

        response = request.get_json()
        # Assert
        assert len(response) == 1


def test_delete_profile_with_id(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_profile = "d74052ac-cf9f-4baa-a49a-3993cdf0e50f"
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

        test_client = app_context.app.test_client()
        # Action
        request = test_client.delete(f'/profiles/{id_profile}')

        # Asserts
        assert request.status_code == 204


def test_update_profile(app_context) -> NoReturn:
    with app_context:
        # Arrange

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

        payload = {'name': 'James', 'last_name': 'Junior', 'conventions_id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                   'coffe_room_id':'e3383c48-9b89-472f-9086-9cb21feaad7f'}

        test_client = app_context.app.test_client()

        request = test_client.patch('/profiles/d74052ac-cf9f-4baa-a49a-3993cdf0e50f', json=payload)
        response = request.get_json()

        assert len(response) == 5
        assert response == {'coffe_room_id': 'e3383c48-9b89-472f-9086-9cb21feaad7f',
                            'conventions_id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                            'id': 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f',
                            'last_name': 'Junior',
                            'name': 'James'}
