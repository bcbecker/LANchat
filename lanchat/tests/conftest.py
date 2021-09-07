#unit test fixtures
import pytest
from lanchat import create_app
from run import socketio
from lanchat.config import Config


@pytest.fixture()
def test_app():
    """
    Create test app with proper config
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SERVER'] = Config.SERVER
    app.config['DEBUG'] = False

    return app

 
@pytest.fixture()
def flask_test_client(test_app):
    """
    Create test app client with proper config
    """
    with test_app.test_client() as test_client:
        with test_app.app_context():
            yield test_client

@pytest.fixture()
def test_sockets_client(test_app):
    """
    Connect sockets to app
    """
    flask_test_client = test_app.test_client()

    socketio_test_client = socketio.test_client(
        test_app, flask_test_client=flask_test_client)

    return socketio_test_client