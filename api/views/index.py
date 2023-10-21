""" This module contains the index view """
from api.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns the status of the API """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Returns the stats of the API """
    return jsonify({'stats': {
        'users': storage.count('User'),
        'books': storage.count('Book'),
    }})


@app_views.route('/stats/users', methods=['GET'], strict_slashes=False)
def stats_users():
    """ Returns the stats of the users """
    return jsonify({'users': storage.count('User')})


@app_views.route('/stats/books', methods=['GET'], strict_slashes=False)
def stats_books():
    """ Returns the stats of the books """
    return jsonify({'books': storage.count('Book')})
