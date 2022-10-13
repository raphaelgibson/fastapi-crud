from typing import Any

from app.presentation.errors.index import ServerError
from app.presentation.protocols.index import HttpResponse


def ok(body: Any) -> HttpResponse:
    return HttpResponse(status_code=200, body=body)


def server_error() -> HttpResponse:
    return HttpResponse(status_code=500, body=ServerError().__str__())