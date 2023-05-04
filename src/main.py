from __future__ import annotations

from .app import create_app
from .config import AppyConfig

app = create_app()

if __name__ == "__main__":
    config = AppyConfig()
    app.run(host=config.APP_HOST, port=config.APP_PORT)
