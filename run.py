from flask import Blueprint, render_template
from app import create_app
from database import db


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)