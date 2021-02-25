from database.repository import save
from app.coffee_room.models import CoffeeRoom
from typing import NoReturn


def test_get_all_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        test_client = app_context.app.test_client()
        # Actions
        request = test_client.get('/coffee-room')

        response = request.get_json()
        # Assert
        assert len(response) == 1


def test_create_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        payload = {
            'id': '07e7eced-e56b-47fe-94e4-d4c24fb4d191',
            'name': "Jon Coffe",
            'capacity': 30}
        test_client = app_context.app.test_client()

        request = test_client.post('/coffee-room', json=payload)
        response = request.get_json()
        assert len(response) == 3


def test_get_by_id_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_coffee_room = "6b6ce977-1339-4461-9e7c-1a930a57dbdb"
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        test_client = app_context.app.test_client()

        request = test_client.get(f'/coffee-room/{id_coffee_room}')
        response = request.get_json()
        assert len(response) == 3


def test_delete_coffee_room_with_id(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_coffee_room = "6b6ce977-1339-4461-9e7c-1a930a57dbdb"
        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        test_client = app_context.app.test_client()
        # Action
        request = test_client.delete(f'/coffee-room/{id_coffee_room}')

        # Asserts
        assert request.status_code == 204


def test_update_coffee_room(app_context) -> NoReturn:
    with app_context:
        # Arrange

        save(CoffeeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))

        payload = {'name': 'Greatest Hall', 'capacity': 70}

        test_client = app_context.app.test_client()

        request = test_client.patch('/coffee-room/6b6ce977-1339-4461-9e7c-1a930a57dbdb', json=payload)
        response = request.get_json()

        assert len(response) == 3
        assert response == {'capacity': 70,
                            'id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                            'name': 'Greatest Hall'}