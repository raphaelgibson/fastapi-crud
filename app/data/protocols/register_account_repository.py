from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class RegisterAccountRepositoryInput(BaseModel):
    name: str
    email: str
    password: str


class RegisterAccountRepositoryOutput(BaseModel):
    name: str
    email: str


class RegisterAccountRepository(metaclass=ABCMeta):
    Input = RegisterAccountRepositoryInput
    Output = RegisterAccountRepositoryOutput

    @abstractmethod
    async def register(self, account: Input) -> Output:
        return
