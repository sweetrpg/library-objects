# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.tag import Tag
import json
from datetime import datetime

tag_json = """
{
    "_id": "this-is-ignored",
    "name": "it",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test"
}
"""
tag_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_tag_from_json():
    j = json.loads(tag_json)
    t = Tag(**j)
    assert isinstance(t, Tag)
    assert t.id == "this-is-ignored"
    assert t.name == "it"
    assert t.created_at == tag_datetime
    assert t.created_by == "test"
    assert t.updated_at == tag_datetime
    assert t.updated_by == "test"
    assert not hasattr(t, "deleted_at") or t.deleted_at is None
    assert not hasattr(t, "deleted_by") or t.deleted_by is None
