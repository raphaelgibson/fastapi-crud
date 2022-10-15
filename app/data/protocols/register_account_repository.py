from abc import ABCMeta, abstractmethod

from app.domain.usecases.index import RegisterAccount


class RegisterAccountRepository(metaclass=ABCMeta):
    Input = RegisterAccount.Input
    Output = RegisterAccount.Output

    @abstractmethod
    async def register(self, data: Input) -> Output:
        return
