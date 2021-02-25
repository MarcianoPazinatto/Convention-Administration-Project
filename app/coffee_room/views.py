from flask import Blueprint, request, jsonify
from app.coffee_room.actions import create as create_coffee_room, \
    get as get_coffee_room, \
    get_by_id as get_by_id_coffee_room, delete_coffee_room, update as update_coffee_room_with_id

app_coffee_room = Blueprint('app.coffee_room', __name__)


@app_coffee_room.route('/coffee-room', methods=['GET'])
def get() -> tuple:
    coffee_rooms = get_coffee_room()
    return jsonify([coffee_room.serialize() for coffee_room in coffee_rooms]), 200


@app_coffee_room.route('/coffee-room', methods=['POST'])
def post() -> tuple:
    coffee_room = request.get_json()
    coffee_room_create = create_coffee_room(coffee_room)
    return jsonify(coffee_room_create.serialize()), 201


@app_coffee_room.route('/coffee-room/<id>', methods=['GET'])
def get_by_id(id: str) -> tuple:
    coffee_room = get_by_id_coffee_room(id)
    return jsonify(coffee_room.serialize()), 200


@app_coffee_room.route('/coffee-room/<id>', methods=['DELETE'])
def delete_coffee_room_with_id(id: str)  -> tuple:
    delete_coffee_room(id)
    return jsonify({}), 204


@app_coffee_room.route('/coffee-room/<id>', methods=['PATCH'])
def update_coffee_room(id: str) -> tuple:
    payload = request.get_json()
    coffee_room = update_coffee_room_with_id(id, payload)
    return jsonify(coffee_room.serialize()), 200
