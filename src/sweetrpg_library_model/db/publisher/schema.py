# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_model.model.publisher import Publisher
from sweetrpg_model_core.schema.base import BaseSchema


class PublisherSchema(BaseSchema):
    model_class = Publisher

    name = fields.String(required=True)  # , load_only=True)
