""" This module contains the blueprint for authentication """
from flask import Blueprint


auth = Blueprint('auth', __name__, url_prefix='/auth/')


from api.auths.auth import *  # noqa: E402
