from __future__ import annotations

from .app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run()
