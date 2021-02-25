from database.repository import save
from app.profiles.models import Profile
from app.conventions.models import Convention
from app.coffee_room.models import CoffeeRoom


def test_model_profile_return_dict(app_context):
    with app_context:
        # Action
        save(CoffeeRoom(
            id='e3383c48-9b89-472f-9086-9cb21feaad7f',
            name='CafeClub',
            capacity=23))

        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hall',
            capacity=23))

        profile = save(Profile(
            id='d74052ac-cf9f-4baa-a49a-3993cdf0e50f',
            name='Jon',
            last_name='Snow',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        # Assert
        assert isinstance(profile, Profile)
        assert profile.name == 'Jon'
        assert profile.last_name == 'Snow'
        assert profile.coffee_room_id == 'e3383c48-9b89-472f-9086-9cb21feaad7f'
        assert profile.conventions_id == '6b6ce977-1339-4461-9e7c-1a930a57dbdb'


def test_profile_serialize(app_context):
    with app_context:
        save(CoffeeRoom(
            id='e3383c48-9b89-472f-9086-9cb21feaad7f',
            name='CafeClub',
            capacity=23))

        save(Convention(
            id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            name='Hall',
            capacity=23))

        profile = save(Profile(
            id='d74052ac-cf9f-4baa-a49a-3993cdf0e50f',
            name='Jon',
            last_name='Snow',
            conventions_id='6b6ce977-1339-4461-9e7c-1a930a57dbdb',
            coffee_room_id='e3383c48-9b89-472f-9086-9cb21feaad7f'))

        profile_serialize = profile.serialize()

        assert profile_serialize == {'coffee_room_id': 'e3383c48-9b89-472f-9086-9cb21feaad7f',
                                     'conventions_id': '6b6ce977-1339-4461-9e7c-1a930a57dbdb',
                                     'id': 'd74052ac-cf9f-4baa-a49a-3993cdf0e50f',
                                     'last_name': 'Snow',
                                     'name': 'Jon'}