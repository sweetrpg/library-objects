# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import Schema, fields, EXCLUDE
from marshmallow import post_load
from sweetrpg_library_model.model.volume import Volume

# from ..utils import to_datetime, to_timestamp
import logging


class VolumeDBSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_object(self, data, **kwargs):
        logging.info("data: %s", data)
        return Volume(**data)

    id = fields.String()  # as_string=True, dump_only=True)
    name = fields.String(required=True)  # , load_only=True)
    slug = fields.String(required=True)  # , load_only=True)
    isbn = fields.String(allow_none=True)  # , load_only=True)
    system = fields.String(required=True)  # , load_only=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
    deleted_at = fields.DateTime(allow_none=True)
    # created_at = fields.Function(serialize=to_timestamp, deserialize=to_datetime, required=True)
    # updated_at = fields.Integer(required=True)
    # deleted_at = fields.Integer(allow_none=True)
    # authors = fields.List(fields.String())
