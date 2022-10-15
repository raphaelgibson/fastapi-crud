from abc import ABCMeta, abstractmethod


class CheckAccountByEmailRepository(metaclass=ABCMeta):
    @abstractmethod
    async def check_by_email(self, email: str) -> bool:
        return
