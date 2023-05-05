from __future__ import annotations

from .app import create_app
from .config import AppyConfig

app = create_app()

config = AppyConfig()
app.config.update(config.toDict())
