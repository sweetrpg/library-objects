# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from pymodm import fields, MongoModel, EmbeddedMongoModel
from pymongo.operations import IndexModel
from pymongo import ASCENDING


class VolumeDocument(MongoModel):
    """A mapping object to convert MongoDB data to a Volume object."""

    class Meta:
        indexes = [
            IndexModel([('slug', ASCENDING)],
                       name="volume_slug",
                       unique=True),
            IndexModel([('name', ASCENDING)],
                       name="volume_name"),
            IndexModel([('system', ASCENDING)],
                       name="volume_system")
        ]
        connection_alias = "default"
        collection_name = "volumes"
        ignore_unknown_fields = True
        cascade = True

    name = fields.CharField(min_length=1, max_length=200, required=True)
    slug = fields.CharField(min_length=2, max_length=50, required=True, primary_key=True)
    system = fields.CharField(min_length=1, max_length=20, required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    deleted_at = fields.DateTimeField(blank=True)
    authors = fields.ListField(field=fields.ReferenceField('AuthorDocument', on_delete=fields.ReferenceField.NULLIFY))
    properties = fields.ListField(field=fields.ReferenceField('VolumePropertyDocument'), on_delete=fields.ReferenceField.DELETE)

class VolumePropertyDocument(EmbeddedMongoModel):
    """A mapping object for volume properties."""

    class Meta:
        indexes = [
            IndexModel([('name', ASCENDING)],
                       name="volume_property_name"),
        ]
        connection_alias = "default"
        collection_name = "volume_properties"
        ignore_unknown_fields = True
        cascade = True

    name = fields.CharField(min_length=1, max_length=50, required=True)
    value = fields.CharField(min_length=2, max_length=200, required=True)
    kind = fields.CharField(min_length=1, max_lenght=20, required=True)
    volume = fields.ReferenceField('VolumeDocument', required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    deleted_at = fields.DateTimeField(blank=True)
