# test_me.py

# Take a look at:
#   1. https://testdriven.io/blog/flask-pytest/
#   2. https://flask.palletsprojects.com/en/1.1.x/testing/

from __future__ import annotations

from src.main import app

client = app.test_client()


def test_get_routes():
    routes_paths = [
        "/",
        "/about",
        "/hello",
        "/hello/",
        "/hello/world",
        "/favicon.ico",
        "/users/",
        "/users/adam",
        "/path",
        "/path/42",
        "/login",
        "/posts/42",
        "/projects/",
    ]

    with client:
        for routes_path in routes_paths:
            response = client.get(routes_path)
            assert response.status_code == 200


def test_post_routes():
    routes_paths = [
        "/login",
    ]

    with client:
        for routes_path in routes_paths:
            login_metadata = {"username": "ackbar", "password_hash": "42"}

            response = client.post(routes_path, json=login_metadata)
            assert response.status_code == 200
