
from app.data.protocols.index import RegisterAccountRepository
from app.infra.sqlalchemy.entities.account import Account
from app.infra.sqlalchemy.helpers.connection import SessionLocal


class AccountSQLAlchemyRepository(RegisterAccountRepository):
    async def register(self, data: RegisterAccountRepository.Input) -> RegisterAccountRepository.Output:
        db = SessionLocal()
        db_account = Account(name=data.name, email=data.email, password=data.password)
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        db.close()

        return db_account
