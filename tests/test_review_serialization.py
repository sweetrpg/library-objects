# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.review import Review
from sweetrpg_library_model.model.volume import Volume
import json
from datetime import datetime

# review_json = """
# {
#     "_id": "this-is-ignored",
#     "title": "This sucks",
#     "text": "I hate it",
#     "created_at": "2021-09-13T07:55:00.001"
# }
# """
# volume_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "Player's Handbook",
#     "slug": "phb",
#     "system": "dnd5",
#     "created_at": "2021-09-13T07:55:00.001"
# }
# """
# review_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


# def test_review_from_json():
#     j = json.loads(review_json)
#     v = json.loads(volume_json)
#     j["volume"] = Volume(**v)
#     r = Review(**j)
#     assert isinstance(r, Review)
#     assert r.title == "This sucks"
#     assert r.text == "I hate it"
#     assert r.id == "this-is-ignored"
#     assert r.created_at == review_datetime
