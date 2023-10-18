""" This module contains routes for authentication """
from api.auths import auth
from models import storage
from flask import current_app, make_response, jsonify, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from hashlib import md5
import jwt


@auth.route('/login', methods=['POST'])
def login():
    """ Logs in a user """
    credentials = request.get_json()
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
        {'id': user.id},
        current_app.config['SECRET_KEY'],
        algorithm='HS256')
    response = make_response(jsonify(user.to_dict()), 200)
    response.set_cookie('token', token, httponly=False)
    return response


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    """ Logs out a user """
    logout_user()
    response = make_response(jsonify({}), 200)
    response.delete_cookie('token')
    return response


@auth.route('/auth_status')
def auth_status():
    """ Checks the authentication status """
    if current_user.is_authenticated:
        return jsonify({'authenticated': True, 'user': current_user.to_dict()})
    return jsonify({'authenticated': False})