from flask import Flask
app = Flask(__name__)


app.config.from_object('core.config.ProductionConfig')
config = app.config

from core import routes
from core.controllers.usercontroller import app as users
from core.controllers.authcontroller import app as auth

# https://flask.palletsprojects.com/en/1.1.x/blueprints/
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='/auth')