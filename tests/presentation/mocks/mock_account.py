from app.domain.usecases.index import DeleteAccount, GetProfile, RegisterAccount, UpdateProfile


class RegisterAccountSpy(RegisterAccount):
    result = {'id': 'any_id', 'name': 'any_name', 'email': 'any_email'}
    register_account_input: RegisterAccount.Input

    async def register(self, account: RegisterAccount.Input) -> RegisterAccount.Output:
        self.register_account_input = account

        return RegisterAccount.Output(**self.result)


class GetProfileSpy(GetProfile):
    result = {'id': 'any_id', 'name': 'any_name', 'email': 'any_email'}
    account_id: str

    async def get(self, account_id: str) -> GetProfile.Output:
        self.account_id = account_id

        return GetProfile.Output(**self.result)


class UpdateProfileSpy(UpdateProfile):
    result = {'id': 'any_id', 'name': 'any_name', 'email': 'any_email'}
    account_id: str
    name: str

    async def update(self, account_id: str, name: str) -> UpdateProfile.Output:
        self.account_id = account_id
        self.name = name

        return UpdateProfile.Output(**self.result)


class DeleteAccountSpy(DeleteAccount):
    result = None
    account_id: str

    async def delete(self, account_id: str) -> None:
        self.account_id = account_id

        return self.result
