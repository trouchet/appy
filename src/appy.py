from flask import Flask, request, Blueprint, render_template, abort

from markupsafe import escape

from .blueprints import simple_blueprint

app = Flask(__name__)

# import declared routes
from .routes import root
from .routes import users
from .routes import projects

