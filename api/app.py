""" This module contains the flask app """
from os import environ
from dotenv.main import load_dotenv
from flask import (
    Flask,
    make_response,
    jsonify,
)
from flask_cors import CORS
from flask_login import LoginManager
from models import storage
from api.views import app_views
from api.auths import auth


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

login_manager = LoginManager(app)

CORS(
    auth,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True)

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
    load_dotenv()
    app.run(
        host='0.0.0.0',
        port=environ.get('PUBLIB_PORT', default='5000'),
        threaded=True)
