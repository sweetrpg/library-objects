# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.review import Review
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_library_model.db.review.schema import ReviewSchema
import json
from datetime import datetime


review_json = """
{
    "_id": "this-is-ignored",
    "title": "This sucks",
    "text": "I hate it",
    "created_at": "2021-09-13T07:55:00.001",
    "updated_at": "2021-09-13T07:55:00.001"
}
"""
review_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)
review_dict = {
    "_id": "another-id",
    "title": "This is great",
    "text": "I love it",
    "created_at": datetime(2021, 9, 15, 7, 35, 0, 2000),
    "updated_at": datetime(2021, 9, 15, 7, 35, 0, 2001),
    "volume": "4",  # Volume(id="4", name="War and Peace", slug="leo", system="peanuts")
}


# def test_review_repr():
#     v = Volume(id="12345", name="Not your best work", slug="yuck", system="boo")
#     a = Review(title="This is fine", text="Just okay is not okay", volume=v)
#     assert isinstance(a, Review)
#     s = f"{a!r}"
#     assert "title=This is fine" in s
#     assert "text=Just okay is not okay" in s
#     assert "volume=" in s


def test_load_review_from_json():
    j = json.loads(review_json)
    j["volume"] = "99"  # Volume(id="99", name="Gretsky", slug="wayne", system="la-kings")
    schema = ReviewSchema()
    a = schema.load(j)
    assert a is not None
    assert isinstance(a, Review)
    assert a.title == "This sucks"
    assert a.text == "I hate it"
    assert a.id == "this-is-ignored"
    assert a.created_at == review_datetime
    assert a.volume == "99"


def test_load_review_from_dict():
    schema = ReviewSchema()
    a = schema.load(review_dict)
    assert a is not None
    assert isinstance(a, Review)
    assert a.title == "This is great"
    assert a.text == "I love it"
    assert a.id == "another-id"
    assert a.created_at == datetime(2021, 9, 15, 7, 35, 0, 2000)
    assert a.updated_at == datetime(2021, 9, 15, 7, 35, 0, 2001)
    assert a.volume == "4"
