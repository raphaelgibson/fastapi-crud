from app.data.usecases.index import DbDeleteAccount
from app.infra.sqlalchemy.index import AccountSQLAlchemyRepository


def make_db_delete_account() -> DbDeleteAccount:
    account_sqlalchemy_repository = AccountSQLAlchemyRepository()

    return DbDeleteAccount(account_sqlalchemy_repository)
