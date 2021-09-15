#flask routes test routes.py 

def test_home_route(flask_test_client, test_sockets_client):
    """
    GIVEN a Flask application configured with sockets
    WHEN a request is made to "/home"
    THEN check that redirects to login, since not logged in
    """
    response = flask_test_client.get("/", data={"name": ""})
    assert response.status_code == 302
    assert test_sockets_client.is_connected()

def test_login_route(flask_test_client, test_sockets_client):
    """
    GIVEN a Flask application configured with sockets
    WHEN a request is made to "/login"
    THEN check that the redirects to home for successful login
    """
    response = flask_test_client.post("/login", data={"name": "test"})
    assert response.status_code == 302
    assert test_sockets_client.is_connected()

def test_history_route(flask_test_client, test_sockets_client):
    """
    GIVEN a Flask application configured with sockets
    WHEN a request is made to "/history"
    THEN check that OK (200) and no messages
    """
    response = flask_test_client.post("/login", data={"name": "test"})
    response = flask_test_client.get("/history")
    assert response.status_code == 200
    assert test_sockets_client.is_connected()