from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class RegisterAccountInput(BaseModel):
    name: str
    email: str
    password: str


class RegisterAccountOutput(BaseModel):
    name: str
    email: str


class RegisterAccount(metaclass=ABCMeta):
    Input = RegisterAccountInput
    Output = RegisterAccountOutput

    @abstractmethod
    async def register(self, account: Input) -> Output:
        return
