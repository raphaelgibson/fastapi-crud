from app.data.usecases.index import DbUpdateProfile
from app.infra.sqlalchemy.index import AccountSQLAlchemyRepository


def make_db_update_profile() -> DbUpdateProfile:
    account_sqlalchemy_repository = AccountSQLAlchemyRepository()

    return DbUpdateProfile(account_sqlalchemy_repository)
