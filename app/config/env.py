import os

DATABASE_URL: str = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise Exception('DATABASE_URL environment variable is not defined')

AUTH_JWT_SECRET: str = os.getenv('AUTH_JWT_SECRET')
if not AUTH_JWT_SECRET:
    raise Exception('AUTH_JWT_SECRET environment variable is not defined')

API_PREFIX: str = os.getenv('API_PREFIX', '/api')
