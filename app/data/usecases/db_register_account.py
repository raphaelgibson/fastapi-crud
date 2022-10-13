from app.data.protocols.index import RegisterAccountRepository
from app.domain.usecases.index import RegisterAccount


class DbRegisterAccount(RegisterAccount):
    def __init__(self, register_account_repository: RegisterAccountRepository):
        self.register_account_repository = register_account_repository

    async def register(self, account: RegisterAccount.Input) -> RegisterAccount.Output:
        new_account = await self.register_account_repository.register(
            RegisterAccountRepository.Input(
                name=account.name,
                email=account.email,
                password=account.password
            )
        )

        return RegisterAccount.Output(
            name=new_account.name,
            email=new_account.email
        )
