from abc import ABCMeta, abstractmethod

from app.domain.usecases.index import UpdateProfile


class UpdateAccountRepository(metaclass=ABCMeta):
    Output = UpdateProfile.Output

    @abstractmethod
    async def update(self, account_id: str, name: str) -> Output:
        return
