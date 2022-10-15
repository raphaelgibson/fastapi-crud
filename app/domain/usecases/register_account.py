from abc import ABCMeta, abstractmethod

from pydantic import BaseModel

from app.domain.models.index import AccountModel


class RegisterAccountInput(BaseModel):
    name: str
    email: str
    password: str


class RegisterAccount(metaclass=ABCMeta):
    Input = RegisterAccountInput
    Output = AccountModel

    @abstractmethod
    async def register(self, data: Input) -> Output:
        return
