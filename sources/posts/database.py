from collections.abc import Sequence

from classic.components import component
from sqlalchemy import and_
from sqlalchemy.orm import Session

from .models import Author
from .schemas import AuthorForCreate, AuthorForSearch

@component
class AuthorRepo:
    session: Session

    def get_author(self, author: AuthorForSearch) -> Sequence:
        filters = []
        if author.id is not None:
            filters.append(Author.id == author.id)
        if author.name:
            filters.append(Author.name == author.name)
        if author.phone:
            filters.append(Author.phone == author.phone)

        authors = self.session.query(Author)
        if filters:
            authors = authors.filter(and_(*filters))
        return [
            {column.name: getattr(author, column.name) for column in author.__table__.columns}
            for author in authors
        ]

    def create(self, author: AuthorForCreate) -> None:
        _author = Author(
            name=author.name,
            phone=author.phone
        )
        self.session.add(_author)