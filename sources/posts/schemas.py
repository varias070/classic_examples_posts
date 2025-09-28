from typing import List, Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    text: Optional[str] = None


class PostForCreate(BaseModel):
    channel_id: int
    title: str
    text: str


class ChannelForCreate(BaseModel):
    title: str
    login_data: str
    author_id: int


class ChannelForSearch(BaseModel):
    title: Optional[str] = None
    login_data: Optional[str] = None
    id: Optional[int] = None
    posts: List[Post] = []


class AuthorForCreate(BaseModel):
    name: str
    phone: Optional[str] = None


class AuthorForSearch(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    id: Optional[int] = None
    channels: Optional[bool] = None
