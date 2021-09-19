# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields, INCLUDE
from marshmallow import post_load
from sweetrpg_library_model.model.review import Review
from sweetrpg_db.schema.base import BaseDBSchema
import logging


class ReviewDBSchema(BaseDBSchema):
    class Meta:
        unknown = INCLUDE

    @post_load
    def make_object(self, data, **kwargs):
        logging.info("data: %s", data)
        return Review(**data)

    title = fields.String(required=True)  # , load_only=True)
    text = fields.String(required=True)  # , load_only=True)
