#flask server test run.py 
from run import socketio

def test_server_and_socket(test_app):
    """
    GIVEN a Flask application configured for testing
    WHEN sockets attempts connection to flask
    THEN check that the connection was successful
    """
    flask_test_client = test_app.test_client()

    socketio_test_client = socketio.test_client(
        test_app, flask_test_client=flask_test_client)

    assert socketio_test_client.is_connected()
