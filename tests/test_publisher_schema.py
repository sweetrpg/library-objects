# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.publisher import Publisher
from sweetrpg_library_model.db.publisher.schema import PublisherDBSchema
import json
from datetime import datetime


# publisher_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "Joe Bob",
#     "created_at": "2021-09-15T21:51:00.001",
#     "updated_at": "2021-09-15T21:51:00.001"
# }
# """
# publisher_datetime = datetime(2021, 9, 15, 21, 51, 0, 1000)
# publisher_dict = {
#     "_id": "another-id",
#     "name": "Billy",
#     "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
#     "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
# }


# def test_publisher_repr():
#     a = Publisher(name="This guy")
#     assert isinstance(a, Publisher)
#     s = f"{a!r}"
#     assert "name=This guy" in s


# def test_load_publisher_from_json():
#     j = json.loads(publisher_json)
#     schema = PublisherDBSchema()
#     a = schema.load(j)
#     assert a is not None
#     assert isinstance(a, Publisher)
#     assert a.name == "Joe Bob"
#     assert a.id == "this-is-ignored"
#     assert a.created_at == publisher_datetime


# def test_load_publisher_from_dict():
#     schema = PublisherDBSchema()
#     a = schema.load(publisher_dict)
#     assert a is not None
#     assert isinstance(a, Publisher)
#     assert a.name == "Billy"
#     assert a.id == "another-id"
#     assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
#     assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
