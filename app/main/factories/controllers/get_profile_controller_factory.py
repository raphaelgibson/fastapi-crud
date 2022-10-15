from app.main.factories.index import make_db_get_profile
from app.presentation.controllers.index import GetProfileController


def make_get_profile_controller() -> GetProfileController:
    return GetProfileController(make_db_get_profile())
