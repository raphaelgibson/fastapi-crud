import logging

from app.presentation.helpers.index import ok, server_error
from app.presentation.protocols.index import Controller, HttpResponse
from app.domain.usecases.index import DeleteAccount


class DeleteAccountController(Controller):
    def __init__(self, delete_account: DeleteAccount):
        self.delete_account = delete_account

    async def handle(self, request: dict) -> HttpResponse:
        try:
            await self.delete_account.delete(request['account_id'])

            return ok({'message': 'Account deleted'})
        except Exception as error:
            logging.log(40, error)

            return server_error()
