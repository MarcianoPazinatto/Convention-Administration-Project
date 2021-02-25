from database.repository import save
from app.conventions.models import Convention
from typing import NoReturn


def test_model_conventions_return_dict(app_context) -> NoReturn:
    with app_context:
        # Action
        conventions = save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Conventions Hall',
            capacity=23))
        # Assert
        assert isinstance(conventions, Convention)
        assert conventions.name == 'Conventions Hall'
        assert conventions.capacity == 23


def test_conventions_serialize(app_context) -> NoReturn:
    with app_context:
        conventions = save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Conventions Hall',
            capacity=23))
        conventions_serialize = conventions.serialize()

        assert conventions_serialize == {'capacity': 23,
                                        'id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                                        'name': 'Conventions Hall'}