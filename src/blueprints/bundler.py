from __future__ import annotations

from error_handler import error_handler_bp
from posts import posts_bp
from projects import projects_bp
from root import root_bp
from users import users_bp

blueprints = [posts_bp, users_bp, projects_bp, root_bp, error_handler_bp]
