import unittest
from apps.factory import create_app
from flask import json


class PingTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()

    def test_get_ping(self):
        res = self.app.get('/ping')
        obj = json.loads(res.data)
        assert obj['status'] == 'success'


if __name__ == '__main__':
    unittest.main()
