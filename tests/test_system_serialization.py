# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.system import System
import json
from datetime import datetime

system_json = """
{
    "_id": "this-is-ignored",
    "name": "dnd5",
    "created_at": "2021-09-13T07:55:00.001"
}
"""
system_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_system_from_json():
    j = json.loads(system_json)
    a = System(**j)
    assert isinstance(a, System)
    assert a.name == "dnd5"
    assert a.id == "this-is-ignored"
    assert a.created_at == system_datetime
