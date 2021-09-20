# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.publisher import Publisher
import json
from datetime import datetime

# publisher_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "Free League",
#     "created_at": "2021-09-14T20:05:00.001"
# }
# """
# publisher_datetime = datetime(2021, 9, 14, 20, 5, 0, 1000)


# def test_publisher_from_json():
#     j = json.loads(publisher_json)
#     p = Publisher(**j)
#     assert isinstance(p, Publisher)
#     assert p.name == "Free League"
#     assert p.id == "this-is-ignored"
#     assert p.created_at == publisher_datetime
