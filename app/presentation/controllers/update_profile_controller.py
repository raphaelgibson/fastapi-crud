import logging

from app.presentation.helpers.index import ok, server_error
from app.presentation.protocols.index import Controller, HttpResponse
from app.domain.usecases.index import UpdateProfile


class UpdateProfileController(Controller):
    def __init__(self, update_profile: UpdateProfile):
        self.update_profile = update_profile

    async def handle(self, request: dict) -> HttpResponse:
        try:
            account = await self.update_profile.update(request['account_id'], request['name'])

            return ok(account)
        except Exception as error:
            logging.log(40, error)

            return server_error()
