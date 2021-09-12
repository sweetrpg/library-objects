# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from datetime import datetime


class Volume(object):
      """
      """
      __tablename__ = 'volumes'

      def __init__(self, *args, **kwargs):
            """
            """
            now = datetime.utcnow().isoformat()
            self.id = kwargs.get('_id') or kwargs.get('id')
            self.name = kwargs['name']
            self.created_at = kwargs.get('created_at', now)
            self.updated_at = kwargs.get('updated_at', now)
            self.deleted_at = kwargs.get('deleted_at')
            self.system = kwargs['system']
            self.slug = kwargs['slug']
            self.isbn = kwargs.get('isbn')
            self.authors = kwargs.get('authors', [])
            self.publishers = kwargs.get('publishers', [])
            self.studios = kwargs.get('studios', [])
            self.reviews = kwargs.get('reviews', [])

      def __repr__(self):
            return f"""<Volume(id={self.id!r},
                        name={self.name!s}, slug={self.slug!s},
                        system={self.system!s}, isbn={self.isbn!s},
                        authors={self.authors!r},
                        publishers={self.publishers!r},
                        studios={self.studios!r},
                        reviews={self.reviews!r},
                        created_at={self.created_at!r}, updated_at={self.updated_at!r}, deleted_at={self.deleted_at!r})>
                        """
