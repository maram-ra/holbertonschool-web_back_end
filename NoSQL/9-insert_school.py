#!/usr/bin/env python3
"""define a function insert_school"""


def insert_school(mongo_collection, **kwargs):
    """insert a new document in a collection MongoDB
    return to the function insert_school
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
