from flask import Blueprint, jsonify, request
from .topics_service import topics_list, create_topic, show_topic, update_topic, destroy_topic
from .topics_serialize import TopicsSchema
from .topics_form import CreateTopicForm

module_topics = Blueprint('module_topics', __name__)


@module_topics.route('', methods=['GET'])
def get_index():
    schema = TopicsSchema(many=True)

    doc_list = topics_list()

    return jsonify(status='success', data=schema.dump(doc_list).data)


@module_topics.route('', methods=['POST'])
def post_topic():
    schema = TopicsSchema()
    form = CreateTopicForm(request.form)

    if request.method == 'POST' and form.validate():
        topic = create_topic(name=form.name.data)

        res = jsonify(status='success', data=schema.dump(topic).data)
        res.status_code = 201

        return res
    else:
        res = jsonify(status='fail', data={'validations': form.errors})
        res.status_code = 400

        return res


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


@module_topics.route('/<topic_id>', methods=['PUT'])
def put_topic(topic_id):
    schema = TopicsSchema()
    form = CreateTopicForm(request.form)

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


@module_topics.route('/<topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    doc_topic = destroy_topic(topic_id)

    if doc_topic:
        return jsonify(status='success', data=None)
    else:
        res = jsonify(status='error', error='not found', message='topic with id=' + topic_id + ' not found')
        res.status_code = 404

        return res
