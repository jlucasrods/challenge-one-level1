from tests.fixture.user import build_user


def build_no_credentials():
    return {}


def build_invalid_credentials():
    return {
        'login': 'asdfghjkl',
        'password': 'asdfghjkl'
    }


def build_credentials_with_email():
    user = build_user()
    return {
        'login': user['email'],
        'password': user['password']
    }


def build_credentials_with_cpf():
    user = build_user()
    return {
        'login': user['cpf'],
        'password': user['password']
    }


def build_credentials_with_pis():
    user = build_user()
    return {
        'login': user['pis'],
        'password': user['password']
    }
