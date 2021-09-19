# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from marshmallow import post_load
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_db.db.base import BaseDBSchema
import logging


class VolumeDBSchema(BaseDBSchema):
    @post_load
    def make_object(self, data, **kwargs):
        logging.info("data: %s", data)
        return Volume(**data)

    name = fields.String(required=True)  # , load_only=True)
    slug = fields.String(required=True)  # , load_only=True)
    isbn = fields.String(allow_none=True)  # , load_only=True)
    system = fields.String(required=True)  # , load_only=True)
    # authors = fields.List(fields.String())
