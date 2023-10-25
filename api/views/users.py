""" This module contains the user view """
from api.views import app_views
from flask import (
    jsonify,
    request,
    abort,
    current_app,
    make_response
)
from flask_login import login_user
from models import storage
from models import manager
from models.user import User
import jwt


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ Returns all users """
    users = storage.all('User')
    return jsonify([user.to_dict() for user in users.values()])


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Creates a user """
    data = request.form.to_dict(flat=True)
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
            abort(400, f'Missing {r}')
    existing_user = storage.lookup(email=data['email'])
    if existing_user:
        abort(409, 'User with email already exists')
    user = User(**data)
    folder_id = manager.create_user_folder(user)
    user.folder = folder_id
    storage.add(user)
    login_user(user)
    token = jwt.encode(
        {'id': user.id},
        current_app.config['SECRET_KEY'],
        algorithm='HS256')
    response = make_response(jsonify(user.to_dict()), 201)
    response.set_cookie('token', token, httponly=False)
    return response


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
    data = request.form.to_dict(flat=True)
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


@app_views.route(
        '/users/<user_id>/books',
        methods=['GET'],
        strict_slashes=False)
def get_user_books(user_id):
    """ Returns all books from a user """
    user = storage.get('User', user_id)
    if not user:
        abort(404)
    with storage.session_scope() as session:
        user = session.merge(user)
        books = [book.to_dict() for book in user.books]
    return jsonify(books)


@app_views.route('/users/top', methods=['GET'], strict_slashes=False)
def get_top_users():
    """ Returns the top n users """
    n = request.args.get('n', 3)
    users = storage.top('User', n)
    return jsonify([user.to_dict() for user in users])
