# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from sweetrpg_db.utils import to_datetime
from reprlib import recursive_repr


class VolumeProperty(object):
    """A model object representing a property key/value pair for a Volume."""

    def __init__(self, *args, **kwargs):
        """ """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs.get("name")
        self.kind = kwargs.get("kind")
        self.value = kwargs.get("value")
        self.volume = kwargs.get("volume")
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))

    @recursive_repr()
    def __repr__(self):
        attrs = []
        for k, v in self.__dict__.items():
            if k.startswith("__"):
                continue
            # v = getattr(self, k)
            attrs.append("{k}={v}".format(k=k, v=v))
        return f'<VolumeProperty({", ".join(attrs)})>'

    def to_dict(self):
        d = {}
        for k in dir(self):
            logging.debug("k: %s, type: %s", k, type(k))
            if k.startswith("__") or k.startswith("to_"):
                continue
            d[k] = getattr(self, k)
        return d
