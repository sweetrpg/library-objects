# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from marshmallow import post_load
from sweetrpg_library_model.model.volume_property import VolumeProperty
from sweetrpg_db.schema.base import BaseSchema
import logging


class VolumePropertySchema(BaseSchema):
    @post_load
    def make_object(self, data, **kwargs):
        logging.info("data: %s", data)
        return VolumeProperty(**data)

    name = fields.String(required=True)  # , load_only=True)
    value = fields.String(required=True)  # , load_only=True)
    kind = fields.String(allow_none=True)  # , load_only=True)
    # TODO: volume
