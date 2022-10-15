from fastapi import APIRouter, Request

from app.main.adapters.fastapi_adapter import adapt_route
from app.main.factories.controllers.index import (
    make_register_account_controller,
    make_get_profile_controller,
    make_update_profile_controller,
    make_delete_account_controller
)


router = APIRouter()


@router.post("/signup", summary="SignUp", tags=["Account"])
async def router_register_account(request: Request):
    return await adapt_route(make_register_account_controller(), request)


@router.get("/profile", summary="Get profile", tags=["Account"])
async def router_get_profile(account_id: str, request: Request):
    return await adapt_route(make_get_profile_controller(), request)


@router.put("/profile/{account_id}", summary="Update profile by ID", tags=["Account"])
async def router_update_profile(account_id: str, request: Request):
    return await adapt_route(make_update_profile_controller(), request)


@router.delete("/account/{account_id}", summary="Delete account by ID", tags=["Account"])
async def router_delete_account(account_id: str, request: Request):
    return await adapt_route(make_delete_account_controller(), request)
