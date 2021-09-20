# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.studio import Studio
from sweetrpg_library_model.db.studio.schema import StudioDBSchema
import json
from datetime import datetime


# studio_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "Joe Bob",
#     "created_at": "2021-09-13T07:55:00.001",
#     "updated_at": "2021-09-13T07:55:00.001"
# }
# """
# studio_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
# studio_dict = {
#     "_id": "another-id",
#     "name": "Billy",
#     "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
#     "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
# }


# def test_studio_repr():
#     a = Studio(name="This guy")
#     assert isinstance(a, Studio)
#     s = f"{a!r}"
#     assert "name=This guy" in s


# def test_load_studio_from_json():
#     j = json.loads(studio_json)
#     schema = StudioDBSchema()
#     a = schema.load(j)
#     assert a is not None
#     assert isinstance(a, Studio)
#     assert a.name == "Joe Bob"
#     assert a.id == "this-is-ignored"
#     assert a.created_at == studio_datetime


# def test_load_studio_from_dict():
#     schema = StudioDBSchema()
#     a = schema.load(studio_dict)
#     assert a is not None
#     assert isinstance(a, Studio)
#     assert a.name == "Billy"
#     assert a.id == "another-id"
#     assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
#     assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
