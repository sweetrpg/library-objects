# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.db.volume.document import VolumeDocument, VolumePropertyDocument


def test_volume_document_setup():
    v = VolumeDocument(name="Bob's Book",
                       slug="bob",
                       system="bob",
                       authors=[],
                       properties=[
                           VolumePropertyDocument(name="value",
                                                  value="1",
                                                  kind="int")
                       ])
    assert v is not None
    assert v.name == "Bob's Book"
    assert v.slug == "bob"
    assert v.system == "bob"
    assert len(v.authors) == 0
    assert len(v.properties) == 1

def test_volume_property_document_setup():
    vp = VolumePropertyDocument(name="value",
                                value="1",
                                kind="int")
    assert vp is not None
    assert vp.name == "value"
    assert vp.value == "1"
    assert vp.kind == "int"
