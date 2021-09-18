# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from sweetrpg_common.utils import to_datetime


class Volume(object):
    """A model object representing an RPG volume (digital or print)."""

    __tablename__ = "volumes"

    def __init__(self, *args, **kwargs):
        """Creates a new Volume object. """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs["name"]
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))
        self.system = kwargs["system"]
        self.slug = kwargs["slug"]
        self.isbn = kwargs.get("isbn")
        self.authors = kwargs.get("authors", [])
        self.publishers = kwargs.get("publishers", [])
        self.studios = kwargs.get("studios", [])
        self.reviews = kwargs.get("reviews", [])
        self.properties = kwargs.get("properties", [])

    def __repr__(self):
        attrs = []
        for k, v in dir(self):
            attrs.append(f"{k}({type(v)})={v}")
        return f'<Volume({", ".join(attrs)})'


class VolumeProperty(object):
    """A model object representing a property key/value pair for a Volume."""

    __tablename__ = "volume_properties"

    def __init__(self, *args, **kwargs):
        """ """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs["name"]
        self.type = kwargs["type"]
        self.value = kwargs["value"]
        self.volume = kwargs["volume"]
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))

    def __repr__(self):
        attrs = []
        for k, v in dir(self):
            attrs.append(f"{k}({type(v)})={v}")
        return f'<VolumeProperty({", ".join(attrs)})'
