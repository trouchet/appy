from __future__ import annotations

from flask import Blueprint

projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("/")
def show_projects():
    return "The project page"
