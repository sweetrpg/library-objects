# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_model.model.tag import Tag
from sweetrpg_model_core.schema.base import BaseSchema


class TagSchema(BaseSchema):
    model_class = Tag

    name = fields.String(required=True)  # , load_only=True)
