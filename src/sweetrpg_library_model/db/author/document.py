# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from mongoengine import Document, fields
from pymongo.operations import IndexModel
from pymongo import ASCENDING


class AuthorDocument(Document):
    """A model object representing an RPG author."""

    meta = {
        'indexes' : [
            {"name": "author_name", "fields": ["name"]}
        ],
        'db_alias' : "default",
        'collection': "authors",
        'strict': False,
    }

    name = fields.StringField(min_length=1, max_length=200, required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    deleted_at = fields.DateTimeField(null=True)
    volumes = fields.ListField(field=fields.ReferenceField('VolumeDocument'))
