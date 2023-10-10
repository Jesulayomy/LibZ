""" This module contains the flask app """
from models import storage
from api.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from dotenv.main import load_dotenv


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.register_blueprint(app_views)

cors = CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True)


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
