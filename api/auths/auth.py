""" This module contains routes for authentication """
from hashlib import md5
from flask import current_app, make_response, jsonify, request, abort
from flask_login import current_user, login_user, logout_user, login_required
import jwt
from api.auths import auth
from models import storage


@auth.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """ Logs in a user """
    credentials = request.form.to_dict()
    if not credentials:
        abort(400, 'Not a JSON')
    email = credentials.get('email')
    if not email:
        abort(400, 'Missing email')
    password = credentials.get('password')
    if not password:
        abort(400, 'Missing password')
    user = storage.lookup(email)
    if not user:
        abort(404, 'No user found')
    md5_password = md5(password.encode('utf-8')).hexdigest()
    if md5_password != user.password:
        abort(401, 'Incorrect password')
    login_user(user)
    token = jwt.encode(
        {'user_id': user.id},
        current_app.config['SECRET_KEY'],
        algorithm='HS256')
    response = make_response(jsonify(user.to_dict()), 200)
    response.set_cookie('token', token, httponly=False)
    return response


@auth.route('/logout', methods=['POST'], strict_slashes=False)
@login_required
def logout():
    """ Logs out a user """
    logout_user()
    response = make_response(jsonify({}), 200)
    response.delete_cookie('token')
    return response


@auth.route('/current_user', methods=['GET'], strict_slashes=False)
def get_current_user():
    """ gets the current authenticated user """
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict())
    return jsonify({})
