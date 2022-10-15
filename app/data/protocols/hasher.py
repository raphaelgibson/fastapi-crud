from abc import ABCMeta, abstractmethod


class Hasher(metaclass=ABCMeta):
    @abstractmethod
    async def hash(self, plaintext: str) -> str:
        return
