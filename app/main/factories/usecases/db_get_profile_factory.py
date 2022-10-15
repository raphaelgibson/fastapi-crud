from app.data.usecases.index import DbGetProfile
from app.infra.sqlalchemy.index import AccountSQLAlchemyRepository


def make_db_get_profile() -> DbGetProfile:
    account_sqlalchemy_repository = AccountSQLAlchemyRepository()

    return DbGetProfile(account_sqlalchemy_repository)
