from flask import Blueprint
from views import get_users

api_route = Blueprint("user", __name__)

api_route.add_url_rule("/users-details", view_func=get_users, methods=["GET"])
