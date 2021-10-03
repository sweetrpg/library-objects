# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import logging
from sweetrpg_model_core.model.base import BaseModel


class Review(BaseModel):
    """A model object representing a review for a Volume."""

    def __init__(self, *args, **kwargs):
        """Creates a new Review object.

        :key str title: The title of the review.
        :key str text: The text of the review.
        """
        logging.debug("args: %s, kwargs: %s", args, kwargs)

        super().__init__(args, kwargs)

        self.title = kwargs.get("title")
        self.text = kwargs.get("text")
        self.volume = kwargs.get("volume")
