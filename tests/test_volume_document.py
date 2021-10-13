# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.db.volume.document import VolumeDocument
from sweetrpg_library_model.db.tag.document import TagDocument
from sweetrpg_library_model.db.publisher.document import PublisherDocument
from sweetrpg_library_model.db.volume_property.document import VolumePropertyDocument


def test_volume_document_setup():
    t = TagDocument(name="tag", value="value")
    p = PublisherDocument(name="Pub Lisher")
    pr = VolumePropertyDocument(name="value", value="1", kind="int")
    v = VolumeDocument(
        name="Bob's Book",
        slug="bob",
        system="bob",
        tags=[t],
        publisher=p,
        properties=[pr],
    )
    assert v is not None
    assert v.name == "Bob's Book"
    assert v.slug == "bob"
    assert v.system == "bob"
    assert v.publisher.name == "Pub Lisher"
    assert len(v.properties) == 1
    pr = v.properties[0]
    assert pr.name == "value"
    assert pr.value == "1"
    assert pr.kind == "int"
    assert len(v.tags) == 1
    t = v.tags[0]
    assert t.name == "tag"
    assert t.value == "value"
