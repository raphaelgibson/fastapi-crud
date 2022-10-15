from app.data.usecases.index import DbRegisterAccount
from app.infra.sqlalchemy.index import AccountSQLAlchemyRepository


def make_db_register_account() -> DbRegisterAccount:
    account_sqlalchemy_repository = AccountSQLAlchemyRepository()

    return DbRegisterAccount(account_sqlalchemy_repository)
