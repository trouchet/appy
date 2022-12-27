"""Flask configuration."""
from __future__ import annotations

from os import environ, path

from dotenv import load_dotenv

base_path = path.dirname(__file__)
basedir = path.abspath(base_path)
env_path = path.join(basedir, ".env")

load_dotenv(env_path)


class ConfigException(Exception):
    pass


class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")

    DATABASE_ENGINE = environ.get("DATABASE_ENGINE")
    DATABASE_USERNAME = environ.get("DATABASE_USERNAME")
    DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
    DATABASE_HOST = environ.get("DATABASE_HOST")
    DATABASE_NAME = environ.get("DATABASE_NAME")
    DATABASE_PORT = environ.get("DATABASE_PORT")

    DATABASE_URI_str = "{engine}://{username}:{password}@{host}:{port}/{name}"

    DATABASE_URI = DATABASE_URI_str.format(
        engine=DATABASE_ENGINE or "postgresql",
        username=DATABASE_USERNAME or "postgres",
        password=DATABASE_PASSWORD or "postgres",
        host=DATABASE_HOST or "localhost",
        name=DATABASE_NAME or "appy_db",
        port=DATABASE_PORT or "5432",
    )

    if FLASK_ENV not in ["development", "production"]:
        message = "There are only option 'development' and 'production'"
        raise ConfigException(message)

    env_flag = True if FLASK_ENV == "development" else False

    DEBUG = env_flag
    TESTING = env_flag
