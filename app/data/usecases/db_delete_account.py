from app.data.protocols.index import DeleteAccountByIdRepository
from app.domain.usecases.index import DeleteAccount


class DbDeleteAccount(DeleteAccount):
    def __init__(self, delete_account_by_id_repository: DeleteAccountByIdRepository):
        self.delete_account_by_id_repository = delete_account_by_id_repository

    async def delete(self, account_id: str) -> None:
        await self.delete_account_by_id_repository.delete_by_id(account_id)
