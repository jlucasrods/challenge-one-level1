import os
import sys
from typing import List

PYTEST_RUNNING = True if "pytest" in sys.modules else False

DB_URL: str = os.getenv('DB_URL')
if not DB_URL:
    raise Exception('DB_URL environment variable is not defined')

AUTH_SECRET: str = os.getenv('AUTH_SECRET')
if not AUTH_SECRET:
    raise Exception('AUTH_SECRET environment variable is not defined')

CORS_ORIGINS: List[str] = os.getenv('CORS_ORIGINS', '').split(',')
