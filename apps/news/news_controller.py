from .news_service import news_list, create_news, show_news, update_news, destroy_news
from .news_serialize import NewsSchema
from .news_form import CreateNewsForm
from flask import Blueprint, jsonify, request
from werkzeug.datastructures import MultiDict

module_news = Blueprint('module_news', __name__)

"""
@api {get} /news List News
@apiName ListNews
@apiGroup News

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X GET -d http://localhost/news

@apiSuccess {DateTime} created_at Created date of the news.
@apiSuccess {Text} description Description of the news.
@apiSuccess {Integer} id Id of the news.
@apiSuccess {String} status Status of the news (draft, publish).
@apiSuccess {String} title Title of the news.
@apiSuccess {Array} topics Array topic id of the news.
@apiSuccess {DateTime} updated_at Updated date of the news.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "data": [
            {
                "created_at": "2018-02-22T14:00:02+00:00",
                "deleted_at": null,
                "description": "indonesia election",
                "id": 1,
                "status": "draft",
                "title": "indonesia election",
                "topics": [
                    145
                ],
                "updated_at": "2018-02-22T14:00:02+00:00"
            },
            {...}
        ],
        "status": "success"
    }
"""


@module_news.route('', methods=['GET'])
def get_index():
    schema = NewsSchema(many=True)
    doc_list = news_list(status=request.args.get('status'), topics=request.args.getlist('topics'))

    return jsonify(status='success', data=schema.dump(doc_list).data)


"""
@api {post} /news Create News
@apiName PostNews
@apiGroup News

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X POST -d "{'title': 'indonesia election', 'description': 'indonesia election', 'topics': [145]}" 
        http://localhost/news

@apiParam (Body) {String} title Title of the news.
@apiParam (Body) {String} description Description of the news.
@apiParam (Body) {Array} topics Array topic id of the news.

@apiParamExample (Body) {json} Request-Body-Example:
    {
        "title": "indonesia election",
        "description": "indonesia election",
        "topics": [145]
    }

@apiSuccess {DateTime} created_at Created date of the news.
@apiSuccess {Text} description Description of the news.
@apiSuccess {Integer} id Id of the news.
@apiSuccess {String} status Status of the news (draft, publish).
@apiSuccess {String} title Title of the news.
@apiSuccess {Array} topics Array topic id of the news.
@apiSuccess {DateTime} updated_at Updated date of the news.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 OK
    {
        "data": {
            "created_at": "2018-02-22T14:00:02+00:00",
            "deleted_at": null,
            "description": "indonesia election",
            "id": 3744,
            "status": "draft",
            "title": "indonesia election",
            "topics": [
                145
            ],
            "updated_at": "2018-02-22T14:00:02+00:00"
        },
        "status": "success"
    }
"""


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


"""
@api {get} /news/:news_id Get News
@apiName GetNews
@apiGroup News

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X get -d http://localhost/news/3744

@apiParam {Integer} news_id Id of the news.

@apiParamExample {json} Request-Body-Example:
    {
        "id": "3744"
    }

@apiSuccess {DateTime} created_at Created date of the news.
@apiSuccess {Text} description Description of the news.
@apiSuccess {Integer} id Id of the news.
@apiSuccess {String} status Status of the news (draft, publish).
@apiSuccess {String} title Title of the news.
@apiSuccess {Array} topics Array topic id of the news.
@apiSuccess {DateTime} updated_at Updated date of the news.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 OK
    {
        "data": {
            "created_at": "2018-02-22T14:00:02+00:00",
            "deleted_at": null,
            "description": "indonesia election",
            "id": 3744,
            "status": "draft",
            "title": "indonesia election",
            "topics": [
                145
            ],
            "updated_at": "2018-02-22T14:00:02+00:00"
        },
        "status": "success"
    }
"""


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


"""
@api {put} /news/:news_id Update News
@apiName PutNews
@apiGroup News

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X POST -d "{'title': 'indonesia election', 'description': 'indonesia election', 'topics': [4711]}" 
        http://localhost/news/3744

@apiParam {Integer} news_id Id of the news.

@apiParamExample (Body) {json} Request-Body-Example:
    {
        "id": "3744"
    }

@apiParam (Body) {String} title Title of the news.
@apiParam (Body) {String} description Description of the news.

@apiParamExample (Body) {json} Request-Body-Example:
    {
        "title": "indonesia election",
        "description": "indonesia election",
    }

@apiSuccess {DateTime} created_at Created date of the news.
@apiSuccess {Text} description Description of the news.
@apiSuccess {Integer} id Id of the news.
@apiSuccess {String} status Status of the news (draft, publish).
@apiSuccess {String} title Title of the news.
@apiSuccess {Array} topics Array topic id of the news.
@apiSuccess {DateTime} updated_at Updated date of the news.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 OK
    {
        "data": {
            "created_at": "2018-02-22T14:00:02+00:00",
            "deleted_at": null,
            "description": "indonesia election",
            "id": 3744,
            "status": "draft",
            "title": "indonesia election",
            "topics": [
                145,
            ],
            "updated_at": "2018-02-22T14:00:02+00:00"
        },
        "status": "success"
    }
"""


@module_news.route('/<news_id>', methods=['PUT'])
def put_news(news_id):
    schema = NewsSchema()
    form = CreateNewsForm(MultiDict(request.get_json()))

    if request.method == 'PUT' and form.validate():
        doc_news = update_news(news_id,
                               title=form.title.data,
                               description=form.description.data,
                               status=form.status.data,
                               topics=form.topics.data
                               )

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


"""
@api {delete} /news/:news_id Delete News
@apiName DeleteNews
@apiGroup News

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X PUT -d http://localhost/news/3744

@apiParam {Integer} news_id Id of the topic.

@apiParamExample {json} Request-Parameter-Example:
    {
        "id": 4711
    }

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 OK
    {
        "data": null,
        "status": "success"
    }
"""


@module_news.route('/<news_id>', methods=['DELETE'])
def delete_news(news_id):
    doc_news = destroy_news(news_id)

    if doc_news:
        return jsonify(status='success', data=None)
    else:
        res = jsonify(status='error', error='not found', message='news with id=' + news_id + ' not found')
        res.status_code = 404

        return res
