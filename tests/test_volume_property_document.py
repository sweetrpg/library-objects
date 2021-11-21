# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_objects.db.volume_property.document import VolumePropertyDocument


def test_volume_property_document_setup():
    vp = VolumePropertyDocument(name="value", value="1", kind="int")
    assert vp is not None
    assert vp.name == "value"
    assert vp.value == "1"
    assert vp.kind == "int"
