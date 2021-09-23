# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from pymodm import fields, MongoModel, EmbeddedMongoModel
from pymongo.operations import IndexModel
from pymongo import ASCENDING


class AuthorDocument(MongoModel):
    """A model object representing an RPG author."""

    class Meta:
        indexes = [
            IndexModel([('name', ASCENDING)],
                       name="author_name"),
        ]
        connection_alias = "default"
        collection_name = "authors"
        ignore_unknown_fields = True
        cascade = True

    name = fields.CharField(min_length=1, max_length=200, required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    deleted_at = fields.DateTimeField(blank=True)
    volumes = fields.ListField(field=fields.ReferenceField('VolumeDocument'))
