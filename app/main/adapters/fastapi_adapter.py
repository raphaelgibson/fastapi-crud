from fastapi import Request
from fastapi.responses import JSONResponse

from app.presentation.protocols.index import Controller


async def adapt_route(controller: Controller, request: Request):
    http_request = request.path_params

    if request.method.lower() != "get":
        http_request = http_request | await request.json()

    http_response = await controller.handle(http_request)
    success_codes = [200, 201]

    if http_response.status_code in success_codes:
        return JSONResponse(status_code=http_response.status_code, content=http_response.body.__dict__)
    else:
        return JSONResponse(status_code=http_response.status_code, content={"error": http_response.body})
