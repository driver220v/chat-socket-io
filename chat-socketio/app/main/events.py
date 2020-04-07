import random
import string
from flask_socketio import send
from .. import socketio


def name_generator():
    dictionary = string.ascii_letters
    name = ''.join(random.choice(dictionary) for i in range(10))
    return name


@socketio.on('connect')
def test_connect():
    name = name_generator()
    send(f'User {name} has joined chat ', broadcast=True)


@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)
