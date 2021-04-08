from flask import Flask

app = Flask(__name__, template_folder='views')

from src.controllers import *

def start_app():
    app.run(port = 5500, debug=True)