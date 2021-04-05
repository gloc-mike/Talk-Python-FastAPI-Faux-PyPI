import fastapi
from starlette.requests import Request

from src.viewmodels.account.account_viewmodel import RegisterViewModel
from src.viewmodels.account.login_viewmodel import LoginViewModel
from src.viewmodels.account.register_viewmodel import AccountViewModel

router = fastapi.APIRouter()


@router.get('/account')
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout():
    return {}
