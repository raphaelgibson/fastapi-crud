from abc import ABCMeta, abstractmethod


class DeleteAccount(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, account_id: str) -> None:
        return
