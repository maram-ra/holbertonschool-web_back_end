#!/usr/bin/env python3
"""define a function list_all"""


def list_all(mongo_collection):
    """list all documents in a collection
    return to mongo_collection
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
