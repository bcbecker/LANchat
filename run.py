from flask import session
from flask_socketio import SocketIO
import time
from lanchat import create_app
from lanchat.config import Config
from lanchat.database import DataBase


app = create_app()
socketio = SocketIO(app)


@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    """
    handles saving messages once received from web server
    and sending message to other clients
    :param json: json
    :param methods: POST GET
    :return: None
    """
    data = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)




if __name__ == "__main__": 
    socketio.run(app, debug=True, host=str(Config.SERVER))
