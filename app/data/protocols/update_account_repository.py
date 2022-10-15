from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class UpdateAccountRepositoryOutput(BaseModel):
    name: str
    email: str


class UpdateAccountRepository(metaclass=ABCMeta):
    Output = UpdateAccountRepositoryOutput

    @abstractmethod
    async def update(self, account_id: str, name: str) -> Output:
        return
