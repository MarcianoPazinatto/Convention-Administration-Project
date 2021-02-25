from flask import Blueprint, request, jsonify
from app.coffe_room.actions import create as create_coffe_room, \
    get as get_coffe_room, \
    get_by_id as get_by_id_coffe_room, delete_coffe_room, update as update_coffe_room_with_id

app_coffe_room = Blueprint('app.coffe_room', __name__)


@app_coffe_room.route('/coffe-room', methods=['GET'])
def get():
    coffe_rooms = get_coffe_room()
    return jsonify([coffe_room.serialize() for coffe_room in coffe_rooms]), 200


@app_coffe_room.route('/coffe-room', methods=['POST'])
def post():
    coffe_room = request.get_json()
    coffe_room_create = create_coffe_room(coffe_room)
    return jsonify(coffe_room_create.serialize()), 201


@app_coffe_room.route('/coffe-room/<id>', methods=['GET'])
def get_by_id(id):
    coffe_room = get_by_id_coffe_room(id)
    return jsonify(coffe_room.serialize()), 200


@app_coffe_room.route('/coffe-room/<id>', methods=['DELETE'])
def delete_coffe_room_with_id(id):
    delete_coffe_room(id)
    return jsonify({}), 204


@app_coffe_room.route('/coffe-room/<id>', methods=['PATCH'])
def update_coffe_room(id):
    payload = request.get_json()
    coffe_room = update_coffe_room_with_id(id, payload)
    return jsonify(coffe_room.serialize()), 200