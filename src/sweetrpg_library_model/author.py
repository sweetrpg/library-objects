# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from datetime import datetime


class Author(object):
      """
      """
      __tablename__ = 'authors'

      def __init__(self, *args, **kwargs):
            """
            Creates a new Author object.
            :param str name: The name of the author.
            """
            print(f"args: {args}, kwargs: {kwargs}")
            now = datetime.utcnow().isoformat()
            self.id = kwargs.get('_id') or kwargs.get('id')
            self.name = name
            self.created_at = kwargs.get('created_at', now)
            self.updated_at = kwargs.get('updated_at', now)
            self.deleted_at = kwargs.get('deleted_at')
            self.volumes = kwargs.get('volumes', [])
            self.studios = kwargs.get('studios', [])

      def __repr__(self):
            return (f"<Author(id={self.id!r}, "
                    f"name={self.name!s}, "
                    f"volumes={self.volumes!r}, "
                    f"studios={self.studios!r}, "
                    f"created_at={self.created_at!r}, updated_at={self.updated_at!r}, deleted_at={self.deleted_at!r})>"
                   )
