from apps.news.news_controller import module_news
from apps.topics.topics_controller import module_topics
from flask import Flask, jsonify
from flask_migrate import Migrate
from helpers.database import db
from helpers.marshmallow import ma


def create_app(config=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.update(config or {})
    app.config.from_pyfile('../config.cfg', silent=True)

    # set up extensions
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    # register blueprints
    register_blueprints(app)

    # endpoint to ping
    @app.route('/ping')
    def get_ping():
        res = jsonify(status='success', data={'message': 'pong'})
        return res

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})

    return app


def register_blueprints(app):
    app.register_blueprint(module_topics, url_prefix='/topics')
    app.register_blueprint(module_news, url_prefix='/news')
    return app
