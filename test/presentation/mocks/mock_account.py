from app.domain.usecases.index import RegisterAccount


class RegisterAccountSpy(RegisterAccount):
    result = {'email': 'any_email', 'name': 'any_name'}
    register_account_input: RegisterAccount.Input

    async def register(self, account: RegisterAccount.Input) -> RegisterAccount.Output:
        self.register_account_input = account

        return RegisterAccount.Output(**self.result)
