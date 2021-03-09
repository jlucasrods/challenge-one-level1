import unittest
from fastapi.testclient import TestClient

from app.main import app
from tests.fixture.credentials import *
from tests.fixture.user import build_user

client = TestClient(app)


class test_auth_router(unittest.TestCase):

    def setUp(self) -> None:
        client.post('/api/users', json=build_user())

    def test_get(self):
        """When request get then response not allowed"""
        response = client.get('/api/auth')
        self.assertEqual(response.status_code, 405)

    def test_post_no_credentials(self):
        """When request post no credentials then response unprocessable entity"""
        response = client.post('/api/auth', json=build_no_credentials())
        self.assertEqual(response.status_code, 422)

    def test_post_invalid_credentials(self):
        """When request post invalid credentials then response unauthorized"""
        response = client.post('/api/auth', json=build_invalid_credentials())
        self.assertEqual(response.status_code, 401)

    def test_post_valid_credentials_email(self):
        """When request post valid credentials with email then response successfully and returns token"""
        response = client.post('/api/auth', json=build_credentials_with_email())
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(), None)

    def test_post_valid_credentials_cpf(self):
        """When request post valid credentials with CPF then response successfully and returns token"""
        response = client.post('/api/auth', json=build_credentials_with_cpf())
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(), None)

    def test_post_valid_credentials_pis(self):
        """When request post valid credentials with PIS then response successfully and returns token"""
        response = client.post('/api/auth', json=build_credentials_with_pis())
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(), None)
