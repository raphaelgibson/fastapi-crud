from typing import Any

from app.presentation.errors.index import ServerError
from app.presentation.protocols.index import HttpResponse


def ok(body: Any) -> HttpResponse:
    return HttpResponse(status_code=200, body=body)


def created(body: Any) -> HttpResponse:
    return HttpResponse(status_code=201, body=body)


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=400, body=error.__str__())


def not_acceptable(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=406, body=error.__str__())


def conflict(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=409, body=error.__str__())


def server_error() -> HttpResponse:
    return HttpResponse(status_code=500, body=ServerError().__str__())
