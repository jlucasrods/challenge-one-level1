import unittest
from fastapi.testclient import TestClient

from app.main import app
from tests.fixture.credentials import *

client = TestClient(app)


class test_user_router(unittest.TestCase):

    authorization = None

    def test_post_user(self):
        """When request get then response successfully"""
        response = client.post('/api/users', json=build_user())
        print(response)
        self.assertEqual(response.json()['email'], build_user()['email'])

    def test_get_user_me(self):
        """When request get then response successfully"""
        token = client.post('/api/auth', json=build_credentials_with_email()).json()['token']
        self.authorization = {'Authorization': f'Bearer {token}'}
        response = client.get('/api/users/me', headers=self.authorization)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], build_user()['email'])

    def test_delete_user_me(self):
        """When delete user then response successfully"""
        client.delete('/api/users/me', headers=self.authorization)
