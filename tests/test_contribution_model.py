# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_objects.model.person import Person
import json
from datetime import datetime

person_json = """
{
    "_id": "this-is-ignored",
    "name": "Joe Bob",
    "created_at": "2021-09-13T07:55:00.001",
    "created_by": "test",
    "updated_at": "2021-09-13T07:55:00.001",
    "updated_by": "test",
    "tags": [
        {"name": "tag", "value": "tag"}
    ],
    "properties": [
        {"name": "property", "kind": "property", "value": "property"}
    ]
}
"""
person_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_person_from_json():
    j = json.loads(person_json)
    a = Person(**j)
    assert isinstance(a, Person)
    assert a.name == "Joe Bob"
    assert a.id == "this-is-ignored"
    assert a.created_at == person_datetime
    assert a.created_by == "test"
    assert a.updated_at == person_datetime
    assert a.updated_by == "test"
    assert not hasattr(a, "deleted_at") or a.deleted_at is None
    assert not hasattr(a, "deleted_by") or a.deleted_by is None
    assert len(a.tags) == 1
    t = a.tags[0]
    assert t["name"] == "tag"
    assert t["value"] == "tag"
    assert len(a.properties) == 1
    p = a.properties[0]
    assert p["name"] == "property"
    assert p["kind"] == "property"
    assert p["value"] == "property"
