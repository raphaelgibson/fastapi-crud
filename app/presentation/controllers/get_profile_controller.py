import logging

from app.presentation.helpers.index import ok, server_error
from app.presentation.protocols.index import Controller, HttpResponse
from app.domain.usecases.index import GetProfile


class GetProfileController(Controller):
    def __init__(self, get_profile: GetProfile):
        self.get_profile = get_profile

    async def handle(self, request: dict) -> HttpResponse:
        try:
            account = await self.get_profile.get(request['account_id'])

            return ok(account)
        except Exception as error:
            logging.log(40, error)

            return server_error()
