from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class UpdateProfileOutput(BaseModel):
    name: str
    email: str


class UpdateProfile(metaclass=ABCMeta):
    Output = UpdateProfileOutput

    @abstractmethod
    async def update(self, account_id: str, name: str) -> Output:
        return
