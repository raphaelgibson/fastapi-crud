from abc import ABCMeta, abstractmethod
from typing import Any

from app.presentation.protocols.http import HttpResponse


class Controller(metaclass=ABCMeta):

    @abstractmethod
    async def handle(self, request: Any) -> HttpResponse:
        return
