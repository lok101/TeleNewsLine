from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///C:/Users/loks1/python/TeleNewsLine/db/Users.db')
async_session = sessionmaker(engine, expire_on_commit=False)
session = Session(bind=engine)
Base = declarative_base()
