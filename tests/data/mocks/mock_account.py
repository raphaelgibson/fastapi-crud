from app.data.protocols.index import (
    DeleteAccountByIdRepository, GetAccountByIdRepository, CheckAccountByEmailRepository,
    RegisterAccountRepository, UpdateAccountRepository
)


class RegisterAccountRepositorySpy(RegisterAccountRepository):
    result = {'id': 'any_id', 'name': 'any_name', 'email': 'any_email'}
    register_account_input: RegisterAccountRepository.Input

    async def register(self, data: RegisterAccountRepository.Input) -> RegisterAccountRepository.Output:
        self.register_account_input = data

        return RegisterAccountRepository.Output(**self.result)


class GetAccountByIdRepositorySpy(GetAccountByIdRepository):
    result = {'id': 'any_id', 'name': 'any_name', 'email': 'any_email'}
    account_id: str

    async def get_by_id(self, account_id: str) -> GetAccountByIdRepository.Output:
        self.account_id = account_id

        return GetAccountByIdRepository.Output(**self.result)


class CheckAccountByEmailRepositorySpy(CheckAccountByEmailRepository):
    result = False
    email: str

    async def check_by_email(self, email: str) -> bool:
        self.email = email

        return self.result


class UpdateAccountRepositorySpy(UpdateAccountRepository):
    result = {'id': 'any_id', 'name': 'any_name', 'email': 'any_email'}
    account_id: str
    name: str

    async def update(self, account_id: str, name: str) -> UpdateAccountRepository.Output:
        self.account_id = account_id
        self.name = name

        return UpdateAccountRepository.Output(**self.result)


class DeleteAccountByIdRepositorySpy(DeleteAccountByIdRepository):
    result = None
    account_id: str

    async def delete_by_id(self, account_id: str) -> None:
        self.account_id = account_id

        return self.result
