# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from datetime import datetime


class Author(object):
      """
      """
      __tablename__ = 'authors'

      def __init__(self, name, *args, **kwargs):
            """
            Creates a new Author object.
            :param str name: The name of the author.
            """
            now = datetime.utcnow().isoformat()
            self.id = kwargs.get('_id') or kwargs.get('id')
            self.name = name
            self.created_at = kwargs.get('created_at', now)
            self.updated_at = kwargs.get('updated_at', now)
            self.deleted_at = kwargs.get('deleted_at')

      def __repr__(self):
            return f"<Author(id={self.id!r}, name={self.name!r}, created_at={self.created_at}, updated_at={self.updated_at}, deleted_at={self.deleted_at})>"
