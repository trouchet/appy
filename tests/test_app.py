# test_me.py

# Take a look at:
#   1. https://testdriven.io/blog/flask-pytest/
#   2. https://flask.palletsprojects.com/en/1.1.x/testing/

from __future__ import annotations
from src.main import app

def test_index_route():
    routes_paths=[
        '/',
        '/about',
        '/hello',
        '/hello/',
        '/hello/world',
        '/favicon.ico',
        '/users/',
        '/users/adam',
        '/path',
        '/path/42',
        '/login',
        '/posts/42',
        '/projects/'
    ]

    with app.test_client() as c:
        for routes_path in routes_paths:
            response = c.get(routes_path)
            assert response.status_code == 200
