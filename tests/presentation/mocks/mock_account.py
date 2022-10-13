from app.domain.usecases.index import RegisterAccount


class RegisterAccountSpy(RegisterAccount):
    result = {'name': 'any_name', 'email': 'any_email'}
    register_account_input: RegisterAccount.Input

    async def register(self, account: RegisterAccount.Input) -> RegisterAccount.Output:
        self.register_account_input = account

        return RegisterAccount.Output(**self.result)
