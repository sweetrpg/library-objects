# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.tag import Tag
from sweetrpg_library_model.db.tag.schema import TagSchema
import json
from datetime import datetime


tag_with_value_json = """
{
    "_id": "this-is-ignored",
    "name": "tag",
    "value": "tag",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test"
}
"""
tag_without_value_json = """
{
    "_id": "this-is-ignored",
    "name": "tag",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test"
}
"""
tag_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
tag_with_value_dict = {
    "_id": "another-id",
    "name": "tag",
    "value": "tag",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2002),
    "deleted_by": "test",
}
tag_without_value_dict = {
    "_id": "another-id",
    "name": "tag",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "created_by": "test",
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "updated_by": "test",
    "deleted_at": datetime(2021, 9, 15, 7, 35, 0, 2002),
    "deleted_by": "test",
}


def test_load_tag_with_value_from_json():
    j = json.loads(tag_with_value_json)
    schema = TagSchema()
    t = schema.load(j)
    assert t is not None
    assert isinstance(t, Tag)
    assert t.id == "this-is-ignored"
    assert t.name == "tag"
    assert t.value == "tag"
    assert t.created_at == tag_datetime
    assert t.created_by == "test"
    assert t.updated_at == tag_datetime
    assert t.updated_by == "test"
    assert t.deleted_at is None
    assert t.deleted_by is None

def test_load_tag_without_value_from_json():
    j = json.loads(tag_without_value_json)
    schema = TagSchema()
    t = schema.load(j)
    assert t is not None
    assert isinstance(t, Tag)
    assert t.id == "this-is-ignored"
    assert t.name == "tag"
    assert t.value is None
    assert t.created_at == tag_datetime
    assert t.created_by == "test"
    assert t.updated_at == tag_datetime
    assert t.updated_by == "test"
    assert t.deleted_at is None
    assert t.deleted_by is None


def test_load_tag_with_value_from_dict():
    schema = TagSchema()
    t = schema.load(tag_with_value_dict)
    assert t is not None
    assert isinstance(t, Tag)
    assert t.id == "another-id"
    assert t.name == "tag"
    assert t.value == "tag"
    assert t.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert t.created_by == "test"
    assert t.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert t.updated_by == "test"
    assert t.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2002)
    assert t.deleted_by == "test"

def test_load_tag_without_value_from_dict():
    schema = TagSchema()
    t = schema.load(tag_without_value_dict)
    assert t is not None
    assert isinstance(t, Tag)
    assert t.id == "another-id"
    assert t.name == "tag"
    assert t.value is None
    assert t.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert t.created_by == "test"
    assert t.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert t.updated_by == "test"
    assert t.deleted_at == datetime(2021, 9, 15, 7, 35, 0, 2002)
    assert t.deleted_by == "test"
