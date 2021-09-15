# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from sweetrpg_common.utils import to_datetime


class Review(object):
    """A model object representing a review for a Volume."""

    __tablename__ = "reviews"

    def __init__(self, *args, **kwargs):
        """
        Creates a new Review object.
        :param str title: The title of the review.
        :param str text: The text of the review.
        """
        logging.debug("args: %s, kwargs: %s", args, kwargs)
        now = datetime.utcnow()  # .isoformat()
        self.id = kwargs.get("_id") or kwargs.get("id")
        self.name = kwargs["title"]
        self.name = kwargs["text"]
        self.created_at = to_datetime(kwargs.get("created_at")) or now
        self.updated_at = to_datetime(kwargs.get("updated_at")) or now
        self.deleted_at = to_datetime(kwargs.get("deleted_at"))
        self.volume = kwargs["volume"]

    def __repr__(self):
        attrs = []
        for k, v in dir(self):
            attrs.append(f"{k}({type(v)})={v}")
        return f'<Review({", ".join(attrs)})'
