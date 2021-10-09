# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import logging
from sweetrpg_model_core.model.base import BaseModel


class Volume(BaseModel):
    """A model object representing an RPG volume (digital or print)."""

    def __init__(self, *args, **kwargs):
        """Creates a new Volume object."""
        logging.debug("args: %s, kwargs: %s", args, kwargs)

        super().__init__(*args, **kwargs)

        self.name = kwargs.get("name")
        self.system = kwargs.get("system")
        self.slug = kwargs.get("slug")
        self.authors = kwargs.get("authors")
        # self.publishers = kwargs.get("publishers")
        # self.studios = kwargs.get("studios")
        # self.reviews = kwargs.get("reviews")
        self.properties = kwargs.get("properties")
