# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import Schema, fields, EXCLUDE
from marshmallow import post_load
from sweetrpg_library_model.model.author import Author
import logging


class AuthorDBSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_object(self, data, **kwargs):
        logging.debug("data: %s, kwargs: %s", data, kwargs)
        return Author(**data)

    id = fields.Str()  # as_string=True, dump_only=True)
    name = fields.Str(required=True)  # , load_only=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
    deleted_at = fields.DateTime(allow_none=True)
    # volumes = fields.List(fields.Str())
