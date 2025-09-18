import falcon
from classic.components import component
from classic.operations import operation

from .schemas import (
    AuthorForCreate,
    AuthorForSearch,
    ChannelForCreate,
)
from .database import (
    AuthorRepo,
    ChannelRepo,
)


@component
class AuthorResource:
    author_repo: AuthorRepo

    @operation
    def on_get(self, req, resp):
        params = req.params
        author = AuthorForSearch.model_validate(params)
        response_data = self.author_repo.get_author(author=author)
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
    def on_post(self, req, resp):
        params = req.media
        channel = ChannelForCreate.model_validate(params)
        self.channel_repo.create(channel=channel)
        resp.status = falcon.HTTP_200
