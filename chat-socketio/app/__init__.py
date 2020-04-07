from flask import Flask
from flask_socketio import SocketIO

from .main import main as main_blueprint

socketio = SocketIO()


def create_app(debug=False):
    # connect extensions
    app = Flask(__name__)
    app.debug = debug
    # CSRF security key
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
