from app.config.auth import AUTH_COOKIE_NAME
from app.models.user import UserModel


def test_login_with_invalid_credentials(client, mocker):
    mocker.patch('app.routers.auth.get_by_login', return_value=None)

    response = client.post('/api/auth/login', json={'login': 'invalid login', 'password': 'bla bla bla'})

    assert response.status_code == 401


def test_login(client, mocker):
    mocker.patch('app.routers.auth.get_by_login', return_value=UserModel(id=1, password='1234'))
    mocker.patch('app.routers.auth.verify_password', return_value=True)

    response = client.post('/api/auth/login', json={'login': 'name@email.com', 'password': '1234'})

    assert response.status_code == 200


def test_logout(client):
    response = client.get('/api/auth/logout', json={'login': 'name@email.com', 'password': '1234'})
    assert response.cookies.get(AUTH_COOKIE_NAME) is None
    assert response.status_code == 200
