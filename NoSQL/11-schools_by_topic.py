#!/usr/bin/env python3
"""define a function schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """ list all documents
        return to the list
    """
    return list(mongo_collection.find({"topics": topic}))
