from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    phone = Column(String(30), nullable=True)
    channels = relationship("Channel", back_populates="author")

class Channel(Base):
    __tablename__ = "channel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    login_data = Column(Text)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=True)
    author = relationship("Author", back_populates="channels")
    posts = relationship("Post", back_populates="channel")

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    text = Column(Text)
    channel_id = Column(Integer, ForeignKey("channel.id"), nullable=True)
    channel = relationship("Channel", back_populates="posts")
