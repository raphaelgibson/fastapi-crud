from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class GetAccountByIdRepositoryOutput(BaseModel):
    name: str
    email: str


class GetAccountByIdRepository(metaclass=ABCMeta):
    Output = GetAccountByIdRepositoryOutput

    @abstractmethod
    async def get_by_id(self, account_id: str) -> Output:
        return
