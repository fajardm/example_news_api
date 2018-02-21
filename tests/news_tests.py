import random
import unittest
from apps.news.news_model import News
from apps.factory import create_app
from faker import Faker
from flask import json
from helpers.database import db

fake = Faker()


class NewsTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        News.query.delete()

    def test_should_success_get_index(self):
        res = self.app.get('/news')

        obj = json.loads(res.data)

        assert res.status_code == 200
        assert obj['status'] == 'success'

    def test_should_success_post_news(self):
        res = self.app.post('/news', data=dict(
            title='title 1',
            description='description 1'
        ))

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

        res = self.app.put('/news/' + str(doc.id), data=dict(
            title='update title',
            description='update description',
            status='publish'
        ))

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

        # res2 = self.app.delete('/news/invalid')
        #
        # obj2 = json.loads(res.data)
        #
        # assert res2.status_code == 404
        # assert obj2['status'] == 'error'
        # assert obj2['error'] == 'not found'


if __name__ == '__main__':
    unittest.main()
