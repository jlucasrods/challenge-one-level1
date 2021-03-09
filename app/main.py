import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config.env import API_PREFIX
from app.config.api_router import api_router
from app.routers.pages_router import pages_router

app = FastAPI(title='Challenge One', version='0.0.1')

app.include_router(router=api_router, prefix=API_PREFIX)

app.mount('/static', StaticFiles(directory='../static'), name='static')

app.mount('/', pages_router, name='pages')

if __name__ == '__main__':
    uvicorn.run('app.main:app', reload=True, debug=True)
