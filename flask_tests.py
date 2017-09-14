import unittest
import json
from index import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get_method_not_allowed(self):
        result = self.app.get('/api/dog_prediction')
        self.assertEqual(result.status_code, 405)

    def test_post_response(self):
        result = self.app.post('/api/dog_prediction',
          data='{"url":"https://s3-eu-west-1.amazonaws.com/rg-human-faces/lfw/Angelina_Jolie/Angelina_Jolie_0001.jpg"}',
          follow_redirects=True)
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['breed'], "American eskimo dog")

if __name__ == '__main__':
    unittest.main()