from fastapi import APIRouter, Request

from app.main.adapters.fastapi_adapter import adapt_route
from app.main.factories.controllers.index import make_register_account_controller


router = APIRouter()


@router.post("/signup", summary="SignUp", tags=["Account"])
async def router_login(request: Request):
    return await adapt_route(make_register_account_controller(), request)
