from __future__ import annotations

from .app import create_app
from flask import Flask

# create our application :)
app = Flask(__name__)
app.run()
