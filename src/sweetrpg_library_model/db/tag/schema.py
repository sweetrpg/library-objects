# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from marshmallow import post_load
from sweetrpg_library_model.model.tag import Tag
from sweetrpg_db.schema.base import BaseDBSchema
import logging


class TagDBSchema(BaseDBSchema):
    @post_load
    def make_object(self, data, **kwargs):
        logging.info("data: %s", data)
        return Tag(**data)

    name = fields.String(required=True)  # , load_only=True)
