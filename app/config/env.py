import os

DATABASE_URL: str = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise Exception('DATABASE_URL environment variable is not defined')

API_PREFIX: str = os.getenv('API_PREFIX') or ''

DEBUG: bool = bool(os.getenv('DEBUG')) or False

RELOAD: bool = bool(os.getenv('RELOAD')) or False

PORT: int = int(os.getenv('PORT')) or 8000
