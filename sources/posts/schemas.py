from typing import List, Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    text: str


class Channel(BaseModel):
    title: str
    login_data: str
    id: int
    posts: List[Post] = []


class AuthorForCreate(BaseModel):
    name: str
    phone: Optional[str] = None
    channels: List[Channel] = []


class AuthorForSearch(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    id: Optional[int] = None
    channels: List[Channel] = []