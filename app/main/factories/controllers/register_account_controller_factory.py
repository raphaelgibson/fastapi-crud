from app.main.factories.index import make_db_register_account
from app.presentation.controllers.index import RegisterAccountController


def make_register_account_controller() -> RegisterAccountController:
    return RegisterAccountController(make_db_register_account())
