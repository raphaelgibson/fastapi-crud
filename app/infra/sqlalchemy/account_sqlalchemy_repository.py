
from app.data.protocols.index import (
    DeleteAccountByIdRepository, GetAccountByIdRepository, CheckAccountByEmailRepository,
    RegisterAccountRepository, UpdateAccountRepository
)
from app.infra.sqlalchemy.index import Account, SessionLocal


class AccountSQLAlchemyRepository(
    RegisterAccountRepository, GetAccountByIdRepository, CheckAccountByEmailRepository,
    UpdateAccountRepository, DeleteAccountByIdRepository
):
    async def register(self, data: RegisterAccountRepository.Input) -> RegisterAccountRepository.Output:
        db = SessionLocal()
        db_account = Account(name=data.name, email=data.email, password=data.password)
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        db.close()

        return db_account

    async def get_by_id(self, account_id: str) -> GetAccountByIdRepository.Output:
        db = SessionLocal()
        db_account = db.query(Account).filter(Account.id == account_id).one()
        db.close()

        return GetAccountByIdRepository.Output(
            id=db_account.id,
            name=db_account.name,
            email=db_account.email
        )

    async def check_by_email(self, email: str) -> bool:
        db = SessionLocal()

        db_account = db.query(Account).filter(Account.email == email).all()
        db.close()

        return len(db_account) > 0

    async def update(self, account_id: str, name: str) -> UpdateAccountRepository.Output:
        db = SessionLocal()
        db.query(Account).filter(Account.id == account_id).update({Account.name: name})
        db.commit()
        db_account = db.query(Account).filter(Account.id == account_id).one()
        db.close()

        return UpdateAccountRepository.Output(
            id=db_account.id,
            name=db_account.name,
            email=db_account.email
        )

    async def delete_by_id(self, account_id: str) -> None:
        db = SessionLocal()
        db.query(Account).filter(Account.id == account_id).delete()
        db.commit()
        db.close()
