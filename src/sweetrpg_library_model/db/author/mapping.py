# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from mongokit_ng import Document, INDEX_ASCENDING


class Author(Document):
    """A model object representing RPG authors."""

    __collection__ = "authors"
    structure = {
        'name': str,
        'created_at': datetime,
        'updated_at': datetime,
        'deleted_at': datetime,
    }
    required_fields = ['name', 'created_at', 'updated_at']
    default_values = {
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
    }
    indexes = [
        {
            'fields':[('name', INDEX_ASCENDING)],
            'name':'author_name'
        },
    ]
    use_dot_notation = True
