# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base
from marshmallow import Schema, fields

# Base = declarative_base()

class Volume(object):
      __tablename__ = 'volumes'

      def __init__(self, name, *args, **kwargs):
            print(name)
            print(args)
            print(kwargs)
            self.id = kwargs.get('_id')
            self.name = name

      def __repr__(self):
            return f"<Volume(id={self.id!r}, name={self.name!r})>"
