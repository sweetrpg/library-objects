# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.review import Review
import json
from datetime import datetime

review_json = """
{
    "_id": "this-is-ignored",
    "title": "This sucks",
    "text": "I hate it",
    "created_at": "2021-09-13T07:55:00.001"
}
"""
review_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


def test_review_from_json():
    j = json.loads(review_json)
    a = Review(**j)
    assert isinstance(a, Review)
    assert a.title == "This sucks"
    assert a.text == "I hate it"
    assert a.id == "this-is-ignored"
    assert a.created_at == review_datetime
