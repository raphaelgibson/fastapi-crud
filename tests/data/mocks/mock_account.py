from app.data.protocols.index import RegisterAccountRepository


class RegisterAccountRepositorySpy(RegisterAccountRepository):
    result = {'name': 'any_name', 'email': 'any_email'}
    register_account_input: RegisterAccountRepository.Input

    async def register(self, account: RegisterAccountRepository.Input) -> RegisterAccountRepository.Output:
        self.register_account_input = account

        return RegisterAccountRepository.Output(**self.result)
