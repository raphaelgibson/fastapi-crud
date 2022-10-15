from app.data.protocols.index import UpdateAccountRepository
from app.domain.usecases.index import UpdateProfile


class DbUpdateProfile(UpdateProfile):
    def __init__(self, update_account_repository: UpdateAccountRepository):
        self.update_account_repository = update_account_repository

    async def update(self, account_id: str, name: str) -> UpdateProfile.Output:
        account = await self.update_account_repository.update(account_id, name)

        return UpdateProfile.Output(id=account.id, name=account.name, email=account.email)
