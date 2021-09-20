# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.studio import Studio
import json
from datetime import datetime

# studio_json = """
# {
#     "_id": "this-is-ignored",
#     "name": "One Room",
#     "created_at": "2021-09-13T07:55:00.001"
# }
# """
# studio_datetime = datetime(2021, 9, 13, 7, 55, 0, 1000)


# def test_studio_from_json():
#     j = json.loads(studio_json)
#     s = Studio(**j)
#     assert isinstance(s, Studio)
#     assert s.name == "One Room"
#     assert s.id == "this-is-ignored"
#     assert s.created_at == studio_datetime
