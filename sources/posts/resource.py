from classic.components import component
from classic.operations import operation

from posts.use_case import (
    CreateAuthor,
    GetAuthor,
    CreateChannel,
    GetChannel,
    GetPost,
    CreateRental
)


@component
class AuthorResource:
    get_author: GetAuthor
    create_author: CreateAuthor

    @operation
    def on_get(self, req, resp):
        params = req.params
        author = self.get_author.run(params)
        resp.media = author

    @operation
    def on_post(self, req, resp):
        params = req.media
        author_id = self.create_author.run(data=params)
        resp.media = author_id


@component
class ChannelResource:
    get_channel: GetChannel
    create_channel: CreateChannel

    @operation
    def on_get(self, req, resp):
        params = req.params
        channel = self.get_channel.run(data=params)
        resp.media = channel

    @operation
    def on_post(self, req, resp):
        params = req.media
        channel_id = self.create_channel.run(params)
        resp.media = channel_id


@component
class PostResource:
    get_post: GetPost

    @operation
    def on_get(self, req, resp):
        post_id = req.params
        post = self.get_post.run(post_id)
        resp.media = post


@component
class RentalResource:
    create_rental: CreateRental

    @operation
    def on_post(self, req, resp):
        params = req.media
        rental_id = self.create_rental.run(data=params)
        resp.media = rental_id
