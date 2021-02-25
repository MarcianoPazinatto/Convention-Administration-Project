from flask import Blueprint, request, jsonify
from app.conventions.actions import create as create_convention, \
    get as get_convention, \
    get_by_id as get_by_id_convention, delete_conventions, update as update_conventions_with_id

app_conventions = Blueprint('app.conventions', __name__)


@app_conventions.route('/conventions', methods=['GET'])
def get() -> tuple:
    conventions = get_convention()
    return jsonify([convention.serialize() for convention in conventions]), 200


@app_conventions.route('/conventions', methods=['POST'])
def post() -> tuple:
    convention = request.get_json()
    convention_create = create_convention(convention)
    return jsonify(convention_create.serialize()), 201


@app_conventions.route('/conventions/<id>', methods=['GET'])
def get_by_id(id: str) -> tuple:
    convention = get_by_id_convention(id)
    return jsonify(convention.serialize()), 200


@app_conventions.route('/conventions/<id>', methods=['DELETE'])
def delete_conventions_with_id(id: str) -> tuple:
    delete_conventions(id)
    return jsonify({}), 204


@app_conventions.route('/conventions/<id>', methods=['PATCH'])
def update_conventions(id: str) -> tuple:
    payload = request.get_json()
    conventions = update_conventions_with_id(id, payload)
    return jsonify(conventions.serialize()), 200
