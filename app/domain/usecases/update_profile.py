from abc import ABCMeta, abstractmethod

from app.domain.models.index import AccountModel


class UpdateProfile(metaclass=ABCMeta):
    Output = AccountModel

    @abstractmethod
    async def update(self, account_id: str, name: str) -> Output:
        return
