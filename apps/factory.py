from apps.news.news_controller import module_news
from flask import Flask, jsonify
from flask_migrate import Migrate
from helpers.database import db
from helpers.marshmallow import ma


def create_app(config=None):
    app = Flask('apps')

    app.config.update(config or {})
    app.config.from_pyfile('../config.cfg', silent=True)

    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)

    register_blueprints(app)

    @app.route('/ping')
    def get_ping():
        res = jsonify(status='success', data={'message': 'pong'})
        return res

    return app


def register_blueprints(app):
    app.register_blueprint(module_news, url_prefix='/news')
    return app
