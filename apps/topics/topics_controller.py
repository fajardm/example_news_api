from .topics_service import topics_list, create_topic, show_topic, update_topic, destroy_topic
from .topics_serialize import TopicsSchema
from .topics_form import CreateTopicForm
from flask import Blueprint, jsonify, request
from werkzeug.datastructures import MultiDict

module_topics = Blueprint('module_topics', __name__)

"""
@api {get} /topics List Topics
@apiName GetTopics
@apiGroup Topics

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X GET -d http://localhost/topics

@apiSuccess {DateTime} created_at Created date of the topic.
@apiSuccess {Integer} id Id of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {DateTime} updated_at Updated date of the topic.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "data": [
            {
                "created_at": "2018-02-22T13:14:24+00:00",
                "deleted_at": null,
                "id": 1,
                "name": "election",
                "news_id": [],
                "updated_at": "2018-02-22T13:14:24+00:00"
            },
            {...}
        ],
        "status": "success"
    }
"""


@module_topics.route('', methods=['GET'])
def get_index():
    schema = TopicsSchema(many=True)

    doc_list = topics_list()

    return jsonify(status='success', data=schema.dump(doc_list).data)


"""
@api {post} /topics Create Topic
@apiName PostTopics
@apiGroup Topics

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X POST -d "{'name': 'election'}" http://localhost/topics
        
@apiParam (Body) {String} name Name of the topic.

@apiParamExample (Body) {json} Request-Body-Example:
    {
        "name": "party"
    }

@apiSuccess {DateTime} created_at Created date of the topic.
@apiSuccess {Integer} id Id of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {DateTime} updated_at Updated date of the topic.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 OK
    {
        "data": {
            "created_at": "2018-02-22T13:14:24+00:00",
            "deleted_at": null,
            "id": 1,
            "name": "pemilu",
            "news_id": [],
            "updated_at": "2018-02-22T13:14:24+00:00"
        },
        "status": "success"
    }
"""


@module_topics.route('', methods=['POST'])
def post_topic():
    schema = TopicsSchema()
    form = CreateTopicForm(MultiDict(request.get_json()))

    if request.method == 'POST' and form.validate():
        topic = create_topic(name=form.name.data)

        res = jsonify(status='success', data=schema.dump(topic).data)
        res.status_code = 201

        return res
    else:
        res = jsonify(status='fail', data={'validations': form.errors})
        res.status_code = 400

        return res


"""
@api {get} /topics/:topic_id Get Topic
@apiName GetTopic
@apiGroup Topics

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X GET -d http://localhost/topics/4711
        
@apiParam {Integer} topic_id Id of the topic.

@apiParamExample {json} Request-Parameter-Example:
    {
        "id": 4711
    }

@apiSuccess {DateTime} created_at Created date of the topic.
@apiSuccess {Integer} id Id of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {DateTime} updated_at Updated date of the topic.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "data": {
            "created_at": "2018-02-22T13:14:24+00:00",
            "deleted_at": null,
            "id": 4711,
            "name": "election",
            "news_id": [],
            "updated_at": "2018-02-22T13:14:24+00:00"
        },
        "status": "success"
    }
"""


@module_topics.route('/<topic_id>', methods=['GET'])
def get_topic(topic_id):
    schema = TopicsSchema()

    doc_topic = show_topic(topic_id)

    if doc_topic:
        return jsonify(status='success', data=schema.dump(doc_topic).data)
    else:
        res = jsonify(status='error', error='not found', message='topic with id=' + topic_id + ' not found')
        res.status_code = 404

        return res


"""
@api {put} /topics/:topic_id Update Topic
@apiName PutTopic
@apiGroup Topics

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X PUT -d "{'name': 'party'}" http://localhost/topics/4711
        
@apiParam {Integer} topic_id Id of the topic.

@apiParamExample {json} Request-Parameter-Example:
    {
        "id": 4711
    }

@apiParam {String} topic_id Id of the topic.

@apiParamExample {json} Request-Body-Example:
    {
        "name": "party"
    }

@apiSuccess {DateTime} created_at Created date of the topic.
@apiSuccess {Integer} id Id of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {String} name Name of the topic.
@apiSuccess {DateTime} updated_at Updated date of the topic.

@apiSuccessExample {json} Success-Response:
    HTTP/1.1 201 OK
    {
        "data": {
            "created_at": "2018-02-22T13:14:24+00:00",
            "deleted_at": null,
            "id": 4711,
            "name": "party",
            "news_id": [],
            "updated_at": "2018-02-22T13:14:24+00:00"
        },
        "status": "success"
    }
"""


@module_topics.route('/<topic_id>', methods=['PUT'])
def put_topic(topic_id):
    schema = TopicsSchema()
    form = CreateTopicForm(MultiDict(request.get_json()))

    if request.method == 'PUT' and form.validate():
        doc_topic = update_topic(topic_id, name=form.name.data)

        if doc_topic:
            return jsonify(status='success', data=schema.dump(doc_topic).data)
        else:
            res = jsonify(status='error', error='not found', message='topic with id=' + topic_id + ' not found')
            res.status_code = 404

            return res
    else:
        res = jsonify(status='fail', data={'validations': form.errors})
        res.status_code = 400

        return res


"""
@api {delete} /topics/:topic_id Delete Topic
@apiName DeleteTopic
@apiGroup Topics

@apiExample {curl} Example usage:
    curl -i \
        -H "Content-Type: application/json" \
        -X PUT -d http://localhost/topics/4711

@apiParam {Integer} topic_id Id of the topic.

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


@module_topics.route('/<topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    doc_topic = destroy_topic(topic_id)

    if doc_topic:
        return jsonify(status='success', data=None)
    else:
        res = jsonify(status='error', error='not found', message='topic with id=' + topic_id + ' not found')
        res.status_code = 404

        return res
