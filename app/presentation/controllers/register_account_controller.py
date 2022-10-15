import logging

from app.presentation.errors.index import EmailAlreadyExistsError, MissingParamError
from app.presentation.helpers.index import bad_request, conflict, created, server_error
from app.presentation.protocols.index import Controller, HttpResponse
from app.domain.usecases.index import RegisterAccount


class RegisterAccountController(Controller):
    def __init__(self, register_account: RegisterAccount):
        self.register_account = register_account

    async def handle(self, request: dict) -> HttpResponse:
        try:
            required_fields = ['name', 'email', 'password']

            for field in required_fields:
                if field not in request or not request[field]:
                    return bad_request(MissingParamError(field))

            account = await self.register_account.register(
                RegisterAccount.Input(
                    name=request['name'],
                    email=request['email'],
                    password=request['password']
                )
            )

            if account is None:
                return conflict(EmailAlreadyExistsError())

            return created(account)
        except Exception as error:
            logging.log(40, error)

            return server_error()
