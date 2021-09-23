# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.db.volume.mapping import VolumeDocument, VolumePropertyDocument


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
    assert v.properties[0].name == "value"
    assert v.properties[0].value == "1"
    assert v.properties[0].kind == "int"
