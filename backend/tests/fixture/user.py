def build_user():
    return {
        'name': 'Name',
        'email': 'example@email.com',
        'cpf': '98130738023',
        'pis': '98503656268',
        'password': 'password',
        'addresses': {
            'country': 'Country',
            'state': 'State',
            'city': 'City',
            'street': 'Street',
            'zip_code': '00000-000',
            'number': 1,
            'complement': 'Complement'
        }
    }


def build_invalid_user():
    return {}


def build_user_with_invalid_cpf():
    user = build_user()
    user['cpf'] = '00000000000'
    return user


def build_user_with_invalid_pis():
    user = build_user()
    user['pis'] = '00000000000'
    return user


def build_user_with_invalid_address():
    user = build_user()
    user['addresses'] = {}
    return user
