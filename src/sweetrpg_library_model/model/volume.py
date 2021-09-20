# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
# from sweetrpg_db.utils import to_datetime
from mongokit_ng import Document, INDEX_ASCENDING


class Volume(Document):
    """A model object representing an RPG volume (digital or print)."""

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

    # __tablename__ = "volumes"

    # def __init__(self, *args, **kwargs):
    #     """Creates a new Volume object. """
    #     logging.debug("args: %s, kwargs: %s", args, kwargs)
    #     now = datetime.utcnow()  # .isoformat()
    #     self.id = kwargs.get("_id") or kwargs.get("id")
    #     self.name = kwargs.get("name")
    #     self.created_at = to_datetime(kwargs.get("created_at")) or now
    #     self.updated_at = to_datetime(kwargs.get("updated_at")) or now
    #     self.deleted_at = to_datetime(kwargs.get("deleted_at"))
    #     self.system = kwargs.get("system")
    #     self.slug = kwargs.get("slug")
    #     self.isbn = kwargs.get("isbn")
    #     self.authors = kwargs.get("authors")
    #     self.publishers = kwargs.get("publishers")
    #     self.studios = kwargs.get("studios")
    #     self.reviews = kwargs.get("reviews")
    #     self.properties = kwargs.get("properties")

    # def __repr__(self):
    #     attrs = []
    #     for k in dir(self):
    #         if k.startswith("__"):
    #             continue
    #         v = getattr(self, k)
    #         attrs.append("{k}={v}".format(k=k, v=v))
    #     return f'<Volume({", ".join(attrs)})'


# class VolumeProperty(object):
#     """A model object representing a property key/value pair for a Volume."""

#     __tablename__ = "volume_properties"

#     def __init__(self, *args, **kwargs):
#         """ """
#         logging.debug("args: %s, kwargs: %s", args, kwargs)
#         now = datetime.utcnow()  # .isoformat()
#         self.id = kwargs.get("_id") or kwargs.get("id")
#         self.name = kwargs.get("name")
#         self.type = kwargs.get("type")
#         self.value = kwargs.get("value")
#         self.volume = kwargs.get("volume")
#         self.created_at = to_datetime(kwargs.get("created_at")) or now
#         self.updated_at = to_datetime(kwargs.get("updated_at")) or now
#         self.deleted_at = to_datetime(kwargs.get("deleted_at"))

#     def __repr__(self):
#         attrs = []
#         for k in dir(self):
#             if k.startswith("__"):
#                 continue
#             v = getattr(self, k)
#             attrs.append("{k}={v}".format(k=k, v=v))
#         return f'<VolumeProperty({", ".join(attrs)})'
