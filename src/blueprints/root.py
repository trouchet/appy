from __future__ import annotations

from os import path

from flask import Blueprint, current_app, request, send_from_directory
from markupsafe import escape

root_bp = Blueprint("root", __name__)


@root_bp.route("/")
def show_projects():
    return "The project page"


@root_bp.route("/about")
def about():
    return "The about page"


@root_bp.route("/login", methods=["GET", "POST"])
def do_login():
    if request.method == "POST":
        return "do login"
    else:
        return "show login form"


@root_bp.route("/hello/")
@root_bp.route("/hello")
@root_bp.route("/hello/<name>")
def say_hello(name=None):
    if name is None:
        return "Hello, World!"
    else:
        return f"Hello, {escape(name)}!"


@root_bp.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


@root_bp.route("/favicon.ico")
def favicon():
    static_path = path.join(current_app.root_path, "static")
    return send_from_directory(static_path, "favicon.ico")
