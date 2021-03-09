from fastapi import Request, APIRouter, Depends, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse

from app.config.auth_security import verify_auth
from app.schemas.auth_schema import AuthData

pages_router = FastAPI()

templates = Jinja2Templates(directory='../pages')


@pages_router.get('/login', response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse('login.html', context={'request': request})


@pages_router.get('/signup', response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse('signup.html', context={'request': request})


@pages_router.get('/account', response_class=HTMLResponse)
def account_page(request: Request, auth_data: AuthData = Depends(verify_auth)):
    return templates.TemplateResponse('account.html', context={'request': request, 'user': auth_data.user})


@pages_router.get('/account/options', response_class=HTMLResponse)
def account_options_page(request: Request, auth_data: AuthData = Depends(verify_auth)):
    return templates.TemplateResponse('account-options.html', context={'request': request, 'user': auth_data.user})


@pages_router.exception_handler(HTTPException)
def custom_http_exception_handler(request, exc):
    return RedirectResponse('/login')
