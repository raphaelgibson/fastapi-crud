from abc import ABCMeta, abstractmethod

from app.domain.models.index import AccountModel


class GetProfile(metaclass=ABCMeta):
    Output = AccountModel

    @abstractmethod
    async def get(self, account_id: str) -> Output:
        return
