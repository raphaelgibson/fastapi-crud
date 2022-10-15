from app.data.usecases.index import DbRegisterAccount
from app.infra.criptography.index import BcryptAdapter
from app.infra.sqlalchemy.index import AccountSQLAlchemyRepository


def make_db_register_account() -> DbRegisterAccount:
    account_sqlalchemy_repository = AccountSQLAlchemyRepository()
    bcrypt_adapter = BcryptAdapter()

    return DbRegisterAccount(account_sqlalchemy_repository, bcrypt_adapter, account_sqlalchemy_repository)
