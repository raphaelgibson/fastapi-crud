from sqlalchemy import Column, Integer, MetaData, String, Table

from app.infra.sqlalchemy.index import Base, engine


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

metadata_obj = MetaData()

account = Table(
    'accounts',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('email', String(100)),
    Column('password', String(50))
)

account.create(engine, checkfirst=True)
