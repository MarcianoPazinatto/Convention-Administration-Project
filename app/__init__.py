from flask import Flask, json
from database import db, migrate
from app.profiles.views import app_profiles
from app.conventions.views import app_conventions
from app.coffe_room.views import app_coffe_room
from werkzeug.exceptions import HTTPException, InternalServerError

def create_app():
    app = Flask(__name__)
    _register_blueprint(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    _register_error_handler(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(app_profiles)
    app.register_blueprint(app_conventions)
    app.register_blueprint(app_coffe_room)


def _handle_default_exception(e):
    response = e.get_response()
    code = e.code
    description = e.description
    response.data = get_data(code, description)
    response.content_type = "application/json"
    return response, code


def get_data(code, description):
    return json.dumps({
        'code': code,
        'message': description,
    })


def _handle_internal_server_error_exception(e):
    response = e.get_response()
    code = 500
    description = 'Sorry, we cant process request. Try again.'
    response.data = get_data(code, description)
    response.content_type = "application/json"
    return response, code


def _register_error_handler(app):
    app.register_error_handler(HTTPException, _handle_default_exception)
    app.register_error_handler(InternalServerError, _handle_internal_server_error_exception)
