import falcon
from classic.components import component
from classic.operations import operation

from .schemas import (
    AuthorForCreate,
    AuthorForSearch,
    ChannelForCreate,
    ChannelForSearch,
    PostForCreate,
    Post,
)
from .database import (
    AuthorRepo,
    ChannelRepo,
    PostRepo,
)


@component
class AuthorResource:
    author_repo: AuthorRepo

    @operation
    def on_get(self, req, resp):
        params = req.params
        author = AuthorForSearch.model_validate(params)
        response_data = self.author_repo.get_authors(author=author)
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.media = [
            {
                "id": obj.id,
                "name": obj.name,
                "phone": obj.phone,
                "channels": [
                    {
                        "id": channel.id,
                        "title": channel.title,
                    }
                    for channel in obj.channels
                ]
            }
            for obj in response_data
        ]


    @operation
    def on_post(self, req, resp):
        params = req.media
        author = AuthorForCreate.model_validate(params)
        self.author_repo.create(author=author)
        resp.status = falcon.HTTP_200


@component
class ChannelResource:
    channel_repo: ChannelRepo

    @operation
    def on_get(self, req, resp):
        params = req.params
        channel = ChannelForSearch.model_validate(params)
        response_data = self.channel_repo.get_channels(channel=channel)
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.media = [
            {
                "id": obj.id,
                "tile": obj.title,
                "login_data": obj.login_data,
                "posts": [
                    {
                        "id": post.id,
                        "title": post.title,
                    }
                    for post in obj.posts
                ]
            }
            for obj in response_data
        ]

    @operation
    def on_post(self, req, resp):
        params = req.media
        channel = ChannelForCreate.model_validate(params)
        self.channel_repo.create(channel=channel)
        resp.status = falcon.HTTP_200


@component
class PostResource:
    post_repo: PostRepo

    @operation
    def on_get(self, req, resp):
        params = req.params
        post = Post.model_validate(params)
        response_data = self.post_repo.get_posts(post=post)
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.media = [
            {
                "id": obj.id,
                "title": obj.title,
                "text": obj.text,
                "channel": obj.channel_id
            }
            for obj in response_data
        ]

    @operation
    def on_post(self, req, resp):
        params = req.media
        post = PostForCreate.model_validate(params)
        self.post_repo.create(post=post)
        resp.status = falcon.HTTP_200