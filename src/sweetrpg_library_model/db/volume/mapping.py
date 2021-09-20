# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
from mongokit_ng import Document, INDEX_ASCENDING


class VolumeMapping(Document):
    """A mapping object to convert MongoDB data to a Volume object."""

    __collection__ = "volumes"
    structure = {
        'name': str,
        'slug': str,
        'system': str,
        'created_at': datetime,
        'updated_at': datetime,
        'deleted_at': datetime,
    }
    required_fields = ['name', 'slug', 'system', 'created_at', 'updated_at']
    default_values = {
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
    }
    indexes = [
        {
            'fields':[('slug', INDEX_ASCENDING)],
            'name':'volume_slug',
            'unique':True
        },
        {'fields':[('name', INDEX_ASCENDING)], 'name':'volume_name'},
        {'fields':[('system', INDEX_ASCENDING)], 'name':'volume_system'},
    ]
    use_dot_notation = True
