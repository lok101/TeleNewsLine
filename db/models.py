from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship

from db.base import Base, engine

user_channel = Table(
    'user_channel', Base.metadata,
    Column('user_id', Integer(), ForeignKey("users.id")),
    Column('channel_id', Integer(), ForeignKey("channels.id"))
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Channel(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    users = relationship("User", secondary=user_channel, backref="channels")


Base.metadata.create_all(engine)
