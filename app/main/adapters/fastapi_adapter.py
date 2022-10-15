from fastapi import Request
from fastapi.responses import JSONResponse

from app.presentation.protocols.index import Controller


async def adapt_route(controller: Controller, request: Request):
    http_request = request.path_params | request.query_params._dict

    if request.method.lower() != 'get' and request.method.lower() != 'delete':
        http_request = http_request | await request.json()

    http_response = await controller.handle(http_request)
    success_codes = [200, 201]

    if http_response.status_code in success_codes:
        if type(http_response.body) != dict:
            http_response = http_response.body.__dict__

        return JSONResponse(status_code=http_response.status_code, content=http_response.body)
    else:
        return JSONResponse(status_code=http_response.status_code, content={"error": http_response.body})
