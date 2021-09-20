# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from sweetrpg_db.utils import to_datetime


class Tag(object):
    """A model object representing a tag value attached to an object."""

    __tablename__ = "tags"

    def __init__(self, *args, **kwargs):
        """Creates a new Tag object.

        :key str name: The name of the tag.
        """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs.get("name")
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))

    def __repr__(self):
        attrs = []
        for k in dir(self):
            if k.startswith("__"):
                continue
            v = getattr(self, k)
            attrs.append("{k}={v}".format(k=k, v=v))
        return f'<Tag({", ".join(attrs)})'
