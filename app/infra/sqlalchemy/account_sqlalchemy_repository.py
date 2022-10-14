
from app.data.protocols.index import RegisterAccountRepository
from app.infra.sqlalchemy.entities.account import Account
from app.infra.sqlalchemy.helpers.connection import SessionLocal


class AccountSQLAlchemyRepository(RegisterAccountRepository):
    async def register(self, account: RegisterAccountRepository.Input) -> RegisterAccountRepository.Output:
        db = SessionLocal()

        db_account = Account(
            name=account.name,
            email=account.email,
            password=account.password
        )
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        db.close()

        return db_account
