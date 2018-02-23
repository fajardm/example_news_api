import unittest
from apps.factory import create_app
from apps.topics.topics_model import Topics
from faker import Faker
from flask import json
from helpers.database import db

fake = Faker()


class TopicsTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        app.app_context().push()
        self.app = app.test_client()

        Topics.query.delete()

    def tearDown(self):
        Topics.query.delete()

    def test_should_success_get_index(self):
        doc = Topics(
            name=fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None),
        )
        db.session.add(doc)
        db.session.commit()

        res = self.app.get('/topics')

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'

    def test_should_success_post_topic(self):
        res = self.app.post('/topics', data=json.dumps(dict(name='topic 1')), content_type='application/json')

        obj = json.loads(res.data)

        assert res.status_code == 201
        assert obj['status'] == 'success'
        assert obj['data']['name'] == 'topic 1'

    def test_should_error_validation_post_topic(self):
        res = self.app.post('/topics')

        obj = json.loads(res.data)

        assert res.status_code == 400
        assert obj['status'] == 'fail'
        assert obj['data']['validations']['name'] is not None

        doc = Topics(name='topic 2')
        db.session.add(doc)
        db.session.commit()

        res2 = self.app.post('/topics', data=json.dumps(dict(name='topic 2')), content_type='application/json')

        obj2 = json.loads(res2.data)

        assert res2.status_code == 400
        assert obj2['status'] == 'fail'
        assert obj2['data']['validations']['name'] is not None

    def test_should_success_get_topic(self):
        doc = Topics(
            name=fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None),
        )
        db.session.add(doc)
        db.session.commit()

        res = self.app.get('/topics/' + str(doc.id))

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'
        assert obj['data']['name'] == doc.name

    def test_should_not_found_get_topic(self):
        res = self.app.get('/topics/10000000')

        obj = json.loads(res.data)

        assert res.status_code == 404
        assert obj['status'] == 'error'
        assert obj['error'] == 'not found'

        res2 = self.app.get('/topics/invalid')

        obj2 = json.loads(res.data)

        assert res2.status_code == 404
        assert obj2['status'] == 'error'
        assert obj2['error'] == 'not found'

    def test_should_success_put_topic(self):
        doc = Topics(name=fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None))
        db.session.add(doc)
        db.session.commit()

        res = self.app.put('/topics/' + str(doc.id), data=json.dumps(dict(name='update name')),
                           content_type='application/json')

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'
        assert obj['data']['name'] == 'update name'

    def test_should_success_delete_topics(self):
        doc = Topics(name=fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None))
        db.session.add(doc)
        db.session.commit()

        res = self.app.delete('/topics/' + str(doc.id))

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'

    def test_should_not_found_delete_topics(self):
        res = self.app.delete('/topics/10000000')

        obj = json.loads(res.data)

        assert res.status_code == 404
        assert obj['status'] == 'error'
        assert obj['error'] == 'not found'

        res2 = self.app.delete('/topics/invalid')

        obj2 = json.loads(res.data)

        assert res2.status_code == 404
        assert obj2['status'] == 'error'
        assert obj2['error'] == 'not found'


if __name__ == '__main__':
    unittest.main()
