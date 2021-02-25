import uuid
from database import db


class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(36), nullable=False)
    last_name = db.Column(db.String(36), nullable=False)
    conventions_id = db.Column(db.String(36), db.ForeignKey('convention.id'), nullable=False)
    coffee_room_id = db.Column(db.String(36), db.ForeignKey('coffee_room.id'), nullable=False)
    coffee_room = db.relationship('CoffeeRoom', back_populates='profiles_id')
    convention = db.relationship('Convention', back_populates='profiles_id')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'coffee_room_id': self.coffee_room_id,
            'conventions_id': self.conventions_id
        }

