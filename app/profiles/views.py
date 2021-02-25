from flask import Blueprint, request, jsonify
from app.profiles.actions import create as create_profile, \
    get as get_profile, \
    get_by_id as get_by_id_profile, \
    get_by_id_all_profile_in_the_same_convention_room as get_by_id_all_profiles_conventions, \
    get_by_id_all_profile_in_the_same_coffee_room as get_by_id_all_profiles_coffee_rooms, delete_profiles, \
    update as update_profiles_with_id
from typing import Tuple

app_profiles = Blueprint('app.profiles', __name__)


@app_profiles.route('/profiles', methods=['GET'])
def get() -> tuple:
    return jsonify([profile.serialize() for profile in get_profile()]), 200


@app_profiles.route('/profiles', methods=['POST'])
def post() -> tuple:
    profile = request.get_json()
    profile_create = create_profile(profile)
    return jsonify(profile_create.serialize()), 201


@app_profiles.route('/profiles/<id>', methods=['GET'])
def get_by_id(id: str) -> tuple:
    profile = get_by_id_profile(id)
    return jsonify(profile.serialize()), 200


@app_profiles.route('/convention/<id>/profiles', methods=['GET'])
def get_by_all_profiles_conventions(id: str) -> Tuple:
    all_profiles = get_by_id_all_profiles_conventions(id)
    return jsonify([profiles.serialize() for profiles in all_profiles]), 200


@app_profiles.route('/coffee-room/<id>/profiles', methods=['GET'])
def get_by_all_profiles_coffee_rooms(id: str) -> Tuple:
    all_profiles = get_by_id_all_profiles_coffee_rooms(id)
    return jsonify([profiles.serialize() for profiles in all_profiles]), 200


@app_profiles.route('/profiles/<id>', methods=['DELETE'])
def delete_profiles_with_id(id: str) -> Tuple:
    delete_profiles(id)
    return jsonify({}), 204


@app_profiles.route('/profiles/<id>', methods=['PATCH'])
def update_profiles(id: str) -> Tuple:
    payload = request.get_json()
    profiles = update_profiles_with_id(id, payload)
    return jsonify(profiles.serialize()), 200
