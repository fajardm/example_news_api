from flask import Blueprint, jsonify
from .news_service import index
from .news_model import NewsSchema

module_news = Blueprint('module_news', __name__)


@module_news.route('/', methods=['GET'])
def get_index():
    schema = NewsSchema(many=True)
    return jsonify(status='success', data=schema.dump(index()).data)
