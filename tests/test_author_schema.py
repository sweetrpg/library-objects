# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.author import Author
from sweetrpg_library_model.db.author.schema import AuthorDBSchema
import json
from datetime import datetime


author_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-13T07:55:00.001",
    "updated_at": "2021-09-13T07:55:00.001",
    "volumes": ["v1"]
}
"""
author_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_load_author():
    j = json.loads(author_json)
    schema = AuthorDBSchema()
    a = schema.load(j)
    assert a is not None
    assert isinstance(a, Author)
    assert a.name == "Joe Bob"
    assert a.id == "this-is-ignored"
    assert a.created_at == author_datetime
    assert len(a.volumes) == 1
    v = a.volumes[0]
    assert v is not None
    assert isinstance(v, str)
    assert v == "v1"
