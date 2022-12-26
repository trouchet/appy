from __future__ import annotations

from flask import Flask

from blueprints.bundler import blueprints

app = Flask(__name__)

map(lambda blueprint: app.register_blueprint(blueprint), blueprints)
