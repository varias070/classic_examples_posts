from collections.abc import Sequence

from classic.components import component
from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload

from .models import Author, Channel, Post
from .schemas import AuthorForCreate, AuthorForSearch, ChannelForCreate


@component
class AuthorRepo:
    session: Session

    def get_author(self, author: AuthorForSearch) -> Sequence:
        filters = self.add_filters(author=author)
        authors = self.session.query(Author)
        if filters:
            authors = authors.filter(and_(*filters))
        return authors.options(joinedload(Author.channels)).all()

    @staticmethod
    def add_filters(author: AuthorForSearch) -> list:
        filters = []
        if author.id is not None:
            filters.append(Author.id == author.id)
        if author.name:
            filters.append(Author.name == author.name)
        if author.phone:
            filters.append(Author.phone == author.phone)
        return filters

    def create(self, author: AuthorForCreate) -> None:
        _author = Author(
            name=author.name,
            phone=author.phone
        )
        self.session.add(_author)


@component
class ChannelRepo:
    session: Session

    def create(self, channel: ChannelForCreate) -> None:
        channel = Channel(
            title=channel.title,
            login_data=channel.login_data,
            author_id=channel.author_id
        )
        self.session.add(channel)
