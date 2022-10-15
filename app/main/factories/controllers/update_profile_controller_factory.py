from app.main.factories.index import make_db_update_profile
from app.presentation.controllers.index import UpdateProfileController


def make_update_profile_controller() -> UpdateProfileController:
    return UpdateProfileController(make_db_update_profile())
