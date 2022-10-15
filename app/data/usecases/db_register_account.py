from app.data.protocols.index import RegisterAccountRepository
from app.domain.usecases.index import RegisterAccount


class DbRegisterAccount(RegisterAccount):
    def __init__(self, register_account_repository: RegisterAccountRepository):
        self.register_account_repository = register_account_repository

    async def register(self, data: RegisterAccount.Input) -> RegisterAccount.Output:
        account = await self.register_account_repository.register(
            RegisterAccountRepository.Input(
                name=data.name,
                email=data.email,
                password=data.password
            )
        )

        return RegisterAccount.Output(id=account.id, name=account.name, email=account.email)
