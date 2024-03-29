from __future__ import annotations

import pytest

from ..src.app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
