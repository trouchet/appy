from __future__ import annotations

from flask import Blueprint
from markupsafe import escape

users_bp = Blueprint("users", __name__, url_prefix='/users')


@users_bp.route("/")
@users_bp.route("/<username>")
def show_user_profile(username=None):
    if username is None:
        return "User unknown"
    else:
        return f"User {escape(username)}"

    # show the user profile for that user
