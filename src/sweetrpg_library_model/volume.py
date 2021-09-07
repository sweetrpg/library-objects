# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from datetime import datetime


class Volume(object):
      """
      """
      __tablename__ = 'volumes'

      def __init__(self, name, slug, system, *args, **kwargs):
            """
            """
            now = datetime.utcnow().isoformat()
            self.id = kwargs.get('_id') or kwargs.get('id')
            self.name = name
            self.created_at = kwargs.get('created_at', now)
            self.updated_at = kwargs.get('updated_at', now)
            self.deleted_at = kwargs.get('deleted_at')
            self.system = system
            self.slug = slug
            self.isbn = kwargs.get('isbn')

      def __repr__(self):
            return f"<Volume(id={self.id!r}, name={self.name!r}, slug={self.slug}, system={self.system}, isbn={self.isbn}, created_at={self.created_at}, updated_at={self.updated_at}, deleted_at={self.deleted_at})>"
