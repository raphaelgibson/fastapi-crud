import logging

from app.presentation.errors.index import ProfileNotFoundError
from app.presentation.helpers.index import not_acceptable, ok, server_error
from app.presentation.protocols.index import Controller, HttpResponse
from app.domain.usecases.index import GetProfile


class GetProfileController(Controller):
    def __init__(self, get_profile: GetProfile):
        self.get_profile = get_profile

    async def handle(self, request: dict) -> HttpResponse:
        try:
            profile = await self.get_profile.get(request['account_id'])

            if profile is None:
                return not_acceptable(ProfileNotFoundError())

            return ok(profile)
        except Exception as error:
            logging.log(40, error)

            return server_error()
