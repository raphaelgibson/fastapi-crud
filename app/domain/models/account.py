from pydantic import BaseModel


class AccountModel(BaseModel):
    id: str
    name: str
    email: str
