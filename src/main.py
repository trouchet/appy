from __future__ import annotations

from .app import create_app
from .config import AppyConfig
from flask import Flask

app = create_app()
config=AppyConfig()

if __name__ == "__main__":
    app.run(host=config.APP_HOST, port=config.APP_PORT)

