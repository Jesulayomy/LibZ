""" This module contains the user view """
from api.views import app_views
from flask import (
    jsonify,
    request,
    abort,
)
from models import storage
from models import manager
from models.user import User
from models.book import Book


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ Returns all users """
    users = storage.all('User')
    return jsonify([user.to_dict() for user in users.values()])


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Creates a user """
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    required = [
        'first_name',
        'last_name',
        'gender',
        'email',
        'password',
    ]
    for r in required:
        if r not in data:
            abort(400, 'Missing {}'.format(r))
    user = User(**data)
    folder_id = manager.create_user_folder(user)
    user.folder = folder_id
    storage.add(user)
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Returns a user """
    user = storage.get('User', user_id)
    if user:
        return jsonify(user.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Updates a user """
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignore = [
        'id',
        'email',
        'created_at',
        'updated_at',
    ]
    for k, v in data.items():
        if k not in ignore:
            setattr(user, k, v)
    storage.add(user)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a user """
    user = storage.get('User', user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/users/<user_id>/books', methods=['GET'], strict_slashes=False)
def get_user_books(user_id):
    """ Returns all books from a user """
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    return jsonify([book.to_dict() for book in user.books])
