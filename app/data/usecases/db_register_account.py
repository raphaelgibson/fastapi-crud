from app.data.protocols.index import CheckAccountByEmailRepository, Hasher, RegisterAccountRepository
from app.domain.usecases.index import RegisterAccount


class DbRegisterAccount(RegisterAccount):
    def __init__(
        self,
        check_account_by_email_repository: CheckAccountByEmailRepository,
        hasher: Hasher,
        register_account_repository: RegisterAccountRepository
    ):
        self.check_account_by_email_repository = check_account_by_email_repository
        self.hasher = hasher
        self.register_account_repository = register_account_repository

    async def register(self, data: RegisterAccount.Input) -> RegisterAccount.Output | None:
        exists = await self.check_account_by_email_repository.check_by_email(data.email)

        if exists:
            return None

        hashed_password = await self.hasher.hash(data.password)

        account = await self.register_account_repository.register(
            RegisterAccountRepository.Input(
                name=data.name,
                email=data.email,
                password=hashed_password
            )
        )

        return RegisterAccount.Output(id=account.id, name=account.name, email=account.email)
