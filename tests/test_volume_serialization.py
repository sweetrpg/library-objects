# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.volume import Volume
import json
from datetime import datetime

volume_json = """
{
    "_id": "this-is-ignored",
    "name": "Player's Handbook",
    "slug": "phb",
    "system": "dnd5",
    "created_at": "2021-09-13T07:55:00.001"
}
"""
volume_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_volume_from_json():
    j = json.loads(volume_json)
    v = Volume(**j)
    assert isinstance(v, Volume)
    assert v.name == "Player's Handbook"
    assert v.slug == "phb"
    assert v.system == "dnd5"
    assert v.id == "this-is-ignored"
    assert v.created_at == volume_datetime
