import uuid
from database import db




class CoffeRoom(db.Model):
    __tablename__ = 'coffe_room'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(36), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    profiles_id = db.relationship('Profile', uselist=False, back_populates='coffe_room')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity
        }
