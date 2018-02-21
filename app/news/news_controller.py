from flask import Blueprint, jsonify, request
from .news_service import news_list
from .news_serialize import NewsSchema

module_news = Blueprint('module_news', __name__)


@module_news.route('/', methods=['GET'])
def get_index():
    schema = NewsSchema(many=True)

    doc_list = news_list(status=request.args.get('status'))

    return jsonify(status='success', data=schema.dump(doc_list).data)
