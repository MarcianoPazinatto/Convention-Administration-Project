from database.repository import save
from app.coffe_room.models import CoffeRoom


def test_model_coffe_room_return_dict(app_context):
    with app_context:
        # Action
        coffe_room = save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        # Assert
        assert isinstance(coffe_room, CoffeRoom)
        assert coffe_room.name == 'CafeClub'
        assert coffe_room.capacity == 23


def test_coffe_room_serialize(app_context):
    with app_context:
        coffe_room = save(CoffeRoom(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='CafeClub',
            capacity=23))
        coffe_room_serialize = coffe_room.serialize()

        assert coffe_room_serialize == {'capacity': 23,
                                        'id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                                        'name': 'CafeClub'}