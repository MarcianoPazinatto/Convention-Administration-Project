import pytest
from sqlalchemy import event

from app import create_app, db
from app.coffe_room.models import CoffeRoom
from app.conventions.models import Convention
from app.profiles.models import Profile


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    app = create_app()
    db.create_all(app=app)
    session.app = app


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """


@pytest.fixture(scope="function", autouse=True)
def app_context(request):
    yield request.session.app.app_context()
    db.drop_all(app=request.session.app)
    db.create_all(app=request.session.app)
