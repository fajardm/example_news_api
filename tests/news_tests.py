# import os
# import unittest
# import tempfile
# import run
#
#
# class NewsTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#         flaskr.app.testing = True
#         self.app = flaskr.app.test_client()
#         with flaskr.app.app_context():
#             flaskr.init_db()
#
#     def tearDown(self):
#         os.close(self.db_fd)
#         os.unlink(flaskr.app.config['DATABASE'])
#
#
# if __name__ == '__main__':
#     unittest.main()
