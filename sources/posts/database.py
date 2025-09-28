from collections.abc import Sequence

from classic.components import component
from classic.operations import operation
from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload

from .models import Author, Channel, Post
from .schemas import (
    AuthorForCreate,
    AuthorForSearch,
    ChannelForCreate,
    ChannelForSearch,
    PostForCreate,
)


@component
class AuthorRepo:
    session: Session

    @operation
    def get_authors(self, author: AuthorForSearch) -> Sequence:
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

    @operation
    def create(self, author: AuthorForCreate) -> None:
        _author = Author(
            name=author.name,
            phone=author.phone
        )
        self.session.add(_author)


@component
class ChannelRepo:
    session: Session

    @operation
    def get_channels(self, channel: ChannelForSearch) -> Sequence:
        filters = self.add_filters(channel=channel)
        channels = self.session.query(Channel)
        if filters:
            channels = channels.filter(and_(*filters))
        return channels.options(joinedload(Channel.posts)).all()

    @staticmethod
    def add_filters(channel: ChannelForSearch) -> list:
        filters = []
        if channel.id is not None:
            filters.append(Channel.id == channel.id)
        if channel.title:
            filters.append(Channel.title == channel.title)
        return filters

    @operation
    def create(self, channel: ChannelForCreate) -> None:
        channel = Channel(
            title=channel.title,
            login_data=channel.login_data,
            author_id=channel.author_id
        )
        self.session.add(channel)


@component
class PostRepo:
    session: Session

    @operation
    def get_posts(self, post: Post) -> Sequence:
        filters = self.add_filters(post=post)
        posts = self.session.query(Post)
        if filters:
            posts = posts.filter(and_(*filters))
        return posts.options(joinedload(Post.channel)).all()

    @staticmethod
    def add_filters(post: Post) -> list:
        filters = []
        if post.id is not None:
            filters.append(Post.id == post.id)
        if post.title:
            filters.append(Post.title == post.title)
        return filters

    @operation
    def create(self, post: PostForCreate) -> None:
        post = Post(
            title=post.title,
            text=post.text,
            channel_id=post.channel_id
        )
        self.session.add(post)
