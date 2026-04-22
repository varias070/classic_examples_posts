from dataclasses import dataclass, field


@dataclass
class Post:
    id: int
    title: str
    text: str
    channel_id: int


@dataclass
class Channel:
    id: str
    title: str
    posts: list[Post] = field(default_factory=list)
    login_data: str = None


@dataclass
class Author:
    id: int
    name: str
    phone: str
    channels: list[Channel] = field(default_factory=list)
