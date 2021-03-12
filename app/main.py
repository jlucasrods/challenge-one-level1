import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.config.env import PYTEST_RUNNING
from app.config.router import api_router
from app.config.models import create_all_models
from app.routers.pages import pages_router

create_all_models()

app = FastAPI(title='Challenge', version='0.1.0')

app.include_router(router=api_router, prefix='/api')

if not PYTEST_RUNNING:
    app.mount('/static', StaticFiles(directory='../static'), name='static')
    app.mount('/', pages_router, name='pages')

if __name__ == '__main__':
    uvicorn.run('app.main:app', reload=True, debug=True)
