# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from marshmallow import post_load
from sweetrpg_library_model.model.author import Author
import logging
from sweetrpg_db.schema.base import BaseDBSchema


class AuthorDBSchema(BaseDBSchema):
    @post_load
    def make_object(self, data, **kwargs):
        logging.debug("data: %s, kwargs: %s", data, kwargs)
        return Author(**data)

    name = fields.Str(required=True)  # , load_only=True)
    volumes = fields.List(fields.Str())
