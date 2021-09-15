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
    "created_at": "2021-09-13T07:55:00.001"
}
"""
tag_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_tag_from_json():
    j = json.loads(tag_json)
    a = Tag(**j)
    assert isinstance(a, Tag)
    assert a.name == "it"
    assert a.id == "this-is-ignored"
    assert a.created_at == tag_datetime
