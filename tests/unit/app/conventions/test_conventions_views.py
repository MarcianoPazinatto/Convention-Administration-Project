from database.repository import save
from app.conventions.models import Convention
from typing import NoReturn


def test_get_all_conventions(app_context) -> NoReturn:
    with app_context:
        # Arrange
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Great Hall',
            capacity=23))
        test_client = app_context.app.test_client()
        # Actions
        request = test_client.get('/conventions')

        response = request.get_json()
        # Assert
        assert len(response) == 1


def test_create_conventions(app_context) -> NoReturn:
    with app_context:
        # Arrange
        payload = {
            'id': '07e7eced-e56b-47fe-94e4-d4c24fb4d191',
            'name': "Master Hall",
            'capacity': 30}
        test_client = app_context.app.test_client()

        request = test_client.post('/conventions', json=payload)
        response = request.get_json()
        assert len(response) == 3


def test_get_by_id_conventions(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_conventions = "6b6ce977-1339-4461-9e7c-1a930a57dbdb"
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Great Hall',
            capacity=23))
        test_client = app_context.app.test_client()

        request = test_client.get(f'/conventions/{id_conventions}')
        response = request.get_json()
        assert len(response) == 3


def test_delete_conventions_room_with_id(app_context) -> NoReturn:
    with app_context:
        # Arrange
        id_conventions = "6b6ce977-1339-4461-9e7c-1a930a57dbdb"
        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Big Master Hall',
            capacity=100))
        test_client = app_context.app.test_client()
        # Action
        request = test_client.delete(f'/conventions/{id_conventions}')

        # Asserts
        assert request.status_code == 204


def test_update_conventions_room(app_context) -> NoReturn:
    with app_context:
        # Arrange

        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hyper Hall',
            capacity=23))

        payload = {'name': 'Greatest Hall', 'capacity': 70}

        test_client = app_context.app.test_client()

        request = test_client.patch('/conventions/6b6ce977-1339-4461-9e7c-1a930a57dbdb', json=payload)
        response = request.get_json()

        assert len(response) == 3
        assert response == {'capacity': 70,
                            'id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                            'name': 'Greatest Hall'}