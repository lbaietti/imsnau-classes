import unittest 
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_code(self):
        resposta = self.client.get("/")
        self.asserEqual(resposta.status_code, 200)

