# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.author import Author
from sweetrpg_library_model.db.author.schema import AuthorDBSchema
import json
from datetime import datetime


# author_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "Joe Bob",
#     "created_at": "2021-09-13T07:55:00.001",
#     "updated_at": "2021-09-13T07:55:00.001",
#     "volumes": ["v1"]
# }
# """
# author_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
# author_dict = {
#     "_id": "another-id",
#     "name": "Billy",
#     "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
#     "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
#     "volumes": ["v2"],
# }


# # def test_author_repr():
# #     a = Author(name="This guy")
# #     assert isinstance(a, Author)
# #     s = f"{a!r}"
# #     assert "name=This guy" in s


# def test_load_author_from_json():
#     j = json.loads(author_json)
#     schema = AuthorDBSchema()
#     a = schema.load(j)
#     assert a is not None
#     assert isinstance(a, Author)
#     assert a.name == "Joe Bob"
#     assert a.id == "this-is-ignored"
#     assert a.created_at == author_datetime
#     assert len(a.volumes) == 1
#     v = a.volumes[0]
#     assert v is not None
#     assert isinstance(v, str)
#     assert v == "v1"


# def test_load_author_from_dict():
#     schema = AuthorDBSchema()
#     a = schema.load(author_dict)
#     assert a is not None
#     assert isinstance(a, Author)
#     assert a.name == "Billy"
#     assert a.id == "another-id"
#     assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
#     assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
#     assert len(a.volumes) == 1
#     v = a.volumes[0]
#     assert v is not None
#     assert isinstance(v, str)
#     assert v == "v2"
