from abc import ABCMeta, abstractmethod

from app.domain.usecases.index import GetProfile


class GetAccountByIdRepository(metaclass=ABCMeta):
    Output = GetProfile.Output

    @abstractmethod
    async def get_by_id(self, account_id: str) -> Output:
        return
