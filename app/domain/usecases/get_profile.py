from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class GetProfileOutput(BaseModel):
    name: str
    email: str


class GetProfile(metaclass=ABCMeta):
    Output = GetProfileOutput

    @abstractmethod
    async def get(self, account_id: str) -> Output:
        return
