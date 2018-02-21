from app.news.news_controller import module_news
from flask import Flask, jsonify
from flask_migrate import Migrate
from helpers.database import db
from helpers.marshmallow import ma

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_pyfile('config.cfg', silent=True)

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

ma.init_app(app)

app.register_blueprint(module_news, url_prefix='/news')


@app.route('/ping')
def get_ping():
    res = jsonify(status='success', data={'message': 'pong'})
    return res


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
