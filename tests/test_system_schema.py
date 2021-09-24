# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.system import System
from sweetrpg_library_model.db.system.schema import SystemSchema
import json
from datetime import datetime


system_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-13T07:55:00.001",
    "updated_at": "2021-09-13T07:55:00.001"
}
"""
system_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
system_dict = {
    "_id": "another-id",
    "name": "Billy",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
}


# def test_system_repr():
#     a = System(name="This guy")
#     assert isinstance(a, System)
#     s = f"{a!r}"
#     assert "name=This guy" in s


def test_load_system_from_json():
    j = json.loads(system_json)
    schema = SystemSchema()
    a = schema.load(j)
    assert a is not None
    assert isinstance(a, System)
    assert a.name == "Joe Bob"
    assert a.id == "this-is-ignored"
    assert a.created_at == system_datetime


def test_load_system_from_dict():
    schema = SystemSchema()
    a = schema.load(system_dict)
    assert a is not None
    assert isinstance(a, System)
    assert a.name == "Billy"
    assert a.id == "another-id"
    assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
