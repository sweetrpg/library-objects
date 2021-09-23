# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.db.author.document import AuthorDocument


def test_author_document_setup():
    a = AuthorDocument(name="Bob",
                       volumes=[])
    assert a is not None
    assert a.name == "Bob"
    assert len(a.volumes) == 0
