from app.main.factories.index import make_db_delete_account
from app.presentation.controllers.index import DeleteAccountController


def make_delete_account_controller() -> DeleteAccountController:
    return DeleteAccountController(make_db_delete_account())
