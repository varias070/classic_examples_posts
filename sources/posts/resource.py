import json

import falcon
from classic.components import component
from classic.operations import operation

from .schemas import AuthorForCreate, AuthorForSearch
from .database import AuthorRepo


@component
class AuthorResource:
    author_repo: AuthorRepo

    @operation
    def on_get(self, req, resp):
        params = req.params
        author = AuthorForSearch.model_validate(params)
        response_data = self.author_repo.get_author(author=author)
        print(response_data)
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.text = json.dumps(response_data)

    @operation
    def on_post(self, req, resp):
        params = req.params
        author = AuthorForCreate.model_validate(params)
        self.author_repo.create(author=author)
        resp.status = falcon.HTTP_200
