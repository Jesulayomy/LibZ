""" This module contains the flask app """
from models import storage
from api.views import app_views
from api.auths import auth
from os import environ
from flask import (
    Flask,
    make_response,
    jsonify,
)
from flask_cors import CORS
from flask_login import LoginManager
from dotenv.main import load_dotenv


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

login_manager = LoginManager(app)

app.register_blueprint(app_views)
app.register_blueprint(auth)

cors = CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True)


@login_manager.user_loader
def load_user(user_id):
    """ Loads the user """
    return storage.get('User', user_id)


@app.teardown_appcontext
def close_db(err):
    """ Closes the storage session on an error """
    storage.close()


@app.errorhandler(404)
def not_found(err):
    """ Handles 404 errors """
    response = make_response(jsonify({'Error': 'Not Found'}), 404)
    return response


if __name__ == '__main__':
    """ Runs the app with the environment variables """
    load_dotenv()
    app.run(
        host='0.0.0.0',
        port=environ.get('DB_DEV_PORT', default='5000'),
        threaded=True)
