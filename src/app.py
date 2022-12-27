from __future__ import annotations

from os import path
from flask import Flask, send_from_directory

# App Factory: https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_filename) 

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            path.join(app.root_path, 'static'),
            'favicon.ico'
    )
    
    from .blueprints.bundler import blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app




