from flask import Blueprint, jsonify, request
from werkzeug.datastructures import MultiDict
from .news_service import news_list, create_news, show_news, update_news, destroy_news
from .news_serialize import NewsSchema
from .news_form import CreateNewsForm

module_news = Blueprint('module_news', __name__)


@module_news.route('', methods=['GET'])
def get_index():
    schema = NewsSchema(many=True)
    doc_list = news_list(status=request.args.get('status'), topics=request.args.getlist('topics'))

    return jsonify(status='success', data=schema.dump(doc_list).data)


@module_news.route('', methods=['POST'])
def post_news():
    schema = NewsSchema()
    form = CreateNewsForm(MultiDict(request.get_json()))

    if request.method == 'POST' and form.validate():
        news = create_news(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            topics=form.topics.data
        )

        res = jsonify(status='success', data=schema.dump(news).data)
        res.status_code = 201

        return res
    else:
        res = jsonify(status='fail', data={'validations': form.errors})
        res.status_code = 400

        return res


@module_news.route('/<news_id>', methods=['GET'])
def get_news(news_id):
    schema = NewsSchema()

    doc_news = show_news(news_id)

    if doc_news:
        return jsonify(status='success', data=schema.dump(doc_news).data)
    else:
        res = jsonify(status='error', error='not found', message='news with id=' + news_id + ' not found')
        res.status_code = 404

        return res


@module_news.route('/<news_id>', methods=['PUT'])
def put_news(news_id):
    schema = NewsSchema()
    form = CreateNewsForm(MultiDict(request.get_json()))

    if request.method == 'PUT' and form.validate():
        doc_news = update_news(news_id, title=form.title.data, description=form.description.data,
                               status=form.status.data)

        if doc_news:
            return jsonify(status='success', data=schema.dump(doc_news).data)
        else:
            res = jsonify(status='error', error='not found', message='news with id=' + news_id + ' not found')
            res.status_code = 404

            return res
    else:
        res = jsonify(status='fail', data={'validations': form.errors})
        res.status_code = 400

        return res


@module_news.route('/<news_id>', methods=['DELETE'])
def delete_news(news_id):
    doc_news = destroy_news(news_id)

    if doc_news:
        return jsonify(status='success', data=None)
    else:
        res = jsonify(status='error', error='not found', message='news with id=' + news_id + ' not found')
        res.status_code = 404

        return res
