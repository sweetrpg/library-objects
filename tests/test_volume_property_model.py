# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.volume_property import VolumeProperty
import json
from datetime import datetime

volume_property_json = """
{
    "name": "ISBN",
    "kind": "isbn",
    "value": "12345"
}
"""
volume_property_bad_json = """
{
    "name": "ISBN",
    "type": "isbn",
    "value": "12345"
}
"""


def test_volume_property_from_json():
    j = json.loads(volume_property_json)
    v = VolumeProperty(**j)
    assert isinstance(v, VolumeProperty)
    assert v.name == "ISBN"
    assert v.kind == "isbn"
    assert v.value == "12345"


def test_volume_property_from_bad_json():
    j = json.loads(volume_property_bad_json)
    v = VolumeProperty(**j)
    assert isinstance(v, VolumeProperty)
    assert v.name == "ISBN"
    assert v.kind is None
    assert hasattr(v, "type") == False
    assert v.value == "12345"
