from pydantic import BaseModel

from app.presentation.helpers.index import ok, server_error
from app.presentation.protocols.index import Controller, HttpResponse
from app.domain.usecases.index import RegisterAccount


class RegisterAccountRequest(BaseModel):
    name: str
    email: str
    password: str


class RegisterAccountController(Controller):
    Request = RegisterAccountRequest

    def __init__(self, register_account: RegisterAccount):
        self.register_account = register_account

    async def handle(self, request: Request) -> HttpResponse:
        try:
            account = await self.register_account.register(
                RegisterAccount.Input(
                    name=request.name,
                    email=request.email,
                    password=request.password
                )
            )

            return ok(account)
        except Exception:
            return server_error()
