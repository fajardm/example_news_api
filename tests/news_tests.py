import random
import unittest
from apps.news.news_model import News
from apps.topics.topics_model import Topics
from apps.factory import create_app
from datetime import datetime
from faker import Faker
from flask import json
from helpers.database import db

fake = Faker()


def create_topic(name):
    topic = Topics(name=name)
    db.session.add(topic)
    db.session.commit()

    return topic


class NewsTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        News.query.delete()
        Topics.query.delete()

    def test_should_success_get_index(self):
        topic1 = create_topic('topic1')
        topic2 = create_topic('topic2')

        doc1 = News(
            title=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            description=fake.text(),
            status=random.choice(['draft', 'publish'])
        )
        doc1.topics.append(topic1)
        db.session.add(doc1)
        db.session.commit()

        doc2 = News(
            title=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            description=fake.text(),
            deleted_at=datetime.utcnow()
        )
        doc2.topics.append(topic2)
        db.session.add(doc2)
        db.session.commit()

        res = self.app.get('/news')

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'
        assert len(obj['data']) == 2

        res2 = self.app.get('/news?status=deleted')

        obj2 = json.loads(res2.data)

        assert res2.status_code == 200
        assert obj2['status'] == 'success'
        assert len(obj2['data']) == 1

        res3 = self.app.get('/news?topics=topic1')

        obj3 = json.loads(res3.data)

        assert res3.status_code == 200
        assert obj3['status'] == 'success'
        assert len(obj3['data']) == 1

    def test_should_success_post_news(self):
        topic = Topics(name='topic 1')
        db.session.add(topic)
        db.session.commit()

        res = self.app.post('/news', data=json.dumps(dict(
            title='title 1',
            description='description 1',
            topics=[topic.id]
        )), content_type='application/json')

        obj = json.loads(res.data)

        assert res.status_code == 201
        assert obj['status'] == 'success'
        assert obj['data']['title'] == 'title 1'
        assert obj['data']['description'] == 'description 1'
        assert obj['data']['status'] == 'draft'

    def test_should_error_validation_post_news(self):
        res = self.app.post('/news')

        obj = json.loads(res.data)

        assert res.status_code == 400
        assert obj['status'] == 'fail'
        assert obj['data']['validations']['title'] is not None
        assert obj['data']['validations']['description'] is not None

    def test_should_success_get_news(self):
        doc = News(
            title=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            description=fake.text(),
            status=random.choice(['draft', 'publish'])
        )
        db.session.add(doc)
        db.session.commit()

        res = self.app.get('/news/' + str(doc.id))

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'
        assert obj['data']['title'] == doc.title
        assert obj['data']['description'] == doc.description
        assert obj['data']['status'] == doc.status

    def test_should_not_found_get_news(self):
        res = self.app.get('/news/10000000')

        obj = json.loads(res.data)

        assert res.status_code == 404
        assert obj['status'] == 'error'
        assert obj['error'] == 'not found'

        res2 = self.app.get('/news/invalid')

        obj2 = json.loads(res.data)

        assert res2.status_code == 404
        assert obj2['status'] == 'error'
        assert obj2['error'] == 'not found'

    def test_should_success_put_news(self):
        doc = News(
            title=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            description=fake.text(),
            status=random.choice(['draft', 'publish'])
        )
        db.session.add(doc)
        db.session.commit()

        res = self.app.put('/news/' + str(doc.id), data=json.dumps(dict(
            title='update title',
            description='update description',
            status='publish'
        )), content_type='application/json')

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'
        assert obj['data']['title'] == 'update title'
        assert obj['data']['description'] == 'update description'
        assert obj['data']['status'] == 'publish'

    def test_should_success_delete_news(self):
        doc = News(
            title=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            description=fake.text(),
            status=random.choice(['draft', 'publish'])
        )
        db.session.add(doc)
        db.session.commit()

        res = self.app.delete('/news/' + str(doc.id))

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'

    def test_should_not_found_delete_news(self):
        res = self.app.delete('/news/10000000')

        obj = json.loads(res.data)

        assert res.status_code == 404
        assert obj['status'] == 'error'
        assert obj['error'] == 'not found'

        res2 = self.app.delete('/news/invalid')

        obj2 = json.loads(res.data)

        assert res2.status_code == 404
        assert obj2['status'] == 'error'
        assert obj2['error'] == 'not found'


if __name__ == '__main__':
    unittest.main()
