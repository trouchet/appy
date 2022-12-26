from __future__ import annotations

from flask import Blueprint

error_handler_bp = Blueprint("error_handlers", __name__)


@error_handler_bp.app_errorhandler(404)
def page_not_found(error):
    return "Error 404"
