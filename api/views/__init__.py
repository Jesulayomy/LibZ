""" This module contains the blueprint for the API """
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/')


from api.views.index import *  # noqa: E402
from api.views.users import *  # noqa: E402
from api.views.books import *  # noqa: E402
