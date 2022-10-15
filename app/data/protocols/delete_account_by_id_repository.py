from abc import ABCMeta, abstractmethod


class DeleteAccountByIdRepository(metaclass=ABCMeta):
    @abstractmethod
    async def delete_by_id(self, account_id: str) -> None:
        return
