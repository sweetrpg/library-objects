# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from sweetrpg_db.utils import to_datetime
from reprlib import recursive_repr


class Volume(object):
    """A model object representing an RPG volume (digital or print)."""

    def __init__(self, *args, **kwargs):
        """Creates a new Volume object. """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs.get("name")
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))
        self.system = kwargs.get("system")
        self.slug = kwargs.get("slug")
        self.isbn = kwargs.get("isbn")
        self.authors = kwargs.get("authors")
        self.publishers = kwargs.get("publishers")
        self.studios = kwargs.get("studios")
        self.reviews = kwargs.get("reviews")
        self.properties = kwargs.get("properties")

    @recursive_repr()
    def __repr__(self):
        attrs = []
        for k in dir(self):
            if k.startswith("__"):
                continue
            v = getattr(self, k)
            attrs.append("{k}={v}".format(k=k, v=v))
        return f'<Volume({", ".join(attrs)})>'

    def to_dict(self):
        d = {}
        for k in dir(self):
            if k.startswith("__"):
                continue
            d[k] = getattr(self, k)
        return d


class VolumeProperty(object):
    """A model object representing a property key/value pair for a Volume."""

    def __init__(self, *args, **kwargs):
        """ """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs.get("name")
        self.type = kwargs.get("type")
        self.value = kwargs.get("value")
        self.volume = kwargs.get("volume")
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))

    @recursive_repr()
    def __repr__(self):
        attrs = []
        for k in dir(self):
            if k.startswith("__"):
                continue
            v = getattr(self, k)
            attrs.append("{k}={v}".format(k=k, v=v))
        return f'<VolumeProperty({", ".join(attrs)})>'

    def to_dict(self):
        d = {}
        for k in dir(self):
            if k.startswith("__"):
                continue
            d[k] = getattr(self, k)
        return d
