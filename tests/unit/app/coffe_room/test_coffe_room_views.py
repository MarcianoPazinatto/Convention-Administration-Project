from database.repository import save
from app.coffe_room.models import CoffeRoom
from typing import NoReturn


def test_get_all_coffe_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        test_client = app_context.app.test_client()
        # Actions
        request = test_client.get('/coffe-room')

        response = request.get_json()
        # Assert
        assert len(response) == 1


def test_create_coffe_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        payload = {
            'id': '07e7eced-e56b-47fe-94e4-d4c24fb4d191',
            'name': "Jon Coffe",
            'capacity': 30}
        test_client = app_context.app.test_client()

        request = test_client.post('/coffe-room', json=payload)
        response = request.get_json()
        assert len(response) == 3


def test_get_by_id_coffe_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_coffe_room = "6b6ce977-1339-4461-9e7c-1a930a57dbdb"
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        test_client = app_context.app.test_client()

        request = test_client.get(f'/coffe-room/{id_coffe_room}')
        response = request.get_json()
        assert len(response) == 3


def test_delete_coffe_room_with_id(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_coffe_room = "6b6ce977-1339-4461-9e7c-1a930a57dbdb"
        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        test_client = app_context.app.test_client()
        # Action
        request = test_client.delete(f'/coffe-room/{id_coffe_room}')

        # Asserts
        assert request.status_code == 204


def test_update_coffe_room(app_context) -> NoReturn:
    with app_context:
        # Arrange

        save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))

        payload = {'name': 'Greatest Hall', 'capacity': 70}

        test_client = app_context.app.test_client()

        request = test_client.patch('/coffe-room/6b6ce977-1339-4461-9e7c-1a930a57dbdb', json=payload)
        response = request.get_json()

        assert len(response) == 3
        assert response == {'capacity': 70,
                            'id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                            'name': 'Greatest Hall'}