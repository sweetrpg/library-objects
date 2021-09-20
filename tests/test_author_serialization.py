# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.author import Author
import json
from datetime import datetime

# author_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "Joe Bob",
#     "created_at": "2021-09-13T07:55:00.001"
# }
# """
# author_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


# def test_author_from_json():
#     j = json.loads(author_json)
#     a = Author(**j)
#     assert isinstance(a, Author)
#     assert a.name == "Joe Bob"
#     assert a.id == "this-is-ignored"
#     assert a.created_at == author_datetime
