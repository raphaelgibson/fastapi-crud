from app.data.protocols.index import GetAccountByIdRepository
from app.domain.usecases.index import GetProfile


class DbGetProfile(GetProfile):
    def __init__(self, get_account_by_id_repository: GetAccountByIdRepository):
        self.get_account_by_id_repository = get_account_by_id_repository

    async def get(self, account_id: str) -> GetProfile.Output:
        account = await self.get_account_by_id_repository.get_by_id(account_id)

        if account is None:
            return account

        return GetProfile.Output(id=account.id, name=account.name, email=account.email)
