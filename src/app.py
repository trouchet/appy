from __future__ import annotations

from flask import Flask
from .config import AppyConfig

# App Factory:
#   https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    app.config.from_object(AppyConfig)

    from .blueprints.bundler import blueprints

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
