# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_model_core.schema.base import BaseSchema
import logging


class VolumeSchema(BaseSchema):
    model_class = Volume

    name = fields.String(required=True)  # , load_only=True)
    slug = fields.String(required=True)  # , load_only=True)
    system = fields.String(required=True)  # , load_only=True)
    # authors = fields.List(fields.String())
