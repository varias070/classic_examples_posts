from typing import Optional
from pydantic import BaseModel


class PostForCreate(BaseModel):
    channel_id: int
    title: str
    text: str


class ChannelForCreate(BaseModel):
    title: str
    login_data: str
    author_id: int


class ChannelForSearch(BaseModel):
    id:  int
    title: Optional[str] = None
    posts: list = []


class AuthorForCreate(BaseModel):
    name: str
    phone: Optional[str] = None


class AuthorForSearch(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    id: Optional[int] = None
